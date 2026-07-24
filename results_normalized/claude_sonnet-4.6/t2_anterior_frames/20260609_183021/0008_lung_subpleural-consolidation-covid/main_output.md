# 0008_lung_subpleural-consolidation-covid

# Lung Ultrasound Analysis — Sequential Frame Review

## Frame-by-Frame Observations

### Frames 1–6 (Dynamic Phase)
- **Two rib shadows** visible at the top of each frame (hyperechoic with posterior acoustic shadowing)
- **Central anechoic/hypoechoic region** (upper-middle): Irregular dark space between rib shadows, consistent with a small **pleural effusion** or acoustic shadow
- **Large echogenic structure** (lower-right quadrant): Appears in every frame, tissue-like in texture — **no** typical A-line reverberation pattern
- **Discrete bright vertical foci** visible along the left and peripheral margins — potential **septal B-lines** adjacent to the main lesion

### Frames 7–10 (Focal Zone Closer View)
- The large echogenic structure becomes more **central and dominant**
- Frame 7: Relatively **homogeneous hepatization** pattern — parenchymal echogenicity resembling liver texture
- Frames 8–9: **Punctate/focal bright hyperechoic foci** appear *within* the echogenic structure → highly suggestive of **air bronchograms**
- Frame 10: Persisting hepatized lung with bright internal foci; irregular deep border may suggest a subtle **shred sign**

---

## B-Lines Assessment

| Feature | Observation |
|---|---|
| Vertical artifacts from pleural line | Present at periphery of consolidation |
| Extension to screen bottom | Yes, in peripheral zones |
| Pattern | Coalescing/merging in central zone; discrete in periphery |

> **lung_rockets = true**
> **Subtype: mixed** — Discrete septal B-lines visible peripherally (frames 1–6); confluent ground-glass–like brightness merging into the consolidation zone centrally

---

## Consolidation Assessment

| Sign | Present? | Details |
|---|---|---|
| Hepatization | ✅ | Tissue-like echogenicity, liver-resembling parenchyma (frames 7–10) |
| Air bronchograms | ✅ | Punctate hyperechoic foci within hepatized lung (frames 8–9) |
| Shred sign | Possible | Irregular deep border in frame 10 |

> **consolidation = true**
> **consolidation_type = "air_bronchogram"** *(predominant feature)*

---

## Summary & Clinical Interpretation

```
lung_rockets     : true
b_line_subtype   : mixed (septal + ground_glass)
consolidation    : true
consolidation_type: air_bronchogram
```

### ⚠️ Pattern Consistent With: **Pneumonia**
- **Anteriorly located consolidation** with air bronchograms = hallmark of alveolar pneumonia
- Surrounding **mixed B-line pattern** suggests perilesional interstitial involvement
- Small **para-consolidation effusion** cannot be excluded
- The dynamic frames show stable morphology, arguing against atelectasis (which typically changes with ventilation)

> **Clinical Correlation Recommended**: This pattern warrants correlation with clinical signs (fever, productive cough, CXR/CT), as anterior consolidation with air bronchograms on LUS carries high specificity for bacterial pneumonia.
