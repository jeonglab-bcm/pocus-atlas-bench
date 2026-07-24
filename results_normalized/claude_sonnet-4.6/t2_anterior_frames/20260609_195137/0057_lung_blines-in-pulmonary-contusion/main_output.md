# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Analysis — Anterior Zone (Sequential 10-Frame Clip)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Pattern Character | Additional Findings |
|-------|-------------|-------------------|-------------------|---------------------|
| 1 | Visible ~2–3 cm | 2–3 discrete hyperechoic vertical streaks | Septal — well-spaced, dark lung between | A-lines partially visible |
| 2 | Visible ~2–3 cm | 2–3 discrete B-lines | Septal — clear spacing preserved | Moderate echogenicity deep field |
| 3 | Visible ~2–3 cm | 3–4 vertical artifacts, mildly widening | Transitional septal → confluent | Faint horizontal A-lines replaced |
| 4 | Visible ~2–3 cm | Multiple B-lines, beginning to coalesce | Mixed — some discrete, some merging | Bright focal spots ~4–5 cm |
| 5 | Visible ~2–3 cm | Multiple coalescing artifacts | Predominantly confluent/ground glass | Bright punctate foci right lateral (~5–6 cm) |
| 6 | Visible ~2–3 cm | Dense confluent vertical sheet | Ground glass — A-lines obliterated | Maximum brightness/whiteout phase |
| 7 | Visible ~2–3 cm | Moderate B-lines, partially discrete | Mixed — transitioning back | Less dense than Frame 6 |
| 8 | Visible ~2–3 cm | Sparse vertical artifacts | Reduced — near septal/clearing | Darker deep field; possible respiration phase |
| 9 | Visible ~2–3 cm | 2–3 discrete B-lines | Septal — returning to baseline | Isolated bright foci |
| 10 | Visible ~2–3 cm | Sparse, near absent | Near A-line dominant | Horizontal reverberation artifacts re-emerging |

---

## B-Lines Assessment

### Observations:
- **Multiple hyperechoic vertical artifacts** arise from the pleural line consistently across frames 1–9
- They **extend to the bottom of the screen (≥10 cm) without fading**, consistent with true B-lines
- **Frames 1–3, 9–10**: Discrete, well-spaced B-lines with preserved dark lung parenchyma between them → **Septal pattern**
- **Frames 5–6**: Artifacts coalesce into a near-confluent white sheet, obliterating A-lines → **Ground glass pattern**
- **Frames 4, 7–8**: Intermediate/mixed morphology visible within the same clip
- Dynamic variation correlates with **respiratory cycle** (likely inspiratory phase = frames 5–6 peak; expiratory phase = frames 8–10 clearing)

### Conclusion:
```
lung_rockets = true
subtype = "mixed"
```
> Discrete septal B-lines and confluent ground-glass B-lines coexist across the clip, likely representing **moderate interstitial syndrome** (e.g., early-to-moderate pulmonary edema or interstitial pneumonia) with respiratory-phase modulation.

---

## Consolidation Assessment

### Observations:
- **No hepatization**: The deep lung parenchyma does **not** adopt a liver-like solid echogenic texture in any frame
- **No shred sign**: The deep border of the lung (where visible) does not show an irregular, shredded interface
- **Bright punctate foci** (frames 5–6, right lateral, ~5–6 cm): These are **embedded within B-line artifacts** and **move with the artifact sweep** — most consistent with **B-line artifact concentration** rather than true static air bronchograms within hepatized tissue
- **No static air bronchograms** identified independent of B-line artifacts
- The anterior lung maintains normal near-field pleural reflection without subpleural consolidation patches

### Conclusion:
```
consolidation = false
consolidation_type = null
```

---

## Summary

| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | ✅ **true** |
| **B-line subtype** | 🔄 **mixed** (septal + ground glass) |
| **consolidation** | ❌ **false** |
| **consolidation_type** | **null** |

### Clinical Interpretation:
This pattern — **mixed B-lines (septal + ground glass) without consolidation** in the anterior lung zone — is characteristic of **moderate pulmonary interstitial syndrome**, most consistent with:
- **Cardiogenic pulmonary edema** (bilateral B-lines, anterior predominance)
- **Viral/atypical pneumonia** (e.g., COVID-19 interstitial pattern)
- **ARDS early phase**

Correlation with bilateral findings, clinical context, and cardiac ultrasound is recommended.
