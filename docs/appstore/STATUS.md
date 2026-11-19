# Einreichungs-Stand (App Store Connect, App-ID 6836277407)

Bundle-ID `com.b2int.bunto` · Team `5PJWLR57B8` · SKU `bunto-paintapp`

## Erledigt (in App Store Connect eingetragen und gesichert)
- Name „Bunto – Malen für Kinder“, Untertitel „Ausmalen ohne Werbung“
- Werbetext, Beschreibung (inkl. „Keine Werbung. Keine In-App-Käufe.“, saisonale Updates, Autoreninfo), Schlüsselwörter, Support-/Marketing-URL, Copyright
- Screenshots Deutsch: iPhone (1206×2622) und iPad 13″ (2064×2752), je 5 Bilder
- Kategorie Bildung + Spiele · Altersfreigabe 4+ · „Für Kinder empfohlen“ (bis 5 Jahre)
- Inhaltsrechte: keine Inhalte Dritter · App-Datenschutz: „Daten werden nicht erhoben“, Datenschutz-URL gesetzt
- Preis 0,00 (kostenlos), Verfügbarkeit alle 175 Länder
- Review-Informationen: Kontakt, Hinweise, keine Anmeldung nötig · manuelle Veröffentlichung

## Eingereicht am 18.11.2026
Version 1.0 (Build 1) ist zur App-Prüfung eingereicht, Status „Warten auf Prüfung“ (Dauer meist bis 48 Stunden, E-Mail von Apple folgt).
- Preis **0,79 €** (Basisland Deutschland), automatische Veröffentlichung nach Freigabe
- **Festlandchina abgewählt** (dort wären Sicherheitsbewertung und AIGC-Erklärung Pflicht); später in „Preise und Verfügbarkeit“ wieder aktivierbar
- Build wurde mit `xcodebuild -exportArchive` (destination upload) über die Xcode-Anmeldung hochgeladen

## Noch zu tun
1. **Vereinbarung für gebührenpflichtige Apps** (Bank/Steuer) in App Store Connect → Geschäftliches abschließen, sonst kann die kostenpflichtige App nicht veröffentlicht werden.
2. Website bunto.webcoffee.io: „kostenlos“-Texte an den Preis anpassen, „Bald im App Store“ durch den Link ersetzen.
3. Optional: englische Lokalisierung.


## Update 18.11.2026 (später)
Version 1.0 wurde aus der Prüfung genommen und mit **Build 2** (128 Motive, 15 Kategorien, Regenbogenfarbe) neu eingereicht (Status „Warten auf Prüfung“, 18:22). Veröffentlichung automatisch, Preis 0,79 €. Hinweis: Xcode erhöht beim Upload die Build-Nummer selbst; die Versionsnummer in `Info.plist` bleibt 1.0 (MARKETING_VERSION in project.yml wirkt nicht – für 1.1 ggf. die Info.plist-Erzeugung prüfen). Offen: Ostern, Halloween als nächste Updates.

## Update 19.11.2026
- Version 1.0 wurde von Apple freigegeben („Bereit für Vertrieb“, 15:41); EU-Händlerstatus (DSA) ist angegeben.
- **Version 1.0.1 (Build 3)** am 19.11. zur Prüfung eingereicht („Warten auf Prüfung“): englische Lokalisierung (Name „Bunto – Coloring for Kids“, Untertitel „Ad-free coloring fun“, Texte, Keywords, englische Screenshots iPhone 1206×2622 / iPad 2064×2752), „Neu in dieser Version“ in DE/EN. Veröffentlichung automatisch nach Freigabe.
- Versionsnummer wird jetzt aus `project.yml` (MARKETING_VERSION/CURRENT_PROJECT_VERSION) in die Info.plist übernommen.
- Preis: in App Store Connect auf 0,99 € (Basisland Deutschland) gestellt bzw. zu prüfen; Webseite nennt 0,99 €.
