# 0027_lung_subpleural-consolidation

# Lung Ultrasound Analysis — RT H/T Zone 1 (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Subpleural Structures | Vertical Artifacts | Deep Parenchyma |
|-------|-------------|----------------------|-------------------|-----------------|
| 1 | Visible, thin, hyperechoic | 1 large hypoechoic rounded structure (rib/vessel shadow) | Subtle, early comet-tail artifacts | Predominantly anechoic (aerated) |
| 2 | Visible | Single round structure | Sparse vertical echogenicities | Largely dark |
| 3 | Visible | Single round structure | 1–2 discrete vertical artifacts | Dark with faint echogenic streaks |
| 4 | Visible | Single round structure | Discrete B-line-like artifacts becoming clearer | Moderately dark |
| 5 | Visible | Single round structure | 2 discrete, well-spaced vertical hyperechoic lines | Dark lung parenchyma between lines |
| 6 | Visible | 1–2 round structures | 2–3 discrete vertical lines | Dark parenchyma preserved between artifacts |
| 7 | Visible | **Two** round structures (second rib space now visible) | 2–3 discrete B-lines in intercostal space | Parenchyma dark between B-lines |
| 8 | Visible | Two round structures | Discrete B-lines, well-separated | Dark intervals preserved |
| 9 | Visible | Two round structures | Similar discrete pattern | No coalescence/white-out |
| 10 | Visible | Single larger round structure (probe repositioned) | 2–3 discrete vertical artifacts | Dark parenchyma between lines |

---

## B-lines Assessment

### ✅ B-lines Present (`lung_rockets = true`)

**Observations:**
- Hyperechoic vertical artifacts arise from the pleural line and extend to the bottom of the screen without fading
- Artifacts are **discrete and well-spaced**, with clearly visible dark (aerated) lung parenchyma preserved between each B-line
- Typically **2–3 B-lines per intercostal space**, consistent with thickened interlobular septa
- A-lines are partially preserved (not completely obliterated)
- No coalescence or white-sheet appearance observed

### Subtype: **`septal`**
> Discrete, countable B-lines with preserved dark parenchyma intervals — indicating thickened interlobular septa rather than alveolar flooding

---

## Consolidation Assessment

### ❌ Consolidation Absent (`consolidation = false`)

**Observations:**
- **No hepatization**: Deep parenchyma does not demonstrate liver-like tissue echogenicity
- **No shred sign**: The deep border of the lung is not irregularly shredded; no aerated/consolidated interface
- **No air bronchograms**: No punctate or linear hyperechoic foci within a hepatized region
- The rounded hypoechoic structures seen in frames are consistent with **rib acoustic shadows and/or intercostal vessels**, not subpleural consolidations
- The pleural line remains intact and smooth throughout

**`consolidation_type = null`**

---

## Summary & Conclusions

```
lung_rockets     = true
b_line_subtype   = "septal"
consolidation    = false
consolidation_type = null
```

### Clinical Interpretation
The pattern of **discrete septal B-lines** (2–3 per intercostal space) without consolidation in the **right anterior zone** is consistent with:

- 🫁 **Mild interstitial syndrome** — thickened interlobular septa
- Differential includes: **mild cardiogenic interstitial edema**, early interstitial lung disease (e.g., pulmonary fibrosis), or lymphangitic spread
- The absence of ground-glass B-lines argues against significant alveolar edema
- The absence of consolidation argues against pneumonia or atelectasis in this zone

> **Recommendation**: Correlate with contralateral zones and clinical context (volume status, BNP, CT findings if available) to characterize the degree of interstitial involvement.
