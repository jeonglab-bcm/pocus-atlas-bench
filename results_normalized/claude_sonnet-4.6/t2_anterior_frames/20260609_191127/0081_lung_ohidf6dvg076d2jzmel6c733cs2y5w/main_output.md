# 0081_lung_ohidf6dvg076d2jzmel6c733cs2y5w

# Lung Ultrasound — Sequential Frame Analysis

---

## Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| **1** (Gen, no THI) | Baseline: multiple hyperechoic vertical artifacts from pleural line; no A-lines visible; no needle artifact yet |
| **2–3** (THI on) | THI improves contrast resolution; **biopsy needle** appears as a bright linear artifact (upper-right quadrant); B-lines become more conspicuous; deeper parenchyma shows increased echogenicity |
| **4–6** | Needle advancing deeper; B-lines remain confluent/coalescing; mid-field parenchymal echogenicity increases, developing a **tissue-like (hepatized)** appearance; deep border becomes irregular |
| **7–10** | Needle tip within the target lesion; hepatized zone stabilizes; **irregular shredded deep border** clearly demarcated; punctate/linear hyperechoic foci within the consolidated area consistent with **air bronchograms** |

---

## B-Lines Assessment

### Observations
- **Multiple hyperechoic vertical artifacts** arise from the pleural line in every frame
- They extend to the **bottom of the screen without fading**
- The lines **coalesce and merge** — interline dark zones are nearly absent
- A-lines are completely **obliterated** by the confluent white curtain
- The lung surface appears **uniformly bright**

### Conclusion

| Parameter | Finding |
|-----------|---------|
| `lung_rockets` | **true** |
| Subtype | **`ground_glass`** — confluent, coalescing B-lines forming a diffuse white sheet; consistent with alveolar edema or diffuse interstitial disease |

---

## Consolidation Assessment

### Observations
- **Mid-to-deep field**: hepatized (liver-like echogenicity) solid-appearing parenchyma
- **Deep border**: markedly irregular, fragmented — classic **shred sign** at the interface between consolidated and residually aerated lung
- **Within the hepatized zone**: punctate/linear hyperechoic foci consistent with **air bronchograms** (distinct from needle artifact by their smaller caliber and static position)
- The **biopsy needle** is directed precisely into this consolidated target, confirming sonographic lesion localization

### Conclusion

| Parameter | Finding |
|-----------|---------|
| `consolidation` | **true** |
| `consolidation_type` | **`air_bronchogram`** — predominant feature is punctate/linear hyperechoic foci within hepatized lung; shred sign present at deep border |

---

## Integrated Summary

```
lung_rockets      = true
  └─ subtype      = "ground_glass"

consolidation     = true
  └─ type         = "air_bronchogram"
                    (+ hepatization + shred sign at deep margin)
```

> **Clinical correlation**: The coexistence of confluent B-lines (ground-glass pattern) with underlying subpleural consolidation bearing air bronchograms and a shred sign is characteristic of **pneumonia or atelectasis with surrounding interstitial edema**. The sequential frames document an **ultrasound-guided biopsy** of the consolidated lesion under real-time visualization.
