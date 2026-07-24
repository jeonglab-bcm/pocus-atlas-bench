# 0133_lung_jr_subpleuralconsolidation

# Lung Ultrasound Analysis — Right Lung Upper Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Key Findings |
|-------|-------------|
| **1** | Pleural line visible; below it, clustered **lobulated hyperechoic foci** within echogenic tissue — classic punctate air bronchogram pattern |
| **2** | Large **hypoechoic/dark zone** (right side) adjacent to echogenic parenchyma; scattered bright foci — hepatized tissue with shadow artifact |
| **3** | Multiple **clustered, lobulated bright nodular foci** scattered throughout; tissue-like background echogenicity |
| **4** | Most striking frame — dense **cluster of lobulated hyperechoic structures** in left field; strongly hepatized surrounding parenchyma |
| **5** | Large **acoustic shadow** (rib) on right; residual bright foci near pleural line on left — hepatization adjacent to rib |
| **6** | Similar to Frame 5; bright foci adjacent to pleural line; large anechoic shadow on right |
| **7** | Bright clustered foci below pleural line; large shadow on right; **no laser-like B-line morphology** |
| **8** | Scattered bright punctate foci; mild tissue-like echogenicity diffusely |
| **9** | Lobulated, rounded **hyperechoic clusters** similar to Frame 4 — highly consistent with air bronchograms |
| **10** | Dense, bright punctate foci in lower field; tissue-like parenchymal echogenicity throughout |

---

## B-Lines Assessment

### Observations:
- **No classic B-lines identified** across any frame
- Absent features of true B-lines:
  - ❌ No laser-like hyperechoic vertical artifacts arising from the pleural line
  - ❌ No artifacts extending continuously to the **bottom of the screen**
  - ❌ No movement synchronized with lung sliding
- The bright hyperechoic structures visible are **localized, clustered, and lobulated** — morphologically inconsistent with B-lines
- **No A-lines** are identifiable either, consistent with loss of normal aeration

### Conclusion:
```
lung_rockets = false
subtype = null
```

---

## Consolidation Assessment

### Observations:

**Hepatization:**
- The lung parenchyma loses its normal echogenic-with-artifact appearance
- Multiple frames (1, 3, 4, 7, 9, 10) demonstrate **solid, tissue-like echogenicity** reminiscent of liver texture
- The normal air-filled lung pattern is abolished

**Air Bronchograms:**
- Predominant finding across the majority of frames
- **Punctate hyperechoic foci** (static air bronchograms) scattered within the hepatized tissue
- **Lobulated/branching bright clusters** in Frames 1, 3, 4, 7, 9 — representing air retained within bronchi surrounded by fluid-filled alveoli
- Distribution is consistent with **segmental/lobar consolidation**

**Shred Sign:**
- In Frames 2 and 5/6, the **deep border** of the consolidation appears somewhat irregular, suggesting an interface between consolidated and partially aerated lung
- Shred sign features are present but **secondary** to the air bronchogram pattern

### Conclusion:
```
consolidation = true
consolidation_type = "air_bronchogram"
```

---

## Summary

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **false** |
| `B-line subtype` | null |
| `consolidation` | **true** |
| `consolidation_type` | **"air_bronchogram"** |

---

## Clinical Interpretation

> The sequential frames demonstrate **right upper lobe consolidation** with **prominent air bronchograms** (punctate and lobulated), set within **hepatized lung parenchyma**. This pattern is highly characteristic of **bacterial lobar pneumonia** (e.g., pneumococcal) or aspiration pneumonia. The absence of B-lines and the solid hepatized appearance indicate **complete loss of aeration** in the affected segment. Clinical correlation with fever, leukocytosis, and CXR/CT is recommended.
