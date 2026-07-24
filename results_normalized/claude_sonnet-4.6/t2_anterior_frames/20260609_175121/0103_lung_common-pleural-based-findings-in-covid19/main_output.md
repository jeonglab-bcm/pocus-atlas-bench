# 0103_lung_common-pleural-based-findings-in-covid19

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frames | Pleural Line | Deep Field | Vertical Artifacts | Horizontal Artifacts |
|--------|-------------|------------|-------------------|---------------------|
| 1–3 | Smooth, hyperechoic, well-defined | Predominantly hypoechoic/dark | None clearly identifiable | A-lines dominant |
| 4–6 | Smooth, visible | Hypoechoic with focal brightening (mid-image) | **1–2 discrete vertical hyperechoic streaks** visible in mid-right zone, appearing to arise from pleural line | A-lines still visible |
| 7–10 | Smooth, visible with apparent sliding | Returns to predominantly dark/hypoechoic | Sparse/minimal vertical artifacts | A-line pattern resumes |

---

## B-Lines Assessment

**Observations:**
- In **frames 4–6**, 1–2 discrete, well-spaced vertical hyperechoic artifacts are visible arising from the pleural line and projecting toward the deep field
- **Dark lung parenchyma is preserved between these artifacts** — no coalescence or "white lung" pattern
- These vertical artifacts do not obliterate A-lines globally
- The predominant pattern across the majority of frames is **A-line dominance** (horizontal reverberation artifacts, consistent with aerated lung)

> **lung_rockets = true**
> **Subtype: `septal`**
> Rationale: Discrete, well-spaced B-lines with preserved dark parenchyma between them, ≤2 per intercostal space; no confluence or merging pattern

---

## Consolidation Assessment

**Observations:**
- No tissue-like hepatization (no liver-echotexture pattern in lung parenchyma)
- No shred sign (deep border remains smooth/regular, not irregular or frayed)
- No punctate or linear air bronchograms within any echogenic focus
- Lung parenchyma appears **normally aerated** in the deep field throughout all frames

> **consolidation = false**
> **consolidation_type = null**

---

## Summary Conclusion

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = false
consolidation_type = null
```

**Clinical Interpretation:** The predominant pattern is **A-lines** (normal aeration) with **sparse, discrete septal B-lines** (1–2 per ICS) in some frames. This pattern in an anterior zone may represent:
- **Early/mild interstitial involvement** (note: up to 2 isolated B-lines/ICS can be at the upper limit of normal)
- No evidence of alveolar consolidation or significant alveolar flooding
