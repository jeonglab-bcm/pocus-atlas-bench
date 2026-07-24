# 0010_lung_pulmonary-shunt-in-pneumonia

# Lung Ultrasound Analysis — Anterior Zone (Sequential Frames)

---

## 🔬 Frame-by-Frame Observations

### Frames 1–3 (Early sequence)
- Lung parenchyma is **markedly echogenic**, beginning to show a **liver-like (hepatized) texture**
- Color Doppler reveals **active vascular flow** (blue signals) within the parenchymal tissue — confirming tissue perfusion, not effusion
- Frame 2 shows a **prominent red vascular signal** (larger vessel within consolidated tissue)
- Some **vertical artifacts** arising from the pleural interface are visible but partially obscured by the Doppler box

### Frames 4–6
- Hepatization becomes **more pronounced**
- Doppler signals are **mixed red and blue**, indicating bidirectional vascular flow within consolidated lung
- Frame 6 shows a **large coalescing red vascular signal** in the deeper tissue — consistent with a pulmonary vessel within hepatized parenchyma
- No dominant A-line pattern; aeration artifacts are suppressed

### Frames 7–10 (Late sequence)
- **Hyperechoic linear and punctate foci** clearly emerge within the hepatized tissue
- These are arranged in branching/linear distributions — classic **air bronchogram morphology**
- Tissue echogenicity is **heterogeneous**, with alternating bright foci (air-filled bronchi) and echogenic soft tissue (alveolar consolidation)
- Color Doppler confirms **preserved vascularity** throughout the consolidated zone
- Deepest border of the consolidated area has a somewhat **irregular/shredded margin** (minor shred sign component)

---

## 🫁 B-Lines Assessment

| Feature | Finding |
|---|---|
| Vertical hyperechoic artifacts from pleural line | Present but partially merged/confluent |
| Extension to bottom of screen without fading | Yes, in several frames |
| Separated discrete lines visible | Partially, at margins of consolidation |
| Confluent "white lung" sheet | Yes, in areas of dense hepatization |

### ✅ `lung_rockets = true`
### Subtype: **`mixed`**
> Discrete B-lines are visible at the **peripheral margins** of the consolidation (septal pattern), while the central consolidated zone shows **confluent, coalescing vertical artifacts** merging into the hepatized tissue (ground-glass pattern). The two subtypes coexist across the frames.

---

## 🫁 Consolidation Assessment

| Sign | Present? | Details |
|---|---|---|
| **Hepatization** | ✅ Yes | Lung parenchyma is uniformly echogenic, liver-like in texture across all frames |
| **Air bronchograms** | ✅ Yes | Hyperechoic linear/punctate foci within hepatized lung, clearly seen in Frames 7–10 |
| **Shred sign** | ⚠️ Partial | Mildly irregular deep border in late frames |
| **Preserved vascularity (Doppler)** | ✅ Yes | Color Doppler confirms blood flow within the solid tissue — excludes effusion, confirms viable consolidation |

### ✅ `consolidation = true`
### Type: **`consolidation_type = "air_bronchogram"`**
> The predominant consolidation pattern is **hepatization with air bronchograms** — hyperechoic linear/punctate structures within solid, liver-like lung parenchyma. This is the hallmark of **alveolar consolidation** (e.g., pneumonia).

---

## 📋 Summary & Clinical Interpretation

```
lung_rockets       = true
b_line_subtype     = "mixed"
consolidation      = true
consolidation_type = "air_bronchogram"
```

> ### 🔴 Pattern: Alveolar Consolidation with Air Bronchograms
> The sequential frames consistently demonstrate **anterior lung consolidation** with:
> - **Hepatized (solid) lung parenchyma** replacing normal aeration
> - **Air bronchograms** (hyperechoic branching foci) within the consolidated zone — indicating the airways remain patent but alveoli are fluid/pus-filled
> - **Preserved vascular flow on Color Doppler** — distinguishing this from necrotic or avascular lesions
> - **Mixed B-line pattern** at consolidation margins
>
> This constellation is **highly characteristic of bacterial pneumonia** (lobar or segmental). The presence of dynamic air bronchograms (if confirmed on real-time viewing) would further increase specificity for infectious consolidation over atelectasis.
