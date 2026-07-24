# 0049_lung_pleural-shred-sign

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Vertical Artifacts | Deep Field | Notes |
|-------|-------------|-------------------|------------|-------|
| 1 | Bright, well-defined | 1–2 discrete hyperechoic verticals | Dark, preserved | B-lines arising from pleural line |
| 2 | Bright, well-defined | 1–2 discrete verticals | Dark | Similar pattern |
| 3 | Bright, continuous | ~2 discrete B-lines | Dark | Slight positional shift |
| 4 | Bright | 2 discrete verticals | Dark | Consistent spacing between lines |
| 5 | Bright | 2–3 discrete B-lines | Dark | Well-separated artifacts |
| 6 | Bright | 2 discrete verticals | Dark | Interspace remains dark |
| 7 | Bright | ~2–3 discrete B-lines | Dark | Pattern stable |
| 8 | Bright | 2 discrete verticals | Dark | No confluence |
| 9 | Bright | 2–3 discrete B-lines | Dark | Preserved dark parenchyma between |
| 10 | Bright | 2 discrete verticals | Dark | No coalescing observed |

---

## B-Lines Assessment

### Observations:
- **Hyperechoic vertical artifacts** consistently arise **from the pleural line** across all frames
- Artifacts extend toward the **bottom of the screen without fading**
- **≤3 B-lines per intercostal space**, clearly **separated from each other**
- **Dark lung parenchyma is visible between B-lines** — no white-out/confluence
- A-lines are **partially suppressed** but not completely abolished
- Motion consistent with lung sliding is implied across the sequence

### Conclusion:
```
lung_rockets = true
subtype = "septal"
```
> Discrete, well-spaced B-lines consistent with **thickened interlobular septa** (e.g., mild interstitial edema, early interstitial syndrome)

---

## Consolidation Assessment

### Observations:
- **No hepatization**: Deep lung parenchyma does not adopt liver-like echogenicity
- **No shred sign**: The deep border of the lung is not irregular/shredded
- **No air bronchograms**: No punctate or linear hyperechoic foci within consolidated tissue
- Lung surface and parenchyma maintain **expected aeration pattern**

### Conclusion:
```
consolidation = false
consolidation_type = null
```

---

## Summary

| Parameter | Result |
|-----------|--------|
| **lung_rockets** | ✅ `true` |
| **B-line subtype** | `septal` |
| **consolidation** | ❌ `false` |
| **consolidation_type** | `null` |

> **Clinical Interpretation:** This anterior LUS clip shows a **septal B-line pattern** without consolidation, most consistent with **mild interstitial syndrome** (e.g., early cardiogenic pulmonary edema, mild interstitial pneumonitis, or resolving edema). The discrete spacing and preserved dark interspace rule out alveolar flooding or ground-glass confluent disease.
