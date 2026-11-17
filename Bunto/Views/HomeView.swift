import SwiftUI

struct HomeView: View {
    private let catalog = Catalog.shared
    @State private var surprise: Motif?

    @Environment(\.horizontalSizeClass) private var hSize
    private var columns: [GridItem] {
        hSize == .regular
            ? [GridItem(.adaptive(minimum: 230, maximum: 340), spacing: 24)]
            : [GridItem(.adaptive(minimum: 150, maximum: 240), spacing: 18)]
    }

    var body: some View {
        NavigationStack {
            ZStack {
                Theme.background.ignoresSafeArea()
                ScrollView {
                    VStack(spacing: 20) {
                        header
                        LazyVGrid(columns: columns, spacing: 18) {
                            ForEach(catalog.categories) { category in
                                NavigationLink(value: category) {
                                    CategoryCard(category: category)
                                }
                                .buttonStyle(BouncyButtonStyle())
                            }
                        }
                        .padding(.horizontal, 20)
                        .padding(.bottom, 30)
                    }
                    .frame(maxWidth: 1100)
                    .frame(maxWidth: .infinity)
                }
            }
            .toolbar(.hidden, for: .navigationBar)
            .navigationDestination(for: MotifCategory.self) { CategoryView(category: $0) }
            .navigationDestination(for: Motif.self) { ColoringView(motif: $0) }
            .onAppear { if surprise == nil { surprise = catalog.allMotifs.randomElement() } }
        }
    }

    private var header: some View {
        HStack {
            BuntoTitle(size: 60)
            Spacer()
            if let motif = surprise {
                NavigationLink(value: motif) {
                    Text("🎲")
                        .font(.system(size: 38))
                        .frame(width: 70, height: 70)
                        .background(Circle().fill(Color(hex: 0xFFD23F)))
                        .shadow(color: Color(hex: 0xFFD23F).opacity(0.5), radius: 6, y: 4)
                }
                .buttonStyle(BouncyButtonStyle())
                .simultaneousGesture(TapGesture().onEnded {
                    // nächstes Überraschungsmotiv vorbereiten
                    DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
                        surprise = catalog.allMotifs.randomElement()
                    }
                })
                .accessibilityLabel("surprise")
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 12)
    }
}

struct CategoryCard: View {
    @Environment(\.horizontalSizeClass) private var hSize
    let category: MotifCategory

    var body: some View {
        VStack(spacing: 8) {
            Text(category.emoji)
                .font(.system(size: hSize == .regular ? 96 : 66))
            Text(category.name)
                .font(Theme.rounded(22))
                .foregroundStyle(Color(hex: 0x2B2D42))
                .minimumScaleFactor(0.7)
                .lineLimit(1)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 22)
        .background(
            RoundedRectangle(cornerRadius: 32, style: .continuous)
                .fill(category.tint.opacity(0.28))
        )
        .overlay(
            RoundedRectangle(cornerRadius: 32, style: .continuous)
                .strokeBorder(category.tint, lineWidth: 4)
        )
        .shadow(color: category.tint.opacity(0.25), radius: 6, y: 4)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(category.name)
    }
}
