# 0120_lung_jr_blines

# Lung Ultrasound Sequential Frame Analysis

## Equipment & Settings
- **Probe**: SonoSite L25xp/13-6 (linear, high-frequency)
- **Preset**: Lung
- **Depth**: 4.9 cm | MI: 0.8 | TIS: 0.3

---

## Frame-by-Frame Analysis

| Frame | Pleural Line | Vertical Artifacts | Deep Field | A-lines |
|-------|-------------|-------------------|------------|---------|
| 1 | Visible, regular | Multiple hyperechoic verticals arising from pleural line | Diffuse brightness | Largely absent |
| 2 | Visible | Multiple coalescing verticals | Bright, homogeneous | Obliterated |
| 3 | Visible | Dense, confluent verticals | Intensely bright/white | Absent |
| 4 | Visible | Multiple verticals, some discrete | Moderately bright | Largely absent |
| 5 | Visible | Confluent vertical artifacts | Diffuse brightness | Absent |
| 6 | Visible | Dense hyperechoic verticals | Bright, no A-lines | Obliterated |
| 7 | Visible | Multiple coalescing B-lines | Diffuse white field | Absent |
| 8 | Visible | Multiple dense verticals | Bright, confluent | Obliterated |
| 9 | Visible | Several vertical artifacts | Moderately bright | Largely absent |
| 10 | Visible | Coalescing verticals | Diffuse brightness | Absent |

---

## B-Lines Assessment

### Observations
- **Pleural line**: Consistently identified across all frames; appears regular and continuous
- **Vertical artifacts**: Hyperechoic vertical streaks originating **from the pleural line**, extending **to the bottom of the screen** without fading
- **Count per intercostal space**: Consistently **≥3** in most frames; artifacts merge/coalesce in the majority of frames
- **A-line status**: A-lines (horizontal reverberation artifacts) are **largely obliterated** across the clip, replaced by diffuse subpleural brightness
- **Dynamic behavior**: The artifacts move with the pleural line (consistent with lung sliding), confirming true B-lines rather than Z-lines or E-lines

### Conclusion
> ✅ **lung_rockets = true**
> 🔵 **Subtype = ground_glass**

**Rationale**: The predominant pattern shows **confluent, coalescing B-lines** forming a near-uniform white sheet below the pleural line. The obliteration of A-lines and diffuse subpleural echogenicity across the majority of frames is consistent with alveolar flooding or severe diffuse interstitial disease (ground-glass pattern), rather than discrete spaced septal B-lines.

---

## Consolidation Assessment

### Observations
- **Hepatization**: No tissue-like, liver-echogenicity pattern identified; the subpleural bright field is artifact-driven (B-lines), not true parenchymal solidification
- **Shred sign**: No irregular, ragged deep border between aerated and non-aerated lung is identified
- **Air bronchograms**: No punctate or linear hyperechoic foci within a hepatized lung parenchyma are visible
- The bright subpleural field is **artifact-based** (vertical B-line artifacts), not echogenic tissue

### Conclusion
> ❌ **consolidation = false**
> **consolidation_type = null**

---

## Summary

| Parameter | Finding |
|-----------|---------|
| **lung_rockets** | ✅ `true` |
| **B-line subtype** | `ground_glass` |
| **consolidation** | ❌ `false` |
| **consolidation_type** | `null` |

### Clinical Interpretation
The pattern of **dense, confluent ground-glass B-lines** with obliteration of A-lines in an anterior lung zone is highly consistent with:
- **Cardiogenic pulmonary edema** (bilateral, gravity-dependent distribution expected)
- **Severe non-cardiogenic pulmonary edema / ARDS**
- **Diffuse alveolar damage or severe viral pneumonitis**

> ⚠️ *Clinical correlation with patient history, bilateral comparison, and integration with other imaging modalities is essential for definitive diagnosis.*
