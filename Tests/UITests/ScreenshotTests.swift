import XCTest

/// Durchläuft alle Hauptbildschirme und legt App-Store-Screenshots ab.
/// Zielordner: Umgebungsvariable SHOT_DIR (siehe appstore/make_screenshots.sh).
final class ScreenshotTests: XCTestCase {
    var app: XCUIApplication!
    var de: Bool { Locale.preferredLanguages.first?.hasPrefix("de") ?? false }

    override func setUp() {
        continueAfterFailure = false
        app = XCUIApplication()
        let lang = ProcessInfo.processInfo.environment["SHOT_LANG"] ?? "de"
        app.launchArguments = ["-AppleLanguages", "(\(lang))", "-AppleLocale", lang == "de" ? "de_DE" : "en_US"]
        app.launch()
    }

    private func shot(_ name: String) {
        let dir = ProcessInfo.processInfo.environment["SHOT_DIR"] ?? NSTemporaryDirectory()
        let data = XCUIScreen.main.screenshot().pngRepresentation
        try? FileManager.default.createDirectory(atPath: dir, withIntermediateDirectories: true)
        try? data.write(to: URL(fileURLWithPath: "\(dir)/\(name).png"))
        let att = XCTAttachment(data: data, uniformTypeIdentifier: "public.png")
        att.name = name; att.lifetime = .keepAlways
        add(att)
    }

    private func button(_ labels: [String]) -> XCUIElement {
        let p = NSPredicate(format: "label IN %@", labels)
        return app.buttons.matching(p).firstMatch
    }

    private func openCategory(_ labels: [String]) {
        let b = button(labels)
        XCTAssertTrue(b.waitForExistence(timeout: 20), "Kategorie \(labels) fehlt")
        b.tap()
    }

    private func paint(_ canvas: XCUIElement, colorIndex: Int, at p: CGVector) {
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Farbe", "Color"])).element(boundBy: colorIndex).tap()
        canvas.coordinate(withNormalizedOffset: p).tap()
    }

    func testAllScreens() {
        // 1. Startseite
        XCTAssertTrue(button(["Dinos"]).waitForExistence(timeout: 20))
        sleep(1)
        shot("01-home")

        // 2. Kategorie
        openCategory(["Dinos"])
        XCTAssertTrue(button(["T-Rex"]).waitForExistence(timeout: 5))
        shot("02-category")

        // 3. Ausmalen: T-Rex bunt
        button(["T-Rex"]).tap()
        let canvas = app.descendants(matching: .any).matching(NSPredicate(format: "label == 'T-Rex'")).firstMatch
        XCTAssertTrue(canvas.waitForExistence(timeout: 5))
        paint(canvas, colorIndex: 4, at: CGVector(dx: 0.49, dy: 0.55))   // Körper grün
        paint(canvas, colorIndex: 3, at: CGVector(dx: 0.79, dy: 0.36))   // Kopf hellgrün
        paint(canvas, colorIndex: 1, at: CGVector(dx: 0.18, dy: 0.67))   // Schwanz orange
        paint(canvas, colorIndex: 9, at: CGVector(dx: 0.50, dy: 0.92))   // Bein rosa
        paint(canvas, colorIndex: 2, at: CGVector(dx: 0.71, dy: 0.66))   // Arm gelb
        // Pinselstrich
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Pinsel", "Brush"])).firstMatch.tap()
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Farbe", "Color"])).element(boundBy: 7).tap()
        let a = canvas.coordinate(withNormalizedOffset: CGVector(dx: 0.30, dy: 0.50))
        let b = canvas.coordinate(withNormalizedOffset: CGVector(dx: 0.62, dy: 0.50))
        a.press(forDuration: 0.1, thenDragTo: b)
        sleep(1)
        shot("03-coloring")

        // 4. Weitere Kategorien
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Zurück", "Back"])).firstMatch.tap()
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Zurück", "Back"])).firstMatch.tap()
        openCategory(["Mandalas"])
        sleep(1)
        shot("04-mandalas")
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Zurück", "Back"])).firstMatch.tap()
        openCategory(["Weltraum", "Space"])
        sleep(1)
        shot("05-space")

        // 5. Würfel
        app.buttons.matching(NSPredicate(format: "label IN %@", ["Zurück", "Back"])).firstMatch.tap()
        let dice = button(["Überrasch mich", "Überrasche mich", "Surprise me"])
        if dice.waitForExistence(timeout: 3) { dice.tap(); sleep(1) }
    }
}
