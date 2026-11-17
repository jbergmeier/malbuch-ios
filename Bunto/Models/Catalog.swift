import SwiftUI
import UIKit

/// Aktuelle App-Sprache (nur Deutsch und Englisch sind lokalisiert).
enum Loc {
    static var isGerman: Bool {
        Bundle.main.preferredLocalizations.first?.hasPrefix("de") ?? false
    }
}

// MARK: - Laufzeit-Modelle

final class Motif: Identifiable, Hashable {
    let id: String
    let nameDE: String
    let nameEN: String
    /// Ausmalbare Flächen (hinten -> vorne), Koordinaten 0...100
    let regions: [CGPath]
    /// Dekorative Linien (nicht ausmalbar)
    let lines: [CGPath]
    /// Kleine ausgefüllte Punkte (Pupillen etc.)
    let dots: [CGPath]

    init(id: String, nameDE: String, nameEN: String, regions: [CGPath], lines: [CGPath], dots: [CGPath]) {
        self.id = id; self.nameDE = nameDE; self.nameEN = nameEN
        self.regions = regions; self.lines = lines; self.dots = dots
    }

    var name: String { Loc.isGerman ? nameDE : nameEN }

    static func == (a: Motif, b: Motif) -> Bool { a.id == b.id }
    func hash(into h: inout Hasher) { h.combine(id) }
}

final class MotifCategory: Identifiable, Hashable {
    let id: String
    let emoji: String
    let nameDE: String
    let nameEN: String
    let colorHex: UInt32
    let motifs: [Motif]

    init(id: String, emoji: String, nameDE: String, nameEN: String, colorHex: UInt32, motifs: [Motif]) {
        self.id = id; self.emoji = emoji; self.nameDE = nameDE; self.nameEN = nameEN
        self.colorHex = colorHex; self.motifs = motifs
    }

    var name: String { Loc.isGerman ? nameDE : nameEN }
    var tint: Color { Color(hex: colorHex) }

    static func == (a: MotifCategory, b: MotifCategory) -> Bool { a.id == b.id }
    func hash(into h: inout Hasher) { h.combine(id) }
}

// MARK: - Laden aus motifs.json

private struct CatalogDTO: Decodable {
    struct MotifDTO: Decodable {
        let id: String
        let de: String
        let en: String
        let regions: [String]
        let lines: [String]
        let dots: [String]
    }
    struct CategoryDTO: Decodable {
        let id: String
        let emoji: String
        let de: String
        let en: String
        let color: String
        let motifs: [MotifDTO]
    }
    let categories: [CategoryDTO]
}

final class Catalog {
    static let shared = Catalog()

    let categories: [MotifCategory]
    var allMotifs: [Motif] { categories.flatMap { $0.motifs } }

    private init() {
        guard let url = Bundle.main.url(forResource: "motifs", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let dto = try? JSONDecoder().decode(CatalogDTO.self, from: data) else {
            categories = []
            return
        }
        categories = dto.categories.map { c in
            let hex = UInt32(c.color.dropFirst(), radix: 16) ?? 0x6BCB77
            let motifs = c.motifs.map { m in
                Motif(id: m.id, nameDE: m.de, nameEN: m.en,
                      regions: m.regions.map(PathParser.parse),
                      lines: m.lines.map(PathParser.parse),
                      dots: m.dots.map(PathParser.parse))
            }
            return MotifCategory(id: c.id, emoji: c.emoji, nameDE: c.de, nameEN: c.en, colorHex: hex, motifs: motifs)
        }
    }

    func category(containing motif: Motif) -> MotifCategory? {
        categories.first { $0.motifs.contains(motif) }
    }
}

// MARK: - Mini-Parser für Pfade ("M x y L x y C x1 y1 x2 y2 x y Z")

enum PathParser {
    static func parse(_ d: String) -> CGPath {
        let path = CGMutablePath()
        let t = d.split(separator: " ")
        var i = 0

        func num() -> CGFloat {
            guard i < t.count else { return 0 }
            let v = Double(t[i]) ?? 0
            i += 1
            return CGFloat(v)
        }

        while i < t.count {
            let cmd = t[i]
            i += 1
            switch cmd {
            case "M":
                let x = num(), y = num()
                path.move(to: CGPoint(x: x, y: y))
            case "L":
                let x = num(), y = num()
                path.addLine(to: CGPoint(x: x, y: y))
            case "C":
                let x1 = num(), y1 = num(), x2 = num(), y2 = num(), x = num(), y = num()
                path.addCurve(to: CGPoint(x: x, y: y),
                              control1: CGPoint(x: x1, y: y1),
                              control2: CGPoint(x: x2, y: y2))
            case "Z":
                path.closeSubpath()
            default:
                break
            }
        }
        return path
    }
}
