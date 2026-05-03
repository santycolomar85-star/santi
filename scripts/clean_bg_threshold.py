#!/usr/bin/env python3
"""
Limpiador conservador: solo reemplaza el fondo oceánico (color #002E4A aprox)
por blanco, preservando capa azul real, tridente cian, medallón dorado, etc.

Más adecuado para Meshy que rembg agresivo.
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = (
    ROOT
    / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/auto_generated"
    / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_FINAL.png"
)
OUT_WHITE = SOURCE.parent / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_bgwhite.png"


def main() -> None:
    src = Image.open(SOURCE).convert("RGB")
    arr = np.array(src).astype(np.float32)

    # Background dominant color (ocean blue near 0,46,74 to 0,60,90)
    bg_lo = np.array([0, 25, 50], dtype=np.float32)
    bg_hi = np.array([20, 75, 110], dtype=np.float32)

    bg_mask = np.all((arr >= bg_lo) & (arr <= bg_hi), axis=-1)

    # Edge softening: feather mask 3 px
    bg_mask_uint = (bg_mask.astype(np.uint8)) * 255
    mask_img = Image.fromarray(bg_mask_uint).filter(
        __import__("PIL.ImageFilter", fromlist=["GaussianBlur"]).GaussianBlur(2)
    )
    soft_mask = np.array(mask_img).astype(np.float32) / 255.0

    white = np.ones_like(arr) * 255
    blended = arr * (1 - soft_mask[..., None]) + white * soft_mask[..., None]

    out = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))
    out.save(OUT_WHITE, "PNG", optimize=True)

    pixels_replaced = bg_mask.sum()
    total = bg_mask.size
    print(f"[done] {OUT_WHITE.name} ({OUT_WHITE.stat().st_size//1024} KB)")
    print(f"  background pixels replaced: {pixels_replaced:,} / {total:,} ({100*pixels_replaced/total:.1f}%)")


if __name__ == "__main__":
    main()
