# 0120_lung_jr_blines

# Lung Ultrasound — Sequential Frame Analysis

## Equipment & Technical Parameters
- **Machine:** SonoSite | **Probe:** L25xp/13-6 (Linear, high-frequency)
- **Preset:** Lung | **Depth:** 4.9 cm | **MI:** 0.8 | **TIS:** 0.3

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Deep Field | Vertical Artifacts | Notes |
|-------|-------------|------------|-------------------|-------|
| 1 | Visible, regular | Moderately bright | 2–3 discrete vertical streaks | Relatively spaced B-lines |
| 2 | Visible | Bright | Multiple vertical lines, moderate spacing | Beginning coalescence |
| 3 | Visible | Bright-white | Multiple B-lines, partially merging | Near-confluent zones |
| 4 | Visible | Moderately bright | Discrete B-lines visible | Septal-type predominance |
| 5 | Visible | Bright | Multiple confluent vertical streaks | Ground-glass zone |
| 6 | Visible | Bright | Mixed discrete + merging | Transition frame |
| 7 | Visible | Very bright | Confluent vertical artifacts | Strong ground-glass pattern |
| 8 | Visible | Moderately bright | 2–3 discrete B-lines | More septal-like spacing |
| 9 | Visible | Bright | Coalescent B-lines | Ground-glass dominance |
| 10 | Visible | Moderately bright | Partially discrete B-lines | Mixed appearance |

---

## B-Lines Assessment

### Qualitative Description
Across all 10 frames, **hyperechoic vertical artifacts** are consistently observed:
- **Origin:** Arise directly from the pleural line
- **Extension:** Propagate to the **bottom of the screen without fading**
- **Quantity:** ≥3 per intercostal space in multiple frames
- **Behavior:** Consistent with lung sliding (frame-to-frame variation consistent with respiratory motion)

### Pattern Classification
- **Frames 1, 4, 8:** B-lines are **relatively discrete and spaced** → *Septal pattern*
- **Frames 3, 5, 7, 9:** B-lines **coalesce and merge** into a diffuse bright sheet, partially obscuring A-lines → *Ground-glass pattern*
- **Frames 2, 6, 10:** **Transitional appearance** with both discrete and confluent zones visible simultaneously

> ⚠️ **No A-line dominance** is observed in any frame; A-lines are largely obliterated by B-line artifacts.

---

## Consolidation Assessment

### Evaluation for Consolidation Signs
| Sign | Finding |
|------|---------|
| **Hepatization** (liver-like echogenicity) | ❌ Absent — no solid parenchymal texture |
| **Shred sign** (irregular deep border) | ❌ Absent — no air-tissue irregular margin |
| **Air bronchograms** (hyperechoic foci within hepatized lung) | ❌ Absent — no punctate/linear bright foci within solid tissue |

The deep field brightness observed is **entirely attributable to confluent B-line artifacts**, not to true parenchymal consolidation.

---

## Conclusions

```
lung_rockets       = true
b_line_subtype     = "mixed"
  ├── septal zones    → frames 1, 4, 8 (discrete, spaced B-lines)
  └── ground_glass    → frames 3, 5, 7, 9 (confluent, sheet-like brightness)

consolidation      = false
consolidation_type = null
```

---

## Clinical Interpretation

The **mixed B-line pattern** in an anterior lung zone is consistent with:

1. **Interstitial syndrome** — thickened interlobular septa (septal B-lines) coexisting with areas of alveolar flooding or dense interstitial edema (ground-glass B-lines)
2. **Differential:** Cardiogenic pulmonary edema (bilateral involvement expected), non-cardiogenic ALI/ARDS, or viral/atypical pneumonitis

> 🔎 **Recommendation:** Correlate with contralateral anterior zone (bilateral B-lines suggest cardiogenic/hydrostatic etiology), posterior/lateral zones for dependent consolidation, and clinical parameters (BNP, fluid status, oxygenation).
