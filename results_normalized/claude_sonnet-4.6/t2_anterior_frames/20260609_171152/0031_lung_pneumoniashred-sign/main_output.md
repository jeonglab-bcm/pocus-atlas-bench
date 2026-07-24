# 0031_lung_pneumoniashred-sign

# Lung Ultrasound Analysis — Right Lung (Sequential Frames)

---

## Frame-by-Frame Observations

| Frames | Findings |
|--------|----------|
| **1–2** | Relatively homogeneous near-field; faint vertical echogenicity beginning to emerge from pleural line; A-line pattern partially visible |
| **3–5** | Increasing vertical hyperechoic artifacts arising from pleural line; some remain discrete and separated (septal pattern); no clear consolidation mass yet |
| **6–7** | Vertical artifacts become more confluent and coalescing ("white lung" zone); A-lines suppressed; upper-central field shows increasing echogenicity consistent with a dense pattern |
| **8–10** | **Distinct echogenic region** emerges in the near-to-mid field with **tissue-like (hepatized) echogenicity**; within this region, **punctate and linear hyperechoic foci** are visible — consistent with **air bronchograms**; shredded/irregular deep border visible in transition zone |

---

## B-Lines Assessment

### ✅ `lung_rockets = true`

**Observations:**
- Hyperechoic vertical artifacts arise from the pleural line in **multiple frames**
- In frames 1–5: artifacts are **discrete and separated** → **septal pattern**
- In frames 6–10: artifacts become **confluent and coalescing**, obliterating A-lines → **ground-glass pattern**
- Artifacts extend to the bottom of the screen without fading

### Subtype: **`mixed`**
> Septal B-lines dominate early frames; ground-glass (confluent) B-lines dominate later frames — indicating evolving interstitial-alveolar involvement

---

## Consolidation Assessment

### ✅ `consolidation = true`

**Observations:**
| Sign | Present? | Detail |
|------|----------|--------|
| **Hepatization** | ✅ Yes | Tissue-like echogenicity mimicking liver texture in upper field (frames 7–10) |
| **Air bronchograms** | ✅ Yes | Punctate/linear bright foci within hepatized parenchyma |
| **Shred sign** | ✅ Partial | Irregular deep border between consolidated and residually aerated lung |

### Type: **`consolidation_type = "air_bronchogram"`**
> Hepatized lung parenchyma with clearly identifiable hyperechoic punctate/linear inclusions (air-filled bronchi), most prominent in frames 7–10

---

## Summary Conclusion

```
lung_rockets     = true
b_line_subtype   = "mixed" (septal → ground_glass progression)
consolidation    = true
consolidation_type = "air_bronchogram"
```

**Clinical Correlation:**
This pattern — **progressive B-lines culminating in ground-glass morphology** combined with **subpleural consolidation with air bronchograms** — is highly consistent with **pneumonia** (viral or bacterial) or **atelectatic consolidation** with partial aeration. The mixed B-line pattern suggests both interstitial edema/thickening and alveolar involvement in adjacent zones.
