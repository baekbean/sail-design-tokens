#!/usr/bin/env python3
"""
Sail Design System — Token → Swift Code Generator

Reads sail-tokens.json and generates type-safe Swift source files.
Run manually or integrate as an Xcode Build Phase:
  python3 scripts/generate_swift.py

Outputs:
  generated/SailColors.swift        — Color primitives + semantic palettes
  generated/SailTypography.swift    — Font styles
  generated/SailSpacing.swift       — Spacing, radius, sizing tokens
  generated/SailAnimation.swift     — Animation durations, easings, params
  generated/SailAssets.swift        — Icon & illustration registries
"""

import json
import re
import os
import sys
from datetime import datetime
from pathlib import Path

# ─── Config ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
TOKENS_PATH = ROOT_DIR / "tokens" / "sail-tokens.json"
OUTPUT_DIR = ROOT_DIR / "generated"

# ─── Helpers ─────────────────────────────────────────────────────────────────

def load_tokens() -> dict:
    with open(TOKENS_PATH, "r") as f:
        return json.load(f)


def header(filename: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""// ─────────────────────────────────────────────────
// {filename}
// Auto-generated from sail-tokens.json
// Generated: {now}
// DO NOT EDIT — re-run generate_swift.py instead
// ─────────────────────────────────────────────────

import SwiftUI
"""


def hex_to_rgb(hex_str: str) -> tuple:
    """Convert #RRGGBB to (r, g, b) floats."""
    h = hex_str.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def rgba_to_components(rgba_str: str) -> tuple:
    """Parse rgba(r,g,b,a) to (r,g,b,a) floats 0-1."""
    m = re.match(r"rgba?\((\d+),\s*(\d+),\s*(\d+),?\s*([\d.]*)\)", rgba_str)
    if not m:
        return None
    r, g, b = int(m.group(1))/255, int(m.group(2))/255, int(m.group(3))/255
    a = float(m.group(4)) if m.group(4) else 1.0
    return (r, g, b, a)


def color_expr(value: str) -> str:
    """Convert a color value string to a Swift Color expression."""
    if value.startswith("#"):
        r, g, b = hex_to_rgb(value)
        return f"Color(red: {r:.3f}, green: {g:.3f}, blue: {b:.3f})"
    rgba = rgba_to_components(value)
    if rgba:
        r, g, b, a = rgba
        return f"Color(red: {r:.3f}, green: {g:.3f}, blue: {b:.3f}).opacity({a})"
    return f'Color.clear /* unresolved: {value} */'


def resolve_ref(value: str, tokens: dict) -> str:
    """Resolve {global.color.ocean.200} style references."""
    if not isinstance(value, str) or not value.startswith("{"):
        return value
    path = value.strip("{}").split(".")
    node = tokens
    for key in path:
        if isinstance(node, dict):
            node = node.get(key)
        else:
            return value
    if isinstance(node, dict) and "$value" in node:
        return resolve_ref(node["$value"], tokens)
    return node if isinstance(node, str) else value


def px_to_cg(value: str) -> str:
    """Convert '12px' to '12' for CGFloat."""
    if isinstance(value, str):
        return value.replace("px", "").replace("ms", "")
    return str(value)


def ms_to_seconds(value) -> str:
    """Convert '500ms' or number to seconds string."""
    if isinstance(value, str) and "ms" in value:
        return f"{int(value.replace('ms', '')) / 1000.0}"
    if isinstance(value, (int, float)):
        return f"{value / 1000.0}" if value > 10 else str(value)
    return str(value)


def swift_name(s: str) -> str:
    """Convert kebab-case or numbers to camelCase."""
    parts = s.replace("-", "_").split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


# ─── Generator: Colors ──────────────────────────────────────────────────────

def generate_colors(tokens: dict) -> str:
    out = header("SailColors.swift")

    # --- Primitives ---
    out += "\n// MARK: - Color Primitives\n\n"
    out += "extension Color {\n    enum Sail {\n"

    color_groups = tokens["global"]["color"]
    for group_name, group in color_groups.items():
        if group_name.startswith("$"):
            continue
        if isinstance(group, dict) and "$value" in group:
            # Simple color (white, black)
            val = resolve_ref(group["$value"], tokens)
            out += f"        static let {swift_name(group_name)} = {color_expr(val)}\n"
        elif isinstance(group, dict):
            # Color scale
            out += f"\n        enum {swift_name(group_name).capitalize()} {{\n"
            for shade, shade_val in group.items():
                if shade.startswith("$"):
                    continue
                val = resolve_ref(shade_val["$value"], tokens)
                name = f"s{shade}" if shade[0].isdigit() else swift_name(shade)
                out += f"            static let {name} = {color_expr(val)}\n"
            out += "        }\n"

    out += "    }\n}\n"

    # --- Semantic Palettes ---
    out += "\n// MARK: - Semantic Palette\n\n"
    out += """struct SailPalette {
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

"""
    out += "extension SailPalette {\n"
    themes = tokens.get("theme", {})
    for theme_name, theme in themes.items():
        if theme_name.startswith("$"):
            continue
        out += f"\n    static let {swift_name(theme_name)} = SailPalette(\n"

        def rv(path_parts):
            node = theme
            for p in path_parts:
                node = node.get(p, {})
            val = node.get("$value", "")
            resolved = resolve_ref(val, tokens)
            return resolved

        sky = theme.get("sky", {})
        water = theme.get("water", {})
        cel = theme.get("celestial", {})
        text = theme.get("text", {})
        ui = theme.get("ui", {})
        boat = theme.get("boat", {})

        out += f"        skyTop: {color_expr(resolve_ref(sky['top']['$value'], tokens))},\n"
        out += f"        skyMid: {color_expr(resolve_ref(sky['mid']['$value'], tokens))},\n"
        out += f"        skyBottom: {color_expr(resolve_ref(sky['bottom']['$value'], tokens))},\n"
        out += f"        waterSurface: {color_expr(resolve_ref(water['surface']['$value'], tokens))},\n"
        out += f"        waterMid: {color_expr(resolve_ref(water['mid']['$value'], tokens))},\n"
        out += f"        waterDeep: {color_expr(resolve_ref(water['deep']['$value'], tokens))},\n"
        out += f"        celestialBody: {color_expr(resolve_ref(cel['body']['$value'], tokens))},\n"
        out += f"        celestialGlow: {color_expr(resolve_ref(cel['glow']['$value'], tokens))},\n"
        out += f"        celestialType: \"{cel['type']['$value']}\",\n"
        out += f"        textPrimary: {color_expr(resolve_ref(text['primary']['$value'], tokens))},\n"
        out += f"        textSecondary: {color_expr(resolve_ref(text['secondary']['$value'], tokens))},\n"
        out += f"        uiRing: {color_expr(resolve_ref(ui['ring']['$value'], tokens))},\n"
        out += f"        uiRingBackground: {color_expr(resolve_ref(ui['ringBackground']['$value'], tokens))},\n"
        out += f"        uiButtonBackground: {color_expr(resolve_ref(ui['buttonBackground']['$value'], tokens))},\n"
        out += f"        uiButtonActive: {color_expr(resolve_ref(ui['buttonActive']['$value'], tokens))},\n"
        out += f"        boatHull: {color_expr(resolve_ref(boat['hull']['$value'], tokens))},\n"
        out += f"        boatSail: {color_expr(resolve_ref(boat['sail']['$value'], tokens))}\n"
        out += "    )\n"

    out += "}\n"

    return out


# ─── Generator: Typography ───────────────────────────────────────────────────

def generate_typography(tokens: dict) -> str:
    out = header("SailTypography.swift")
    typo = tokens.get("typography", {})

    # Font families
    out += "\n// MARK: - Font Families\n\n"
    out += "enum SailFont {\n"
    for name, val in typo.get("fontFamily", {}).items():
        if name.startswith("$"):
            continue
        out += f"    static let {swift_name(name)} = \"{val['$value']}\"\n"
    out += "}\n"

    # Font weights
    out += "\n// MARK: - Font Weights\n\n"
    out += "extension Font.Weight {\n"
    for name, val in typo.get("fontWeight", {}).items():
        if name.startswith("$"):
            continue
        w = val["$value"]
        swift_w = {300: ".light", 400: ".regular", 500: ".medium"}.get(w, ".regular")
        out += f"    static let sail{name.capitalize()} = Font.Weight{swift_w}\n"
    out += "}\n"

    # Font sizes
    out += "\n// MARK: - Font Sizes\n\n"
    out += "enum SailFontSize {\n"
    for name, val in typo.get("fontSize", {}).items():
        if name.startswith("$"):
            continue
        size = px_to_cg(val["$value"])
        out += f"    static let {swift_name(name)}: CGFloat = {size}\n"
    out += "}\n"

    # Letter spacing
    out += "\n// MARK: - Letter Spacing\n\n"
    out += "enum SailLetterSpacing {\n"
    for name, val in typo.get("letterSpacing", {}).items():
        if name.startswith("$"):
            continue
        sp = px_to_cg(val["$value"])
        out += f"    static let {swift_name(name)}: CGFloat = {sp}\n"
    out += "}\n"

    # Composite styles
    out += "\n// MARK: - Text Styles\n\n"
    out += """struct SailTextStyle {
    let fontFamily: String
    let fontWeight: Font.Weight
    let fontSize: CGFloat
    let letterSpacing: CGFloat
    let lineHeight: CGFloat

    var font: Font {
        .custom(fontFamily, size: fontSize).weight(fontWeight)
    }
}

"""
    out += "extension SailTextStyle {\n"
    composites = typo.get("composite", {})
    for name, val in composites.items():
        if name.startswith("$"):
            continue
        comp = val["$value"]

        # Resolve references
        ff_ref = comp.get("fontFamily", "")
        fw_ref = comp.get("fontWeight", "")
        fs_ref = comp.get("fontSize", "")
        ls_ref = comp.get("letterSpacing", "0px")
        lh_ref = comp.get("lineHeight", "1.5")

        def resolve_typo(ref, section):
            if isinstance(ref, str) and ref.startswith("{"):
                path = ref.strip("{}").split(".")
                node = tokens
                for p in path:
                    node = node.get(p, {})
                return node.get("$value", ref)
            return ref

        ff = resolve_typo(ff_ref, "fontFamily")
        fw = resolve_typo(fw_ref, "fontWeight")
        fs = px_to_cg(str(resolve_typo(fs_ref, "fontSize")))
        ls = px_to_cg(str(resolve_typo(ls_ref, "letterSpacing")))
        lh = resolve_typo(lh_ref, "lineHeight")
        if isinstance(lh, str):
            lh = px_to_cg(lh)

        fw_swift = {300: ".light", 400: ".regular", 500: ".medium"}.get(fw, ".regular")

        out += f"\n    static let {swift_name(name)} = SailTextStyle(\n"
        out += f"        fontFamily: \"{ff}\",\n"
        out += f"        fontWeight: {fw_swift},\n"
        out += f"        fontSize: {fs},\n"
        out += f"        letterSpacing: {ls},\n"
        out += f"        lineHeight: {lh}\n"
        out += "    )\n"

    out += "}\n"

    return out


# ─── Generator: Spacing ─────────────────────────────────────────────────────

def generate_spacing(tokens: dict) -> str:
    out = header("SailSpacing.swift")

    # Spacing
    out += "\n// MARK: - Spacing\n\n"
    out += "enum SailSpacing {\n"
    for name, val in tokens.get("spacing", {}).items():
        if name.startswith("$"):
            continue
        out += f"    static let {swift_name(name)}: CGFloat = {px_to_cg(val['$value'])}\n"
    out += "}\n"

    # Radius
    out += "\n// MARK: - Border Radius\n\n"
    out += "enum SailRadius {\n"
    for name, val in tokens.get("radius", {}).items():
        if name.startswith("$"):
            continue
        v = val["$value"]
        if v == "50%":
            out += f"    // {swift_name(name)}: use .clipShape(Circle())\n"
        elif v == "9999px":
            out += f"    static let {swift_name(name)}: CGFloat = .infinity\n"
        else:
            out += f"    static let {swift_name(name)}: CGFloat = {px_to_cg(v)}\n"
    out += "}\n"

    # Sizing
    out += "\n// MARK: - Component Sizing\n\n"
    out += "enum SailSize {\n"
    for name, val in tokens.get("sizing", {}).items():
        if name.startswith("$"):
            continue
        out += f"    static let {swift_name(name)}: CGFloat = {px_to_cg(val['$value'])}\n"
    out += "}\n"

    return out


# ─── Generator: Animation ───────────────────────────────────────────────────

def generate_animation(tokens: dict) -> str:
    out = header("SailAnimation.swift")
    anim = tokens.get("animation", {})

    # Durations
    out += "\n// MARK: - Durations\n\n"
    out += "enum SailDuration {\n"
    for name, val in anim.get("duration", {}).items():
        if name.startswith("$"):
            continue
        out += f"    static let {swift_name(name)}: Double = {ms_to_seconds(val['$value'])}\n"
    out += "}\n"

    # Boat animation
    out += "\n// MARK: - Boat Animation\n\n"
    out += "enum SailBoatAnimation {\n"
    boat = anim.get("boat", {})
    for name, val in boat.items():
        if name.startswith("$"):
            continue
        v = val["$value"]
        if isinstance(v, str) and "ms" in v:
            out += f"    static let {swift_name(name)}: Double = {ms_to_seconds(v)}\n"
        elif isinstance(v, str) and "px" in v:
            out += f"    static let {swift_name(name)}: CGFloat = {px_to_cg(v)}\n"
        else:
            out += f"    static let {swift_name(name)}: Double = {v}\n"
    out += "}\n"

    # Wave layers
    out += "\n// MARK: - Wave Animation\n\n"
    out += """struct SailWaveParams {
    let amplitude: CGFloat
    let frequency: CGFloat
    let speed: Double
    let opacity: Double
    let yOffset: CGFloat
}

"""
    out += "enum SailWaveAnimation {\n"
    wave = anim.get("wave", {})
    for layer_name, layer in wave.items():
        if layer_name.startswith("$"):
            continue
        amp = layer["amplitude"]["$value"]
        freq = layer["frequency"]["$value"]
        speed = ms_to_seconds(layer["speed"]["$value"])
        opac = layer["opacity"]["$value"]
        yoff = layer["yOffset"]["$value"]
        out += f"\n    static let {swift_name(layer_name)} = SailWaveParams(\n"
        out += f"        amplitude: {amp},\n"
        out += f"        frequency: {freq},\n"
        out += f"        speed: {speed},\n"
        out += f"        opacity: {opac},\n"
        out += f"        yOffset: {yoff}\n"
        out += "    )\n"
    out += "\n    static let allLayers: [SailWaveParams] = [layer0, layer1, layer2]\n"
    out += "}\n"

    # Star animation
    out += "\n// MARK: - Star Animation\n\n"
    out += "enum SailStarAnimation {\n"
    star = anim.get("star", {})
    for name, val in star.items():
        if name.startswith("$"):
            continue
        v = val["$value"]
        if isinstance(v, str) and "ms" in v:
            out += f"    static let {swift_name(name)}: Double = {ms_to_seconds(v)}\n"
        else:
            out += f"    static let {swift_name(name)}: Double = {v}\n"
    out += "}\n"

    # Transition durations
    out += "\n// MARK: - Transitions\n\n"
    out += "enum SailTransition {\n"
    trans = anim.get("transition", {})
    for name, val in trans.items():
        if name.startswith("$"):
            continue
        out += f"    static let {swift_name(name)}: Double = {ms_to_seconds(val['$value'])}\n"
    out += "}\n"

    return out


# ─── Generator: Assets ──────────────────────────────────────────────────────

def generate_assets(tokens: dict) -> str:
    out = header("SailAssets.swift")

    # Icons
    out += "\n// MARK: - Icons\n\n"
    out += "/// Icon registry — matches token definitions to asset catalog names.\n"
    out += "/// Add SVG files to Assets.xcassets and reference by these names.\n"
    out += "enum SailIcon: String, CaseIterable {\n"
    icons = tokens.get("icons", {})
    for name, val in icons.items():
        if name.startswith("$"):
            continue
        usage = val.get("usage", "")
        out += f"    /// {usage}\n"
        out += f"    case {swift_name(name)} = \"icon.{name}\"\n"
    out += "\n    var image: Image { Image(rawValue) }\n"
    out += "\n    var sizes: [Int] {\n        switch self {\n"
    for name, val in icons.items():
        if name.startswith("$"):
            continue
        sizes = val.get("sizes", [])
        sizes_str = ", ".join(str(s) for s in sizes)
        out += f"        case .{swift_name(name)}: return [{sizes_str}]\n"
    out += "        }\n    }\n"
    out += "}\n"

    # Illustrations
    out += "\n// MARK: - Illustrations\n\n"
    out += "enum SailIllustration: String, CaseIterable {\n"
    illus = tokens.get("illustrations", {})
    for name, val in illus.items():
        if name.startswith("$"):
            continue
        usage = val.get("usage", "")
        out += f"    /// {usage}\n"
        out += f"    case {swift_name(name)} = \"illust.{name}\"\n"
    out += "\n    var image: Image { Image(rawValue) }\n"
    out += "}\n"

    # Sound
    out += "\n// MARK: - Sound Assets\n\n"
    out += """struct SailSoundAsset {
    let resourceName: String
    let fileExtension: String
    let isLoop: Bool
    let fadeIn: Double
    let fadeOut: Double
    let defaultVolume: Float
}

"""
    out += "enum SailSound {\n"
    sounds = tokens.get("sound", {})
    for name, val in sounds.items():
        if name.startswith("$"):
            continue
        source = val.get("source", "")
        fname = source.split("/")[-1]
        rname = fname.rsplit(".", 1)[0] if "." in fname else fname
        ext = fname.rsplit(".", 1)[1] if "." in fname else "mp3"
        loop = str(val.get("loop", False)).lower()
        fade_in = ms_to_seconds(val.get("fadeIn", "0ms"))
        fade_out = ms_to_seconds(val.get("fadeOut", "0ms"))
        vol = val.get("defaultVolume", 1.0)

        out += f"\n    static let {swift_name(name)} = SailSoundAsset(\n"
        out += f"        resourceName: \"{rname}\",\n"
        out += f"        fileExtension: \"{ext}\",\n"
        out += f"        isLoop: {loop},\n"
        out += f"        fadeIn: {fade_in},\n"
        out += f"        fadeOut: {fade_out},\n"
        out += f"        defaultVolume: {vol}\n"
        out += "    )\n"
    out += "}\n"

    return out


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print(f"📐 Loading tokens from {TOKENS_PATH}")
    tokens = load_tokens()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generators = {
        "SailColors.swift": generate_colors,
        "SailTypography.swift": generate_typography,
        "SailSpacing.swift": generate_spacing,
        "SailAnimation.swift": generate_animation,
        "SailAssets.swift": generate_assets,
    }

    for filename, gen_fn in generators.items():
        path = OUTPUT_DIR / filename
        content = gen_fn(tokens)
        with open(path, "w") as f:
            f.write(content)
        line_count = content.count("\n")
        print(f"  ✅ {filename} ({line_count} lines)")

    print(f"\n🎉 Generated {len(generators)} files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
