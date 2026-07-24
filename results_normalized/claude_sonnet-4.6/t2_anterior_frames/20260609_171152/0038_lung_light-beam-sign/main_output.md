# 0038_lung_light-beam-sign

# Lung Ultrasound — Sequential Frame Analysis (Right Anterior Zone R3)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Deep Field | Vertical Artifacts | Horizontal Artifacts |
|-------|-------------|------------|-------------------|---------------------|
| 1 | Bright, smooth | Dark/anechoic | None identified | A-lines present |
| 2 | Bright, smooth | Dark/anechoic | None identified | A-lines present |
| 3 | Bright, smooth | Dark/anechoic | **1 discrete vertical artifact** visible, mid-field | A-lines present |
| 4 | Bright, smooth | Dark/anechoic | **1 discrete vertical artifact** persisting | A-lines present |
| 5 | Bright, smooth | Dark/anechoic | None clear | A-lines dominant |
| 6 | Bright, smooth | Dark/anechoic | Faint suggestion | A-lines dominant |
| 7 | Bright, smooth | Dark/anechoic | None clear | A-lines dominant |
| 8 | Bright, smooth | Dark/anechoic | None clear | A-lines dominant |
| 9 | Bright, slightly irregular | Dark/anechoic | **1–2 discrete vertical artifacts** descending | A-lines present |
| 10 | Bright, slightly irregular | Dark/anechoic | **1–2 discrete vertical artifacts** extending deep | A-lines present |

---

## B-Lines Assessment

### Observations:
- **Dominant pattern across all frames**: A-lines (horizontal reverberation artifacts parallel to and below the pleural line) — consistent with **normal aeration**
- **In frames 3, 4, 9, and 10**: 1–2 discrete, well-defined **hyperechoic vertical artifacts** are visible, originating at the pleural line and extending toward the deep field
- These vertical artifacts are **clearly separated** from one another (dark parenchyma visible between them)
- They appear to **move with lung sliding** across sequential frames
- **No confluent or coalescing white-sheet pattern** is observed; A-lines remain visible between artifacts

### Conclusion:
> **lung_rockets = true**
> **subtype = "septal"**
>
> Isolated, discrete B-lines (≤2 per intercostal space) intermittently visible in select frames, with preserved dark inter-B-line spacing. Consistent with minimal thickening of interlobular septa. The overall field is A-line dominant, indicating predominantly normal aeration with early or mild interstitial involvement.

---

## Consolidation Assessment

### Observations:
- **No hepatization**: Lung parenchyma deep to the pleural line remains **uniformly anechoic/dark** — no liver-like solid tissue echogenicity
- **No shred sign**: No irregular or fragmented deep border between consolidated and aerated lung
- **No air bronchograms**: No punctate or linear hyperechoic foci within a solidified parenchymal region
- The pleural line itself is intact and continuous across all frames

### Conclusion:
> **consolidation = false**
> **consolidation_type = null**

---

## Summary

| Parameter | Result |
|-----------|--------|
| **lung_rockets** | ✅ **true** |
| **B-line subtype** | **septal** |
| **consolidation** | ❌ **false** |
| **consolidation_type** | **null** |

**Overall interpretation**: This anterior zone shows a **predominantly A-line pattern** with **isolated septal B-lines** (1–2) intermittently apparent on respiratory phases. This pattern is consistent with **mild interstitial involvement** (e.g., early interstitial edema or thickened septa) without alveolar flooding or consolidation. Clinical correlation is recommended.
