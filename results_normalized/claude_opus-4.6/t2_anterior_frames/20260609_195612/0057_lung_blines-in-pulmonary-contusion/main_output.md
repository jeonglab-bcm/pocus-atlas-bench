# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Analysis: Frame-by-Frame Assessment

## Frame-by-Frame Analysis

**Frames 1–3:** The pleural line is identifiable at approximately 2–3 cm depth. A broad, bright vertical artifact extends from the pleural line toward the bottom of the screen. The subpleural lung parenchyma shows a diffuse "white-out" pattern with confluent hyperechoic artifacts, obscuring A-lines. There is tissue-like echogenicity immediately beneath the pleural line.

**Frames 4–5:** The pleural line shows multiple irregular hyperechoic foci. Below the pleural line, lung parenchyma appears solid and tissue-like (hepatized). Within this consolidated tissue, multiple **punctate hyperechoic foci** are clearly visible — consistent with **air bronchograms**. The deep border is irregular/shredded.

**Frames 6:** Transition zone visible with some B-line artifacts and partial hepatization in the near field.

**Frames 7–8:** A different scanning angle showing the pleural surface laterally. The lung parenchyma appears markedly consolidated with tissue-like echogenicity (hepatization). Near-complete loss of normal aeration pattern.

**Frame 9:** A rounded hyperechoic focus is visible within tissue-like consolidated lung — clearly an **air bronchogram**. Surrounding tissue shows hepatization.

**Frame 10:** Diffuse whitening below the pleural line with confluent B-lines creating a "white lung" appearance.

---

## B-lines Assessment

**lung_rockets = true**

**Subtype: ground_glass**

In the non-consolidated portions of the clip (particularly frames 1–3, 6, 10), confluent B-lines coalesce into a diffuse white sheet, obscuring A-lines entirely. No discrete, well-separated B-lines are identifiable — the pattern is uniformly bright, consistent with the ground-glass (confluent) subtype.

---

## Consolidation Assessment

**consolidation = true**

**consolidation_type = "air_bronchogram"**

Multiple frames (4, 5, 7, 8, 9) demonstrate clear alveolar consolidation characterized by:
- **Hepatization:** Tissue-like solid echogenicity of the lung parenchyma resembling liver
- **Air bronchograms:** Punctate and linear hyperechoic foci within the consolidated tissue (most prominent in frames 4–5 and 9)
- **Shred sign:** Irregular deep border between consolidated and partially aerated lung visible in transitional zones

The **predominant consolidation type is air_bronchogram**, as the bright punctate foci within hepatized lung are the most conspicuous and diagnostic feature across multiple frames.

---

## Summary

| Finding | Result | Subtype |
|---------|--------|---------|
| B-lines | **Present** | **Ground glass** (confluent) |
| Consolidation | **Present** | **Air bronchogram** |

**Clinical Correlation:** This anterior zone pattern of consolidation with air bronchograms and surrounding confluent B-lines is highly concerning for significant alveolar pathology (e.g., pneumonia, ARDS) in an anterior zone — a region that is normally well-aerated.
