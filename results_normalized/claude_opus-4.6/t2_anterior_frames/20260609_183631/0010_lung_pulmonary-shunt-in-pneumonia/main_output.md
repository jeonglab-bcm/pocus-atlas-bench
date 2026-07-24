# 0010_lung_pulmonary-shunt-in-pneumonia

# Lung Ultrasound Analysis: Sequential Frame Assessment

## Frame-by-Frame Analysis

**Frames 1, 4, 5:** A color Doppler box (cyan outline) is placed over the lung region. The grayscale background reveals a relatively echogenic, tissue-like parenchyma below the pleural line. Scattered, sparse blue and red Doppler signals are present, indicating low-velocity vascular flow within the tissue.

**Frame 2:** A larger red Doppler signal appears superiorly within the box, suggesting a pulsating vessel within solid-appearing tissue. The surrounding parenchyma maintains its tissue-like echotexture.

**Frame 3:** Prominent blue Doppler signals cluster throughout the tissue, demonstrating diffuse vascularity — a hallmark of hepatized (consolidated) lung.

**Frame 6 & 10:** Large red Doppler signals in the inferior portion of the box confirm significant arterial flow within the solid-appearing lung tissue. This "color flow within tissue" sign is strongly supportive of consolidation.

**Frames 7, 8, 9:** Persistent scattered vascular signals (blue > red) within echogenic, solid-appearing parenchyma.

## B-lines Assessment

**Observation:** No vertical hyperechoic artifacts are seen arising from the pleural line and extending to the bottom of the screen. No A-lines are visible either, as the normal air-tissue interface has been replaced by consolidated tissue. The pattern is dominated by solid tissue echotexture rather than reverberation artifacts.

**Conclusion:**
- **lung_rockets = false**
- **Subtype = null**

## Consolidation Assessment

**Observations:**
1. **Tissue-like hepatization:** The lung parenchyma below the pleural line appears solid, echogenic, and resembles liver texture throughout the clip. The normal aeration pattern is completely absent.
2. **Vascularity within tissue:** Color Doppler demonstrates both arterial (red) and venous (blue) blood flow within the consolidated parenchyma — this is pathognomonic for true hepatization and distinguishes it from artifacts.
3. **Possible air bronchograms:** Small punctate hyperechoic foci are visible within the hepatized tissue in several frames (especially frames 4–5), suggesting air-filled bronchi within airless lung.

**Conclusion:**
- **consolidation = true**
- **consolidation_type = "hepatization"**

## Summary

| Finding | Result |
|---------|--------|
| B-lines | **Absent** |
| Consolidation | **Present** |
| Consolidation Type | **Hepatization** |

The anterior zone demonstrates significant alveolar consolidation with a hepatized, tissue-like pattern and demonstrable vascularity on color Doppler. The presence of vascular flow within solid-appearing lung tissue in an anterior zone is highly concerning for extensive consolidation (e.g., pneumonia, ARDS, or atelectasis).
