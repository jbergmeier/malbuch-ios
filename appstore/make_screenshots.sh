#!/bin/bash
# Erzeugt App-Store-Screenshots (DE + EN) per UI-Test auf den passenden Simulatoren.
# Nutzung: ./appstore/make_screenshots.sh
set -euo pipefail
cd "$(dirname "$0")/.."
IPHONE="iPhone 18 Pro Max"      # 6.9" -> 1320x2868
IPAD="iPad Pro 13-inch (M5)"    # 13"  -> 2064x2752
xcodegen generate >/dev/null
for dev in "$IPHONE" "$IPAD"; do
  folder=$([ "$dev" = "$IPHONE" ] && echo "iphone-6.9" || echo "ipad-13")
  for lang in de en; do
    out="$PWD/appstore/screenshots/$lang/$folder"
    rm -rf "$out"; mkdir -p "$out"
    xcrun simctl boot "$dev" 2>/dev/null || true
    xcrun simctl status_bar "$dev" override --time 9:41 --batteryState charged --batteryLevel 100 --wifiBars 3 --cellularBars 4 || true
    xcrun simctl uninstall "$dev" com.example.bunto 2>/dev/null || true
    TEST_RUNNER_SHOT_DIR="$out" TEST_RUNNER_SHOT_LANG="$lang" \
    xcodebuild test -project Bunto.xcodeproj -scheme Bunto \
      -destination "platform=iOS Simulator,name=$dev" -derivedDataPath build \
      CODE_SIGNING_ALLOWED=NO -quiet 2>&1 | tail -5
  done
done
echo "Fertig: appstore/screenshots/"
