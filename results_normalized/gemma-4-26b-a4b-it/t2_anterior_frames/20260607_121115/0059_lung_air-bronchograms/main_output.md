# 0059_lung_air-bronchograms

The sequential frames of this lung ultrasound (LUS) of the right anterior lung zone (Z4) show the following:

## B-lines Assessment
The ultrasound shows a relatively dark (hypoechoic) region of aerated lung just below the pleural line. There are no clear, discrete, or confluent hyperechoic vertical artifacts (B-lines) originating from the pleural line and extending to the bottom of the screen. The area above the consolidated lung lacks typical A-lines but does not demonstrate the characteristic "lung rocket" appearance of B-lines. Therefore, **lung_rockets = false**.

## Consolidation Assessment
There is a prominent area of lung consolidation in the lower portion of the field of view. 
- **Tissue-like hepatization**: The consolidated lung appears as a solid, highly echogenic (bright) mass with a texture resembling liver tissue.
- **Shred sign**: The boundary between the aerated lung (darker area) and the consolidated lung is irregular and "shredded."
- **Air bronchograms**: Within the hepatized tissue, small, punctate hyperechoic foci are visible, representing trapped air within the bronchi.

Because the tissue-like, liver-like appearance is the most striking feature of the consolidation, it is classified as hepatization. Therefore, **consolidation = true** and **consolidation_type = "hepatization"**.

**Summary:**
- **lung_rockets**: false
- **consolidation**: true
- **consolidation_type**: "hepatization"
