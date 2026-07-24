# 0093_lung_i989ozcw1em02me41iblif5k8augx2

# M-Mode Analysis: Lung Ultrasound

## Per-Position Classification

### p00 (~5% lateral position)
**Observation:** Dense, bright horizontal parallel lines in the upper ~45% of the image. Below this boundary, the image is almost entirely black with no discernible texture (neither granular nor horizontal lines). No A-lines visible below.
**Classification: UNCLASSIFIABLE** — Edge position with loss of deep signal, preventing reliable pattern determination.

### p01 (~15%)
**Observation:** Horizontal lines in the upper portion. Below the pleural line region, some texture/signal is visible with slight irregularity that's not purely horizontal. The pleural line shows mild waviness.
**Classification: SEASHORE** (mild)

### p02 (~25%)
**Observation:** Clear horizontal lines above. Below the pleural line, distinct complex texture with granular quality. Pleural line appears wavy/irregular. Not purely horizontal lines below.
**Classification: SEASHORE**

### p03 (~35%)
**Observation:** Horizontal lines above; below the pleural line, clear granular texture with A-lines overlaid on a sandy background. Pleural line is wavy.
**Classification: SEASHORE**

### p04 (~45%)
**Observation:** Horizontal lines above; below, visible granular texture between A-lines. Pleural line shows irregularity.
**Classification: SEASHORE**

### p05 (~55%)
**Observation:** Horizontal lines above; complex granular texture below with areas of brightness. Background texture between structures is sandy/irregular.
**Classification: SEASHORE**

### p06 (~65%)
**Observation:** Horizontal lines above; below the pleural line, brighter textured areas with granular quality. Not continuous horizontal lines.
**Classification: SEASHORE**

### p07 (~75%)
**Observation:** Horizontal lines above; below, some granular texture visible with bright spots near the bottom. Texture is not purely organized horizontal lines.
**Classification: SEASHORE**

### p08 (~85%)
**Observation:** Horizontal lines in the upper portion. Middle zone is dark but bright irregular spots/fragments near the bottom show some non-horizontal patterning.
**Classification: SEASHORE** (weak)

### p09 (~95%)
**Observation:** Horizontal lines above; below the pleural line area, very limited signal with mostly darkness. Insufficient texture to determine pattern.
**Classification: UNCLASSIFIABLE** — Edge position with inadequate deep signal.

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Unclassifiable |
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

Excluding the 2 unclassifiable edge positions, all 8 remaining positions (p01–p08) show **seashore** pattern with granular texture below the pleural line and wavy/irregular pleural lines — consistent with pleural sliding being present throughout. No alternating patterns or spatial transitions detected.

## **Overall Label: PRESENT**
