# 0049_lung_pleural-shred-sign

# M-Mode Image Analysis

## Per-Position Classification

### p00 (leftmost, ~5%)
**Observation:** Nearly entirely black/dark with only very faint water-like texture visible. Minimal structure.
**Classification: UNCLASSIFIABLE** (edge of active region)

### p01 (~15%)
**Observation:** A bright horizontal band (pleural line) is visible in the upper portion. Below it, the texture appears somewhat granular/irregular rather than consisting of smooth parallel lines. Above the pleural line, some horizontal lines are visible.
**Classification: SEASHORE**

### p02 (~25%)
**Observation:** Bright pleural line visible in upper third. Below it, darker region with granular/sandy texture. Horizontal lines above the pleural line.
**Classification: SEASHORE**

### p03 (~35%)
**Observation:** Bright pleural band. Below it, texture with granular quality — irregular, not perfectly smooth horizontal lines.
**Classification: SEASHORE**

### p04 (~45%)
**Observation:** Prominent bright pleural line. Below it, granular/sandy texture is visible — clearly not continuous smooth horizontal lines.
**Classification: SEASHORE**

### p05 (~55%)
**Observation:** Prominent bright band (pleural line). Below it, the texture is dark with granular irregularity. Horizontal lines only above.
**Classification: SEASHORE**

### p06 (~65%)
**Observation:** Bright pleural line. Below it, darker granular texture visible, similar to neighboring positions.
**Classification: SEASHORE**

### p07 (~75%)
**Observation:** Bright pleural band. Below it, granular/sandy texture is present. Consistent with seashore sign.
**Classification: SEASHORE**

### p08 (~85%)
**Observation:** Bright horizontal bands visible at BOTH top and bottom of the image. The middle area between them appears smooth and dark without granular texture. Horizontal lines extend continuously throughout the image.
**Classification: STRATOSPHERE**

### p09 (~95%)
**Observation:** Very dense, bright, perfectly parallel horizontal lines dominate the lower half. Upper portion shows a horizontal bright band. The density and continuity of lines with no granularity between them is characteristic of barcode/stratosphere pattern.
**Classification: STRATOSPHERE**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | UNCLASSIFIABLE |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Seashore |
| p05 | Seashore |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Stratosphere |
| p09 | Stratosphere |

## Overall Decision

There is a clear **spatial transition**: positions p01–p07 show seashore pattern (pleural sliding present), while positions p08–p09 show stratosphere pattern (pleural sliding absent). This coexistence of both patterns across different lateral positions indicates a **lung point** — the boundary where a pneumothorax meets normally sliding lung.

**Overall Label: BOTH (Lung Point)**
