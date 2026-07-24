# 0049_lung_pleural-shred-sign

## Step 1 — Per-Position Classification

---

### p00 (leftmost, ~5%)
**Observation:** Nearly entirely black. No discernible pleural line, no sky/lung texture visible. Falls outside the active ultrasound cone.
**Classification: UNCLASSIFIABLE**

---

### p01 (~15%)
**Observation:** A visible bright pleural line with horizontal parallel lines above (sky region). Below the pleural line, the texture shows a mixed granular/sandy appearance. The pleural line itself appears slightly irregular/wavy.
**Classification: SEASHORE**

---

### p02 (~25%)
**Observation:** Clear pleural line present. Above: well-defined horizontal lines. Below: distinct granular/sandy texture is visible. The pleural line shows slight waviness suggesting motion. Some A-lines visible overlying sandy background.
**Classification: SEASHORE**

---

### p03 (~35%)
**Observation:** Pleural line is bright and somewhat irregular. Below the pleural line, there is a mix of horizontal lines and granular heterogeneity — not purely smooth parallel lines. The unevenness of the pleural line supports sliding motion.
**Classification: SEASHORE**

---

### p04 (~45%)
**Observation:** A bright pleural line with fine horizontal lines above. Below the pleural line, the background shows heterogeneous granular texture rather than dense uniform parallel lines. The pleural line has a slight undulating contour.
**Classification: SEASHORE**

---

### p05 (~55%)
**Observation:** Horizontal lines visible above the pleural line. Below the pleural line, while horizontal streaking is present, there is clear textural heterogeneity (not purely dense even parallel lines). Pleural line appears slightly irregular.
**Classification: SEASHORE**

---

### p06 (~65%)
**Observation:** Similar to p05. The pleural line is visible with horizontal lines above. Below: horizontal streaks are present but interspersed with granular texture. No perfectly smooth, uniform barcode pattern is seen throughout.
**Classification: SEASHORE**

---

### p07 (~75%)
**Observation:** Pleural line visible with the typical horizontal sky pattern above. Below the pleural line: mixed granular and streaky texture. The inferior region shows some patchy granularity. Not a pure dense-line stratosphere pattern.
**Classification: SEASHORE**

---

### p08 (~85%)
**Observation:** The image is darker overall, but a faint pleural line and some horizontal lines above are still discernible. Below: predominantly dark with some subtle horizontal streaking and granular elements. Just enough structure to classify.
**Classification: SEASHORE** (subtle but consistent with seashore)

---

### p09 (rightmost, ~95%)
**Observation:** Predominantly black upper region with a very bright white bar at the very bottom — a classic edge artifact. No interpretable lung/pleural structure in the active image area.
**Classification: UNCLASSIFIABLE**

---

## Summary Table

| Position | Pattern | Pleural Sliding |
|----------|---------|----------------|
| p00 | Unclassifiable | — |
| p01 | **Seashore** | Present |
| p02 | **Seashore** | Present |
| p03 | **Seashore** | Present |
| p04 | **Seashore** | Present |
| p05 | **Seashore** | Present |
| p06 | **Seashore** | Present |
| p07 | **Seashore** | Present |
| p08 | **Seashore** | Present |
| p09 | Unclassifiable | — |

---

## Step 2 — Overall Decision

- **Classifiable positions:** p01–p08 (8 positions)
- **Seashore:** 8/8 classifiable positions
- **Stratosphere:** 0/8
- **Alternating/Lung point:** None detected
- No spatial transition between seashore and stratosphere patterns observed

> ## ✅ Overall Label: **PRESENT**
> Pleural sliding is **present** across all classifiable lateral positions. The granular/sandy texture below the pleural line, combined with the irregular/wavy pleural line morphology at multiple positions, consistently indicates active pleural sliding with no evidence of pneumothorax.
