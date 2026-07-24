# 0037_lung_pulmonary-contusion

# Lung Ultrasound — Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Horizontal A-Lines | Deep Field |
|-------|-------------|-------------------|-------------------|------------|
| 1 | Clear, hyperechoic | 1–2 faint discrete streaks | Dominant, regularly spaced | Dark, no hepatization |
| 2 | Clear, hyperechoic | 1–2 faint discrete streaks | Dominant | Dark |
| 3 | Clear, hyperechoic | Faint, isolated streak mid-field | Dominant | Dark |
| 4 | Clear, hyperechoic | ~1–2 discrete streaks | Dominant | Dark |
| 5 | Clear, hyperechoic | Discrete streak, slightly more conspicuous | Dominant | Dark |
| 6 | Clear, hyperechoic | ~1–2 discrete streaks | Dominant | Dark |
| 7 | Clear, hyperechoic | Slightly more prominent vertical artifacts | A-lines visible | Dark |
| 8 | Clear, hyperechoic | ~2 discrete vertical streaks | A-lines visible | Dark |
| 9 | Clear, hyperechoic | Discrete streaks, mid-field | A-lines | Dark |
| 10 | Clear, hyperechoic | 2 discrete vertical streaks | A-lines | Dark |

---

## B-Lines Assessment

### Observations
- The **dominant artifact pattern** across all frames is **A-lines** — regularly spaced horizontal reverberation artifacts parallel to the pleural line, fading with depth. This indicates **predominantly normal aeration**.
- In multiple frames (especially frames 5–10), **1–2 discrete, well-defined vertical hyperechoic streaks** are identifiable, arising from the pleural line and extending toward the deep field. These are separated by visible dark lung parenchyma.
- These vertical artifacts do **not coalesce** into a white sheet; there is no obliteration of A-lines.
- No confluent or ground-glass-type B-line flooding is observed.

### Conclusion
> **lung_rockets = true**
> **subtype = septal**

Discrete, isolated B-lines (≤3 per intercostal space) with preserved dark inter-B-line parenchyma and coexisting A-lines. Consistent with **mild interstitial thickening** (thickened interlobular septa).

---

## Consolidation Assessment

### Observations
- **No tissue-like hepatization**: The lung parenchyma below the pleural line maintains its characteristic dark, aerated appearance — no liver-like echogenicity is present.
- **No shred sign**: The deep border of the image does not show an irregular shredded transition zone.
- **No air bronchograms**: No punctate or linear hyperechoic foci within any solid-appearing parenchymal area.
- The deep field remains uniformly dark/echolucent throughout all 10 frames.

### Conclusion
> **consolidation = false**
> **consolidation_type = null**

---

## Summary

| Parameter | Finding |
|-----------|---------|
| `lung_rockets` | **true** |
| `b_line_subtype` | **septal** |
| `consolidation` | **false** |
| `consolidation_type` | **null** |

**Clinical Interpretation**: This anterior lung zone demonstrates a **predominantly A-line pattern with isolated septal B-lines**, suggesting mild interstitial changes (e.g., early interstitial edema, mild fibrosis, or resolving pathology) without evidence of alveolar flooding or consolidation.
