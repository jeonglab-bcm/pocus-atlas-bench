# 0028_lung_normal-lung-sliding

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Upper zone: clear bright horizontal parallel lines. Below "pleural" zone: nearly completely black — no granularity, no horizontal lines, insufficient signal. Consistent with left edge of active region. | **UNCLASSIFIABLE** |
| **p01** | Upper zone: clear horizontal lines. Lower zone: still predominantly black, only minimal signal. Edge artefact persists. | **UNCLASSIFIABLE** |
| **p02** | Upper zone: distinct horizontal lines. A mid-level bright band (pleural line). Below: faint but emerging granular/sandy texture — begins to show the sandy background characteristic of seashore. Pleural line has slight irregularity. | **SEASHORE** |
| **p03** | Upper zone: bright horizontal lines. Pleural line visible. Below: clearly developing granular texture, no continuous parallel lines extending below. | **SEASHORE** |
| **p04** | Upper zone: well-defined horizontal lines. Pleural line visible. Below: definite sandy/granular texture occupying the sub-pleural zone; no barcode pattern. | **SEASHORE** |
| **p05** | Upper zone: bright horizontal lines. Pleural line: bright, slightly wavy/irregular. Below: clear granular/sandy texture — classic seashore appearance. | **SEASHORE** |
| **p06** | Upper zone: horizontal lines, slightly less bright at very top. Pleural line visible. Below: granular texture with scattered bright speckles; no horizontal line continuation below. | **SEASHORE** |
| **p07** | Upper zone: horizontal lines (fewer visible at top margin). Pleural zone: visible. Below: mixed but clearly granular/sandy texture rather than horizontal lines. | **SEASHORE** |
| **p08** | Upper zone: getting darker at top margin; some residual horizontal banding. Below pleural zone: reduced but still recognizably granular/textured rather than pure lines. | **SEASHORE** |
| **p09** | Upper zone: markedly dark at top — horizontal lines largely absent. Overall signal much reduced. Consistent with right edge of active region. | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

- **Unclassifiable positions:** p00, p01, p09 (edge artefact — excluded)
- **Classifiable positions (p02–p08): 7/7 → SEASHORE**
- No stratosphere pattern detected at any position (no region shows continuous parallel horizontal lines below the pleural line with absence of granularity)
- No alternating (lung point) pattern detected

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is present across the entire classifiable active ultrasound region. The consistent sandy/granular sub-pleural texture with a slightly irregular pleural line at all classifiable positions confirms normal lung sliding bilaterally at this probe location.
