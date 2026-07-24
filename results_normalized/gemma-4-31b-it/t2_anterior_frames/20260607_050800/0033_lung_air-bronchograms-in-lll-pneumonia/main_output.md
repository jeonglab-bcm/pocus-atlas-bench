# 0033_lung_air-bronchograms-in-lll-pneumonia

Across the sequential frames of the ultrasound clip for the left lung zone 2, the findings remain consistent.

### Frame-by-Frame Analysis
In every frame, the normal appearance of the lung (which should show a distinct pleural line with horizontal A-lines or vertical B-lines) is absent. Instead, a large portion of the lung field is replaced by a solid, tissue-like region with an echogenicity similar to the liver. Within this consolidated area, there are multiple bright, hyperechoic punctate and linear foci. The border between this solid tissue and the remaining darker regions is irregular and "shredded."

### B-lines Assessment
There are no hyperechoic vertical artifacts arising from the pleural line and extending to the bottom of the screen. The normal pleural interface is largely obscured by the consolidation.
- **lung_rockets = false**

### Consolidation Assessment
The image displays several hallmark signs of alveolar consolidation:
- **Tissue-like hepatization:** The lung parenchyma has lost its aeration and appears solid and liver-like in texture.
- **Shred sign:** There is an irregular, jagged border where the consolidated lung meets aerated lung.
- **Air bronchograms:** There are distinct, bright hyperechoic foci within the consolidated lung, representing air trapped in the bronchi.

Because these features are clearly present, consolidation is confirmed. The most specific diagnostic feature visible within the hepatized lung is the presence of air bronchograms.
- **consolidation = true**
- **consolidation_type = "air_bronchogram"**
