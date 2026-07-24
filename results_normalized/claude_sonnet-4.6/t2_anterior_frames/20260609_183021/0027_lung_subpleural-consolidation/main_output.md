# 0027_lung_subpleural-consolidation

# Lung Ultrasound Analysis — RT H/T Zone 1 (Right Anterior Zone)
## Sequential Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| **1** | Pleural line visible; deep parenchyma appears uniformly hypoechoic/dark; no vertical artifacts |
| **2** | Similar dark parenchyma; no B-line artifacts; A-line pattern absent |
| **3** | Emerging subtle rounded hypoechoic structure just below pleural line |
| **4** | **Well-defined, round hypoechoic subpleural nodule** becomes clearly visible; smooth borders; homogeneous interior |
| **5** | Nodule persists; surrounding parenchyma shows mild echogenicity; no vertical artifacts |
| **6** | Nodule clearly defined; no hyperechoic streaks extending to screen bottom |
| **7** | Structure begins to elongate/show adjacent component; still subpleural |
| **8** | **Two adjacent round/oval hypoechoic structures** now visible — likely two subpleural consolidations |
| **9** | Twin subpleural nodules persist; tissue-like echogenicity within each |
| **10** | Consolidations remain; deep parenchyma dark without aeration reverberation |

---

## B-Lines Assessment

### Observations:
- No hyperechoic vertical artifacts arising from the pleural line are identified in any frame
- No "comet tail" artifacts extending to the bottom of the screen
- No confluent white-sheet pattern consistent with ground-glass B-lines
- Deep parenchyma is predominantly **dark/hypoechoic** rather than showing reverberation artifact stacking

### Conclusion:
> **lung_rockets = false**
> No B-lines (septal, ground_glass, or mixed) are present

---

## Consolidation Assessment

### Observations:
- **Frames 4–10**: One to two well-defined, **round/oval subpleural hypoechoic nodules** are visible immediately deep to the pleural line
- The internal echogenicity of the structures is **tissue-like** — resembling solid organ (liver-like) texture
- **No air bronchograms** (hyperechoic punctate/linear foci) are identified within the structures
- **No shred sign** (irregular deep border) — borders are relatively smooth
- The structures persist across multiple frames, confirming they are real findings and not artifact
- No normal A-line pattern is visible beneath these structures — the parenchyma is occupied by consolidated tissue

### Conclusion:
> **consolidation = true**
> **consolidation_type = "hepatization"**

---

## Summary

| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | `false` |
| **B-line subtype** | `null` |
| **consolidation** | `true` |
| **consolidation_type** | `"hepatization"` |

### Clinical Interpretation:
The sequential frames reveal **subpleural consolidation(s) with tissue-like (hepatized) echogenicity** in the right anterior zone, without associated B-lines. This pattern is most consistent with:
- **Focal pneumonia** (subpleural consolidative pneumonia)
- **Subpleural atelectasis**
- Possibly **pulmonary infarction** (Hampton's hump equivalent on US)

The absence of B-lines argues against cardiogenic pulmonary edema or diffuse interstitial disease as the primary process. Clinical correlation with symptomatology, fever, and additional zones is recommended.
