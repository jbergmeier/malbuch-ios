import SwiftUI
import UIKit

struct BrushStroke: Codable {
    var region: Int
    /// Palettenindex, -1 = Weiß (Radierer)
    var color: Int
    /// Breite in Motiv-Einheiten (Motiv ist 100 x 100)
    var width: CGFloat
    var points: [CGPoint]
}

/// Der gespeicherte Mal-Zustand eines Motivs.
struct Coloring: Codable {
    var fills: [Int: Int] = [:]
    var strokes: [BrushStroke] = []
    /// Wird bei jedem Speichern erhöht (für Vorschaubild-Cache)
    var rev: Int = 0

    var isEmpty: Bool { fills.isEmpty && strokes.isEmpty }
}

enum Tool: CaseIterable {
    case fill, brush, eraser
}

enum BrushSize: CaseIterable {
    case small, medium, large

    var width: CGFloat {
        switch self {
        case .small: return 1.8
        case .medium: return 3.6
        case .large: return 7
        }
    }
}

/// Logik des Malens: Tippen = Füllen, Wischen = Pinsel (bleibt innerhalb der Fläche, in der man startet).
@MainActor
final class ColoringModel: ObservableObject {
    let motif: Motif

    @Published var tool: Tool = .fill
    @Published var colorIndex: Int = 0
    @Published var brushSize: BrushSize = .medium
    @Published private(set) var canUndo = false
    @Published private(set) var hasContent = false

    private(set) var coloring: Coloring
    private(set) var current: BrushStroke?
    /// Wird von der Zeichenfläche gesetzt
    var redraw: (() -> Void)?

    private var undoStack: [Coloring] = []
    private var pendingSnapshot: Coloring?
    private var startPoint: CGPoint = .zero
    private var startRegion: Int?
    private var travel: CGFloat = 0
    private var lastPoint: CGPoint = .zero

    init(motif: Motif) {
        self.motif = motif
        let stored = ProgressStore.shared.coloring(for: motif.id) ?? Coloring()
        self.coloring = stored
        self.hasContent = !stored.isEmpty
    }

    // MARK: Hit-Test

    func hit(_ p: CGPoint) -> Int? {
        var i = motif.regions.count - 1
        while i >= 0 {
            if motif.regions[i].contains(p) { return i }
            i -= 1
        }
        return nil
    }

    // MARK: Touch-Ereignisse (Koordinaten 0...100)

    func begin(at p: CGPoint) {
        startPoint = p
        lastPoint = p
        travel = 0
        startRegion = hit(p)
        current = nil
        guard tool != .fill, let r = startRegion else { return }
        pendingSnapshot = coloring
        current = BrushStroke(region: r,
                              color: tool == .eraser ? -1 : colorIndex,
                              width: tool == .eraser ? max(brushSize.width, 4) : brushSize.width,
                              points: [p])
        redraw?()
    }

    func move(to p: CGPoint) {
        let d = hypot(p.x - lastPoint.x, p.y - lastPoint.y)
        guard d > 0.25 else { return }
        travel += d
        lastPoint = p
        if current != nil {
            current?.points.append(p)
            redraw?()
        }
    }

    func end(at p: CGPoint) {
        defer {
            current = nil
            pendingSnapshot = nil
            startRegion = nil
        }
        // Radierer antippen: ganze Fläche wieder weiß machen
        if tool == .eraser, let r = startRegion, travel < 3 {
            if coloring.fills[r] != nil || coloring.strokes.contains(where: { $0.region == r }) {
                push(coloring)
                coloring.fills[r] = nil
                coloring.strokes.removeAll { $0.region == r }
                commit()
                Haptics.tap()
            } else {
                redraw?()
            }
            return
        }
        if let stroke = current {
            if let snap = pendingSnapshot { push(snap) }
            coloring.strokes.append(stroke)
            commit()
            return
        }
        // Tippen mit dem Eimer: Fläche füllen
        if tool == .fill, let r = startRegion, travel < 5 {
            push(coloring)
            coloring.fills[r] = colorIndex
            coloring.strokes.removeAll { $0.region == r }
            commit()
            Haptics.tap()
        }
    }

    func cancel() {
        current = nil
        pendingSnapshot = nil
        redraw?()
    }

    // MARK: Aktionen

    func undo() {
        guard let last = undoStack.popLast() else { return }
        coloring = last
        canUndo = !undoStack.isEmpty
        commit()
    }

    func reset() {
        guard !coloring.isEmpty else { return }
        push(coloring)
        coloring = Coloring()
        commit()
    }

    func exportImage() -> UIImage {
        Exporter.image(for: motif, coloring: coloring)
    }

    // MARK: Intern

    private func push(_ snapshot: Coloring) {
        undoStack.append(snapshot)
        if undoStack.count > 40 { undoStack.removeFirst() }
        canUndo = true
    }

    private func commit() {
        hasContent = !coloring.isEmpty
        ProgressStore.shared.save(coloring, for: motif.id)
        redraw?()
    }
}
