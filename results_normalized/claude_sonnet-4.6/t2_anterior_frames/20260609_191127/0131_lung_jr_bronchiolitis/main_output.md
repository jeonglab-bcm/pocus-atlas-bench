# 0131_lung_jr_bronchiolitis

# Left Lung Ultrasound — Sequential Frame Analysis

---

## Frame-by-Frame Observations

### Frames 1–4 (Early Sequence)
| Feature | Observation |
|---|---|
| Pleural line | Bright, smooth, hyperechoic horizontal line visible |
| Deep field | Predominantly **dark/anechoic** below pleural line |
| Artifact pattern | **Horizontal A-lines** dominate → normal reverberation pattern |
| Vertical artifacts | No discrete hyperechoic vertical streaks extending to screen bottom |
| B-lines | **Not identified** |

> ✅ These frames represent a **normally aerated** lung zone with classic A-line pattern.

---

### Frames 5–7 (Transitional Sequence)
| Feature | Observation |
|---|---|
| Pleural line | Increasingly disrupted/irregular |
| Subpleural area | Large **echogenic (bright) mass-like area** emerging |
| Texture | **Tissue-like, hepatized** — resembles liver parenchyma in echogenicity |
| Deep border | Becomes **irregular and ragged** |
| B-lines | Obscured by consolidation |

> ⚠️ Transition from aerated to **consolidated** lung territory becoming apparent.

---

### Frames 8–10 (Late Sequence)
| Feature | Observation |
|---|---|
| Parenchymal texture | Extensive **hepatization** — solid, homogeneous, liver-like echogenicity |
| Deep margin | Markedly **irregular, shredded border** between consolidated and aerated lung |
| Internal foci | Punctate/linear **hyperechoic foci** within the hepatized area consistent with **air bronchograms** |
| Normal aeration artifacts | Absent in affected zone |
| Extent | Consolidation occupies the majority of the scan field |

---

## B-Lines Assessment

### Findings:
- In **Frames 1–4**: Classic A-line pattern; no B-lines meeting diagnostic criteria (no hyperechoic vertical streaks from pleural line to screen bottom)
- In **Frames 5–10**: The field is dominated by consolidation; B-line assessment is not applicable/masked

### Conclusion:
```
lung_rockets = false
```
> No discrete B-lines (septal or ground-glass) are identifiable in the assessable, non-consolidated zone. A-lines predominate in the normally aerated portion.

---

## Consolidation Assessment

### Signs Present:

| Sign | Present | Detail |
|---|---|---|
| **Hepatization** | ✅ Yes | Lung parenchyma loses air artifacts; appears solid with liver-like echogenicity (Frames 6–10) |
| **Shred sign** | ✅ Yes | Irregular, ragged deep border at the consolidation–aeration interface (Frames 7–10) |
| **Air bronchograms** | ✅ Yes | Hyperechoic linear/punctate foci within the hepatized area (Frames 8–10) |

### Conclusion:
```
consolidation = true
consolidation_type = "hepatization"
```
*(with co-existing shred sign at deep margins and air bronchograms internally)*

---

## Summary Interpretation

> This LUS clip demonstrates **progressive left anterior lung consolidation** with **complete hepatization**, a **shred sign** at its deep irregular border, and **air bronchograms**, in a background of otherwise normally aerated lung (A-line pattern). This pattern is most consistent with **lobar or sublobar pneumonia** or significant **atelectasis with secondary consolidation**. The absence of B-lines in the aerated zone argues against concurrent interstitial edema in this field.

**Recommended correlation**: Clinical context (fever, CXR, CT) to differentiate pneumonia from compressive/obstructive atelectasis.
