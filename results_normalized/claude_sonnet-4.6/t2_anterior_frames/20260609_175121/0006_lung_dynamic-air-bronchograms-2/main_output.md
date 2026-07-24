# 0006_lung_dynamic-air-bronchograms-2

# Frame-by-Frame Lung Ultrasound Analysis

## Sequential Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Parenchyma |
|-------|-------------|-------------------|-----------------|
| 1 | Visible, intact | Multiple B-lines, partially coalescing | Diffusely bright |
| 2 | Visible | Discrete B-lines, 3–4/ICS | Moderately echogenic |
| 3 | Visible | B-lines, beginning to merge | Bright, foci emerging |
| 4 | Visible | More discrete, spaced B-lines | Relatively preserved |
| 5 | Visible | Mixed: discrete + coalescing | Patchy bright areas |
| 6 | Visible | Confluent white-sheet pattern | Obscured A-lines |
| 7 | Visible | B-lines + **dark hypoechoic region** mid-field | **Hepatized texture + bright punctate foci** |
| 8 | Visible | B-lines + consolidated area | **Air bronchograms clearly visible** |
| 9 | Visible | Moderately coalescing | Irregular deep border |
| 10 | Visible | Confluent/ground-glass | Diffusely white |

---

## B-Lines Assessment

### 🔍 Observed Features:
- **Frames 2–4**: Discrete, well-separated vertical hyperechoic artifacts (~3/ICS) arising from the pleural line → **septal B-lines**
- **Frames 6, 10**: Confluent, merging vertical artifacts forming a "white lung" curtain, A-lines fully obliterated → **ground-glass B-lines**
- **Frames 5, 7–9**: Coexistence of both discrete and confluent patterns in different regions

### ✅ Conclusion:
```
lung_rockets = true
subtype = "mixed"
```
> Rationale: Both discrete septal B-lines (spaced, ≤3/ICS, dark intervals visible) and confluent ground-glass B-lines (merging white sheets) are identified across different frames and regions of the clip.

---

## Consolidation Assessment

### 🔍 Observed Features:
- **Frames 7–8**: A focal **hypoechoic region** with liver-like (hepatized) echogenicity visible in the mid-to-deep field
- **Within this region**: Multiple **punctate and linear hyperechoic foci** consistent with **air bronchograms** (air-filled bronchi within consolidated parenchyma)
- **Frame 9**: The deep border of this region appears **irregular/shredded** — subtle shred sign component
- No normal A-line reverberation artifacts beneath the consolidated zone

### ✅ Conclusion:
```
consolidation = true
consolidation_type = "air_bronchogram"
```
> Rationale: The dominant finding is hepatized lung parenchyma containing punctate/linear hyperechoic air bronchograms (frames 7–8), most consistent with **alveolar consolidation** (e.g., pneumonia, atelectasis with air bronchograms). A secondary shred sign is present but less dominant.

---

## Summary Table

| Parameter | Value |
|-----------|-------|
| `lung_rockets` | ✅ **true** |
| `b_line_subtype` | **mixed** (septal + ground_glass) |
| `consolidation` | ✅ **true** |
| `consolidation_type` | **air_bronchogram** |

---

## Clinical Interpretation
The combination of **mixed B-lines** (interstitial syndrome) with **consolidation + air bronchograms** in the anterior zone is most consistent with **lobar or segmental pneumonia**, where surrounding peri-lesional interstitial edema/inflammation generates B-lines while the consolidated core shows air bronchograms. Atelectasis with surrounding edema is an alternative consideration.
