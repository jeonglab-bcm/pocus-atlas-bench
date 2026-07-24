# 0037_lung_pulmonary-contusion

# Lung Ultrasound Analysis: Frame-by-Frame

## Frame-by-Frame Assessment

**Frames 1-10:** Across all sequential frames, I observe:
- A well-defined, bright **pleural line** at the top of the image with overlying rib shadows creating acoustic shadowing on either side
- **2-3 discrete vertical hyperechoic artifacts** arising from the pleural line and extending to the bottom of the screen without fading
- **Dark lung parenchyma** clearly visible between these vertical artifacts
- The vertical lines appear to move subtly with respiration across frames, consistent with lung sliding
- No horizontal A-line reverberation artifacts are dominant — they are obscured by the B-lines
- No tissue-like or hepatized regions visible beneath the pleural line

## B-lines Assessment

**Observation:** Throughout all 10 frames, there are consistently 2-3 well-defined, discrete vertical hyperechoic lines originating from the pleural line, extending without fading to the far field. They are clearly separated by dark (aerated) lung parenchyma. They do not coalesce into a white-out pattern.

**Conclusion:**
- **lung_rockets = true**
- **Subtype = septal**

These are classic **septal B-lines**: discrete, well-spaced, with visible dark intervals between them, suggesting thickened interlobular septa (early interstitial edema or mild interstitial disease).

## Consolidation Assessment

**Observation:** There is no tissue-like (hepatized) echotexture below the pleural line. The pleural line remains smooth and well-defined. No shred sign (irregular deep border) is seen. No punctate or linear hyperechoic foci (air bronchograms) are identified within the subpleural space.

**Conclusion:**
- **consolidation = false**
- **consolidation_type = null**

## Summary

| Finding | Result |
|---------|--------|
| B-lines present | **True** |
| B-line subtype | **Septal** |
| Consolidation | **False** |
| Consolidation type | **Null** |
