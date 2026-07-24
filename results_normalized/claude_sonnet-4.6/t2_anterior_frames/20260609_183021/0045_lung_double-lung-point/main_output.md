# 0045_lung_double-lung-point

# Left Lung Anterior Zone — Sequential LUS Frame Analysis

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Field | A-lines |
|-------|-------------|-------------------|------------|---------|
| 1 | Bright, smooth | Faint, single vertical streak | Dark/anechoic | Faint horizontal reverberations |
| 2 | Bright, smooth | Minimal | Dark | Present |
| 3 | Bright, slightly irregular | 1 discrete vertical artifact | Dark | Present |
| 4 | Bright | 1–2 discrete B-lines visible | Dark | Partially obscured |
| 5 | Bright | 1–2 discrete B-lines | Dark | Present |
| 6 | Bright, complex | Discrete vertical artifact | Dark | Present |
| 7 | Bright | Discrete single artifact | Dark | Present |
| 8 | Bright | 1 discrete vertical streak | Dark | Present |
| 9 | Bright, prominent | 1–2 discrete B-lines | Dark | Partially present |
| 10 | Bright | 1–2 discrete B-lines | Dark | Faint |

---

## B-lines Assessment

**Findings:**
- Discrete hyperechoic vertical artifacts arise from the pleural line in multiple frames
- They extend toward the far field without fading
- **Dark lung parenchyma is preserved between artifacts** (no merging or confluence)
- Lung sliding is visible (pleural line moves across frames)
- ≤2–3 B-lines per intercostal space at any one time
- No diffuse white-sheet appearance or A-line obliteration

> ✅ **lung_rockets = true**
> 📋 **Subtype: `septal`**
> *Discrete, well-spaced B-lines with preserved dark parenchyma between them, consistent with thickened interlobular septa (e.g., mild interstitial edema or early ILD)*

---

## Consolidation Assessment

**Findings:**
- No tissue-like hepatization (liver-echotexture) identified
- No shred sign at deep lung border
- No air bronchograms (punctate or linear hyperechoic foci within solid lung)
- Pleural line remains well-defined with no subpleural consolidation

> ❌ **consolidation = false**
> 🔘 **consolidation_type = null**

---

## Summary

```
lung_rockets      = true
b_line_subtype    = "septal"
consolidation     = false
consolidation_type = null
```

**Interpretation:** This anterior left lung zone demonstrates a **septal B-line pattern** (sparse, discrete B-lines with preserved A-lines and dark inter-B-line spaces), suggesting mild-to-moderate interstitial thickening without alveolar flooding or consolidation. This pattern may be seen in early cardiogenic pulmonary edema, mild interstitial pneumonia, or chronic interstitial lung disease.
