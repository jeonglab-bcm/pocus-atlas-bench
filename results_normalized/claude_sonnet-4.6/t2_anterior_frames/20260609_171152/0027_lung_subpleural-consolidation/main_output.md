# 0027_lung_subpleural-consolidation

# Lung Ultrasound Analysis — RT H/T Zone 1 (Right Anterior Lung)

---

## Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| **1–2** | Pleural line identifiable; a single **rounded hypoechoic/anechoic structure** appears sub-pleurally; deeper field is relatively dark with faint heterogeneity; no discrete laser-like vertical artifacts from pleural line |
| **3–4** | Rounded anechoic structure becomes **well-circumscribed**, with apparent posterior acoustic enhancement; borders are relatively defined; surrounding parenchyma begins to show increased echogenicity |
| **5–6** | Structure shows **internal heterogeneous echogenicity**, suggesting it is not a simple fluid collection; surrounding tissue progressively more echogenic/solid-appearing (hepatization); irregular deep borders emerging |
| **7–8** | **Two distinct rounded hypoechoic foci** now visible side by side; surrounding and intervening tissue shows **liver-like (hepatized) echogenicity**; loss of normal A-line reverberation artifact |
| **9–10** | Consolidated zone consolidates further; **irregular shredded border** at the deep margin between consolidated and aerated lung; punctate/linear hyperechoic foci within the hepatized zone consistent with **air bronchograms** |

---

## B-Lines Assessment

### Observations:
- No classic **laser-like hyperechoic vertical artifacts** originating from the pleural line and extending uninterrupted to the bottom of the screen are identified in any frame
- The few vertical artifacts present appear **embedded within the consolidation** itself, not independently arising from the pleural interface
- **A-lines** (horizontal reverberation) are partially visible in frames 2–3 in areas away from the consolidation
- The dominant artifact pattern is **vertical shadowing from consolidated tissue**, not interstitial B-lines

### Conclusion:
> **lung_rockets = `false`**
> No B-lines meeting diagnostic criteria are present. The absence of B-lines, combined with the consolidative process, is consistent with alveolar rather than interstitial pathology.

---

## Consolidation Assessment

### Observations:

| Sign | Present? | Description |
|------|----------|-------------|
| **Hepatization** | ✅ Yes | Lung parenchyma loses normal aeration artifacts and becomes solid, with echogenicity resembling liver tissue (frames 5–10) |
| **Shred sign** | ✅ Yes | Irregular, shredded deep border between consolidated zone and residual aerated lung (frames 9–10) |
| **Air bronchograms** | ✅ Yes | Punctate and linear hyperechoic foci within the hepatized zone visible in frames 8–10, representing trapped air in bronchi |

### Conclusion:
> **consolidation = `true`**
> **consolidation_type = `"hepatization"`** (predominant), with co-existing **shred sign** and **air bronchograms**

---

## Summary Interpretation

```
lung_rockets      = false
consolidation     = true
consolidation_type = "hepatization"
```

The sequential frames demonstrate a **progressive focal consolidation** in the right anterior lung zone. The **hepatized, solid-appearing parenchyma** with an **irregular shred sign border** and **air bronchograms** is most consistent with:

- **Pneumonia** (community-acquired or aspiration) — most likely
- Alternatively: evolving atelectasis or pulmonary infarction

The **absence of B-lines** argues against a pure interstitial/cardiogenic pattern and supports an **alveolar consolidation** etiology. Clinical correlation (fever, leukocytosis, cough) is recommended.
