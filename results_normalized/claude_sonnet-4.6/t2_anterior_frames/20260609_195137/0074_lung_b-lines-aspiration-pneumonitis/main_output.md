# 0074_lung_b-lines-aspiration-pneumonitis

# Lung Ultrasound Analysis — LS7 Anterior Zone

---

## Frame-by-Frame Observations

### Frames 1–5 (Unlabeled/Early Sequence)

| Frame | Pleural Line | Vertical Artifacts | Deep Field |
|-------|-------------|-------------------|------------|
| 1 | Visible, smooth | 1–2 discrete hyperechoic vertical artifacts from pleural line | Mostly anechoic |
| 2 | Visible, smooth | 1–2 discrete B-lines, some early coalescence | Mostly anechoic |
| 3 | Visible | Right lateral reverberation artifacts (rib shadowing); 1–2 B-lines centrally | Anechoic |
| 4 | Visible | Vertical artifacts becoming slightly more confluent | Anechoic |
| 5 | Visible | Similar to frame 4; vertical comet-tail artifacts with minimal merging | Anechoic |

**Key observation (Frames 1–5):** Predominantly **discrete, well-spaced** vertical hyperechoic artifacts consistent with **septal B-lines**, with dark parenchyma visible between them. No complete coalescence yet.

---

### Frames 6–10 (Timestamped: 03/28/21 02:34:46–02:34:48 AM)

| Frame | Pleural Line | Vertical Artifacts | Deep Field |
|-------|-------------|-------------------|------------|
| 6 | Thickened, echogenic | Multiple vertical artifacts; early merging centrally | Anechoic |
| 7 | Thickened, echogenic | Artifacts coalescing into a **brighter white sheet** centrally | Anechoic |
| 8 | Thickened | Confluent vertical artifacts dominating mid-field | Anechoic |
| 9 | Thickened | Near-complete **merging of B-lines** into a diffuse white zone | Anechoic |
| 10 | Thickened | Full confluence of B-lines; A-lines **obliterated** centrally | Anechoic |

**Key observation (Frames 6–10):** Transition to **confluent, coalescing vertical artifacts** creating a diffuse white curtain — characteristic of the **ground-glass** B-line pattern. A-lines are completely obliterated in these frames.

---

## B-Lines Assessment

### ✅ B-lines Present: `lung_rockets = true`

**Evidence:**
- Hyperechoic vertical artifacts arise **directly from the pleural line**
- Extend to the **bottom of the screen** without fading
- Move in synchrony with the pleural line (lung sliding)
- No A-line horizontal reverberation dominance

### Subtype: `mixed`

| Pattern Component | Frames | Characteristics |
|-------------------|--------|-----------------|
| **Septal** | 1–4 | Discrete, spaced B-lines; dark parenchyma visible between them; ≤3 per ICS |
| **Ground-glass** | 7–10 | Confluent white sheet; B-lines merge; A-lines obliterated; uniformly bright pleural surface |

> The clip demonstrates a **temporal evolution** from septal to ground-glass pattern across frames — this dynamic transition is the basis for the **mixed** classification.

---

## Consolidation Assessment

### ❌ Consolidation: `consolidation = false`

**Assessment by sign:**

| Sign | Finding |
|------|---------|
| **Hepatization** | ❌ Absent — no liver-like echogenicity of parenchyma |
| **Shred sign** | ❌ Absent — no irregular deep border between consolidated and aerated lung |
| **Air bronchograms** | ❌ Absent — no punctate or linear hyperechoic foci within parenchyma |

> The deep field remains **anechoic** throughout all frames. The echogenicity is confined to **vertical artifacts** (B-lines) arising from the pleural line — not from parenchymal consolidation.

`consolidation_type = null`

---

## Summary

```
lung_rockets     = true
b_line_subtype   = "mixed"   (septal → ground_glass temporal evolution)
consolidation    = false
consolidation_type = null
```

### Clinical Interpretation
The **mixed B-line pattern** with progression from septal to ground-glass suggests **increasing interstitial/alveolar fluid** — raising concern for **pulmonary edema (cardiogenic or non-cardiogenic)** or **diffuse interstitial lung disease**. The absence of consolidation argues against pneumonia as the primary etiology, though clinical correlation is essential.
