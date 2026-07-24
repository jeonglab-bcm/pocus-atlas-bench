# 0013_lung_lung-slide-mmode

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

### M-Mode (Upper Panel)
| Frames | M-Mode Pattern |
|--------|---------------|
| 1–2 | Predominantly horizontal lines above and below pleural line; limited granularity below |
| 3–6 | Transition to more granular/sandy texture below pleural line; suggests progressive lung sliding |
| 7–10 | Well-developed granular (seashore-like) pattern below pleural line; lung sliding confirmed |

> ⚠️ Early frames may show transiently reduced sliding, but overall lung sliding is present across the clip.

---

### B-Mode (Lower Panel) — Frame-by-Frame

| Frame | Pleural Line | Vertical Artifacts | Pattern Character |
|-------|-------------|-------------------|-------------------|
| 1 | Present, mildly irregular | Faint vertical streaks | Early/subtle B-lines |
| 2 | Visible | Sparse discrete B-lines | Septal-type |
| 3 | Visible | Multiple discrete B-lines | Septal-type |
| 4 | Slightly thickened | Multiple B-lines, partially coalescing | Transitional |
| 5 | Irregular, bright | Confluent bright vertical artifacts | Ground-glass type |
| 6 | Bright, irregular | Coalescent, sheet-like brightness | Ground-glass type |
| 7 | Bright | Mixed discrete + coalescent | Mixed |
| 8 | Bright | Coalescent B-lines dominating | Ground-glass type |
| 9 | Bright | Multiple B-lines, some discrete | Mixed |
| 10 | Bright, thickened | Multiple B-lines, partially confluent | Mixed |

---

## B-Lines Assessment

### Findings:
- **Hyperechoic vertical artifacts** arise consistently from the pleural line across all frames
- Artifacts extend **to the bottom of the screen without fading**
- They **move with lung sliding** (confirmed by M-mode seashore pattern in frames 3–10)
- A-lines are **largely obscured** in mid-to-late frames
- Early frames show **discrete, well-separated B-lines** (septal type, ≤3 per ICS with visible dark parenchyma between)
- Mid and late frames show **coalescing, sheet-like brightness** with merging of vertical artifacts (ground-glass type)

### Conclusion:
> **lung_rockets = true**
> **B-line subtype = mixed**
> *(Discrete septal B-lines in early frames transitioning to confluent ground-glass-type coalescing B-lines in later frames)*

---

## Consolidation Assessment

### Findings:
- **No hepatization**: Lung parenchyma does not display liver-like solid echogenicity
- **No shred sign**: Deep border of the lung field, where visible, lacks the characteristic irregular/shredded appearance
- **No air bronchograms**: No punctate or linear hyperechoic foci within consolidated parenchyma
- The bright appearance is attributable to **confluent B-lines**, not solid consolidation

### Conclusion:
> **consolidation = false**
> **consolidation_type = null**

---

## Summary

```
lung_rockets       = true
b_line_subtype     = "mixed"
consolidation      = false
consolidation_type = null
```

### Clinical Interpretation:
The mixed B-line pattern (septal → ground-glass progression across frames) in an **anterior lung zone** is consistent with **pulmonary interstitial edema** (e.g., cardiogenic pulmonary edema, ARDS early phase, or diffuse interstitial lung disease). The absence of consolidation suggests predominantly interstitial, not alveolar, involvement at this zone. Correlation with posterior/lateral zones and clinical context is recommended.
