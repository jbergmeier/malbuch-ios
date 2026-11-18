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

    /// Zusätzliche Spezialfarbe nach den Grundfarben: Regenbogen (Verlauf beim Füllen, wechselnde Farben beim Pinsel).
    static let rainbowIndex = hexes.count

    /// Farben des Regenbogens, von Rot bis Violett.
    static let rainbowHexes: [UInt32] = [0xE63946, 0xFF8C42, 0xFFD23F, 0x2EC27E, 0x3FD0C9, 0x3A7BD5, 0x9B5DE5]

    static var count: Int { hexes.count + 1 }

    static func isRainbow(_ index: Int) -> Bool { index == rainbowIndex }

    /// Farbe des Regenbogens an Position t (0...1, zyklisch).
    static func rainbow(at t: CGFloat) -> UIColor {
        let n = rainbowHexes.count
        let x = (t - floor(t)) * CGFloat(n)
        let i = Int(x) % n
        let f = x - floor(x)
        func comps(_ c: UIColor) -> (CGFloat, CGFloat, CGFloat) {
            var r: CGFloat = 0, g: CGFloat = 0, bl: CGFloat = 0, al: CGFloat = 0
            c.getRed(&r, green: &g, blue: &bl, alpha: &al)
            return (r, g, bl)
        }
        let a = comps(UIColor(hex: rainbowHexes[i]))
        let b = comps(UIColor(hex: rainbowHexes[(i + 1) % n]))
        return UIColor(red: a.0 + (b.0 - a.0) * f, green: a.1 + (b.1 - a.1) * f,
                       blue: a.2 + (b.2 - a.2) * f, alpha: 1)
    }

    static func ui(_ index: Int) -> UIColor {
        guard index >= 0, index < hexes.count else { return .white }
        return UIColor(hex: hexes[index])
    }

    static func color(_ index: Int) -> Color {
        if isRainbow(index) { return Color(hex: rainbowHexes[0]) }
        guard index >= 0, index < hexes.count else { return .white }
        return Color(hex: hexes[index])
    }
}
