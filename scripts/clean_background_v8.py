#!/usr/bin/env python3
"""
Quita el fondo de v8 FINAL para preparar input limpio para Meshy.

El fondo oceánico oscuro confundió a Meshy v9 (antenas mezcladas con fondo).
Con fondo blanco puro, Meshy detecta mejor las siluetas finas.
"""
from pathlib import Path

from PIL import Image
from rembg import remove, new_session

ROOT = Path(__file__).resolve().parent.parent
SOURCE = (
    ROOT
    / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/auto_generated"
    / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_FINAL.png"
)
OUTPUT_DIR = SOURCE.parent
OUTPUT_TRANSPARENT = OUTPUT_DIR / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_clean_transparent.png"
OUTPUT_WHITE = OUTPUT_DIR / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_clean_white.png"


def main() -> None:
    print(f"[load] {SOURCE.name}")
    src = Image.open(SOURCE).convert("RGBA")
    print(f"  size: {src.size}")

    print("[rembg] removing background (isnet-general-use)")
    session = new_session("isnet-general-use")
    cleaned = remove(src, session=session, alpha_matting=True,
                     alpha_matting_foreground_threshold=240,
                     alpha_matting_background_threshold=10,
                     alpha_matting_erode_size=10)

    cleaned.save(OUTPUT_TRANSPARENT, "PNG")
    print(f"[save] {OUTPUT_TRANSPARENT.name} ({OUTPUT_TRANSPARENT.stat().st_size//1024} KB)")

    white_bg = Image.new("RGBA", cleaned.size, (255, 255, 255, 255))
    composed = Image.alpha_composite(white_bg, cleaned).convert("RGB")
    composed.save(OUTPUT_WHITE, "PNG", optimize=True)
    print(f"[save] {OUTPUT_WHITE.name} ({OUTPUT_WHITE.stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
