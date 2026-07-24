# 0064_lung_g5gayowofxkrfzewtw958o3is7kb8j

# Lung Ultrasound Sequential Frame Analysis

## Frame-by-Frame Observations

| Frame | Pleural Line | Subpleural Zone | Deep Field |
|-------|-------------|-----------------|------------|
| 1 | Visible, bright | Anechoic space dominates | Echogenic tissue mass, lower-center |
| 2 | Visible | Large anechoic area | Echogenic tissue, slightly shifted |
| 3 | Visible | Anechoic (effusion) | Echogenic tissue moves right |
| 4–6 | Visible | Persistent anechoic space | Echogenic tissue repositioning |
| 7–10 | Visible | Anechoic space stable | Echogenic tissue oscillates dynamically |

> **Key dynamic observation**: The echogenic deep tissue **shifts position across frames**, consistent with a **"swinging/floating lung"** sign — atelectatic/consolidated lung moving freely within a large pleural effusion.

---

## B-Lines Assessment

### Findings:
- No hyperechoic vertical artifacts arise from the pleural line and extend to the bottom of the screen
- The subpleural space is dominated by a **large anechoic collection** (pleural effusion), which acoustically replaces the normal reverberation environment
- No A-lines or B-lines are identifiable; the fluid medium prevents typical reverberation artifact generation

### Conclusion:
```
lung_rockets = false
subtype = null
```

---

## Consolidation Assessment

### Findings:

**1. Hepatization** ✅
- The echogenic mass at the deep field demonstrates **liver-like parenchymal echogenicity**
- Homogeneous, solid-tissue texture — loss of normal aeration artifacts

**2. Shred Sign** ✅ (partial)
- The deep border of the consolidation is **irregular and partially frayed**, especially visible in frames 3, 8–10
- Represents the interface between consolidated and residually aerated lung

**3. Air Bronchograms** ✅ (subtle)
- Within the hepatized region, **punctate hyperechoic foci** are intermittently visible across several frames
- Consistent with entrapped air within consolidated bronchi

**4. Dynamic "Floating Lung"**
- The consolidated lobe oscillates within the effusion — a hallmark of **compressive atelectasis** or large effusion-associated consolidation

### Conclusion:
```
consolidation = true
consolidation_type = "hepatization"
(with associated shred sign and subtle air bronchograms)
```

---

## Summary Interpretation

| Parameter | Result |
|-----------|--------|
| `lung_rockets` | **false** |
| `B-line subtype` | null |
| `consolidation` | **true** |
| `consolidation_type` | **hepatization** |

> **Clinical Interpretation**: This clip demonstrates a **large pleural effusion with compressive/passive atelectasis** of the underlying lung. The floating consolidated lung (hepatized parenchyma with subtle air bronchograms) moves dynamically with respiration/cardiac motion. No B-lines are identifiable due to the effusion replacing the normal pleural interface acoustics. This pattern is most consistent with **parapneumonic effusion, transudative effusion with compressive atelectasis, or malignant effusion** — clinical correlation required.
