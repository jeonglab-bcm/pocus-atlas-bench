# POCUS Atlas Benchmark - Reproducibility Release

Computational reproducibility for the manuscript **"Morphology, Not Motion:
Benchmarking Vision-Language Models on Multi-Sign Lung Ultrasound
Interpretation."**

This repository regenerates the manuscript's benchmark figures and numbers from
the **frozen model outputs** - the `results_normalized → aggregate → plot →
figures` chain. It does **not** re-run the LLM inference pipeline: API models
drift and are deprecated over time, so the frozen raw outputs are the only
verifiable artifact. Method reproducibility (prompts, model IDs, frame/M-mode
extraction) is documented in the manuscript appendices and summarized below.

> ⚠️ **PLACEHOLDER - manuscript not yet submitted.** Title, authors, venue, year,
> and DOI are provisional and will be finalized at preprint/submission time.
> See [Citation](#citation).

## What's included

```
results_normalized/         Frozen per-model LLM outputs (8 models, 8,010 predictions)
hfdatasets/pocus_atlas/      Ground-truth metadata (metadata.csv) + variable docs
scripts/                     Figure-generation chain (see below)
manuscript/figures/          Final figure artifacts (PDF/PNG/CSV) for comparison
requirements.txt             Pinned dependencies
LICENSE                      MIT
```

The evaluation **videos/frames are not redistributed here** - the dataset is
public on Hugging Face: **`bcm-liuzlab/pocus-atlas-bench`**
(https://huggingface.co/datasets/bcm-liuzlab/pocus-atlas-bench), CC-BY-NC-4.0.
The figure chain in this repo runs entirely from `results_normalized/` +
`metadata.csv` and does not need the raw videos.

## Reproduce the figures

```bash
# 1. Environment (Python 3.11+)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Regenerate the headline benchmark figures + CSVs
python -m scripts.plot_benchmark_publiplots

# 3. Above-chance permutation test (appendix)
python -m scripts.above_chance_permutation \
    --results-dir results_normalized \
    --metadata hfdatasets/pocus_atlas/metadata.csv \
    --n-perm 10000 --seed 42 \
    --out manuscript/figures/above_chance_permutation.csv

# 4. PLAPS composition breakdown (appendix, prints to stdout)
python -m scripts.plaps_composition --csv hfdatasets/pocus_atlas/metadata.csv

# 5. Figure 1 panel (d): per-run F1 vs. permutation-chance baseline
python -m scripts.fig1d_results_summary

# 6. Combine T1/T2 panel pairs into the manuscript's Fig 2-5 montages
python -m scripts.combine_panel_pngs
```

Outputs are written to `manuscript/figures/`. The headline CSVs
(`benchmark_barplot_t1_t2_t3_values_ci.csv`, `benchmark_t2_paired_tests.csv`,
`benchmark_5run_accuracy_summary.csv`, `heatmap_model_response_correlation_*.csv`)
regenerate **byte-identical** to the shipped versions.

### Verifying a match

```bash
md5sum manuscript/figures/*.csv
```

Compare against the shipped values; the five headline CSVs above match exactly.

## Figure-by-figure reproducibility

The manuscript's numeric results (all F1 / accuracy / κ values and their CSVs)
regenerate byte-identically from this release. Figure *images* fall into three
tiers depending on whether their plotting code ships here.

| Manuscript figure | Displayed file | Generator (this release) | Status |
|---|---|---|---|
| **Fig 1** composite | `overview_2x2.png` | 2×2 montage - see per-panel rows below | ⚠️ partial (panel d only) |
|  – Fig 1(a) pipeline | `pipeline_panel.png` | illustration (notebook) | ❌ not included |
|  – Fig 1(b) dataset diagram | `dataset_overview.png` | schematic (notebook) | ❌ not included |
|  – Fig 1(c) per-task stats | thumbnails + table | illustration (notebook) | ❌ not included |
|  - **Fig 1(d) results summary** | `fig1d_results_summary.{png,pdf}` | **`scripts.fig1d_results_summary`** | ✅ **reproduced from CSV** |
| **Fig 2** T1 F1 | `barplot_t1_combined_f1.png` | `scripts.plot_benchmark_publiplots` + `scripts.combine_panel_pngs` | ✅ reproduced |
| **Fig 3** T1 confusion | `confusion_t1_combined.png` | `scripts.plot_benchmark_publiplots` + `scripts.combine_panel_pngs` | ✅ reproduced |
| **Fig 4** T2 F1 | `barplot_t2_combined_f1.png` | `scripts.plot_benchmark_publiplots` + `scripts.combine_panel_pngs` | ✅ reproduced |
| **Fig 5** T2 confusion | `confusion_t2_combined.png` | `scripts.plot_benchmark_publiplots` + `scripts.combine_panel_pngs` | ✅ reproduced |
| **Fig 6** T3 F1 | `barplot_t3_plaps_f1.png` | `scripts.plot_benchmark_publiplots` | ✅ reproduced |
| **Fig 7** T3 confusion | `confusion_t3.png` | `scripts.plot_benchmark_publiplots` | ✅ reproduced |
| **Fig 8** model correlation | `heatmap_model_response_correlation.png` | `scripts.plot_benchmark_publiplots` | ✅ reproduced |
| **Fig 9** per-source (appendix) | `by_source_t1t2.png` | — | ❌ not included |
| **Fig 10** BLUE protocol (appendix) | `blue_protocol_mapping.png` | — | ❌ not included |

**Legend.** ✅ reproduced = the displayed image regenerates from shipped code +
frozen outputs. For Fig 2-5, `scripts.plot_benchmark_publiplots` renders the
individual sub-panels and `scripts.combine_panel_pngs` vertically stacks each
pair (a/b) into the montage shown in the manuscript (regenerates md5-identical).
❌ not included = an illustration/schematic or otherwise out-of-scope figure whose
generator is not part of this release; the final image is shipped for completeness
but is not regenerated here.

For **Fig 1** specifically: only panel **(d)** is data-driven (from
`benchmark_barplot_t1_t2_t3_values_ci.csv` + `above_chance_permutation.csv`) and
is regenerated by `scripts.fig1d_results_summary`. Panels (a)-(c) are
illustrative/schematic assets, and the 2×2 compositing step is not shipped.

## Method parameters (from the manuscript, for completeness)

The inference code is not part of this release, but the following method details
are recorded here so the frozen outputs are interpretable:

- **Models & providers:** see manuscript appendix "Models" (`@tbl-models`) -
  8 models across AWS Bedrock (Claude), OpenRouter (hosted Gemma/Qwen), and
  local GGUF endpoints. Each evaluated over **N=5** independent complete runs.
- **Decoding `max_tokens`:** reasoning/vision pass `65536`; structured
  extraction pass `4096`.
- **Temperature:** not explicitly set - each provider's **default** sampling
  temperature was used.
- **Frame extraction:** 10 evenly-spaced frames per clip via linear
  interpolation (`np.linspace`).
- **Synthetic M-mode (T1):** 15%-of-peak temporal-std active-region detection,
  10 lateral positions (5%...95%), 20-px strips, CLAHE clip 3.0, 4:3 resize.
- **Prompts:** verbatim Pass-1 reasoning prompts are reproduced in the
  manuscript appendix "Task Prompts."

## Known limitations

- **`above_chance_permutation.csv` z-values are numpy-version-sensitive.** F1 and
  chance columns are exact; the standardized effect size `z` can drift ~1-2%
  across numpy versions because the permutation null's RNG stream is
  version-dependent. `requirements.txt` pins `numpy==2.4.4` for deterministic
  regeneration. Conclusions are unaffected.
- **A few figure images are not regenerated by this release** (marked ❌ not
  included in the Figure-by-figure table above): Fig 1(a)-(c), the per-source
  appendix figure (Fig 9), and the BLUE-protocol schematic (Fig 10). These are
  illustrations/schematics or out-of-scope derived figures. Their final files
  (`by_source_long.csv` / `by_source_t1t2.*`, `manuscript/figures/examples/**`,
  etc.) are shipped so the manuscript is complete.

## Citation

> **PLACEHOLDER - do not cite yet.** The manuscript has not been submitted.

```bibtex
@misc{pocus_atlas_bench_PLACEHOLDER,
  title  = {Morphology, Not Motion: Benchmarking Vision-Language Models on
            Multi-Sign Lung Ultrasound Interpretation},
  author = {Lee, Jaeyeon and others},
  year   = {TBD},
  note   = {Preprint in preparation. Venue, year, and DOI to be finalized.},
  howpublished = {\url{TBD}}
}
```

## License

Code and documentation: [MIT](LICENSE). The POCUS Atlas dataset is
CC-BY-NC-4.0 and hosted separately on Hugging Face.
