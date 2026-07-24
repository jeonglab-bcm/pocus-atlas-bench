# 0009_lung_lung-point-pneumothorax

# M-Mode Image Analysis

## Per-Position Classification

**p00 (Position ~5%):**
Upper portion is dark/black. Lower portion shows vertical bright columns with **granular/sandy texture** within them. No continuous horizontal lines below the pleural line. The bright speckled pattern is consistent with lung sliding.
→ **Seashore**

**p01 (Position ~15%):**
Horizontal lines visible above pleural line (chest wall). Below, there are A-lines present but the **background between them is clearly granular/sandy**. Pleural line appears somewhat irregular/wavy.
→ **Seashore**

**p02 (Position ~25%):**
Similar structure — horizontal lines above, below the pleural line shows A-lines with **granular texture between them**. Still has a sandy quality in the background.
→ **Seashore**

**p03 (Position ~35%):**
Dense, **continuous parallel horizontal lines** extend throughout both above and below the pleural line. Granularity is absent — replaced by smooth stratified bands. Pleural line appears straight.
→ **Stratosphere**

**p04 (Position ~45%):**
Dense horizontal lines throughout. No granular texture visible. The pattern is continuous horizontal striations both above and below.
→ **Stratosphere**

**p05 (Position ~55%):**
Vertical bands still visible but dominated by **continuous horizontal lines** with no granularity between them.
→ **Stratosphere**

**p06 (Position ~65%):**
Horizontal lines dominant throughout. Some vertical structures remain but the texture is **smooth horizontal striations without granularity**.
→ **Stratosphere**

**p07 (Position ~75%):**
Predominantly horizontal lines. Dense, continuous striations throughout. No sandy texture.
→ **Stratosphere**

**p08 (Position ~85%):**
Bright continuous horizontal bands. Clearly stratified, no granularity. Fading signal in lower portion.
→ **Stratosphere**

**p09 (Position ~95%):**
Very weak signal, mostly dark with faint horizontal bands in mid-portion. Insufficient detail for confident classification.
→ **Unclassifiable**

## Summary Table

| Position | Classification |
|----------|---------------|
| p00 | Seashore |
| p01 | Seashore |
| p02 | Seashore |
| p03 | Stratosphere |
| p04 | Stratosphere |
| p05 | Stratosphere |
| p06 | Stratosphere |
| p07 | Stratosphere |
| p08 | Stratosphere |
| p09 | Unclassifiable |

## Overall Decision

There is a clear **spatial transition**: positions p00–p02 show seashore (pleural sliding present) while positions p03–p08 show stratosphere (pleural sliding absent). This coexistence of both patterns across different spatial positions indicates a **lung point**.

**Overall Label: BOTH (Lung Point)**
