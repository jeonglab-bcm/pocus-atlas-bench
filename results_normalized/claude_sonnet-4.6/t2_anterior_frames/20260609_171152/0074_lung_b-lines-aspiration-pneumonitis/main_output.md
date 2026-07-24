# 0074_lung_b-lines-aspiration-pneumonitis

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

### Frames 1–5 (Teaching Reference Series, LS7 Probe)

| Frame | Pleural Line | Vertical Artifacts | Background |
|-------|-------------|-------------------|------------|
| 1 | Bright, continuous | 1–2 discrete hyperechoic vertical streaks | Lung field dark between artifacts |
| 2 | Intact | 1–2 discrete B-lines, well-separated | Preserved dark interstitial spaces |
| 3 | Intact | 1 prominent vertical artifact (right), spacing maintained | Dark areas visible between lines |
| 4 | Intact | Bright vertical artifact right-lateral; left side relatively dark | No confluence; dark spaces preserved |
| 5 | Intact | Similar to Frame 4; discrete single artifact | No coalescing pattern |

### Frames 6–10 (Timestamped: 03/28/21 02:34–02:34, C1-5 Abdomen Probe)

| Frame | Findings |
|-------|----------|
| 6 | Liver visible upper-left (expected landmark); pleural line identifiable; 1–2 discrete vertical artifacts |
| 7 | Liver-lung interface visible; discrete hyperechoic vertical streaks from pleural line |
| 8 | Similar pattern; artifacts remain discrete with preserved dark inter-artifact spaces |
| 9 | Discrete B-lines persist; no confluence into white sheet |
| 10 | Continued septal-type artifact pattern; no hepatization visible |

---

## B-Lines Assessment

### Observations
- **Hyperechoic vertical artifacts** arise consistently from the pleural line across all frames
- Artifacts **extend to the bottom of the screen** without fading
- Dark lung parenchyma is **clearly preserved between artifacts** in every frame
- Typically **1–2 (≤3) discrete B-lines** per intercostal space
- No merging or coalescing into a diffuse "white lung" sheet
- A-lines are partially obscured but not completely replaced

### Conclusion
> **lung_rockets = `true`**
> **subtype = `"septal"`**
> Discrete, well-spaced B-lines with preserved inter-artifact dark spaces, consistent with thickened interlobular septa (e.g., interstitial edema, early heart failure, or interstitial lung disease)

---

## Consolidation Assessment

### Observations
- **No tissue-like hepatization**: Lung parenchyma does not take on liver-like echogenicity in the lung field
- **No shred sign**: Deep border of the lung, where visible, appears smooth — no irregular shredded interface
- **No air bronchograms**: No punctate or linear hyperechoic foci within a hepatized lung field
- The liver (frames 6–10) serves as an acoustic window; it does **not** indicate lung consolidation

### Conclusion
> **consolidation = `false`**
> **consolidation_type = `null`**

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| `b_line_subtype` | **septal** |
| `consolidation` | **false** |
| `consolidation_type` | **null** |

**Clinical Correlation:** The septal B-line pattern (discrete, ≤3 per ICS, well-separated) seen consistently across all frames is most compatible with **interstitial syndrome** — likely early/moderate pulmonary interstitial edema, fibrosis, or another interstitial process. No alveolar consolidation is present.
