# 0130_lung_jr_pedsptxx

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (leftmost, ~5%)
**Observations:** Dense parallel horizontal lines occupy the top half (chest wall). A distinct bright pleural line is visible. Below it the zone transitions to a uniformly dark, largely signal-free region with minimal echo texture.
**Classification: SEASHORE** — absence of continuing horizontal lines below pleural line; the dark zone is consistent with the "sea" (lung tissue); subtle granular noise visible.

---

### p01 (~15%)
**Observations:** Clear parallel lines above; bright pleural line showing slight waviness. The lower portion remains dark but shows faint columnar brighter patches (granular noise clusters).
**Classification: SEASHORE** — columnar/sandy texture below pleural line; pleural line irregularity supports lung sliding.

---

### p02 (~25%)
**Observations:** Parallel lines above; pleural line visible with 2–3 bright A-line replications below it. Background texture between A-lines and deeper down shows a mottled/granular appearance; bright clumps at bottom corners.
**Classification: SEASHORE** — A-lines overlying a granular background; pleural line shows mild waviness consistent with sliding.

---

### p03 (~35%)
**Observations:** Fewer/wider-spaced lines above; multiple strong horizontal bright bands (A-lines) in the mid-zone; below the A-lines the background is distinctly granular/noisy with bright blobs present.
**Classification: SEASHORE** — granular sandy texture persists between and below A-lines; no continuous dense horizontal-line "barcode" below pleural line.

---

### p04 (~45%)
**Observations:** Parallel chest-wall lines at top; a wavy pleural line; multiple A-lines below it; the inter-A-line and sub-A-line background shows clear granular/sandy texture; pleural line curvature varies over time (horizontal axis).
**Classification: SEASHORE** — classic granular texture with A-lines; wavy pleural line confirms motion/sliding.

---

### p05 (~55%)
**Observations:** Similar to p04; horizontal lines above; A-lines below pleural line; pleural line shows an undulating contour; granular speckle texture fills the background throughout the lower zone.
**Classification: SEASHORE** — granular background predominates; A-lines ride on top of sandy texture.

---

### p06 (~65%)
**Observations:** Horizontal lines at top; complex mid-zone with multiple A-line bands; lower portion shows alternating brighter and darker horizontal swaths but background between bands retains mottled/granular character; two rounded bright patches visible at bottom corners (reverberation blobs over granular lung).
**Classification: SEASHORE** — granular background between A-lines confirmed; no true barcode pattern; the bright blobs suggest tissue-level echoes consistent with sliding lung.

---

### p07 (~75%)
**Observations:** Parallel lines at top; bright pleural line; mid-zone shows complex horizontal banding; a prominent bright white horizontal band appears in the lower portion (likely a strong A-line or deep reflector); below it the background is granular.
**Classification: SEASHORE** — granular texture below pleural line and around bright reflector; no continuous barcode throughout.

---

### p08 (~85%)
**Observations:** Clear horizontal lines at top (chest wall); clean, relatively straight-but-still-faintly-wavy bright pleural line; below it the zone is predominantly dark with scattered lighter granular patches in the lower third.
**Classification: SEASHORE** — transition to dark granular lower zone; lack of horizontal-line continuation below pleural line distinguishes this from stratosphere.

---

### p09 (rightmost, ~95%)
**Observations:** Only a single faint thin bright line at the very top; the remainder of the image is essentially black with no discernible structure.
**Classification: UNCLASSIFIABLE** — near-total absence of signal consistent with lateral edge of active ultrasound region; excluded from decision.

---

## Step 2 — Overall Decision

| Position | Classification |
|----------|---------------|
| p00 | Seashore ✓ |
| p01 | Seashore ✓ |
| p02 | Seashore ✓ |
| p03 | Seashore ✓ |
| p04 | Seashore ✓ |
| p05 | Seashore ✓ |
| p06 | Seashore ✓ |
| p07 | Seashore ✓ |
| p08 | Seashore ✓ |
| p09 | **Unclassifiable** |

**Classifiable positions: 9/9 → Seashore**
No stratosphere positions; no alternating (lung point) pattern detected.

## ✅ Overall Conclusion: **PRESENT**
**Pleural sliding is PRESENT** across all classifiable positions. The M-mode pattern consistently demonstrates the seashore sign: structured parallel lines above the pleural line (chest wall), a pleural line with time-varying waviness indicating motion, and a granular/sandy texture below — all features of normal lung sliding.
