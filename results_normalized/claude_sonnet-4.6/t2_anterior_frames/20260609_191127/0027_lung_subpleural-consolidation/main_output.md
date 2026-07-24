# 0027_lung_subpleural-consolidation

# Lung Ultrasound Analysis — RT H/T Zone 1 (Sequential Frames)

---

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| **1–3** | Pleural line clearly visible; deep field shows diffuse vertical hyperechoic streaking arising from pleural line, with some preservation of dark lung parenchyma between artifacts; early B-line pattern |
| **4–6** | A single, well-defined **rounded hypoechoic/anechoic structure** emerges just below the pleural line; vertical artifacts less prominent; structure has sharp borders suggesting vascular origin |
| **7–8** | **Two adjacent rounded hypoechoic structures** now visible — classic "double-barrel" appearance consistent with intercostal or subpleural vessels in cross-section |
| **9–10** | Structures persist; surrounding parenchyma shows heterogeneous echogenicity; no clear hepatization; no shred sign; no air bronchograms |

---

## B-Lines Assessment

**Findings:**
- In frames 1–3, discrete **hyperechoic vertical artifacts** arise from the pleural line and extend toward the bottom of the screen
- They are **spaced apart** with visible dark lung parenchyma between them
- They do **not** coalesce into a confluent white sheet
- Pattern is consistent with **thickened interlobular septa**, not alveolar flooding

> ✅ **lung_rockets = true**
> 🔹 **Subtype: `septal`** — discrete, well-separated B-lines (≤3 per ICS), dark parenchyma preserved between them

---

## Consolidation Assessment

**Findings:**
- The rounded hypoechoic/anechoic structures (frames 4–10) are sharply defined, smoothly bordered, and **progressively appear as paired structures** — morphology consistent with **vascular structures** (intercostal vessels) imaged in transverse cross-section
- **No hepatization**: parenchyma does not take on liver-like echogenicity
- **No shred sign**: deep border is not irregular/shredded
- **No air bronchograms**: no punctate/linear hyperechoic foci within solid-appearing lung tissue

> ❌ **consolidation = false**
> 🔹 **consolidation_type = null**

---

## Summary Conclusion

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **true** |
| B-line subtype | **septal** |
| `consolidation` | **false** |
| `consolidation_type` | **null** |

**Clinical Interpretation:** The discrete septal B-lines in the anterior right zone suggest **mild interstitial thickening** (e.g., early interstitial edema, mild pulmonary congestion, or resolving interstitial process). The absence of consolidation and the vascular-appearing subpleural structures argue against pneumonia or atelectasis at this zone.
