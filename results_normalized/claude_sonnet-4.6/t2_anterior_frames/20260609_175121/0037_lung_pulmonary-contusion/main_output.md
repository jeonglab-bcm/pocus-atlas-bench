# 0037_lung_pulmonary-contusion

# Lung Ultrasound — Sequential Frame Analysis

---

## Frame-by-Frame Observations

| Frames | Pleural Line | Deep Field | Vertical Artifacts | A-Lines |
|--------|-------------|------------|-------------------|---------|
| 1–2 | Clear, hyperechoic, smooth | Predominantly dark/anechoic | None clearly identified | Dominant horizontal reverberation artifacts |
| 3–4 | Clear, visible | Dark | 1 faint discrete vertical artifact possible | A-lines visible |
| 5–7 | Clear, bright | Dark with subtle brightness | **1–2 discrete, narrow, hyperechoic vertical artifacts** arising from pleural line, extending deep | Partially interrupted where verticals present |
| 8–10 | Clear | Dark | Possible 1 discrete vertical artifact | A-lines re-emerge as dominant |

---

## B-Lines Assessment

### Observations:
- The **dominant pattern** across all frames is **A-lines** — well-defined, horizontal, parallel reverberation artifacts below the pleural line at equally spaced intervals, consistent with **normal/near-normal lung aeration**
- In frames **5–7**, **1–2 discrete, narrow, hyperechoic vertical artifacts** are seen arising from the pleural line, appearing to extend toward the deep field without clear fading — these meet partial criteria for B-lines
- These vertical artifacts are:
  - **Well-spaced** (not confluent)
  - **Dark lung parenchyma visible between them**
  - **Not merging into a white sheet**
  - **Not ≥3 per intercostal space**
- No coalescing or ground-glass type flooding of the screen observed

### Conclusion:
> **lung_rockets = true**
> **Subtype: `septal`**
> Sparse, discrete, well-spaced B-lines (1–2 per intercostal space) visible in mid-clip frames, with preserved dark lung parenchyma between them — consistent with focally thickened interlobular septa. A-lines remain the dominant pattern overall.

---

## Consolidation Assessment

### Observations:
- **No tissue-like hepatization** — lung parenchyma does not display liver-like echogenicity
- **No shred sign** — no irregular/shredded deep border visible
- **No air bronchograms** — no punctate or linear hyperechoic foci within any solid-appearing region
- The deep lung field remains **dark and anechoic**, consistent with aerated lung

### Conclusion:
> **consolidation = false**
> **consolidation_type = null**
> No consolidation signs identified in any frame.

---

## Summary

| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | ✅ `true` |
| **B-line subtype** | `septal` |
| **consolidation** | ❌ `false` |
| **consolidation_type** | `null` |

**Clinical Interpretation:** This anterior lung zone shows a **predominantly A-line pattern with sparse septal B-lines** (1–2 per window in some frames). This is consistent with **minimal interstitial thickening** (e.g., early/mild interstitial edema, early fibrosis, or physiological variant) without frank alveolar involvement or consolidation. A-line dominance suggests maintained global aeration.
