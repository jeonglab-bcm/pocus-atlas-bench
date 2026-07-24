# 0022_lung_air-bronchograms2

# Lung Ultrasound — Sequential Frame Analysis

---

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| 1–3 | Pleural line visible (bright horizontal line). 2–3 discrete vertical hyperechoic streaks arising from pleural line, extending toward screen bottom. Dark lung parenchyma visible **between** artifacts. |
| 4–6 | Same pattern maintained. Vertical artifacts remain discrete and separated. No merging/coalescence. No dominant bright white sheet. |
| 7–10 | Consistent with prior frames. Bright foci remain individualized. Background parenchyma retains relative hypoechogenicity between B-lines. |

---

## B-Lines Assessment

### ✅ `lung_rockets = true`

**Observations:**
- Hyperechoic **vertical artifacts** originate from the pleural line
- Extend to the **bottom of the screen without fading**
- Approximately **2–3 per intercostal space**, clearly individualized
- **Dark lung parenchyma is preserved between lines** — no confluent white sheet
- No obliteration of A-lines across the full field

### Subtype: **`septal`**
> Discrete, well-spaced B-lines with preserved dark parenchyma between them — consistent with **thickened interlobular septa** (e.g., interstitial pulmonary edema, early ILD)

---

## Consolidation Assessment

### ❌ `consolidation = false`

**Observations:**
- No **tissue-like hepatization** (liver-echogenicity pattern) identified
- No **shred sign** (irregular deep border between aerated/consolidated lung)
- Bright foci are attributable to **B-line artifacts**, not air bronchograms within hepatized parenchyma
- Underlying parenchyma remains **hypoechoic and non-solid**

### `consolidation_type = null`

---

## Summary

```
lung_rockets     = true
b_line_subtype   = "septal"
consolidation    = false
consolidation_type = null
```

> **Clinical correlation**: This anterior zone pattern of discrete septal B-lines without consolidation is consistent with **mild-to-moderate interstitial syndrome** (e.g., cardiogenic pulmonary edema Grade 1–2, early interstitial pneumonia). Recommend correlation with bilateral findings and clinical context.
