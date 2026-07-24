# 0130_lung_jr_pedsptxx

# M-Mode Image Analysis

## Per-Position Classification

**p00 (Image 1):**
Upper portion shows parallel horizontal lines (stationary chest wall). Below the pleural line, the texture is clearly dark and granular/sandy with no organized horizontal lines. The pleural line appears slightly irregular.
→ **Seashore**

**p01 (Image 2):**
Horizontal lines above the pleural line. Below, the texture remains granular/sandy with dark vertical columns visible. The background between structures is grainy, not linearly organized.
→ **Seashore**

**p02 (Image 3):**
More horizontal line structure than p00-p01, but the pleural line appears wavy/irregular, and the background between prominent A-lines still retains some granularity. Not purely dense continuous lines.
→ **Seashore** (borderline)

**p03 (Image 4):**
Dense, continuous horizontal lines extending throughout both above and below the pleural line. The pleural line appears straight. No granular texture visible below.
→ **Stratosphere**

**p04 (Image 5):**
Continuous parallel horizontal lines dominate the entire image. No granular/sandy texture visible anywhere below the pleural line.
→ **Stratosphere**

**p05 (Image 6):**
Same dense horizontal line pattern throughout. Lines are continuous with no granularity between them.
→ **Stratosphere**

**p06 (Image 7):**
Horizontal lines throughout with dark vertical bands. The texture between bands shows organized horizontal lines, not granular patterns.
→ **Stratosphere**

**p07 (Image 8):**
Clear organized horizontal lines at top, structured horizontal banding below with dark vertical columns. Pattern remains linear throughout.
→ **Stratosphere**

**p08 (Image 9):**
Horizontal lines above pleural line, then predominantly dark below with subtle granular texture. No dense continuous horizontal lines below the pleural line.
→ **Seashore**

**p09 (Image 10):**
Nearly entirely black with only thin bright lines at the very top. Insufficient structure to classify.
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

There is a clear **spatial transition**: positions p00–p02 and p08 show seashore pattern (sliding present), while positions p03–p07 show stratosphere pattern (sliding absent). This coexistence of both patterns across different lateral positions indicates a **lung point**.

**Overall Label: BOTH (Lung Point)**
