# 0023_lung_pneumothorax-with-lung-point

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Assessment

### p00 (Image 1)
**Observation:** Mostly dark with a thin band of tissue visible. Bright pleural line with minimal signal above and below. Very limited depth penetration.
**Classification: UNCLASSIFIABLE** — edge of active scan region

### p01 (Image 2)
**Observation:** Multiple bright horizontal lines visible (pleural line + A-lines). In the lower/deeper portions, the background texture between the bright lines shows granular/speckled quality, not perfectly smooth.
**Classification: SEASHORE** (with prominent A-lines)

### p02 (Image 3)
**Observation:** Very dense, continuous parallel horizontal lines fill the entire image depth — both above and below the pleural line. Spaces between lines are smooth and horizontally uniform, with no granular texture.
**Classification: STRATOSPHERE**

### p03 (Image 4)
**Observation:** Similar to p02 — dense, unbroken horizontal lines throughout, uniform over time. No granular component visible between lines.
**Classification: STRATOSPHERE**

### p04 (Image 5)
**Observation:** Prominent bright pleural line with some waviness. Below it, horizontal A-lines present BUT background texture between them shows granularity and temporal variation (left vs. right sides differ). Lower-left darker zone suggests tissue motion.
**Classification: SEASHORE**

### p05 (Image 6)
**Observation:** Bright pleural line. Below, predominantly continuous horizontal lines extending uniformly across time. Spaces between lines are smooth/horizontal in character with minimal granularity.
**Classification: STRATOSPHERE**

### p06 (Image 7)
**Observation:** Below the pleural line, clear irregular, complex texture patterns that don't form clean horizontal lines. Granular/noisy quality with varied brightness — distinctly different from the smooth lines above.
**Classification: SEASHORE**

### p07 (Image 8)
**Observation:** Below the pleural line, varied, complex texture with bright irregular patches. Background is granular/sandy, not smooth horizontal lines. Temporal variation evident.
**Classification: SEASHORE**

### p08 (Image 9)
**Observation:** Horizontal lines above pleural line. Below, some granular variation visible, texture is not purely horizontal. Less signal in deeper areas but pattern is consistent with mild granularity.
**Classification: SEASHORE**

### p09 (Image 10)
**Observation:** Very dark overall with minimal signal. Faint lines at top, large dark zone centrally with some bright texture at very bottom. Insufficient structure for classification.
**Classification: UNCLASSIFIABLE**

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | UNCLASSIFIABLE |
| p01 | Seashore |
| p02 | **Stratosphere** |
| p03 | **Stratosphere** |
| p04 | Seashore |
| p05 | **Stratosphere** |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | UNCLASSIFIABLE |

---

## Overall Decision

**Classifiable positions:** 8
- **Seashore:** p01, p04, p06, p07, p08 (5 positions)
- **Stratosphere:** p02, p03, p05 (3 positions)

There is a clear **spatial coexistence** of both patterns — stratosphere at central positions (p02, p03, p05) and seashore at adjacent positions (p01, p04, p06–p08). This spatial transition from absent to present sliding across the scan region is diagnostic of a **lung point**.

## **Overall Label: BOTH (Lung Point)**
