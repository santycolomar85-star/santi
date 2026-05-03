#!/usr/bin/env python3
"""Compose tricolor Ecuador tassels (yellow-blue-red) on top of v8 FINAL antennae.

This is the deterministic fallback in case gpt-image-1 fails to render the
tassels with the exact tricolor order. Position arguments allow manual
adjustment after visual inspection.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "ECUANUTRITION" / "MARKETING" / "ECUAMAN" / "07_ASSETS_OFICIALES" / "auto_generated"
SOURCE = ASSETS / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_FINAL.png"
OUTPUT = ASSETS / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v9_TASSELS.png"

YELLOW = (255, 221, 0, 255)
BLUE = (0, 56, 147, 255)
RED = (206, 17, 38, 255)
LEATHER = (92, 58, 30, 255)


def draw_tassel(canvas: Image.Image, anchor_x: int, anchor_y: int,
                ribbon_w: int = 22, ribbon_h: int = 70,
                gap: int = 2, mirror: bool = False) -> None:
    """Draw a tricolor flat-ribbon tassel hanging from (anchor_x, anchor_y).

    Order top→bottom: yellow, blue, red. A small leather knot sits at the anchor.
    `mirror=True` flips the slight wave so the right antenna leans the opposite way.
    """
    draw = ImageDraw.Draw(canvas)

    knot_r = max(6, ribbon_w // 3)
    draw.ellipse(
        (anchor_x - knot_r, anchor_y - knot_r,
         anchor_x + knot_r, anchor_y + knot_r),
        fill=LEATHER,
    )

    direction = -1 if mirror else 1
    sway = int(ribbon_w * 0.4) * direction

    colors = [YELLOW, BLUE, RED]
    y = anchor_y + knot_r // 2
    for i, color in enumerate(colors):
        top = y + i * (ribbon_h + gap)
        bottom = top + ribbon_h
        ribbon = [
            (anchor_x - ribbon_w // 2, top),
            (anchor_x + ribbon_w // 2, top),
            (anchor_x + ribbon_w // 2 + sway, bottom),
            (anchor_x - ribbon_w // 2 + sway, bottom),
        ]
        draw.polygon(ribbon, fill=color)

        edge = (max(0, color[0] - 50), max(0, color[1] - 50), max(0, color[2] - 50), 255)
        draw.line(
            (ribbon[0], ribbon[3]),
            fill=edge, width=2,
        )


def erase_old_tassel(canvas: Image.Image, x1: int, y1: int, x2: int, y2: int,
                     bg_color: tuple = (0, 46, 74, 255)) -> None:
    """Paint over an old tassel area with the deep ocean background color."""
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((x1, y1, x2, y2), fill=bg_color)


def composite(source_path: Path, output_path: Path,
              left: tuple[int, int], right: tuple[int, int],
              ribbon_w: int = 38, ribbon_h: int = 110,
              erase_box: tuple[int, int, int, int] | None = None) -> None:
    base = Image.open(source_path).convert("RGBA")

    if erase_box is not None:
        erase_old_tassel(base, *erase_box)

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw_tassel(overlay, left[0], left[1], ribbon_w=ribbon_w, ribbon_h=ribbon_h, mirror=False)
    draw_tassel(overlay, right[0], right[1], ribbon_w=ribbon_w, ribbon_h=ribbon_h, mirror=True)

    composited = Image.alpha_composite(base, overlay)
    composited.convert("RGB").save(output_path, "PNG", optimize=True)
    print(f"v9 tassels saved: {output_path.name} "
          f"({output_path.stat().st_size // 1024} KB)")
    print(f"  ribbon size: {ribbon_w}x{ribbon_h}")
    print(f"  left tassel anchor:  {left}")
    print(f"  right tassel anchor: {right}")
    if erase_box:
        print(f"  erased area: {erase_box}")


if __name__ == "__main__":
    lx = int(sys.argv[1]) if len(sys.argv) > 1 else 215
    ly = int(sys.argv[2]) if len(sys.argv) > 2 else 270
    rx = int(sys.argv[3]) if len(sys.argv) > 3 else 460
    ry = int(sys.argv[4]) if len(sys.argv) > 4 else 90
    rw = int(sys.argv[5]) if len(sys.argv) > 5 else 38
    rh = int(sys.argv[6]) if len(sys.argv) > 6 else 110

    erase = None
    if len(sys.argv) >= 11:
        erase = (int(sys.argv[7]), int(sys.argv[8]),
                 int(sys.argv[9]), int(sys.argv[10]))

    if not SOURCE.exists():
        print(f"ERROR: source not found {SOURCE}")
        sys.exit(1)

    composite(SOURCE, OUTPUT, (lx, ly), (rx, ry), rw, rh, erase)
