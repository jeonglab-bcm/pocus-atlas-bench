# 0072_lung_m01vhapdm99ri51nm8bbpce5wev26y

# Lung Ultrasound Analysis — Miliary TB Sequential Frames

---

## Frame-by-Frame Observations

### Frames 1–6 (Anatomical Landmark Frames)

| Structure | Observation |
|-----------|-------------|
| **Soft Tissue** | Normal superficial echogenicity |
| **Ribs** | Hyperechoic with posterior acoustic shadowing |
| **Pleural Line** | Visible but **irregular/nodular** — not smooth as in normal lung |
| **Lung Field** | Vertical hyperechoic artifacts emerging from pleural line; progressive clarity across frames |

> The pleural line shows **progressive irregularity** across frames 1→6, with subtle nodular disruptions becoming more apparent.

---

### Frames 7–10 (Pathology Annotation Frames)

| Finding | Observation |
|---------|-------------|
| **Sub-pleural nodules (bilateral)** | Small hypoechoic/echogenic foci disrupting the pleural line on **both left and right** sides — characteristic of subpleural granulomas |
| **B-lines** | **3 discrete, well-defined hyperechoic vertical artifacts** arising from the pleural line (origin points coinciding with nodule sites), extending to the **bottom of the screen without fading** |
| **Spacing between B-lines** | Dark lung parenchyma is **visible between each B-line** — no confluence or merging |
| **A-lines** | **Absent/obscured** beneath B-line origins |

---

## B-Lines Assessment

### ✅ `lung_rockets = TRUE`

**Morphological criteria met:**
- Hyperechoic vertical artifacts arising **from the pleural line**
- Extend to **screen bottom without fading**
- Discrete with **interspace dark parenchyma preserved**
- ≤3 clearly separated B-lines per intercostal space

### Subtype Classification: **`septal`**

```
Rationale:
- B-lines are DISCRETE, not confluent
- Dark lung parenchyma visible BETWEEN each artifact
- No white-sheet coalescence (rules out ground_glass)
- Origin points coincide with subpleural nodules
  → granuloma-driven thickening of subpleural/interlobular septa
```

> ⚠️ In Miliary TB specifically, septal B-lines arise from **subpleural miliary granulomas** rather than cardiac/hydrostatic edema — a distinct mechanism producing identical artifact morphology.

---

## Consolidation Assessment

### ❌ `consolidation = FALSE`

| Sign | Present? | Observation |
|------|----------|-------------|
| **Hepatization** | ❌ | No liver-like echogenicity; lung not solid |
| **Shred sign** | ❌ | No irregular shredded deep border |
| **Air bronchograms** | ❌ | No punctate/linear hyperechoic foci within hepatized tissue |

> Sub-pleural nodules are **micro-focal** (millimeter-scale granulomas) and do **not** constitute alveolar consolidation by LUS criteria.

### `consolidation_type = null`

---

## Summary

```
┌─────────────────────────────────────────────────┐
│  lung_rockets    = TRUE                         │
│  b_line_subtype  = "septal"                     │
│  consolidation   = FALSE                        │
│  consolidation_type = null                      │
└─────────────────────────────────────────────────┘
```

**Interpretation:** This LUS pattern — **bilateral sub-pleural nodules generating discrete septal B-lines** without consolidation — is the **characteristic sonographic signature of Miliary TB**. The nodules physically disrupt pleural line continuity and act as point-source generators of B-line artifacts, distinguishing this pattern from cardiogenic edema (diffuse, gravity-dependent ground_glass B-lines) or bacterial pneumonia (hepatization ± air bronchograms).
