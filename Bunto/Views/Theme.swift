import SwiftUI

enum Theme {
    static let background = LinearGradient(
        colors: [Color(hex: 0xFFF6DA), Color(hex: 0xFFE3F1), Color(hex: 0xDDEBFF)],
        startPoint: .topLeading, endPoint: .bottomTrailing)

    static let letterColors: [Color] = [
        Color(hex: 0xE63946), Color(hex: 0xFF8C42), Color(hex: 0xF2B705),
        Color(hex: 0x2EC27E), Color(hex: 0x3A7BD5)
    ]

    static func rounded(_ size: CGFloat, _ weight: Font.Weight = .heavy) -> Font {
        .system(size: size, weight: weight, design: .rounded)
    }
}

/// Große, hüpfende Knöpfe – gut für kleine Finger.
struct BouncyButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.92 : 1)
            .animation(.spring(response: 0.25, dampingFraction: 0.55), value: configuration.isPressed)
    }
}

/// Runder Symbol-Knopf (mind. 56 pt)
struct CircleIconButton: View {
    let systemName: String
    let label: LocalizedStringKey
    var tint: Color = Color(hex: 0x3A7BD5)
    var enabled: Bool = true
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            Image(systemName: systemName)
                .font(.system(size: 26, weight: .bold, design: .rounded))
                .foregroundStyle(.white)
                .frame(width: 60, height: 60)
                .background(Circle().fill(tint))
                .shadow(color: tint.opacity(0.35), radius: 6, y: 4)
                .opacity(enabled ? 1 : 0.35)
        }
        .buttonStyle(BouncyButtonStyle())
        .disabled(!enabled)
        .accessibilityLabel(label)
    }
}

struct BuntoTitle: View {
    var size: CGFloat = 56
    var body: some View {
        HStack(spacing: 1) {
            ForEach(Array("Bunto".enumerated()), id: \.offset) { i, ch in
                Text(String(ch))
                    .font(Theme.rounded(size))
                    .foregroundStyle(Theme.letterColors[i % Theme.letterColors.count])
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("Bunto")
    }
}
