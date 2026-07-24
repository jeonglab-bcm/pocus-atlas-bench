"""Classify PLAPS-positive POCUS Atlas cases by underlying finding.

Reproduces the PLAPS-composition table used in Methods/Limitations: of the
PLAPS-positive cases (same filter as the T3 pipeline), how many carry
effusion evidence, consolidation evidence, both, or neither, from the curated
annotation fields (title + tags + categories). This is annotation-derived, not
a measured acquisition site, and is documented as a limitation.

Usage:
    uv run python scripts/plaps_composition.py [--csv hfdatasets/pocus_atlas/metadata.csv]
"""

import argparse
import csv
import re
from pathlib import Path

# Curated fields matched (body excluded, consistent with the annotation pipeline).
CURATED_FIELDS = ("title", "tags", "categories")

CONSOLIDATION_RE = re.compile(
    r"consolidat|hepatiz|shred|air[\s-]?bronchogram", re.IGNORECASE
)
EFFUSION_RE = re.compile(
    r"effusion|empyema|hemothorax|pleural[\s-]?fluid|loculat", re.IGNORECASE
)


def curated_text(row: dict) -> str:
    return " ".join((row.get(f) or "") for f in CURATED_FIELDS)


def load_plaps_positive(csv_path: Path) -> list[dict]:
    """PLAPS-positive cases using the same filter as the T3 pipeline."""
    cases = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, quotechar='"'):
            if row.get("excluded", "").strip():
                continue
            if row.get("pathology", "").strip() == "Pneumothorax":
                continue
            if row.get("interp::PLAPS", "").strip() != "True":
                continue
            cases.append(row)
    return cases


def classify(row: dict) -> str:
    text = curated_text(row)
    # Structured consolidation tag counts as consolidation evidence.
    has_cons = row.get("interp::Consolidation", "").strip() == "True" or bool(
        CONSOLIDATION_RE.search(text)
    )
    has_eff = bool(EFFUSION_RE.search(text))
    if has_cons and has_eff:
        return "both"
    if has_cons:
        return "consolidation_only"
    if has_eff:
        return "effusion_only"
    return "other"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--csv",
        type=Path,
        default=Path("hfdatasets/pocus_atlas/metadata.csv"),
    )
    args = ap.parse_args()

    cases = load_plaps_positive(args.csv)
    counts = {"effusion_only": 0, "consolidation_only": 0, "both": 0, "other": 0}
    other_ids = []
    for row in cases:
        label = classify(row)
        counts[label] += 1
        if label == "other":
            other_ids.append(row.get("id", "?"))

    total = len(cases)
    assert total > 0, "no PLAPS-positive cases found"

    def pct(n: int) -> str:
        return f"{round(100 * n / total)}%"

    any_cons = counts["consolidation_only"] + counts["both"]
    print(f"PLAPS-positive total: {total}")
    print(f"  Effusion only         : {counts['effusion_only']:>2}  ({pct(counts['effusion_only'])})")
    print(f"  Consolidation only    : {counts['consolidation_only']:>2}  ({pct(counts['consolidation_only'])})")
    print(f"  Both effusion + cons. : {counts['both']:>2}  ({pct(counts['both'])})")
    print(f"  Other / undetermined  : {counts['other']:>2}  ({pct(counts['other'])})")
    print(f"  Any consolidation     : {any_cons} ({pct(any_cons)}); pure posterolateral consolidation: {counts['consolidation_only']}")
    if other_ids:
        print(f"  Other case ids        : {', '.join(other_ids)}")


if __name__ == "__main__":
    main()
