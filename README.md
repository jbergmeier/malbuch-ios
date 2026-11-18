# Bunto – Ausmal-App für Kinder (iPhone & iPad)

Kostenlos, ohne Werbung, ohne Login, ohne Internet. 128 selbst erstellte, lizenzfreie Motive in 15 Kategorien (inkl. Weihnachten, Advent, Winter, Freies Malen)
(Dinos, Baustelle, Häuser, Mandalas, Tiere, Meer, Fahrzeuge, Weltraum, Essen, Natur, Fantasie).

## Bedienung (für kleine Kinder)
- 🪣 **Eimer**: Farbe wählen, Fläche antippen – füllt exakt bis zum Rand.
- 🖌️ **Pinsel**: Mit dem Finger malen – die Farbe bleibt automatisch innerhalb der Fläche, in der man startet (Randhilfe).
- 🧽 **Radierer**, ↩︎ Rückgängig, 🗑 Neu anfangen, 💾 In **Fotos** speichern, 🎲 Überraschungsmotiv.
- Fortschritt wird automatisch lokal gespeichert; Vorschaubilder zeigen das bereits Gemalte.

## Projekt bauen (Mac mit Xcode 15+)
```bash
brew install xcodegen
xcodegen generate
open Bunto.xcodeproj
```
1. In `project.yml`: `bundleIdPrefix` / `PRODUCT_BUNDLE_IDENTIFIER` und `DEVELOPMENT_TEAM` setzen, dann erneut `xcodegen generate`.
2. Auf Simulator (iPhone + iPad) oder Gerät starten.
3. Für den App Store: *Product → Archive → Distribute App → App Store Connect*.

## Motive ändern / ergänzen
Alle Motive werden per Python-Code erzeugt (`tools/motifs/`), also komplett eigene Werke ohne Fremdmaterial.
```bash
python3 tools/motifs/build.py      # schreibt Bunto/Resources/motifs.json + Vorschau-PNGs in tools/motifs/_preview/
python3 tools/make_icon.py Bunto/Resources/Assets.xcassets/AppIcon.appiconset/icon.png
```

## Veröffentlichen
Anleitung: [docs/appstore/RELEASE.md](docs/appstore/RELEASE.md) · Store-Texte: [docs/appstore/listing.md](docs/appstore/listing.md) · Screenshots: `docs/appstore/screenshots/`

## Checkliste App-Store-Veröffentlichung
- [ ] Apple Developer Account (99 $/Jahr), App in App Store Connect anlegen (Name „Bunto“ prüfen, ggf. Untertitel ergänzen).
- [ ] **Kids Category** wählen (Alter 5 und jünger oder 6–8): erlaubt, da keine Werbung, kein Tracking, keine Drittanbieter-SDKs, keine externen Links, keine Käufe.
- [ ] **Altersfreigabe 4+** (Fragebogen: überall „Nein“).
- [ ] **App-Datenschutz**: „Daten werden nicht erhoben“. `PrivacyInfo.xcprivacy` ist enthalten (kein Tracking).
- [ ] **Datenschutz-URL** angeben: `docs/privacy-policy.md` z. B. per GitHub Pages veröffentlichen, Kontaktadresse eintragen.
- [ ] Screenshots: iPhone 6.9" + iPad 13" (Simulator → ⌘S), Beschreibung DE/EN.
- [ ] Export-Compliance: `ITSAppUsesNonExemptEncryption = NO` ist gesetzt.
- [ ] Foto-Berechtigung: nur Schreibzugriff (`NSPhotoLibraryAddUsageDescription`, DE/EN lokalisiert).
- [ ] Support-URL angeben (Pflichtfeld).
