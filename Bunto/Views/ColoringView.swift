import SwiftUI
import UIKit

// MARK: - Zeichenfläche (UIKit für präzise, ruckelfreie Touch-Eingabe)

final class CanvasUIView: UIView {
    weak var model: ColoringModel?

    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        isOpaque = true
        contentMode = .redraw
        isMultipleTouchEnabled = false   // Handballen / zweite Finger werden ignoriert
        layer.cornerRadius = 0
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) has not been implemented") }

    override func draw(_ rect: CGRect) {
        guard let model, let cg = UIGraphicsGetCurrentContext(), bounds.width > 0 else { return }
        CanvasRenderer.draw(motif: model.motif, coloring: model.coloring,
                            current: model.current, in: cg, size: bounds.width)
    }

    private func unit(_ touch: UITouch) -> CGPoint {
        let p = touch.location(in: self)
        return CGPoint(x: p.x / bounds.width * 100, y: p.y / bounds.height * 100)
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let t = touches.first else { return }
        model?.begin(at: unit(t))
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let t = touches.first else { return }
        let all = event?.coalescedTouches(for: t) ?? [t]
        for c in all { model?.move(to: unit(c)) }
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let t = touches.first else { return }
        model?.end(at: unit(t))
    }

    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        model?.cancel()
    }
}

struct CanvasView: UIViewRepresentable {
    let model: ColoringModel

    func makeUIView(context: Context) -> CanvasUIView {
        let v = CanvasUIView()
        v.model = model
        model.redraw = { [weak v] in v?.setNeedsDisplay() }
        return v
    }

    func updateUIView(_ uiView: CanvasUIView, context: Context) {
        uiView.setNeedsDisplay()
    }
}

// MARK: - Mal-Bildschirm

struct ColoringView: View {
    @StateObject private var model: ColoringModel
    @Environment(\.dismiss) private var dismiss

    @State private var showSaved = false
    @State private var showDenied = false
    @State private var confirmReset = false
    @State private var saving = false
    @Environment(\.horizontalSizeClass) private var hSize
    private var k: CGFloat { hSize == .regular ? 1.45 : 1 }

    init(motif: Motif) {
        _model = StateObject(wrappedValue: ColoringModel(motif: motif))
    }

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()

            GeometryReader { geo in
                let landscape = geo.size.width > geo.size.height * 1.15
                if landscape {
                    HStack(spacing: 18) {
                        canvas
                            .frame(width: min(geo.size.height - 24, geo.size.width * 0.62))
                            .frame(maxHeight: .infinity)
                        VStack(spacing: 18) {
                            topBar
                            Spacer(minLength: 0)
                            toolsBar
                            PaletteView(model: model, columns: 4)
                            Spacer(minLength: 0)
                        }
                        .frame(maxWidth: hSize == .regular ? 470 : 360)
                    }
                    .padding(12)
                } else {
                    VStack(spacing: 12) {
                        topBar
                        canvas
                            .frame(maxWidth: min(geo.size.width, max(geo.size.height - 260, 220)))
                        toolsBar
                        PaletteView(model: model, columns: 7)
                        Spacer(minLength: 0)
                    }
                    .padding(.horizontal, 14)
                    .padding(.vertical, 8)
                }
            }

            if showSaved {
                Text("saved_toast")
                    .font(Theme.rounded(26))
                    .foregroundStyle(.white)
                    .padding(.horizontal, 28)
                    .padding(.vertical, 16)
                    .background(Capsule().fill(Color(hex: 0x2EC27E)))
                    .shadow(radius: 10, y: 6)
                    .transition(.scale.combined(with: .opacity))
                    .zIndex(2)
            }
        }
        .toolbar(.hidden, for: .navigationBar)
        .navigationBarBackButtonHidden(true)   // verhindert versehentliches Zurückwischen beim Malen
        .alert("photos_denied_title", isPresented: $showDenied) {
            Button("ok", role: .cancel) {}
        } message: {
            Text("photos_denied_message")
        }
        .confirmationDialog("reset_title", isPresented: $confirmReset, titleVisibility: .visible) {
            Button("reset_confirm", role: .destructive) { model.reset() }
            Button("cancel", role: .cancel) {}
        }
    }

    private var canvas: some View {
        CanvasView(model: model)
            .aspectRatio(1, contentMode: .fit)
            .clipShape(RoundedRectangle(cornerRadius: 24, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: 24, style: .continuous)
                .strokeBorder(Color(hex: 0xD9CFF5), lineWidth: 4))
            .shadow(color: .black.opacity(0.12), radius: 10, y: 6)
            .accessibilityLabel(model.motif.name)
    }

    private var topBar: some View {
        HStack(spacing: 12) {
            BackButton()
            Spacer(minLength: 4)
            CircleIconButton(systemName: "arrow.uturn.backward", label: "undo",
                             tint: Color(hex: 0xFF8C42), enabled: model.canUndo) { model.undo() }
            CircleIconButton(systemName: "trash.fill", label: "reset",
                             tint: Color(hex: 0xE63946), enabled: model.hasContent) { confirmReset = true }
            CircleIconButton(systemName: "photo.badge.plus.fill", label: "save",
                             tint: Color(hex: 0x2EC27E), enabled: !saving) { save() }
        }
    }

    private var toolsBar: some View {
        HStack(spacing: 12) {
            toolButton(.fill, emoji: "🪣", label: "tool_fill")
            toolButton(.brush, emoji: "🖌️", label: "tool_brush")
            toolButton(.eraser, emoji: "🧽", label: "tool_eraser")
            Spacer(minLength: 4)
            HStack(spacing: 8) {
                ForEach(BrushSize.allCases, id: \.self) { size in
                    let selected = model.brushSize == size
                    Button { model.brushSize = size } label: {
                        Circle()
                            .fill(Color(hex: 0x2B2D42))
                            .frame(width: (8 + size.width * 2.6) * k, height: (8 + size.width * 2.6) * k)
                            .frame(width: 38 * k, height: 38 * k)
                            .background(Circle().fill(selected ? Color(hex: 0xFFD23F) : .white))
                            .overlay(Circle().strokeBorder(Color(hex: 0xD9CFF5), lineWidth: 3))
                    }
                    .buttonStyle(BouncyButtonStyle())
                    .accessibilityLabel(sizeLabel(size))
                }
            }
            .opacity(model.tool == .fill ? 0.35 : 1)
        }
    }

    private func sizeLabel(_ size: BrushSize) -> LocalizedStringKey {
        switch size {
        case .small: return "size_small"
        case .medium: return "size_medium"
        case .large: return "size_large"
        }
    }

    private func toolButton(_ tool: Tool, emoji: String, label: LocalizedStringKey) -> some View {
        let selected = model.tool == tool
        return Button { model.tool = tool } label: {
            Text(emoji)
                .font(.system(size: 30 * k))
                .frame(width: 58 * k, height: 58 * k)
                .background(RoundedRectangle(cornerRadius: 20, style: .continuous)
                    .fill(selected ? Color(hex: 0xFFD23F) : .white))
                .overlay(RoundedRectangle(cornerRadius: 20, style: .continuous)
                    .strokeBorder(selected ? Color(hex: 0xFF8C42) : Color(hex: 0xD9CFF5), lineWidth: 4))
                .scaleEffect(selected ? 1.06 : 1)
                .animation(.spring(response: 0.3, dampingFraction: 0.6), value: selected)
        }
        .buttonStyle(BouncyButtonStyle())
        .accessibilityLabel(label)
        .accessibilityAddTraits(selected ? .isSelected : [])
    }

    private func save() {
        saving = true
        let image = model.exportImage()
        Task {
            let ok = await PhotoSaver.save(image)
            saving = false
            if ok {
                Haptics.success()
                withAnimation(.spring(response: 0.4, dampingFraction: 0.6)) { showSaved = true }
                try? await Task.sleep(nanoseconds: 2_000_000_000)
                withAnimation(.easeOut(duration: 0.3)) { showSaved = false }
            } else {
                showDenied = true
            }
        }
    }
}

struct PaletteView: View {
    @ObservedObject var model: ColoringModel
    let columns: Int

    var body: some View {
        let cols = Array(repeating: GridItem(.flexible(), spacing: 10), count: columns)
        LazyVGrid(columns: cols, spacing: 10) {
            ForEach(0..<Palette.count, id: \.self) { i in
                let selected = model.colorIndex == i
                Button {
                    model.colorIndex = i
                    if model.tool == .eraser { model.tool = .fill }
                } label: {
                    Circle()
                        .fill(Palette.color(i))
                        .aspectRatio(1, contentMode: .fit)
                        .overlay(Circle().strokeBorder(.white, lineWidth: 3))
                        .overlay(Circle().strokeBorder(selected ? Color(hex: 0x2B2D42) : .clear, lineWidth: 4).padding(-4))
                        .shadow(color: .black.opacity(0.2), radius: 3, y: 2)
                        .scaleEffect(selected ? 1.12 : 1)
                        .animation(.spring(response: 0.3, dampingFraction: 0.55), value: selected)
                        .frame(maxWidth: 64)
                }
                .buttonStyle(BouncyButtonStyle())
                .accessibilityLabel("color")
                .accessibilityAddTraits(selected ? .isSelected : [])
            }
        }
        .padding(8)
    }
}
