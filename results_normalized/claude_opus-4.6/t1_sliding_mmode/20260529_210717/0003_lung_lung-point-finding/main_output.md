# 0003_lung_lung-point-finding

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Observations

**p00:** Extremely dark image with minimal visible structure. Only very faint horizontal banding barely perceptible. Insufficient signal for classification.
→ **UNCLASSIFIABLE**

**p01:** Shows faint horizontal bands in the upper portion with some brighter horizontal lines around the mid-section. Below, the texture appears as dim horizontal striations without granularity.
→ **STRATOSPHERE**

**p02:** Bright horizontal lines in the upper-mid section with a distinct pleural line. Below the pleural line, horizontal striations continue without sandy/granular texture. Pleural line appears straight.
→ **STRATOSPHERE**

**p03:** Dense horizontal parallel lines visible throughout. Bright pleural line appears straight. Below it, horizontal striations dominate with no granular background.
→ **STRATOSPHERE**

**p04:** Very clear barcode pattern — dense, bright, continuous parallel horizontal lines extending through the entire image both above and below the pleural line. No granularity anywhere.
→ **STRATOSPHERE**

**p05:** Horizontal lines throughout with a bright pleural line. Below, continuous horizontal striations with no sandy texture. Pleural line is smooth/straight.
→ **STRATOSPHERE**

**p06:** Prominent bright parallel horizontal lines dominating the image. Classic barcode/stratosphere appearance.
→ **STRATOSPHERE**

**p07:** Same as p06 — very bright, continuous horizontal parallel lines throughout. Clear stratosphere pattern.
→ **STRATOSPHERE**

**p08:** Dimmer image but horizontal line pattern persists throughout. No granular texture visible. Lines are continuous.
→ **STRATOSPHERE**

**p09:** Predominantly dark with minimal discernible structure. Insufficient signal.
→ **UNCLASSIFIABLE**

## Summary Table
| Position | Classification |
|----------|---------------|
| p00 | Unclassifiable |
| p01 | Stratosphere |
| p02 | Stratosphere |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Stratosphere |
| p07 | Stratosphere |
| p08 | Stratosphere |
| p09 | Unclassifiable |

## Overall Decision

All 8 classifiable positions (p01–p08) show **stratosphere/barcode** pattern with dense continuous horizontal parallel lines and no granular texture below the pleural line.

**Overall Label: ABSENT** (pleural sliding is absent)
