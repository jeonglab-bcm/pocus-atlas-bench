"""Regenerate Figure 1 panel (d): per-run F1 vs. permutation-chance baseline.

Figure 1 in the manuscript is a 2x2 composite. Only panel (d) is data-driven;
panels (a)-(c) are illustrative/schematic image assets built from notebooks that
are outside this reproducibility release. This script regenerates panel (d) as a
standalone figure directly from the two shipped CSVs, so the quantitative content
of Figure 1 is reproducible here.

Inputs (both shipped in this repo):
  manuscript/figures/benchmark_barplot_t1_t2_t3_values_ci.csv  (per-run F1)
  manuscript/figures/above_chance_permutation.csv              (chance F1 + z)

Run:
  python -m scripts.fig1d_results_summary

Outputs:
  manuscript/figures/qmd/fig1d_results_summary.png   (600 dpi raster)
  manuscript/figures/fig1d_results_summary.pdf       (vector sibling)
"""
from __future__ import annotations

import random
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / "manuscript" / "figures"
QMD = FIGS / "qmd"
OUT_PNG = QMD / "fig1d_results_summary.png"
OUT_PDF = FIGS / "fig1d_results_summary.pdf"

INK = "#1a1a1a"

# Four task rows, top-to-bottom, matching the composite Figure 1 layout.
ROW_TOP = 0.90
ROW_H = 0.155
ROW_YS = [ROW_TOP - i * ROW_H for i in range(4)]
AXIS_Y = ROW_YS[-1] - 0.06

# (row label -> per-run F1 panels + chance keys); T1 holds Frames + M-mode.
ROWS = [
    ("T1 Sliding", [("T1 Frames — Pleura Sliding Macro F1", "T1 Frames", "o"),
                    ("T1 M-mode — Pleura Sliding Macro F1", "T1 M-mode", "^")]),
    ("T2 B-lines", [("T2-1 Lung Rockets — F1", "T2 B-lines", "o")]),
    ("T2 Consol.", [("T2-2 Consolidation — F1", "T2 Consolidation", "o")]),
    ("T3 PLAPS", [("T3 PLAPS — F1", "T3 PLAPS", "o")]),
]
# Colorblind-safe; mirrors scripts/plot_benchmark_publiplots.py MODEL_COLORS.
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
MODEL_LABEL = {
    "claude_opus-4.6": "Claude Opus 4.6", "claude_sonnet-4.6": "Claude Sonnet 4.6",
    "gemma-4-12b": "Gemma 4 12B", "gemma-4-26b-a4b-it": "Gemma 4 26B",
    "gemma-4-31b-it": "Gemma 4 31B", "gemma-4-e4e": "Gemma 4 E4B",
    "medgemma-27b": "MedGemma 27B", "qwen3.6-35b-a3b": "Qwen 3.6 35B",
}


def draw_results_summary(ax):
    """Horizontal per-run F1 jitter with a per-task permutation chance line.
    Each dot is one model-run; the dashed line is the label-shuffle chance F1."""
    f1 = pd.read_csv(FIGS / "benchmark_barplot_t1_t2_t3_values_ci.csv")
    ch = pd.read_csv(FIGS / "above_chance_permutation.csv").set_index("task")

    models = sorted(f1["model"].unique())
    model_color = {m: MODEL_COLORS.get(m, "#888888") for m in models}
    rng = random.Random(42)
    ax.set_xlim(0, 1.22)
    ax.set_ylim(0.16, 1)
    band = ROW_H * 0.34
    for (label, panels), yc in zip(ROWS, ROW_YS):
        for panel, chkey, marker in panels:
            sub = f1[f1["panel"] == panel]
            for _, r in sub.iterrows():
                col = model_color[r["model"]]
                for x in str(r["per_run_f1"]).split(";"):
                    jy = yc + rng.uniform(-band, band)
                    ax.scatter(float(x), jy, s=11, color=col, alpha=0.7,
                               marker=marker, edgecolors="none", zorder=3)
        chance_vals = []
        for _, chkey, _m in panels:
            if chkey in ch.index:
                chance_vals.append(float(ch.loc[chkey, "chance_f1"]))
        for cval in sorted(set(round(c, 3) for c in chance_vals)):
            ax.plot([cval, cval], [yc - band * 1.25, yc + band * 1.25], ls="--",
                    lw=2.0, color="#c0392b", zorder=6, solid_capstyle="butt",
                    path_effects=[pe.Stroke(linewidth=4.0, foreground="white"),
                                  pe.Normal()])
        zs = [float(ch.loc[chkey, "z_null"]) for _, chkey, _m in panels
              if chkey in ch.index]
        finite = [z for z in zs if z == z]
        if not finite:
            ztxt = "z n/a"
        elif len(finite) > 1 and (max(finite) - min(finite) >= 0.5):
            ztxt = f"z={min(finite):.1f}\u2013{max(finite):.1f}"
        else:
            ztxt = f"z={sum(finite)/len(finite):.1f}"
        ax.text(1.05, yc, ztxt, ha="left", va="center", fontsize=8,
                color="#c0392b" if not finite else INK,
                fontstyle="italic" if not finite else "normal")
        ax.text(-0.01, yc, label, ha="right", va="center", fontsize=9,
                color=INK, transform=ax.transData)
    ax.text(1.05, ROW_TOP + ROW_H * 0.55, "above-chance", ha="left", va="bottom",
            fontsize=7, color=INK, fontstyle="italic")
    ax.set_yticks([])
    ax.set_xlabel("Macro / binary F1", fontsize=8.0)
    ax.spines["bottom"].set_position(("data", AXIS_Y))
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    model_handles = [Line2D([], [], marker="o", ls="", ms=5,
                            color=model_color[m], label=MODEL_LABEL.get(m, m))
                     for m in models]
    marker_handles = [
        Line2D([], [], marker="o", ls="", ms=5, color="#555", label="T1 Frames / T2 / T3"),
        Line2D([], [], marker="^", ls="", ms=5, color="#555", label="T1 M-mode"),
        Line2D([], [], ls="--", color="#c0392b", label="chance"),
    ]
    leg1 = ax.legend(handles=model_handles, loc="upper left", fontsize=6.5,
                     frameon=False, ncol=2, columnspacing=0.8, handletextpad=0.3,
                     bbox_to_anchor=(0.0, 0.14))
    ax.add_artist(leg1)
    ax.legend(handles=marker_handles, loc="upper right", fontsize=6.5,
              frameon=False, ncol=1, handletextpad=0.3,
              bbox_to_anchor=(1.0, 0.14))


def main():
    plt.rcParams["font.family"] = "DejaVu Sans"
    fig = plt.figure(figsize=(6.0, 4.5), dpi=200)
    ax = fig.add_subplot(1, 1, 1)
    draw_results_summary(ax)
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=600, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT_PDF, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", OUT_PNG)
    print("wrote", OUT_PDF)


if __name__ == "__main__":
    main()
