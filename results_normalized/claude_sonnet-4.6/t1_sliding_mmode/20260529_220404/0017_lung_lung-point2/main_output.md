# 0017_lung_lung-point2

# M-Mode Lung Ultrasound Analysis

## Step 1 — Per-Position Classification

| Position | Key Observations | Classification |
|----------|-----------------|----------------|
| **p00** | Upper: clear horizontal parallel lines. Transition: distinctly **bumpy/irregular** pleural boundary. Lower: near-black but the jagged, undulating interface indicates tissue motion. | **Seashore** |
| **p01** | Upper: well-defined horizontal lines. Transition: irregular, scalloped pleural line. Lower: dark but slightly more texture than p00; wavy interface confirms motion. | **Seashore** |
| **p02** | Upper: horizontal lines. Lower: visible **vertical striping / columnar texture** emerging below pleural line — classic "sand" granularity appearing. | **Seashore** |
| **p03** | Upper: horizontal lines. Lower: **prominent alternating light/dark vertical banding** below the pleural line — strongest granular/sandy texture in the series. | **Seashore** |
| **p04** | Upper: horizontal lines. Lower: clear horizontal bands with visible intervening granular texture; pleural line shows mild irregularity. | **Seashore** |
| **p05** | Upper: horizontal lines plus one distinct **bright A-line band**. Lower: darker but residual granular background visible between A-lines; no dense barcode. | **Seashore** |
| **p06** | Upper: horizontal lines. Lower: noticeably darker; some faint textural heterogeneity and mildly irregular pleural line persist. Borderline but still interpretable. | **Seashore** *(borderline)* |
| **p07** | Upper narrow bright zone. Lower: near-black, minimal discernible structure. Likely approaching right edge of active beam. | **Unclassifiable** |
| **p08** | Upper narrow bright zone. Lower: near-black; only very faint shadow columns. Insufficient signal for confident classification. | **Unclassifiable** |
| **p09** | Upper narrow bright zone. Lower: nearly black throughout. Rightmost position — outside active ultrasound region. | **Unclassifiable** |

---

## Step 2 — Overall Decision

**Classifiable positions:** p00–p06 (7 positions)

- **All 7 classifiable positions → Seashore**
- No stratosphere/barcode pattern identified at any position (lower regions are dark-granular, never dense horizontal lines throughout)
- No alternating (lung point) pattern identified
- No spatial seashore↔stratosphere transition across positions

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is **present**. The granular/sandy texture below an irregular, motion-associated pleural line is consistently demonstrated across all classifiable M-mode positions.
