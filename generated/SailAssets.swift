// ─────────────────────────────────────────────────
// SailAssets.swift
// Auto-generated from sail-tokens.json
// Generated: 2026-02-16 14:53
// DO NOT EDIT — re-run generate_swift.py instead
// ─────────────────────────────────────────────────

import SwiftUI

// MARK: - Icons

/// Icon registry — matches token definitions to asset catalog names.
/// Add SVG files to Assets.xcassets and reference by these names.
enum SailIcon: String, CaseIterable {
    /// Main boat illustration in ocean scene
    case sailboat = "icon.sailboat"
    /// Decorative wave icon
    case wave = "icon.wave"
    /// Celestial body for dawn/day/dusk
    case sun = "icon.sun"
    /// Celestial body for night
    case moon = "icon.moon"
    /// Session stop action
    case stop = "icon.stop"
    /// Alternative sail/start icon
    case play = "icon.play"

    var image: Image { Image(rawValue) }

    var sizes: [Int] {
        switch self {
        case .sailboat: return [24, 32, 64]
        case .wave: return [24]
        case .sun: return [24, 44]
        case .moon: return [24, 28]
        case .stop: return [16, 24]
        case .play: return [16, 24]
        }
    }
}

// MARK: - Illustrations

enum SailIllustration: String, CaseIterable {
    /// Full ocean scene with boat (if using pre-rendered approach)
    case boatScene = "illust.boatScene"
    /// App icon — exported to AppIcon.appiconset
    case appIcon = "illust.appIcon"
    /// Launch screen background
    case launchImage = "illust.launchImage"

    var image: Image { Image(rawValue) }
}

// MARK: - Sound Assets

struct SailSoundAsset {
    let resourceName: String
    let fileExtension: String
    let isLoop: Bool
    let fadeIn: Double
    let fadeOut: Double
    let defaultVolume: Float
}

enum SailSound {

    static let waveLoop = SailSoundAsset(
        resourceName: "wave_loop",
        fileExtension: "mp3",
        isLoop: true,
        fadeIn: 1.5,
        fadeOut: 1.0,
        defaultVolume: 0.4
    )

    static let endChime = SailSoundAsset(
        resourceName: "end_chime",
        fileExtension: "mp3",
        isLoop: false,
        fadeIn: 0.0,
        fadeOut: 0.0,
        defaultVolume: 0.5
    )
}
