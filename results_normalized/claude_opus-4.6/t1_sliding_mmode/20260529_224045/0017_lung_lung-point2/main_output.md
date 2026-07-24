# 0017_lung_lung-point2

# M-Mode Image Analysis

## Per-Position Classification

### p00 (leftmost, ~5%)
**Observation:** Bright horizontal parallel lines in the upper ~25%. Below, the image is nearly black with minimal visible structure.
**Classification: UNCLASSIFIABLE** – insufficient signal (edge of active region)

### p01 (~15%)
**Observation:** Horizontal lines at top. Below the pleural line, some scattered/granular texture is visible, distinct from the smooth lines above. Faint but recognizable textural change.
**Classification: SEASHORE**

### p02 (~28%)
**Observation:** Clear horizontal lines above. Below the pleural line, distinct vertical columnar structures with granular texture between them. Clear pattern change from above to below — temporal variation is evident.
**Classification: SEASHORE** (high confidence)

### p03 (~38%)
**Observation:** Horizontal lines above. Below, prominent vertical bar-like structures with inter-column texture. Pattern clearly differs from the smooth horizontal lines above.
**Classification: SEASHORE** (high confidence)

### p04 (~50%)
**Observation:** Horizontal lines at top. Below the pleural line, multiple horizontal bands continue (broader but still horizontal). No granular texture visible between bands — lines persist across the entire depth.
**Classification: STRATOSPHERE**

### p05 (~60%)
**Observation:** Bright horizontal bands at top. Below, faint but recognizable horizontal striations continue. No granular/sandy texture identifiable.
**Classification: STRATOSPHERE**

### p06–p09 (~72%–95%)
**Observation:** All show bright horizontal lines concentrated at the top with predominantly dark fields below. Insufficient visible structure to determine pattern type.
**Classification: UNCLASSIFIABLE** (all four)

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Unclassifiable |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Seashore |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Unclassifiable |
| p07 | Unclassifiable |
| p08 | Unclassifiable |
| p09 | Unclassifiable |

## Overall Decision

**Classifiable positions:** p01–p03 = Seashore; p04–p05 = Stratosphere

There is a clear **spatial transition** — seashore (sliding present) on the left side transitioning to stratosphere (sliding absent) on the right side. This spatial coexistence of both patterns is the hallmark of a **lung point**.

## **Overall Label: BOTH (Lung Point)**
