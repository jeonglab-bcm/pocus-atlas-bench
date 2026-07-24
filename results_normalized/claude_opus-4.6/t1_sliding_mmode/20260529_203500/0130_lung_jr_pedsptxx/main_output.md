# 0130_lung_jr_pedsptxx

# M-Mode Analysis: Per-Position Classification

## Position-by-Position Assessment

**p00 (leftmost ~5%):**
Clear horizontal lines in the upper portion (chest wall). Below the pleural line, the texture is distinctly granular/sandy with no continuous horizontal lines. The pleural line shows slight irregularity.
→ **Seashore**

**p01 (~15%):**
Horizontal lines above. Below the pleural line, granular/sandy texture dominates with some dark vertical regions. Background between any A-lines is clearly grainy.
→ **Seashore**

**p02 (~27%):**
More horizontal lines extend below the pleural line (prominent A-lines), but the background between them retains granular texture. Pleural line shows some waviness.
→ **Seashore**

**p03 (~38%):**
Dense, continuous parallel horizontal lines extending throughout both above and below the pleural line. Minimal granularity visible. Pleural line appears straight.
→ **Stratosphere**

**p04 (~50%):**
Dense continuous horizontal lines dominate the entire image. No granular texture between lines. Pleural line relatively straight.
→ **Stratosphere**

**p05 (~61%):**
Predominantly parallel horizontal lines throughout. Background between lines shows fine horizontal striations rather than granularity.
→ **Stratosphere**

**p06 (~72%):**
Dense horizontal lines with some vertical intensity variation. Lines remain continuous; background between them is lined, not granular.
→ **Stratosphere**

**p07 (~83%):**
Clear parallel lines above. Below pleural line, horizontal lines visible in lighter areas; dark vertical bands represent temporal signal variation but lined pattern persists.
→ **Stratosphere**

**p08 (~90%):**
Lines above pleural line. Below: predominantly dark, granular texture without continuous horizontal lines.
→ **Seashore**

**p09 (~95%):**
Extremely dark throughout with minimal discernible structure. Nearly black below a single bright line.
→ **Unclassifiable**

---

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
| p08 | Seashore |
| p09 | Unclassifiable |

---

## Overall Decision

There is a **clear spatial transition**: positions p00–p02 and p08 show **seashore** (pleural sliding present), while positions p03–p07 show **stratosphere** (pleural sliding absent). Both patterns coexist across different lateral positions.

**Overall Label: BOTH (Lung Point)**
