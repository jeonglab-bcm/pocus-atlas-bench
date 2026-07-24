# 0148_lung_jr_pediatric-consolidation

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

### Frames 1–2 (Narrow Field / Linear-Appearing Views)
- Pleural line visible near the top (~1–1.5 cm depth)
- **Discrete, well-separated vertical hyperechoic artifacts** arise from the pleural line and extend toward the bottom of the screen
- Dark lung parenchyma remains visible *between* these artifacts
- No obvious posterior acoustic shadowing from ribs at the artifact origin
- → **Consistent with septal B-lines**

### Frames 3–5 (Transitional / Widening Field)
- Field progressively widens (probe orientation shifting)
- **Bright hyperechoic punctate/linear foci** appear within the near-field lung parenchyma (~depth 3–4 cm, left of field)
- The surrounding tissue takes on a **granular, heterogeneous, liver-like echogenicity**
- Some zones retain discrete vertical artifacts laterally
- → **Air bronchogram pattern emerging within hepatized tissue**; residual septal B-lines laterally

### Frames 6–7 (Broader Convex View)
- A **hypoechoic (anechoic) zone** is visible in the upper-mid field (~depth 2–3 cm), consistent with a **fluid bronchogram** or necrotic foci
- Surrounding tissue shows **clear hepatization** (solid, echogenic, liver-like texture)
- Bright foci scattered within the consolidated region → **air bronchograms**
- The deep border shows some irregularity → subtle **shred sign**
- Vertical artifacts (B-lines) appear **confluent and coalescing** in adjacent aerated zones → **ground-glass pattern**

### Frames 8–9 (Peripheral / Lateral Sweep)
- More **diffuse, uniformly bright** texture throughout the field
- A-lines are suppressed; white-sheet appearance
- → **Ground-glass B-line pattern** (confluent, merging vertical artifacts)

---

## B-Lines Assessment

| Feature | Finding |
|---|---|
| **lung_rockets** | **true** |
| **Subtype** | **mixed** |

**Rationale:**
- Frames 1–2 and laterally in frames 3–5: **Septal B-lines** — discrete, well-spaced, dark parenchyma visible between them
- Frames 6–9: **Ground-glass B-lines** — confluent, coalescing white sheet pattern, A-lines obliterated
- Both subtypes are present at different time points in the clip → **mixed**

---

## Consolidation Assessment

| Feature | Finding |
|---|---|
| **consolidation** | **true** |
| **consolidation_type** | **air_bronchogram** |

**Rationale:**
- Frames 3–7 demonstrate unambiguous **hepatization**: solid, echogenic parenchyma resembling liver texture
- **Multiple punctate and linear hyperechoic foci** are embedded within the hepatized zone, consistent with **air-filled bronchi (air bronchograms)**
- Frames 6–7 additionally show an anechoic focus suggesting a **fluid bronchogram** component
- A subtly irregular deep border (shred sign) is present but not predominant
- → Predominant consolidation type: **air_bronchogram** within hepatized lung

---

## Summary / Conclusions

```
lung_rockets       = true
b_line_subtype     = "mixed"   (septal → ground_glass across the clip)
consolidation      = true
consolidation_type = "air_bronchogram"
```

**Clinical Interpretation:**
This pattern — anterior zone consolidation with air bronchograms, surrounded by mixed septal and ground-glass B-lines — is most consistent with **lobar/segmental pneumonia** with adjacent interstitial edema or reactive alveolar disease. The ground-glass B-line areas adjacent to the consolidation suggest **perilesional interstitial thickening**. Correlation with clinical context (fever, respiratory symptoms) and CT is recommended.
