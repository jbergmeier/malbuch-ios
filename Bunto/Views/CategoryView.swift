import SwiftUI

struct BackButton: View {
    @Environment(\.dismiss) private var dismiss
    var systemName = "chevron.left"

    var body: some View {
        CircleIconButton(systemName: systemName, label: "back", tint: Color(hex: 0x9B5DE5)) {
            dismiss()
        }
    }
}

struct CategoryView: View {
    let category: MotifCategory
    @ObservedObject private var store = ProgressStore.shared
    @Environment(\.displayScale) private var displayScale

    private let columns = [GridItem(.adaptive(minimum: 150, maximum: 260), spacing: 16)]

    var body: some View {
        ZStack {
            Theme.background.ignoresSafeArea()
            VStack(spacing: 0) {
                HStack(spacing: 14) {
                    BackButton()
                    Text(category.emoji).font(.system(size: 44))
                    Text(category.name)
                        .font(Theme.rounded(32))
                        .foregroundStyle(Color(hex: 0x2B2D42))
                        .minimumScaleFactor(0.6)
                        .lineLimit(1)
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.vertical, 10)

                ScrollView {
                    LazyVGrid(columns: columns, spacing: 16) {
                        ForEach(category.motifs) { motif in
                            NavigationLink(value: motif) {
                                MotifCard(motif: motif,
                                          coloring: store.colorings[motif.id],
                                          tint: category.tint,
                                          scale: displayScale)
                            }
                            .buttonStyle(BouncyButtonStyle())
                        }
                    }
                    .padding(.horizontal, 20)
                    .padding(.bottom, 30)
                    .frame(maxWidth: 1100)
                    .frame(maxWidth: .infinity)
                }
            }
        }
        .toolbar(.hidden, for: .navigationBar)
    }
}

struct MotifCard: View {
    let motif: Motif
    let coloring: Coloring?
    let tint: Color
    let scale: CGFloat

    var body: some View {
        GeometryReader { geo in
            let side = max(geo.size.width - 16, 10)
            Image(uiImage: Thumbnails.image(for: motif, coloring: coloring, side: side, scale: scale))
                .resizable()
                .scaledToFit()
                .clipShape(RoundedRectangle(cornerRadius: 18, style: .continuous))
                .padding(8)
        }
        .aspectRatio(1, contentMode: .fit)
        .background(RoundedRectangle(cornerRadius: 26, style: .continuous).fill(.white))
        .overlay(RoundedRectangle(cornerRadius: 26, style: .continuous).strokeBorder(tint, lineWidth: 4))
        .shadow(color: tint.opacity(0.25), radius: 5, y: 3)
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(motif.name)
    }
}
