# 0039_lung_hepatization-of-lung

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Field |
|-------|-------------|-------------------|------------|
| 1–2 | Visible, regular | 1–2 discrete bright vertical artifacts | Dark, posterior attenuation |
| 3–4 | Intact | Discrete B-line(s) arising from pleural line | Relatively anechoic |
| 5–6 | Visible | Bright focal vertical artifact; some comet-tail morphology | Moderate brightness |
| 7–8 | Present | 1–2 spaced vertical lines descending toward far field | Preserved dark zones between artifacts |
| **9–10** | Present | **Bright linear/rod-like hyperechoic structures** within deeper lung tissue | **Increased echogenicity of surrounding parenchyma** |

---

## B-Lines Assessment

### Observations
- Frames 1–8: **Discrete, well-spaced vertical hyperechoic artifacts** arise from the pleural line and extend deep without fading — classic B-line morphology
- Dark lung parenchyma is clearly visible **between** the artifacts
- Typically ≤2–3 B-lines per frame/intercostal space
- No confluent "white lung" or merging artifact sheets observed

### Conclusion
> **lung_rockets = `true`**
> **Subtype = `septal`**
> Discrete, separated B-lines consistent with thickened interlobular septa

---

## Consolidation Assessment

### Observations
- **Frames 9–10**: The deep lung field shows:
  - **Increased parenchymal echogenicity** (tissue-like hepatization) in a focal region
  - **Bright linear/punctate hyperechoic structures** embedded within this echogenic tissue — consistent with **air bronchograms**
  - No clear shred sign identified at this zone

### Conclusion
> **consolidation = `true`**
> **consolidation_type = `"air_bronchogram"`**
> Focal area of hepatized lung with linear/punctate air-filled bronchi visible within

---

## Integrated Interpretation

```
┌─────────────────────────────────────────────────────┐
│  lung_rockets     = true                            │
│  b_line_subtype   = "septal"                        │
│  consolidation    = true                            │
│  consolidation_type = "air_bronchogram"             │
└─────────────────────────────────────────────────────┘
```

**Clinical Correlation:** This combined pattern — **septal B-lines + anterior consolidation with air bronchograms** — is most consistent with **pneumonia** (bacterial or viral), where focal alveolar filling coexists with perilesional interstitial edema. The anterior location of consolidation increases its significance.
