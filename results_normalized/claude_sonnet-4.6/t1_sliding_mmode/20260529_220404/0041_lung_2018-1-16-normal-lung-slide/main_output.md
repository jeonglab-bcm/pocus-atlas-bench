# 0041_lung_2018-1-16-normal-lung-slide

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observation:** Upper portion shows multiple **wavy/irregular** horizontal lines (chest wall with motion). Pleural line is noticeably undulating. Below: **granular/sandy texture** with scattered brighter foci.
→ **SEASHORE**

---

### p01 (Image 2)
**Observation:** Multiple clear parallel horizontal lines above; prominent pleural line appearing **wavy**. Below: granular texture + visible A-line + granularity continuing below the A-line.
→ **SEASHORE**

---

### p02 (Image 3)
**Observation:** Multiple horizontal lines above. Below: clear **sandy/granular** texture with A-lines riding over it. No pure horizontal-only zone below pleural line.
→ **SEASHORE**

---

### p03 (Image 4)
**Observation:** Horizontal lines above becoming more uniform. Below: uniform but distinctly **granular** background texture.
→ **SEASHORE**

---

### p04 (Image 5)
**Observation:** Clear parallel lines above. Below the pleural line: well-developed **granular/sandy** texture with superimposed bright horizontal lines (A-lines over sandy background).
→ **SEASHORE**

---

### p05 (Image 6)
**Observation:** Parallel lines above; bright pleural line with slight waviness. Below: predominantly **granular texture**, some horizontal banding developing but granularity still dominant.
→ **SEASHORE**

---

### p06 (Image 7)
**Observation:** Horizontal lines in upper field; below the pleural zone: alternating **dark vertical columns** and lighter areas. The lighter areas show **granular texture** (not horizontal lines), consistent with intermittent lung contact.
→ **SEASHORE** (with partial shadowing artifact)

---

### p07 (Image 8)
**Observation:** Only 1–2 faint lines at top. Dominant feature: very **thick bright reflector** (probable rib cortex) followed by **4 large acoustic shadow columns** occupying most of the image. Insufficient lung-zone information below.
→ **UNCLASSIFIABLE** (rib shadow artifact)

---

### p08 (Image 9)
**Observation:** Upper field: multiple bright horizontal stripes (chest wall + A-lines). Then: **large dark anechoic band** (wide A-line spacing consistent with air gap). Then: another bright reflector (A-line). Then further horizontal banding below. **No granularity anywhere** in the sub-pleural field.
→ **STRATOSPHERE / BARCODE**

---

### p09 (Image 10)
**Observation:** The entire image is filled with **multiple evenly-spaced bright horizontal lines** at regular intervals (classic barcode). Background between lines is dark with zero granular texture. Perfectly straight pleural line.
→ **STRATOSPHERE / BARCODE**

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | ✅ Seashore |
| p01 | ✅ Seashore |
| p02 | ✅ Seashore |
| p03 | ✅ Seashore |
| p04 | ✅ Seashore |
| p05 | ✅ Seashore |
| p06 | ✅ Seashore |
| p07 | ⬜ Unclassifiable |
| p08 | ❌ Stratosphere |
| p09 | ❌ Stratosphere |

---

## Step 2 — Overall Decision

**Clear spatial transition detected:**
- Positions p00–p06 → **Seashore** (pleural sliding PRESENT)
- Position p07 → Excluded (unclassifiable)
- Positions p08–p09 → **Stratosphere** (pleural sliding ABSENT)

Both patterns coexist at different lateral positions, indicating a **lung point** — the anatomical boundary where sliding lung ends and non-sliding lung begins.

> ## 🔴 Overall Label: **"BOTH" (Lung Point)**
> The spatial seashore-to-stratosphere transition strongly suggests **pneumothorax** with a detectable lung point at approximately the p07–p08 boundary.
