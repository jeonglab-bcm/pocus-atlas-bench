# 0017_lung_lung-point2

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (~5% lateral)
**Observations:** Bright horizontal parallel bands in the upper ~40%. Bright white pleural line present. Below the pleural line: predominantly dark lower region, but the transition zone shows irregular/bumpy texture immediately sub-pleural; the pleural line boundary itself appears noticeably **wavy and non-smooth**.
**Classification: Seashore** — wavy pleural line + irregular sub-pleural texture indicates motion/sliding.

---

### p01 (~16%)
**Observations:** Clear horizontal bands above. Below the pleural line: more visible sub-pleural structure than p00, with scattered brighter foci creating a heterogeneous, slightly granular-appearing texture. Pleural line shows mild irregularity.
**Classification: Seashore** — granular/heterogeneous sub-pleural texture.

---

### p02 (~27%)
**Observations:** Horizontal parallel bands above. Below the pleural line: **pronounced alternating bright/dark vertical columnar modulation** throughout the sub-pleural zone. This represents time-varying depth changes — a classic marker of lung motion producing sandy texture. NOT continuous horizontal lines.
**Classification: Seashore** — clear granular/sandy texture with strong sub-pleural activity.

---

### p03 (~38%)
**Observations:** Horizontal parallel bands above. Below the pleural line: **most prominent vertical columnar banding** of all 10 strips, with clearly defined bright columns interspersed with dark regions across the full lower field. Pleural line transition is clearly non-smooth.
**Classification: Seashore** — strongest granular texture; most convincing sliding pattern.

---

### p04 (~49%)
**Observations:** Horizontal parallel bands above. Below the pleural line: visible texture and horizontal-ish banding but with residual vertical modulation and variability — NOT the continuous, uniform, dense horizontal lines required for stratosphere. The sub-pleural zone retains some granularity, though subdued compared to p02/p03.
**Classification: Seashore** — retained granularity below; not dense barcode pattern.

---

### p05 (~60%)
**Observations:** Clear horizontal bands above, including a very bright double-band appearance (pleural line + A-line). Below: predominantly dark with subtle horizontal elements. A-lines are present, but background between/below A-lines shows minimal dense parallel lines — not the packed continuous stratosphere appearance. A-lines over a quiet/dark background still falls within the seashore envelope per the stated caveat.
**Classification: Seashore** — A-line over dark/granular background; no dense barcode below.

---

### p06 (~71%)
**Observations:** Bright horizontal bands occupy only the upper ~25% of the strip. The lower ~75% is **nearly black** with minimal discernible structure — insufficient signal to reliably evaluate sub-pleural texture.
**Classification: Unclassifiable** — near-black lower region, insufficient detail.

---

### p07 (~82%)
**Observations:** Bright bands confined to upper portion; lower field is **almost completely black** with negligible texture.
**Classification: Unclassifiable** — near-black; likely outside active beam.

---

### p08 (~88%)
**Observations:** Bright bands in upper portion only; lower field remains very dark with only faint noise-level horizontal texture.
**Classification: Unclassifiable** — near-black; insufficient signal.

---

### p09 (~95%)
**Observations:** Narrow bright band at top; rest of image is **uniformly near-black**. Rightmost edge position.
**Classification: Unclassifiable** — edge of active ultrasound region, near-black.

---

## Summary Table

| Position | ~Lateral % | Pattern | Classification |
|---|---|---|---|
| p00 | 5% | Wavy pleural line, irregular sub-pleural texture | **Seashore** |
| p01 | 16% | Granular sub-pleural heterogeneity | **Seashore** |
| p02 | 27% | Prominent vertical modulation = granularity | **Seashore** |
| p03 | 38% | Strongest granular/sandy texture | **Seashore** |
| p04 | 49% | Subdued but present granularity | **Seashore** |
| p05 | 60% | A-line + dark granular background | **Seashore** |
| p06 | 71% | Near-black | **Unclassifiable** |
| p07 | 82% | Near-black | **Unclassifiable** |
| p08 | 88% | Near-black | **Unclassifiable** |
| p09 | 95% | Near-black | **Unclassifiable** |

---

## Step 2 — Overall Decision

- **Classifiable positions:** p00–p05 (6 positions)
- **Seashore:** 6/6 classifiable positions
- **Stratosphere:** 0
- **Alternating:** 0
- No spatial seashore→stratosphere transition detected

> ## ✅ Overall Label: **PRESENT**
> Pleural sliding is **present**. All classifiable M-mode positions demonstrate the seashore sign (granular/sandy sub-pleural texture with non-smooth pleural line), indicating normal lung sliding throughout the assessable ultrasound region.
