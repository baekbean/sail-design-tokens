// ─────────────────────────────────────────────────
// SailColors.swift
// Auto-generated from sail-tokens.json
// Generated: 2026-02-16 14:53
// DO NOT EDIT — re-run generate_swift.py instead
// ─────────────────────────────────────────────────

import SwiftUI

// MARK: - Color Primitives

extension Color {
    enum Sail {

        enum Ocean {
            static let s50 = Color(red: 0.922, green: 0.961, blue: 0.984)
            static let s100 = Color(red: 0.682, green: 0.839, blue: 0.945)
            static let s200 = Color(red: 0.537, green: 0.812, blue: 0.941)
            static let s300 = Color(red: 0.365, green: 0.678, blue: 0.886)
            static let s400 = Color(red: 0.180, green: 0.525, blue: 0.757)
            static let s500 = Color(red: 0.106, green: 0.310, blue: 0.447)
            static let s600 = Color(red: 0.082, green: 0.263, blue: 0.376)
            static let s700 = Color(red: 0.055, green: 0.184, blue: 0.267)
            static let s800 = Color(red: 0.039, green: 0.122, blue: 0.180)
            static let s900 = Color(red: 0.020, green: 0.059, blue: 0.090)
        }

        enum Sunset {
            static let s50 = Color(red: 1.000, green: 0.961, blue: 0.902)
            static let s100 = Color(red: 1.000, green: 0.918, blue: 0.655)
            static let s200 = Color(red: 1.000, green: 0.745, blue: 0.463)
            static let s300 = Color(red: 1.000, green: 0.624, blue: 0.263)
            static let s400 = Color(red: 1.000, green: 0.420, blue: 0.420)
            static let s500 = Color(red: 0.933, green: 0.353, blue: 0.141)
            static let s600 = Color(red: 0.882, green: 0.439, blue: 0.333)
            static let s700 = Color(red: 0.753, green: 0.224, blue: 0.169)
            static let s800 = Color(red: 0.545, green: 0.102, blue: 0.102)
            static let s900 = Color(red: 0.361, green: 0.063, blue: 0.063)
        }

        enum Twilight {
            static let s50 = Color(red: 0.941, green: 0.902, blue: 1.000)
            static let s100 = Color(red: 0.800, green: 0.839, blue: 0.965)
            static let s200 = Color(red: 0.788, green: 0.839, blue: 1.000)
            static let s300 = Color(red: 0.651, green: 0.757, blue: 0.933)
            static let s400 = Color(red: 0.533, green: 0.573, blue: 0.690)
            static let s500 = Color(red: 0.400, green: 0.494, blue: 0.918)
            static let s600 = Color(red: 0.424, green: 0.361, blue: 0.906)
            static let s700 = Color(red: 0.290, green: 0.247, blue: 0.420)
            static let s800 = Color(red: 0.204, green: 0.122, blue: 0.592)
            static let s900 = Color(red: 0.102, green: 0.102, blue: 0.306)
        }

        enum Dawn {
            static let s50 = Color(red: 1.000, green: 0.961, blue: 0.976)
            static let s100 = Color(red: 0.984, green: 0.761, blue: 0.922)
            static let s200 = Color(red: 0.973, green: 0.647, blue: 0.824)
            static let s300 = Color(red: 0.910, green: 0.627, blue: 0.749)
            static let s400 = Color(red: 0.765, green: 0.812, blue: 0.886)
            static let s500 = Color(red: 0.651, green: 0.757, blue: 0.933)
            static let s600 = Color(red: 0.482, green: 0.557, blue: 0.784)
            static let s700 = Color(red: 0.361, green: 0.290, blue: 0.447)
            static let s800 = Color(red: 0.227, green: 0.110, blue: 0.443)
            static let s900 = Color(red: 0.118, green: 0.039, blue: 0.235)
        }

        enum Night {
            static let s50 = Color(red: 0.910, green: 0.925, blue: 0.957)
            static let s100 = Color(red: 0.788, green: 0.839, blue: 1.000)
            static let s200 = Color(red: 0.533, green: 0.573, blue: 0.690)
            static let s300 = Color(red: 0.290, green: 0.322, blue: 0.502)
            static let s400 = Color(red: 0.176, green: 0.208, blue: 0.380)
            static let s500 = Color(red: 0.078, green: 0.118, blue: 0.380)
            static let s600 = Color(red: 0.047, green: 0.078, blue: 0.271)
            static let s700 = Color(red: 0.039, green: 0.039, blue: 0.180)
            static let s800 = Color(red: 0.020, green: 0.020, blue: 0.082)
            static let s900 = Color(red: 0.008, green: 0.008, blue: 0.031)
        }
        static let white = Color(red: 1.000, green: 1.000, blue: 1.000)
        static let black = Color(red: 0.000, green: 0.000, blue: 0.000)
    }
}

// MARK: - Semantic Palette

struct SailPalette {
    let skyTop: Color
    let skyMid: Color
    let skyBottom: Color
    let waterSurface: Color
    let waterMid: Color
    let waterDeep: Color
    let celestialBody: Color
    let celestialGlow: Color
    let celestialType: String
    let textPrimary: Color
    let textSecondary: Color
    let uiRing: Color
    let uiRingBackground: Color
    let uiButtonBackground: Color
    let uiButtonActive: Color
    let boatHull: Color
    let boatSail: Color
}

extension SailPalette {

    static let dawn = SailPalette(
        skyTop: Color(red: 0.984, green: 0.761, blue: 0.922),
        skyMid: Color(red: 0.651, green: 0.757, blue: 0.933),
        skyBottom: Color(red: 0.765, green: 0.812, blue: 0.886),
        waterSurface: Color(red: 0.400, green: 0.494, blue: 0.918),
        waterMid: Color(red: 0.361, green: 0.290, blue: 0.447),
        waterDeep: Color(red: 0.227, green: 0.110, blue: 0.443),
        celestialBody: Color(red: 1.000, green: 0.918, blue: 0.655),
        celestialGlow: Color(red: 1.000, green: 0.878, blue: 0.400).opacity(0.25),
        celestialType: "sun",
        textPrimary: Color(red: 0.290, green: 0.247, blue: 0.420),
        textSecondary: Color(red: 0.290, green: 0.247, blue: 0.420).opacity(0.5),
        uiRing: Color(red: 1.000, green: 0.878, blue: 0.400).opacity(0.8),
        uiRingBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.15),
        uiButtonBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.2),
        uiButtonActive: Color(red: 1.000, green: 0.878, blue: 0.400).opacity(0.4),
        boatHull: Color(red: 0.361, green: 0.290, blue: 0.447),
        boatSail: Color(red: 1.000, green: 0.961, blue: 0.902)
    )

    static let day = SailPalette(
        skyTop: Color(red: 0.537, green: 0.812, blue: 0.941),
        skyMid: Color(red: 0.365, green: 0.678, blue: 0.886),
        skyBottom: Color(red: 0.682, green: 0.839, blue: 0.945),
        waterSurface: Color(red: 0.180, green: 0.525, blue: 0.757),
        waterMid: Color(red: 0.106, green: 0.310, blue: 0.447),
        waterDeep: Color(red: 0.082, green: 0.263, blue: 0.376),
        celestialBody: Color(red: 1.000, green: 0.918, blue: 0.655),
        celestialGlow: Color(red: 1.000, green: 0.945, blue: 0.463).opacity(0.2),
        celestialType: "sun",
        textPrimary: Color(red: 0.055, green: 0.184, blue: 0.267),
        textSecondary: Color(red: 0.102, green: 0.227, blue: 0.290).opacity(0.45),
        uiRing: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.9),
        uiRingBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.15),
        uiButtonBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.2),
        uiButtonActive: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.4),
        boatHull: Color(red: 0.173, green: 0.243, blue: 0.314),
        boatSail: Color(red: 1.000, green: 1.000, blue: 1.000)
    )

    static let dusk = SailPalette(
        skyTop: Color(red: 1.000, green: 0.420, blue: 0.420),
        skyMid: Color(red: 0.933, green: 0.353, blue: 0.141),
        skyBottom: Color(red: 0.882, green: 0.439, blue: 0.333),
        waterSurface: Color(red: 0.424, green: 0.361, blue: 0.906),
        waterMid: Color(red: 0.204, green: 0.122, blue: 0.592),
        waterDeep: Color(red: 0.118, green: 0.039, blue: 0.235),
        celestialBody: Color(red: 1.000, green: 0.745, blue: 0.463),
        celestialGlow: Color(red: 1.000, green: 0.745, blue: 0.463).opacity(0.3),
        celestialType: "sun",
        textPrimary: Color(red: 0.973, green: 0.910, blue: 0.816),
        textSecondary: Color(red: 0.973, green: 0.910, blue: 0.816).opacity(0.5),
        uiRing: Color(red: 1.000, green: 0.745, blue: 0.463).opacity(0.85),
        uiRingBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.1),
        uiButtonBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.12),
        uiButtonActive: Color(red: 1.000, green: 0.745, blue: 0.463).opacity(0.35),
        boatHull: Color(red: 0.176, green: 0.106, blue: 0.306),
        boatSail: Color(red: 1.000, green: 0.918, blue: 0.655)
    )

    static let night = SailPalette(
        skyTop: Color(red: 0.047, green: 0.078, blue: 0.271),
        skyMid: Color(red: 0.078, green: 0.118, blue: 0.380),
        skyBottom: Color(red: 0.008, green: 0.008, blue: 0.031),
        waterSurface: Color(red: 0.008, green: 0.008, blue: 0.031),
        waterMid: Color(red: 0.039, green: 0.039, blue: 0.180),
        waterDeep: Color(red: 0.020, green: 0.020, blue: 0.082),
        celestialBody: Color(red: 0.788, green: 0.839, blue: 1.000),
        celestialGlow: Color(red: 0.788, green: 0.839, blue: 1.000).opacity(0.08),
        celestialType: "moon",
        textPrimary: Color(red: 0.788, green: 0.839, blue: 1.000),
        textSecondary: Color(red: 0.788, green: 0.839, blue: 1.000).opacity(0.35),
        uiRing: Color(red: 0.788, green: 0.839, blue: 1.000).opacity(0.7),
        uiRingBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.06),
        uiButtonBackground: Color(red: 1.000, green: 1.000, blue: 1.000).opacity(0.06),
        uiButtonActive: Color(red: 0.788, green: 0.839, blue: 1.000).opacity(0.25),
        boatHull: Color(red: 0.533, green: 0.573, blue: 0.690),
        boatSail: Color(red: 0.788, green: 0.839, blue: 1.000)
    )
}
