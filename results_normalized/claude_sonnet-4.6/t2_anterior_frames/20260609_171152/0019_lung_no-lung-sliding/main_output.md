# 0019_lung_no-lung-sliding

# Lung Ultrasound Analysis — Sequential Frame Review

---

## Frame-by-Frame Observations

| Frames | Pleural Line | Vertical Artifacts | Deep Parenchyma |
|--------|-------------|-------------------|-----------------|
| 1–3 | Bright, continuous; lung sliding present | 1–2 discrete hyperechoic vertical rays arising from pleural line | Large hypoechoic/solid-appearing mass occupying lower-left field; sharp upper border, irregular deep border |
| 4–6 | Same; minor respiratory excursion visible | Similar discrete vertical artifacts persist; A-lines visible laterally | Hypoechoic region grows slightly with respiratory phase; deep margin remains irregular/shredded |
| 7–10 | Consistent pleural line; sliding maintained | Discrete B-lines again visible adjacent to consolidation zone | Hyperechoic punctate/linear foci appear *within* the hypoechoic region — dynamic, suggesting air-filled bronchi |

---

## B-Lines Assessment

### Observations
- In multiple frames (especially 1, 8–10), **discrete hyperechoic vertical artifacts** arise from the pleural line and extend toward the far field
- They are **well-separated**, with dark parenchyma visible between them
- They **do not merge** into a white sheet; A-lines remain visible in non-consolidated zones
- Movement is synchronous with lung sliding

### Conclusion
```
lung_rockets = true
subtype     = "septal"
```
> Discrete, spaced B-lines consistent with thickened interlobular septa — ≤3 per ICS, clearly individualized

---

## Consolidation Assessment

### Observations

| Sign | Finding |
|------|---------|
| **Hepatization** | Large region of tissue-like echogenicity (hypo-to-isoechoic, liver-like texture) occupying the lower-left lung field |
| **Shred Sign** | Deep border of the consolidated zone is **irregular and jagged**, transitioning abruptly to aerated lung |
| **Air Bronchograms** | In frames 7–10, **punctate and linear hyperechoic foci** appear *within* the hepatized region, consistent with air-filled bronchi; appear to move dynamically with respiration |

### Conclusion
```
consolidation       = true
consolidation_type  = "air_bronchogram"
```
> The dominant finding is **hepatized lung with air bronchograms**, indicating **alveolar consolidation** — most compatible with **pneumonia** (community-acquired or aspiration), where patent bronchi contain air within an otherwise airless, fluid-filled parenchyma.

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| `B-line subtype` | **septal** |
| `consolidation` | **true** |
| `consolidation_type` | **air_bronchogram** |

**Clinical Correlation:** This pattern — anterior zone consolidation with air bronchograms + adjacent septal B-lines — is highly characteristic of **lobar/segmental pneumonia**. The presence of dynamic air bronchograms (moving with respiration) further supports an **infectious/inflammatory consolidation** rather than obstructive atelectasis.
