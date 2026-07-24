# 0119_lung_jr_normal-lung-slide

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (Position 0 — leftmost)
**Observation:** Horizontal lines visible only in upper ~50%; lower half is nearly black with minimal signal. Insufficient active ultrasound coverage.
**→ UNCLASSIFIABLE** (edge dropout)

---

### p01
**Observation:** Multiple horizontal bright lines present throughout, but the background between lines shows visible noise/granularity. Lines are slightly irregular and not perfectly parallel or continuous. The texture is mixed rather than purely banded.
**→ SEASHORE** (A-lines over granular/noisy background; lines lack the rigid regularity of stratosphere)

---

### p02
**Observation:** Similar to p01 — horizontal lines are present but the inter-line background retains a visible speckled/granular texture. Lines are somewhat irregular.
**→ SEASHORE** (granular background texture detectable between lines)

---

### p03
**Observation:** Transition visible — lines become denser, more evenly spaced, and more continuous. Background texture between lines diminishes. The pattern starts approaching a barcode appearance.
**→ STRATOSPHERE** (dense, continuous parallel lines; granularity largely absent)

---

### p04
**Observation:** Dense, regular, continuous parallel horizontal bands throughout the entire frame. Minimal granularity between lines. Classic barcode/stratosphere appearance.
**→ STRATOSPHERE**

---

### p05
**Observation:** Very similar to p04 — dense parallel horizontal lines with no sandy texture between them. Some lateral edge-blurring visible but core pattern is barcode.
**→ STRATOSPHERE**

---

### p06
**Observation:** Marked change in pattern — a single, prominent, bright hyperechoic pleural line appears clearly in the upper third. Below it: relatively dark region with sparse granular/speckled texture (the lung parenchymal zone). Above it: chest wall parallel lines. Classic seashore morphology.
**→ SEASHORE**

---

### p07
**Observation:** Clear pleural line present. Below the pleural line: dark background with subtle A-lines but the background between them is granular/speckled rather than densely banded. The pleural line shows slight waviness.
**→ SEASHORE**

---

### p08
**Observation:** Bright pleural line visible. Below: dark with a granular texture and subtle A-line echoes. The overall subpleural region retains a sandy rather than continuously banded appearance.
**→ SEASHORE**

---

### p09 (Position 9 — rightmost)
**Observation:** Very dark throughout with minimal detectable structure. Near-black frame consistent with edge of active ultrasound region.
**→ UNCLASSIFIABLE** (edge dropout)

---

## Summary Table

| Position | Classification | Rationale |
|----------|---------------|-----------|
| p00 | **UNCLASSIFIABLE** | Edge — nearly black, no active signal |
| p01 | **Seashore** | Lines + visible granular background |
| p02 | **Seashore** | Lines + visible granular background |
| p03 | **Stratosphere** | Dense continuous lines, no granularity |
| p04 | **Stratosphere** | Dense barcode pattern |
| p05 | **Stratosphere** | Dense barcode pattern |
| p06 | **Seashore** | Clear pleural line + granular below |
| p07 | **Seashore** | Clear pleural line + granular below |
| p08 | **Seashore** | Clear pleural line + granular below |
| p09 | **UNCLASSIFIABLE** | Edge — nearly black, no active signal |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)

A **clear spatial transition** is present:
- p01–p02: **Seashore** (sliding present)
- p03–p05: **Stratosphere** (sliding absent)
- p06–p08: **Seashore** (sliding present)

This constitutes coexistence of both patterns across lateral positions, consistent with a **lung point** — the interface between a pneumothorax (medially, p03–p05) and aerated lung (laterally, p06–p08, and possibly medially at p01–p02).

> ## ✅ Overall Label: **"BOTH"** — Lung Point Identified
