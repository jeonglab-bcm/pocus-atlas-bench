# 0133_lung_jr_subpleuralconsolidation

# Right Upper Lung Zone — Sequential LUS Frame Analysis

---

## Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| **1** | Pleural line intact; clustered hyperechoic nodular foci below pleural line; no vertical laser-like artifacts extending to screen bottom |
| **2** | Large hypoechoic/anechoic mass-like area (right side); scattered bright foci; deep border suggests hepatization |
| **3** | Multiple punctate + curvilinear hyperechoic foci within hypoechoic tissue — early air bronchogram pattern |
| **4** | **Most diagnostic frame**: Large heterogeneous echogenic zone with liver-like texture; multiple discrete hyperechoic punctate and branching foci = classic air bronchograms |
| **5** | Large dark consolidated zone (right); irregular/shredded deep border visible; transition to aerated lung |
| **6** | Similar to Frame 5; irregular shred-sign interface; hyperechoic foci persist within hepatized zone |
| **7** | Clustered bright air bronchograms; hepatized parenchyma; no B-line criteria met |
| **8** | Heterogeneous hepatization; scattered internal echogenic foci (air bronchograms) |
| **9** | Bright clustered nodular foci; hepatized background tissue |
| **10** | Hepatized tissue with prominent internal air bronchograms; irregular deep border |

---

## B-Lines Assessment

### ❌ `lung_rockets = false`

**Reasoning:**
- **No laser-like vertical artifacts** arise from the pleural line and extend unattenuated to the screen bottom
- The bright hyperechoic foci seen are **intrapulmonary** (within hepatized tissue), not pleural-line-origin artifacts
- **No A-lines** visible either — the normal reverberation pattern is obliterated by consolidation
- Subtype: `null`

---

## Consolidation Assessment

### ✅ `consolidation = true`

**Evidence across frames:**

| Sign | Present | Description |
|------|---------|-------------|
| **Hepatization** | ✅ | Liver-like tissue echogenicity replacing normal aeration pattern |
| **Air bronchograms** | ✅ *(dominant)* | Multiple punctate + branching hyperechoic foci within hepatized lung |
| **Shred sign** | ✅ | Irregular deep border between consolidated and residually aerated parenchyma (Frames 5–6) |

### `consolidation_type = "air_bronchogram"`

> Air bronchograms are the **predominant and most consistently visible** pattern across all 10 frames, representing trapped/patent air-filled bronchi within the consolidated lung parenchyma.

---

## Summary

```
lung_rockets       = false
consolidation      = true
consolidation_type = "air_bronchogram"
```

**Clinical Interpretation:**
This pattern — **hepatized lung with air bronchograms and shred sign** in the right upper anterior zone — is highly consistent with **lobar or segmental pneumonia**. The air bronchograms suggest patent (non-obstructed) bronchi, favoring **infectious consolidation** over obstructive atelectasis. Correlation with clinical findings and chest X-ray/CT is recommended.
