# 0039_lung_hepatization-of-lung

# Lung Ultrasound Analysis: Sequential Frame Assessment

## Frame-by-Frame Analysis

**Frames 1-3:** The pleural line is clearly visible. Below it, there is a large area of homogeneous, tissue-like echotexture (hepatization). The lung parenchyma has lost its normal aerated appearance and resembles liver tissue. Some scattered hyperechoic foci are beginning to appear within this tissue.

**Frames 4-5:** The consolidation becomes more apparent with a clear tissue-density pattern. A darker anechoic stripe (likely a vessel) is visible within the consolidated tissue. The border between consolidated and aerated lung appears irregular in places (shred sign).

**Frames 6-7:** Bright punctate hyperechoic foci become more prominent within the hepatized lung tissue — these are **air bronchograms** (trapped air within bronchi surrounded by consolidated, non-aerated parenchyma).

**Frames 8-10:** Prominent bright **linear hyperechoic structures** are clearly visible within the consolidated tissue, representing dynamic or static air bronchograms. The consolidation extends deep into the field of view.

---

## B-lines Assessment

Some vertical bright artifacts are visible at the periphery/transition zones of the consolidation, consistent with confluent B-lines in a **ground_glass** pattern. The extensive consolidation largely replaces the normal air-tissue interface but B-lines are present at the aerated margins.

- **lung_rockets = true**
- **Subtype: ground_glass** (confluent pattern consistent with severe alveolar disease)

---

## Consolidation Assessment

The dominant finding is extensive **alveolar consolidation**:
- ✅ **Hepatization**: Tissue-like echogenicity replacing normal lung pattern
- ✅ **Air bronchograms**: Punctate and linear hyperechoic foci within hepatized tissue (most prominent in frames 6-10)
- ✅ **Shred sign**: Irregular deep border visible in some frames

- **consolidation = true**
- **consolidation_type = "air_bronchogram"** (predominant feature — bright linear/punctate foci clearly embedded within hepatized lung)

---

## Summary

| Finding | Result |
|---------|--------|
| B-lines | Present (ground_glass) |
| Consolidation | Present (air bronchogram) |

This pattern is consistent with **significant alveolar consolidation** (e.g., pneumonia, ARDS) with air bronchograms indicating non-aerated, fluid/cell-filled alveoli surrounding patent airways.
