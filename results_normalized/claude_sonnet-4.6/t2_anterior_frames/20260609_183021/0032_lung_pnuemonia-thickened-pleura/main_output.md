# 0032_lung_pnuemonia-thickened-pleura

# Lung Ultrasound Analysis — RT H/T Zone 3 Low (Sequential Frames)

---

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| 1–2 | Pleural line clearly visible; **2–3 discrete vertical hyperechoic artifacts** arising perpendicularly from pleural line, extending to far field; dark inter-artifact spaces preserved |
| 3–4 | B-line artifacts persist; remain distinct and separated; no coalescence into white sheet; A-lines partially suppressed but not abolished |
| 5–6 | Consistent discrete vertical artifacts; **dark lung parenchyma visible between lines**; pleural line shows subtle sliding motion |
| 7–8 | Slight variation in near-field appearance (probe angulation); B-lines remain separated; no new artifacts; no deep border abnormality |
| 9–10 | Pattern stable; vertical artifacts discrete; **no merging or confluent white shading**; deep pleural border appears regular |

---

## B-Lines Assessment

### Presence
> **lung_rockets = ✅ TRUE**

**Criteria met:**
- Hyperechoic vertical artifacts originating at the pleural line
- Extend to the **bottom of the screen without fading**
- Move synchronously with lung sliding
- Well-defined, laser-like appearance

### Subtype Classification
> **Subtype = SEPTAL**

**Supporting evidence:**
- ≤3 discrete B-lines per intercostal space visible across frames
- **Clear dark lung parenchyma preserved between each B-line**
- No coalescence or merging into a diffuse white "ground-glass" sheet
- A-lines partially visible in far field beyond B-lines
- Pattern consistent with **thickened interlobular septa** (e.g., mild interstitial edema, early pulmonary congestion, or interstitial fibrosis)

---

## Consolidation Assessment

> **consolidation = ❌ FALSE**

**Assessment per sign:**

| Sign | Finding |
|------|---------|
| **Hepatization** | ❌ Not present — no tissue-like, liver-echogenicity area |
| **Shred sign** | ❌ Not present — deep border is smooth and regular |
| **Air bronchograms** | ❌ Not present — no punctate/linear hyperechoic foci within parenchyma |

> **consolidation_type = null**

---

## Summary

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = false
consolidation_type = null
```

**Interpretation:** This right anterior zone 3 clip demonstrates a **septal B-line pattern** (moderate interstitial syndrome) without evidence of alveolar consolidation. The discrete, well-spaced B-lines with preserved dark inter-line spaces are characteristic of **thickened interlobular septa**, most commonly seen in interstitial pulmonary edema (e.g., early/moderate cardiogenic pulmonary edema, viral pneumonitis, or interstitial lung disease).
