# Sail Design System

JSON 토큰 기반 디자인 시스템. `sail-tokens.json` 하나를 수정하면 Swift 코드가 자동 생성됩니다.

## 구조

```
SailDesignSystem/
├── tokens/
│   └── sail-tokens.json        ← 이 파일만 수정하면 됨 (single source of truth)
├── scripts/
│   └── generate_swift.py       ← 토큰 → Swift 코드 변환기
├── generated/                  ← 자동 생성된 Swift 파일 (직접 수정 금지)
│   ├── SailColors.swift        — 컬러 프리미티브 + 시맨틱 팔레트 (dawn/day/dusk/night)
│   ├── SailTypography.swift    — 폰트 패밀리, 사이즈, 웨이트, 합성 스타일
│   ├── SailSpacing.swift       — 스페이싱, 라디우스, 컴포넌트 사이징
│   ├── SailAnimation.swift     — 듀레이션, 보트/파도/별 애니메이션 파라미터
│   └── SailAssets.swift        — 아이콘, 일러스트, 사운드 에셋 레지스트리
├── icons/                      ← SVG 아이콘 원본 (sailboat, wave, sun, moon 등)
└── illustrations/              ← SVG/PNG 일러스트 원본 (앱아이콘, 씬 등)
```

## 사용법

### 1. 토큰 수정

`tokens/sail-tokens.json`을 열어서 원하는 값을 변경합니다.

**컬러 변경 예시:**
```json
"ocean": {
  "400": { "$value": "#2E86C1" }   ← 이 값을 바꾸면
}
```

**애니메이션 조정 예시:**
```json
"boat": {
  "bobDuration": { "$value": "3500ms" },   ← 보트 흔들림 속도
  "bobDistance": { "$value": "-8px" }       ← 보트 흔들림 거리
}
```

**새 아이콘 추가 예시:**
```json
"icons": {
  "anchor": {
    "source": "icons/anchor.svg",
    "sizes": ["24", "32"],
    "usage": "Harbor mode icon"
  }
}
```

### 2. Swift 코드 생성

```bash
python3 scripts/generate_swift.py
```

### 3. Xcode 프로젝트에 적용

`generated/` 폴더의 Swift 파일들을 Xcode 프로젝트에 추가합니다.

**첫 설정:**
1. `generated/` 폴더를 Xcode에 그룹으로 추가
2. 기존 `ThemeManager.swift`의 `OceanPalette`를 `SailPalette`로 교체
3. 뷰에서 생성된 토큰 사용

**이후 수정:**
1. `sail-tokens.json` 수정
2. `python3 scripts/generate_swift.py` 실행
3. Xcode가 자동으로 변경 감지 → 빌드

### 4. Xcode Build Phase로 자동화 (권장)

Xcode에서 빌드할 때마다 자동으로 코드 생성:

1. Xcode → 프로젝트 타겟 → **Build Phases**
2. **+** → **New Run Script Phase**
3. "Compile Sources" 위로 드래그
4. 스크립트 입력:
```bash
cd "${SRCROOT}/SailDesignSystem"
python3 scripts/generate_swift.py
```

## 토큰 카테고리

| 카테고리 | 토큰 수 | 설명 |
|---------|--------|------|
| **global.color** | 5개 스케일 × 10단계 | 컬러 프리미티브 (ocean, sunset, twilight, dawn, night) |
| **theme** | 4개 테마 × 17속성 | 시맨틱 팔레트 (dawn, day, dusk, night) |
| **typography** | 7개 합성 스타일 | appTitle, timer, phrase, button, pill, label, subtitle |
| **spacing** | 13단계 | xxs(4) ~ 8xl(80) |
| **animation** | 보트/파도/별/전환 | 모든 모션 파라미터 |
| **icons** | 6개 | sailboat, wave, sun, moon, stop, play |
| **illustrations** | 3개 | boatScene, appIcon, launchImage |
| **sound** | 2개 | waveLoop, endChime |

## Figma Token Studio 연동

`sail-tokens.json`은 [Figma Token Studio](https://tokens.studio/) 포맷과 호환됩니다.

1. Figma에서 Token Studio 플러그인 설치
2. **Settings → Add new → URL/JSON**으로 이 JSON 연결
3. Figma에서 수정 → JSON 동기화 → `generate_swift.py` 실행

`$value` + `$type` + `{}` 레퍼런스 문법이 Token Studio의 DTCG 스펙을 따릅니다.

## 생성된 코드 사용 예시

```swift
// 컬러 프리미티브
let blue = Color.Sail.Ocean.s400

// 시맨틱 팔레트 (시간대별)
let palette = SailPalette.dusk
view.foregroundColor(palette.textPrimary)

// 타이포그래피
Text("Sail")
    .font(SailTextStyle.appTitle.font)
    .tracking(SailTextStyle.appTitle.letterSpacing)

// 스페이싱
.padding(.bottom, SailSpacing.xl5)

// 애니메이션
withAnimation(.easeInOut(duration: SailBoatAnimation.bobDuration)
    .repeatForever(autoreverses: true)) {
    offset = SailBoatAnimation.bobDistance
}

// 파도 레이어 (데이터 드리븐)
ForEach(Array(SailWaveAnimation.allLayers.enumerated()), id: \.offset) { _, params in
    WaveLayerView(params: params, color: palette.waterSurface)
}

// 아이콘
SailIcon.sailboat.image
    .resizable()

// 사운드
let asset = SailSound.waveLoop
player.volume = asset.defaultVolume
```
