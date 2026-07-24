# 0013_lung_lung-slide-mmode

# Lung Ultrasound Analysis — Sequential Frame Review

## Frame-by-Frame Observations

### M-Mode (Upper Panel)
Across all 10 frames, the M-mode consistently demonstrates:
- **Superficial horizontal lines** (chest wall layers — static)
- **Granular/heterogeneous pattern** below the pleural interface (~2–2.5 cm depth)
- This constitutes a classic **"seashore sign"** → confirming **lung sliding is present**

---

### B-Mode (Lower Panel) — Frame-by-Frame

| Frames | Observations |
|--------|-------------|
| 1–2 | Pleural line clearly defined; subtle vertical hyperechoic artifacts arising from it; sparse dark lung parenchyma between artifacts |
| 3–5 | 2–3 discrete vertical bright artifacts extending from pleural line to screen bottom; dark lung tissue visible between them |
| 6–8 | Discrete B-lines persist; spacing maintained; no coalescence into white sheet; A-lines not dominant |
| 9–10 | Continued discrete vertical artifacts; preserved inter-B-line lung darkness; no hepatization pattern |

---

## B-Lines Assessment

### ✅ lung_rockets = **true**

**Observable features supporting B-lines:**
- Hyperechoic vertical artifacts **arising from the pleural line**
- Artifacts **extend to the bottom of the screen without fading**
- Present **across all frames**, moving synchronously with lung sliding
- **≤3 per intercostal space** in all frames
- **Dark lung parenchyma remains visible between individual B-lines** (no coalescence)
- A-lines are **not dominant** but the lung surface is not uniformly white

### Subtype: **Septal**
> Discrete, well-separated B-lines with preserved inter-B-line echolucency, consistent with **thickened interlobular septa** (e.g., interstitial pulmonary edema or interstitial lung disease)

---

## Consolidation Assessment

### ❌ consolidation = **false**

**No consolidation features identified:**
- ❌ No tissue-like hepatization (liver-like echogenicity of lung parenchyma)
- ❌ No shred sign (irregular deep border between consolidated/aerated lung)
- ❌ No air bronchograms (punctate/linear hyperechoic foci within solid-appearing lung)
- The lung parenchyma maintains **normal sub-pleural aeration pattern**

### consolidation_type = **null**

---

## Summary Conclusion

```
lung_rockets     = true
b_line_subtype   = "septal"
consolidation    = false
consolidation_type = null
```

**Clinical Correlation:** The finding of **discrete septal B-lines** in the anterior zone with **preserved lung sliding** and **no consolidation** is consistent with **mild-to-moderate interstitial syndrome** (e.g., early/mild pulmonary edema, interstitial lung disease). Correlation with clinical context, bilateral distribution, and the total B-line score (LUS score) is recommended.
