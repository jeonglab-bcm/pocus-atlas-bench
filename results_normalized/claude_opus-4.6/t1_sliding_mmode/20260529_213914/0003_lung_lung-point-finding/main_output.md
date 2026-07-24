# 0003_lung_lung-point-finding

# M-mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00:** Nearly completely black with minimal signal structure. This appears to be at the edge of the active ultrasound region.
→ **UNCLASSIFIABLE**

**p01:** Some horizontal lines are visible in the upper-middle region. Below the pleural line area, the texture appears somewhat granular/irregular rather than purely composed of continuous horizontal lines. Signal is dim but there is discernible texture difference above vs. below.
→ **Seashore**

**p02:** A brighter band is visible in the mid-portion (pleural line region) which appears slightly wavy/irregular. Below this band, the texture has a granular quality mixed with some horizontal elements, distinct from the pure horizontal lines above.
→ **Seashore**

**p03:** Bright horizontal bands visible in the middle. Below these, the texture shows some granularity interspersed with horizontal elements. The pleural line region shows some irregularity. Not as clearly all-horizontal-lines as later positions.
→ **Seashore**

**p04:** Very dense, bright, continuous parallel horizontal lines spanning the entire visible portion of the image. No discernible granular texture between the lines. Pattern is uniform above and below the pleural line.
→ **Stratosphere**

**p05:** Bright horizontal lines in the middle with continuous horizontal striations throughout. Limited granularity below the pleural line — pattern dominated by parallel lines.
→ **Stratosphere**

**p06:** Very prominent, distinct, bright parallel horizontal lines throughout. Classic barcode/stratosphere appearance with no granular texture visible.
→ **Stratosphere**

**p07:** Nearly identical to p06 — dense, continuous, well-defined parallel horizontal lines throughout. No granularity.
→ **Stratosphere**

**p08:** Fainter but still clearly horizontal parallel lines without granular texture. Consistent with stratosphere pattern at reduced signal.
→ **Stratosphere**

**p09:** Very dark image with minimal visible structure — at the edge of the active region.
→ **UNCLASSIFIABLE**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | UNCLASSIFIABLE |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Stratosphere |
| p07 | Stratosphere |
| p08 | Stratosphere |
| p09 | UNCLASSIFIABLE |

## Overall Decision

There is a clear **spatial transition**: positions p01–p03 show seashore pattern (granular texture below the pleural line, indicating sliding present), while positions p04–p08 show stratosphere/barcode pattern (continuous horizontal lines throughout, indicating sliding absent). This transition from sliding-present on the left to sliding-absent on the right is characteristic of a **lung point**.

## **Overall Label: BOTH (Lung Point)**
