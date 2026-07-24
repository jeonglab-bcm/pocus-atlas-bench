# 0057_lung_blines-in-pulmonary-contusion

The analysis of the sequential lung ultrasound frames reveals the following:

**B-lines Assessment:**
*   **Observation:** In the initial frames (1-3), there are vertical hyperechoic artifacts arising from the pleural line. These lines appear relatively discrete and spaced, consistent with **septal** B-lines. However, in frame 4, the vertical artifacts become more numerous and coalesce, creating a "white lung" appearance or a diffuse bright zone, which is characteristic of **ground-glass** B-lines. This transition or coexistence of discrete and confluent patterns fits the **mixed** classification.
*   **Conclusion:** `lung_rockets = true`, `subtype = mixed`.

**Consolidation Assessment:**
*   **Observation:** Frames 4, 5, and 6 display a significant area of tissue-like, echogenic parenchyma that resembles liver tissue (**hepatization**), indicating a loss of normal aeration. Within this consolidated area, specifically in frames 5 and 6, there are distinct, punctate linear hyperechoic foci. These are **air bronchograms**, representing air-filled bronchi surrounded by fluid or cellular debris. The border between the consolidated area and adjacent tissue (visible in frame 5) appears irregular, suggestive of a shred sign, but the air bronchograms are a prominent internal feature.
*   **Conclusion:** `consolidation = true`. Given the distinct hyperechoic foci within the consolidated lung, the predominant type is `air_bronchogram`.

**Final Classification:**
*   **lung_rockets:** true
*   **subtype:** mixed
*   **consolidation:** true
*   **consolidation_type:** air_bronchogram
