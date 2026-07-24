# 0039_lung_hepatization-of-lung

Based on the sequential frames of the lung ultrasound (LUS) clip:

**B-lines Assessment:**
There are no hyperechoic vertical artifacts (B-lines) extending from the pleural line to the bottom of the screen. The typical "lung rocket" appearance is absent.
- **lung_rockets = false**

**Consolidation Assessment:**
The lung parenchyma in the anterior zone exhibits a solid, tissue-like appearance that closely resembles the echogenicity of the liver, which is characteristic of **hepatization**. Furthermore, multiple punctate and linear hyperechoic foci are visible within this consolidated region, representing **air bronchograms**. The transition between the consolidated area and the remaining lung is irregular.
- **consolidation = true**
- **consolidation_type = "hepatization"** (The predominant finding is the overall tissue-like, liver-like appearance of the lung parenchyma, containing air bronchograms).

**Summary:**
- lung_rockets = false
- consolidation = true
- consolidation_type = "hepatization"
