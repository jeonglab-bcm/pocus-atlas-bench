# 0072_lung_m01vhapdm99ri51nm8bbpce5wev26y

# Lung Ultrasound Analysis — Miliary TB: Frame-by-Frame Assessment

---

## Frame-by-Frame Observations

### Frames 1–6 (Anatomically Labeled)

| Feature | Observation |
|---|---|
| Soft tissue | Normal superficial layer |
| Ribs | Hyperechoic with posterior acoustic shadowing |
| Pleural line | Present, **irregular/nodular contour**, thickened appearance |
| Subpleural zone | Small hypoechoic interruptions emerging at the pleura |
| Deep lung | Predominantly hypoechoic (dark), but subtle vertical artifacts begin to emerge |
| A-lines | **Not dominant** — largely replaced by vertical artifacts |

> Across these frames, the pleural line loses its smooth, regular linear appearance. Early vertical artifact generation is visible, increasing progressively frame-to-frame.

---

### Frames 7–10 (Annotated: Sub-pleural Nodules + B-lines)

| Feature | Observation |
|---|---|
| **Sub-pleural nodules** | Bilaterally visible — small hypoechoic focal lesions interrupting the pleural line, consistent with miliary granulomas |
| **B-lines** | 3 discrete hyperechoic vertical artifacts arising from the pleural line, extending to the screen bottom without fading |
| Inter-B-line spaces | Dark intervals visible between lines in some frames (septal component) |
| Coalescing zones | Lateral regions show increased pleural brightness suggestive of partial confluence (ground-glass component) |

---

## B-Lines Assessment

### ✅ `lung_rockets = TRUE`

**Subtype: `MIXED`**

| Component | Evidence |
|---|---|
| **Septal** | ≤3 discrete, well-separated B-lines per ICS visible in frames 7–10; dark lung parenchyma preserved between lines |
| **Ground-glass** | Peripleural zone shows areas of increased echogenicity with partial B-line coalescence, particularly laterally; A-lines fully abolished |

> **Pathophysiologic explanation (Miliary TB):** The mixed pattern reflects both thickened interlobular septa from subpleural granuloma deposition (septal B-lines) *and* partial alveolar involvement from miliary dissemination (ground-glass coalescence). Sub-pleural nodules themselves generate focal B-line artifacts.

---

## Consolidation Assessment

### ❌ `consolidation = FALSE`

| Sign | Status |
|---|---|
| Hepatization (liver-like echogenicity) | **Absent** — lung parenchyma remains predominantly hypoechoic |
| Shred sign | **Absent** — no deep irregular border between consolidated/aerated lung |
| Air bronchograms | **Absent** — no hyperechoic linear/punctate foci within hepatized tissue |

> **Note:** The sub-pleural nodules represent focal **subpleural micro-consolidations** characteristic of miliary disease, but they do **not** fulfill criteria for frank alveolar consolidation (no hepatization, no shred sign, no air bronchograms).

**`consolidation_type = null`**

---

## Summary

```
lung_rockets         = TRUE
b_line_subtype       = "mixed"  (septal + ground_glass)
consolidation        = FALSE
consolidation_type   = null
```

### Key Ultrasound Features of Miliary TB in This Clip:
1. **Sub-pleural nodules** — pathognomonic microlesions at pleural surface
2. **Mixed B-line pattern** — reflecting interstitial granulomatous disease + partial alveolar involvement
3. **Pleural line irregularity** — disrupted by subpleural granulomas
4. **Absence of frank consolidation** — distinguishes miliary from lobar TB
