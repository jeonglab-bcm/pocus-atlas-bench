# 0119_lung_jr_normal-lung-slide

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00
**Observation:** Horizontal parallel bright lines in the upper third; lower two-thirds is substantially dark. Some banding structure is visible but signal is weak inferiorly.
**Classification: STRATOSPHERE** *(horizontal banding in the visible zone; dark lower margin likely edge/gain fall-off — not nearly-black overall)*

---

### p01
**Observation:** Multiple bright horizontal lines distributed fairly evenly throughout. Background between lines shows predominantly horizontal texture with minimal granularity.
**Classification: STRATOSPHERE**

---

### p02
**Observation:** Very regular, evenly spaced bright horizontal bands from top to bottom. Background between bands is horizontally textured, not sandy/granular.
**Classification: STRATOSPHERE**

---

### p03
**Observation:** Classic dense, evenly spaced bright horizontal lines — near-perfect barcode appearance. Pleural line appears smooth and straight. No granular background.
**Classification: STRATOSPHERE**

---

### p04
**Observation:** Identical barcode morphology to p03 — dense, continuous, parallel horizontal lines throughout. No granularity detectable between lines.
**Classification: STRATOSPHERE**

---

### p05
**Observation:** Dense parallel horizontal lines persist throughout. Slightly more variation in line brightness than p03–p04, but no sand-like texture; the inter-line background remains linear/horizontal.
**Classification: STRATOSPHERE**

---

### p06
**Observation:** Clear structural shift: a distinct pleural line is visible with a dark space below it. Above and below the pleural line the dense barcode pattern is replaced by sparser lines and a transitional, somewhat granular background. The pleural line shows mild irregularity/waviness.
**Classification: SEASHORE**

---

### p07
**Observation:** Well-defined pleural line. Below it: characteristic coarse granular/sandy texture (the "seashore"). Above: a few smooth parallel lines (soft tissue). Classic seashore pattern with pleural line waviness.
**Classification: SEASHORE**

---

### p08
**Observation:** Similar to p07 — pleural line identified, sandy granular texture below, soft tissue parallel lines above. Seashore pattern is clear, though slightly fainter than p07.
**Classification: SEASHORE**

---

### p09
**Observation:** Image is predominantly black/near-black. Only faint traces of structure in the upper margin. Insufficient signal to characterize the pleural or sub-pleural zone.
**Classification: UNCLASSIFIABLE** *(right edge of active region — excluded from count)*

---

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Stratosphere |
| p01 | Stratosphere |
| p02 | Stratosphere |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Seashore |
| p07 | Seashore |
| p08 | Seashore |
| p09 | **Unclassifiable** |

---

## Step 2 — Overall Decision

**Classifiable positions (9): p00–p08**
- Stratosphere: p00–p05 (6 positions, left/mid field)
- Seashore: p06–p08 (3 positions, right field)

There is a **clear spatial transition** from absent pleural sliding (stratosphere/barcode, left) to present pleural sliding (seashore, right) across lateral positions. This is the hallmark of a **lung point**.

> ## ✅ Overall Label: **"BOTH" — Lung Point Present**
> Pleural sliding is **absent** laterally (left positions) and **present** medially (right positions), defining a lung point at approximately the p05–p06 boundary.
