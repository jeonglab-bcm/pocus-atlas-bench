# 0010_lung_pulmonary-shunt-in-pneumonia

## Frame-by-Frame Analysis

**Frames 1, 4, 5:** The region within the color Doppler box shows homogeneous, gray, tissue-like echotexture below the pleural line. Scattered minimal color Doppler signals (mostly blue) are present. No vertical B-line artifacts are seen. Small hyperechoic punctate foci are visible within the parenchyma.

**Frames 2, 6, 10:** More prominent red and blue color Doppler signals appear within the tissue-like parenchyma, indicating active blood flow (vascular sign). The tissue maintains its liver-like echogenicity. The large red flow signals in frames 6 and 10 confirm pulmonary vasculature coursing through non-aerated tissue.

**Frames 3, 7, 8, 9:** Predominantly blue Doppler signals with tissue-like echotexture persisting throughout. No horizontal A-lines or vertical B-lines are identified. The parenchyma appears uniformly solid.

---

## B-lines Assessment

**Observation:** Across all 10 frames, I do not identify hyperechoic vertical artifacts arising from the pleural line and extending to the bottom of the screen. The sub-pleural space is occupied by solid, tissue-like parenchyma rather than aerated lung. No A-lines are visible either, which is consistent with complete loss of aeration.

**Conclusion:** 
- **lung_rockets = false**
- No B-lines are present because the lung is fully consolidated (B-lines require a partially aerated air-fluid interface).

---

## Consolidation Assessment

**Observation:**
1. **Hepatization:** The lung parenchyma appears solid, homogeneous, and echogenic — closely resembling liver tissue throughout all frames.
2. **Vascular flow (color Doppler confirmation):** Red and blue signals within the consolidated tissue confirm preserved blood flow through non-aerated lung, supporting true tissue-like consolidation.
3. **Air bronchograms:** Scattered punctate hyperechoic foci are visible within the hepatized parenchyma (best seen in frames 1–4), representing air trapped within bronchi surrounded by consolidated lung.

**Conclusion:**
- **consolidation = true**
- **consolidation_type = "hepatization"**

The dominant finding is extensive anterior lung consolidation with a liver-like tissue pattern and preserved vascularity on color Doppler. Punctate air bronchograms are a supporting secondary finding within the hepatized lung.
