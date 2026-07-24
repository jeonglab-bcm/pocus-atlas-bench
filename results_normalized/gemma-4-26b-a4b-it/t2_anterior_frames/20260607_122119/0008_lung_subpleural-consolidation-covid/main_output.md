# 0008_lung_subpleural-consolidation-covid

The video clip shows a lung ultrasound of an anterior lung zone. 

**B-lines Assessment:**
There are no discrete B-lines (lung rockets) visible. There is a large, hyperechoic area in the lower part of the image, but it does not originate from the pleural line and does not exhibit the characteristic vertical, non-fading, narrow, moving artifact pattern of B-lines. Instead, there is a significant anechoic (dark) area immediately below the pleural line, which is characteristic of a large pleural effusion. Therefore, **lung_rockets = false**.

**Consolidation Assessment:**
Beneath the large anechoic area (likely a pleural effusion), there is a large, bright, and textured region. This area exhibits a tissue-like, echogenic appearance that resembles liver parenchyma, which is a classic sign of **hepatization**. Furthermore, the border between this consolidated lung tissue and the underlying anechoic area is irregular and ragged, exhibiting a **shred sign**. Because the most prominent feature of this region is its solid, liver-like texture, the predominant type is hepatization. Therefore, **consolidation = true** and **consolidation_type = "hepatization"**.

**Conclusion:**
- **B-lines**: Absent
- **Consolidation**: Present (predominantly hepatization with a shred sign)
