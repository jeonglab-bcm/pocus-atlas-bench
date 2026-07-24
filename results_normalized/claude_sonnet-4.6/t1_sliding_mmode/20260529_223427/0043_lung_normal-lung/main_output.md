# 0043_lung_normal-lung

## Step 1 — Per-Position Classification

### p00 (~5%)
**Observation:** Almost entirely black; no discernible pleural line or sub-pleural texture. Minimal signal.
→ **UNCLASSIFIABLE** (edge artifact / outside active region)

---

### p01 (~15%)
**Observation:** Very dim; a faint diffuse grainy smear is barely visible in the mid-frame. Signal is too weak to confidently distinguish pattern.
→ **UNCLASSIFIABLE** (near-edge, insufficient signal)

---

### p02 (~25%)
**Observation:** A faint but definite bright horizontal band appears (pleural line). Below it, low-amplitude granular/sandy noise is visible with no dense parallel lines. Pleural line appears mildly irregular.
→ **Seashore** (subtle, early-in-beam)

---

### p03 (~35%)
**Observation:** Clearer pleural line; below it a mix of faint A-line echoes over a distinctly granular, sandy background. The background between any horizontal bands is noisy/speckled, not smooth parallel lines.
→ **Seashore**

---

### p04 (~45%)
**Observation:** Well-defined bright pleural line with A-line echoes beneath. Background texture between A-lines is clearly granular/sandy. Pleural line shows slight waviness/irregularity consistent with motion.
→ **Seashore**

---

### p05 (~55%)
**Observation:** Similar to p04 — prominent pleural line, A-lines, granular sandy background throughout the sub-pleural zone. No continuous dense parallel lines visible.
→ **Seashore**

---

### p06 (~65%)
**Observation:** Bright horizontal bands (pleural line + A-lines) with granular, heterogeneous texture filling the spaces between them. Slightly less bright than peak positions but clearly granular. Pleural line not perfectly straight.
→ **Seashore**

---

### p07 (~75%)
**Observation:** Bright pleural line, A-lines, and granular texture below — identical pattern to p04–p06. Background retains a sandy, speckled quality throughout.
→ **Seashore**

---

### p08 (~85%)
**Observation:** Signal dimming toward the edge; dark upper zone, a bright pleural band, granular sub-pleural texture with a bright artifact line at the very bottom (likely edge/reverberation artifact). Texture where visible is granular.
→ **Seashore** (borderline, signal fading)

---

### p09 (~95%)
**Observation:** Mostly dark; a prominent bright line at the very bottom is a border/edge artifact. Sub-pleural texture is essentially absent. Near-edge position.
→ **UNCLASSIFIABLE** (edge artifact)

---

## Summary Table

| Position | Classification |
|---|---|
| p00 | ❌ Unclassifiable |
| p01 | ❌ Unclassifiable |
| p02 | 🌊 Seashore |
| p03 | 🌊 Seashore |
| p04 | 🌊 Seashore |
| p05 | 🌊 Seashore |
| p06 | 🌊 Seashore |
| p07 | 🌊 Seashore |
| p08 | 🌊 Seashore |
| p09 | ❌ Unclassifiable |

---

## Step 2 — Overall Decision

- **Classifiable positions:** p02–p08 → **7/7 Seashore**
- No stratosphere pattern detected at any classifiable position
- No alternating (lung point) pattern detected
- No spatial seashore/stratosphere transition

> ## ✅ Overall Label: **PRESENT**
> **Pleural sliding is PRESENT** across the entire probe footprint. The consistent granular/sandy sub-pleural texture with an irregular, moving pleural line at all classifiable positions confirms lung sliding throughout.
