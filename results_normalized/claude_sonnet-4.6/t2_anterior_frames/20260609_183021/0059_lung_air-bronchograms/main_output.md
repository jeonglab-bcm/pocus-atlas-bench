# 0059_lung_air-bronchograms

# Lung Ultrasound Analysis — Right Zone 4 (Sequential Frame Review)

## Technical Context
- **Machine**: SonoSite | **Probe**: C60xp/5-2 (curved array)
- **Setting**: ED | **Date**: 19 Nov 2018, 11:20
- **Depth**: 14.3 cm | **Zone**: Right Z4 (right lateral/basal zone)

---

## Frame-by-Frame Analysis

| Frame | Pleural Line | Vertical Artifacts | Deep Field |
|---|---|---|---|
| 1 | Visible, bright | Multiple coalescing hyperechoic streaks | Increased echogenicity, heterogeneous |
| 2 | Visible | Confluent vertical artifacts, A-lines obscured | Emerging tissue-like density |
| 3 | Visible | Coalescing B-lines, bright near field | Clear hepatization with bright foci |
| 4 | Visible | Multiple fusing vertical streaks | Consolidated region with punctate hyperechoic spots |
| 5 | Visible | Confluent, "white lung" pattern emerging | Hepatized parenchyma with air bronchograms |
| 6 | Visible | Dense, merging B-lines | Multiple punctate/linear bright foci within echogenic tissue |
| 7 | Visible | Coalescing vertical artifacts | Shredded deep border visible |
| 8 | Visible | Confluent B-line sheet | Hepatization + scattered air bronchograms |
| 9 | Visible | Dense vertical artifacts from pleural line | Consolidated tissue with bright inclusions |
| 10 | Visible | Multiple fusing B-lines | Irregular border between consolidated/aerated lung |

---

## B-Lines Assessment

### Observations
- **Across all 10 frames**, multiple hyperechoic vertical artifacts arise from the pleural line and extend to the bottom of the screen without fading
- The artifacts **coalesce and merge** into a confluent bright sheet, **abolishing A-line visibility**
- The subpleural field appears **uniformly white/bright**, consistent with massive B-line confluence
- No discrete, well-separated (septal) B-lines are identifiable; all artifacts fuse together

### Conclusion
```
lung_rockets = true
subtype = "ground_glass"
```
> Confluent/coalescing B-lines forming a diffuse white lung appearance, indicating severe interstitial–alveolar involvement (alveolar flooding or diffuse interstitial disease)

---

## Consolidation Assessment

### Observations
- **Hepatization**: In frames 3–10, the mid-to-deep lung parenchyma demonstrates **liver-like echogenicity** — solid, homogeneously echogenic tissue replacing normal aerated lung
- **Air bronchograms**: Within the consolidated region, **multiple punctate and short linear hyperechoic foci** are consistently visible across frames, representing **air-filled bronchi** trapped within consolidated lung
- **Shred sign**: Frames 7–10 show an **irregular, jagged deep border** between the consolidated and still-aerated lung tissue
- No anechoic fluid (hepatic or pleural) noted to confound the consolidated tissue appearance

### Conclusion
```
consolidation = true
consolidation_type = "air_bronchogram"
```
> Hepatized lung parenchyma with prominent punctate/linear air bronchograms is the predominant finding; shred sign is secondarily present at the deep margin

---

## Integrated Interpretation

| Parameter | Finding |
|---|---|
| **lung_rockets** | ✅ TRUE |
| **B-line subtype** | Ground glass (confluent) |
| **consolidation** | ✅ TRUE |
| **consolidation_type** | Air bronchogram (within hepatized lung) |

### Clinical Correlation
The combination of:
1. **Confluent ground-glass B-lines** (surrounding aerated zones)
2. **Lobar/segmental consolidation with air bronchograms** (right basal zone)
3. **Shred sign** at the consolidation margin

is **highly characteristic of bacterial pneumonia** (right lower lobe), where consolidated parenchyma coexists with reactive interstitial edema in the perilesional lung. This pattern should be distinguished from cardiogenic pulmonary edema (bilateral symmetric ground-glass B-lines without air bronchograms).

> ⚠️ *Clinical correlation with history, fever, CRP, and further imaging (CT) is recommended.*
