# 0013_lung_lung-slide-mmode

# Lung Ultrasound Sequential Frame Analysis — Anterior Zone

---

## Frame-by-Frame Observations

### M-Mode (Upper Panel — All Frames)
| Feature | Finding |
|---|---|
| Chest wall zone | Flat, horizontal parallel lines (normal soft tissue) |
| Pleural interface | Bright horizontal reflector at ~2 cm depth |
| Subpleural zone | Granular/sandy texture below pleural line |
| Pattern | **Seashore sign** → lung sliding **present** |

---

### B-Mode (Lower Panel — Sequential Frames)

**Frames 1–3:**
- Pleural line well-defined, hyperechoic
- Below pleural line: sparse, discrete vertical hyperechoic artifacts visible
- Background parenchyma partially visible between artifacts → **septal pattern**

**Frames 4–6:**
- Increasing number of vertical bright artifacts arising from pleural line
- Artifacts begin to **coalesce** laterally
- A-lines partially obscured → transitioning toward confluent pattern

**Frames 7–10:**
- Multiple bright vertical artifacts extending to screen bottom without fading
- Several artifacts **merge**, creating white/bright sheets in focal areas
- Discrete B-lines still identifiable in adjacent regions
- No clear A-line dominance remaining

---

## B-Line Assessment

### Presence
> ✅ **B-lines present (`lung_rockets = true`)**

**Supporting features:**
- Hyperechoic vertical artifacts arising from pleural line
- Extend to the bottom of the screen without fading
- Move with confirmed lung sliding (seashore sign on M-mode)
- Present consistently across all frames

### Subtype Classification
> **`b_line_subtype = "mixed"`**

| Pattern | Frames | Description |
|---|---|---|
| **Septal** | 1–3 | Discrete, well-spaced B-lines with dark parenchyma between them |
| **Ground-glass** | 6–10 | Confluent, coalescing B-lines forming white sheets, obscuring A-lines |

The clip demonstrates a **temporal progression** from discrete to confluent B-lines, with both patterns co-existing across the sequence.

---

## Consolidation Assessment

> ❌ **No consolidation (`consolidation = false`)**

| Sign | Finding |
|---|---|
| Hepatization | Absent — no liver-like echogenicity of lung parenchyma |
| Shred sign | Absent — no irregular shredded deep border |
| Air bronchograms | Absent — no hyperechoic punctate/linear foci within solid-appearing lung |

The subpleural findings are attributable entirely to **B-line artifacts**, not tissue consolidation.

> **`consolidation_type = null`**

---

## Summary Conclusion

```
lung_rockets      = true
b_line_subtype    = "mixed"
consolidation     = false
consolidation_type = null
```

### Clinical Interpretation
The anterior zone demonstrates a **mixed B-line pattern** with progression from septal (discrete) to ground-glass (confluent) B-lines across the clip. This pattern is consistent with **interstitial syndrome** — possibly representing early-to-moderate pulmonary edema or diffuse interstitial lung disease. The mixed subtype suggests heterogeneous interstitial involvement. Lung sliding is preserved. No consolidation is identified.
