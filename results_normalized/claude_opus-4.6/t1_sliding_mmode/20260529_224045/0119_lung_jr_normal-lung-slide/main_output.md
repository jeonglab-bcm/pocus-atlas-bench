# 0119_lung_jr_normal-lung-slide

# M-mode Lung Ultrasound Analysis

## Per-Position Classification

### p00 (leftmost, ~5%)
**Observation:** Clear horizontal lines in the upper portion (chest wall). Below the pleural line, I observe granular/sandy texture with some A-lines visible. The pleural line appears slightly irregular/wavy.
**Classification: Seashore**

### p01 (~15%)
**Observation:** Horizontal lines above the pleural line. Below, there is visible granular texture interspersed with A-lines. Sandy background is discernible.
**Classification: Seashore**

### p02 (~25%)
**Observation:** Dense, closely-spaced continuous horizontal lines extend throughout the image both above and below the pleural line. No granular texture is visible between the lines; instead, finer horizontal lines fill the spaces.
**Classification: Stratosphere**

### p03 (~35%)
**Observation:** Very similar to p02 — dense, continuous parallel horizontal lines throughout. No granularity below the pleural line. Lines appear uniform and uninterrupted.
**Classification: Stratosphere**

### p04 (~45%)
**Observation:** Dense horizontal lines continue both above and below the pleural line. Background between lines shows more continuous lines rather than sandy texture.
**Classification: Stratosphere**

### p05 (~55%)
**Observation:** Horizontal lines above pleural line. Below, the texture transitions back to showing some granularity between A-lines. Less dense horizontal lines than p02-p04.
**Classification: Seashore**

### p06 (~65%)
**Observation:** Distinct bright pleural line visible. Below it, relatively darker area with faint granular texture. No dense continuous horizontal lines below.
**Classification: Seashore**

### p07 (~75%)
**Observation:** Bright pleural line with granular/sandy texture below. A-lines visible but background between them is granular rather than lined.
**Classification: Seashore**

### p08 (~85%)
**Observation:** Faint but visible structure. Horizontal lines above, with some granular texture below pleural line. Signal diminished but pattern is discernible.
**Classification: Seashore**

### p09 (rightmost, ~95%)
**Observation:** Very dark image with minimal visible structure. Insufficient signal to determine pattern.
**Classification: Unclassifiable**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Stratosphere |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | Unclassifiable |

## Overall Decision

There is a clear **spatial transition**: positions p00-p01 show seashore, positions p02-p04 show stratosphere, and positions p05-p08 return to seashore. Both patterns coexist across different spatial positions, indicating a lung point.

**Overall Label: BOTH (Lung Point)**
