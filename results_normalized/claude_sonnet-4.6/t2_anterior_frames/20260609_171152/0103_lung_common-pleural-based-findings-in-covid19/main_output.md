# 0103_lung_common-pleural-based-findings-in-covid19

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

### Chest Wall / Pleural Line
- **All frames**: The chest wall layers (skin → subcutaneous tissue → intercostal muscles) are clearly identifiable in the near field
- The **pleural line** is consistently visible as a bright, sharply-defined hyperechoic horizontal line across all 10 frames
- Lung sliding is implied by the subtle shimmering motion at the pleural interface across the sequence

---

### Deep Field Characterization

| Frame Group | Pattern Observed |
|---|---|
| **Frames 1–3** | Relatively dark deep field; horizontal reverberation artifacts (A-lines) parallel to the pleural line are dominant; minimal vertical activity |
| **Frames 4–6** | Increased sub-pleural brightness; **discrete vertical hyperechoic streaks** arise from the pleural line, extending toward the bottom of the screen without fading |
| **Frames 7–10** | Vertical artifacts remain visible but are **clearly separated** by dark lung parenchyma between them; A-lines partially visible between vertical streaks |

---

## B-Lines Assessment

### Morphological Criteria Check
- ✅ Arise perpendicularly from the pleural line
- ✅ Hyperechoic (laser-like bright)
- ✅ Extend to the bottom of the screen without fading
- ✅ Move with pleural sliding
- ✅ **Obliterate A-lines** at their course
- ✅ Dark lung parenchyma **visible between** individual lines (not confluent/merged)

### Conclusion

```
lung_rockets = true
subtype = "septal"
```

**Rationale**: B-lines are discrete, well-separated, and non-confluent. The inter-B-line lung tissue remains clearly hypoechoic, consistent with thickened interlobular septa (e.g., interstitial syndrome, early pulmonary edema, or interstitial pneumopathy). The count appears ≤3 per intercostal space without merging into a white sheet — this **excludes a ground-glass pattern**.

---

## Consolidation Assessment

### Criteria Check
| Sign | Present? | Observation |
|---|---|---|
| Tissue-like hepatization | ❌ | No liver-like echogenicity; deep field maintains acoustic properties of aerated lung |
| Shred sign | ❌ | Deep border of lung is not visible or irregular |
| Air bronchograms | ❌ | No punctate/linear hyperechoic foci within parenchyma |

### Conclusion

```
consolidation = false
consolidation_type = null
```

**Rationale**: The sub-pleural lung parenchyma shows no hepatization, no shredded border, and no air bronchograms. The pattern is fully explained by an interstitial process with septal B-lines without lobar or segmental consolidation.

---

## Summary Interpretation

> **Anterior LUS Zone — Interstitial Syndrome Pattern**
> Discrete septal B-lines are present (lung rockets positive, septal subtype) without consolidation. This is consistent with an **interstitial syndrome** (BLUE protocol "B-profile"), which in the appropriate clinical context raises differential diagnoses of:
> - Cardiogenic pulmonary edema (early/mild)
> - Viral or bacterial interstitial pneumonia
> - Pulmonary fibrosis
> - COVID-19 interstitial pneumonitis *(given the March 2020 date on the study)*
