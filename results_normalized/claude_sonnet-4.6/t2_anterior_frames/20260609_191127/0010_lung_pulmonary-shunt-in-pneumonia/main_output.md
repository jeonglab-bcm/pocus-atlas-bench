# 0010_lung_pulmonary-shunt-in-pneumonia

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Grayscale Findings | Color Doppler Findings |
|-------|-------------------|----------------------|
| 1 | Heterogeneous, mildly echogenic parenchyma; indistinct pleural line | Sparse blue signals, minimal red |
| 2 | Liver-like echogenicity in mid-zone | **Large confluent red signal** — prominent arterial phase vascularity |
| 3 | Diffuse increased echogenicity; loss of A-lines | Extensive blue predominance, scattered throughout |
| 4 | Heterogeneous echo texture with bright foci | Sparse mixed small signals |
| 5 | Similar to frame 4; small echogenic foci | Minimal mixed signals |
| 6 | **Most echogenic frame**; tissue-like parenchymal texture | **Large red signal inferiorly + scattered blue** — peak systolic vascularity |
| 7 | Moderately echogenic, faint vertical artifacts | Reduced color signal, small areas |
| 8 | Echogenic parenchyma with hyperechoic punctate foci | Small red dot + blue signals |
| 9 | Similar to frame 8 | Minimal color activity |
| 10 | Bright parenchyma with patchy texture | **Large red area** + blue signals return |

---

## B-Lines Assessment

### Observations:
- **Vertical hyperechoic artifacts** are visible arising from the pleural line in multiple frames (particularly frames 3, 6, 7)
- In **frames 3 and 6**, B-lines appear to **coalesce and merge**, creating a diffuse white/bright parenchymal appearance — consistent with **ground-glass** pattern
- In **frames 1, 4, 5, 7–9**, more **discrete, separated** vertical artifacts are visible with some preservation of darker lung tissue between them — consistent with **septal** pattern
- A-lines are **largely absent** across all frames

### Conclusion:
> ✅ **lung_rockets = true**
> 🔀 **Subtype = mixed** (septal in lower-flow frames; ground_glass predominance in high-flow frames 3 and 6)

---

## Consolidation Assessment

### Observations:
- **Hepatization**: The lung parenchyma across multiple frames (especially 2, 3, 6, 10) demonstrates **liver-like echogenicity** with loss of aeration artifacts — tissue-like texture is evident
- **Air bronchograms**: Punctate and short linear **hyperechoic foci** are visible within the parenchyma in frames 4, 5, 8, and 9 — consistent with static air bronchograms
- **Preserved vascularity on Color Doppler**: The pulsatile large red signals (frames 2, 6, 10) cyclically appearing with each cardiac beat confirm **vascular flow within consolidated tissue** — this distinguishes consolidation from infarction
- No classic **shred sign** (irregular deep border) is clearly identified
- The **cardiac-cycle dependence** of color signals confirms this is true parenchymal vascularity, not artifact

### Conclusion:
> ✅ **consolidation = true**
> 🫁 **consolidation_type = "hepatization"** with superimposed **air bronchograms**

---

## Summary & Clinical Interpretation

```
lung_rockets        = true
b_line_subtype      = "mixed" (septal → ground_glass)
consolidation       = true
consolidation_type  = "hepatization" + air_bronchograms
vascularity         = preserved (pulsatile color flow)
```

### 🔴 Pattern Consistent With:
**Bacterial/Viral Pneumonia** — the combination of:
1. Mixed B-line pattern (interstitial involvement)
2. Hepatized consolidated lung
3. **Preserved vascularity** (rules out pulmonary embolism-associated infarction)
4. Air bronchograms within the consolidation

> ⚠️ **Clinical correlation recommended.** This LUS pattern should be interpreted alongside clinical history, SpO₂, fever/leukocytosis, and chest X-ray/CT for definitive diagnosis.
