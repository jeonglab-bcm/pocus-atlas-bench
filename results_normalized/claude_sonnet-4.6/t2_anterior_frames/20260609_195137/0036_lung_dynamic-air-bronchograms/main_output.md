# 0036_lung_dynamic-air-bronchograms

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Pattern Character |
|-------|-------------|-------------------|------------------|
| 1 | Visible, smooth | 2–3 discrete B-lines | Septal, spaced |
| 2 | Visible | 2–3 discrete B-lines | Septal, spaced |
| 3 | Visible | 3 discrete B-lines | Septal, mild coalescing |
| 4 | Visible | 3–4 B-lines | Transitional |
| 5 | Visible | 3–4 B-lines | Transitional |
| 6 | Visible | 4–5 B-lines, partial fusion | Early ground-glass |
| 7 | Visible | 5+ B-lines, coalescing | Ground-glass tendency |
| 8 | Visible | 5+ B-lines, merging | Ground-glass |
| 9 | Visible | Multiple confluent | Ground-glass |
| 10 | Visible | Multiple confluent | Ground-glass |

---

## B-Line Assessment

**Findings:**
- Hyperechoic vertical artifacts arise consistently from the pleural line
- Artifacts extend to the bottom of the screen without fading
- **Early frames (1–4):** Discrete, well-spaced B-lines with preserved dark parenchyma between them → **septal pattern**
- **Later frames (6–10):** B-lines increase in number, begin coalescing and merging into a brighter, more confluent sheet → **ground-glass pattern**
- A-lines are largely obscured in the latter half of the clip

> ✅ **lung_rockets = true**
> 🔀 **subtype = mixed** *(septal transitioning to ground-glass across the clip)*

---

## Consolidation Assessment

**Findings:**
- No tissue-like hepatization observed (lung does not resemble liver echogenicity)
- No shred sign (deep border remains smooth without irregular shredding)
- No air bronchograms (no punctate/linear hyperechoic foci within hepatized lung)
- Parenchyma remains dominated by vertical artifacts, not solid tissue signal

> ❌ **consolidation = false**
> **consolidation_type = null**

---

## Summary Conclusion

```
lung_rockets      : true
b_line_subtype    : mixed (septal → ground_glass progression)
consolidation     : false
consolidation_type: null
```

**Clinical Interpretation:** This clip is consistent with an **interstitial syndrome** (e.g., cardiogenic pulmonary edema, early ARDS, or interstitial pneumonia). The dynamic progression from septal to ground-glass B-lines within a single sweep may reflect heterogeneous alveolar-interstitial involvement. No consolidative process is identified in this anterior zone.
