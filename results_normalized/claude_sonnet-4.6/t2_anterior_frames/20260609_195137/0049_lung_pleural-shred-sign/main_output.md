# 0049_lung_pleural-shred-sign

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Field | A-lines |
|-------|-------------|-------------------|------------|---------|
| 1 | Bright, continuous hyperechoic line | 2–3 discrete vertical streaks arising from pleural line | Dark, echolucent | Partially visible |
| 2 | Bright, continuous | Discrete vertical artifacts persisting | Dark | Partially visible |
| 3 | Bright, continuous | 2–3 discrete B-lines; spaced apart | Dark between B-lines | Faintly visible |
| 4 | Bright, continuous | Similar discrete vertical artifacts | Dark | Partially suppressed |
| 5 | Bright, continuous | Discrete B-lines; dark parenchyma between them | Dark | Partially visible |
| 6 | Bright, continuous | Vertical artifacts stable | Dark | Partially visible |
| 7 | Bright, continuous | 2–3 B-lines, clearly separated | Dark | Partially suppressed |
| 8 | Bright, continuous | Discrete B-lines persist | Dark | Partially visible |
| 9 | Bright, continuous | B-lines stable, well-spaced | Dark | Faintly visible |
| 10 | Bright, continuous | B-lines persist with dark intervening lung | Dark | Partially visible |

---

## B-lines Assessment

### Observations:
- **Pleural line**: Clearly defined, bright, continuous horizontal hyperechoic line in all frames
- **Vertical artifacts**: 2–3 discrete, hyperechoic vertical artifacts arise directly from the pleural line in every frame, extending to the **bottom of the screen without fading**
- **Spacing**: The B-lines are **clearly separated** from one another; dark (echolucent) lung parenchyma is visible **between** each B-line
- **A-lines**: Present but **partially suppressed** beneath the B-lines — consistent with true B-line physiology
- **Confluency**: B-lines do **not** merge or coalesce into a diffuse white sheet; discrete boundaries are maintained throughout all frames

### Classification:
| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | ✅ **true** |
| **Subtype** | **septal** — discrete, well-spaced B-lines (≤3 per ICS) with dark lung parenchyma visible between them |

> **Interpretation**: Thickened interlobular septa — consistent with mild interstitial syndrome (e.g., early cardiogenic pulmonary edema, mild interstitial pneumonia, or interstitial fibrosis)

---

## Consolidation Assessment

### Observations:
- **Hepatization**: ❌ No tissue-like, liver-echogenicity parenchyma observed — the deep lung field remains uniformly dark
- **Shred sign**: ❌ No irregular, shredded deep border between consolidated and aerated lung
- **Air bronchograms**: ❌ No punctate or linear hyperechoic foci within any consolidated region

### Classification:
| Parameter | Finding |
|-----------|---------|
| **consolidation** | ❌ **false** |
| **consolidation_type** | **null** |

---

## Summary Conclusion

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = false
consolidation_type = null
```

> This pattern — **discrete septal B-lines** in the anterior zone **without consolidation** — is most consistent with a **mild-to-moderate interstitial syndrome**, such as early pulmonary edema or interstitial lung disease, with preserved alveolar aeration in this zone.
