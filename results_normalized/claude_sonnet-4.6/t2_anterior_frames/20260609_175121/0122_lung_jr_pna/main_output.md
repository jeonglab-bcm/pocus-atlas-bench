# 0122_lung_jr_pna

# Lung Ultrasound Analysis — Sequential Frame Review

## Frame-by-Frame Observations

| Frames | Pleural Line | Deep Field | Notable Artifacts |
|--------|-------------|------------|-------------------|
| 1–3 | Bright, relatively smooth, mobile | Predominantly anechoic/dark | Faint horizontal A-line reverberations; no vertical artifacts from pleural line |
| 4–6 | Mildly irregular, still identifiable | Increasing echogenicity; heterogeneous texture begins | Scattered punctate hyperechoic foci emerge in deeper parenchyma |
| 7–10 | Irregular, partially disrupted | Clearly heterogeneous, tissue-like (hepatized) echo texture | Multiple punctate/short linear hyperechoic foci throughout parenchyma; no continuous vertical laser-like lines reaching screen bottom |

---

## B-Lines Assessment

### Observations
- **No classic B-lines identified** in any frame.
- Frames 1–3 demonstrate a normal A-line pattern (horizontal reverberation artifacts), indicating preserved anterior aeration.
- The hyperechoic foci appearing in frames 4–10 **do not arise from the pleural line** and **do not extend vertically to the bottom of the screen** — they fail B-line criteria.

### Conclusion
> **lung_rockets = `false`**
> **subtype = `null`**

---

## Consolidation Assessment

### Observations
- **Frames 4–10** show progressive transition from an aerated to a **non-aerated, tissue-like (hepatized)** parenchymal pattern.
- The deep lung loses its normal dark acoustic signature and takes on **liver-like echogenicity**.
- Multiple **punctate and short linear hyperechoic foci** are scattered throughout the hepatized parenchyma — classic morphology of **air bronchograms** (air-filled bronchi surrounded by fluid/cellular-filled alveoli).
- These foci are distinct from B-lines: they are **embedded within** the consolidated tissue, not arising from the pleural surface.
- No clearly defined shred sign at the deep border within the visible field.

### Conclusion
> **consolidation = `true`**
> **consolidation_type = `"air_bronchogram"`**

---

## Summary

```
lung_rockets       = false
consolidation      = true
consolidation_type = "air_bronchogram"
```

### Clinical Interpretation
The sequential clip captures an **anterior zone consolidation** with **air bronchograms**, most consistent with:
- **Lobar/segmental pneumonia** (air bronchograms within hepatized tissue)
- Less likely: compressive or absorptive atelectasis (dynamic air bronchograms would help distinguish)

The early frames (1–3) showing preserved A-lines suggest the consolidation may be **sub-pleural or partially aerated at the surface**, with deeper alveolar filling. This pattern warrants correlation with clinical findings, fever, inflammatory markers, and chest X-ray/CT.
