# 0036_lung_dynamic-air-bronchograms

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | A-lines | Notable Features |
|-------|-------------|-------------------|---------|-----------------|
| 1 | Clear, well-defined | 2–3 discrete hyperechoic vertical artifacts | Visible between artifacts | Artifacts arise from pleural line, extend deep |
| 2 | Clear | 2–3 discrete B-lines | Present | Separation between B-lines maintained |
| 3 | Clear | Slightly fewer artifacts | More prominent | A-lines dominate slightly |
| 4 | Clear | Discrete vertical artifacts | Present | Similar pattern |
| 5 | Clear | 2–3 B-lines | Present | Consistent spacing |
| 6 | Clear | Discrete artifacts | Present | Mixed A/B pattern |
| 7 | Clear | More prominent vertical artifacts | Partially visible | B-lines more conspicuous |
| 8 | Clear | 3–4 discrete hyperechoic B-lines | Partially visible | Clearly separated, not confluent |
| 9 | Clear | Discrete B-lines | Present | Dark parenchyma between lines |
| 10 | Clear | Discrete B-lines | Present | Pattern consistent throughout |

---

## B-lines Assessment

### Observations:
- **Hyperechoic vertical artifacts** arise perpendicularly from the pleural line across all frames
- Artifacts **extend to the bottom of the screen** without fading
- B-lines are **clearly separated** with dark lung parenchyma visible between them
- **A-lines remain visible** between B-lines, indicating incomplete white-out
- **≤3–4 B-lines per intercostal space**, each discretely defined
- No coalescence or merging into a diffuse white sheet

### Conclusion:
```
lung_rockets = TRUE
subtype = "SEPTAL"
```
> Discrete, well-spaced B-lines with preserved A-lines and visible dark parenchyma between them — consistent with **thickened interlobular septa** (e.g., early interstitial edema, pulmonary fibrosis, or mild heart failure)

---

## Consolidation Assessment

### Observations:
- **No tissue-like hepatization** — lung parenchyma does not appear liver-like or solid
- **No shred sign** — deep border between lung and artifacts is not irregular/shredded
- **No air bronchograms** — no punctate or linear hyperechoic foci within hepatized tissue
- The lung field appears **normally aerated** between B-line artifacts

### Conclusion:
```
consolidation = FALSE
consolidation_type = null
```

---

## Final Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | ✅ **TRUE** |
| `b_line_subtype` | **SEPTAL** |
| `consolidation` | ❌ **FALSE** |
| `consolidation_type` | **null** |

### Clinical Interpretation:
This pattern of **discrete septal B-lines** without consolidation in an anterior zone suggests **mild-to-moderate interstitial syndrome**, most consistent with:
- Early **cardiogenic pulmonary edema** (Grade B1)
- Mild **interstitial lung disease**
- Early **pneumonitis**

> ⚠️ *Clinical correlation with patient history, bilateral comparison, and other LUS zones is essential for definitive diagnosis.*
