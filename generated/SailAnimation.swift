// ─────────────────────────────────────────────────
// SailAnimation.swift
// Auto-generated from sail-tokens.json
// Generated: 2026-02-16 14:53
// DO NOT EDIT — re-run generate_swift.py instead
// ─────────────────────────────────────────────────

import SwiftUI

// MARK: - Durations

enum SailDuration {
    static let instant: Double = 0.1
    static let fast: Double = 0.25
    static let normal: Double = 0.5
    static let slow: Double = 0.6
    static let slower: Double = 0.8
    static let entrance: Double = 1.2
}

// MARK: - Boat Animation

enum SailBoatAnimation {
    static let bobDuration: Double = 3.5
    static let bobDistance: CGFloat = -8
    static let rotationDegree: Double = 2.5
    static let rotationDuration: Double = 4.0
}

// MARK: - Wave Animation

struct SailWaveParams {
    let amplitude: CGFloat
    let frequency: CGFloat
    let speed: Double
    let opacity: Double
    let yOffset: CGFloat
}

enum SailWaveAnimation {

    static let layer0 = SailWaveParams(
        amplitude: 8,
        frequency: 1.5,
        speed: 8.0,
        opacity: 0.35,
        yOffset: 0.2
    )

    static let layer1 = SailWaveParams(
        amplitude: 6,
        frequency: 2.0,
        speed: 6.0,
        opacity: 0.55,
        yOffset: 0.35
    )

    static let layer2 = SailWaveParams(
        amplitude: 5,
        frequency: 2.5,
        speed: 5.0,
        opacity: 0.85,
        yOffset: 0.45
    )

    static let allLayers: [SailWaveParams] = [layer0, layer1, layer2]
}

// MARK: - Star Animation

enum SailStarAnimation {
    static let minDuration: Double = 2.0
    static let maxDuration: Double = 4.0
    static let minOpacity: Double = 0.3
    static let maxOpacity: Double = 1.0
}

// MARK: - Transitions

enum SailTransition {
    static let screenFade: Double = 0.5
    static let ringAppear: Double = 1.0
    static let phraseEntrance: Double = 1.2
}
