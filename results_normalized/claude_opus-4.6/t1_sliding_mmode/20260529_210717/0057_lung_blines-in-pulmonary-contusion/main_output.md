# 0057_lung_blines-in-pulmonary-contusion

# M-mode Image Analysis

## Per-Position Classification

**p00:** The left portion is largely dark (edge of active region), but the right side shows bright areas with clear granular/speckled texture in columnar formations. Sandy texture is visible below the pleural line level during periods of signal.
→ **Seashore**

**p01:** Shows more consistent signal. Granular/sandy texture is clearly visible in the bright columnar regions separated by dark vertical gaps. The texture below the pleural line is speckled.
→ **Seashore**

**p02:** Full-coverage granular texture. Dome-shaped/irregular tops to the bright columns suggest pleural line motion. Sandy texture predominates below.
→ **Seashore**

**p03:** Clear granular/sandy texture throughout the bright areas. A bright vertical structure visible on the right. The background remains clearly speckled.
→ **Seashore**

**p04:** Horizontal lines (A-lines) become more prominent. However, the background *between* these lines still shows granular texture. The pleural line appears somewhat wavy/irregular.
→ **Seashore** (with prominent A-lines)

**p05:** Similar to p04. Prominent A-lines visible, but granular texture persists between them. Not purely parallel horizontal lines throughout.
→ **Seashore** (with A-lines)

**p06:** Horizontal structures visible with a bright vertical line. Granular texture still discernible between the horizontal lines. Pleural line appears slightly irregular.
→ **Seashore**

**p07:** Upper portion darkens somewhat but lower portion retains granular texture. Sandy background visible.
→ **Seashore**

**p08:** Upper region is dark; lower portion shows granular texture but with reduced signal. Still enough visible granularity to classify.
→ **Seashore**

**p09:** Dramatically different from all other positions. Shows very dense, thin, perfectly parallel horizontal lines spanning the full depth of the image. No granular/sandy texture is visible between these lines. The pleural line is not distinguishable as a separate wavy structure — horizontal lines are continuous across all depths. Classic barcode appearance.
→ **Stratosphere**

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
| p09 | Stratosphere |

## Overall Decision

There is a clear **spatial transition**: positions p00–p08 show seashore pattern (pleural sliding present) while position p09 shows stratosphere pattern (pleural sliding absent). This indicates a lung point at the rightmost lateral boundary of the scan.

**Overall Label: BOTH (lung point)**
