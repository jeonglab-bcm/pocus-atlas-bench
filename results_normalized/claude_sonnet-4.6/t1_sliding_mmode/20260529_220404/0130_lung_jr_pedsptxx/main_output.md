# 0130_lung_jr_pedsptxx

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observation:** Clear parallel horizontal chest-wall lines in the upper ~40%. A distinct bright pleural line. Below the pleural line: predominantly dark, low-signal field with faint, diffuse granular texture and no continuation of structured horizontal lines.
**Classification: Seashore** — pleural line visible; dark granular zone below.

---

### p01 (Image 2)
**Observation:** Clean parallel chest-wall lines at top. Bright pleural line. Below: dark field with faint granularity and two faint vertical column artifacts at the lateral margins (active-region edge effect). No barcode pattern below the pleural line.
**Classification: Seashore**

---

### p02 (Image 3)
**Observation:** Chest-wall lines at top. Multiple bright horizontal bands at regular sub-pleural depths = A-lines. The background *between* the A-lines has a mottled, non-uniform texture with no dense parallel-line continuity. Bright reflections at the bottom consistent with deep A-lines over sandy background.
**Classification: Seashore** (A-lines over granular background)

---

### p03 (Image 4)
**Observation:** Parallel chest-wall lines; pleural line identifiable. Multiple A-lines at increasing depths. The inter-A-line background retains granular/mottled character. The pleural line shows slight waviness in places.
**Classification: Seashore** (A-lines over granular background)

---

### p04 (Image 5)
**Observation:** Chest-wall lines at top; complex mid-field with multiple bright horizontal bands that display slight waviness/undulation over time — a strong indicator of motion. Background between bands has granular quality.
**Classification: Seashore** (wavy pleural line + granular background)

---

### p05 (Image 6)
**Observation:** Multiple bright horizontal bands with a notable "step-down" shift across the time axis — this depth change indicates pleural movement. Granular/mottled texture visible between bright bands. Not a uniform barcode.
**Classification: Seashore** (depth-shifting bands = motion; granular inter-band texture)

---

### p06 (Image 7)
**Observation:** Prominent multiple A-lines throughout the field. Between the bright bands, the background shows granular speckle rather than dense, continuous parallel lines. Bright lower-field reflections consistent with deeper A-lines over a seashore background.
**Classification: Seashore** (A-lines + granular inter-band texture)

---

### p07 (Image 8)
**Observation:** Very prominent, regularly spaced bright horizontal bands (A-lines) from mid-field onward. The inter-band background has visible granular/sandy texture rather than uniform horizontal striping. The overall structure is classic seashore with prominent A-lines.
**Classification: Seashore** (strong A-lines, granular background)

---

### p08 (Image 9)
**Observation:** Parallel chest-wall lines at top. Bright pleural line. Below: mostly dark field with faint low-level texture and subtle vertical column structures at the margins. The signal is reduced but not absent; granular character below pleural line discernible.
**Classification: Seashore** (subtle, reduced signal)

---

### p09 (Image 10)
**Observation:** Only 2–3 faint bright lines at the very top. The remainder is almost entirely black. Insufficient structure to determine any lung pattern.
**Classification: UNCLASSIFIABLE** — excluded from majority count.

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore ✓ |
| p01 | Seashore ✓ |
| p02 | Seashore ✓ |
| p03 | Seashore ✓ |
| p04 | Seashore ✓ |
| p05 | Seashore ✓ |
| p06 | Seashore ✓ |
| p07 | Seashore ✓ |
| p08 | Seashore ✓ |
| p09 | **Unclassifiable** |

---

## Step 2 — Overall Decision

- No alternating (lung-point) positions detected.
- No stratosphere/barcode positions detected.
- **9/9 classifiable positions = Seashore**, consistently showing: parallel chest-wall lines above, an identifiable (often slightly wavy) pleural line, and granular/dark sandy texture below — with A-lines superimposed in the mid-field positions, but always over a granular rather than a linear background.

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is present across the entire active scan region.
