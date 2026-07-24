# 0012_lung_bronchogenic-cancer

# Lung Ultrasound Analysis — RUQ Sagittal View

## Frame-by-Frame Observations

### Frames 1–3 (Early)
- Pleural line visible as a distinct hyperechoic line
- Lung parenchyma shows **moderate gray echogenicity**
- Faint vertical artifacts arising from pleural line — early B-line formation
- A-lines partially visible; normal aeration still present

### Frames 4–6 (Mid)
- Pleural line remains identifiable
- **Vertical hyperechoic artifacts** become more prominent, extending toward screen bottom
- B-lines beginning to coalesce — reduced inter-B-line spacing
- A-lines progressively obscured

### Frames 7–10 (Late)
- Lung parenchyma becomes **markedly hyperechoic and homogeneous**
- Echogenicity approaches that of the liver (hepatization pattern)
- Loss of A-lines; B-lines fully confluent → "white lung" appearance
- In frames 9–10: lung texture indistinguishable from liver parenchyma
- No discrete air bronchograms clearly identified

---

## B-Lines Assessment

| Feature | Finding |
|---|---|
| **Presence** | ✅ Present |
| **Pattern** | Discrete in early frames → confluent in late frames |
| **Subtype** | **`ground_glass`** (dominant) |

> B-lines coalesce into a diffuse white sheet, obliterating A-lines and producing a "white lung" appearance — consistent with alveolar flooding or severe interstitial edema.

---

## Consolidation Assessment

| Feature | Finding |
|---|---|
| **Presence** | ✅ Present |
| **Type** | **`hepatization`** |

> In frames 8–10, the lung parenchyma demonstrates **tissue-like echogenicity indistinguishable from liver**, consistent with alveolar consolidation without clearly identifiable air bronchograms in this clip.

---

## Conclusions

```
lung_rockets     = true
b_line_subtype   = "ground_glass"
consolidation    = true
consolidation_type = "hepatization"
```

### Clinical Correlation
This RUQ sagittal view demonstrates a **progression from confluent B-lines (ground-glass pattern) to frank hepatization** of the right lower lobe. This combination is highly suggestive of:
- **Pneumonia** (most likely given focal posterior consolidation), or
- Severe **cardiogenic pulmonary edema** with dependent consolidation

Correlation with clinical context (fever, respiratory rate, cardiac history) and the remaining FAST/LUS views is essential.
