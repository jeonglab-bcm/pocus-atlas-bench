"""Vertically stack pairs of figure PNGs into single combined panels.

Reads figure pairs from `manuscript/figures/qmd/` and writes combined panels with
a/b sub-labels in the top-left corner of each sub-panel. The combined files are
used by `manuscript/results/0[12]-*.qmd` to avoid DOCX layout-ncol cropping of
wide images.

Run after regenerating figures:

    uv run python scripts/combine_panel_pngs.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FIGS = ROOT / "manuscript" / "figures" / "qmd"

PAIRS: list[tuple[str, str, str]] = [
    ("barplot_t1_frames_f1.png",       "barplot_t1_mmode_f1.png",       "barplot_t1_combined_f1.png"),
    ("confusion_t1_frames.png",        "confusion_t1_mmode.png",        "confusion_t1_combined.png"),
    ("barplot_t2_1_rockets_f1.png",    "barplot_t2_2_consolidation_f1.png", "barplot_t2_combined_f1.png"),
    ("confusion_t2_1.png",             "confusion_t2_2.png",             "confusion_t2_combined.png"),
]

LABEL_FONT_SIZE = 48
LABEL_PADDING = 24
GAP = 30
BG = (255, 255, 255)


def _load_font() -> ImageFont.ImageFont:
    candidates = [
        # Arial/Helvetica metric-compatible (Nature convention) first, DejaVu fallback.
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, LABEL_FONT_SIZE)
    return ImageFont.load_default()


def _draw_label(im: Image.Image, letter: str, font: ImageFont.ImageFont) -> Image.Image:
    out = im.copy()
    draw = ImageDraw.Draw(out)
    draw.text((LABEL_PADDING, LABEL_PADDING), letter, fill=(0, 0, 0), font=font)
    return out


def _vstack(top: Image.Image, bottom: Image.Image, gap: int = GAP) -> Image.Image:
    width = max(top.width, bottom.width)
    height = top.height + gap + bottom.height
    canvas = Image.new("RGB", (width, height), BG)
    canvas.paste(top, ((width - top.width) // 2, 0))
    canvas.paste(bottom, ((width - bottom.width) // 2, top.height + gap))
    return canvas


def main() -> None:
    font = _load_font()
    for top_name, bottom_name, out_name in PAIRS:
        top_path = FIGS / top_name
        bottom_path = FIGS / bottom_name
        out_path = FIGS / out_name
        assert top_path.exists(), f"missing input: {top_path}"
        assert bottom_path.exists(), f"missing input: {bottom_path}"
        top = _draw_label(Image.open(top_path).convert("RGB"), "a", font)
        bottom = _draw_label(Image.open(bottom_path).convert("RGB"), "b", font)
        combined = _vstack(top, bottom)
        # Preserve the input DPI so DOCX scales the combined image the same way.
        dpi = Image.open(top_path).info.get("dpi", (200, 200))
        combined.save(out_path, dpi=dpi)
        print(f"wrote {out_path.relative_to(ROOT)} ({combined.width}x{combined.height})")


if __name__ == "__main__":
    main()
