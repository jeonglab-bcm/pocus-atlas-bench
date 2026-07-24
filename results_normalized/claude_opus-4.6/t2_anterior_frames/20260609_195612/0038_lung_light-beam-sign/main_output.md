# 0038_lung_light-beam-sign

# Lung Ultrasound Analysis: Frame-by-Frame

## Frame-by-Frame Assessment

**Frame 1:** The pleural line is visible as a bright hyperechoic line with chest wall layers above. Below the pleural line, the field is predominantly dark with a faint vertical artifact beginning to appear.

**Frame 2:** A prominent vertical hyperechoic artifact (B-line) extends from the pleural line downward toward the bottom of the screen. It is narrow and laser-like.

**Frame 3:** A very clear, well-defined single B-line extends from the pleural line all the way to the bottom of the screen without fading. This is a classic B-line appearance.

**Frame 4:** Similar to frame 3 — a single discrete B-line persists. There is some increased echogenicity near the pleural interface but no tissue-like pattern.

**Frame 5:** The B-line artifact is less prominent; the pleural line remains clearly identified with normal chest wall layers above.

**Frame 6:** The pleural line is bright; below it, the artifact extends downward but is slightly less conspicuous.

**Frame 7:** A vertical artifact again extends from the pleural line downward — discrete and well-separated from surrounding dark lung parenchyma.

**Frame 8:** Some brighter echogenicity near the pleural line; a vertical artifact is visible extending deep.

**Frame 9:** Multiple chest wall layers visible; below the pleural line, vertical artifacts and some irregular echogenicity are noted.

**Frame 10:** A clear single B-line is visible extending to the screen bottom, with a small hyperechoic focus deeper in the field.

---

## B-lines Assessment

**Observation:** Across the clip, discrete vertical hyperechoic artifacts arise from the pleural line and extend to the bottom of the screen without fading. They are well-separated with dark (aerated) lung parenchyma visible between them. There are approximately 1–2 B-lines visible per frame, and they move with the pleural line/lung sliding.

**Conclusion:**
- **lung_rockets = true**
- **Subtype = septal**

These are discrete, well-spaced B-lines consistent with thickened interlobular septa. They do not coalesce into a "white lung" or ground-glass pattern.

---

## Consolidation Assessment

**Observation:** The bright structures in the near field represent normal chest wall layers (subcutaneous tissue, intercostal muscles, and the pleural line). Below the pleural line, no tissue-like hepatization is identified — there is no solid, liver-like echotexture of the lung parenchyma. No shred sign (irregular deep border between consolidated and aerated lung) is seen. No definitive air bronchograms (punctate/linear hyperechoic foci within hepatized tissue) are present. The dominant subpleural pattern is aerated lung generating B-line artifacts.

**Conclusion:**
- **consolidation = false**
- **consolidation_type = null**

---

## Summary

| Finding | Result |
|---------|--------|
| B-lines (lung rockets) | **Present** |
| B-line subtype | **Septal** |
| Consolidation | **Absent** |
| Consolidation type | **Null** |
