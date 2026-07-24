# 0036_lung_dynamic-air-bronchograms

Across the sequential frames of the lung ultrasound video clip, the following observations are made:

**B-lines Assessment:**
There are no hyperechoic vertical artifacts (lung rockets) arising from the pleural line that extend to the bottom of the screen. The normal pleural line and A-line patterns are obscured by the underlying pathology. Therefore, B-lines are absent.
- **lung_rockets: false**

**Consolidation Assessment:**
The images show a large area of lung parenchyma that has lost its normal aeration and instead exhibits a solid, tissue-like appearance resembling the liver, which is characteristic of **hepatization**. Within this consolidated tissue, there are multiple punctate and linear hyperechoic (bright) foci, which represent **air bronchograms** (air trapped within the bronchi of a consolidated lung). The border between the consolidated and non-consolidated areas is irregular, suggesting a **shred sign**. Because these signs are present, consolidation is confirmed. The presence of distinct air bronchograms within the hepatized lung is a prominent feature.
- **consolidation: true**
- **consolidation_type: "air_bronchogram"**
