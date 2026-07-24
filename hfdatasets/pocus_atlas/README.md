---
license: cc-by-nc-4.0
task_categories:
  - video-classification
tags:
  - medical
  - ultrasound
  - lung
  - point-of-care
  - POCUS
size_categories:
  - n<1K
---

# POCUS Atlas Lung Ultrasound Benchmark

A curated dataset of 150 lung ultrasound (LUS) video clips from [The POCUS Atlas](https://www.thepocusatlas.com/), annotated with clinical findings for automated interpretation benchmarking.

## Dataset Description

Each case is a short MP4 video clip of a lung ultrasound exam with accompanying metadata (YAML) and structured annotations (CSV).

### Sources
- **lung** (115 cases): Adult lung ultrasound atlas
- **lung_jr** (35 cases): Pediatric lung ultrasound atlas

### Annotations

`metadata.csv` contains per-case ground-truth labels for:
- Pleural signs (M-mode patterns, sliding, morphology)
- B-line findings (lung rockets, ground-glass, septal)
- Consolidation findings (air bronchograms, hepatization)
- Effusion findings (PLAPS, spine sign, sinusoid sign)
- Pathology classification and BLUE protocol profile assignment
- Predicted scan zone (anterior/posterior)

The first columns (`file_name`, `categories`, `tags`, `body`, `author`,
`case_page_url`) carry HF-compatible metadata; the remaining 37 columns
are the annotation matrix consumed by the evaluation pipelines.

See `variable_explanations.csv` for annotation column definitions.

## File Structure

```
unified_mp4/                 # 150 MP4 videos + 150 YAML metadata files
metadata.csv                 # single source of truth: HF metadata + annotations
variable_explanations.csv    # annotation-column documentation
```

## Usage

```python
from datasets import load_dataset

ds = load_dataset("bcm-liuzlab/pocus-atlas-bench")
```

## Citation

If you use this dataset, please cite The POCUS Atlas:
- https://www.thepocusatlas.com/
