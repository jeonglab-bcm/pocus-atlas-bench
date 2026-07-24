# 0010_lung_pulmonary-shunt-in-pneumonia

# Lung Ultrasound Analysis — Anterior Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Grayscale Parenchyma | Color Doppler Pattern | Notable Features |
|-------|---------------------|----------------------|-----------------|
| 1 | Heterogeneous, mild brightness | Predominantly blue, small red foci | Subtle hyperechoic punctate foci within parenchyma |
| 2 | Moderately echogenic | Large confluent red signal (superior) | Prominent vascular blush; parenchyma brighter than normal |
| 3 | Diffusely bright | Heavy blue signal scattered | Loss of clear A-line reverberation |
| 4 | Similar to Frame 1 | Blue dominant, red spots | Punctate bright foci visible |
| 5 | Mild-moderate echogenicity | Blue dominant | Preserved background brightness |
| 6 | **Markedly echogenic (hepatized)** | Large red pool (inferior), mixed | Strong suggestion of tissue-like parenchyma; bright foci = possible air bronchograms |
| 7 | Echogenic with linear bright foci | Blue dominant, scattered red | Linear/punctate hyperechoic elements within parenchyma |
| 8 | Moderately echogenic | Blue dominant, mid-lower red | Similar pattern; bright foci persist |
| 9 | Similar to Frame 8 | Blue dominant, central red | Consistent with Frames 7–8 |
| 10 | **Markedly echogenic** | Large red pool (inferior), mixed | Recurrent hepatization with prominent vascular flow |

---

## B-Lines Assessment

### Observations:
- **No classic discrete B-lines** (laser-like vertical artifacts arising from the pleural line) are identifiable as isolated artifacts
- The parenchyma shows **diffuse increased echogenicity** in multiple frames (especially 2, 3, 6, 10), with **loss of A-line pattern**
- This diffuse brightness is more consistent with **confluent/coalescing B-lines** rather than discrete septal B-lines
- In frames with lower echogenicity (1, 4, 5, 7–9), a more mixed pattern with partially discrete vertical foci is suggested at the parenchymal margins

### Conclusion — B-Lines:
> **`lung_rockets = true`**
> **Subtype: `mixed`**
> — Predominantly ground-glass-type confluent brightness in peak-signal frames (2, 3, 6, 10), with intermediate septal-type pattern in lower-signal frames (1, 4, 7–9). The absence of A-lines and diffuse parenchymal brightness strongly support this classification.

---

## Consolidation Assessment

### Observations:
1. **Hepatization**: Multiple frames (notably 2, 6, 10) show parenchymal echogenicity approaching **liver-like texture**, with loss of normal aeration artifact
2. **Air Bronchograms**: Across frames 1, 4, 6, 7, 8, 9 — **punctate and linear hyperechoic foci** are consistently visible *within* the echogenic parenchyma, representing air-filled bronchi within consolidated tissue
3. **Vascularity**: Color Doppler confirms preserved blood flow within the echogenic tissue, confirming viable consolidated lung (not effusion or atelectasis)
4. **Shred sign**: The deep border of the echogenic zone appears irregular and heterogeneous in frames 6 and 10, suggesting a **shred component** at the consolidation margins, though less dominant

### Conclusion — Consolidation:
> **`consolidation = true`**
> **`consolidation_type = "air_bronchogram"`**
> — Tissue-like hepatization is present across multiple frames, with the **predominant pattern being air bronchograms** (punctate/linear hyperechoic foci within consolidated parenchyma). A secondary shred sign is present at consolidation margins.

---

## Summary

```
lung_rockets         = true
b_line_subtype       = "mixed"
consolidation        = true
consolidation_type   = "air_bronchogram"
```

### Clinical Interpretation:
This pattern — **consolidation with air bronchograms** superimposed on a **mixed interstitial (B-line) pattern** — in an **anterior lung zone** is most consistent with:
- **Pneumonia** (most likely): consolidation + air bronchograms + B-lines at margins
- Alternatively, **atelectasis with preserved bronchial patency** (though vascularity argues against complete atelectasis)
- The mixed B-line pattern at consolidation margins may reflect **perilesional interstitial edema or ground-glass change**

> ⚠️ *Correlation with clinical presentation, other lung zones, and additional imaging is recommended.*
