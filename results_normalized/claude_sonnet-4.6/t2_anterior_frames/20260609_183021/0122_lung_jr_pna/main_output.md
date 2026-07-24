# 0122_lung_jr_pna

# Lung Ultrasound — Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Sub-pleural Field | Deep Field Artifacts |
|-------|-------------|-------------------|----------------------|
| 1–3 | Bright, well-defined | Relatively dark/anechoic | Homogeneous, no discrete foci |
| 4–5 | Intact | Slightly heterogeneous | Emerging small hyperechoic foci, ~2–3 cm depth |
| 6–7 | Intact | Increased echogenicity | Foci become more organized, linear/punctate |
| 8–10 | Intact | Heterogeneous, echogenic | Multiple bright linear/punctate foci scattered through mid-deep field |

---

## B-Lines Assessment

**Observation:** No vertical hyperechoic artifacts arise from the pleural line and extend to the bottom of the screen. The dominant deep-field artifacts are **horizontal/punctate**, not laser-beam vertical artifacts. A-line pattern is partially visible in early frames.

> ✅ **lung_rockets = false**
> **Subtype: null**

---

## Consolidation Assessment

**Observation:**
- In frames 4–10, the **deep parenchyma becomes progressively echogenic** with a tissue-like, heterogeneous texture
- Multiple **punctate and short linear hyperechoic foci** appear scattered throughout the consolidation, **not connected to the pleural line**
- These represent **air-filled bronchi within hepatized lung** — classic **air bronchograms**
- The deep border appears **irregular/shredded** in several frames, suggesting interface with remaining aerated lung

> ✅ **consolidation = true**
> **consolidation_type = "air_bronchogram"**

---

## Summary

| Parameter | Finding |
|-----------|---------|
| `lung_rockets` | **false** |
| `b_line_subtype` | **null** |
| `consolidation` | **true** |
| `consolidation_type` | **air_bronchogram** |

**Clinical Interpretation:** The anterior zone shows **alveolar consolidation with air bronchograms**, suggesting pneumonia, lobar atelectasis, or early ARDS consolidation phase. Absence of B-lines and presence of air bronchograms in an anterior zone is particularly concerning for **infectious/inflammatory consolidation**.
