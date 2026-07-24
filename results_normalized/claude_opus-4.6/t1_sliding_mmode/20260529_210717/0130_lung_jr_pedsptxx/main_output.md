# 0130_lung_jr_pedsptxx

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00:** The upper portion shows parallel horizontal lines (stationary tissue above pleura). Below the bright pleural line, the texture is clearly dark and granular/sandy with minimal horizontal layering. The pleural line appears slightly wavy.
→ **Seashore**

**p01:** Similar to p00 — horizontal lines above, and below the pleural line, granular texture is visible with vertical dark columns (rib shadows). The background between structures is sandy/speckled.
→ **Seashore**

**p02:** Horizontal lines above are becoming more prominent. Below the pleural line, there's increasing horizontal line density, but granular texture is still visible between lines. The pleural line shows some irregularity/waviness.
→ **Seashore** (borderline)

**p03:** Very dense, continuous horizontal lines fill both above and below the pleural line. Minimal granularity visible between the lines. The lines are tightly packed and parallel throughout.
→ **Stratosphere**

**p04:** Extremely dense continuous horizontal lines spanning the entire image. No discernible granular texture anywhere — just parallel lines from top to bottom.
→ **Stratosphere**

**p05:** Dense horizontal lines throughout, similar to p04 though with slight texture variation. Still predominantly continuous parallel lines with no clear granular background.
→ **Stratosphere**

**p06:** Horizontal lines predominate throughout with dark vertical columns visible. Some slight texture variation but mostly continuous horizontal lines. Granularity is minimal.
→ **Stratosphere**

**p07:** Clear horizontal striped lines at top. Below shows organized rectangular dark structures (rib shadows) with lighter horizontal-lined areas between. The pattern is more structured/stratified.
→ **Stratosphere**

**p08:** Bright pleural line visible with dark, granular texture below. Some faint structure but predominantly sandy/dark below the pleura — similar to p00/p01.
→ **Seashore**

**p09:** Nearly entirely black with only a single thin bright line near the top. Minimal signal or structure visible throughout. Falls outside the active region.
→ **Unclassifiable**

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
| p08 | Seashore |
| p09 | Unclassifiable |

## Overall Decision

There is a clear **spatial transition**: positions p00–p02 and p08 show seashore pattern (pleural sliding present), while positions p03–p07 show stratosphere pattern (pleural sliding absent). This coexistence of both patterns across different lateral positions indicates a **lung point**.

## **Overall Label: BOTH (Lung Point)**
