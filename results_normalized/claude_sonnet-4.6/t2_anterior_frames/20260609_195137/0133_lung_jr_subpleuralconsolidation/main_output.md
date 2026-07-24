# 0133_lung_jr_subpleuralconsolidation

# Lung Ultrasound Analysis — Right Lung Upper Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| 1 | Clustered hyperechoic lobulated foci below pleural line; surrounding tissue has soft-tissue echogenicity |
| 2 | Scattered punctate bright foci within parenchyma; mild hepatization; possible faint vertical streaks |
| 3 | Multiple discrete punctate hyperechoic spots within hepatized parenchyma; air bronchogram pattern |
| 4 | Large bright conglomerate cluster in lower-left; prominent hepatization; multiple air bronchograms |
| 5 | Large **hypoechoic solid mass** occupying right half of image (hepatization bulk); residual air bronchograms at margin |
| 6 | Continuation of large hypoechoic hepatized zone; bright foci (air bronchograms) at its anterior border |
| 7 | Hepatized tissue with mixed echogenicity; bright punctate foci; irregular deep border suggestive of **shred sign** |
| 8 | Scattered hyperechoic foci within parenchyma; hepatized background; vertical artifacts within consolidation |
| 9 | Bright clustered nodular foci; surrounding tissue-like echogenicity; hepatization with air bronchograms |
| 10 | Prominent hyperechoic clusters; lobulated appearance; hepatization |
| 11 | Similar to Frame 10; clustered bright foci; no visible A-lines; hepatized parenchyma |

---

## B-Lines Assessment

> **Conclusion: `lung_rockets = false`**

**Reasoning:**
- The bright hyperechoic artifacts in these frames do **not** arise cleanly from the pleural line and extend uninterrupted to the bottom of the screen (classic B-line behavior)
- They are **localized within consolidated parenchyma** at variable depths — consistent with **air bronchograms**, not true B-lines
- No discrete, well-separated vertical "laser-beam" artifacts from the pleural surface are identifiable across any frame
- The absence of A-lines is explained by the consolidation replacing aerated tissue, not by B-line pattern

---

## Consolidation Assessment

> **Conclusion: `consolidation = true` | `consolidation_type = "air_bronchogram"`**

**Evidence across frames:**

### ✅ Hepatization
- Frames 5, 6, 7, 8: The right lung parenchyma shows **liver-like echogenicity** — homogeneous soft-tissue signal replacing normal aeration artifacts
- Frames 1, 4, 9–11: Surrounding the bright foci, the parenchyma is abnormally echogenic and solid-appearing

### ✅ Air Bronchograms (Predominant Pattern)
- **Punctate hyperechoic foci** (frames 1–4, 9–11): Round/oval bright spots within hepatized tissue = static air bronchograms
- **Clustered distribution** suggests bronchi within lobular consolidation
- This is the **dominant and recurring pattern** throughout the clip

### ✅ Shred Sign
- Frame 7: Irregular, angulated deep border between consolidated and partially aerated lung — consistent with **shred sign**

---

## Summary

```
lung_rockets     = false
consolidation    = true
consolidation_type = "air_bronchogram"
```

### Clinical Interpretation
The pattern across all 11 frames is consistent with **lobar or segmental pneumonia** of the right upper lung zone:
- **Hepatization** indicates complete alveolar consolidation
- **Air bronchograms** (punctate, static) within the consolidation are a hallmark of **bacterial pneumonia** or atelectasis with preserved bronchial patency
- **Shred sign** at the deep margin confirms active consolidation bordering aerated lung
- Absence of true B-lines confirms the alveolar (not interstitial) nature of the pathology
