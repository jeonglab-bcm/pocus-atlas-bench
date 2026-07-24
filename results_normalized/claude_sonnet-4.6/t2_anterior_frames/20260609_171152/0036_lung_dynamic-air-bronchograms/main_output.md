# 0036_lung_dynamic-air-bronchograms

# Lung Ultrasound Analysis — Anterior Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | A-Lines | Notes |
|-------|-------------|-------------------|---------|-------|
| 1 | Visible, regular | 2–3 discrete B-lines | Absent | Well-separated B-lines |
| 2 | Visible | 2–3 discrete B-lines | Absent | Similar spacing |
| 3 | Visible | 2–3 B-lines, slight crowding | Absent | Mild coalescence beginning |
| 4 | Visible | Fewer, more discrete | Absent | More septal appearance |
| 5 | Visible | 2–3 B-lines | Absent | Discrete pattern |
| 6 | Visible | Multiple B-lines, crowding | Absent | Partial coalescence |
| 7 | Visible | Multiple, partially confluent | Absent | Ground-glass tendency |
| 8 | Visible | Dense, partially coalescing | Absent | More confluent |
| 9 | Visible | Multiple discrete + confluent | Absent | Mixed appearance |
| 10 | Visible | Multiple B-lines | Absent | Returns to mixed pattern |

---

## B-Lines Assessment

### Findings:
- **Hyperechoic vertical artifacts** arise consistently from the pleural line across all frames
- They **extend to the bottom** of the screen without fading
- **No A-lines** (horizontal reverberation artifacts) are visible — entirely replaced by B-lines
- In **frames 1–2 and 4–5**: B-lines are **discrete and well-separated** → consistent with thickened interlobular septa (*septal pattern*)
- In **frames 6–9**: B-lines become **denser and partially coalescing**, approaching a white-sheet appearance → consistent with *ground-glass pattern*
- **Dynamic variability** across the clip between discrete and confluent B-lines

### Conclusion:
```
lung_rockets = true
subtype = "mixed"
```
> Both **septal** (discrete, spaced B-lines) and **ground_glass** (confluent, coalescing B-lines) patterns are visible at different time points in the clip.

---

## Consolidation Assessment

### Findings:
- **No hepatization**: Lung parenchyma does not demonstrate liver-like echogenicity
- **No shred sign**: Deep border of lung is not visible as an irregular shredded margin
- **No air bronchograms**: No punctate or linear hyperechoic foci within hepatized tissue
- The anterior lung zone maintains a **hyperechoic pleural line** without subpleural tissue-like density
- All artifacts are consistent with **interstitial/alveolar edema** rather than frank consolidation

### Conclusion:
```
consolidation = false
consolidation_type = null
```

---

## Summary Interpretation

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | ✅ **true** |
| `b_line_subtype` | 🔀 **mixed** (septal + ground_glass) |
| `consolidation` | ❌ **false** |
| `consolidation_type` | **null** |

> **Clinical correlation**: The mixed B-line pattern (septal → ground_glass progression across frames) in an anterior zone is consistent with **pulmonary edema or diffuse interstitial syndrome** (e.g., cardiogenic pulmonary edema, ARDS early phase). The dynamic shift between septal and ground-glass subtypes likely reflects respiratory cycle variation in aeration. No consolidation to suggest pneumonia or atelectasis.
