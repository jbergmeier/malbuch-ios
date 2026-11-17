import SwiftUI
import UIKit

extension UIColor {
    convenience init(hex: UInt32) {
        self.init(red: CGFloat((hex >> 16) & 0xFF) / 255,
                  green: CGFloat((hex >> 8) & 0xFF) / 255,
                  blue: CGFloat(hex & 0xFF) / 255,
                  alpha: 1)
    }
}

extension Color {
    init(hex: UInt32, opacity: Double = 1) {
        self.init(.sRGB,
                  red: Double((hex >> 16) & 0xFF) / 255,
                  green: Double((hex >> 8) & 0xFF) / 255,
                  blue: Double(hex & 0xFF) / 255,
                  opacity: opacity)
    }
}

/// Kinderfreundliche, kräftige Farbpalette. Index -1 = Weiß (Radierer).
enum Palette {
    static let hexes: [UInt32] = [
        0xE63946, // Rot
        0xFF8C42, // Orange
        0xFFD23F, // Gelb
        0xA7D676, // Hellgrün
        0x2EC27E, // Grün
        0x3FD0C9, // Türkis
        0x6EC6FF, // Himmelblau
        0x3A7BD5, // Blau
        0x9B5DE5, // Lila
        0xFF7EB6, // Rosa
        0x8B5A2B, // Braun
        0xF2C9A0, // Hautton
        0x9AA5B1, // Grau
        0x2B2D42  // Schwarz
    ]

    static var count: Int { hexes.count }

    static func ui(_ index: Int) -> UIColor {
        guard index >= 0, index < hexes.count else { return .white }
        return UIColor(hex: hexes[index])
    }

    static func color(_ index: Int) -> Color {
        guard index >= 0, index < hexes.count else { return .white }
        return Color(hex: hexes[index])
    }
}
