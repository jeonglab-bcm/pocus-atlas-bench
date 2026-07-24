# 0127_lung_jr_5yolunghepatization

# Sequential Lung Ultrasound Analysis — Left Anterior Zone

## Frame-by-Frame Observations

### Frames 1–3
- Pleural line is identifiable, mildly irregular in contour
- Below the pleural line: **heterogeneous, echogenic parenchymal texture** — tissue-like echogenicity replacing expected anechoic/reverberation pattern
- **Scattered hyperechoic foci** visible within the deeper field; irregular interface between echogenic and less echogenic regions
- No clear discrete A-lines (horizontal reverberation artifacts)

### Frames 4–6
- A **rounded/lobulated hyperechoic structure** appears in the upper-right (consistent with a rib cross-section entering the scan plane)
- Deep parenchyma becomes progressively **more hypoechoic** but retains some heterogeneous bright foci
- The transition zone between echogenic and anechoic parenchyma has an **irregular, shredded appearance**

### Frames 7–10
- Rib shadow persists upper-right
- Deep field shows **punctate/linear hyperechoic foci** scattered within a relatively hypoechoic parenchymal background
- Irregular deep border persists; no clean posterior acoustic enhancement typical of pure fluid

---

## B-Lines Assessment

| Feature | Finding |
|---|---|
| Vertical artifacts from pleural line | Present but not classically discrete |
| Extension to screen bottom | Partial / obscured by consolidation |
| Spacing between artifacts | Partially confluent |

**lung_rockets = true**
**Subtype: ground_glass**

> The increased parenchymal echogenicity and partially coalescing vertical artifacts create a diffuse bright pattern rather than clearly separated discrete rockets, consistent with **confluent/ground-glass B-lines**, likely reflecting alveolar flooding or dense interstitial disease. Classic A-lines are abolished.

---

## Consolidation Assessment

| Sign | Present? | Detail |
|---|---|---|
| Hepatization | ✅ | Tissue-like echogenicity replacing aerated lung, particularly frames 1–3 |
| Shred sign | ✅ | Irregular, non-geometric deep border between consolidated and residually aerated lung (frames 3–6) |
| Air bronchograms | ✅ | Punctate/linear hyperechoic foci within echogenic parenchyma (frames 7–10) |

**consolidation = true**
**consolidation_type = "air_bronchogram"** *(predominant feature in later frames, superimposed on hepatization and shred sign)*

---

## Summary & Interpretation

```
lung_rockets      = true
b_line_subtype    = "ground_glass"
consolidation     = true
consolidation_type = "air_bronchogram"
```

### Clinical Correlation
This pattern — **confluent B-lines + hepatization + shred sign + air bronchograms** — in an anterior zone is most consistent with:

1. **Pneumonia with consolidation** (air bronchograms + shred sign are hallmark findings)
2. **Severe cardiogenic or non-cardiogenic pulmonary edema** evolving toward alveolar flooding (ground-glass B-lines + hepatization)
3. **ARDS** (combined interstitial and alveolar involvement)

> ⚠️ The presence of **air bronchograms within hepatized tissue** is a high-specificity sign for **pneumonic consolidation**. Correlation with clinical findings, contralateral zone comparison, and Doppler/color flow is recommended.
