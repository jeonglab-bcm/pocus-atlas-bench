# Normalized Results

This directory is a clean normalized copy of `results/`. The original source runs remain under `results/`.

Canonical layout:

```text
results_normalized/<model>/<task_mode>/<run_id>/
```

Model directories and `run_meta.json` `model_id` values use short model names only. Provider prefixes, quantization labels, packaging labels, and extra run suffixes are not used here.

Canonical task/mode directories:

- `t1_sliding_frames` -> `input_mode: frames`
- `t1_sliding_mmode` -> `input_mode: mmode`
- `t2_anterior_frames` -> `input_mode: frames`
- `t3_posterior_frames` -> `input_mode: frames`

Main pipeline check:

- No file named `mainfast` was found. The relevant pipeline source files are the three POCUS Atlas `main.nf` files.
- T1 `main.nf` accepts `frames`, `video`, and `mmode`; this normalized directory uses `mmode` for T1 M-mode runs.

Run counts:

- `claude_opus-4.6`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `claude_sonnet-4.6`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `gemma-4-12b`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `gemma-4-26b-a4b-it`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `gemma-4-31b-it`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `gemma-4-e4e`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `medgemma-27b`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
- `qwen3.6-35b-a3b`: t1_sliding_frames: 5, t1_sliding_mmode: 5, t2_anterior_frames: 5, t3_posterior_frames: 5
