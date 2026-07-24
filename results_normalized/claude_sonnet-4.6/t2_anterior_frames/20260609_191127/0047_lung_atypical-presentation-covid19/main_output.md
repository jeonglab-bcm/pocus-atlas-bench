# 0047_lung_atypical-presentation-covid19

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Parenchyma Deep to Pleura | Notes |
|-------|-------------|-------------------|--------------------------|-------|
| 1 | Bright, curved | 1–2 discrete hyperechoic columns to screen bottom | Dark between artifacts | Classic discrete B-line |
| 2 | Intact, hyperechoic | 1–2 well-spaced vertical rays | Dark intervening lung | Septal pattern |
| 3 | Intact | 1–2 discrete B-lines | Dark parenchyma preserved | Septal |
| 4 | Intact | 2 discrete B-lines with spacing | Dark between them | Septal |
| 5 | Intact | 1–2 B-lines, well-demarcated | Dark parenchyma | Septal |
| 6 | Intact | 2 discrete vertical artifacts | Some brightness but B-lines spaced | Septal |
| 7 | Intact | 1 dominant bright vertical column | Darker adjacent lung | Septal |
| 8 | Intact | Multiple, slightly more numerous B-lines | Parenchyma slightly brighter | Transitional — possible early coalescence |
| 9 | Intact | **Two very distinct, widely-spaced B-lines** flanking darker central lung | Clear dark parenchyma between artifacts | Classic septal pattern |
| 10 | Intact | Multiple vertical artifacts, some crowding | Parenchyma slightly echogenic overall | Mixed tendency |

---

## B-Line Assessment

### ✅ B-lines Present: `lung_rockets = true`

**Supporting observations:**
- Hyperechoic vertical artifacts **arise directly from the pleural line** in every frame
- Artifacts **extend without fading to the bottom** of the screen
- Artifacts demonstrate **movement synchronous with lung sliding**
- In frames 1–7 and especially frame 9: B-lines are **discrete and well-separated**, with preserved dark lung parenchyma between them — hallmark of **thickened interlobular septa**
- In frames 8 and 10: slightly increased number of B-lines with mild parenchymal brightness, suggesting borderline coalescence

### B-line Subtype: `septal`

> The **predominant pattern across the clip is septal**: ≤3 discrete, well-spaced B-lines per intercostal space with clearly preserved dark intervening parenchyma. The minor brightening in late frames does **not reach confluent ground-glass sheet** criteria.

---

## Consolidation Assessment

### ❌ Consolidation Absent: `consolidation = false`

**Evidence against consolidation:**
- **No hepatization**: Deep lung parenchyma does not adopt liver-like tissue echogenicity; the zone beneath the pleural line remains predominantly dark
- **No shred sign**: The deep border of the aerated lung is not irregular or "shredded"
- **No air bronchograms**: No punctate or linear hyperechoic foci are identified within a hepatized zone

### `consolidation_type = null`

---

## Summary Conclusions

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = false
consolidation_type = null
```

### Clinical Interpretation
The sequential frames are consistent with **moderate interstitial syndrome** (B3 pattern — multiple but discrete septal B-lines in the anterior zone), most compatible with:
- **Interstitial pulmonary edema** (early/moderate)
- **Interstitial pneumonia or fibrosis** (early)

The absence of ground-glass coalescence and consolidation argues against **alveolar flooding** or **lobar pneumonia** at this zone and time point.
