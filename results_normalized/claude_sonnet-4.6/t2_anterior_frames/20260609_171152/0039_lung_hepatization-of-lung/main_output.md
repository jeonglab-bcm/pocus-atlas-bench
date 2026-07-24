# 0039_lung_hepatization-of-lung

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Parenchymal Echogenicity | Notable Features |
|-------|-------------|-------------------|--------------------------|-----------------|
| 1 | Visible, regular | Discrete bright verticals | Moderate | Early B-lines apparent |
| 2 | Visible | Discrete, spaced | Moderate | Septal-type artifacts |
| 3 | Visible | Discrete, spaced | Moderate | Similar to Frame 2 |
| 4 | Visible | Discrete, spaced | Moderate | Interspace darkness preserved |
| 5 | Visible | Discrete, slight increase | Moderate-high | Transition zone |
| 6 | Visible | Fewer discrete lines | **Increased echogenicity** | Tissue-like texture emerging |
| 7 | Visible | Fewer discrete lines | **Hepatization pattern** | Solid echogenicity |
| 8 | Visible | Linear bright structures | **Hepatized parenchyma** | Bright linear foci |
| 9 | Visible | **Prominent linear hyperechoic structure** | Hepatized | **Air bronchogram visible** |
| 10 | Visible | **Prominent linear hyperechoic structure** | Hepatized | **Air bronchogram confirmed** |

---

## B-Lines Assessment

### Observations:
- **Frames 1–5**: Discrete, well-spaced vertical hyperechoic artifacts arise from the pleural line, with dark lung parenchyma visible *between* them — characteristic of **septal B-lines**
- The interspace darkness is preserved, indicating incomplete confluence
- **Fewer than 3 per intercostal space**, clearly separated
- **No white-sheet confluent pattern** (no ground-glass type B-lines)

### Conclusion:
```
lung_rockets = true
subtype = "septal"
```

---

## Consolidation Assessment

### Observations:
- **Frames 6–10**: Progressive transition to **tissue-like hepatization** — the lung parenchyma adopts liver-like echogenicity, losing aeration artifacts
- **Frames 9–10**: Prominent **linear hyperechoic foci** within the hepatized tissue, oriented along bronchial paths → classic **air bronchograms**
- No visible shred sign at the deep border in the accessible field
- The consolidation occupies the mid-to-deep field of the anterior zone

### Conclusion:
```
consolidation = true
consolidation_type = "air_bronchogram"
```

---

## Summary Interpretation

| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | ✅ **TRUE** |
| **B-line subtype** | **Septal** (discrete, spaced) |
| **consolidation** | ✅ **TRUE** |
| **consolidation_type** | **Air bronchogram** within hepatized lung |

### Clinical Correlation:
> The combination of **septal B-lines** (perilesional interstitial edema/inflammatory infiltration) transitioning to **hepatization with air bronchograms** in the anterior zone is most consistent with **lobar or segmental pneumonia**. Air bronchograms within consolidation confirm patent airways surrounded by alveolar filling (exudate/fluid), distinguishing infectious consolidation from obstructive atelectasis (which typically shows **fluid bronchograms** or absent bronchograms).
