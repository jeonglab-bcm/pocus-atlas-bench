#!/usr/bin/env python3
"""
Aggregate metrics across multiple benchmark runs for T1 sliding, T2 anterior, and T3 posterior.

Scans data/outputs/ for run directories, groups by model_id from run_meta.json,
computes per-run metrics, and reports mean ± 95% CI across repetitions.

Usage:
    python scripts/aggregate_metrics.py
    python scripts/aggregate_metrics.py --output-dir data/outputs --task t1
    python scripts/aggregate_metrics.py --task all --csv-path hfdatasets/pocus_atlas/metadata.csv
"""

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_OUTPUT_DIR = "data/outputs"
DEFAULT_CSV_PATH = "hfdatasets/pocus_atlas/metadata.csv"

SLIDING_LABELS = ["present", "absent", "both"]
NORMALIZED_TASK_DIRS = {
    "pocus_atlas_t1_sliding": ("t1_sliding_frames", "t1_sliding_mmode"),
    "pocus_atlas_t2_anterior": ("t2_anterior_frames",),
    "pocus_atlas_t3_posterior": ("t3_posterior_frames",),
}


# ─── GT loaders (reused from evaluate scripts) ───────────────────────────────

def load_sliding_gt(csv_path: Path) -> dict[str, str]:
    cases = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, quotechar='"')
        for row in reader:
            if row.get("excluded", "").strip():
                continue
            sliding = row.get("interp::Pleura::Sliding", "").strip()
            if sliding == "not assessed":
                continue
            assert sliding in SLIDING_LABELS, f"Unexpected GT '{sliding}' for {row['id']}"
            cases[row["id"]] = sliding
    return cases


def load_anterior_gt(csv_path: Path) -> dict[str, dict]:
    cases = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, quotechar='"')
        for row in reader:
            if row.get("excluded", "").strip():
                continue
            plaps = row.get("interp::PLAPS", "").strip() == "True"
            normal_post = row.get("interp_extra::Normal posterior", "").strip() == "True"
            pneumothorax = row.get("pathology", "").strip() == "Pneumothorax"
            is_posterior = (plaps or normal_post) and not pneumothorax
            consol = row.get("interp::Consolidation", "").strip() == "True"
            lung_point = row.get("interp::Lung point", "").strip() == "True"
            sliding = row.get("interp::Pleura::Sliding", "").strip()
            rockets = row.get("interp::Lung rockets", "").strip() == "True"
            alines = row.get("interp_extra::A-lines", "").strip() == "True"
            is_anterior = (
                (not plaps and consol)
                or lung_point
                or (sliding != "not assessed")
                or (rockets and not plaps)
                or alines
                or pneumothorax
            )
            if not (is_anterior and not is_posterior):
                continue
            cases[row["id"]] = {
                "lung_rockets": rockets,
                "consolidation": consol,
            }
    return cases


def load_posterior_gt(csv_path: Path) -> dict[str, dict]:
    cases = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, quotechar='"')
        for row in reader:
            if row.get("excluded", "").strip():
                continue
            if row.get("pathology", "").strip() == "Pneumothorax":
                continue
            plaps = row.get("interp::PLAPS", "").strip() == "True"
            normal_post = row.get("interp_extra::Normal posterior", "").strip() == "True"
            if not (plaps or normal_post):
                continue
            cases[row["id"]] = {"plaps": plaps}
    return cases


# ─── Metric computation ──────────────────────────────────────────────────────

def compute_multiclass_f1(y_true: list[str], y_pred: list[str], labels: list[str]) -> dict:
    per_class = {}
    for label in labels:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == label and p == label)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t != label and p == label)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == label and p != label)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        per_class[label] = {"precision": precision, "recall": recall, "f1": f1}
    macro_f1 = sum(m["f1"] for m in per_class.values()) / len(labels)
    accuracy = sum(1 for t, p in zip(y_true, y_pred) if t == p) / len(y_true)
    return {"macro_f1": macro_f1, "accuracy": accuracy, "per_class": per_class}


def compute_random_baseline_multiclass(y_true: list[str], labels: list[str], n_bootstrap: int = 1000, seed: int = 42) -> dict:
    """Random baseline: predict at GT class prevalence."""
    import random
    rng = random.Random(seed)
    n = len(y_true)
    weights = [y_true.count(l) / n for l in labels]
    f1_scores = []
    for _ in range(n_bootstrap):
        y_rand = [rng.choices(labels, weights=weights, k=1)[0] for _ in range(n)]
        f1_scores.append(compute_multiclass_f1(y_true, y_rand, labels)["macro_f1"])
    f1_scores.sort()
    return {"f1_mean": sum(f1_scores) / n_bootstrap, "f1_ci": (f1_scores[25], f1_scores[975])}


def compute_random_baseline_binary(y_true: list[bool], n_bootstrap: int = 1000, seed: int = 42) -> dict:
    """Random baseline: predict at GT class prevalence for binary task."""
    import random
    rng = random.Random(seed)
    n = len(y_true)
    p_pos = sum(y_true) / n
    f1_scores = []
    for _ in range(n_bootstrap):
        y_rand = [rng.random() < p_pos for _ in range(n)]
        f1_scores.append(compute_binary_f1(y_true, y_rand)["f1"])
    f1_scores.sort()
    return {"f1_mean": sum(f1_scores) / n_bootstrap, "f1_ci": (f1_scores[25], f1_scores[975])}


def compute_binary_f1(y_true: list[bool], y_pred: list[bool]) -> dict:
    tp = sum(1 for t, p in zip(y_true, y_pred) if t and p)
    tn = sum(1 for t, p in zip(y_true, y_pred) if not t and not p)
    fp = sum(1 for t, p in zip(y_true, y_pred) if not t and p)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t and not p)
    n = len(y_true)
    accuracy = (tp + tn) / n if n else 0.0
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    f1 = 2 * precision * sensitivity / (precision + sensitivity) if (precision + sensitivity) > 0 else 0.0
    return {"f1": f1, "accuracy": accuracy, "sensitivity": sensitivity, "specificity": specificity}


# ─── Run discovery ────────────────────────────────────────────────────────────

def discover_runs(output_dir: Path, task_subdir: str) -> dict[str, list[Path]]:
    """Return {model_id/input_mode: [run_dir, ...]} for old or normalized layouts."""
    task_dir = output_dir / task_subdir
    by_model = defaultdict(list)

    if task_dir.is_dir():
        run_dirs = sorted(task_dir.iterdir())
    else:
        run_dirs = []
        for normalized_task_dir in NORMALIZED_TASK_DIRS.get(task_subdir, ()):
            run_dirs.extend(sorted(output_dir.glob(f"*/{normalized_task_dir}/*")))

    for run_dir in run_dirs:
        meta_file = run_dir / "run_meta.json"
        if not meta_file.is_file():
            continue
        meta = json.loads(meta_file.read_text())
        model_id = meta.get("model_id", "unknown")
        input_mode = meta.get("input_mode", "frames")
        key = f"{model_id} [{input_mode}]"
        by_model[key].append(run_dir)
    return dict(by_model)


# ─── Per-run evaluation ───────────────────────────────────────────────────────

def evaluate_t1_run(run_dir: Path, gt: dict[str, str]) -> dict | None:
    predictions = {}
    for pred_file in sorted(run_dir.rglob("prediction.json")):
        case_id = pred_file.parent.name
        data = json.loads(pred_file.read_text())
        predictions[case_id] = data["pleura_sliding"]
    matched = sorted(set(gt.keys()) & set(predictions.keys()))
    if not matched:
        return None
    y_true = [gt[c] for c in matched]
    y_pred = [predictions[c] for c in matched]
    metrics = compute_multiclass_f1(y_true, y_pred, SLIDING_LABELS)
    metrics["n_cases"] = len(matched)
    return metrics


def evaluate_t2_run(run_dir: Path, gt: dict[str, dict]) -> dict | None:
    predictions = {}
    for pred_file in sorted(run_dir.rglob("prediction.json")):
        case_id = pred_file.parent.name
        data = json.loads(pred_file.read_text())
        predictions[case_id] = data
    matched = sorted(set(gt.keys()) & set(predictions.keys()))
    if not matched:
        return None
    rockets_true = [gt[c]["lung_rockets"] for c in matched]
    rockets_pred = [predictions[c]["lung_rockets"] for c in matched]
    consol_true = [gt[c]["consolidation"] for c in matched]
    consol_pred = [predictions[c]["consolidation"] for c in matched]
    rockets_metrics = compute_binary_f1(rockets_true, rockets_pred)
    consol_metrics = compute_binary_f1(consol_true, consol_pred)
    return {"lung_rockets": rockets_metrics, "consolidation": consol_metrics, "n_cases": len(matched)}


def evaluate_t3_run(run_dir: Path, gt: dict[str, dict]) -> dict | None:
    predictions = {}
    for pred_file in sorted(run_dir.rglob("prediction.json")):
        case_id = pred_file.parent.name
        data = json.loads(pred_file.read_text())
        predictions[case_id] = data
    matched = sorted(set(gt.keys()) & set(predictions.keys()))
    if not matched:
        return None
    plaps_true = [gt[c]["plaps"] for c in matched]
    plaps_pred = [predictions[c]["plaps"] for c in matched]
    plaps_metrics = compute_binary_f1(plaps_true, plaps_pred)
    return {"plaps": plaps_metrics, "n_cases": len(matched)}


# ─── Aggregation ──────────────────────────────────────────────────────────────

def majority_vote(values: list) -> tuple[object | None, int]:
    counts = Counter(values)
    top_count = max(counts.values())
    winners = [value for value, count in counts.items() if count == top_count]
    if len(winners) != 1:
        return None, top_count
    return winners[0], top_count


def summarize_5run_accuracy(
    run_dirs: list[Path],
    gt: dict,
    prediction_getter,
) -> dict | None:
    """Summarize exact-match accuracy across repeated runs.

    pass@1 is the mean single-run accuracy. any_correct is an oracle upper bound:
    a case is correct if at least one repetition predicted the ground truth.
    """
    predictions_by_run = []
    for run_dir in run_dirs:
        predictions = {}
        for pred_file in sorted(run_dir.rglob("prediction.json")):
            case_id = pred_file.parent.name
            data = json.loads(pred_file.read_text())
            predictions[case_id] = prediction_getter(data)
        if predictions:
            predictions_by_run.append(predictions)
    if not predictions_by_run:
        return None

    full_cases = set(gt.keys())
    for predictions in predictions_by_run:
        full_cases &= set(predictions.keys())
    full_cases = sorted(full_cases)
    if not full_cases:
        return None

    per_run_acc = []
    for predictions in predictions_by_run:
        correct = sum(1 for case_id in full_cases if predictions[case_id] == gt[case_id])
        per_run_acc.append(correct / len(full_cases))

    consensus_correct = 0
    consensus_count = 0
    any_correct = 0
    tie_count = 0
    for case_id in full_cases:
        votes = [predictions[case_id] for predictions in predictions_by_run]
        consensus, _top_count = majority_vote(votes)
        if consensus is None:
            tie_count += 1
        else:
            consensus_count += 1
            if consensus == gt[case_id]:
                consensus_correct += 1
        if any(vote == gt[case_id] for vote in votes):
            any_correct += 1

    pass_mean, pass_lo, pass_hi = mean_ci(per_run_acc)
    return {
        "n_runs": len(predictions_by_run),
        "n_cases": len(full_cases),
        "pass_at_1": pass_mean,
        "pass_at_1_ci": (pass_lo, pass_hi),
        "per_run_accuracy": per_run_acc,
        "consensus_accuracy": consensus_correct / len(full_cases),
        "consensus_coverage": consensus_count / len(full_cases),
        "tie_count": tie_count,
        "any_correct_accuracy": any_correct / len(full_cases),
    }


def mean_ci(values: list[float]) -> tuple[float, float, float]:
    """Return (mean, ci_lo, ci_hi) using t-distribution 95% CI."""
    n = len(values)
    if n < 2:
        return (values[0] if values else 0.0, 0.0, 0.0)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / (n - 1)
    se = math.sqrt(variance / n)
    # t critical value for 95% CI with n-1 df (approximation for n>=5)
    t_crit = {2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365,
              8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 15: 2.145, 20: 2.086}
    t = t_crit.get(n, 1.96)  # fallback to z for large n
    return (mean, mean - t * se, mean + t * se)


def print_t1_aggregate(model_id: str, runs_metrics: list[dict], baseline: dict):
    n = len(runs_metrics)
    macro_f1s = [m["macro_f1"] for m in runs_metrics]
    accs = [m["accuracy"] for m in runs_metrics]
    f1_mean, f1_lo, f1_hi = mean_ci(macro_f1s)
    acc_mean, acc_lo, acc_hi = mean_ci(accs)

    print(f"\n### T1 Sliding — {model_id} ({n} runs, {runs_metrics[0]['n_cases']} cases/run)")
    print(f"\nRandom baseline macro F1: {baseline['f1_mean']:.3f} (95% CI: [{baseline['f1_ci'][0]:.3f}, {baseline['f1_ci'][1]:.3f}])\n")
    print(f"| Metric | Mean | 95% CI | Δ vs baseline |")
    print(f"|--------|------|--------|---------------|")
    print(f"| Macro F1 | {f1_mean:.3f} | [{f1_lo:.3f}, {f1_hi:.3f}] | {f1_mean - baseline['f1_mean']:+.3f} |")
    print(f"| Accuracy | {acc_mean:.3f} | [{acc_lo:.3f}, {acc_hi:.3f}] | — |")

    # Per-class breakdown
    for label in SLIDING_LABELS:
        f1s = [m["per_class"][label]["f1"] for m in runs_metrics]
        lmean, llo, lhi = mean_ci(f1s)
        print(f"| F1 ({label}) | {lmean:.3f} | [{llo:.3f}, {lhi:.3f}] | — |")

    print(f"\nPer-run macro F1: {[f'{v:.3f}' for v in macro_f1s]}")


def print_t2_aggregate(model_id: str, runs_metrics: list[dict], baselines: dict):
    n = len(runs_metrics)
    rockets_f1s = [m["lung_rockets"]["f1"] for m in runs_metrics]
    consol_f1s = [m["consolidation"]["f1"] for m in runs_metrics]
    rf1_mean, rf1_lo, rf1_hi = mean_ci(rockets_f1s)
    cf1_mean, cf1_lo, cf1_hi = mean_ci(consol_f1s)

    rb = baselines["lung_rockets"]
    cb = baselines["consolidation"]

    print(f"\n### T2 Anterior — {model_id} ({n} runs, {runs_metrics[0]['n_cases']} cases/run)")
    print(f"\nRandom baselines — Rockets F1: {rb['f1_mean']:.3f} [{rb['f1_ci'][0]:.3f}, {rb['f1_ci'][1]:.3f}], Consolidation F1: {cb['f1_mean']:.3f} [{cb['f1_ci'][0]:.3f}, {cb['f1_ci'][1]:.3f}]\n")
    print(f"| Metric | Mean | 95% CI | Δ vs baseline |")
    print(f"|--------|------|--------|---------------|")
    print(f"| Lung Rockets F1 | {rf1_mean:.3f} | [{rf1_lo:.3f}, {rf1_hi:.3f}] | {rf1_mean - rb['f1_mean']:+.3f} |")
    print(f"| Consolidation F1 | {cf1_mean:.3f} | [{cf1_lo:.3f}, {cf1_hi:.3f}] | {cf1_mean - cb['f1_mean']:+.3f} |")

    # Sensitivity / specificity
    for name, key in [("Lung Rockets", "lung_rockets"), ("Consolidation", "consolidation")]:
        sens = [m[key]["sensitivity"] for m in runs_metrics]
        spec = [m[key]["specificity"] for m in runs_metrics]
        s_mean, s_lo, s_hi = mean_ci(sens)
        sp_mean, sp_lo, sp_hi = mean_ci(spec)
        print(f"| {name} Sens | {s_mean:.3f} | [{s_lo:.3f}, {s_hi:.3f}] | — |")
        print(f"| {name} Spec | {sp_mean:.3f} | [{sp_lo:.3f}, {sp_hi:.3f}] | — |")

    print(f"\nPer-run Rockets F1: {[f'{v:.3f}' for v in rockets_f1s]}")
    print(f"Per-run Consol F1:  {[f'{v:.3f}' for v in consol_f1s]}")


def print_t3_aggregate(model_id: str, runs_metrics: list[dict], baseline: dict):
    n = len(runs_metrics)
    plaps_f1s = [m["plaps"]["f1"] for m in runs_metrics]
    f1_mean, f1_lo, f1_hi = mean_ci(plaps_f1s)

    print(f"\n### T3 Posterior — {model_id} ({n} runs, {runs_metrics[0]['n_cases']} cases/run)")
    print(f"\nRandom baseline PLAPS F1: {baseline['f1_mean']:.3f} [{baseline['f1_ci'][0]:.3f}, {baseline['f1_ci'][1]:.3f}]\n")
    print(f"| Metric | Mean | 95% CI | Δ vs baseline |")
    print(f"|--------|------|--------|---------------|")
    print(f"| PLAPS F1 | {f1_mean:.3f} | [{f1_lo:.3f}, {f1_hi:.3f}] | {f1_mean - baseline['f1_mean']:+.3f} |")

    sens = [m["plaps"]["sensitivity"] for m in runs_metrics]
    spec = [m["plaps"]["specificity"] for m in runs_metrics]
    s_mean, s_lo, s_hi = mean_ci(sens)
    sp_mean, sp_lo, sp_hi = mean_ci(spec)
    print(f"| PLAPS Sens | {s_mean:.3f} | [{s_lo:.3f}, {s_hi:.3f}] | — |")
    print(f"| PLAPS Spec | {sp_mean:.3f} | [{sp_lo:.3f}, {sp_hi:.3f}] | — |")

    print(f"\nPer-run PLAPS F1: {[f'{v:.3f}' for v in plaps_f1s]}")


def print_5run_accuracy_table(title: str, summaries: dict[str, dict]):
    if not summaries:
        return

    print(f"\n### {title}\n")
    print("| Model | Runs | Cases | Pass@1 Acc | 95% CI | Consensus Acc | Consensus Coverage | Any-Correct Acc |")
    print("|-------|------|-------|------------|--------|---------------|--------------------|-----------------|")
    for model_id, summary in sorted(summaries.items()):
        ci_lo, ci_hi = summary["pass_at_1_ci"]
        print(
            f"| {model_id} | {summary['n_runs']} | {summary['n_cases']} | "
            f"{summary['pass_at_1']:.3f} | [{ci_lo:.3f}, {ci_hi:.3f}] | "
            f"{summary['consensus_accuracy']:.3f} | "
            f"{summary['consensus_coverage']:.3f} | "
            f"{summary['any_correct_accuracy']:.3f} |"
        )


def print_5run_accuracy_summary(args):
    print("## Five-Run Accuracy Summary\n")
    print(
        "Pass@1 is the mean single-run exact-match accuracy across repetitions. "
        "Consensus accuracy uses a majority vote across runs; unresolved ties count as incorrect "
        "and reduce consensus coverage. Any-correct accuracy is an oracle upper bound: a case is "
        "counted correct if at least one of the repeated runs got it right, so it should not be "
        "used as a standalone paper performance metric unless the protocol permits repeated attempts.\n"
    )

    if args.task in ("t1", "all"):
        gt_sliding = load_sliding_gt(args.csv_path)
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t1_sliding")
        summaries = {
            model_id: summary
            for model_id, run_dirs in runs_by_model.items()
            if (summary := summarize_5run_accuracy(
                run_dirs,
                gt_sliding,
                lambda data: data["pleura_sliding"],
            ))
        }
        print_5run_accuracy_table("T1 Sliding Exact Match", summaries)

    if args.task in ("t2", "all"):
        gt_anterior = load_anterior_gt(args.csv_path)
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t2_anterior")
        for label, feature_key in [
            ("T2 Lung Rockets", "lung_rockets"),
            ("T2 Consolidation", "consolidation"),
        ]:
            gt_feature = {case_id: values[feature_key] for case_id, values in gt_anterior.items()}
            summaries = {
                model_id: summary
                for model_id, run_dirs in runs_by_model.items()
                if (summary := summarize_5run_accuracy(
                    run_dirs,
                    gt_feature,
                    lambda data, key=feature_key: data[key],
                ))
            }
            print_5run_accuracy_table(label, summaries)

    if args.task in ("t3", "all"):
        gt_posterior = load_posterior_gt(args.csv_path)
        gt_plaps = {case_id: values["plaps"] for case_id, values in gt_posterior.items()}
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t3_posterior")
        summaries = {
            model_id: summary
            for model_id, run_dirs in runs_by_model.items()
            if (summary := summarize_5run_accuracy(
                run_dirs,
                gt_plaps,
                lambda data: data["plaps"],
            ))
        }
        print_5run_accuracy_table("T3 PLAPS", summaries)

    print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Aggregate metrics across benchmark repetitions")
    parser.add_argument("--output-dir", type=Path, default=Path(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--csv-path", type=Path, default=Path(DEFAULT_CSV_PATH))
    parser.add_argument("--task", choices=["t1", "t2", "t3", "all"], default="all")
    args = parser.parse_args()

    assert args.csv_path.is_file(), f"CSV not found: {args.csv_path}"

    print("# Benchmark Aggregation Report\n")
    print_5run_accuracy_summary(args)

    if args.task in ("t1", "all"):
        gt_sliding = load_sliding_gt(args.csv_path)
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t1_sliding")
        if not runs_by_model:
            print("## T1 Sliding\n\nNo runs found.\n")
        else:
            print("## T1 Sliding\n")
            # Compute baseline once from GT
            gt_values = list(gt_sliding.values())
            t1_baseline = compute_random_baseline_multiclass(gt_values, SLIDING_LABELS)
            for model_id, run_dirs in sorted(runs_by_model.items()):
                metrics_list = []
                for rd in run_dirs:
                    m = evaluate_t1_run(rd, gt_sliding)
                    if m:
                        metrics_list.append(m)
                if metrics_list:
                    print_t1_aggregate(model_id, metrics_list, t1_baseline)
                else:
                    print(f"\n### {model_id}: no valid runs")

    if args.task in ("t2", "all"):
        gt_anterior = load_anterior_gt(args.csv_path)
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t2_anterior")
        if not runs_by_model:
            print("\n## T2 Anterior\n\nNo runs found.\n")
        else:
            print("\n## T2 Anterior\n")
            rockets_gt = [v["lung_rockets"] for v in gt_anterior.values()]
            consol_gt = [v["consolidation"] for v in gt_anterior.values()]
            t2_baselines = {
                "lung_rockets": compute_random_baseline_binary(rockets_gt),
                "consolidation": compute_random_baseline_binary(consol_gt),
            }
            for model_id, run_dirs in sorted(runs_by_model.items()):
                metrics_list = []
                for rd in run_dirs:
                    m = evaluate_t2_run(rd, gt_anterior)
                    if m:
                        metrics_list.append(m)
                if metrics_list:
                    print_t2_aggregate(model_id, metrics_list, t2_baselines)
                else:
                    print(f"\n### {model_id}: no valid runs")

    if args.task in ("t3", "all"):
        gt_posterior = load_posterior_gt(args.csv_path)
        runs_by_model = discover_runs(args.output_dir, "pocus_atlas_t3_posterior")
        if not runs_by_model:
            print("\n## T3 Posterior\n\nNo runs found.\n")
        else:
            print("\n## T3 Posterior\n")
            plaps_gt = [v["plaps"] for v in gt_posterior.values()]
            t3_baseline = compute_random_baseline_binary(plaps_gt)
            for model_id, run_dirs in sorted(runs_by_model.items()):
                metrics_list = []
                for rd in run_dirs:
                    m = evaluate_t3_run(rd, gt_posterior)
                    if m:
                        metrics_list.append(m)
                if metrics_list:
                    print_t3_aggregate(model_id, metrics_list, t3_baseline)
                else:
                    print(f"\n### {model_id}: no valid runs")


if __name__ == "__main__":
    main()
