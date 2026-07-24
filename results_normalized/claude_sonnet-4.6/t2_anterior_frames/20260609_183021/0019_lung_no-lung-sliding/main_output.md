# 0019_lung_no-lung-sliding

# Lung Ultrasound Sequential Frame Analysis

## Technical Parameters
- **Probe**: L14-6Ns (Linear, high-frequency)
- **Depth**: 3.5 cm
- **Protocol**: EM FAST
- **Mode**: B-mode

---

## Frame-by-Frame Observations

### Frames 1–3 (Early)
| Feature | Observation |
|--------|-------------|
| Chest wall | Normal layered soft tissue |
| Pleural line | Bright, well-defined hyperechoic line |
| Left field | Rounded/rectangular hypoechoic structure (likely rib with acoustic shadowing) |
| Right-deep field | Early tissue-like echogenicity appearing below pleural line (~1.5–2 cm depth) |
| Vertical artifacts | Absent or nascent |

### Frames 4–6 (Mid)
| Feature | Observation |
|--------|-------------|
| Pleural line | Still clearly defined |
| Lower-right region | Increasingly solid, **hepatized** (liver-like echogenicity) region becoming more apparent |
| Superior border of echogenic region | Begins to demonstrate **irregular, shredded interface** with overlying aerated lung |
| Vertical artifacts | Subtle, not yet clearly formed discrete B-lines |

### Frames 7–10 (Late)
| Feature | Observation |
|--------|-------------|
| Pleural line | Present, identifiable |
| Left structure | Persistent hypoechoic rounded structure (rib shadow) |
| Consolidation | **Clearly consolidated region** in lower-right, with tissue-like (hepatized) echogenicity |
| Border | **Irregular shredded superficial border** between consolidated and partially aerated lung |
| Hyperechoic foci | **Punctate/linear bright foci** visible within consolidated tissue — consistent with **air bronchograms** |
| Vertical artifacts | 1–2 discrete hyperechoic vertical lines visible arising from pleural line in frames 8–10 |

---

## B-Line Assessment

### Presence
> **lung_rockets = TRUE**

### Evidence
- In frames 7–10, **discrete hyperechoic vertical artifacts** arise from the pleural line
- These are **separated by hypoechoic lung parenchyma** between them
- They do not fully fade within the field but are not confluent/coalescing

### Subtype
> **subtype = "septal"**

- Discrete, well-spaced vertical artifacts
- Dark parenchyma visible between them
- Not merging into a confluent white sheet
- ≤2–3 B-lines visible per intercostal space, each clearly separated

---

## Consolidation Assessment

### Presence
> **consolidation = TRUE**

### Evidence
| Sign | Present? | Details |
|------|----------|---------|
| **Tissue-like hepatization** | ✅ Yes | Lower-right lung parenchyma shows solid, liver-like echogenicity |
| **Shred sign** | ✅ Yes | Irregular, jagged superior border between consolidated and aerated lung |
| **Air bronchograms** | ✅ Yes | Punctate/linear hyperechoic foci within the consolidated region |

### Predominant Type
> **consolidation_type = "shred_sign"**

- The dominant feature is the **irregular shredded interface** between consolidated and aerated lung
- Hepatization is present in the body of the lesion
- Air bronchograms are present but secondary
- This configuration is most consistent with **peripheral/subpleural consolidation** (e.g., pneumonia, pulmonary contusion)

---

## Summary & Interpretation

```
lung_rockets      = true
b_line_subtype    = "septal"
consolidation     = true
consolidation_type = "shred_sign"
```

### Clinical Correlation
This EM FAST anterior lung zone demonstrates a **subpleural consolidation with shred sign, hepatization, and air bronchograms**, surrounded by discrete septal B-lines in adjacent lung. This pattern is most consistent with:

1. **Community-acquired pneumonia** (most likely — air bronchograms + shred sign + B-lines)
2. **Pulmonary contusion** (trauma context — given EM FAST setting)
3. Less likely: focal atelectasis without air bronchograms predominance

> ⚠️ **Clinical context and correlation with other FAST views is essential for definitive diagnosis.**
