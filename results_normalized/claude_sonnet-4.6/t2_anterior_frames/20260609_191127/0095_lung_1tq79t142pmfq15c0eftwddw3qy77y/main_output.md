# 0095_lung_1tq79t142pmfq15c0eftwddw3qy77y

# Lung Ultrasound — Sequential Frame Analysis

---

## 🔬 Frame-by-Frame Observations

| Frames | Key Findings |
|--------|-------------|
| **1–3** | Pleural line visible; multiple vertical hyperechoic artifacts arising from pleural surface, extending to screen bottom; early signs of increased echogenicity in near field |
| **4–6** | B-lines become more numerous and begin to **coalesce/merge**; loss of distinct A-line pattern; lung surface appears progressively brighter |
| **7–8** | Parenchymal echogenicity increases; **tissue-like (hepatized)** appearance emerges; scattered bright punctate foci visible within the echogenic tissue |
| **9–10** | Clear **hepatization** of lung parenchyma visible; **multiple hyperechoic punctate and linear foci** distributed within consolidated tissue — consistent with **air bronchograms** |

---

## 📊 B-Lines Assessment

**`lung_rockets = TRUE`**

### Observations:
- Hyperechoic vertical artifacts clearly arise from the pleural line in frames 1–6
- In early frames: discrete, countable B-lines (septal-type)
- In mid-to-late frames: B-lines **merge and coalesce**, creating diffuse white sheets obscuring A-lines
- Both patterns co-exist across the clip

**B-line Subtype: `mixed`**
> Discrete septal B-lines in early frames → confluent ground-glass pattern in later frames

---

## 📊 Consolidation Assessment

**`consolidation = TRUE`**

### Observations:
- Frames 7–10 demonstrate **hepatization**: lung parenchyma takes on liver-like echogenicity, losing aeration artifacts
- Within the hepatized zone: **punctate and linear hyperechoic foci** are distributed throughout — classic **air bronchograms**
- No clean shred sign identified at the deep border (obscured by air bronchograms)

**`consolidation_type = "air_bronchogram"`**
> Predominant consolidation pattern is hepatized lung containing multiple air bronchograms

---

## ✅ Final Conclusions

```
lung_rockets        = true
b_line_subtype      = mixed (septal → ground_glass progression)
consolidation       = true
consolidation_type  = air_bronchogram
```

### 🩺 Clinical Interpretation:
This pattern — **consolidation with air bronchograms + perilesional confluent B-lines** — is highly characteristic of **bacterial pneumonia** or **atelectasis with retained secretions**. The presence of air bronchograms within hepatized tissue in the **anterior zone** supports a **lobar/segmental consolidation**. The surrounding B-line progression (septal → ground-glass) indicates **associated perilesional interstitial edema or inflammatory infiltrate**.
