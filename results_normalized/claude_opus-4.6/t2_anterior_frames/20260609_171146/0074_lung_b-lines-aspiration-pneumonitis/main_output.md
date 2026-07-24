# 0074_lung_b-lines-aspiration-pneumonitis

# Lung Ultrasound Frame-by-Frame Analysis

## Frame-by-Frame Description

**Frames 1–2:** The pleural line is clearly visible near the top of the image. A single, prominent hyperechoic vertical artifact arises from the pleural line and extends to the bottom of the screen. Some irregular echogenicity is noted at the pleural interface. Dark (anechoic) lung parenchyma surrounds the artifact.

**Frames 3–5:** A dominant, well-defined B-line persists from the pleural line to the far field. The surrounding lung field remains dark. No A-lines are visible. The B-line appears to shift slightly with respiratory movement, consistent with lung sliding.

**Frames 6–7 (timestamped 03/28/21):** Acquired with a C1-5 curvilinear abdominal probe. One to two B-lines are seen, with frame 7 showing possibly 2–3 parallel vertical artifacts. Some irregular echogenicity is noted at the pleural line but does not resemble solid tissue.

**Frames 8–10:** Return to a single dominant B-line. The pleural line is smooth. Surrounding lung is dark without evidence of hepatization or tissue-like echotexture. No air bronchograms are identified.

---

## B-lines Assessment

**Findings:**
- A consistent, well-defined hyperechoic vertical artifact arises from the pleural line in every frame
- It extends without fading to the bottom of the screen
- It moves with lung sliding (respiratory variation seen across sequential frames)
- Between B-lines, the lung parenchyma appears dark/anechoic
- Typically 1–3 discrete B-lines per intercostal space, clearly separated

**Conclusion:**

- **lung_rockets = true**
- **Subtype = septal**

The B-lines are discrete and well-spaced, with dark lung parenchyma visible between them, consistent with thickened interlobular septa. They do not coalesce into a white sheet (ruling out ground glass pattern).

---

## Consolidation Assessment

**Findings:**
- No tissue-like (hepatized) lung parenchyma identified
- No irregular "shredded" deep border between consolidated and aerated lung
- No punctate or linear hyperechoic foci (air bronchograms) within lung parenchyma
- The pleural line remains relatively smooth across frames
- Minor irregularity at the pleural interface does not meet criteria for true consolidation

**Conclusion:**

- **consolidation = false**
- **consolidation_type = null**

---

## Summary

| Finding | Result |
|---------|--------|
| B-lines present | **True** |
| B-line subtype | **Septal** |
| Consolidation | **False** |
| Consolidation type | **Null** |

**Interpretation:** This anterior zone demonstrates discrete septal B-lines without consolidation, a pattern consistent with early interstitial syndrome (e.g., early pulmonary edema, mild interstitial lung disease, or early ARDS). The absence of confluent/coalescing B-lines and consolidation suggests the process has not progressed to alveolar flooding or complete loss of aeration.
