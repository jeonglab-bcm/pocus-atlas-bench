# 0031_lung_pneumoniashred-sign

# Lung Ultrasound Sequential Frame Analysis — Right Lung (Anterior Zone)

---

## Frame-by-Frame Observations

| Frame | Near-Field (Pleural/Subpleural) | Mid-Field | Deep Border | Notable Features |
|---|---|---|---|---|
| 1 | Pleural line visible; subpleural tissue relatively homogeneous, low-gray | Dark, minimally artifact-rich | Indistinct | Minimal aeration artifacts; early consolidation pattern |
| 2 | Subpleural echogenicity increasing | Faint vertical artifacts emerging | Irregular | Early B-line-type artifacts developing |
| 3 | Brighter subpleural zone; tissue-like | Scattered hyperechoic foci | Irregular/shredded | Possible early air bronchograms; shred sign emerging |
| 4 | Hepatized tissue-like echogenicity near pleural line | Bright punctate foci within tissue | Shredded | Hepatization + air bronchograms + shred sign |
| 5 | Continued hepatization | Confluent bright foci | Irregular | Coalescing bright reflectors — consolidation dominant |
| 6 | Prominent hepatized parenchyma | Multiple bright hyperechoic spots | Irregular/shred | Air bronchograms clearly visible within consolidated tissue |
| 7 | Hepatization with echogenic nodular foci | Patchy bright areas | Deep shred sign | Mixed air bronchograms + hepatization |
| 8 | Heterogeneous hepatized tissue | Bright foci persisting | Shred sign present | Air bronchograms prominent |
| 9 | Continuation of hepatized pattern | Hyperechoic foci dispersed | Deep margin irregular | Air bronchograms + shred sign |
| 10 | Dense hepatized zone near surface | Large hyperechoic air-containing foci | Shredded border | Most prominent air bronchograms; clear hepatization |

---

## B-Lines Assessment

### Observations:
- **Frames 1–3**: A transition from a relatively dark subpleural zone toward the emergence of vertical hyperechoic streaks originating at the pleural line. These early artifacts are spaced and partially discrete.
- **Frames 4–7**: Vertical artifacts become increasingly confluent, merging into a bright "white lung" appearance in zones of consolidation. Distinction between true B-lines and artifacts generated at consolidation edges becomes challenging.
- **Frames 8–10**: The vertical artifact pattern is largely subsumed within the consolidation; residual B-line-like artifacts at lateral edges are confluent and coalescing.

### Conclusion:

> **lung_rockets = true**
> **Subtype: `mixed`**
> - Early frames display **septal-type** discrete, spaced vertical artifacts
> - Later frames show **ground_glass-type** confluent coalescing pattern, with bright sheets obscuring A-lines
> - The overall predominance shifts toward ground_glass as consolidation develops

---

## Consolidation Assessment

### Observations:

**1. Tissue-like Hepatization:**
- Visible from Frame 3 onward with increasing intensity
- The subpleural lung parenchyma loses aeration and assumes liver-like gray echogenicity
- Particularly prominent in Frames 6–10

**2. Air Bronchograms:**
- Multiple punctate and linear hyperechoic foci appear *within* the hepatized tissue
- Clearly visible from Frame 4, highly prominent in Frames 6–10
- Represent air-filled bronchi trapped within consolidated (airless) parenchyma

**3. Shred Sign:**
- The deep margin of consolidation is **irregular and shredded** — not smooth
- Consistent finding from Frames 3–10
- Represents the interface between consolidated and partially aerated lung

### Conclusion:

> **consolidation = true**
> **consolidation_type = `air_bronchogram`** *(predominant)*
> - With co-existing **hepatization** and **shred sign**
> - The air bronchogram pattern dominates the later frames and is the most diagnostically prominent feature

---

## Summary Interpretation

```
lung_rockets       = true
b_line_subtype     = "mixed"  (septal → ground_glass progression)

consolidation      = true
consolidation_type = "air_bronchogram"
                     (+ hepatization + shred sign)
```

### Clinical Correlation:
This pattern — **progressive consolidation with air bronchograms, hepatization, and shred sign** combined with **confluent B-lines** — is most consistent with:
- **Pneumonia** (community-acquired or hospital-acquired) as the primary diagnosis
- Alternatively, **atelectasis with secondary B-line pattern** if there is lobar/segmental collapse
- The air bronchograms (particularly if **dynamic/moving** on real-time review) favor **pneumonia** over atelectasis

> ⚠️ *Clinical integration with patient history, oxygenation status, and complementary zones is recommended for definitive diagnosis.*
