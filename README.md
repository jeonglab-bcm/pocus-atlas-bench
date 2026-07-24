# POCUS Atlas Benchmark — Reproducibility Release

Computational reproducibility for the manuscript **"Morphology, Not Motion:
Benchmarking Vision-Language Models on Multi-Sign Lung Ultrasound
Interpretation."**

This repository regenerates the manuscript's benchmark figures and numbers from
the **frozen model outputs** — the `results_normalized → aggregate → plot →
figures` chain. It does **not** re-run the LLM inference pipeline: API models
drift and are deprecated over time, so the frozen raw outputs are the only
verifiable artifact. Method reproducibility (prompts, model IDs, frame/M-mode
extraction) is documented in the manuscript appendices and summarized below.

> ⚠️ **PLACEHOLDER — manuscript not yet submitted.** Title, authors, venue, year,
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

The evaluation **videos/frames are not redistributed here** — the dataset is
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

## Method parameters (from the manuscript, for completeness)

The inference code is not part of this release, but the following method details
are recorded here so the frozen outputs are interpretable:

- **Models & providers:** see manuscript appendix "Models" (`@tbl-models`) —
  8 models across AWS Bedrock (Claude), OpenRouter (hosted Gemma/Qwen), and
  local GGUF endpoints. Each evaluated over **N=5** independent complete runs.
- **Decoding `max_tokens`:** reasoning/vision pass `65536`; structured
  extraction pass `4096`.
- **Temperature:** not explicitly set — each provider's **default** sampling
  temperature was used.
- **Frame extraction:** 10 evenly-spaced frames per clip via linear
  interpolation (`np.linspace`).
- **Synthetic M-mode (T1):** 15%-of-peak temporal-std active-region detection,
  10 lateral positions (5%…95%), 20-px strips, CLAHE clip 3.0, 4:3 resize.
- **Prompts:** verbatim Pass-1 reasoning prompts are reproduced in the
  manuscript appendix "Task Prompts."

## Known limitations

- **`above_chance_permutation.csv` z-values are numpy-version-sensitive.** F1 and
  chance columns are exact; the standardized effect size `z` can drift ~1–2%
  across numpy versions because the permutation null's RNG stream is
  version-dependent. `requirements.txt` pins `numpy==2.4.4` for deterministic
  regeneration. Conclusions are unaffected.
- **Per-source (adult/junior) appendix figure and example-frame panels are
  provided as static artifacts only.** Their generators are omitted from this
  release (one has an upstream import break; the other requires raw frames that
  are out of scope). The final `by_source_long.csv` / `by_source_t1t2.*` and
  `manuscript/figures/examples/**` are included so the manuscript is complete.

## Citation

> **PLACEHOLDER — do not cite yet.** The manuscript has not been submitted.

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
