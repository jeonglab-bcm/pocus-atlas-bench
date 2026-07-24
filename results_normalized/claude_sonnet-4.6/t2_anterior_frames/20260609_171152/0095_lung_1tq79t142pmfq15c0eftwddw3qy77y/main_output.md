# 0095_lung_1tq79t142pmfq15c0eftwddw3qy77y

# Lung Ultrasound — Sequential Frame Analysis

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| 1–2 | Pleural line identifiable; early scattered hyperechoic vertical artifacts; moderate parenchymal echogenicity |
| 3–4 | Vertical artifacts more defined; background parenchyma increasingly echogenic with discrete bright foci |
| 5–6 | Multiple bright punctate/linear foci within echogenic parenchyma; some vertical streaming; artifacts begin to coalesce |
| 7–8 | Parenchymal echogenicity clearly increased (tissue-like); scattered bright hyperechoic punctate foci more prominent |
| 9–10 | Dense echogenic parenchyma with multiple bright reflective foci distributed throughout — most prominent air bronchogram-like pattern |

---

## B-Lines Assessment

**`lung_rockets = true`**
**`subtype = "mixed"`**

### Observations:
- Hyperechoic vertical artifacts arising from the pleural line are present, particularly in early-to-mid frames
- In frames 1–4, discrete, separated B-lines are visible (**septal pattern**)
- In frames 5–10, these artifacts become more confluent and coalesce into a brighter sheet-like appearance (**ground-glass pattern**)
- The co-existence of both discrete and confluent artifacts across the clip defines a **mixed** subtype

---

## Consolidation Assessment

**`consolidation = true`**
**`consolidation_type = "air_bronchogram"`**

### Observations:
- By frames 6–10, the deep lung parenchyma loses normal aeration pattern and becomes **hepatized** — solid, echogenic, resembling liver texture
- Within this hepatized parenchyma, **multiple punctate and linear hyperechoic foci** are clearly visible — classic **air bronchograms** representing air-filled bronchi within consolidated lung
- No clearly defined shred sign at the deep margin is identifiable in this anterior view
- The consolidation appears subpleural and progressively evident across the clip

---

## Summary & Interpretation

```
lung_rockets      = true
b_line_subtype    = "mixed"
consolidation     = true
consolidation_type = "air_bronchogram"
```

> **Clinical Correlation:** The combination of confluent B-lines (ground-glass/mixed pattern) transitioning into hepatized lung with **dynamic air bronchograms** in the anterior zone is highly characteristic of **alveolar consolidation** — most consistent with **pneumonia**. Air bronchograms within hepatized tissue help differentiate infectious/inflammatory consolidation from atelectasis (which typically shows fluid bronchograms or absent bronchograms).
