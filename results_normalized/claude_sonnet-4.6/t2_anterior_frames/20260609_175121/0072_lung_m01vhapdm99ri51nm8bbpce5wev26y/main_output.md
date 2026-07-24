# 0072_lung_m01vhapdm99ri51nm8bbpce5wev26y

# Lung Ultrasound Analysis — Miliary TB

---

## Frame-by-Frame Observations

### Frames 1–6 (Anatomical Labeling Phase)
| Feature | Observation |
|--------|-------------|
| Soft Tissue | Normal superficial layer |
| Ribs | Bilateral acoustic shadowing present |
| Pleural Line | Visible but **irregular/thickened** compared to normal smooth appearance |
| Lung Field | Mostly anechoic/dark; **vertical streak artifacts** beginning to emerge below pleura |
| A-lines | **Not clearly dominant**; normal horizontal reverberation pattern is disrupted |

---

### Frames 7–10 (Pathology Identification Phase)

#### Sub-pleural Nodules
- **Bilateral small hypoechoic/echogenic foci** immediately beneath the pleural line
- Consistent with **miliary granulomas** tracking along the pleural surface
- Discontinuous pleural line with focal nodular interruptions

#### B-lines
- **Multiple discrete vertical hyperechoic artifacts** arising directly from the pleural line
- Extend to the **bottom of the screen without fading**
- Three clearly labeled B-lines visible simultaneously
- **Dark lung parenchyma remains visible between B-lines** (not fully merged)

---

## B-lines Assessment

### ✅ lung_rockets = **true**

| Criterion | Finding |
|-----------|---------|
| Origin | Arising from irregular/nodular pleural line |
| Directionality | Strictly vertical |
| Depth | Reach bottom of screen without fading |
| Spacing | Discrete, with visible dark intervals between them |
| Coalescence | **Not confluent** — parenchyma visible between lines |

### Subtype: **`septal`**

> Discrete, well-spaced B-lines with dark lung parenchyma visible between them. Each B-line is individually distinguishable. This pattern reflects **thickened interlobular septa** from granulomatous interstitial infiltration in miliary TB — not alveolar flooding (ground glass) or fully mixed pattern.

---

## Consolidation Assessment

### ❌ consolidation = **false**

| Consolidation Sign | Finding |
|-------------------|---------|
| Hepatization | ❌ Absent — no liver-like echogenicity of lung parenchyma |
| Shred Sign | ❌ Absent — no irregular deep border between consolidated/aerated zones |
| Air Bronchograms | ❌ Absent — no hyperechoic punctate/linear foci within hepatized tissue |

> **Sub-pleural nodules are present** but represent **focal miliary granulomas at the pleural surface**, not frank alveolar consolidation. They do not meet criteria for hepatization, shred sign, or air bronchograms.

### consolidation_type = **`null`**

---

## Summary

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = false
consolidation_type = null
additional_finding = "bilateral sub-pleural nodules (miliary pattern)"
```

### Clinical Correlation
The combination of **sub-pleural nodules + discrete septal B-lines** on LUS is the hallmark sonographic signature of **miliary tuberculosis**, reflecting:
1. Hematogenous seeding of miliary granulomas to the pleural/subpleural surface
2. Interstitial involvement with thickened septa generating septal B-lines
3. Absence of alveolar filling (no ground glass or consolidation pattern)
