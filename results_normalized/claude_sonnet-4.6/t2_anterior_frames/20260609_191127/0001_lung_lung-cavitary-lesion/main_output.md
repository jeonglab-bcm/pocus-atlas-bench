# 0001_lung_lung-cavitary-lesion

# Left Anterior Lung Ultrasound — Sequential Frame Analysis

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| **1–2** | Hypoechoic, tissue-like (hepatized) region deep to the pleural line; a curved, bright hyperechoic arc appears at ~6–7 cm — early consolidation border; no A-lines; no vertical B-lines |
| **3–4** | The curved hyperechoic structure becomes more prominent and irregular; the overlying parenchyma is uniformly hypoechoic with liver-like echogenicity; multiple punctate bright foci begin to emerge within the consolidated tissue |
| **5–6** | Fragmented, scattered hyperechoic foci clearly visible within the hypoechoic consolidated region — classic **air bronchogram** pattern; deep border is irregular and shredded |
| **7–8** | Respiratory motion changes the viewing angle; air bronchograms transition to elongated linear hyperechoic structures (linear air bronchograms) moving dynamically |
| **9–10** | More linear, dual-layer echogenic structures; the consolidated region is still present but appears thinner; underlying deep field is anechoic — no aeration artifacts recovered |

---

## B-Lines Assessment

### Findings
> No classic **B-lines** (laser-like vertical artifacts arising from the pleural line, extending uninterrupted to the screen bottom) are identified in any frame.

The bright vertical/oblique artifacts visible are **intrapulmonary** (air bronchograms within consolidated tissue), not originating from the pleural line. A-lines are also **absent**, replaced entirely by tissue-like echogenicity.

```
lung_rockets = false
subtype = null
```

---

## Consolidation Assessment

### Findings

Three consolidation signs are present across the sequential frames:

1. **Hepatization** ✅
   - The lung parenchyma between the pleural line and the deep bright structures exhibits **liver-like echogenicity** — uniform, medium-level gray echogenicity — in all frames, confirming tissue-like consolidation.

2. **Air Bronchograms** ✅
   - Frames 4–8: Multiple **punctate and linear hyperechoic foci** move dynamically within the consolidated tissue.
   - Branching linear pattern in frames 7–8 confirms **dynamic air bronchograms** (indicating patent airways with preserved airflow → favors **pneumonia** over atelectasis).

3. **Shred Sign** ✅ (partial)
   - The deep border of consolidated tissue in frames 4–6 is **irregular and shredded**, representing the interface between consolidated and partially aerated lung.

```
consolidation = true
consolidation_type = "air_bronchogram"
(with co-existing hepatization and shred sign)
```

---

## Conclusion

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **false** |
| `B-line subtype` | null |
| `consolidation` | **true** |
| `consolidation_type` | **air_bronchogram** |

### Clinical Interpretation
The sequential frames demonstrate **left anterior lung consolidation** characterized by:
- **Hepatization** of the parenchyma
- **Dynamic air bronchograms** (highly specific for **infectious pneumonia**)
- **Shred sign** at the deep consolidation border

The presence of **dynamic (rather than static) air bronchograms** is a key differentiating feature, suggesting **patent conducting airways** with **alveolar filling** — most consistent with **community-acquired pneumonia** rather than resorptive atelectasis. Correlation with clinical findings (fever, CRP, SpO₂) and chest X-ray is recommended.
