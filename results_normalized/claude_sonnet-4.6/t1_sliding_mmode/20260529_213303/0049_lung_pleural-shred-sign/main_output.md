# 0049_lung_pleural-shred-sign

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

### p00 (~5%, leftmost)
**Observation:** Nearly uniformly black frame with minimal signal structure. No discernible pleural line or tissue texture.
**Classification: UNCLASSIFIABLE** *(outside active ultrasound region)*

---

### p01 (~15%)
**Observation:** A moderately bright pleural line is visible in the upper third. Above: clear horizontal parallel lines. Below: visible **granular/sandy texture** predominates; the pleural line appears slightly irregular/wavy — indicating motion.
**Classification: SEASHORE** ✅

---

### p02 (~25%)
**Observation:** Pleural line brightens slightly. Above: horizontal parallel lines. Below: **granular sandy texture** is clearly present, interspersed with subtle A-line shadows over the sandy background. Pleural line shows mild waviness.
**Classification: SEASHORE** ✅

---

### p03 (~35%)
**Observation:** Clear, moderately bright pleural line. Above: horizontal lines. Below: **granular/sandy texture** visible throughout, with the pleural line showing mild undulation consistent with sliding.
**Classification: SEASHORE** ✅

---

### p04 (~45%)
**Observation:** Bright pleural line. Above: classic parallel horizontal lines. Below: **mixed texture** but clear granularity (sandy pattern) is detectable between streaks. Pleural line shows slight waviness.
**Classification: SEASHORE** ✅

---

### p05 (~55%)
**Observation:** Pleural line visible. Above: horizontal parallel lines. Below: texture is a mix of horizontal streaks and **granular background**, leaning seashore. Pleural line is mildly irregular.
**Classification: SEASHORE** ✅ *(borderline)*

---

### p06 (~65%)
**Observation:** Pleural line present. Above: horizontal lines. Below: predominantly horizontal streaking increases, but **residual granular texture** is still detectable in the background. Pleural line is not perfectly straight.
**Classification: SEASHORE** ✅ *(borderline)*

---

### p07 (~75%)
**Observation:** Pleural line remains visible. Above: horizontal lines. Below: horizontal line pattern is more prominent, but there is **still some granularity** in the background texture. The pleural line is not razor-straight.
**Classification: SEASHORE** ✅ *(borderline)*

---

### p08 (~85%)
**Observation:** Very bright, notably **straight and smooth** pleural line. Above: uniform horizontal parallel lines. Below: the region is **dark**, with faint horizontal lines extending uniformly — no sandy or granular texture visible. This is consistent with a stratosphere/barcode pattern.
**Classification: STRATOSPHERE** 🔲

---

### p09 (~95%, rightmost)
**Observation:** Extremely bright horizontal bands dominate the bottom of the frame; the central zone is nearly black. This distribution (strong near-field and far-field artifact) suggests the probe is at or beyond the active beam edge.
**Classification: UNCLASSIFIABLE** *(edge artifact)*

---

## Summary Table

| Position | Pattern | Notes |
|----------|---------|-------|
| p00 | UNCLASSIFIABLE | Near-black, no signal |
| p01 | **Seashore** | Granular texture, wavy pleural line |
| p02 | **Seashore** | Sandy texture, mild pleural waviness |
| p03 | **Seashore** | Granular texture below |
| p04 | **Seashore** | Sandy background, slight pleural waviness |
| p05 | **Seashore** | Mixed but granular; borderline |
| p06 | **Seashore** | Residual granularity; borderline |
| p07 | **Seashore** | Granular texture still present; borderline |
| p08 | **Stratosphere** | Straight pleural line, no granularity |
| p09 | UNCLASSIFIABLE | Edge artifact |

---

## Step 2 — Overall Decision

**Classifiable positions:** p01–p08 (8 positions)
- Seashore: **7/8** (p01–p07)
- Stratosphere: **1/8** (p08)

> Although p08 shows a stratosphere pattern, it represents a single lateral position at the far edge and does not constitute a clear spatial transition indicative of a lung point (which would require a more defined boundary between seashore and stratosphere zones across adjacent positions). The overwhelming majority (7/8) classify as seashore.

### ✅ Overall Label: **PRESENT**
**Pleural sliding is present.** The dominant pattern across classifiable positions is seashore, indicating lung sliding is occurring.
