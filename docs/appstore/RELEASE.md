# Bunto veröffentlichen – TestFlight und App Store

Alles, was Sie von Hand erledigen müssen, in der richtigen Reihenfolge. Was ich nicht für Sie tun kann
(Apple-Anmeldung, Zahlung, Zertifikate, Einreichen), ist mit 👤 markiert.

## 1. Einmalig vorbereiten
1. 👤 **Apple Developer Program** beitreten: <https://developer.apple.com/programs/enroll/> (99 $/Jahr, Freischaltung bis 2 Tage).
2. 👤 **Team-ID** notieren: developer.apple.com → Account → Membership details → *Team ID* (10 Zeichen).
3. **Bundle-ID** festlegen, z. B. `de.ihrefirma.bunto`. In `project.yml` ersetzen:
   - `bundleIdPrefix: com.example` → `de.ihrefirma`
   - `PRODUCT_BUNDLE_IDENTIFIER: com.example.bunto` → `de.ihrefirma.bunto`
   - `DEVELOPMENT_TEAM: ""` → Ihre Team-ID
   Danach `xcodegen generate`.
4. 👤 In Xcode → Settings → Accounts die Apple-ID hinzufügen.
5. 👤 **App in App Store Connect anlegen**: <https://appstoreconnect.apple.com> → Apps → „+“ → Neue App
   (iOS, Name „Bunto – Malen für Kinder“, Primärsprache Deutsch, Bundle-ID aus Schritt 3, SKU z. B. `bunto-001`).
6. 👤 **Datenschutz-URL** bereitstellen: in `docs/privacy-policy.md` die Kontaktadresse eintragen, dann in GitHub
   Settings → Pages (Branch `main`, Ordner `/docs`) aktivieren. Die URL wird dann
   `https://<user>.github.io/malbuch-ios/privacy-policy`.

## 2. Bauen und hochladen
Variante A – per Skript (Terminal):
```bash
TEAM_ID=ABCDE12345 ./tools/appstore/archive.sh
```
Das Skript erzeugt `build/Bunto.xcarchive` und `build/export/Bunto.ipa`. Hochladen:
```bash
xcrun altool --upload-app -f build/export/Bunto.ipa -t ios --apiKey <KEY_ID> --apiIssuer <ISSUER_ID>
```
(API-Key: App Store Connect → Benutzer und Zugriff → Integrationen → App-Store-Connect-API.)
Oder die `.ipa` mit der kostenlosen Mac-App **Transporter** hochladen.

Variante B – in Xcode: `open Bunto.xcodeproj` → Ziel *Any iOS Device (arm64)* → Product → Archive → Distribute App →
App Store Connect → Upload.

Build-Nummer vor jedem weiteren Upload erhöhen (`CURRENT_PROJECT_VERSION` in `project.yml`).

## 3. TestFlight
1. Nach 10–30 Minuten Verarbeitung erscheint der Build unter App Store Connect → TestFlight.
2. Export-Compliance-Frage beantworten („Keine Verschlüsselung“, ist im Build bereits hinterlegt).
3. 👤 **Interne Tester**: Gruppe anlegen, Teammitglieder (App-Store-Connect-Nutzer) hinzufügen – sofort, ohne Prüfung.
4. 👤 **Externe Tester**: Gruppe + öffentlicher Link, kurze Beta-Prüfung durch Apple.
5. Tester installieren über die App **TestFlight** auf dem iPhone/iPad.

## 4. Direkt auf dem eigenen Gerät testen
iPhone per Kabel verbinden → Einstellungen → Datenschutz & Sicherheit → *Entwicklermodus* an → in Xcode das Gerät
wählen → ▶.

## 5. App Store einreichen
1. 👤 In App Store Connect die Version 1.0 öffnen und aus `listing.md` einfügen: Texte (DE und EN), Keywords, URLs.
2. 👤 Screenshots hochladen aus `docs/appstore/screenshots/` (iPhone 6.9″ und iPad 13″, je DE/EN).
3. 👤 App-Datenschutz: „Daten werden nicht erhoben“. Altersfreigabe 4+, Kids Category, Preis kostenlos.
4. 👤 Build auswählen (aus TestFlight), Review-Hinweise aus `listing.md` einfügen.
5. 👤 „Zur Prüfung einreichen“. Prüfung meist 1–2 Tage.

## Screenshots neu erzeugen
```bash
python3 tools/appstore/seed_progress.py "<Simulator-Container>/Library/Application Support/Bunto"
```
befüllt einen Simulator mit schön ausgemalten Beispielen; Aufnahme per `xcrun simctl io <Gerät> screenshot datei.png`.
Hinweis: Die iPhone-Bilder stammen vom iPhone 17 (1206×2622) und wurden auf 1320×2868 (6.9″) hochskaliert. Für
pixelgenaue Bilder die Aufnahme auf dem **iPhone 18 Pro Max** wiederholen. Die Statusleiste (09:41) ist per
`xcrun simctl status_bar … override` gesetzt, ihre Sprache folgt dem Simulator (Deutsch).
