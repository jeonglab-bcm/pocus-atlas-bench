# 0019_lung_no-lung-sliding

# Lung Ultrasound — Sequential Frame Analysis

## Probe & Technical Parameters
- **Probe:** L14-6Ns (linear, high-frequency)
- **Protocol:** EM FAST | **Depth:** ~3.5 cm
- **Zone:** Anterior lung

---

## Frame-by-Frame Observations

| Frame | Pleural Line | Sub-pleural Zone | Notable Feature |
|-------|-------------|-----------------|-----------------|
| 1 | Bright, smooth | Predominantly anechoic/dark inferior field | Rib + acoustic shadow (left); faint A-lines |
| 2 | Visible | Large hypoechoic-to-anechoic inferior region begins | Pattern evolving |
| 3 | Visible | Dark inferior region persists; subtle internal echo texture | Possible early hepatization |
| 4 | Visible | Echogenic tissue-like area begins emerging centrally | Consolidation encroaching |
| 5 | Visible | Mixed dark/echogenic zone; irregular deep border appears | Shred sign feature |
| 6 | Visible | Echogenic area consolidates; liver-like texture | Hepatization pattern |
| 7 | Visible | Large echogenic mass below pleural line | Prominent hepatization |
| 8 | Visible | Echogenic area with internal granular texture | Possible air bronchograms |
| 9 | Visible | Broad hepatized zone; irregular posterior margin | Shred sign at deep border |
| 10 | Visible | Maximal hepatization visible; deep border shredded | Consolidation confirmed |

---

## B-Lines Assessment

### Observations:
- **No hyperechoic vertical laser-like artifacts** arise from the pleural line and extend to the bottom of the screen
- In the non-consolidated regions (particularly the superior pleural interface), **horizontal A-lines** (reverberation artifacts parallel to the pleural line) are the dominant subpleural pattern
- The vertical echoes seen in later frames are **not independent B-lines**; they represent the echogenic texture of the hepatized parenchyma itself

### Conclusion:
> **lung_rockets = `false`**
> **subtype = `null`**

---

## Consolidation Assessment

### Observations:

**Hepatization:**
- Beginning in frames 3–4 and fully developed by frames 7–10, the subpleural lung parenchyma develops a **solid, tissue-like echogenicity** resembling hepatic tissue
- Loss of normal aeration artifacts below the pleural line in the affected region

**Shred Sign:**
- The **deep border** of the consolidation is distinctly **irregular and shredded**, especially in frames 9–10
- This irregular interface between hepatized lung and residual aerated parenchyma is the classic shred sign

**Air Bronchograms:**
- In frames 8–9, subtle **punctate/linear hyperechoic foci** are visible within the consolidated tissue, suggesting entrapped air bronchi
- These are not dynamic (static air bronchograms), consistent with obstructive atelectasis or early pneumonia

### Conclusion:
> **consolidation = `true`**
> **consolidation_type = `"hepatization"`** *(with co-existing shred sign and static air bronchograms)*

---

## Summary

```
{
  "lung_rockets": false,
  "lung_rocket_subtype": null,
  "consolidation": true,
  "consolidation_type": "hepatization",
  "additional_features": ["shred_sign", "static_air_bronchograms"]
}
```

**Clinical Correlation:** The anterior zone demonstrates lobar/segmental consolidation with hepatization, a shredded deep border, and static air bronchograms — most consistent with **pneumonia or obstructive atelectasis**. The absence of B-lines argues against cardiogenic pulmonary edema as the primary etiology. Correlation with the remaining FAST views and clinical context is recommended.
