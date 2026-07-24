# 0130_lung_jr_pedsptxx

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Sub-pleural Zone | Deep Border | Notable Features |
|-------|-------------|------------------|-------------|-----------------|
| 1 | Irregular, hyperechoic | Heterogeneous, confluent brightness | Irregular | Diffuse white lung zone |
| 2 | Irregular | Confluent bright zone, coalescing | Shredded | Similar pattern |
| 3 | Slightly thickened | Bright, merging artifacts | Ill-defined | Confluent B-lines |
| 4-10 | Consistently irregular | Persistent heterogeneous echogenicity | Irregular, shredded deep margin | Stable pathological pattern across frames |

**Consistent across all frames:**
- The **pleural line** is irregular and discontinuous in areas
- A complex, heterogeneous **echogenic zone** occupies the sub-pleural lung field
- A **relatively hypoechoic band** is present deeper, with an irregular transition zone
- Bright punctate/linear foci are scattered within the echogenic zone

---

## B-Lines Assessment

### ✅ `lung_rockets = true`

**Observations:**
- Vertical hyperechoic artifacts arise from the pleural line
- These artifacts **coalesce and merge** rather than appearing as discrete, spaced lines
- A-lines are **completely abolished** — replaced by a diffuse bright "white lung" appearance
- The merging is persistent and consistent across all 10 frames, confirming real pathology (not artifact)

### Subtype: **`ground_glass`**

> The B-lines are **confluent and coalescing**, forming a continuous white sheet below the pleural line without visible dark lung parenchyma between them — consistent with alveolar flooding or severe interstitial disease.

---

## Consolidation Assessment

### ✅ `consolidation = true`

**Observations:**
- The sub-pleural zone shows **tissue-like hepatization** — the lung parenchyma has lost its normal aeration and appears solid and echogenic, resembling liver texture
- The **deep border** between the consolidated zone and the underlying lung is **irregular and shredded** — not a smooth transition
- Within the echogenic zone, **bright punctate/linear hyperechoic foci** are visible, compatible with **air bronchograms**

### Consolidation Type: **`shred_sign`** (predominant) with **air bronchograms**

> The deep, ragged, irregular border between consolidated and partially aerated lung is the **dominant finding** across all frames, consistent with the **shred sign**. Air bronchograms are present as secondary features within the consolidated tissue.

---

## Summary & Interpretation

```
lung_rockets       = true
b_line_subtype     = "ground_glass"
consolidation      = true
consolidation_type = "shred_sign"
```

### Clinical Correlation

This ultrasound pattern — combining **ground-glass confluent B-lines + subpleural consolidation with shred sign + air bronchograms** in the **anterior zone** — is most consistent with:

| Differential | Supporting Features |
|---|---|
| **Pneumonia** (most likely) | Shred sign, air bronchograms, focal consolidation |
| **COVID-19 pneumonitis** | Ground-glass B-lines + shred sign, anterior involvement |
| **Atelectasis** | Hepatization, but less likely anteriorly without effusion |
| **Pulmonary edema** | Ground-glass B-lines present, but shred sign/air bronchograms favor infection |

> ⚠️ **The stability of findings across all sequential frames** confirms these are true pathological features, not motion or probe-pressure artifacts. Clinical correlation with fever, SpO₂, and inflammatory markers is recommended.
