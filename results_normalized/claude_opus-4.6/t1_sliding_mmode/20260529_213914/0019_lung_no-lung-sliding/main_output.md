# 0019_lung_no-lung-sliding

# M-mode Image Analysis

## Per-Position Classification

### p00 (leftmost ~5%)
**Observation:** Bright horizontal parallel lines in the upper ~30%, with a markedly dark/disorganized lower portion. The texture below the pleural line is scattered and granular rather than showing organized horizontal lines.
**Classification: SEASHORE**

### p01 (~15%)
**Observation:** Well-defined horizontal lines in the upper portion with a clear transition to a darker, more chaotic/grainy texture below the pleural line. No continuous horizontal line organization in the lower zone.
**Classification: SEASHORE**

### p02 (~25%)
**Observation:** Bright organized horizontal lines in the upper portion. Below the pleural line, the texture appears granular/disorganized — distinctly different from pure horizontal lines. Clear division between "sky" and "sand."
**Classification: SEASHORE**

### p03 (~35%)
**Observation:** Dense, continuous horizontal parallel lines extending throughout the ENTIRE image — from top to bottom. No granular texture visible anywhere. No textural division between upper and lower zones.
**Classification: STRATOSPHERE**

### p04 (~45%)
**Observation:** Very dense continuous horizontal parallel lines throughout the full depth. Uniform organization with no sandy/granular areas. Classic barcode appearance.
**Classification: STRATOSPHERE**

### p05 (~55%)
**Observation:** Continuous dense horizontal lines throughout the entire image. No textural change between upper and lower zones. Clear stratosphere pattern.
**Classification: STRATOSPHERE**

### p06 (~65%)
**Observation:** Dense horizontal parallel lines extending from top to bottom. Consistent horizontal organization maintained throughout with no granularity.
**Classification: STRATOSPHERE**

### p07 (~75%)
**Observation:** Horizontal lines present throughout the image. While the lower portion is somewhat less bright, the horizontal LINE ORGANIZATION is maintained below the pleural line (unlike p01-p02 where it becomes granular).
**Classification: STRATOSPHERE**

### p08 (~85%)
**Observation:** Bright horizontal lines in the upper portion with faint but discernible horizontal streaks continuing below. Maintains some horizontal organization in the lower zone, though dimmer.
**Classification: STRATOSPHERE**

### p09 (rightmost ~95%)
**Observation:** Predominantly black/very dark image with minimal visible structure. Insufficient signal to determine pattern.
**Classification: UNCLASSIFIABLE**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Stratosphere |
| p07 | Stratosphere |
| p08 | Stratosphere |
| p09 | Unclassifiable |

## Overall Decision

**There is a clear spatial transition:** positions p00–p02 show seashore pattern (pleural sliding present), while positions p03–p08 show stratosphere pattern (pleural sliding absent). This spatial coexistence of both patterns indicates a **lung point** — the boundary between sliding and non-sliding lung located around position p02–p03.

## **Overall Label: BOTH (Lung Point)**
