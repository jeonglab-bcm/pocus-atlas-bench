#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
import sys
from pathlib import Path
from typing import Callable, Any

os.environ.setdefault("MPLCONFIGDIR", "/tmp/pocus-research-matplotlib")
Path(os.environ["MPLCONFIGDIR"]).mkdir(parents=True, exist_ok=True)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist
from scipy.stats import chi2_contingency, binomtest, ttest_rel

try:
    import publiplots as pp
except ModuleNotFoundError:
    class _PlotFallback:
        @staticmethod
        def barplot(
            data: pd.DataFrame,
            x: str,
            y: str,
            hue: str | None = None,
            order: list[str] | None = None,
            hue_order: list[str] | None = None,
            legend: bool = False,
            errorbar=None,
            ax=None,
            xlabel: str = "",
            ylabel: str = "",
            title: str = "",
        ):
            del hue, hue_order, legend, errorbar
            if ax is None:
                ax = plt.gca()
            labels = order or data[x].tolist()
            values = [float(data.loc[data[x] == label, y].iloc[0]) for label in labels]
            colors = plt.cm.tab20(np.linspace(0, 1, max(len(labels), 1)))
            ax.bar(labels, values, color=colors[: len(labels)], edgecolor="black", linewidth=0.7)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_title(title)
            return ax

        @staticmethod
        def heatmap(
            data: pd.DataFrame,
            annot=None,
            fmt: str = "",
            cmap="viridis",
            vmin=None,
            vmax=None,
            norm=None,
            legend: bool = True,
            ax=None,
            title: str = "",
            xlabel: str = "",
            ylabel: str = "",
        ):
            if ax is None:
                ax = plt.gca()
            if norm is not None:
                im = ax.imshow(data.to_numpy(), aspect="auto", cmap=cmap, norm=norm)
            else:
                im = ax.imshow(data.to_numpy(), aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax)
            ax.set_xticks(np.arange(data.shape[1]))
            ax.set_xticklabels(data.columns, rotation=45, ha="right", fontsize=11)
            if data.shape[0] <= 60:
                ax.set_yticks(np.arange(data.shape[0]))
                ax.set_yticklabels(data.index, fontsize=11)
            else:
                ax.set_yticks([])
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            if annot is not None and data.shape[0] * data.shape[1] <= 500:
                annot_df = annot if isinstance(annot, pd.DataFrame) else data
                arr = data.to_numpy()
                val_range = arr.max() - arr.min() if arr.max() != arr.min() else 1.0
                for row_idx in range(data.shape[0]):
                    for col_idx in range(data.shape[1]):
                        val = annot_df.iloc[row_idx, col_idx]
                        if fmt:
                            text = f"{val:{fmt}}"
                        else:
                            text = str(val)
                        norm_val = (arr[row_idx, col_idx] - arr.min()) / val_range
                        # Adaptive: white on dark cells, black on light cells
                        text_color = "white" if norm_val > 0.45 else "black"
                        ax.text(
                            col_idx,
                            row_idx,
                            text,
                            ha="center",
                            va="center",
                            fontsize=9,
                            color=text_color,
                        )
            if legend:
                plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
            return ax

        @staticmethod
        def savefig(path: str):
            plt.savefig(path, bbox_inches="tight")

    pp = _PlotFallback()


def _binary_f1(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    if tp == 0:
        return 0.0
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0


def _macro_f1_multiclass(y_true: list[str], y_pred: list[str], labels: list[str]) -> float:
    f1s = []
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    for label in labels:
        tp = np.sum((y_true == label) & (y_pred == label))
        fp = np.sum((y_true != label) & (y_pred == label))
        fn = np.sum((y_true == label) & (y_pred != label))
        if tp == 0:
            f1s.append(0.0)
            continue
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
        f1s.append(f1)
    return float(np.mean(f1s))


ROOT = Path(os.environ.get("POCUS_ROOT", Path(__file__).resolve().parent.parent))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.aggregate_metrics import (
    load_sliding_gt,
    load_anterior_gt,
    load_posterior_gt,
    evaluate_t1_run,
    evaluate_t2_run,
    evaluate_t3_run,
    summarize_5run_accuracy,
    mean_ci,
)

OUTPUT_DIR = ROOT / "results_normalized" if (ROOT / "results_normalized").is_dir() else ROOT / "data/outputs"
CSV_PATH = ROOT / "hfdatasets/pocus_atlas/metadata.csv"
FIG_DIR = ROOT / "manuscript" / "figures"

TASKS = {
    "T1-frames": {"dir": "pocus_atlas_t1_sliding", "normalized_dir": "t1_sliding_frames", "eval": evaluate_t1_run},
    "T1-mmode": {"dir": "pocus_atlas_t1_sliding", "normalized_dir": "t1_sliding_mmode", "eval": evaluate_t1_run},
    "T2": {"dir": "pocus_atlas_t2_anterior", "normalized_dir": "t2_anterior_frames", "eval": evaluate_t2_run},
    "T3": {"dir": "pocus_atlas_t3_posterior", "normalized_dir": "t3_posterior_frames", "eval": evaluate_t3_run},
}
FRAMES_ROOT = ROOT / "data/processed/pocus_atlas/POCUS_Atlas_Bench/frames"
MMODES_ROOT = ROOT / "data/processed/pocus_atlas/POCUS_Atlas_Bench/mmodes"

# Co-author-approved success/failure example case_ids for issue #139.
# Selections finalized in discussions #145–#154.
EXAMPLE_CASE_ALLOWLIST: dict[tuple[str, str], list[str]] = {
    ("t1_frames", "correct"):   ["0060_lung_q7shylclnfsc3w5qezhq9rmxee06vk"],
    ("t1_frames", "incorrect"): ["0009_lung_lung-point-pneumothorax"],
    ("t1_mmode",  "correct"):   ["0013_lung_lung-slide-mmode"],
    ("t1_mmode",  "incorrect"): ["0130_lung_jr_pedsptxx",
                                 "0087_lung_cc6awlu86x2dv20d6j6vll98lkuwi2"],
    ("t2_1",      "correct"):   ["0120_lung_jr_blines"],
    ("t2_1",      "incorrect"): ["0122_lung_jr_pna"],
    ("t2_2",      "correct"):   ["0043_lung_normal-lung"],
    ("t2_2",      "incorrect"): ["0049_lung_pleural-shred-sign"],
    ("t3",        "correct"):   ["0007_lung_pleural-effusion-with-compressed-lung-and-spine-sign"],
    ("t3",        "incorrect"): ["0071_lung_0qbrvrw4ouvowjw3rqjd49q8ujia34",
                                 "0091_lung_r0rwfjsuyay58csdb4lriyu6byephy"],
}

MODEL_PARAM_B = {
    "gemma-4-e4e": 4,
    "gemma-4-12b": 12,
    "gemma-4-26b-a4b-it": 26,
    "medgemma-27b": 27,
    "gemma-4-31b-it": 31,
    "qwen3.6-35b-a3b": 35,
    # Claude sizes are approximate sorting keys (not disclosed); Sonnet < Opus
    "claude_sonnet-4.6": 40,
    "claude_opus-4.6": 200,
}


def model_size_sort_key(model: str) -> tuple[float, str]:
    """Sort size-known models by parameter count; keep unknown-size models last."""
    return (MODEL_PARAM_B.get(model, float("inf")), model)


def sort_models(models: list[str]) -> list[str]:
    return sorted(models, key=model_size_sort_key)


# --------------------------- run selection ---------------------------
def _candidate_run_dirs(task_key: str) -> list[Path]:
    old_task_dir = OUTPUT_DIR / TASKS[task_key]["dir"]
    if old_task_dir.is_dir():
        return sorted(p for p in old_task_dir.iterdir() if p.is_dir())

    normalized_task_dir = TASKS[task_key]["normalized_dir"]
    return sorted(OUTPUT_DIR.glob(f"*/{normalized_task_dir}/*"))


def _expected_input_mode(task_key: str) -> str:
    """Return expected input_mode for a task key."""
    if task_key == "T1-mmode":
        return "mmode"
    return "frames"


def collect_frame_full_runs(task_key: str, gt: dict, eval_fn: Callable) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    expected_mode = _expected_input_mode(task_key)

    for run_dir in _candidate_run_dirs(task_key):
        meta_file = run_dir / "run_meta.json"
        if not meta_file.exists():
            continue
        meta = json.loads(meta_file.read_text())
        if meta.get("input_mode") != expected_mode:
            continue

        metrics = eval_fn(run_dir, gt)
        if not metrics:
            continue

        rows.append(
            {
                "run_dir": run_dir,
                "run_id": meta.get("run_id", run_dir.name),
                "model": meta.get("model_id", "unknown"),
                "metrics": metrics,
                "n_cases": metrics.get("n_cases", 0),
            }
        )

    if not rows:
        return []

    # keep complete runs only
    max_cases = max(r["n_cases"] for r in rows)
    return [r for r in rows if r["n_cases"] == max_cases]


def select_frame_full_runs(task_key: str, gt: dict, eval_fn: Callable) -> list[dict[str, Any]]:
    rows = collect_frame_full_runs(task_key, gt, eval_fn)
    if not rows:
        return []

    # one run per model (latest run_id)
    by_model: dict[str, dict[str, Any]] = {}
    for r in rows:
        m = r["model"]
        if m not in by_model or r["run_id"] > by_model[m]["run_id"]:
            by_model[m] = r

    return list(by_model.values())


def build_task_runs_and_gt():
    gt_t1 = load_sliding_gt(CSV_PATH)
    gt_t2 = load_anterior_gt(CSV_PATH)
    gt_t3 = load_posterior_gt(CSV_PATH)

    runs = {
        "T1-frames": select_frame_full_runs("T1-frames", gt_t1, evaluate_t1_run),
        "T1-mmode": select_frame_full_runs("T1-mmode", gt_t1, evaluate_t1_run),
        "T2": select_frame_full_runs("T2", gt_t2, evaluate_t2_run),
        "T3": select_frame_full_runs("T3", gt_t3, evaluate_t3_run),
    }
    gts = {"T1-frames": gt_t1, "T1-mmode": gt_t1, "T2": gt_t2, "T3": gt_t3}
    return runs, gts


def build_all_frame_runs_and_gt():
    gt_t1 = load_sliding_gt(CSV_PATH)
    gt_t2 = load_anterior_gt(CSV_PATH)
    gt_t3 = load_posterior_gt(CSV_PATH)

    runs = {
        "T1-frames": collect_frame_full_runs("T1-frames", gt_t1, evaluate_t1_run),
        "T1-mmode": collect_frame_full_runs("T1-mmode", gt_t1, evaluate_t1_run),
        "T2": collect_frame_full_runs("T2", gt_t2, evaluate_t2_run),
        "T3": collect_frame_full_runs("T3", gt_t3, evaluate_t3_run),
    }
    gts = {"T1-frames": gt_t1, "T1-mmode": gt_t1, "T3": gt_t3, "T2": gt_t2}
    return runs, gts


# --------------------------- barplot (one figure per panel) ---------------------------
PUB_STYLE = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "axes.linewidth": 0.8,
    "axes.edgecolor": "#333333",
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 9,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
}
# Colorblind-safe model palette.
MODEL_COLORS = {
    "gemma-4-e4e": "#DE8F05",
    "gemma-4-12b": "#029E73",
    "gemma-4-26b-a4b-it": "#CC78BC",
    "medgemma-27b": "#CA9161",
    "gemma-4-31b-it": "#D55E00",
    "qwen3.6-35b-a3b": "#000000",
    "claude_sonnet-4.6": "#56B4E9",
    "claude_opus-4.6": "#0173B2",
}

# Display names matching the manuscript model labels.
MODEL_DISPLAY_NAMES = {
    "gemma-4-e4e": "Gemma-4 e4e",
    "gemma-4-12b": "Gemma-4 12B",
    "gemma-4-26b-a4b-it": "Gemma-4 26B-A4B-IT",
    "medgemma-27b": "MedGemma 27B",
    "gemma-4-31b-it": "Gemma-4 31B-IT",
    "qwen3.6-35b-a3b": "Qwen3.6 35B-A3B",
    "claude_sonnet-4.6": "Claude Sonnet 4.6",
    "claude_opus-4.6": "Claude Opus 4.6",
}


def _model_display_name(model: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model, model)


def _save_figure(pdf_path: str) -> None:
    """Save the figure as a PDF and mirror it as a 300-DPI PNG under figures/qmd/."""
    pp.savefig(pdf_path)
    p = Path(pdf_path)
    if p.suffix == ".pdf":
        qmd_dir = p.parent / "qmd"
        qmd_dir.mkdir(parents=True, exist_ok=True)
        plt.savefig(str(qmd_dir / p.with_suffix(".png").name), bbox_inches="tight", dpi=300)


def _model_color(model: str) -> str:
    return MODEL_COLORS.get(model, "#888888")


def _pub_barplot_one(
    d: pd.DataFrame,
    title: str,
    ylabel: str,
    out_name: str,
    show_legend: bool = False,
    extra_markers: dict[str, pd.Series] | None = None,
) -> None:
    """Draw a single publication-quality barplot."""
    if d.empty:
        return
    order = d["model"].tolist()
    colors = [_model_color(m) for m in order]

    # Cap width at the double-column text block (183 mm = 7.2 in).
    fig_w = min(7.2, 3.2 + 0.55 * len(order))
    fig, ax = plt.subplots(figsize=(fig_w, 4.5))
    x = np.arange(len(order))
    vals = d["value"].to_numpy()
    lo = d["lo"].to_numpy()
    hi = d["hi"].to_numpy()

    bars = ax.bar(x, vals, color=colors, edgecolor="#333333", linewidth=0.6, width=0.7)
    yerr = np.vstack([vals - lo, hi - vals])
    ax.errorbar(x, vals, yerr=yerr, fmt="none", ecolor="black", elinewidth=1.2, capsize=3.5, zorder=5)

    for xi, yi, hzi in zip(x, vals, hi):
        ax.text(xi, hzi + 0.02, f"{yi:.2f}", ha="center", va="bottom",
                fontsize=6.5,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.8, "pad": 0.3})

    if extra_markers:
        marker_styles = {
            "consensus": {"marker": "D", "s": 38, "color": "black", "label": "Consensus"},
            "any_correct": {"marker": "X", "s": 52, "color": "#B00020", "label": "Any correct"},
        }
        for key, series in extra_markers.items():
            style = marker_styles.get(key, {"marker": "o", "s": 30, "color": "gray"})
            ax.scatter(x, series, marker=style["marker"], s=style["s"],
                       color=style["color"], zorder=6, label=style["label"])
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2,
                  frameon=False, fontsize=7)

    short_labels = [_model_display_name(m) for m in order]
    ax.set_xticks(x)
    ax.set_xticklabels(short_labels, rotation=30, ha="right")
    ax.set_ylabel(ylabel)
    # In-plot title intentionally omitted: the Quarto caption carries the
    # panel description (Nature style; issue #327). `title` is retained as a
    # parameter only for the summary-CSV `panel` column at the call site.
    all_y = list(vals) + list(hi)
    if extra_markers:
        for series in extra_markers.values():
            all_y.extend(float(v) for v in series if pd.notna(v))
    y_upper = max(all_y) if all_y else 1.0
    # headroom above the CI cap for the value-label text (labels sit at hi + 0.02)
    ylim_top = min(1.25, y_upper + 0.14)
    ax.set_ylim(0, ylim_top)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.grid(axis="y", which="major", linestyle="--", linewidth=0.4, alpha=0.5)
    ax.grid(axis="y", which="minor", linestyle=":", linewidth=0.3, alpha=0.3)

    fig.tight_layout()
    _save_figure(str(FIG_DIR / out_name))
    plt.close(fig)


sliding_key = "T1-frames"  # canonical ground-truth key for T1 sliding


def _t1_pred_key(task_key: str) -> str:
    """Map T1 task keys back to 'T1' for _extract_case_predictions."""
    return "T1" if task_key.startswith("T1") else task_key


def make_barplot(task_runs: dict[str, list[dict[str, Any]]], gts: dict[str, dict]) -> None:
    """Headline F1 barplots: mean per-run F1 with a 95% CI across each model's runs.

    `task_runs` must carry every complete run per model (from
    `collect_frame_full_runs`), not one run per model.
    """
    t1_labels = ["present", "absent", "both"]

    def t1_f1_for_run(run, task_key: str) -> float:
        preds = _extract_case_predictions(run["run_dir"], _t1_pred_key(task_key))
        gt = gts[task_key]
        common = sorted(set(gt.keys()).intersection(preds.keys()))
        y_true = [gt[c] for c in common]
        y_pred = [preds[c] for c in common]
        return _macro_f1_multiclass(y_true, y_pred, t1_labels)

    def t2_f1_for_run(run, key: str) -> float:
        preds = _extract_case_predictions(run["run_dir"], "T2")
        common = sorted(set(gts["T2"].keys()).intersection(preds.keys()))
        y_true = np.array([int(bool(gts["T2"][c][key])) for c in common])
        y_pred = np.array([int(bool(preds[c][key])) for c in common])
        return _binary_f1(y_true, y_pred)

    def t3_f1_for_run(run) -> float:
        preds = _extract_case_predictions(run["run_dir"], "T3")
        common = sorted(set(gts["T3"].keys()).intersection(preds.keys()))
        y_true = np.array([int(bool(gts["T3"][c]["plaps"])) for c in common])
        y_pred = np.array([int(bool(preds[c])) for c in common])
        return _binary_f1(y_true, y_pred)

    panel_defs = [
        ("T1-frames", "T1 Frames — Pleura Sliding Macro F1", "F1", "barplot_t1_frames_f1.pdf", lambda r: t1_f1_for_run(r, "T1-frames")),
        ("T1-mmode", "T1 M-mode — Pleura Sliding Macro F1", "F1", "barplot_t1_mmode_f1.pdf", lambda r: t1_f1_for_run(r, "T1-mmode")),
        ("T2", "T2-1 Lung Rockets — F1", "F1", "barplot_t2_1_rockets_f1.pdf", lambda r: t2_f1_for_run(r, "lung_rockets")),
        ("T2", "T2-2 Consolidation — F1", "F1", "barplot_t2_2_consolidation_f1.pdf", lambda r: t2_f1_for_run(r, "consolidation")),
        ("T3", "T3 PLAPS — F1", "F1", "barplot_t3_plaps_f1.pdf", lambda r: t3_f1_for_run(r)),
    ]

    summary_rows = []
    for task_key, title, ylabel, out_name, f1_fn in panel_defs:
        runs_by_model: dict[str, list[dict[str, Any]]] = {}
        for run in task_runs[task_key]:
            runs_by_model.setdefault(run["model"], []).append(run)

        rows = []
        for model in sorted(runs_by_model, key=model_size_sort_key):
            per_run_f1 = [f1_fn(run) for run in runs_by_model[model]]
            mean_f1, lo, hi = mean_ci(per_run_f1)
            rows.append({"model": model, "value": mean_f1, "lo": lo, "hi": hi})
            summary_rows.append(
                {
                    "panel": title,
                    "model": model,
                    "value": mean_f1,
                    "ci_lo": lo,
                    "ci_hi": hi,
                    "n_runs": len(per_run_f1),
                    "per_run_f1": ";".join(f"{v:.4f}" for v in per_run_f1),
                }
            )

        d = pd.DataFrame(rows)
        with plt.rc_context(PUB_STYLE):
            _pub_barplot_one(d, title=title, ylabel=ylabel, out_name=out_name)

    pd.DataFrame(summary_rows).to_csv(FIG_DIR / "benchmark_barplot_t1_t2_t3_values_ci.csv", index=False)


def make_t2_paired_tests(all_task_runs: dict[str, list[dict[str, Any]]], gts: dict[str, dict]) -> None:
    """Paired between-model tests for the top two T2 models on each binary panel.

    For the two highest-mean-F1 models on a panel, compare their per-case
    correctness on the shared cases. Runs are paired chronologically. Reports
    per-run exact McNemar tests (binomial on discordant pairs) and a paired
    t-test on the five per-run F1 values. Writes benchmark_t2_paired_tests.csv.
    """
    panels = [
        ("T2-1 Lung Rockets", "lung_rockets"),
        ("T2-2 Consolidation", "consolidation"),
    ]
    runs_by_model: dict[str, list[dict[str, Any]]] = {}
    for run in all_task_runs["T2"]:
        runs_by_model.setdefault(run["model"], []).append(run)
    gt = gts["T2"]

    def panel_f1(pred: dict, common: list[str], key: str) -> float:
        y = np.array([int(bool(gt[c][key])) for c in common])
        p = np.array([int(bool(pred[c][key])) for c in common])
        return _binary_f1(y, p)

    rows = []
    for panel_name, key in panels:
        ranked = sorted(
            runs_by_model,
            key=lambda m: np.mean(
                [panel_f1(_extract_case_predictions(r["run_dir"], "T2"),
                          sorted(set(gt) & set(_extract_case_predictions(r["run_dir"], "T2"))), key)
                 for r in runs_by_model[m]]
            ),
            reverse=True,
        )
        a, b = ranked[0], ranked[1]
        ra = sorted(runs_by_model[a], key=lambda x: x["run_id"])
        rb = sorted(runs_by_model[b], key=lambda x: x["run_id"])

        fa_list, fb_list = [], []
        disc_b_total, disc_c_total, per_run_p = 0, 0, []
        for xa, xb in zip(ra, rb):
            pa = _extract_case_predictions(xa["run_dir"], "T2")
            pb = _extract_case_predictions(xb["run_dir"], "T2")
            common = sorted(set(gt) & set(pa) & set(pb))
            fa_list.append(panel_f1(pa, common, key))
            fb_list.append(panel_f1(pb, common, key))
            b_ct = sum(1 for c in common
                       if (bool(pa[c][key]) == bool(gt[c][key])) and (bool(pb[c][key]) != bool(gt[c][key])))
            c_ct = sum(1 for c in common
                       if (bool(pb[c][key]) == bool(gt[c][key])) and (bool(pa[c][key]) != bool(gt[c][key])))
            disc_b_total += b_ct
            disc_c_total += c_ct
            d = b_ct + c_ct
            per_run_p.append(binomtest(b_ct, d, 0.5).pvalue if d > 0 else 1.0)

        disc = disc_b_total + disc_c_total
        pooled_p = binomtest(disc_b_total, disc, 0.5).pvalue if disc > 0 else 1.0
        t_stat, t_p = ttest_rel(fa_list, fb_list)
        rows.append(
            {
                "panel": panel_name,
                "model_a": a,
                "model_b": b,
                "mean_f1_a": float(np.mean(fa_list)),
                "mean_f1_b": float(np.mean(fb_list)),
                "mean_f1_diff": float(np.mean(fa_list) - np.mean(fb_list)),
                "mcnemar_pooled_b": disc_b_total,
                "mcnemar_pooled_c": disc_c_total,
                "mcnemar_pooled_p": pooled_p,
                "mcnemar_per_run_p": ";".join(f"{p:.4f}" for p in per_run_p),
                "paired_t_stat": float(t_stat),
                "paired_t_p": float(t_p),
            }
        )

    pd.DataFrame(rows).to_csv(FIG_DIR / "benchmark_t2_paired_tests.csv", index=False)


def _group_run_dirs_by_model(runs: list[dict[str, Any]]) -> dict[str, list[Path]]:
    by_model: dict[str, list[Path]] = {}
    for run in runs:
        by_model.setdefault(run["model"], []).append(run["run_dir"])
    return by_model


def make_5run_accuracy_barplot(all_task_runs: dict[str, list[dict[str, Any]]], gts: dict[str, dict]) -> None:
    panel_defs = [
        (
            "T1-frames",
            "T1 Frames — 5-run accuracy",
            "Accuracy",
            "barplot_t1_frames_5run_accuracy.pdf",
            gts["T1-frames"],
            lambda data: data["pleura_sliding"],
        ),
        (
            "T1-mmode",
            "T1 M-mode — 5-run accuracy",
            "Accuracy",
            "barplot_t1_mmode_5run_accuracy.pdf",
            gts["T1-mmode"],
            lambda data: data["pleura_sliding"],
        ),
        (
            "T2",
            "T2-1 Lung Rockets — 5-run accuracy",
            "Accuracy",
            "barplot_t2_1_5run_accuracy.pdf",
            {case_id: values["lung_rockets"] for case_id, values in gts["T2"].items()},
            lambda data: data["lung_rockets"],
        ),
        (
            "T2",
            "T2-2 Consolidation — 5-run accuracy",
            "Accuracy",
            "barplot_t2_2_5run_accuracy.pdf",
            {case_id: values["consolidation"] for case_id, values in gts["T2"].items()},
            lambda data: data["consolidation"],
        ),
        (
            "T3",
            "T3 PLAPS — 5-run accuracy",
            "Accuracy",
            "barplot_t3_5run_accuracy.pdf",
            {case_id: values["plaps"] for case_id, values in gts["T3"].items()},
            lambda data: data["plaps"],
        ),
    ]

    summary_rows = []
    for task_key, title, ylabel, out_name, gt, getter in panel_defs:
        rows = []
        for model, run_dirs in sorted(
            _group_run_dirs_by_model(all_task_runs[task_key]).items(),
            key=lambda x: model_size_sort_key(x[0]),
        ):
            summary = summarize_5run_accuracy(run_dirs, gt, getter)
            if not summary:
                continue
            ci_lo, ci_hi = summary["pass_at_1_ci"]
            rows.append(
                {
                    "model": model,
                    "value": summary["pass_at_1"],
                    "lo": ci_lo,
                    "hi": ci_hi,
                    "consensus": summary["consensus_accuracy"],
                    "any_correct": summary["any_correct_accuracy"],
                }
            )
            summary_rows.append({"panel": title, **rows[-1]})

        d = pd.DataFrame(rows)
        if d.empty:
            continue
        extra = {
            "consensus": d["consensus"],
            "any_correct": d["any_correct"],
        }
        with plt.rc_context(PUB_STYLE):
            _pub_barplot_one(d, title=title, ylabel=ylabel, out_name=out_name, extra_markers=extra)

    pd.DataFrame(summary_rows).to_csv(FIG_DIR / "benchmark_5run_accuracy_summary.csv", index=False)


# --------------------------- per-case response matrices ---------------------------
def _extract_case_predictions(run_dir: Path, task_key: str) -> dict[str, Any]:
    preds: dict[str, Any] = {}
    for pred_file in sorted(run_dir.rglob("prediction.json")):
        case_id = pred_file.parent.name
        p = json.loads(pred_file.read_text())
        if (_t1_pred_key(task_key) == "T1") and "pleura_sliding" in p:
            preds[case_id] = p["pleura_sliding"]
        elif task_key == "T2":
            preds[case_id] = {
                "lung_rockets": bool(p.get("lung_rockets", False)),
                "consolidation": bool(p.get("consolidation", False)),
            }
        elif task_key == "T3" and "plaps" in p:
            preds[case_id] = bool(p.get("plaps", False))
    return preds


def _cluster_indices(df: pd.DataFrame, fix_first_col: bool = False) -> tuple[np.ndarray, np.ndarray]:
    arr = df.to_numpy()

    if df.shape[0] > 1:
        rdist = pdist(arr, metric="hamming")
        rord = leaves_list(linkage(rdist, method="average")) if np.any(rdist) else np.arange(df.shape[0])
    else:
        rord = np.arange(df.shape[0])

    if df.shape[1] <= 1:
        cord = np.arange(df.shape[1])
    elif fix_first_col:
        if df.shape[1] == 2:
            cord = np.array([0, 1])
        else:
            arr_sub = arr[:, 1:]
            cdist = pdist(arr_sub.T, metric="hamming")
            c_sub = leaves_list(linkage(cdist, method="average")) if np.any(cdist) else np.arange(arr_sub.shape[1])
            cord = np.concatenate(([0], c_sub + 1))
    else:
        cdist = pdist(arr.T, metric="hamming")
        cord = leaves_list(linkage(cdist, method="average")) if np.any(cdist) else np.arange(df.shape[1])

    return rord, cord


GT_COL = "Ground-truth"


def _plot_confusion_matrix_panel(
    models: list[str],
    cms: dict[str, np.ndarray],
    task_name: str,
    labels: list[str],
    out_name: str,
) -> None:
    """Plot one confusion-matrix subplot per model in a grid."""
    n_models = len(models)
    if n_models == 0:
        return

    n_labels = len(labels)
    ncols = min(4, n_models)
    nrows = (n_models + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(ncols * 3.2, nrows * 3.0))
    if nrows * ncols == 1:
        axes = np.array([[axes]])
    elif nrows == 1:
        axes = axes[np.newaxis, :]
    elif ncols == 1:
        axes = axes[:, np.newaxis]

    cmap_cm = matplotlib.colors.LinearSegmentedColormap.from_list(
        "cm_steel", ["#FFFFFF", "#4C72B0"], N=256
    )

    for idx, m in enumerate(models):
        ax = axes.flat[idx]
        cm = cms.get(m)
        if cm is None:
            ax.axis("off")
            continue
        cm_float = cm.astype(float)
        row_sums = cm_float.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1
        cm_pct = cm_float / row_sums * 100

        ax.imshow(cm_pct, cmap=cmap_cm, vmin=0, vmax=100, aspect="equal")
        ax.set_xticks(range(n_labels))
        ax.set_yticks(range(n_labels))
        ax.set_xticklabels(labels, fontsize=7, rotation=45, ha="right")
        ax.set_yticklabels(labels, fontsize=7)
        ax.set_xlabel("Predicted", fontsize=8)
        ax.set_ylabel("Ground-truth", fontsize=8)
        short = _model_display_name(m)
        ax.set_title(short, fontsize=9, fontweight="bold")

        for i in range(n_labels):
            for j in range(n_labels):
                count = cm[i, j]
                pct = cm_pct[i, j]
                text_color = "black"
                ax.text(j, i, f"{count}\n({pct:.0f}%)",
                        ha="center", va="center", fontsize=7, color=text_color)

    # Hide unused axes
    for idx in range(n_models, nrows * ncols):
        axes.flat[idx].axis("off")

    fig.suptitle(f"{task_name} — Confusion matrices", fontsize=12, fontweight="bold")
    plt.tight_layout()
    _save_figure(str(FIG_DIR / out_name))
    plt.close(fig)


def make_confusion_matrices(task_runs: dict[str, list[dict[str, Any]]], gts: dict[str, dict]) -> None:
    # ---- T1 Frames — 3-class confusion matrices ----
    t1_labels = ["Present", "Absent", "Both"]
    t1_label_map = {"present": 0, "absent": 1, "both": 2}

    for t1_key, t1_title, t1_out in [
        ("T1-frames", "T1 Frames — Sliding", "confusion_t1_frames.pdf"),
        ("T1-mmode", "T1 M-mode — Sliding", "confusion_t1_mmode.pdf"),
    ]:
        if not task_runs.get(t1_key):
            continue
        models_t1 = sort_models(list({r["model"] for r in task_runs[t1_key]}))
        cms_t1: dict[str, np.ndarray] = {}
        for run in task_runs[t1_key]:
            m = run["model"]
            if m in cms_t1:
                continue
            preds = _extract_case_predictions(run["run_dir"], "T1")
            common = sorted(set(gts[t1_key].keys()) & set(preds.keys()))
            cm = np.zeros((3, 3), dtype=int)
            for c in common:
                gi = t1_label_map[gts[t1_key][c]]
                pi = t1_label_map[preds[c]]
                cm[gi, pi] += 1
            cms_t1[m] = cm
        _plot_confusion_matrix_panel(
            models_t1, cms_t1,
            task_name=t1_title,
            labels=t1_labels,
            out_name=t1_out,
        )

    # T2-1 Rockets & T2-2 Consolidation — binary confusion matrices
    # Binary: True (0) first, False (1) second
    BINARY_LABELS = ["True", "False"]

    if task_runs["T2"]:
        models_t2 = sort_models(list({r["model"] for r in task_runs["T2"]}))
        cms_t2r: dict[str, np.ndarray] = {}
        cms_t2c: dict[str, np.ndarray] = {}
        for run in task_runs["T2"]:
            m = run["model"]
            if m in cms_t2r:
                continue
            preds = _extract_case_predictions(run["run_dir"], "T2")
            common = sorted(set(gts["T2"].keys()) & set(preds.keys()))
            cm_r = np.zeros((2, 2), dtype=int)
            cm_c = np.zeros((2, 2), dtype=int)
            for c in common:
                # True=0, False=1
                gi_r = 0 if gts["T2"][c]["lung_rockets"] else 1
                pi_r = 0 if preds[c]["lung_rockets"] else 1
                cm_r[gi_r, pi_r] += 1
                gi_c = 0 if gts["T2"][c]["consolidation"] else 1
                pi_c = 0 if preds[c]["consolidation"] else 1
                cm_c[gi_c, pi_c] += 1
            cms_t2r[m] = cm_r
            cms_t2c[m] = cm_c
        _plot_confusion_matrix_panel(
            models_t2, cms_t2r,
            task_name="T2-1 Rockets",
            labels=BINARY_LABELS,
            out_name="confusion_t2_1.pdf",
        )
        _plot_confusion_matrix_panel(
            models_t2, cms_t2c,
            task_name="T2-2 Consolidation",
            labels=BINARY_LABELS,
            out_name="confusion_t2_2.pdf",
        )

    # T3 — binary confusion matrices
    if task_runs["T3"]:
        models_t3 = sort_models(list({r["model"] for r in task_runs["T3"]}))
        cms_t3: dict[str, np.ndarray] = {}
        for run in task_runs["T3"]:
            m = run["model"]
            if m in cms_t3:
                continue
            preds = _extract_case_predictions(run["run_dir"], "T3")
            common = sorted(set(gts["T3"].keys()) & set(preds.keys()))
            cm = np.zeros((2, 2), dtype=int)
            for c in common:
                # True=0, False=1
                gi = 0 if gts["T3"][c]["plaps"] else 1
                pi = 0 if preds[c] else 1
                cm[gi, pi] += 1
            cms_t3[m] = cm
        _plot_confusion_matrix_panel(
            models_t3, cms_t3,
            task_name="T3 PLAPS",
            labels=BINARY_LABELS,
            out_name="confusion_t3.pdf",
        )


# --------------------------- model-model response correlation ---------------------------
def cramers_v_from_crosstab(ct: pd.DataFrame) -> float:
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return np.nan
    chi2, _, _, _ = chi2_contingency(ct)
    n = ct.values.sum()
    if n == 0:
        return np.nan
    r, k = ct.shape
    return float(np.sqrt((chi2 / n) / max(1, min(r - 1, k - 1))))


def _per_task_pred_vector(run_dir: Path, task_key: str) -> dict[str, str]:
    """Return {case_id -> stringified label} for a single run / task.

    Mirrors the in-line collection that lived in make_response_correlation_heatmap
    before option B switched to per-task computation. Each task contributes one
    or two named outcomes; T2 expands into rockets and consolidation.
    """
    out: dict[str, str] = {}
    for pred_file in sorted(run_dir.rglob("prediction.json")):
        case_id = pred_file.parent.name
        pred = json.loads(pred_file.read_text())
        if _t1_pred_key(task_key) == "T1" and "pleura_sliding" in pred:
            out[f"sliding::{case_id}"] = str(pred["pleura_sliding"])
        elif task_key == "T2":
            out[f"rockets::{case_id}"] = str(bool(pred.get("lung_rockets", False)))
            out[f"consolidation::{case_id}"] = str(bool(pred.get("consolidation", False)))
        elif task_key == "T3" and "plaps" in pred:
            out[f"plaps::{case_id}"] = str(bool(pred.get("plaps", False)))
    return out


def _cramers_v_between(a: dict[str, str], b: dict[str, str]) -> float:
    """Cramér's V on the case-level intersection of two prediction dicts."""
    keys = sorted(set(a).intersection(b))
    if not keys:
        return float("nan")
    s1 = pd.Series([a[k] for k in keys], name="a")
    s2 = pd.Series([b[k] for k in keys], name="b")
    ct = pd.crosstab(s1, s2)
    return cramers_v_from_crosstab(ct)


def _cohens_k_between(a: dict[str, str], b: dict[str, str]) -> float:
    """Unweighted Cohen's κ on the case-level intersection of two prediction dicts.

    Returns NaN when the intersection is empty or when the two raters'
    marginals make 1 - p_e degenerate (i.e. perfect chance agreement),
    matching the NaN convention used by Cramér's V on degenerate tables.
    """
    keys = sorted(set(a).intersection(b))
    if not keys:
        return float("nan")
    s1 = [a[k] for k in keys]
    s2 = [b[k] for k in keys]
    labels = sorted(set(s1).union(s2))
    n = len(keys)
    if n == 0 or len(labels) < 2:
        return float("nan")
    idx = {l: i for i, l in enumerate(labels)}
    cm = np.zeros((len(labels), len(labels)), dtype=float)
    for x, y in zip(s1, s2):
        cm[idx[x], idx[y]] += 1
    p_o = float(np.trace(cm) / n)
    row = cm.sum(axis=1) / n
    col = cm.sum(axis=0) / n
    p_e = float(np.dot(row, col))
    if p_e >= 1.0 - 1e-12:
        return float("nan")
    return float((p_o - p_e) / (1 - p_e))


def make_response_correlation_heatmap(task_runs: dict[str, list[dict[str, Any]]]) -> None:
    # Per-model, per-task, per-run prediction map. Both diagonal and off-diagonal
    # cells are unweighted task-averaged Cohen's κ over within-task run pairs
    # (issue #144 follow-up to #142): the diagonal averages over the C(5, 2) = 10
    # within-model run pairs per task; the off-diagonal averages over the
    # 5 × 5 = 25 cross-model run pairs per task. Same metric, same averaging
    # structure, end-to-end. κ subtracts chance agreement explicitly, which
    # is robust to T3's high-prevalence regime and to the 3-class vs binary
    # cardinality mix between T1 and T2/T3 in a way that Cramér's V is not
    # (cf. PR #143 review thread).
    model_task_runs: dict[str, dict[str, dict[str, dict[str, str]]]] = {}

    for task_key, runs in task_runs.items():
        for r in runs:
            model = r["model"]
            run_id = r["run_id"]
            preds = _per_task_pred_vector(r["run_dir"], task_key)
            model_task_runs.setdefault(model, {}).setdefault(task_key, {})[run_id] = preds

    models = sort_models(list(model_task_runs.keys()))
    if not models:
        return

    task_keys = sorted({tk for runs in model_task_runs.values() for tk in runs})

    # Self-consistency aggregate stats for the companion CSV.
    self_rows: list[dict[str, Any]] = []
    # Per-pair task-level values for the off-diagonal companion CSV.
    pair_rows: list[dict[str, Any]] = []

    mat = np.full((len(models), len(models)), np.nan)

    for i, m1 in enumerate(models):
        for j, m2 in enumerate(models):
            if i == j:
                # Diagonal: mean within-task run-pair Cohen's κ averaged across tasks.
                per_task_means: list[float] = []
                all_pairs: list[float] = []
                tasks_with_pairs = 0
                for tk in task_keys:
                    runs = model_task_runs.get(m1, {}).get(tk, {})
                    run_ids = sorted(runs.keys())
                    if len(run_ids) < 2:
                        continue
                    pair_vs: list[float] = []
                    for a in range(len(run_ids)):
                        for b in range(a + 1, len(run_ids)):
                            v = _cohens_k_between(runs[run_ids[a]], runs[run_ids[b]])
                            pair_vs.append(v)
                            all_pairs.append(v)
                    if pair_vs and not all(np.isnan(v) for v in pair_vs):
                        per_task_means.append(float(np.nanmean(pair_vs)))
                        tasks_with_pairs += 1
                if per_task_means:
                    mat[i, j] = float(np.nanmean(per_task_means))
                self_rows.append(
                    {
                        "model": m1,
                        # Plotted heatmap diagonal (task-averaged within-run-pair κ).
                        "self_consistency": (
                            float(mat[i, j]) if not np.isnan(mat[i, j]) else float("nan")
                        ),
                        # κ pooled equally over all valid run pairs.
                        "mean_pooled_pairs": (
                            float(np.nanmean(all_pairs))
                            if all_pairs and not all(np.isnan(v) for v in all_pairs)
                            else float("nan")
                        ),
                        "std_across_pairs": (
                            float(np.nanstd(all_pairs, ddof=1))
                            if sum(1 for v in all_pairs if not np.isnan(v)) > 1
                            else float("nan")
                        ),
                        "n_tasks": tasks_with_pairs,
                        "n_pairs_total": len(all_pairs),
                    }
                )
                continue

            # Off-diagonal: per-task Cohen's κ averaged over all 5×5 cross
            # run pairs, then averaged across tasks. This puts off-diagonal
            # cells on the same "mean over run pairs within a task" footing
            # as the diagonal, so the heatmap colour scale carries one
            # definition end-to-end. The earlier "latest run vs latest run"
            # construction was a holdover from PR #143 when only a single
            # run per model was available downstream.
            per_task_vs: list[float] = []
            per_task_record: dict[str, float] = {}
            per_task_n_pairs: dict[str, int] = {}
            for tk in task_keys:
                runs_a = model_task_runs.get(m1, {}).get(tk, {})
                runs_b = model_task_runs.get(m2, {}).get(tk, {})
                if not runs_a or not runs_b:
                    continue
                cross_ks: list[float] = []
                for rid_a in sorted(runs_a):
                    for rid_b in sorted(runs_b):
                        v = _cohens_k_between(runs_a[rid_a], runs_b[rid_b])
                        cross_ks.append(v)
                if cross_ks and not all(np.isnan(v) for v in cross_ks):
                    task_mean = float(np.nanmean(cross_ks))
                    per_task_record[tk] = task_mean
                    per_task_n_pairs[tk] = len(cross_ks)
                    per_task_vs.append(task_mean)
                else:
                    per_task_record[tk] = float("nan")
                    per_task_n_pairs[tk] = len(cross_ks)
            if per_task_vs:
                mat[i, j] = float(np.nanmean(per_task_vs))
            # Record one row per ordered pair (i < j) so the off-diagonal CSV
            # is half the size of the matrix and not duplicated by symmetry.
            if i < j:
                row = {
                    "model_a": m1,
                    "model_b": m2,
                    "mean": float(np.nanmean(per_task_vs)) if per_task_vs else float("nan"),
                    "std_across_tasks": (
                        float(np.nanstd(per_task_vs, ddof=1))
                        if len(per_task_vs) > 1
                        else float("nan")
                    ),
                    "min": float(min(per_task_vs)) if per_task_vs else float("nan"),
                    "max": float(max(per_task_vs)) if per_task_vs else float("nan"),
                    "n_tasks": len(per_task_vs),
                }
                for tk in task_keys:
                    row[f"K_{tk}"] = per_task_record.get(tk, float("nan"))
                    row[f"n_pairs_{tk}"] = per_task_n_pairs.get(tk, 0)
                pair_rows.append(row)

    # Sanity: diagonal should not be lower than that row's max off-diagonal.
    for i, m in enumerate(models):
        diag = mat[i, i]
        if np.isnan(diag):
            continue
        off = np.array([mat[i, j] for j in range(len(models)) if j != i])
        off = off[~np.isnan(off)]
        if off.size and float(off.max()) > diag + 1e-9:
            print(
                f"warning: self-consistency for {m} ({diag:.3f}) is below its "
                f"highest off-diagonal value ({off.max():.3f})"
            )

    df = pd.DataFrame(mat, index=models, columns=models).fillna(0.0)
    rord, cord = _cluster_indices(df, fix_first_col=False)
    df = df.iloc[rord, cord]

    # Save the precise Cohen's κ matrix to CSV for verification.
    df.to_csv(FIG_DIR / "heatmap_model_response_correlation_values.csv")

    # Companion CSV: per-model self-consistency (headline `self_consistency` is
    # the plotted diagonal; `mean_pooled_pairs` + std/counts for auditing).
    self_df = pd.DataFrame(self_rows).set_index("model")
    self_df = self_df.reindex(df.index)
    self_df.to_csv(FIG_DIR / "heatmap_model_response_correlation_self.csv")

    # Companion CSV: per-pair task-level breakdown of off-diagonal cells.
    # Records one row per (model_a, model_b) with model_a < model_b and the
    # raw per-task Cohen's κ values that get averaged into the matrix cell,
    # so the off-diagonal point estimate's spread across tasks is auditable.
    pair_df = pd.DataFrame(pair_rows)
    pair_df.to_csv(FIG_DIR / "heatmap_model_response_correlation_pairs.csv", index=False)

    # Plot lower triangle plus diagonal; mask upper triangle only. The diagonal
    # now carries information (self-consistency) instead of being a placeholder.
    df_masked = df.copy().astype(float)
    df_annot = df_masked.copy().round(2).astype(str)
    for i in range(df_masked.shape[0]):
        for j in range(df_masked.shape[1]):
            if j > i:  # upper triangle only
                df_masked.iloc[i, j] = np.nan
                df_annot.iloc[i, j] = ""

    fig, ax = plt.subplots(figsize=(9, 8))
    df_masked = df_masked.rename(index=_model_display_name, columns=_model_display_name)
    df_annot = df_annot.rename(index=_model_display_name, columns=_model_display_name)
    # κ can take negative values when systematic disagreement exceeds chance.
    # Use a divergent palette anchored at zero so 0 maps to white, positive
    # values to red, and negative values to blue. TwoSlopeNorm keeps zero
    # centred regardless of the asymmetric data range ([-0.2, 1.0] here).
    from matplotlib.colors import TwoSlopeNorm
    norm = TwoSlopeNorm(vmin=-0.2, vcenter=0.0, vmax=1.0)
    pp.heatmap(data=df_masked, annot=df_annot, fmt="", cmap="RdBu_r",
               norm=norm, ax=ax)
    plt.tight_layout()
    _save_figure(str(FIG_DIR / "heatmap_model_response_correlation.pdf"))
    plt.close(fig)


def make_example_frames(
    gts: dict[str, dict],
    max_cases: int = 10,
) -> None:
    """Render co-author-approved success/failure example PDFs for each subtask.

    Selection comes from EXAMPLE_CASE_ALLOWLIST (issue #139, discussions #145–#154).
    Each output directory is wiped before render so the on-disk set matches the
    allow-list exactly.

    Saves to figures/examples/<subtask_tag>/<category>/<case_id>.pdf
    """
    from PIL import Image as PILImage

    subtask_defs = [
        ("t1_frames", "T1 Frames — Pleura Sliding",
         lambda c: gts["T1-frames"][c], FRAMES_ROOT),
        ("t1_mmode", "T1 M-mode — Pleura Sliding",
         lambda c: gts["T1-mmode"][c], MMODES_ROOT),
        ("t2_1", "T2-1 — Lung Rockets",
         lambda c: gts["T2"][c]["lung_rockets"], FRAMES_ROOT),
        ("t2_2", "T2-2 — Consolidation",
         lambda c: gts["T2"][c]["consolidation"], FRAMES_ROOT),
        ("t3", "T3 — PLAPS",
         lambda c: gts["T3"][c]["plaps"], FRAMES_ROOT),
    ]
    cat_labels = {"correct": "All models correct", "incorrect": "All models incorrect"}

    for subtask_tag, subtask_name, gt_fn, img_root in subtask_defs:
        for cat_key, cat_label in cat_labels.items():
            cases = EXAMPLE_CASE_ALLOWLIST.get((subtask_tag, cat_key), [])
            assert cases, f"allow-list missing entry for ({subtask_tag}, {cat_key})"

            out_dir = FIG_DIR / "examples" / subtask_tag / cat_key
            shutil.rmtree(out_dir, ignore_errors=True)
            out_dir.mkdir(parents=True)

            for case_id in cases[:max_cases]:
                case_dir = img_root / case_id
                assert case_dir.is_dir(), f"frame dir missing: {case_dir}"
                frame_files = sorted(
                    list(case_dir.glob("*.jpg")) + list(case_dir.glob("*.png"))
                )[:10]
                assert frame_files, f"no frames found in {case_dir}"

                images = []
                for ff in frame_files:
                    img = PILImage.open(ff).convert("RGB")
                    images.append(np.array(img))

                gt_val = gt_fn(case_id)
                gt_display = str(gt_val).capitalize()

                fig, axes = plt.subplots(2, 5, figsize=(10, 4.5))
                fig.suptitle(
                    f"{subtask_name}  |  {cat_label}\n{case_id}  —  Ground-truth: {gt_display}",
                    fontsize=11, fontweight="bold", y=0.98,
                )
                for fi in range(10):
                    ax = axes.flat[fi]
                    if fi < len(images):
                        ax.imshow(images[fi])
                    ax.set_xticks([])
                    ax.set_yticks([])
                    ax.set_frame_on(False)

                plt.tight_layout(rect=[0, 0, 1, 0.92])
                out_path = out_dir / f"{case_id}.pdf"
                fig.savefig(str(out_path), dpi=300, bbox_inches="tight")
                plt.close(fig)
                print(f"  Saved {out_path.relative_to(FIG_DIR)}")



def main() -> None:
    FIG_DIR.mkdir(exist_ok=True)

    task_runs, gts = build_task_runs_and_gt()
    all_task_runs, all_gts = build_all_frame_runs_and_gt()

    make_barplot(all_task_runs, all_gts)
    make_t2_paired_tests(all_task_runs, all_gts)
    make_5run_accuracy_barplot(all_task_runs, all_gts)
    make_confusion_matrices(task_runs, gts)
    make_response_correlation_heatmap(all_task_runs)
    # make_example_frames omitted from this release: it renders qualitative
    # per-case example panels that require the raw extracted frames
    # (data/processed/.../frames|mmodes, out of release scope) and are not
    # embedded in the manuscript. The example PDFs are shipped as static
    # artifacts under manuscript/figures/examples/.

    print("Saved:")
    for p in sorted(FIG_DIR.glob("*.pdf")):
        print(" -", p)
    for p in sorted(FIG_DIR.glob("*.csv")):
        print(" -", p)


if __name__ == "__main__":
    main()
