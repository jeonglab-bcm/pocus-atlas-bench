# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Frame-by-Frame Analysis

## Frame-by-Frame Assessment

**Frame 1:** The pleural line is visible at ~2 cm depth. Below it, a subpleural area of tissue-like echogenicity is seen. A broad, bright vertical artifact extends from the pleural line toward the bottom of the screen. The artifact appears wide and somewhat confluent.

**Frame 2:** Similar to Frame 1. A bright vertical artifact (B-line) descends from the pleural line. The subpleural area shows increased echogenicity with a tissue-like texture. The B-line extends to the far field.

**Frame 3:** The pleural line is irregular. A vertical hyperechoic artifact extends downward. Subpleural tissue appears heterogeneously echogenic, suggesting early consolidation/hepatization.

**Frame 4:** This frame shows the most convincing consolidation. Multiple bright **punctate hyperechoic foci** are visible within tissue-like (hepatized) lung parenchyma. These represent **air bronchograms**. The pleural line is irregular with multiple echogenic spots.

**Frame 5:** Clear consolidation with hepatized lung tissue. Multiple **punctate and linear hyperechoic foci (air bronchograms)** are prominent within the solid-appearing parenchyma. The consolidated area extends several centimeters deep.

**Frame 6:** The pleural line shows irregularity. Below it, partially hepatized tissue is visible with some hyperechoic foci. B-line artifacts extend from the border of the consolidated region.

**Frame 7:** The pleural surface appears irregular with a **shredded deep border** between consolidated and aerated lung. The transition is ragged/irregular (shred sign).

**Frame 8:** Similar irregular pleural interface. Small subpleural consolidation visible with an irregular deep margin. The far field shows some vertical artifacts.

**Frame 9:** A bright hyperechoic focus (likely air bronchogram) is seen within a region of hepatized tissue. Surrounding tissue appears heterogeneous.

**Frame 10:** Relatively more aerated-appearing lung with some B-line artifacts extending into the far field. These appear somewhat confluent.

---

## B-lines Assessment

**Observation:** Multiple frames demonstrate vertical hyperechoic artifacts arising from the pleural line and extending to the bottom of the screen. In several frames (particularly 1-3, 6, 10), these artifacts appear **confluent and coalescing**, creating a diffuse bright "white-out" pattern in the far field rather than discrete, well-separated lines. A-lines are obliterated in most frames.

**Conclusion:**
- **lung_rockets = true**
- **Subtype: ground_glass** — The B-lines coalesce into a near-continuous bright sheet, consistent with diffuse alveolar-interstitial syndrome (confluent B-lines).

---

## Consolidation Assessment

**Observation:** Across multiple frames (especially 4, 5, 7, 9), there is:
1. **Hepatization**: Tissue-like echogenicity of the lung parenchyma, resembling liver texture, with loss of normal aeration artifacts.
2. **Air bronchograms**: Multiple punctate and linear hyperechoic foci within the hepatized lung (most prominent in frames 4–5).
3. **Shred sign**: Irregular, shredded deep border between consolidated and aerated lung (most visible in frame 7).

**Conclusion:**
- **consolidation = true**
- **consolidation_type = "air_bronchogram"** — The predominant finding is punctate/linear hyperechoic foci within hepatized lung tissue, consistent with air-filled bronchi trapped within consolidated parenchyma.

---

## Summary

| Finding | Result |
|---------|--------|
| B-lines | **Present** |
| B-line subtype | **Ground glass** (confluent) |
| Consolidation | **Present** |
| Consolidation type | **Air bronchogram** |

This pattern is consistent with significant alveolar disease (e.g., pneumonia, ARDS) with anterior zone consolidation containing air bronchograms and surrounding confluent B-lines indicating diffuse alveolar edema/inflammation.
