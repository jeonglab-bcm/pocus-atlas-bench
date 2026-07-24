# 0017_lung_lung-point2

# M-mode Analysis of Lung Ultrasound

## Per-Position Classification

### p00 (leftmost, ~5%)
**Observation:** Bright horizontal lines in the upper ~25%. Below the pleural line, the image is extremely dark with barely perceptible texture.
**Classification: UNCLASSIFIABLE** — Insufficient signal below the pleural line to determine pattern.

### p01 (~15%)
**Observation:** Horizontal lines in the upper portion. Below the pleural line, faint but visible texture with some columnar/vertical bright patches, similar in character to p02–p03 but dimmer.
**Classification: SEASHORE** — Faint granular elements visible below pleural line.

### p02 (~28%)
**Observation:** Clear horizontal lines above. Below the pleural line, distinct vertical columnar structures and scattered brightness create a clearly granular/sandy texture. A-lines may be present but the background between them is textured.
**Classification: SEASHORE** — Unmistakable granular pattern.

### p03 (~38%)
**Observation:** Horizontal lines above. Below the pleural line, prominent vertical columnar structures and granular texture — the most clearly "sandy" of all positions.
**Classification: SEASHORE** — High-confidence granular/sandy pattern.

### p04 (~50%)
**Observation:** Horizontal lines above. Below the pleural line, the texture transitions to more horizontally-organized bands without the columnar/granular character seen at p02–p03. The sub-pleural area lacks sandy texture and maintains horizontal continuity.
**Classification: STRATOSPHERE** — Horizontal pattern continues below without granularity.

### p05 (~60%)
**Observation:** Bright horizontal lines extend further into the image. Below the pleural line, faint horizontal bands persist with smooth/uniform texture between them. No granularity or vertical disruption is visible.
**Classification: STRATOSPHERE** — Horizontal continuity below the pleural line, no sandy texture.

### p06 (~72%)
**Observation:** Bright horizontal lines at top. Below is predominantly dark with minimal discernible texture.
**Classification: UNCLASSIFIABLE** — Insufficient detail below pleural line.

### p07 (~82%)
**Observation:** Similar to p06 — very dark below the pleural line.
**Classification: UNCLASSIFIABLE**

### p08 (~88%)
**Observation:** Bright lines at top; very dark below with faint texture that is insufficient for classification.
**Classification: UNCLASSIFIABLE**

### p09 (~95%)
**Observation:** Bright lines at top; dark below with minimal structure.
**Classification: UNCLASSIFIABLE**

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

**Classifiable positions:** 5 (3 Seashore, 2 Stratosphere)

---

## Overall Decision

There is a **clear spatial transition**: positions p01–p03 (left-to-center) show seashore pattern (granular texture = sliding present), while positions p04–p05 (center-to-right) show stratosphere pattern (horizontal continuity = sliding absent). This coexistence of both patterns across adjacent spatial positions is characteristic of a **lung point**.

## **Overall Label: BOTH (Lung Point)**
