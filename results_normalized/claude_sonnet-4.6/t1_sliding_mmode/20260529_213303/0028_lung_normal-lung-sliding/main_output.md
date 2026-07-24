# 0028_lung_normal-lung-sliding

# M-Mode Lung Ultrasound Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Bright parallel horizontal lines in upper portion; lower half is nearly completely black with minimal structure. Likely at the left edge of the active US beam. | **UNCLASSIFIABLE** |
| **p01** | Horizontal lines visible above; lower portion still very dark with only marginal signal. Insufficient texture to distinguish pattern. | **UNCLASSIFIABLE** |
| **p02** | Clear horizontal lines above a bright pleural band; lower portion begins to show faint but discernible granular/sandy texture. Pleural line shows slight waviness. | **SEASHORE** |
| **p03** | Well-defined horizontal lines (chest wall/A-lines) above; below the pleural line, granular/sandy texture is clearly developing in the mid-lower field. | **SEASHORE** |
| **p04** | Strong horizontal lines above; granular sandy texture clearly visible below the pleural line. Pleural line has a subtly irregular, non-flat contour. | **SEASHORE** |
| **p05** | Horizontal lines above; prominent granular background below. No continuous parallel lines extending below the pleural line. | **SEASHORE** |
| **p06** | Horizontal lines above; granular texture below. Pattern is consistent across the strip. | **SEASHORE** |
| **p07** | Upper horizontal lines slightly less bright but still visible; lower field shows granular texture with subtle wave-like features. | **SEASHORE** |
| **p08** | Horizontal lines becoming fainter at top; lower portion retains wavy/granular texture. No barcode-like extension below the pleural line. | **SEASHORE** |
| **p09** | Upper lines very faint; lower portion predominantly dark with minimal discernible structure. Likely approaching the right edge of the active beam. | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p02 through p08 → **7 positions**, all classified as **SEASHORE**

- No stratosphere/barcode pattern observed at any position (no continuous parallel horizontal lines below the pleural line).
- No alternating bands (lung point) observed.
- Granular/sandy texture below the pleural line is consistently present across all central positions.
- Pleural line shows subtle waviness/irregularity in multiple strips, confirming pleural motion.

---

## ✅ Overall Label: **PRESENT**
*Pleural sliding is present across the scanned lung zone.*
