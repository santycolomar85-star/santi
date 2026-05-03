#!/usr/bin/env python3
"""Composite the official Ecuanutrition logo onto the medallion area of v4 master."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "ECUANUTRITION" / "MARKETING" / "ECUAMAN" / "07_ASSETS_OFICIALES" / "auto_generated"
LOGO = ROOT / "ECUANUTRITION" / "MARKETING" / "ECUAMAN" / "03_REFERENCIAS" / "logo_ecuanutrition_oficial" / "ECUANUTRITION_LOGO_OFICIAL.png"
SOURCE = ASSETS / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v4.png"
OUTPUT = ASSETS / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v5.png"


def composite_logo(source_path: Path, logo_path: Path, output_path: Path,
                   center_x: int, center_y: int, diameter: int):
    base = Image.open(source_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    inner_diameter = int(diameter * 0.82)
    logo_resized = logo.resize((inner_diameter, inner_diameter), Image.LANCZOS)

    inner_canvas = Image.new("RGBA", (inner_diameter, inner_diameter), (255, 255, 255, 255))
    inner_canvas = Image.alpha_composite(inner_canvas, logo_resized)

    medallion = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
    draw_med = ImageDraw.Draw(medallion)
    gold_outer = (242, 199, 68, 255)
    gold_inner = (255, 228, 138, 255)

    draw_med.ellipse((0, 0, diameter, diameter), fill=gold_outer)
    ring_thickness = max(4, int(diameter * 0.06))
    draw_med.ellipse(
        (ring_thickness, ring_thickness, diameter - ring_thickness, diameter - ring_thickness),
        fill=gold_inner,
    )

    inner_pad = (diameter - inner_diameter) // 2
    inner_mask = Image.new("L", (inner_diameter, inner_diameter), 0)
    ImageDraw.Draw(inner_mask).ellipse((0, 0, inner_diameter, inner_diameter), fill=255)
    medallion.paste(inner_canvas, (inner_pad, inner_pad), inner_mask)

    full_mask = Image.new("L", (diameter, diameter), 0)
    ImageDraw.Draw(full_mask).ellipse((0, 0, diameter, diameter), fill=255)

    pos_x = center_x - diameter // 2
    pos_y = center_y - diameter // 2

    base.paste(medallion, (pos_x, pos_y), full_mask)

    base.convert("RGB").save(output_path, "PNG", optimize=True)
    print(f"v5 saved: {output_path.name} ({output_path.stat().st_size // 1024} KB)")
    print(f"  base size: {base.size}, medallion at center=({center_x},{center_y}) diameter={diameter}")


if __name__ == "__main__":
    if not SOURCE.exists():
        print(f"ERROR: source not found {SOURCE}")
        sys.exit(1)
    if not LOGO.exists():
        print(f"ERROR: logo not found {LOGO}")
        sys.exit(1)

    cx = int(sys.argv[1]) if len(sys.argv) > 1 else 490
    cy = int(sys.argv[2]) if len(sys.argv) > 2 else 870
    d  = int(sys.argv[3]) if len(sys.argv) > 3 else 130

    composite_logo(SOURCE, LOGO, OUTPUT, cx, cy, d)
