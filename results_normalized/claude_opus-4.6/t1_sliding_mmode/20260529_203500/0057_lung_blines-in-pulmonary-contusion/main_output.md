# 0057_lung_blines-in-pulmonary-contusion

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00 (leftmost ~5%):** Upper portion is predominantly dark, but visible bright areas show clear granular/sandy texture in vertical columns. Below the indistinct pleural line, texture is speckled and granular.
→ **Seashore**

**p01 (~15%):** Bright columns with clear granular/sandy texture throughout the below-pleural region. Dark vertical gaps between columns, but the textured areas are distinctly granular.
→ **Seashore**

**p02 (~25%):** Rounded, irregular tops on bright columns (indicating pleural motion). Below, clear granular/sandy texture fills the image. No organized horizontal lines below the pleural line.
→ **Seashore**

**p03 (~35%):** Granular texture dominates below the pleural line. Pleural line appears irregular/wavy. Sandy background pattern is clearly visible.
→ **Seashore**

**p04 (~45%):** Horizontal layering above the pleural line (normal). Below, granular texture persists though mixed with some horizontal elements. Background between any lines remains sandy/textured.
→ **Seashore**

**p05 (~55%):** Similar to p04. Horizontal lines above pleural line; below, granular texture still identifiable. Background is not purely composed of continuous parallel lines.
→ **Seashore**

**p06 (~65%):** Bright, wavy/irregular pleural line visible. Below it, granular texture with some vertical structures. The pleural line irregularity supports sliding.
→ **Seashore**

**p07 (~75%):** Granular texture visible in left/center areas. Some horizontal elements present but interspersed with sandy texture. Not dominated by continuous parallel lines.
→ **Seashore**

**p08 (~85%):** Dark upper region, but the mid-to-lower portion displays granular/sandy texture. Sufficient signal to classify.
→ **Seashore**

**p09 (rightmost ~95%):** Prominent, thick, evenly-spaced horizontal black bands dominate the entire image. This appears to be a scanning/extraction artifact at the edge of the active ultrasound region rather than genuine tissue pattern.
→ **Unclassifiable**

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

All 9 classifiable positions show **seashore** pattern (granular/sandy texture below the pleural line, with irregular/wavy pleural lines indicating motion). No positions show stratosphere or alternating patterns.

**Overall Label: PRESENT** (pleural sliding is present)
