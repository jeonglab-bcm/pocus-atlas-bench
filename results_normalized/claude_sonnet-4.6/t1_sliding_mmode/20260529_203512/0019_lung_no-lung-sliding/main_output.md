# 0019_lung_no-lung-sliding

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

| Position | Observation | Classification |
|----------|-------------|----------------|
| **p00** | Very bright white band near top; lower ~50% nearly black with minimal structure. Likely at or near edge of active ultrasound region. | **UNCLASSIFIABLE** |
| **p01** | Some horizontal banding visible in upper half; lower portion is dark but shows faint continuous horizontal striations. No granular texture discernible. | **Stratosphere** |
| **p02** | Bright horizontal band in upper third; below shows horizontal lines with decreasing signal toward bottom. Lines appear continuous, no sandy texture. | **Stratosphere** |
| **p03** | Better coverage; multiple distinct horizontal bands throughout. Between bright lines the texture is fine horizontal striations — no granularity. Pleural line appears smooth/straight. | **Stratosphere** |
| **p04** | Full image coverage with multiple uniform horizontal bands at varying brightness. No granular "sandy" background detected between lines. | **Stratosphere** |
| **p05** | Very similar to p04. Parallel horizontal bands throughout, continuous and uniform. No granularity. Pleural line straight. | **Stratosphere** |
| **p06** | Well-defined, dense parallel horizontal lines throughout entire depth. Highly characteristic barcode/stratosphere appearance. No granularity. | **Stratosphere** |
| **p07** | Horizontal banding in upper portion; lower portion shows slightly different brightness distribution but remains horizontally structured. No granular texture identified. | **Stratosphere** |
| **p08** | Bright horizontal band in mid-image; above and below show horizontal line patterns. No sandy background texture. | **Stratosphere** |
| **p09** | Nearly entirely black with only faint, barely visible horizontal traces. Likely at/beyond edge of active region. | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

- **Unclassifiable positions**: p00, p09 (excluded)
- **Classifiable positions**: p01–p08 (8 positions)
- **Seashore**: 0/8
- **Stratosphere**: 8/8
- **Alternating**: 0/8

> ### ✅ Overall Conclusion: **ABSENT**
> All 8 classifiable positions demonstrate the **stratosphere/barcode pattern** — dense, continuous parallel horizontal lines above and below the pleural line with a straight, smooth pleural line and **no granular/sandy texture** anywhere below it. This is consistent with **absent pleural sliding** across the entire interrogated region (e.g., pneumothorax, pleural adhesion, or apnea).
