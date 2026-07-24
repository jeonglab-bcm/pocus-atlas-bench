# 0057_lung_blines-in-pulmonary-contusion

# Lung Ultrasound Analysis: Frame-by-Frame Assessment

## Frame-by-Frame Description

**Frames 1–3:** The pleural line is visible at approximately 2–3 cm depth. Below it, there is a region of tissue-like echogenicity (hepatization) with an irregular, shredded deep border. Vertical hyperechoic artifacts extend from the aerated deep border toward the bottom of the screen. The artifacts appear relatively confluent.

**Frames 4–5:** These are the most diagnostic frames. Clear **punctate and linear hyperechoic foci** are visible within a solid, tissue-like (hepatized) lung parenchyma. These represent **air bronchograms**—air trapped in bronchi surrounded by consolidated, non-aerated tissue. The irregular deep margin of the consolidation is also evident.

**Frame 6:** Shows a transition zone with consolidated tissue superficially and confluent B-lines extending from the aerated boundary into deeper lung.

**Frames 7–8:** A different scanning angle showing a large area of tissue-like hepatization extending from the pleural line with minimal aeration artifacts. The lung appears almost entirely consolidated in this plane.

**Frame 9:** A focal area of bright hyperechoic consolidation with surrounding tissue-like echotexture and some B-lines at the margins.

**Frame 10:** More B-lines visible extending to the bottom of the screen with less consolidation, representing an adjacent partially aerated zone.

---

## B-lines Assessment

**lung_rockets = true**

Vertical hyperechoic artifacts are present in multiple frames, arising from the pleural line/consolidation border and extending without fading. In the frames showing aerated lung (frames 6, 10), these artifacts are **confluent and coalescing**, forming a diffuse bright sheet below the pleural line rather than discrete, spaced lines.

**Subtype: ground_glass**

The B-lines merge into white-out areas, indicating significant alveolar/interstitial involvement consistent with diffuse loss of aeration.

---

## Consolidation Assessment

**consolidation = true**

Multiple clear consolidation signs are present:
1. **Hepatization:** Tissue-like echotexture resembling liver is seen in frames 1–8
2. **Shred sign:** Irregular, shredded deep border between consolidated and aerated lung (frames 1–3, 6)
3. **Air bronchograms:** Punctate and linear hyperechoic foci within hepatized lung (frames 4–5, most prominent)

**consolidation_type = "air_bronchogram"**

The predominant and most diagnostic finding is the presence of **bright hyperechoic punctate/linear foci within hepatized lung parenchyma**, clearly visible in frames 4–5. This represents air-filled bronchi within non-aerated, consolidated alveolar tissue—a hallmark of alveolar consolidation (e.g., pneumonia, ARDS).

---

## Summary

| Finding | Result | Subtype |
|---------|--------|---------|
| B-lines | **Present** | **Ground glass** (confluent) |
| Consolidation | **Present** | **Air bronchogram** |

**Clinical Correlation:** The combination of anterior zone consolidation with air bronchograms and confluent B-lines in an anterior zone is highly concerning for significant lung pathology such as ARDS, severe pneumonia, or advanced pulmonary edema with associated atelectasis/consolidation.
