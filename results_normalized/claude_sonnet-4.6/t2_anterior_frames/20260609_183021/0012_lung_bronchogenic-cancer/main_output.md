# 0012_lung_bronchogenic-cancer

# Lung Ultrasound Analysis — RUQ Sagittal Sequential Frames

## Frame-by-Frame Observations

### Frames 1–3 (Early)
- Liver parenchyma occupies the majority of the image with homogeneous echotexture
- Diaphragm visible as a bright, curved hyperechoic arc at the lower border
- Lung base zone (cephalad to diaphragm, upper-left) appears **dark** with faint horizontal reverberation artifacts → consistent with **A-lines**
- No discrete vertical hyperechoic artifacts identifiable yet
- No tissue-like echogenicity beyond the pleuro-diaphragmatic interface

---

### Frames 4–6 (Transitional)
- Lung base begins to enter the imaging plane with respiratory motion
- **Discrete vertical hyperechoic artifacts** arise from the pleural line and extend to the bottom of the field without fading → **B-line candidates**
- These are **well-spaced**, with dark parenchyma visible between them
- The diaphragm remains clearly defined
- No confluent white sheet; no hepatization pattern yet

---

### Frames 7–8 (Mid-Late)
- The lung base zone shows **progressive increase in echogenicity**
- The tissue deep to the diaphragm begins to take on a **solid, liver-like texture**
- Discrete B-lines are less prominent; the hepatized tissue starts to dominate the far field
- The border between normal liver and supra-diaphragmatic tissue becomes increasingly difficult to distinguish

---

### Frames 9–10 (Late)
- **Striking hepatization pattern** at the right lung base
- Lung parenchyma is **isoechoic to the liver** — classic tissue-like appearance
- Small **punctate/linear hyperechoic foci** are visible within the consolidated zone → consistent with **air bronchograms**
- Loss of A-line reverberation artifact
- The shredded border between consolidated and aerated lung is suggested at the deep margin of the hyperechoic zone

---

## B-Lines Assessment

| Feature | Finding |
|---|---|
| **lung_rockets** | ✅ `true` |
| **Subtype** | `septal` |
| **Rationale** | Discrete, well-separated vertical hyperechoic artifacts arising from the pleural line in frames 4–6; dark parenchyma visible between them (≤3 per intercostal space); classic thickened interlobular septa morphology |

---

## Consolidation Assessment

| Feature | Finding |
|---|---|
| **consolidation** | ✅ `true` |
| **consolidation_type** | `"hepatization"` with **air bronchograms** |
| **Rationale** | Frames 8–10 demonstrate isoechoic-to-liver echogenicity of the right lung base (hepatization); punctate/linear hyperechoic foci within the consolidated tissue represent trapped air in bronchi (air bronchograms); loss of aeration artifacts confirms full alveolar replacement |

---

## Summary & Clinical Correlation

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = true
consolidation_type = "hepatization" (+ air bronchograms)
```

> **Interpretation:** This sequence demonstrates **right lower lobe consolidation** with hepatization and air bronchograms, preceded by septal B-lines in early frames — a pattern highly consistent with **lobar/segmental pneumonia**. The septal B-lines likely reflect perilesional interstitial thickening surrounding the consolidated lobe. Compressive atelectasis from an underlying effusion is a secondary consideration, though no anechoic free fluid is clearly identified.
