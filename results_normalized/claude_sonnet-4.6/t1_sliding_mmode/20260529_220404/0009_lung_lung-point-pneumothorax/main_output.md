# 0009_lung_lung-point-pneumothorax

# M-Mode Lung Ultrasound Analysis

## Step 1 — Per-Position Classification

### p00 (Image 1)
**Observed:** Upper ~40% is pure black. Lower portion has a few faint bright columns with minimal structural detail. Strong evidence of left-edge beam truncation.
**Classification: UNCLASSIFIABLE** — Edge artifact; insufficient active signal.

---

### p01 (Image 2)
**Observed:** Multiple distinct bright vertical columns (A-lines in depth-horizontal display) spanning the full image height. The inter-column spaces show a **grainy, sandy, non-organized texture** with no dense horizontal lines filling the gaps. The columns themselves have irregular, slightly wavy margins.
**Classification: SEASHORE** — A-lines present over a granular background; pleural motion implied by column irregularity.

---

### p02 (Image 3)
**Observed:** Similar vertical A-line columns; some faint horizontal banding beginning to appear but the **inter-column zones remain primarily granular and non-linear**. No dense continuous horizontal line fill below the pleural level.
**Classification: SEASHORE** — Granular background dominates between A-lines.

---

### p03 (Image 4)
**Observed:** A clear **cross-hatch grid** emerges — A-line columns intersecting with horizontal bands. However, the inter-section texture still retains visible **granular noise elements**; the horizontal bands are not yet uniformly dense. The cross-hatch appearance reflects A-lines superimposed on a still-active sandy zone.
**Classification: SEASHORE** — A-lines crossing a background with residual granularity.

---

### p04 (Image 5)
**Observed:** Dense cross-hatch continues, with both vertical A-line columns and horizontal bands very prominent. The image is complex, but on close inspection **granular texture is still discernible** in the cells of the grid. Borderline but still non-purely-linear.
**Classification: SEASHORE** (borderline) — Granular elements persist.

---

### p05 (Image 6)
**Observed:** The balance tips: **horizontal parallel bands now dominate** the image. Vertical columns are present but subdued. The spaces between horizontal lines are dark and clean rather than granular. The horizontal lines extend uniformly without sandy interruption.
**Classification: STRATOSPHERE** — Continuous horizontal lines, loss of granularity.

---

### p06 (Image 7)
**Observed:** Further increase in **horizontal line density**. Some vertical elements are still visible at left, but the overall pattern is clearly dominated by dense, regular horizontal parallel lines with no granular fill. No sandy background detectable.
**Classification: STRATOSPHERE** — Dense parallel horizontal lines throughout.

---

### p07 (Image 8)
**Observed:** Predominantly **horizontal bright and dark bands**, very regular and parallel. The left margin shows a small region of residual complexity (possibly the spatial transition still in view), but the majority is barcode-like. No granular zones.
**Classification: STRATOSPHERE** — Barcode/parallel line pattern dominant.

---

### p08 (Image 9)
**Observed:** Clear **parallel horizontal bands** with increasingly dark zones at lower depths (approaching right edge). The visible portions are cleanly horizontal and line-dominated, with no granularity.
**Classification: STRATOSPHERE** — Horizontal parallel lines; right-edge fade beginning.

---

### p09 (Image 10)
**Observed:** Lower half is predominantly **dark/black** (right-edge beam truncation). Upper portion shows a few horizontal lines, but the image lacks sufficient active signal throughout.
**Classification: UNCLASSIFIABLE** — Right-edge artifact; insufficient active signal.

---

## Summary Table

| Position | Pattern | Classification |
|----------|---------|----------------|
| p00 | Mostly black, edge artifact | **UNCLASSIFIABLE** |
| p01 | A-line columns + granular background | **SEASHORE** |
| p02 | A-line columns + granular background | **SEASHORE** |
| p03 | Cross-hatch with residual granularity | **SEASHORE** |
| p04 | Dense cross-hatch, still granular | **SEASHORE** |
| p05 | Horizontal lines dominant, no granularity | **STRATOSPHERE** |
| p06 | Dense horizontal parallel lines | **STRATOSPHERE** |
| p07 | Dense horizontal parallel lines | **STRATOSPHERE** |
| p08 | Horizontal lines, right-edge fade | **STRATOSPHERE** |
| p09 | Mostly black, edge artifact | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)

There is a **clear and consistent spatial transition**:
- **p01 → p04**: SEASHORE (pleural sliding **present**)
- **p05 → p08**: STRATOSPHERE (pleural sliding **absent**)

The lung point falls between positions p04 and p05.

> ## ✅ Overall Classification: **"BOTH"** — Lung Point Detected
>
> Pleural sliding is **present** at the left lateral positions (p01–p04) and **absent** at the right lateral positions (p05–p08). This spatial seashore-to-stratosphere transition defines a **lung point**, consistent with a **localized pneumothorax** limited to the right lateral scan region.
