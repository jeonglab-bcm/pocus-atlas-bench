# 0119_lung_jr_normal-lung-slide

# M-Mode Lung Ultrasound Analysis

## Step 1 — Per-Position Classification

| Position | Observed Features | Classification |
|----------|-------------------|----------------|
| **p00** | A few faint horizontal lines in upper portion; lower half nearly black with minimal signal. Substantially lower SNR than adjacent positions — likely at edge of active beam. | **UNCLASSIFIABLE** |
| **p01** | Multiple dense, bright, continuous horizontal lines running uniformly top-to-bottom. Background between lines is horizontal striping — **no granular texture**. Pleural line perfectly straight. | **STRATOSPHERE** |
| **p02** | Same as p01 but slightly denser packing of lines. Fully continuous parallel stripes, no sandy/granular component anywhere in the field. Straight pleural line. | **STRATOSPHERE** |
| **p03** | Maximum line density. Thick, bright, regularly-spaced horizontal bands throughout. Background is composed entirely of horizontal striping. Zero granularity. | **STRATOSPHERE** |
| **p04** | Nearly identical to p03. Dense barcode pattern; all horizontal lines parallel and continuous. No granular texture between or below lines. | **STRATOSPHERE** |
| **p05** | Slightly reduced density vs. p03–p04, but still clearly a barcode pattern. Continuous horizontal lines dominate. No granularity. Pleural line straight. | **STRATOSPHERE** |
| **p06** | Abrupt change in appearance: clear bright pleural line visible, distinct soft-tissue layers above it (wavy/irregular pleural line contour), fewer A-lines below, and background between A-lines shows **granular/speckled texture**. | **SEASHORE** |
| **p07** | Classic seashore morphology: well-defined pleural line (slightly irregular/wavy), 2–3 A-lines below with clearly **granular/sandy background** in between. Upper tissue layers show wave-like motion artifact. | **SEASHORE** |
| **p08** | Similar to p07. Pleural line present, A-lines below overlying a **granular background**. Texture below pleural line is speckled, not striped. | **SEASHORE** |
| **p09** | Nearly completely black throughout. Minimal detectable signal or structure. Rightmost edge of active beam. | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)

| Pattern | Positions |
|---------|-----------|
| Stratosphere | p01, p02, p03, p04, p05 (5 positions — left-to-center) |
| Seashore | p06, p07, p08 (3 positions — center-to-right) |

> There is a **clear spatial transition** from Stratosphere (left) → Seashore (right) across the scan region. This represents co-existence of absent sliding (left) and present sliding (right) at different lateral positions.

---

## ✅ Overall Label: **BOTH — Lung Point Present**

**Interpretation:** Pleural sliding is **absent** on the left portion of the scan (stratosphere/barcode pattern, p01–p05) and **present** on the right portion (seashore pattern, p06–p08). The transition zone between approximately p05 and p06 marks the **lung point** — the boundary where the lung re-contacts the parietal pleura — consistent with a **pneumothorax** on the left side of this scan window.
