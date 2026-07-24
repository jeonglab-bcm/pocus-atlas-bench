# 0059_lung_air-bronchograms

# Lung Ultrasound Analysis — Right Zone 4 (Sequential Frames)

## Equipment & Technical Details
- **Machine:** SonoSite | **Probe:** C60xp/5-2 (curved array) | **Depth:** 14.3 cm
- **Date/Time:** 19 Nov 2018 / 11:20 | **Zone:** Right Z4 (posterior-lateral)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Parenchyma |
|---|---|---|---|
| 1 | Bright, continuous | Discrete B-lines, 2–3 visible | Mildly heterogeneous |
| 2 | Intact | Discrete-to-coalescing B-lines | Heterogeneous, echogenic foci appearing |
| 3 | Intact | Coalescing B-lines | Denser echogenicity deepening |
| 4 | Intact | Confluent bright sheet forming | Hepatized-appearing parenchyma |
| 5 | Intact | Confluent — A-lines largely obscured | Echogenic consolidation, hyperechoic foci |
| 6 | Intact | Confluent/ground-glass pattern | Hyperechoic punctate foci within dense tissue |
| 7 | Intact | Confluent white sheet | Dense consolidation + hyperechoic linear foci |
| 8 | Intact | Partially discrete again | Echogenic mass-like parenchyma, foci visible |
| 9 | Intact | Mixed — discrete + confluent | Consolidation with irregular shredded deep border |
| 10 | Intact | Discrete B-lines re-emerge | Residual hepatization, air bronchogram foci |

---

## B-Lines Assessment

### Observations
- **Frames 1–2:** Discrete, well-separated vertical hyperechoic artifacts arising from the pleural line — classic **septal B-lines** (≤3 per ICS, dark gaps between them)
- **Frames 3–8:** B-lines progressively **coalesce** into a white confluent sheet, obliterating A-lines — **ground-glass pattern**
- **Frames 9–10:** Partial return to discrete B-lines — **septal pattern** re-emerging

### Conclusion
> **lung_rockets = `true`**
> **Subtype = `mixed`**
> *(Septal B-lines dominate early and late frames; ground-glass confluent pattern dominates mid-sequence — indicating dynamic alveolar/interstitial involvement)*

---

## Consolidation Assessment

### Observations
- **Hepatization:** In frames 4–9, the deep lung parenchyma loses its normal aeration appearance and adopts a **liver-like echogenicity** (tissue-like, solid texture)
- **Air bronchograms:** Multiple **punctate and short linear hyperechoic foci** are identifiable *within* the hepatized parenchyma across frames 5–10 — consistent with air-filled bronchi surrounded by consolidated alveoli
- **Shred sign:** Frame 9 demonstrates an **irregular, non-geometric deep border** between aerated and consolidated lung, consistent with a shred sign
- No free pleural effusion is definitively identified in these frames

### Conclusion
> **consolidation = `true`**
> **consolidation_type = `"air_bronchogram"`**
> *(Hepatization present with predominant punctate/linear air bronchograms; shred sign at deep margin in mid-to-late frames)*

---

## Integrated Interpretation

```
lung_rockets:      true
b_line_subtype:    mixed (septal → ground_glass → septal)
consolidation:     true
consolidation_type: air_bronchogram
```

### Clinical Correlation
The combination of:
1. **Mixed B-lines** (interstitial thickening + alveolar flooding)
2. **Consolidation with air bronchograms** (alveolar filling with patent bronchi)
3. **Shred sign** at the aeration boundary

...is highly characteristic of **infectious pneumonia** (bacterial or viral) in the right posterior-lateral zone, with superimposed interstitial involvement. This pattern could also be seen in aspiration pneumonitis or atelectasis with secondary infection. Clinical correlation with fever, WBC, CRP, and sputum culture is recommended.
