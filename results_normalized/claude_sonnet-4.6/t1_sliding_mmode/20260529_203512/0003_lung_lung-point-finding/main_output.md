# 0003_lung_lung-point-finding

# Lung Ultrasound M-Mode Analysis

## Step 1 — Per-Position Classification

| Position | Observations | Classification |
|----------|-------------|----------------|
| **p00** | Nearly entirely black; only a faint thin bright line near the top; no discernible pleural line or sub-pleural texture | **UNCLASSIFIABLE** |
| **p01** | Very faint signal emerging; sparse horizontal lines visible in upper portion; subtle granular haze beginning to appear below | **SEASHORE** (borderline) |
| **p02** | Clearer pleural line forming; upper chest wall lines visible; below pleural line shows early granular/sandy background texture | **SEASHORE** |
| **p03** | Multiple horizontal bands above; distinct pleural line; below shows mixed horizontal lines over a clearly granular background — sandy sea floor appearance | **SEASHORE** |
| **p04** | Well-developed pattern; bright pleural band with A-line reverberations; background below is definitively granular/speckled, not pure line-based | **SEASHORE** |
| **p05** | Similar to p04; horizontal lines above + strong granular texture below the pleural line; pleural line slightly irregular (wavy) suggesting motion | **SEASHORE** |
| **p06** | Bright horizontal bands; sub-pleural region shows granularity intermixed — no pure barcode appearance; pleural line has subtle waviness | **SEASHORE** |
| **p07** | Good signal; seashore morphology persists — sandy texture dominant below the pleural line; A-lines present but riding over granular background | **SEASHORE** |
| **p08** | Signal beginning to fade but sub-pleural granularity still visible; no transition to pure horizontal stratosphere lines | **SEASHORE** |
| **p09** | Nearly black; minimal to no structure; edge dropout artifact | **UNCLASSIFIABLE** |

---

## Step 2 — Overall Decision

- **Unclassifiable**: p00, p09 (excluded)
- **Classifiable positions**: p01–p08 → **8/8 = Seashore**
- No stratosphere/barcode position detected
- No alternating (lung point) pattern detected

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is **present** across all classifiable lateral positions. The consistent granular/sandy sub-pleural texture with no barcode pattern confirms normal lung sliding throughout this region.
