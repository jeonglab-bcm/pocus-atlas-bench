# 0055_lung_xj3qs1t4t9d98j8nryo5pwy24gyy67

# Lung Ultrasound — Sequential Frame Analysis

## Frame-by-Frame Observations

### Frames 1–2 (Early Frames)
| Feature | Observation |
|---|---|
| Pleural line | Bright, well-defined horizontal line visible in mid-field |
| Sub-pleural pattern | Predominantly **dark/anechoic** parenchyma below pleural line |
| Artifacts | **Horizontal reverberation lines (A-lines)** visible — indicates normal aeration |
| Vertical artifacts | None extending to screen bottom |

---

### Frames 3–6 (Transitional Frames)
| Feature | Observation |
|---|---|
| Pleural line | Still identifiable; lung sliding detectable |
| Sub-pleural pattern | Progressive increase in echogenicity in deeper fields |
| Vertical artifacts | Brief bright reflections below pleural line, but **fading before screen bottom** → do NOT meet B-line criteria |
| A-lines | Still partially visible → not obliterated |

---

### Frames 7–10 (Later Frames)
| Feature | Observation |
|---|---|
| Pleural line | Less distinct; irregular interface at tissue–air boundary |
| Deep parenchyma | **Hepatization** — tissue-like, liver-echogenicity occupying lower half of image |
| Air bronchograms | **Punctate and linear hyperechoic foci** within hepatized tissue, consistent with air-filled bronchi |
| Shred sign | Irregular deep margin between consolidated and aerated lung visible in frames 9–10 |
| A-lines | Completely absent below consolidated tissue |

---

## B-Lines Assessment

**No classic B-lines identified** across any frame.

> Criteria not met:
> - No laser-like vertical hyperechoic artifacts arising from the pleural line and **reaching the bottom of the screen without fading**
> - Bright vertical-ish reflections in transitional frames fade early and are overshadowed by consolidation in later frames
> - Early frames dominated by **A-line** pattern

```
lung_rockets = false
b_line_subtype = null
```

---

## Consolidation Assessment

**Consolidation clearly present**, progressing across the sequence:

| Sign | Present? | Details |
|---|---|---|
| Hepatization | ✅ Yes | Liver-like echogenicity, frames 7–10 |
| Air bronchograms | ✅ Yes | Multiple punctate/linear hyperechoic foci within hepatized tissue |
| Shred sign | ✅ Partial | Irregular deep border frames 9–10 |

```
consolidation = true
consolidation_type = "air_bronchogram"
```

---

## Summary & Interpretation

```
lung_rockets       = false
consolidation      = true
consolidation_type = "air_bronchogram"
```

### Clinical Correlation
In a patient presenting with **chest pain**, this pattern is most consistent with:
- **Lobar/segmental pneumonia** — hepatized lung with air bronchograms in anterior zone
- Less likely: atelectasis (would lack air bronchograms in this pattern)
- PE workup note: consolidation with air bronchogram may also represent **pulmonary infarction** — clinical context, D-dimer, and further imaging (CTPA) warranted

> ⚠️ The **absence of B-lines** in non-consolidated zones and the presence of **anterior consolidation** are both significant findings warranting urgent clinical correlation.
