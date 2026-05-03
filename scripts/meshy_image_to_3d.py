#!/usr/bin/env python3
"""
Pipeline Meshy AI image-to-3D para Ecuaman.

Toma el master IA-only v8 FINAL como input, lanza un task image-to-3D
en Meshy, hace polling hasta SUCCEEDED, descarga el .glb + texturas y
los guarda en 07_ASSETS_OFICIALES/3d_models/v9_meshy/.

Usa la variable de entorno MESHY_API_KEY.
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
OUTPUT_DIR = ROOT / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/3d_models/v9_meshy"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.meshy.ai/openapi"
API_KEY = os.environ.get("MESHY_API_KEY")
if not API_KEY:
    sys.exit("ERROR: env var MESHY_API_KEY no definida")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def get_balance() -> int:
    r = requests.get(f"{API_BASE}/v1/balance", headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    print(f"[balance] {json.dumps(data)}")
    return data.get("balance", 0)


def public_image_url() -> str:
    """Return the public GitHub raw URL of v8 FINAL on the working branch."""
    branch = os.environ.get("GITHUB_REF_NAME", "claude/ecuaman-sessions-continuation-O3QGo")
    repo = os.environ.get("GITHUB_REPOSITORY", "santycolomar85-star/santi")
    rel = SOURCE_IMAGE.relative_to(ROOT).as_posix()
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{rel}"


def create_task(image_url: str) -> str:
    payload = {
        "image_url": image_url,
        "ai_model": "meshy-5",
        "topology": "quad",
        "target_polycount": 50000,
        "should_remesh": True,
        "should_texture": True,
        "enable_pbr": True,
        "symmetry_mode": "auto",
    }
    print(f"[create] payload: {json.dumps(payload, indent=2)}")
    r = requests.post(
        f"{API_BASE}/v1/image-to-3d",
        headers=HEADERS,
        json=payload,
        timeout=60,
    )
    if r.status_code >= 400:
        print(f"[create] HTTP {r.status_code}: {r.text}")
    r.raise_for_status()
    data = r.json()
    task_id = data.get("result") or data.get("id") or data.get("task_id")
    if not task_id:
        sys.exit(f"ERROR: no task id en respuesta: {data}")
    print(f"[create] task_id = {task_id}")
    return task_id


def poll_task(task_id: str, timeout_s: int = 900) -> dict:
    url = f"{API_BASE}/v1/image-to-3d/{task_id}"
    deadline = time.time() + timeout_s
    last_progress = -1
    while time.time() < deadline:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        data = r.json()
        status = data.get("status") or data.get("state")
        progress = data.get("progress", 0)
        if progress != last_progress:
            print(f"[poll] status={status} progress={progress}%")
            last_progress = progress
        if status == "SUCCEEDED":
            return data
        if status in ("FAILED", "CANCELED", "EXPIRED"):
            sys.exit(f"ERROR: task termino con status {status}: {data.get('task_error')}")
        time.sleep(8)
    sys.exit("ERROR: poll timeout")


def download_artifacts(task: dict) -> None:
    model_urls = task.get("model_urls", {})
    texture_urls = task.get("texture_urls", []) or []
    thumb = task.get("thumbnail_url")

    saved = []
    for fmt, url in model_urls.items():
        if not url:
            continue
        out = OUTPUT_DIR / f"ecuaman_v9_meshy.{fmt}"
        print(f"[download] {fmt} -> {out.name}")
        r = requests.get(url, timeout=180)
        r.raise_for_status()
        out.write_bytes(r.content)
        saved.append(out.name)

    if thumb:
        out = OUTPUT_DIR / "thumbnail.png"
        print(f"[download] thumbnail -> {out.name}")
        r = requests.get(thumb, timeout=60)
        r.raise_for_status()
        out.write_bytes(r.content)
        saved.append(out.name)

    for i, tx in enumerate(texture_urls):
        for k, url in (tx or {}).items():
            if not url:
                continue
            out = OUTPUT_DIR / f"texture_{i}_{k}.png"
            print(f"[download] texture {i}/{k} -> {out.name}")
            r = requests.get(url, timeout=120)
            r.raise_for_status()
            out.write_bytes(r.content)
            saved.append(out.name)

    metadata = OUTPUT_DIR / "task_metadata.json"
    metadata.write_text(json.dumps(task, indent=2))
    saved.append(metadata.name)

    print(f"[done] {len(saved)} archivos guardados en {OUTPUT_DIR.relative_to(ROOT)}")
    for s in saved:
        print(f"  - {s}")


def main() -> None:
    try:
        get_balance()
    except Exception as e:
        print(f"[warn] balance check failed: {e}")

    img_url = public_image_url()
    print(f"[image] {img_url}")

    task_id = create_task(img_url)
    task = poll_task(task_id)
    download_artifacts(task)


if __name__ == "__main__":
    main()
