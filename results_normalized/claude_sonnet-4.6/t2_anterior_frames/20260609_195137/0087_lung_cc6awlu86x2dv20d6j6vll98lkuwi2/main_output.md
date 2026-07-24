# 0087_lung_cc6awlu86x2dv20d6j6vll98lkuwi2

# Lung Ultrasound Analysis — A2 PULM (Anterior Zone 2)
**Date:** 2018-Feb-14 | **Probe:** Curved Array C60 | **Settings:** THI, MB

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Deep Field | Vertical Artifacts | Notes |
|-------|-------------|------------|-------------------|-------|
| 1 (4s) | Bright, well-defined | Predominantly dark/anechoic | 2–3 discrete vertical streaks | Possible B-lines arising from pleural line |
| 2 (6s) | Clear, hyperechoic | Dark with mild heterogeneity | Discrete vertical artifacts visible | Separated by dark lung parenchyma |
| 3 (6s) | Clear | Dark | Vertical streaks present | Well-spaced, not confluent |
| 4–6 (Pg2) | Continuous, bright | Predominantly anechoic deep field | Discrete vertical lines | Spacing consistent across frames |
| 7–8 (Pg2) | Clear | Dark background | Vertical artifacts more prominent | Still discrete, not merging |
| 9–10 (Pg2) | Well-defined | Dark | Discrete vertical artifacts | No sheet-like brightness |

---

## B-Lines Assessment

### Observations:
- **Pleural line**: Clearly visible, hyperechoic, smooth, continuous across all frames
- **Vertical artifacts**: Discrete hyperechoic vertical lines arise from the pleural line in multiple frames, extending toward the bottom of the screen without fading
- **Spacing**: Dark lung parenchyma is clearly visible **between** the vertical artifacts — they do **not** coalesce or merge into a white sheet
- **Count per intercostal space**: Appears ≤3 discrete lines
- **A-lines**: Partially visible in some frames in the dark deep field, indicating residual aeration between B-lines
- **No confluent white-out**: The image is not uniformly bright; the ground-glass/white-sheet pattern is absent

### Conclusion:
```
lung_rockets = true
B-line subtype = "septal"
```
> Discrete, well-separated B-lines with dark parenchyma visible between them, consistent with **thickened interlobular septa** (e.g., mild interstitial edema, early cardiogenic pulmonary edema, or interstitial lung disease)

---

## Consolidation Assessment

### Observations:
- **Hepatization**: ❌ No tissue-like liver echogenicity in the lung parenchyma
- **Shred sign**: ❌ No irregular/shredded deep border between consolidated and aerated lung
- **Air bronchograms**: ❌ No punctate or linear hyperechoic foci within hepatized lung tissue
- Deep field remains **anechoic/dark** — consistent with normal aeration artifacts, not solid tissue

### Conclusion:
```
consolidation = false
consolidation_type = null
```

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| `b_line_subtype` | **septal** |
| `consolidation` | **false** |
| `consolidation_type` | **null** |

### Clinical Interpretation:
The pattern of **discrete septal B-lines** in the anterior zone (A2) without consolidation is most consistent with:
- **Mild interstitial pulmonary edema** (e.g., early cardiogenic)
- **Mild interstitial syndrome** (thickened septa without alveolar flooding)
- Correlation with clinical findings and other lung zones recommended for BLUE/LUS protocol classification
