# 0010_lung_pulmonary-shunt-in-pneumonia

# Lung Ultrasound — Sequential Frame Analysis

---

## Frame-by-Frame Observations

| Frame | Grayscale Findings | Color Doppler Notes |
|-------|-------------------|---------------------|
| 1 | Mildly echogenic parenchyma; faint vertical artifacts from pleural line | Sparse blue signals, 1 small red spot |
| 2 | Heterogeneous parenchyma; subtle vertical streaks | Large confluent red blob — prominent vascular signal |
| 3 | **Diffuse bright parenchyma**; near-white lung appearance; A-lines effaced | Dense blue filling nearly entire box |
| 4 | Mixed echogenicity; discrete bright foci | Mixed red/blue |
| 5 | Moderate echogenicity; discrete vertical artifacts visible at edges | Predominantly blue with red spots |
| 6 | **Solid-appearing echogenic zone** in lower field; internal punctate bright foci (possible air bronchograms); hepatized texture | Large red pool inferiorly + mixed blue |
| 7 | Rib shadows prominent; parenchyma between ribs appears heterogeneous; linear bright foci | Focal blue/red spots |
| 8 | Similar to Frame 7; bright linear structures consistent with ribs; slightly heterogeneous lung | Scattered blue/red |
| 9 | Similar to Frame 8; faint vertical artifacts | Small discrete signals |
| 10 | **Recurrence of solid echogenic area** inferiorly; punctate bright foci within; irregular deep border | Large red zone + mixed signals |

---

## B-Lines Assessment

### Observations:
- **Frames 3 & 5:** The lung parenchyma shows a **diffuse bright/white appearance** with effacement of A-lines — consistent with **confluent/coalescing B-lines** (ground-glass pattern)
- **Frames 1, 4, 7, 8, 9:** Discrete, separated vertical hyperechoic artifacts arising from the pleural line are visible at the margins of the color box — consistent with **septal-type B-lines** (spaced, with dark intervals between them)
- No frame demonstrates clear A-line dominance

### Conclusion:
> ✅ **`lung_rockets = true`**
> 📋 **Subtype: `mixed`**
> *(Septal discrete B-lines co-existing with confluent/ground-glass B-lines across different frames)*

---

## Consolidation Assessment

### Observations:
- **Frames 6 & 10:** The inferior portion of the scanning field shows:
  - **Tissue-like (hepatized) echogenicity** — solid, liver-like texture replacing normal aerated lung
  - **Punctate and linear hyperechoic foci** embedded within the hepatized area → consistent with **air bronchograms**
  - A **deep irregular border** between the consolidated zone and deeper aerated lung → consistent with **shred sign**
- These findings recur in multiple frames, confirming they are structural (not artifact)
- Color Doppler demonstrates **vascularity within the consolidated zone** — supports true consolidation (vs. atelectasis alone)

### Conclusion:
> ✅ **`consolidation = true`**
> 📋 **`consolidation_type = "air_bronchogram"`** *(predominant feature within hepatized zone)*
> *(Shred sign is also present as a secondary feature)*

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| B-line subtype | **mixed** (septal + ground_glass) |
| `consolidation` | **true** |
| `consolidation_type` | **air_bronchogram** |

### Clinical Interpretation:
This pattern — **mixed B-lines + consolidation with air bronchograms** in an anterior zone — is most consistent with **infectious pneumonia** (e.g., bacterial or viral/COVID-19 pneumonia). The mixed interstitial pattern (B-lines) surrounding an area of alveolar consolidation with air bronchograms is a classic LUS presentation of **pneumonia** rather than cardiogenic pulmonary edema (which typically shows bilateral symmetric ground-glass B-lines without consolidation).
