#!/usr/bin/env bash
# Erzeugt ein signiertes App-Store-Archiv und eine .ipa.  Aufruf:  TEAM_ID=ABCDE12345 ./tools/appstore/archive.sh
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${TEAM_ID:?TEAM_ID setzen (Apple Developer -> Membership -> Team ID)}"

xcodegen generate
rm -rf build/Bunto.xcarchive build/export
xcodebuild -project Bunto.xcodeproj -scheme Bunto -configuration Release \
  -destination 'generic/platform=iOS' -archivePath build/Bunto.xcarchive \
  DEVELOPMENT_TEAM="$TEAM_ID" -allowProvisioningUpdates archive

sed "s/TEAM_ID_PLATZHALTER/$TEAM_ID/" tools/appstore/ExportOptions.plist > build/ExportOptions.plist
xcodebuild -exportArchive -archivePath build/Bunto.xcarchive \
  -exportOptionsPlist build/ExportOptions.plist -exportPath build/export -allowProvisioningUpdates
echo "Fertig: build/export/Bunto.ipa"
