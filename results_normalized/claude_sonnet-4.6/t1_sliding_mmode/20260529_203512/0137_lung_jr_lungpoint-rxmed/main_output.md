# 0137_lung_jr_lungpoint-rxmed

## Step 1 — Per-Position Classification

| Pos | Observed Features | Classification |
|-----|-------------------|----------------|
| **p00** | Horizontal parallel lines above pleural line; below shows coarse granular/sandy texture with subtle A-lines over a grainy background; pleural line slightly irregular | **Seashore** |
| **p01** | Parallel lines above; below pleural line shows granular background with sandy texture; small dark vertical artifact (rib shadow) on left does not obscure the sandy subpleural zone | **Seashore** |
| **p02** | Clear pleural line with horizontal bands above; subpleural zone displays distinct granular/sandy background; pleural line shows mild waviness | **Seashore** |
| **p03** | Horizontal lines above; granular texture below pleural line; bright vertical structure on right edge consistent with rib shadow — texture in between is sandy | **Seashore** |
| **p04** | Well-defined pleural line with classic wavy/irregular contour; clear granular sandy texture below; A-lines present over sandy background | **Seashore** |
| **p05** | Horizontal lines above and below; A-lines visible but background texture between them is granular, not purely parallel-linear; subpleural zone lacks the "dense barcode" appearance | **Seashore** |
| **p06** | Similar to p05; horizontal lines above; background below pleural line retains granular quality; no pure dense-barcode appearance | **Seashore** |
| **p07** | Parallel lines above; below shows sandy/granular texture between rib-shadow artifacts; pleural line shows slight motion irregularity | **Seashore** |
| **p08** | Horizontal lines above; subpleural zone shows prominent granular texture; pleural line appears wavy/irregular, supporting sliding | **Seashore** |
| **p09** | Some vertical rib-shadow structures; between them the subpleural texture is granular; enough detail for classification | **Seashore** |

---

## Step 2 — Overall Decision

- **No Alternating/lung-point** pattern detected at any position  
- **No Stratosphere/barcode** pattern detected at any position  
- **No Unclassifiable** positions (all 10 have sufficient signal)  
- **10/10 classifiable positions = Seashore**

> ### ✅ Overall Label: **PRESENT**
> Pleural sliding is present across the entire interrogated lung region. The consistently granular/sandy subpleural texture, wavy pleural lines, and absence of any barcode-like zones confirm normal lung sliding throughout.
