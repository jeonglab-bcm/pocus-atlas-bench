# 0083_lung_ftdbu61923rlre4jj2aj6yec8c57ei

# Lung Ultrasound Frame-by-Frame Analysis

## Technical Parameters
| Parameter | Value |
|-----------|-------|
| Probe | Curvilinear (C60) — Abdominal |
| Depth | 5.6 cm |
| Side | Left (L) |
| Mode | THI + MB On |
| Date | 2012-Mar-01 |

---

## Frame-by-Frame Observations

### Frames 1–3 (Baseline)
- Pleural line is identifiable as a hyperechoic curved structure in the near field
- **Below the pleural line**: echogenic, tissue-like parenchyma visible — **no normal A-line reverberation pattern**
- Heterogeneous, liver-like echogenicity beginning immediately sub-pleurally
- Punctate/linear **hyperechoic foci** visible within the echogenic parenchyma → suggestive of **air bronchograms**

### Frames 4–6 (Mid-sequence)
- Findings are consistent and stable
- The deep border of the consolidation zone is **irregular and poorly defined** → consistent with a **shred sign**
- No discrete vertical artifacts (B-lines) arising from the pleural line and extending to screen bottom
- The parenchymal texture remains **hepatized** (solid, liver-like)

### Frames 7–10 (Late sequence)
- Same consolidation pattern persists — confirms this is **not motion artifact**
- Air bronchograms (hyperechoic linear/punctate structures) remain visible within the hepatized zone
- No A-lines visible anywhere in the field
- No classic discrete or confluent B-lines identified

---

## B-Lines Assessment

| Finding | Result |
|---------|--------|
| **lung_rockets** | **false** |
| Subtype | null |

**Reasoning:**
- No hyperechoic vertical artifacts arise from the pleural line and extend to the bottom of the screen
- A-lines are absent — replaced entirely by the consolidation pattern
- The bright parenchyma represents solid tissue, **not B-line artifacts**

---

## Consolidation Assessment

| Finding | Result |
|---------|--------|
| **consolidation** | **true** |
| **consolidation_type** | **air_bronchogram** |

**Supporting Evidence:**

✅ **Hepatization**: Sub-pleural lung parenchyma demonstrates solid, liver-like echogenicity across all frames — loss of normal aerated lung appearance

✅ **Air Bronchograms**: Multiple punctate and short linear hyperechoic foci are visible within the consolidated tissue — representing trapped air within bronchi

✅ **Shred Sign**: The deep border of the consolidated zone is irregular and shredded — indicating the interface between consolidated and adjacent aerated (or partially aerated) lung

---

## Summary & Clinical Interpretation

```
lung_rockets    = false
consolidation   = true
consolidation_type = "air_bronchogram"
```

> **Pattern**: Anterior left lung **alveolar consolidation** with air bronchograms and shred sign, without B-lines.

**Differential diagnosis for this LUS pattern:**
1. 🦠 **Community-acquired pneumonia** *(most likely — air bronchograms suggest patent bronchi within infected alveoli)*
2. 🫁 **Obstructive atelectasis** *(fluid bronchograms rather than air would be expected)*
3. 💉 **Pulmonary infarction** *(wedge-shaped, subpleural; less likely anteriorly)*

The **dynamic air bronchograms** (if motion is visible in the clip — which these frames suggest given the sequential changes in hyperechoic foci position) would strongly favor **infectious pneumonia** over atelectasis.
