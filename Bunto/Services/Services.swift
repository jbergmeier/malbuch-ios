import SwiftUI
import UIKit
import Photos

// MARK: - Fortschritt (lokal auf dem Gerät, kein Konto, kein Netzwerk)

@MainActor
final class ProgressStore: ObservableObject {
    static let shared = ProgressStore()

    @Published private(set) var colorings: [String: Coloring] = [:]
    private let directory: URL

    private init() {
        let base = FileManager.default.urls(for: .applicationSupportDirectory, in: .userDomainMask)[0]
        directory = base.appendingPathComponent("Bunto", isDirectory: true)
        try? FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        load()
    }

    func coloring(for id: String) -> Coloring? { colorings[id] }

    func save(_ coloring: Coloring, for id: String) {
        let file = directory.appendingPathComponent("\(id).json")
        if coloring.isEmpty {
            colorings[id] = nil
            try? FileManager.default.removeItem(at: file)
            return
        }
        var c = coloring
        c.rev = (colorings[id]?.rev ?? 0) + 1
        colorings[id] = c
        if let data = try? JSONEncoder().encode(c) {
            try? data.write(to: file, options: .atomic)
        }
    }

    private func load() {
        let files = (try? FileManager.default.contentsOfDirectory(at: directory, includingPropertiesForKeys: nil)) ?? []
        for url in files where url.pathExtension == "json" {
            if let data = try? Data(contentsOf: url),
               let c = try? JSONDecoder().decode(Coloring.self, from: data) {
                colorings[url.deletingPathExtension().lastPathComponent] = c
            }
        }
    }
}

// MARK: - Zeichnen (gemeinsam für Bildschirm, Vorschau und Foto-Export)

enum CanvasRenderer {
    static let ink = UIColor(hex: 0x2B2D42)

    static func draw(motif: Motif, coloring: Coloring, current: BrushStroke?,
                     in cg: CGContext, size: CGFloat, outline: CGFloat = 1.5) {
        cg.saveGState()
        cg.setFillColor(UIColor.white.cgColor)
        cg.fill(CGRect(x: 0, y: 0, width: size, height: size))
        cg.scaleBy(x: size / 100, y: size / 100)
        cg.setLineJoin(.round)
        cg.setLineCap(.round)

        var all = coloring.strokes
        if let c = current { all.append(c) }
        let byRegion = Dictionary(grouping: all, by: { $0.region })

        for (i, path) in motif.regions.enumerated() {
            let fillIndex = coloring.fills[i] ?? -1
            if Palette.isRainbow(fillIndex) {
                cg.saveGState()
                cg.addPath(path)
                cg.clip()
                let box = path.boundingBox
                let colors = (Palette.rainbowHexes + [Palette.rainbowHexes[0]]).map { UIColor(hex: $0).cgColor } as CFArray
                if let g = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(), colors: colors, locations: nil) {
                    cg.drawLinearGradient(g, start: CGPoint(x: box.minX, y: box.minY),
                                          end: CGPoint(x: box.maxX, y: box.maxY), options: [.drawsBeforeStartLocation, .drawsAfterEndLocation])
                }
                cg.restoreGState()
            } else {
                cg.addPath(path)
                cg.setFillColor(Palette.ui(fillIndex).cgColor)
                cg.fillPath()
            }

            if let list = byRegion[i] {
                cg.saveGState()
                cg.addPath(path)
                cg.clip()
                for s in list { draw(stroke: s, in: cg) }
                cg.restoreGState()
            }

            cg.addPath(path)
            cg.setStrokeColor(ink.cgColor)
            cg.setLineWidth(outline)
            cg.strokePath()
        }

        cg.setStrokeColor(ink.cgColor)
        cg.setLineWidth(outline)
        for l in motif.lines {
            cg.addPath(l)
            cg.strokePath()
        }
        cg.setFillColor(ink.cgColor)
        for d in motif.dots {
            cg.addPath(d)
            cg.fillPath()
        }
        cg.restoreGState()
    }

    private static func draw(stroke s: BrushStroke, in cg: CGContext) {
        guard let first = s.points.first else { return }
        if Palette.isRainbow(s.color) {
            // Regenbogen-Pinsel: Farbe wechselt entlang des Strichs
            cg.setLineWidth(s.width)
            var dist: CGFloat = 0
            var prev = first
            if s.points.count == 1 {
                cg.setFillColor(Palette.rainbow(at: 0).cgColor)
                let r = s.width / 2
                cg.fillEllipse(in: CGRect(x: first.x - r, y: first.y - r, width: s.width, height: s.width))
                return
            }
            for p in s.points.dropFirst() {
                dist += hypot(p.x - prev.x, p.y - prev.y)
                cg.setStrokeColor(Palette.rainbow(at: dist / 18).cgColor)
                cg.move(to: prev)
                cg.addLine(to: p)
                cg.strokePath()
                prev = p
            }
            return
        }
        let color = Palette.ui(s.color).cgColor
        if s.points.count == 1 {
            cg.setFillColor(color)
            let r = s.width / 2
            cg.fillEllipse(in: CGRect(x: first.x - r, y: first.y - r, width: s.width, height: s.width))
            return
        }
        cg.setStrokeColor(color)
        cg.setLineWidth(s.width)
        cg.move(to: first)
        for p in s.points.dropFirst() { cg.addLine(to: p) }
        cg.strokePath()
    }
}

enum Exporter {
    /// Hochauflösendes Bild (2048 x 2048) für die Fotos-App
    static func image(for motif: Motif, coloring: Coloring) -> UIImage {
        let side: CGFloat = 2048
        let fmt = UIGraphicsImageRendererFormat()
        fmt.scale = 1
        fmt.opaque = true
        let renderer = UIGraphicsImageRenderer(size: CGSize(width: side, height: side), format: fmt)
        return renderer.image { ctx in
            CanvasRenderer.draw(motif: motif, coloring: coloring, current: nil,
                                in: ctx.cgContext, size: side, outline: 1.2)
        }
    }
}

enum Thumbnails {
    private static let cache: NSCache<NSString, UIImage> = {
        let c = NSCache<NSString, UIImage>()
        c.countLimit = 300
        return c
    }()

    static func image(for motif: Motif, coloring: Coloring?, side: CGFloat, scale: CGFloat) -> UIImage {
        let key = "\(motif.id)-\(coloring?.rev ?? 0)-\(Int(side))-\(Int(scale))" as NSString
        if let hit = cache.object(forKey: key) { return hit }
        let fmt = UIGraphicsImageRendererFormat()
        fmt.scale = scale
        fmt.opaque = true
        let renderer = UIGraphicsImageRenderer(size: CGSize(width: side, height: side), format: fmt)
        let img = renderer.image { ctx in
            CanvasRenderer.draw(motif: motif, coloring: coloring ?? Coloring(), current: nil,
                                in: ctx.cgContext, size: side, outline: 2)
        }
        cache.setObject(img, forKey: key)
        return img
    }
}

// MARK: - Fotos speichern (nur Schreibzugriff, kein Lesen der Mediathek)

enum PhotoSaver {
    static func save(_ image: UIImage) async -> Bool {
        let status = await PHPhotoLibrary.requestAuthorization(for: .addOnly)
        guard status == .authorized || status == .limited else { return false }
        do {
            try await PHPhotoLibrary.shared().performChanges {
                PHAssetChangeRequest.creationRequestForAsset(from: image)
            }
            return true
        } catch {
            return false
        }
    }
}

// MARK: - Haptik

enum Haptics {
    @MainActor static func tap() {
        UIImpactFeedbackGenerator(style: .light).impactOccurred()
    }

    @MainActor static func success() {
        UINotificationFeedbackGenerator().notificationOccurred(.success)
    }
}
