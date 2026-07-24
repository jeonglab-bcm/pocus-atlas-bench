# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observation:** Left half is nearly black (outside active ultrasound field). Right half shows two faint bright columns with minimal discernible structure. The upper portion is heavily shadowed.
**Classification: UNCLASSIFIABLE** — edge artifact, insufficient signal.

---

### p01 (Image 2)
**Observation:** Upper portion shows clear horizontal bands (chest wall layers). Below the pleural transition, the background texture becomes distinctly **granular/sandy** with mottled gray patterns. The pleural line shows some irregularity suggesting motion.
**Classification: SEASHORE** ✓

---

### p02 (Image 3)
**Observation:** Horizontal parallel bands above; below the pleural line, texture transitions to a **coarse granular/sandy pattern**. The pleural line appears wavy and irregular — supporting active sliding.
**Classification: SEASHORE** ✓

---

### p03 (Image 4)
**Observation:** Top portion shows horizontal banding (chest wall). Lower portion has a mix of horizontal lines and **granular texture**. Granularity is clearly present in the lung field.
**Classification: SEASHORE** ✓

---

### p04 (Image 5)
**Observation:** Horizontal banding becomes more prominent throughout, consistent with A-lines. However, the background between A-lines retains a **granular/irregular quality** — not purely continuous horizontal lines. Per the A-line caveat, this is consistent with seashore.
**Classification: SEASHORE** ✓

---

### p05 (Image 6)
**Observation:** Similar to p04. Prominent A-lines visible, but between and below them the texture shows **granular/sandy background**. No purely continuous horizontal stratification.
**Classification: SEASHORE** ✓

---

### p06 (Image 7)
**Observation:** A large dark vertical band appears on the right (likely rib shadow/acoustic shadow). The left-to-center region shows **granular lung-field texture** with horizontal chest-wall lines above.
**Classification: SEASHORE** ✓

---

### p07 (Image 8)
**Observation:** Dark band persists on the right. Left-center area shows **granular texture** with some bright irregular patches — characteristic of sandy/seashore background. The pleural line contour is irregular.
**Classification: SEASHORE** ✓

---

### p08 (Image 9)
**Observation:** Dark area on the right remains. Left portion shows bright rounded/lumpy structures surrounded by **coarse granular texture** — still consistent with seashore pattern. Pleural line appears irregular.
**Classification: SEASHORE** ✓

---

### p09 (Image 10)
**Observation:** Strikingly **different** from all prior positions. The upper portion shows **multiple, evenly-spaced, very bright, clean horizontal lines** extending uniformly. Below the A-lines, the background texture is predominantly composed of **continuous horizontal lines with little to no granularity** — no sandy background visible. The pleural line itself appears perfectly straight and smooth. This pattern is present throughout both the chest wall and lung field regions.
**Classification: STRATOSPHERE/BARCODE** ✗

---

## Step 2 — Overall Decision

| Position | Classification |
|----------|---------------|
| p00 | ⬛ UNCLASSIFIABLE |
| p01 | 🟢 SEASHORE |
| p02 | 🟢 SEASHORE |
| p03 | 🟢 SEASHORE |
| p04 | 🟢 SEASHORE |
| p05 | 🟢 SEASHORE |
| p06 | 🟢 SEASHORE |
| p07 | 🟢 SEASHORE |
| p08 | 🟢 SEASHORE |
| p09 | 🔴 STRATOSPHERE |

**Spatial transition detected:** Positions p01–p08 show **Seashore** (pleural sliding PRESENT), while position p09 shows **Stratosphere** (pleural sliding ABSENT). This represents a clear lateral spatial transition — the hallmark of a **lung point**.

---

## ✅ Overall Label: **"BOTH" — Lung Point Present**

> A lung point is identified at approximately the rightmost lateral extent of the scan region (p09), where pleural sliding disappears. This finding is highly specific for pneumothorax, with the lung point marking the boundary between collapsed and aerated lung.
