# 0057_lung_blines-in-pulmonary-contusion

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observation:** Top ~40% is pure black. Only two isolated bright vertical columns emerge from an otherwise featureless dark field. No identifiable pleural line or texture below it.
**→ UNCLASSIFIABLE** (outside active ultrasound region)

---

### p01 (Image 2)
**Observation:** Substantial black band at top (~20–25%). Below it, horizontal layering starts to emerge in the chest-wall zone. The lower portion of the active strip shows a faintly granular, speckled texture, consistent with an early seashore appearance. Pleural line is not perfectly straight.
**→ SEASHORE** (marginal)

---

### p02 (Image 3)
**Observation:** Horizontal parallel lines visible in the upper (chest-wall) zone. The pleural line shows a clearly undulating, bumpy profile — indicating motion. Below it: distinctly granular/sandy texture.
**→ SEASHORE**

---

### p03 (Image 4)
**Observation:** Well-defined horizontal layers in upper chest-wall region. A wavy, irregular pleural line. Below: mixed granular texture with some faint A-line echoes over a sandy background.
**→ SEASHORE**

---

### p04 (Image 5)
**Observation:** Clear stratified chest-wall layers above. Pleural line is wavy/irregular. Below: granular speckled pattern typical of lung sliding, with faint A-lines riding over sandy background.
**→ SEASHORE**

---

### p05 (Image 6)
**Observation:** Upper horizontal banding (chest wall) clearly defined. Below pleural level: granular texture with some A-line reflections over speckled background. A bright vertical stripe on the right side is an artifact but does not alter the overall pattern.
**→ SEASHORE**

---

### p06 (Image 7)
**Observation:** Upper zone: defined horizontal layers. Below: granular background with A-line echoes. Large dark column on far right is likely acoustic shadow or field edge — the central/left portion classifies clearly.
**→ SEASHORE**

---

### p07 (Image 8)
**Observation:** Horizontal chest-wall layers above. Bright focal spots near pleural level (motion artifact supports sliding). Below: granular/sandy texture. Dark right-side strip excluded.
**→ SEASHORE**

---

### p08 (Image 9)
**Observation:** Rounded, ball-like bright structures near the pleural level (hallmark of sliding). Above: layered chest wall. Below: granular/speckled texture. Some horizontal line components present, but background is sandy — consistent with seashore.
**→ SEASHORE**

---

### p09 (Image 10)
**Observation:** Dramatically different from all prior images. Large black area at top, then multiple **evenly-spaced, bright, continuous parallel horizontal lines** throughout the active zone. The inter-line background is **uniformly dark — zero granularity**. No pleural irregularity, no sandy texture anywhere. Classic **barcode/stratosphere** pattern.
**→ STRATOSPHERE**

---

## Step 2 — Overall Decision

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
| p09 | **Stratosphere** |

There is a clear **spatial transition**: positions p01–p08 = Seashore (sliding present), position p09 = Stratosphere (sliding absent). Both patterns coexist across different lateral positions.

## ✅ Overall Label: **"BOTH" — Lung Point Present**

The lung point is located at the rightmost lateral extent of this scan zone, where pleural sliding disappears (p09 = stratosphere) while it is confirmed throughout the left and central portions (p01–p08 = seashore).
