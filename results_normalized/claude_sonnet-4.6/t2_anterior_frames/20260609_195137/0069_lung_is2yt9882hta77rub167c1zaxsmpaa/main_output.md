# 0069_lung_is2yt9882hta77rub167c1zaxsmpaa

# Lung Ultrasound — Sequential Frame Analysis

---

## 🔬 Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| **1–2** | Pleural line identifiable; 1–2 discrete vertical hyperechoic artifacts arising from pleural line; partial A-line pattern visible; no dominant consolidation |
| **3–4** | Abrupt appearance of a **rounded subpleural hypoechoic/mixed-echogenicity mass** below pleural line; pleural line overlying it is disrupted/irregular |
| **5** | Consolidation persists; deep border is **jagged and irregular** (shred sign morphology); tissue echogenicity resembles liver parenchyma |
| **6–7** | Transition zone; posterior enhancement deep to lesion; residual vertical artifacts at lesion margins; partial return of pleural line in adjacent zones |
| **8–9** | Consolidation re-centered; **tissue-like hepatization** clearly seen; deep border remains shredded; possible internal punctate echogenicities (air bronchograms) |
| **10** | Consolidation with irregular shredded deep margin; heterogeneous internal texture; no clean A-line pattern in this zone |

---

## 🫁 B-Lines Assessment

### Observations
- In frames **1–2** and **6–7** (areas adjacent to consolidation), **discrete, well-spaced vertical artifacts** arise from the pleural line and extend toward the deep field
- These artifacts are **separated by dark parenchyma**, not confluent
- No sheet-like whiteout or obliteration of A-lines indicative of ground-glass pattern
- B-line activity near consolidation margins may be partially contributed by the **shred sign interface**

### Conclusion
| Parameter | Finding |
|-----------|---------|
| `lung_rockets` | **true** |
| `subtype` | **septal** — discrete, spaced B-lines; dark inter-B-line intervals preserved |

---

## 🩻 Consolidation Assessment

### Observations
- **Hepatization**: The subpleural lesion displays **liver-like echogenicity**, loss of normal aeration artifacts, and solid tissue texture — classic hepatization
- **Shred sign**: The **deep border is markedly irregular and jagged**, creating a shredded interface between consolidated and adjacent aerated lung (most visible in frames 3–5, 8–10)
- **Air bronchograms**: Subtle **punctate hyperechoic foci** are detectable within the consolidated tissue in frames 8–9, suggesting retained air in bronchi within consolidation

### Conclusion
| Parameter | Finding |
|-----------|---------|
| `consolidation` | **true** |
| `consolidation_type` | **shred_sign** (dominant feature) with co-existing hepatization and probable air bronchograms |

---

## 📋 Summary & Clinical Interpretation

```
lung_rockets       = true
  └─ subtype       = "septal"

consolidation      = true
  └─ type          = "shred_sign" (+ hepatization + air bronchograms)
```

> ⚠️ **Clinical Correlation**: The combination of a **subpleural consolidation with hepatization, shred sign, and air bronchograms**, surrounded by **septal B-lines**, is highly characteristic of **bacterial pneumonia** with peripheral alveolar consolidation. The shred sign specifically indicates the consolidation-aeration interface typical of infectious (non-compressive) consolidation. Clinical and laboratory correlation is recommended.
