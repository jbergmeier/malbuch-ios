import SwiftUI

/// Cooler Start: Farbkleckse platschen auf den Bildschirm, die Buchstaben hüpfen herein.
struct SplashView: View {
    let onFinish: () -> Void

    @State private var go = false
    @State private var wobble = false
    @State private var finished = false

    private struct Splat {
        let x: CGFloat, y: CGFloat, size: CGFloat, color: Color, delay: Double
    }

    private let splats: [Splat] = [
        Splat(x: 0.15, y: 0.14, size: 170, color: Color(hex: 0xFF7EB6), delay: 0.00),
        Splat(x: 0.85, y: 0.10, size: 130, color: Color(hex: 0xFFD23F), delay: 0.10),
        Splat(x: 0.90, y: 0.42, size: 190, color: Color(hex: 0x6EC6FF), delay: 0.18),
        Splat(x: 0.08, y: 0.50, size: 140, color: Color(hex: 0xA7D676), delay: 0.26),
        Splat(x: 0.20, y: 0.86, size: 200, color: Color(hex: 0x9B5DE5), delay: 0.12),
        Splat(x: 0.78, y: 0.88, size: 160, color: Color(hex: 0xFF8C42), delay: 0.22),
        Splat(x: 0.50, y: 0.08, size: 90, color: Color(hex: 0x3FD0C9), delay: 0.30),
        Splat(x: 0.52, y: 0.95, size: 100, color: Color(hex: 0xE63946), delay: 0.34)
    ]

    private let letters = Array("Bunto")

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()

            GeometryReader { geo in
                ForEach(splats.indices, id: \.self) { i in
                    let s = splats[i]
                    Circle()
                        .fill(s.color.opacity(0.85))
                        .frame(width: s.size, height: s.size)
                        .scaleEffect(go ? 1 : 0.001)
                        .position(x: geo.size.width * s.x, y: geo.size.height * s.y)
                        .animation(.spring(response: 0.7, dampingFraction: 0.5).delay(s.delay), value: go)
                }
            }
            .ignoresSafeArea()

            VStack(spacing: 18) {
                HStack(spacing: 2) {
                    ForEach(letters.indices, id: \.self) { i in
                        Text(String(letters[i]))
                            .font(.system(size: 96, weight: .heavy, design: .rounded))
                            .foregroundStyle(Theme.letterColors[i % Theme.letterColors.count])
                            .rotationEffect(.degrees(wobble ? (i % 2 == 0 ? 5 : -5) : (i % 2 == 0 ? -5 : 5)))
                            .animation(.easeInOut(duration: 0.55).repeatForever(autoreverses: true), value: wobble)
                            .scaleEffect(go ? 1 : 0.01)
                            .offset(y: go ? 0 : -320)
                            .animation(.spring(response: 0.6, dampingFraction: 0.45).delay(0.45 + Double(i) * 0.12), value: go)
                    }
                }
                .padding(.horizontal, 24)
                .padding(.vertical, 10)
                .background(
                    RoundedRectangle(cornerRadius: 40, style: .continuous)
                        .fill(.white.opacity(0.9))
                        .shadow(color: .black.opacity(0.12), radius: 14, y: 8)
                        .scaleEffect(go ? 1 : 0.2)
                        .animation(.spring(response: 0.6, dampingFraction: 0.6).delay(0.3), value: go)
                )

                Text("🖍️")
                    .font(.system(size: 64))
                    .rotationEffect(.degrees(wobble ? 14 : -14))
                    .offset(y: wobble ? -8 : 8)
                    .scaleEffect(go ? 1 : 0.01)
                    .animation(.spring(response: 0.6, dampingFraction: 0.5).delay(1.0), value: go)
                    .animation(.easeInOut(duration: 0.55).repeatForever(autoreverses: true), value: wobble)
            }
        }
        .contentShape(Rectangle())
        .onTapGesture { finish() }
        .onAppear {
            go = true
            DispatchQueue.main.asyncAfter(deadline: .now() + 1.3) { wobble = true }
            let total: Double = UIAccessibility.isReduceMotionEnabled ? 1.2 : 3.0
            DispatchQueue.main.asyncAfter(deadline: .now() + total) { finish() }
        }
        .accessibilityHidden(true)
    }

    private func finish() {
        guard !finished else { return }
        finished = true
        onFinish()
    }
}
