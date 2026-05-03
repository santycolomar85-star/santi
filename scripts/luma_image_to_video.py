#!/usr/bin/env python3
"""
Pipeline Luma Dream Machine image-to-video para Ecuaman.

Toma el master IA-only v8 FINAL como keyframe inicial y lo anima con
Ray 2 (mejor calidad). Descarga el .mp4 + thumbnail al repo en
07_ASSETS_OFICIALES/videos/v1_luma/.

Usa la variable de entorno LUMA_API_KEY.
"""
import json
import os
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
SOURCE_IMAGE = (
    ROOT
    / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/auto_generated"
    / "00_DAY0_MASTER_HEROIC_THREEQUARTER_v8_FINAL.png"
)
OUTPUT_DIR = ROOT / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/videos/v1_luma"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.lumalabs.ai/dream-machine/v1"
API_KEY = os.environ.get("LUMA_API_KEY")
if not API_KEY:
    sys.exit("ERROR: env var LUMA_API_KEY no definida")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
}

# Animación heroica para Ecuaman
PROMPT = (
    "ECUAMAN the heroic shrimp mascot, slowly turning his head and smiling "
    "warmly at camera, the cyan plasma trident glowing brighter with energy, "
    "long antennae waving gently in underwater current, royal blue cape "
    "billowing softly behind him, subtle bioluminescent particles floating "
    "around, god rays from above, cinematic Pixar quality, smooth confident "
    "motion, no camera movement, character stays centered, brand mascot reveal."
)

MODEL = os.environ.get("LUMA_MODEL", "ray-2")  # ray-2 (best) | ray-flash-2 (faster)
DURATION = os.environ.get("LUMA_DURATION", "5s")  # 5s | 9s
ASPECT_RATIO = os.environ.get("LUMA_ASPECT", "9:16")  # vertical for socials


def public_image_url() -> str:
    branch = os.environ.get("GITHUB_REF_NAME", "claude/ecuaman-sessions-continuation-O3QGo")
    repo = os.environ.get("GITHUB_REPOSITORY", "santycolomar85-star/santi")
    rel = SOURCE_IMAGE.relative_to(ROOT).as_posix()
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{rel}"


def create_generation(image_url: str) -> str:
    payload = {
        "prompt": PROMPT,
        "model": MODEL,
        "duration": DURATION,
        "aspect_ratio": ASPECT_RATIO,
        "keyframes": {
            "frame0": {"type": "image", "url": image_url}
        },
    }
    print(f"[create] payload:")
    print(json.dumps(payload, indent=2))
    r = requests.post(f"{API_BASE}/generations", headers=HEADERS,
                      json=payload, timeout=60)
    if r.status_code >= 400:
        print(f"[create] HTTP {r.status_code}: {r.text}")
    r.raise_for_status()
    data = r.json()
    gen_id = data.get("id")
    if not gen_id:
        sys.exit(f"ERROR: no generation id en respuesta: {data}")
    print(f"[create] generation_id = {gen_id}")
    return gen_id


def poll_generation(gen_id: str, timeout_s: int = 1200) -> dict:
    url = f"{API_BASE}/generations/{gen_id}"
    deadline = time.time() + timeout_s
    last_state = ""
    while time.time() < deadline:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        data = r.json()
        state = data.get("state", "?")
        if state != last_state:
            print(f"[poll] state={state}")
            last_state = state
        if state == "completed":
            return data
        if state == "failed":
            sys.exit(f"ERROR: generation failed: {data.get('failure_reason')}")
        time.sleep(8)
    sys.exit("ERROR: poll timeout (Luma >20 min)")


def download_video(generation: dict) -> None:
    assets = generation.get("assets") or {}
    video_url = assets.get("video")
    if not video_url:
        sys.exit(f"ERROR: no video URL en respuesta: {generation}")

    out_video = OUTPUT_DIR / "ecuaman_v1_luma.mp4"
    print(f"[download] video -> {out_video.relative_to(ROOT)}")
    r = requests.get(video_url, timeout=300)
    r.raise_for_status()
    out_video.write_bytes(r.content)
    print(f"[download] {out_video.stat().st_size//1024} KB")

    metadata = OUTPUT_DIR / "generation_metadata.json"
    metadata.write_text(json.dumps(generation, indent=2))
    print(f"[done] saved {out_video.name} + metadata")


def main() -> None:
    if not SOURCE_IMAGE.exists():
        sys.exit(f"ERROR: source image not found {SOURCE_IMAGE}")

    img_url = public_image_url()
    print(f"[image] {img_url}")
    print(f"[model] {MODEL}, duration={DURATION}, aspect={ASPECT_RATIO}")

    gen_id = create_generation(img_url)
    generation = poll_generation(gen_id)
    download_video(generation)


if __name__ == "__main__":
    main()
