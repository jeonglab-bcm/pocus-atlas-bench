# 0010_lung_pulmonary-shunt-in-pneumonia

Based on the analysis of the provided lung ultrasound frames:

### B-lines Assessment
Throughout the sequence, there are no hyperechoic vertical artifacts originating from the pleural line. The typical "lung rocket" appearance is absent because the normal aeration of the lung is lost.
- **lung_rockets = false**

### Consolidation Assessment
The lung parenchyma exhibits a classic "hepatization" pattern. Instead of the usual air-filled appearance with A-lines or B-lines, the lung appears as a solid, moderately echogenic mass with a texture resembling liver tissue. The use of color Doppler (the green box) reveals vascularity within this tissue, which is a key finding to confirm consolidated lung parenchyma and differentiate it from a pleural effusion. Small hyperechoic foci are also visible, suggesting air bronchograms.
- **consolidation = true**
- **consolidation_type = "hepatization"**

**Conclusion:**
The images show a complete loss of normal lung aeration with a predominant pattern of tissue-like hepatization, confirmed by the presence of internal vascularity on color Doppler. No B-lines are present.
