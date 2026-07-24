# 0026_lung_pneumonia-b-lines

# Lung Ultrasound Analysis — LT H/T Zone 2 (Sequential Frames)

---

## Frame-by-Frame Observations

| Frames | Key Observations |
|--------|-----------------|
| 1–3 | Pleural line visible; **rounded anechoic–hypoechoic structure** seated at/just below the pleural line; deep field predominantly dark; no vertical artifacts extending to screen bottom |
| 4–6 | The rounded structure becomes progressively more echogenic; structure is well-circumscribed with a defined superficial border; no discrete laser-like vertical artifacts |
| 7–8 | Structure transitions to a **tissue-like, heterogeneous echogenicity**; clearly hepatized appearance; surrounding deep field remains dark |
| 9–10 | Echogenic rounded structure is prominent; **deep border appears irregular/shredded** (shred sign); some punctate internal echogenicity may represent early air bronchograms |

---

## B-Lines Assessment

**Observations:**
- No hyperechoic vertical artifacts arising from the pleural line and extending to the bottom of the screen are identified across any frame
- A-lines are absent (consistent with subpleural pathology occupying the near-field)
- The deep field posterior to the lesion is predominantly **anechoic/dark**, not a white-lung or B-line dominant pattern

> **lung_rockets = false**
> **subtype = null**

---

## Consolidation Assessment

**Observations:**
- A **rounded/oval subpleural structure** is consistently present across all frames at the pleural line
- In frames 1–3: early hypoechoic/anechoic appearance
- In frames 6–10: **tissue-like hepatization** — echogenicity resembles liver parenchyma
- **Deep border irregularity** is visible in frames 9–10, consistent with a **shred sign** at the transition between consolidated and aerated lung
- **Punctate hyperechoic foci** visible within the hepatized tissue in later frames, suggesting **air bronchograms**

> **consolidation = true**
> **consolidation_type = "hepatization"** *(with associated shred sign at deep margin and early air bronchograms)*

---

## Summary Conclusion

```
lung_rockets       = false
consolidation      = true
consolidation_type = "hepatization"
```

This pattern is consistent with a **subpleural alveolar consolidation** in the left anterior zone (Zone 2). The lesion evolves dynamically across frames (likely respiratory motion), showing the classical triad of hepatization, shred sign at the deep border, and early air bronchograms. This appearance is most consistent with **pneumonia, atelectasis, or a contusion** in this zone. No interstitial syndrome (B-lines) is present.
