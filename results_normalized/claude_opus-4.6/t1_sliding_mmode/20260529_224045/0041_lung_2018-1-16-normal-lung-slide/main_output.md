# 0041_lung_2018-1-16-normal-lung-slide

# M-Mode Image Analysis

## Per-Position Classification

**p00 (~5%):** The upper portion shows clear horizontal parallel lines (subcutaneous tissue). Below the pleural line, there is granular/sandy texture with scattered bright echoes. The pleural line appears somewhat irregular/wavy. → **Seashore**

**p01 (~15%):** Horizontal lines above, with a slightly wavy pleural line. Below, there is clear granular/sandy texture with a visible A-line overlying the sandy background. → **Seashore**

**p02 (~25%):** Horizontal lines above. Below the pleural line, two darker columns are visible with granular texture. The granularity is still the dominant pattern below the pleural line. → **Seashore**

**p03 (~35%):** Horizontal lines above with relatively uniform granular/sandy texture below the pleural line. No distinct horizontal lines extending below. → **Seashore**

**p04 (~45%):** Similar to p03 — granular texture below pleural line, horizontal lines confined above. → **Seashore**

**p05 (~55%):** Horizontal lines above, predominantly granular texture below the pleural line with slight horizontal component. Pleural line shows some waviness. → **Seashore**

**p06 (~65%):** Horizontal lines above. Below the pleural line, two dark granular columns are visible separated by brighter areas — granular texture still dominates. → **Seashore**

**p07 (~75%):** Three distinct dark columns below the pleural line alternate with brighter bands showing horizontal line structure. This cyclic temporal alternation between granular (seashore) and horizontal lines (stratosphere) within the same strip is characteristic. → **Alternating (Lung Point)**

**p08 (~85%):** Dark rectangular areas below the pleural line bordered by bright horizontal lines (A-lines). Between A-lines, the texture is dark/non-granular with horizontal organization. Right portion shows more stratosphere pattern. → **Stratosphere**

**p09 (~95%):** Very regular, evenly-spaced bright horizontal lines spanning the entire image depth. No granular texture visible anywhere. Pleural line perfectly straight. Classic barcode pattern. → **Stratosphere**

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
| p07 | Alternating (Lung Point) |
| p08 | Stratosphere |
| p09 | Stratosphere |

## Overall Decision

Two criteria are met for "both":
1. **p07 is classified as Alternating** → triggers "both"
2. **Clear spatial transition** from seashore (p00–p06) to stratosphere (p08–p09) → also triggers "both"

**Overall Label: BOTH (Lung Point Present)**

The lung point is located at approximately the p07 position (~75% lateral), marking the boundary where pleural sliding transitions from present (left) to absent (right).
