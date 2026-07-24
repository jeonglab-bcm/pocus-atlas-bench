# 0013_lung_lung-slide-mmode

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Very dark top band (edge artifact); below: multiple horizontal lines of varying brightness → bright pleural line → **granular/sandy texture** below. Pleural line appears slightly wavy/irregular. | **Seashore** |
| **p01** | Reduced top darkness; organized horizontal parallel lines in near field → bright pleural line → **granular noisy background** below. Pleural line shows mild waviness. | **Seashore** |
| **p02** | Similar to p01; near-field parallel lines → pleural line → **granular texture** below. Pleural line not perfectly straight. | **Seashore** |
| **p03** | Near-field parallel lines → bright pleural line → **granular/sandy background** below. | **Seashore** |
| **p04** | Parallel lines above → pleural line → **granular texture** below; a brighter A-line band visible overlying the sandy background (not replacing it). | **Seashore** |
| **p05** | Parallel lines above → pleural line → **granular background** with an A-line superimposed below; background between A-lines is clearly sandy/noisy. | **Seashore** |
| **p06** | Same structure; near-field lines → pleural line → **granular texture** (with A-lines over it). No pure horizontal-line filling below. | **Seashore** |
| **p07** | Prominent parallel lines above → pleural line → **granular/noisy texture** below. | **Seashore** |
| **p08** | Horizontal lines above → bright pleural line → **granular texture** below; slightly noisier but clearly not barcode. | **Seashore** |
| **p09** | Dark top band (edge artifact) + unusual bright rectangular patches at lower edge (array edge artifacts); core pattern still shows near-field lines → pleural line → **granular background**. | **Seashore** |

---

## Step 2 — Overall Decision

**Key observations across all positions:**
- **Above the pleural line**: organized, relatively thin parallel horizontal lines (near-field reverberation) ✓
- **Pleural line itself**: bright but shows waviness/irregularity (indicating motion) ✓
- **Below the pleural line**: consistently **granular/sandy texture** — no position shows uninterrupted dense parallel lines filling the far field ✓
- A-lines present in several positions but always overlying sandy background (not replacing it) ✓
- No position shows pure Stratosphere/Barcode (continuous parallel lines with zero granularity)
- No position shows Alternating (lung point) pattern

> **No Stratosphere positions detected → no spatial transition → majority rule applies**

---

## ✅ Overall Label: **PRESENT**

**Pleural sliding is PRESENT** across the entire scanned region. All 10 classifiable positions demonstrate the Seashore sign, confirming normal pleural sliding throughout this lung zone.
