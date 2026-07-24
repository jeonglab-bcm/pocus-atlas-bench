# 0041_lung_2018-1-16-normal-lung-slide

# Lung Ultrasound Analysis — Anterior Zone (Sequential Frames)

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Deep Field (Left) | Deep Field (Right) | Notable Feature |
|-------|-------------|-------------------|-------------------|-----------------|
| 1 | Visible, regular | Hypoechoic/dark | Mildly echogenic | Baseline |
| 2 | Visible, regular | Hypoechoic | Moderate echogenicity | Echogenic area beginning |
| 3 | Visible | Hypoechoic | **Clearly hyperechoic tissue-like area** | Consolidation entering frame |
| 4 | Visible | Hypoechoic | **Prominent hepatized region** | Hepatization most visible |
| 5 | Visible | Hypoechoic | **Hepatized region, irregular deep border** | Possible shred sign |
| 6 | Visible | Relatively dark | Fading echogenicity | Respiratory movement |
| 7 | Visible | Dark/A-line pattern | Reduced echogenicity | Consolidation moving out |
| 8 | Visible | Hypoechoic | **Bright echogenic area returns** | Hepatization again |
| 9 | Visible | Hypoechoic | Moderately echogenic | Partial view |
| 10 | Visible | Hypoechoic | Moderate echogenicity | Returning to baseline |

---

## B-Lines Assessment

> **No classic B-lines identified**

**Observations:**
- No discrete, laser-like vertical hyperechoic artifacts arise from the pleural line and extend to the bottom of the screen
- The left/central deep field is predominantly **hypoechoic**, consistent with **A-line** pattern (normal aeration)
- The bright vertical-appearing signals on the right side of frames are not B-lines — they represent the **edge of consolidation** spilling into the scan plane

```
lung_rockets = false
subtype = null
```

---

## Consolidation Assessment

> **Consolidation present**

**Observations across frames:**

1. **Hepatization** — The echogenic region on the right side of multiple frames displays a **liver-like tissue texture**, with internal echogenicity resembling soft tissue rather than aerated lung
2. **Shred sign** — The **deep border** of the consolidation is **irregular and shredded** (most evident in frames 3–5, 8), representing the interface between consolidated and residually aerated lung
3. **Possible air bronchograms** — In frames 4–5, small punctate hyperechoic foci are visible within the hepatized area, raising concern for **air bronchograms**
4. **Respiratory dynamics** — The consolidation moves **in and out of frame** with respiration across the 10-frame clip, confirming it is within the lung parenchyma

```
consolidation = true
consolidation_type = "hepatization"
(with associated shred sign at deep border; possible air bronchograms)
```

---

## Summary and Interpretation

| Parameter | Finding |
|-----------|---------|
| **B-lines (lung rockets)** | ❌ Absent |
| **B-line subtype** | — |
| **Consolidation** | ✅ Present |
| **Consolidation type** | Hepatization (+ shred sign) |

**Clinical Correlation:**
This anterior zone LUS pattern — tissue-like hepatization with shredded deep border and absent B-lines in the adjacent aerated lung — is **highly consistent with lobar or segmental pneumonia** or other consolidative pathology. The shred sign indicates the consolidation is **non-complete** (partial aeration preserved at depth). Clinical context (fever, cough, WBC) should guide further workup.
