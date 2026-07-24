# 0059_lung_air-bronchograms

# Lung Ultrasound Analysis — Right Zone 4 (Sequential Frames)

## Technical Context
- **Probe**: C60xp curvilinear (5–2 MHz), abdominal preset
- **Depth**: 14.3 cm | **THI mode active**
- **Location**: Right anterior zone 4

---

## Frame-by-Frame Observations

### Frames 1–3 (Early sweep)
| Feature | Observation |
|--------|-------------|
| Pleural line | Visible but irregular/disrupted |
| Sub-pleural area | Heterogeneous echogenicity begins to emerge |
| Deep field | Patchy echogenic tissue appearing in lower-mid field |
| Artifacts | Faint vertical streaks arising from disrupted pleural line |

### Frames 4–7 (Mid sweep)
| Feature | Observation |
|--------|-------------|
| Lung parenchyma | **Increasingly hepatized** — liver-like echogenicity replacing air-filled lung |
| Bright foci | **Punctate and cluster-like hyperechoic foci** visible within echogenic mass → consistent with **air bronchograms** |
| Deep border | **Irregular, shredded margin** between consolidated and residually aerated lung |
| Vertical artifacts | **Confluent bright vertical streaks** arising from the pleural-consolidation interface |

### Frames 8–10 (Late sweep)
| Feature | Observation |
|--------|-------------|
| Consolidation | Fully established hepatized zone, persistent across frames |
| Air bronchograms | **Prominent** — both punctate (static) and elongated (dynamic) hyperechoic foci |
| Shred sign | Clearly visible at the deep irregular border |
| B-line differentiation | Vertical artifacts coalesce with consolidation boundary — ground-glass-type pattern adjacent to consolidation |

---

## B-Lines Assessment

### Observations
- Discrete A-lines are **absent** — replaced by vertical artifacts
- **Confluent vertical hyperechoic artifacts** arise from the pleural-consolidation interface, extending deep without fading
- In some frames, focal areas adjacent to consolidation show **merging white streaks** consistent with ground-glass B-lines
- No clearly spaced, discrete septal B-lines are individually identifiable

### Conclusion

```
lung_rockets     = true
b_line_subtype   = "ground_glass"
```
> Confluent B-lines dominate, likely representing alveolar flooding/inflammatory exudate at the margins of the consolidated zone

---

## Consolidation Assessment

### Observations
| Sign | Present | Description |
|------|---------|-------------|
| **Hepatization** | ✅ | Lung parenchyma exhibits liver-like echogenicity, loss of normal aeration artifacts |
| **Air bronchograms** | ✅ | Multiple punctate and linear hyperechoic foci scattered within hepatized lung, most prominent in frames 5–9 |
| **Shred sign** | ✅ | Irregular, non-geometric deep border between consolidated and partially aerated lung visible in frames 4–8 |

### Conclusion

```
consolidation         = true
consolidation_type    = "air_bronchogram"
```
> Predominant feature is **air bronchograms within hepatized lung**, superimposed on a shred sign at the deep border

---

## Integrated Interpretation

```json
{
  "lung_rockets": true,
  "b_line_subtype": "ground_glass",
  "consolidation": true,
  "consolidation_type": "air_bronchogram"
}
```

### Clinical Correlation
The combination of:
1. **Hepatization** (tissue-like echo texture)
2. **Air bronchograms** (retained air in bronchi within airless alveoli)
3. **Shred sign** (aeration gradient at consolidation border)
4. **Ground-glass B-lines** at the periphery

...in a **right anterior zone** is **highly consistent with bacterial pneumonia** (lobar or segmental). The presence of **air bronchograms** within consolidation is a key distinguishing feature from atelectasis (where air bronchograms tend to be dynamic/absent) and is supportive of an **infectious/inflammatory consolidation**.

> ⚠️ *Clinical correlation with symptoms, vitals, and laboratory data is essential for definitive diagnosis.*
