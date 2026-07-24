"""Above-chance permutation test per task (label-shuffle null, z effect size).

Usage:
    python scripts/above_chance_permutation.py \
        --results-dir /path/to/results_normalized \
        --metadata hfdatasets/pocus_atlas/metadata.csv \
        --n-perm 10000 --seed 42 --out manuscript/figures/above_chance_permutation.csv
"""

import argparse
import csv
import json
import random
import statistics
from pathlib import Path

# --- F1 helpers -------------------------------------------------------------

def binary_f1(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t and p)
    fp = sum(1 for t, p in zip(y_true, y_pred) if (not t) and p)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t and (not p))
    denom = 2 * tp + fp + fn
    return (2 * tp / denom) if denom else 0.0


def macro_f1(y_true, y_pred, labels):
    total = 0.0
    for lab in labels:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == lab and p == lab)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t != lab and p == lab)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == lab and p != lab)
        denom = 2 * tp + fp + fn
        total += (2 * tp / denom) if denom else 0.0
    return total / len(labels)


def chance_f1_binary(prevalence):
    """All-positive predictor F1 = 2p/(1+p)."""
    return 2 * prevalence / (1 + prevalence)


def chance_macro_f1_majority(y_true, labels):
    """Macro-F1 of the deterministic majority-class predictor (multi-class chance)."""
    from collections import Counter
    maj = Counter(y_true).most_common(1)[0][0]
    return macro_f1(y_true, [maj] * len(y_true), labels)


# --- Ground-truth derivation (mirrors pipeline *_evaluate.py) ---------------

T1_LABELS = ["present", "absent", "both"]


def load_metadata(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [row for row in csv.DictReader(f, quotechar='"')]


def t1_gt(rows):
    gt = {}
    for row in rows:
        if row.get("excluded", "").strip():
            continue
        s = row.get("interp::Pleura::Sliding", "").strip()
        if s == "not assessed" or s == "":
            continue
        assert s in T1_LABELS
        gt[row["id"]] = s
    return gt


def _is_anterior(row):
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
    return is_anterior and not is_posterior


def t2_gt(rows):
    """Returns {case_id: {'lung_rockets': bool, 'consolidation': bool}}."""
    gt = {}
    for row in rows:
        if row.get("excluded", "").strip():
            continue
        if not _is_anterior(row):
            continue
        gt[row["id"]] = {
            "lung_rockets": row.get("interp::Lung rockets", "").strip() == "True",
            "consolidation": row.get("interp::Consolidation", "").strip() == "True",
        }
    return gt


def t3_gt(rows):
    """Posterior cases; returns {case_id: plaps_bool}."""
    gt = {}
    for row in rows:
        if row.get("excluded", "").strip():
            continue
        plaps = row.get("interp::PLAPS", "").strip() == "True"
        normal_post = row.get("interp_extra::Normal posterior", "").strip() == "True"
        pneumothorax = row.get("pathology", "").strip() == "Pneumothorax"
        is_posterior = (plaps or normal_post) and not pneumothorax
        if not is_posterior:
            continue
        gt[row["id"]] = plaps
    return gt


# --- Prediction loading -----------------------------------------------------

def load_runs(results_dir, model, task_dir, field):
    """Return list of runs; each run is {case_id: prediction_value}."""
    base = Path(results_dir) / model / task_dir
    runs = []
    if not base.exists():
        return runs
    for run in sorted(p for p in base.iterdir() if p.is_dir()):
        preds = {}
        for pf in run.rglob("prediction.json"):
            data = json.loads(pf.read_text())
            if field not in data:
                continue
            preds[pf.parent.name] = data[field]
        if preds:
            runs.append(preds)
    return runs


# --- Permutation test -------------------------------------------------------

def _null_z(obs, null):
    """Standardized effect size: (obs - null mean) / null sd; None if sd == 0."""
    sd = statistics.pstdev(null)
    if sd == 0:
        return None
    return (obs - statistics.mean(null)) / sd

def perm_test_binary(runs, gt_map, n_perm, rng):
    """runs: list of {case:pred_bool}; gt_map: {case:bool}."""
    per_run = []
    for preds in runs:
        cases = [c for c in preds if c in gt_map]
        yt = [gt_map[c] for c in cases]
        yp = [bool(preds[c]) for c in cases]
        per_run.append((yt, yp))
    obs = sum(binary_f1(yt, yp) for yt, yp in per_run) / len(per_run)
    null = []
    for _ in range(n_perm):
        tot = 0.0
        for yt, yp in per_run:
            shuffled = yt[:]
            rng.shuffle(shuffled)
            tot += binary_f1(shuffled, yp)
        null.append(tot / len(per_run))
    return obs, _null_z(obs, null)


def perm_test_multiclass(runs, gt_map, labels, n_perm, rng):
    per_run = []
    for preds in runs:
        cases = [c for c in preds if c in gt_map]
        yt = [gt_map[c] for c in cases]
        yp = [preds[c] for c in cases]
        per_run.append((yt, yp))
    obs = sum(macro_f1(yt, yp, labels) for yt, yp in per_run) / len(per_run)
    null = []
    for _ in range(n_perm):
        tot = 0.0
        for yt, yp in per_run:
            shuffled = yt[:]
            rng.shuffle(shuffled)
            tot += macro_f1(shuffled, yp, labels)
        null.append(tot / len(per_run))
    return obs, _null_z(obs, null)


# --- Best-model selection ---------------------------------------------------

def best_model_binary(results_dir, models, task_dir, field, gt_map):
    # Ties (e.g. T3 all-positive) break by iteration order; immaterial to the verdict.
    best, best_f1 = None, -1.0
    for model in models:
        runs = load_runs(results_dir, model, task_dir, field)
        if not runs:
            continue
        f1s = []
        for preds in runs:
            cases = [c for c in preds if c in gt_map]
            f1s.append(binary_f1([gt_map[c] for c in cases], [bool(preds[c]) for c in cases]))
        mean = sum(f1s) / len(f1s)
        if mean > best_f1:
            best, best_f1 = model, mean
    return best


def best_model_t2(results_dir, models, gt_map, finding):
    best, best_f1 = None, -1.0
    for model in models:
        runs = load_runs(results_dir, model, "t2_anterior_frames", finding)
        if not runs:
            continue
        f1s = []
        for preds in runs:
            cases = [c for c in preds if c in gt_map]
            f1s.append(binary_f1([gt_map[c][finding] for c in cases], [bool(preds[c]) for c in cases]))
        mean = sum(f1s) / len(f1s)
        if mean > best_f1:
            best, best_f1 = model, mean
    return best


def best_model_t1(results_dir, models, task_dir, gt_map):
    best, best_f1 = None, -1.0
    for model in models:
        runs = load_runs(results_dir, model, task_dir, "pleura_sliding")
        if not runs:
            continue
        f1s = []
        for preds in runs:
            cases = [c for c in preds if c in gt_map]
            f1s.append(macro_f1([gt_map[c] for c in cases], [preds[c] for c in cases], T1_LABELS))
        mean = sum(f1s) / len(f1s)
        if mean > best_f1:
            best, best_f1 = model, mean
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results-dir", required=True)
    ap.add_argument("--metadata", required=True)
    ap.add_argument("--n-perm", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    rows = load_metadata(args.metadata)
    models = sorted(p.name for p in Path(args.results_dir).iterdir() if p.is_dir())

    gt1 = t1_gt(rows)
    gt2 = t2_gt(rows)
    gt3 = t3_gt(rows)

    prev = {
        "T2 B-lines": sum(v["lung_rockets"] for v in gt2.values()) / len(gt2),
        "T2 Consolidation": sum(v["consolidation"] for v in gt2.values()) / len(gt2),
        "T3 PLAPS": sum(gt3.values()) / len(gt3),
    }

    results = []
    rng = random.Random(args.seed)

    # T1 frames + mmode (multiclass); chance = majority-class predictor macro-F1
    t1_chance = chance_macro_f1_majority(list(gt1.values()), T1_LABELS)
    for label, task_dir in [("T1 Frames", "t1_sliding_frames"), ("T1 M-mode", "t1_sliding_mmode")]:
        bm = best_model_t1(args.results_dir, models, task_dir, gt1)
        runs = load_runs(args.results_dir, bm, task_dir, "pleura_sliding")
        obs, z = perm_test_multiclass(runs, gt1, T1_LABELS, args.n_perm, rng)
        results.append({"task": label, "best_model": bm, "metric": "macro-F1",
                        "observed_f1": obs, "chance_f1": t1_chance, "n_runs": len(runs),
                        "z_null": z})

    # T2 rockets + consolidation (binary)
    for label, finding in [("T2 B-lines", "lung_rockets"), ("T2 Consolidation", "consolidation")]:
        gt_bin = {c: v[finding] for c, v in gt2.items()}
        bm = best_model_t2(args.results_dir, models, gt2, finding)
        runs = load_runs(args.results_dir, bm, "t2_anterior_frames", finding)
        obs, z = perm_test_binary(runs, gt_bin, args.n_perm, rng)
        results.append({"task": label, "best_model": bm, "metric": "binary-F1",
                        "observed_f1": obs, "chance_f1": chance_f1_binary(prev[label]),
                        "n_runs": len(runs), "z_null": z})

    # T3 PLAPS (binary)
    bm = best_model_binary(args.results_dir, models, "t3_posterior_frames", "plaps", gt3)
    runs = load_runs(args.results_dir, bm, "t3_posterior_frames", "plaps")
    obs, z = perm_test_binary(runs, gt3, args.n_perm, rng)
    results.append({"task": "T3 PLAPS", "best_model": bm, "metric": "binary-F1",
                    "observed_f1": obs, "chance_f1": chance_f1_binary(prev["T3 PLAPS"]),
                    "n_runs": len(runs), "z_null": z})

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["task", "best_model", "metric", "n_runs",
                                          "observed_f1", "chance_f1", "z_null"])
        w.writeheader()
        for r in results:
            w.writerow({k: r[k] for k in w.fieldnames})

    for r in results:
        cf = f"{r['chance_f1']:.3f}" if r["chance_f1"] != "" else "n/a"
        zf = f"{r['z_null']:.1f}" if r["z_null"] is not None else "n/a"
        print(f"{r['task']:18} {r['best_model']:20} F1={r['observed_f1']:.3f} "
              f"chance={cf} z={zf}")


if __name__ == "__main__":
    main()
