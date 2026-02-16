// ─────────────────────────────────────────────────
// SailTypography.swift
// Auto-generated from sail-tokens.json
// Generated: 2026-02-16 14:53
// DO NOT EDIT — re-run generate_swift.py instead
// ─────────────────────────────────────────────────

import SwiftUI

// MARK: - Font Families

enum SailFont {
    static let display = "Cormorant Garamond"
    static let body = "DM Sans"
    static let mono = "SF Mono"
}

// MARK: - Font Weights

extension Font.Weight {
    static let sailLight = Font.Weight.light
    static let sailRegular = Font.Weight.regular
    static let sailMedium = Font.Weight.medium
}

// MARK: - Font Sizes

enum SailFontSize {
    static let xxs: CGFloat = 11
    static let xs: CGFloat = 12
    static let sm: CGFloat = 13
    static let md: CGFloat = 16
    static let lg: CGFloat = 22
    static let xl: CGFloat = 36
    static let xxl: CGFloat = 42
}

// MARK: - Letter Spacing

enum SailLetterSpacing {
    static let tight: CGFloat = 0.5
    static let normal: CGFloat = 1
    static let wide: CGFloat = 2
    static let wider: CGFloat = 3
    static let widest: CGFloat = 6
}

// MARK: - Text Styles

struct SailTextStyle {
    let fontFamily: String
    let fontWeight: Font.Weight
    let fontSize: CGFloat
    let letterSpacing: CGFloat
    let lineHeight: CGFloat

    var font: Font {
        .custom(fontFamily, size: fontSize).weight(fontWeight)
    }
}

extension SailTextStyle {

    static let appTitle = SailTextStyle(
        fontFamily: "Cormorant Garamond",
        fontWeight: .light,
        fontSize: 42,
        letterSpacing: 6,
        lineHeight: 1.5
    )

    static let timer = SailTextStyle(
        fontFamily: "Cormorant Garamond",
        fontWeight: .light,
        fontSize: 36,
        letterSpacing: 2,
        lineHeight: 1.5
    )

    static let phrase = SailTextStyle(
        fontFamily: "Cormorant Garamond",
        fontWeight: .light,
        fontSize: 22,
        letterSpacing: 0.5,
        lineHeight: 1.6
    )

    static let button = SailTextStyle(
        fontFamily: "Cormorant Garamond",
        fontWeight: .regular,
        fontSize: 22,
        letterSpacing: 3,
        lineHeight: 1.5
    )

    static let pill = SailTextStyle(
        fontFamily: "DM Sans",
        fontWeight: .regular,
        fontSize: 13,
        letterSpacing: 1,
        lineHeight: 1.5
    )

    static let label = SailTextStyle(
        fontFamily: "DM Sans",
        fontWeight: .light,
        fontSize: 11,
        letterSpacing: 2,
        lineHeight: 1.5
    )

    static let subtitle = SailTextStyle(
        fontFamily: "DM Sans",
        fontWeight: .light,
        fontSize: 12,
        letterSpacing: 3,
        lineHeight: 1.5
    )
}
