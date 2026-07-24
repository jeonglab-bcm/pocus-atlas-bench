# 0003_lung_lung-point-finding

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frames | Pleural Line | Deep Field | Artifacts |
|--------|-------------|------------|-----------|
| 1–3 | Smooth, well-defined | Relatively anechoic | Dominant **horizontal A-lines** |
| 4–7 | Intact, sliding apparent | Gradually brightening zones | **Discrete vertical artifacts** arising from pleural line, well-separated, extending to screen bottom |
| 8–10 | Intact but partially obscured locally | **Echogenic mass-like region** in deep field | Vertical artifacts persist; bright **punctate/linear foci** embedded within echogenic parenchyma |

---

## B-Line Assessment

### ✅ `lung_rockets = true`

**Subtype: `septal`**

> In frames 4–7 (and persisting into 8–10), **discrete, well-spaced hyperechoic vertical artifacts** arise perpendicularly from the pleural line and fan out to the screen's bottom edge without fading. Dark lung parenchyma is visible *between* them. They are clearly separated (≤3 per ICS), never coalescing into a white sheet — ruling out ground_glass. No mixed pattern is identified.

---

## Consolidation Assessment

### ✅ `consolidation = true`

**Type: `air_bronchogram`**

> In frames **8–10**, the deep field demonstrates:
> - **Tissue-like hepatization**: Lung parenchyma acquires liver-like echogenicity — loss of normal aerated appearance
> - **Punctate/linear hyperechoic foci** embedded within the hepatized tissue, consistent with **air bronchograms** (air-filled bronchi trapped within consolidated lung)
> - A somewhat **irregular deep border** (early shred sign) between consolidated and aerated lung

---

## Summary & Interpretation

```
lung_rockets       = true
b_line_subtype     = "septal"
consolidation      = true
consolidation_type = "air_bronchogram"
```

### Clinical Correlation
The combination of **septal B-lines + anterior air bronchogram consolidation** in sequential frames is highly suggestive of **lobar/segmental pneumonia** (bacterial pneumonia pattern), where interstitial edema produces B-lines peripherally while the affected parenchyma undergoes hepatization with retained air bronchi. Less likely: atelectasis (usually no B-lines, more dependent location).
