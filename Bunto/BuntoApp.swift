import SwiftUI

@main
struct BuntoApp: App {
    var body: some Scene {
        WindowGroup {
            RootView()
                .preferredColorScheme(.light)
        }
    }
}

/// Zeigt zuerst den animierten Start, danach die Startseite.
struct RootView: View {
    @State private var showSplash = true

    var body: some View {
        ZStack {
            HomeView()
            if showSplash {
                SplashView {
                    withAnimation(.easeInOut(duration: 0.6)) { showSplash = false }
                }
                .transition(.opacity)
                .zIndex(1)
            }
        }
    }
}
