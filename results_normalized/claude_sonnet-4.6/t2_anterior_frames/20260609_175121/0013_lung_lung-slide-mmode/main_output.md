# 0013_lung_lung-slide-mmode

# Lung Ultrasound Analysis — Sequential Frame Assessment

---

## Frame-by-Frame Observations

### B-Mode (Lower Panel — All Frames)

| Feature | Observation |
|---|---|
| Chest wall | Normal layered appearance (skin → subcutaneous fat → intercostal muscles) |
| Pleural line | Identifiable, bright, horizontal at ~1.5–2 cm depth |
| Sub-pleural artifacts | **Multiple vertical hyperechoic streaks** arise from the pleural line and extend toward the bottom of the image without fading |
| Between artifacts | Dark/hypoechoic lung parenchyma is visible **between** the vertical lines in most frames |
| Artifact spacing | Discrete, relatively well-separated; approximately **2–4 per intercostal space** |

### M-Mode (Upper Panel — All Frames)

| Feature | Observation |
|---|---|
| Above pleural line | Horizontal stratified lines → **"sea"** (chest wall, stationary) |
| Below pleural line | **Granular/sandy texture** → consistent with **seashore sign** |
| Implication | Lung sliding **present** across frames |

---

## Sequential Progression

- **Frames 1–3:** 2–3 discrete vertical artifacts visible; dark lung between them
- **Frames 4–6:** Slight brightening of pleural zone; artifacts remain individually distinguishable
- **Frames 7–10:** Consistent discrete vertical artifact pattern persists; no new coalescence or hepatization

---

## B-Lines Assessment

> **lung_rockets = true**

### Supporting Findings:
- ✅ Hyperechoic vertical artifacts arising **from** the pleural line
- ✅ Extend to **bottom of screen** without fading
- ✅ Confirmed to move with **lung sliding** (seashore sign on M-mode)
- ✅ Discrete, well-separated, with visible dark lung parenchyma between them

### Subtype Classification:

> **septal**

**Rationale:** B-lines are individually countable (≤3–4 per ICS), well-spaced, with preserved dark interstitial zones between each line. There is **no coalescence or white-out** pattern, ruling out ground-glass subtype.

---

## Consolidation Assessment

> **consolidation = false**

### Supporting Findings:
- ❌ No **hepatization** — no liver-like echogenic solid parenchyma
- ❌ No **shred sign** — no irregular deep lung border
- ❌ No **air bronchograms** — no hyperechoic punctate/linear foci within consolidated lung
- ✅ Lung parenchyma below pleural line retains expected acoustic behavior

> **consolidation_type = null**

---

## Summary & Clinical Interpretation

```
lung_rockets     = true
b_line_subtype   = "septal"
consolidation    = false
consolidation_type = null
lung_sliding     = present (seashore sign)
```

### Clinical Correlation:
The **septal B-line pattern with preserved lung sliding and no consolidation** in an anterior zone is consistent with:
- **Interstitial syndrome** (early/moderate)
- Differential includes: **cardiogenic pulmonary edema (early)**, interstitial pneumonia, pulmonary fibrosis
- The discrete, spaced nature of B-lines (rather than confluent) suggests **thickened interlobular septa** rather than alveolar flooding
