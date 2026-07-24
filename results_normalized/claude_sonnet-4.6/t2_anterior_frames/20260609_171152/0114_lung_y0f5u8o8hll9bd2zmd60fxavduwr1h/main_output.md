# 0114_lung_y0f5u8o8hll9bd2zmd60fxavduwr1h

# Lung Ultrasound Frame-by-Frame Analysis

## Equipment & Settings
- **Machine**: SonoSite | **Probe**: P21xp/5-1 (Cardiac)
- **Depth**: 11.0 cm | **Date**: 27 Apr 2018, 15:48
- **Color annotations**: Green = chest wall surface, Red = pleural line, Blue (×2) = depth reference markers

---

## Frame-by-Frame Observations

| Frame | Pleural Line (Red) | Sub-pleural Zone | Vertical Artifacts | Deep Field |
|---|---|---|---|---|
| 1 | Bright, continuous | Mildly echogenic | 2–3 discrete vertical streaks | Fades normally |
| 2 | Bright, continuous | Similar | 2–3 vertical streaks, slightly spaced | No focal density |
| 3 | Bright, continuous | Mildly echogenic | Discrete streaks, dark intervals visible | Normal fade |
| 4 | Bright, continuous | Mild brightness | 2–3 discrete streaks | No consolidation |
| 5 | Bright, continuous | Mildly echogenic | Discrete vertical artifacts | Normal |
| 6 | Bright, continuous | Similar | Discrete streaks, spacing preserved | Normal fade |
| 7 | Bright, continuous | Mild echogenicity | 2–3 spaced vertical artifacts | No abnormality |
| 8 | Bright, continuous | Similar | Discrete B-line-like streaks | Normal |
| 9 | Bright, continuous | Mild brightness | Discrete vertical streaks | Normal |
| 10 | Bright, continuous | Slightly increased | 2–3 discrete vertical artifacts | No focal lesion |

---

## B-Lines Assessment

### Observations:
- **Pleural line** is clearly defined (red marker), bright and regular across all 10 frames
- **Vertical hyperechoic artifacts** arise from the pleural line in every frame, extending toward the bottom of the screen without fading
- These artifacts are **discrete and well-separated** — dark lung parenchyma is clearly visible *between* them
- Typically **2–3 artifacts per frame/intercostal space**, never merging into a confluent white sheet
- **No dominant A-line pattern** is present (no horizontal reverberation artifacts)
- Artifacts appear to move with the respiratory cycle across sequential frames (consistent with pleural sliding)

### Conclusion:
```
lung_rockets = true
subtype = "septal"
```
> Discrete, spaced B-lines with preserved dark intervals between them — consistent with thickened interlobular septa (interstitial syndrome, early/mild)

---

## Consolidation Assessment

### Observations:
- **No hepatization**: Lung parenchyma does not acquire liver-like solid echogenicity
- **No shred sign**: The deep border of the aerated lung is not irregular or shredded
- **No air bronchograms**: No punctate or linear hyperechoic foci within any parenchymal area
- Sub-pleural field between the blue markers appears hypoechoic and homogeneous — consistent with normal acoustic shadowing of aerated lung
- No focal region of tissue-density change is identified in any of the 10 frames

### Conclusion:
```
consolidation = false
consolidation_type = null
```

---

## Summary

| Parameter | Result |
|---|---|
| **lung_rockets** | ✅ `true` |
| **B-line subtype** | 🔵 `septal` |
| **consolidation** | ❌ `false` |
| **consolidation_type** | `null` |

### Clinical Interpretation
This anterior zone LUS clip demonstrates a **mild interstitial syndrome** pattern characterized by discrete, septal B-lines (2–3 per ICS) without alveolar consolidation. This pattern is most consistent with:
- **Early cardiogenic pulmonary edema** (subpleural septal thickening)
- **Mild interstitial pneumonia**
- **Early ARDS** (interstitial phase)

Correlation with the contralateral lung, posterior zones, and clinical context (BNP, respiratory status) is recommended for definitive diagnosis.
