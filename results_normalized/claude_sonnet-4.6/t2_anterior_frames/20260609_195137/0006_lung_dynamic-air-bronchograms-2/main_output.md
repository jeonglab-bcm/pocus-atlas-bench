# 0006_lung_dynamic-air-bronchograms-2

# Lung Ultrasound Analysis — Anterior Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| 1–3 | Pleural line visible; **discrete, well-separated vertical hyperechoic streaks** arising from pleural line — early/septal B-line pattern |
| 4–6 | B-lines **increase in density**; adjacent lines begin to coalesce; background lung parenchyma appears progressively brighter — transition toward ground-glass pattern |
| 7–8 | A **hypoechoic region** emerges in the mid-field with **punctate/linear hyperechoic foci** within it; A-lines absent; possible early consolidation |
| 9–10 | Pattern stabilizes; confluent B-lines dominate; **bright echogenic foci within the hypoechoic parenchymal zone** consistent with air bronchograms |

---

## B-Lines Assessment

**`lung_rockets = true`**

> Multiple vertical hyperechoic artifacts originate from the pleural line, extend without fading to the bottom of the screen, and move with lung sliding. A-lines are **absent**.

**Subtype: `mixed`**

- **Septal component** (frames 1–3): Discrete, countable B-lines (~3–4 per ICS) with hypoechoic lung visible between them
- **Ground-glass component** (frames 4–10): B-lines coalesce into a near-confluent white sheet, obscuring the normal parenchymal pattern

---

## Consolidation Assessment

**`consolidation = true`**

**`consolidation_type = "air_bronchogram"`**

Observed features (frames 7–10):
- ✅ **Tissue-like hypoechoic region** with loss of normal aeration artifacts (partial hepatization)
- ✅ **Punctate and short linear hyperechoic foci** within the consolidated parenchyma — consistent with **air bronchograms**
- ❌ No well-defined shred sign at the deep border (border is relatively smooth)

---

## Summary & Interpretation

```
lung_rockets       : true
b_line_subtype     : mixed (septal → ground_glass progression)
consolidation      : true
consolidation_type : air_bronchogram
```

> **Clinical Correlation**: The combination of confluent/mixed B-lines and air bronchograms in the anterior zone suggests **alveolar filling pathology** — most consistent with **pneumonia** (community-acquired or atypical) or **pulmonary edema with superimposed consolidation**. The air bronchograms favor an **infectious/inflammatory** etiology over pure hydrostatic edema.
