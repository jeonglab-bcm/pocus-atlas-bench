# 0072_lung_m01vhapdm99ri51nm8bbpce5wev26y

# Lung Ultrasound Analysis — Miliary TB Sequential Frame Review

---

## 🔬 Frame-by-Frame Observations

### Frames 1–6 (Anatomically Labeled Frames)

| Frame | Pleural Line | Lung Field | Artifacts |
|-------|-------------|------------|-----------|
| 1 | Bright, thin, regular | Mostly anechoic | No vertical artifacts yet |
| 2 | Slightly irregular | Anechoic | Faint vertical artifact beginning |
| 3 | Mildly thickened/irregular | Slightly echogenic | Early vertical comet-tail artifacts emerging |
| 4 | Mildly thickened | Echogenic cone developing | Vertical artifacts more pronounced |
| 5 | Irregular, partially disrupted | Bright cone visible | Multiple vertical artifacts |
| 6 | Noticeably irregular | Vertical streak prominent | Discrete B-lines identifiable |

> **Progressive pattern**: From clean pleural line → increasing pleural irregularity → emergence of vertical artifacts over sequential frames.

---

### Frames 7–10 (Annotated Diagnostic Frames)

**Sub-pleural nodules (bilateral arrows):**
- Small hypoechoic/iso-echoic nodular irregularities **interrupting the pleural line** bilaterally
- Characteristic of miliary seeding along the visceral pleura
- Consistent with **sub-pleural miliary granulomas**

**B-lines (three arrows):**
- Clearly hyperechoic **vertical laser-like artifacts**
- Arise from the **pleural line**
- Extend **to the bottom of the screen without fading**
- Appear **discrete and separated** with dark parenchyma visible between them
- ≥3 B-lines visible per intercostal space
- Consistent movement with lung sliding implied by sequential frame consistency

---

## 📊 B-Lines Assessment

```
lung_rockets = TRUE
```

### Subtype Characterization

| Criterion | Observation |
|-----------|-------------|
| Spacing | Discrete, individually identifiable — not fully confluent |
| Intervening parenchyma | Dark lung tissue visible **between** B-lines |
| Coalescence | Partial — some tendency toward merging in frames 5–6 |
| A-line obliteration | Partially present |
| Number per ICS | ≥3, clustered |

**Subtype → `mixed`**

> **Rationale**: Predominantly **septal-type** discrete B-lines dominate (clear separation, dark lung between), but some frames (5–6) show partial coalescence consistent with early **ground-glass** features — a pattern expected in miliary TB where diffuse interstitial infiltration creates heterogeneous B-line distribution across zones and time points.

---

## 🫁 Consolidation Assessment

```
consolidation = FALSE
consolidation_type = null
```

### Findings Review

| Sign | Present? | Comment |
|------|----------|---------|
| Hepatization (liver-like echogenicity) | ❌ No | Lung parenchyma remains predominantly anechoic/dark |
| Shred sign | ❌ No | No irregular deep border between consolidated/aerated lung |
| Air bronchograms | ❌ No | No hyperechoic linear/punctate foci within hepatized tissue |

> ⚠️ **Important distinction**: The **sub-pleural nodules** noted in frames 7–10 represent small pleural/sub-pleural granulomas — these are **not equivalent to alveolar consolidation**. They are localized pleural surface lesions without the hepatization pattern required for consolidation classification.

---

## 🏁 Final Conclusions

```json
{
  "lung_rockets": true,
  "bline_subtype": "mixed",
  "consolidation": false,
  "consolidation_type": null
}
```

### Clinical Correlation

The combination of:
1. ✅ **Multiple discrete-to-coalescent B-lines** (mixed septal/ground-glass)
2. ✅ **Bilateral sub-pleural nodules**
3. ✅ **Pleural line irregularity**
4. ❌ **Absence of frank consolidation**

...is **highly characteristic of Miliary TB**, consistent with the header label. The diffuse hematogenous seeding creates interstitial thickening (B-lines) and small pleural granulomas without producing the lobar/segmental consolidation typical of bacterial pneumonia.
