# 0072_lung_m01vhapdm99ri51nm8bbpce5wev26y

# Lung Ultrasound Analysis — Miliary TB (Sequential Frames)

---

## Frame-by-Frame Observations

### Frames 1–6 (Anatomical Landmark Frames)

| Feature | Observation |
|---|---|
| Soft tissue | Normal superficial layer |
| Ribs | Bilateral acoustic shadows, normal appearance |
| Pleural line | **Irregular, thickened, nodular** — not smooth as in normal lung |
| Sub-pleural zone | Progressive revelation of **focal hypoechoic interruptions** at pleural surface |
| Deep field | Vertical artifact emergence increasing across frames |

> The pleural line shows progressive irregularity across frames 1→6, with punctate hyperechoic foci beginning to emerge at the pleural-lung interface.

---

### Frames 7–10 (Annotated Pathology Frames)

| Feature | Observation |
|---|---|
| **Sub-pleural nodules** | **Bilateral**, small hypoechoic/isoechoic foci **interrupting the pleural line** — characteristic of miliary seeding |
| **B-lines** | **Multiple (≥3)** vertical hyperechoic artifacts arising directly from sub-pleural nodule sites |
| B-line character | Arise from discrete nodular origins → **converge and coalesce** distally toward screen bottom |
| A-lines | **Absent** — obliterated by B-line density |
| Deep lung | Dark, no hepatization pattern |

---

## B-Lines Assessment

### ✅ `lung_rockets = true`

**Evidence:**
- Multiple hyperechoic vertical artifacts arising from the pleural line
- Extend to the **bottom of the screen without fading**
- Originate from sub-pleural nodule sites (miliary granulomas acting as B-line generators)
- A-lines are abolished

### Subtype: **`mixed`**

| Pattern Component | Frames | Appearance |
|---|---|---|
| **Septal** component | Early frames (1–4) | Discrete, spaced B-lines with dark lung parenchyma between them |
| **Ground-glass** component | Later frames (5–10) | B-lines converge and coalesce distally, merging into a whitish sheet |

> In miliary TB, each sub-pleural granuloma generates its own focal B-line; when numerous, they coalesce — producing a **mixed septal + ground-glass pattern** depending on density and spatial distribution.

---

## Consolidation Assessment

### ❌ `consolidation = false`
### `consolidation_type = null`

**Reasoning:**

| Sign | Present? | Comment |
|---|---|---|
| Hepatization | ❌ | No liver-like echogenicity of lung parenchyma |
| Shred sign | ❌ | No irregular deep border between consolidated/aerated zones |
| Air bronchograms | ❌ | No hyperechoic linear/punctate foci within consolidated tissue |

> ⚠️ **Important distinction**: The **sub-pleural nodules** represent **focal pleural-surface granulomas** (< 5mm), not alveolar consolidation in the classical LUS sense. They are pathognomonic of miliary pattern but do not meet threshold criteria for consolidation scoring.

---

## Final Conclusions

```
lung_rockets     = true
b_line_subtype   = "mixed"
consolidation    = false
consolidation_type = null
```

### Clinical Correlation — Miliary TB LUS Pattern

| Finding | Significance |
|---|---|
| Bilateral sub-pleural nodules | Hematogenous miliary seeding of pleural surface |
| Mixed B-line pattern | Interstitial involvement with focal alveolar component |
| Irregular pleural line | Granulomatous pleural thickening |
| No consolidation | Disease is **interstitial/miliary phase**, not pneumonic phase |

> This ultrasound pattern — **bilateral sub-pleural nodules + mixed B-lines + irregular pleural line** — is the characteristic triad of **miliary tuberculosis on lung ultrasound** and should prompt urgent clinical workup (sputum AFB, IGRA, CT chest).
