# 0043_lung_normal-lung

# M-Mode Lung Ultrasound Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Nearly all black; faint diffuse noise in a narrow mid-band; no discernible pleural line or subpleural structure | **UNCLASSIFIABLE** |
| **p01** | Low signal; faint granular/speckled texture distributed across the middle band; no clear horizontal line dominance | **SEASHORE** (weak) |
| **p02** | Black top, then a pleural line emerging as a bright band; below it: A-lines over a clearly granular/sandy background; pleural line slightly irregular | **SEASHORE** |
| **p03** | Well-defined bright pleural line; multiple A-lines visible; background between lines is granular/heterogeneous — not uniformly linear | **SEASHORE** |
| **p04** | Dense pattern; bright horizontal bands (A-lines) in upper portion; lower region shows granular/noisy texture intermixed with lines; horizontal lines do NOT form perfectly uniform barcode | **SEASHORE** |
| **p05** | Very similar to p04; horizontal bands prominent but background granularity clearly visible in mid-to-lower zones; texture is sandy, not purely linear | **SEASHORE** |
| **p06** | Bright A-lines in upper half; lower portion has complex mixed texture with visible granularity; no pure barcode appearance | **SEASHORE** |
| **p07** | Prominent bright pleural line and A-lines; texture below is granular/sandy; pleural line shows mild waviness suggesting motion | **SEASHORE** |
| **p08** | Signal fading toward edge; pleural line visible as a distinct bright line; below: some granular texture, some horizontal lines; above: large dark band | **SEASHORE** |
| **p09** | Mostly black with a single bright line near the bottom edge; essentially no subpleural texture visible; edge artifact | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)
**Seashore:** 8/8 — **Stratosphere:** 0/8 — **Alternating:** 0

> No spatial transition between seashore and stratosphere zones. No alternating (lung point) pattern detected. All classifiable positions consistently show granular/sandy texture below the pleural line (with A-lines superimposed), indicating active pleural sliding throughout the interrogated region.

---

## ✅ Overall Label: **PRESENT**
*Pleural sliding is present across the entire active ultrasound zone.*
