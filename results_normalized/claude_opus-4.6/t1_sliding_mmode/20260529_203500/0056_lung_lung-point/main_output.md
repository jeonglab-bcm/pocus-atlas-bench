# 0056_lung_lung-point

# M-Mode Image Analysis

## Per-Position Classification

### p00 (left ~5%)
**Observation:** Bright horizontal lines confined to the upper ~15-20% of the image (chest wall). Below the pleural line, the image is dark with subtle granular/rippling texture, particularly visible at the bottom. No horizontal lines continue below.
**Classification: Seashore**

### p01 (~15%)
**Observation:** Similar to p00 — well-defined horizontal lines at top, below the pleural line is a dark region with subtle granular texture. Lines do not extend into the lower portion.
**Classification: Seashore**

### p02 (~28%)
**Observation:** Horizontal lines at top. Below the pleural line, clearly visible irregular, patchy bright structures — these are distinctly non-linear and granular in character.
**Classification: Seashore**

### p03 (~38%)
**Observation:** Prominent horizontal lines in the upper portion. Below the pleural line, bright irregular blob-like structures are clearly visible over a textured/sandy background. Not horizontal line organization.
**Classification: Seashore**

### p04 (~50%)
**Observation:** Dense horizontal lines occupy the upper ~45%. Below, some granular elements and irregular bright patches are still visible, though lines are beginning to encroach. Background between structures still appears granular.
**Classification: Seashore**

### p05 (~60%)
**Observation:** Horizontal lines occupy the upper ~55-60%. Below, some irregular bright areas remain visible, but the granular texture is diminishing. Still not fully continuous horizontal lines throughout.
**Classification: Seashore (borderline)**

### p06 (~70%)
**Observation:** Horizontal lines extend throughout the entire image — from top to bottom. The background texture between the lines is smooth/uniform with no granular component. Lines are continuous and uninterrupted.
**Classification: Stratosphere**

### p07 (~80%)
**Observation:** Dense, continuous parallel horizontal lines span the full vertical extent of the image. No granular texture visible anywhere. Background between lines is uniform gray. Classic barcode pattern.
**Classification: Stratosphere**

### p08 (~85%)
**Observation:** Bright horizontal lines confined to the upper ~35% with a prominent bright band. Below this boundary, the texture transitions to darker with subtle rippling/irregular texture. Horizontal lines do NOT continue clearly below.
**Classification: Seashore**

### p09 (~95%)
**Observation:** Very bright horizontal lines at top (~30%), clear bright boundary band, then dark area below with minimal structure. Lines clearly stop at the pleural line level — they do not continue below as in stratosphere.
**Classification: Seashore**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | **Stratosphere** |
| p07 | **Stratosphere** |
| p08 | Seashore |
| p09 | Seashore |

## Overall Decision

There is a clear **spatial transition**: positions p00–p05 and p08–p09 show seashore pattern (pleural sliding present), while positions p06–p07 show stratosphere/barcode pattern (pleural sliding absent). This coexistence of both patterns across different lateral positions indicates a **lung point**.

## **Overall Label: BOTH (Lung Point)**
