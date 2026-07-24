# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Analysis — Sequential Frame Assessment

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Pattern Impression |
|-------|-------------|-------------------|-------------------|
| 1 | Visible ~2–3 cm | 1–2 discrete hyperechoic vertical rays | Early septal B-lines |
| 2 | Visible ~2–3 cm | 1–2 discrete, spaced vertical artifacts | Septal pattern |
| 3 | Visible, partially obscured | Diffuse vertical brightening, mild coalescence | Transitioning toward ground-glass |
| 4 | Visible | Multiple discrete bright foci at 3–6 cm, well-separated | **Septal B-lines** dominant |
| 5 | Visible | Mixed: discrete B-lines laterally + coalescing centrally | **Mixed** pattern |
| 6 | Partially obscured | Dense, confluent vertical brightening, A-lines effaced | **Ground-glass** dominant |
| 7 | Visible | 1–2 discrete vertical rays, dark lung between | Septal |
| 8 | Visible | Discrete hyperechoic foci, moderate spacing | Septal |
| 9 | Visible | Moderate vertical artifacts with partial merging | Mixed |
| 10 | Visible | Faint, widely spaced vertical artifacts | Resolving / sparse septal |

---

## B-Lines Assessment

### Observations
- **Pleural line** is identifiable in all frames at approximately **2–3 cm depth**, generally smooth without step-off or irregular thickening
- **Hyperechoic vertical artifacts** arise consistently from the pleural line and **extend to the bottom of the screen without fading** — fulfilling B-line criteria
- In frames **1, 2, 4, 7, 8**: artifacts are **discrete and well-separated**, with hypoechoic (dark) lung parenchyma visible between them → classic **septal B-lines**
- In frames **3, 6, 9**: artifacts **coalesce and merge**, forming a **white curtain** that obliterates A-lines → **ground-glass** pattern
- Frame **5** demonstrates both patterns simultaneously in different regions of the field

### Conclusion
```
lung_rockets     = true
b_line_subtype   = "mixed"
```
> Rationale: The clip demonstrates temporal and spatial alternation between **discrete septal B-lines** (≤3 per ICS, separated by dark lung) and **confluent ground-glass B-lines** (coalescing white sheet, A-lines effaced). Neither pattern is exclusively dominant across all frames.

---

## Consolidation Assessment

### Observations
- **Hepatization**: The lung parenchyma does **not** acquire liver-like solid echogenicity at any point in the clip. The echogenic zones consistently represent vertical artifact propagation, not tissue-equivalent signal.
- **Shred sign**: No irregular, ragged deep border between consolidated and aerated lung is identifiable. Deep margins, where visible, are smooth or artifact-obscured.
- **Air bronchograms**: The bright hyperechoic foci seen in frames 4–5 at 3–6 cm depth are **linear/streak artifacts tracking vertically** from the pleural surface, consistent with **B-line origins**, not punctate air bronchograms embedded within hepatized parenchyma.

### Conclusion
```
consolidation        = false
consolidation_type   = null
```

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| `b_line_subtype` | **mixed** (septal ↔ ground_glass across frames) |
| `consolidation` | **false** |
| `consolidation_type` | **null** |

### Clinical Interpretation
This pattern — variable B-lines oscillating between septal and ground-glass subtypes across frames of the **anterior zone** — is consistent with:
- **Cardiogenic pulmonary edema** (dynamic fluid redistribution), or
- **Diffuse interstitial syndrome** (e.g., interstitial pneumonia, ARDS early phase)

The absence of consolidation argues against pneumonia as the primary etiology but does not exclude it entirely. Correlation with the clinical context and bilateral zone assessment is recommended.
