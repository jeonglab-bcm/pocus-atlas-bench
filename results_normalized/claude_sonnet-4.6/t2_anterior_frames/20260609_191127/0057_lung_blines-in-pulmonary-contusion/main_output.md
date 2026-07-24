# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Analysis — Anterior Zone (10-Frame Sequential Clip)

---

## 🔬 Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Parenchymal Pattern | Consolidation Signs |
|-------|-------------|-------------------|--------------------|--------------------|
| 1 | Visible ~2–3 cm | 1–2 discrete hyperechoic vertical artifacts | Moderately echogenic | None |
| 2 | Visible | 1–2 spaced vertical streaks | Moderate echogenicity | None |
| 3 | Visible | 1–2 discrete B-lines | Moderate | None |
| 4 | Visible | 2–3 discrete, well-separated B-lines | Patchy bright areas | None definitive |
| 5 | Visible | Multiple B-lines; some right-field coalescing | Brighter parenchyma, focal bright punctate foci | Possible early confluent |
| 6 | Visible | Multiple B-lines; right portion shows near-confluent sheet | Uniformly bright right field | No hepatization |
| 7 | Visible | Reduced count; 1–2 artifacts | Moderate | None |
| 8 | Visible | Few vertical artifacts | Upper field echogenic, brighter | No clear hepatization/shred |
| 9 | Visible | 2–3 discrete B-lines | Moderate echogenicity | None |
| 10 | Visible | 2–3 discrete, spaced B-lines | Moderate | None |

---

## 📊 B-Lines Assessment

### Presence
> **lung_rockets = `true`**

**Observations:**
- Vertical hyperechoic artifacts arise from the pleural line in **all 10 frames**
- They extend to the **bottom of the screen without fading**
- They move with respiratory/sliding motion (consistent with genuine B-lines)
- In **Frames 1–4, 7–10**: ≤3 discrete, clearly separated B-lines per intercostal space — dark parenchyma visible *between* them
- In **Frames 5–6**: B-lines become more numerous and begin to **coalesce** in the right field, forming a near-confluent bright sheet that partially obscures A-lines

### Subtype
> **`mixed`**

| Region/Frames | Pattern | Interpretation |
|--------------|---------|----------------|
| Frames 1–4, 7–10 | Discrete, spaced B-lines | **Septal** — thickened interlobular septa |
| Frames 5–6 (right field) | Confluent, merging into white sheet | **Ground-glass** — alveolar edema or diffuse interstitial disease |

---

## 🫁 Consolidation Assessment

### Presence
> **consolidation = `false`**

**Observations:**
- No **hepatization** seen: parenchyma does not acquire liver-like solid echogenicity uniformly
- No definitive **shred sign**: deep borders, where visible, are not sharply irregular/shredded
- The bright punctate foci in Frames 5–6 represent **B-line artifacts**, not air bronchograms within hepatized tissue
- Frame 8 shows a focal brighter superficial zone but lacks the solid tissue-like texture required for consolidation classification

> **consolidation_type = `null`**

---

## ✅ Final Conclusions

```
lung_rockets        = true
b_line_subtype      = mixed
  - Dominant:       septal  (Frames 1–4, 7–10)
  - Focal:          ground_glass (Frames 5–6, right field)

consolidation       = false
consolidation_type  = null
```

### Clinical Interpretation
This pattern is consistent with **bilateral/focal interstitial syndrome** (e.g., early-to-moderate cardiogenic pulmonary edema, non-cardiogenic pulmonary edema, or interstitial pneumonitis). The mixed B-line pattern — transitioning from septal to near-confluent ground-glass across frames — suggests **heterogeneous interstitial fluid distribution** rather than a uniform alveolar process. No consolidation is evident in the anterior zone examined.
