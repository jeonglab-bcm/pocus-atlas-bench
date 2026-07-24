# 0057_lung_blines-in-pulmonary-contusion

# M-mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00 (leftmost, ~5%):**
Upper and left portions are predominantly dark (edge of active region). The visible bright areas show granular, speckled texture. Some dark vertical gaps separate textured columns.
→ **Seashore** (granular texture clearly visible in active portions)

**p01 (~15%):**
More structure visible. Bright textured columns with clear granular/sandy pattern. No continuous horizontal lines dominating below the pleural region.
→ **Seashore**

**p02 (~25%):**
Well-filled image with granular texture throughout. Rounded bright structures at the top of columns (dome-like pleural line). Sandy/speckled texture below.
→ **Seashore**

**p03 (~35%):**
Granular texture throughout visible areas. Some brighter patches but no smooth, continuous horizontal lines below the pleural zone. Pleural line appears slightly irregular.
→ **Seashore**

**p04 (~45%):**
Horizontal layering visible in the upper portion (chest wall). Below a bright band (pleural line), texture is still predominantly granular with some A-line reverberations. Background between A-lines remains sandy.
→ **Seashore** (with A-lines)

**p05 (~55%):**
Similar to p04. Horizontal lines in chest wall region; below the pleural line, granular texture persists between visible A-lines. Not purely horizontal lines throughout.
→ **Seashore** (with A-lines)

**p06 (~65%):**
Bright, slightly wavy/irregular pleural line visible. Below: granular texture with some vertical bright structures. The waviness of the pleural line supports motion (sliding).
→ **Seashore**

**p07 (~75%):**
Upper portion darker; lower portion shows granular speckled texture. A bright vertical stripe on the right. Underlying texture remains sandy/granular.
→ **Seashore**

**p08 (~85%):**
Upper portion dark. Lower visible portion shows granular texture though signal is weaker. Still identifiable sandy pattern.
→ **Seashore** (borderline)

**p09 (rightmost, ~95%):**
Extremely prominent, thick, evenly-spaced horizontal black bands spanning the entire image. These are too regular and uniform — consistent with edge/dropout artifacts rather than genuine tissue patterns. Underlying texture between bands shows some granularity.
→ **Unclassifiable** (edge artifacts)

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | Unclassifiable |

## Overall Decision

9 out of 9 classifiable positions show **seashore pattern** (granular/sandy texture below the pleural line, with irregular/wavy pleural lines supporting motion).

**Overall Label: PRESENT** (pleural sliding is present)
