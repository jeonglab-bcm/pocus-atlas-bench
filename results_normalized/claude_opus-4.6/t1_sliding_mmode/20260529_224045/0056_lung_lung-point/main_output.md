# 0056_lung_lung-point

# M-Mode Image Analysis

## Per-Position Classification

**p00 (leftmost, ~5%):**
Bright horizontal lines confined to the upper ~15%. Below: predominantly dark with scattered granular/speckled noise texture. No continuous horizontal lines extend into the lower portion. The texture below is sandy/noisy, not lined.
→ **Seashore**

**p01 (~15%):**
Similar structure — horizontal lines in upper ~20%, below which is a dark region with subtle granular texture visible throughout. Background is speckled, not composed of parallel lines.
→ **Seashore**

**p02 (~25%):**
Horizontal lines above (~15-20%). Below: clearly visible patchy, granular texture with brighter reflections scattered over a sandy background. Distinct contrast between upper (lines) and lower (granular) regions.
→ **Seashore**

**p03 (~35%):**
Horizontal lines in upper ~25-30%. Below: bright spots (A-lines) are visible, but the background between them shows granular/speckled texture rather than continuous lines.
→ **Seashore**

**p04 (~45%):**
Dense horizontal lines extending through 55-60% of the image. Below the pleural line, lines continue with minimal interruption. Very little granularity visible — dominated by continuous parallel lines.
→ **Stratosphere**

**p05 (~55%):**
Dense, continuous horizontal lines extending through ~65%+ of the image. Below the pleural line, the lines persist with no sandy/granular background. Classic barcode appearance.
→ **Stratosphere**

**p06 (~65%):**
Dense horizontal lines fill nearly the entire image. No discernible transition to granular texture below the pleural line. Continuous parallel lines throughout.
→ **Stratosphere**

**p07 (~75%):**
Dense horizontal parallel lines dominate the entire image top to bottom. No granular texture visible. Pure barcode/stratosphere pattern.
→ **Stratosphere**

**p08 (~85%):**
Bright horizontal lines in upper ~30-35%. Below: darker region with subtle texture but notably NO continuation of dense horizontal lines as seen in p04-p07. The lower portion appears more similar to the dark granular pattern seen at p00/p01.
→ **Seashore**

**p09 (~95%):**
Very bright horizontal lines in upper ~35-40%. Below: dark region with mild texture. Clear structural break between upper lined portion and lower portion. Does not show continuous lines extending throughout as in stratosphere.
→ **Seashore**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Stratosphere |
| p07 | Stratosphere |
| p08 | Seashore |
| p09 | Seashore |

## Overall Decision

There is a clear **spatial transition**: positions p00–p03 and p08–p09 show seashore pattern (pleural sliding present), while positions p04–p07 show stratosphere/barcode pattern (pleural sliding absent). Both patterns coexist across different lateral positions, indicating a **lung point**.

## **Overall Label: BOTH (Lung Point)**
