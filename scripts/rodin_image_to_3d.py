#!/usr/bin/env python3
"""
Pipeline Hyper3D Rodin Gen-2 image-to-3D para Ecuaman.

Toma el master IA-only v8 FINAL como input, lanza un task image-to-3D
en Rodin (Gen-2 con calidad alta + PBR), hace polling hasta SUCCEEDED,
descarga el .glb + texturas y los guarda en
07_ASSETS_OFICIALES/3d_models/v9_rodin/.

Usa la variable de entorno RODIN_API_KEY.
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
OUTPUT_DIR = ROOT / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/3d_models/v9_rodin"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.hyper3d.com/api/v2"
API_KEY = os.environ.get("RODIN_API_KEY")
if not API_KEY:
    sys.exit("ERROR: env var RODIN_API_KEY no definida")

HEADERS_BEARER = {"Authorization": f"Bearer {API_KEY}"}

PROMPT = (
    "ECUAMAN, official superhero mascot of Ecuanutrition. "
    "Anthropomorphic Penaeus vannamei whiteleg shrimp character with: "
    "muscular humanoid orange torso fused with segmented chitin cephalothorax, "
    "six clearly visible abdominal segments curving down into a fan tail "
    "(telson plus uropods), serrated rostrum beak with small dorsal teeth, "
    "two long antennae, two short bifurcated antennules, pedunculated eyes, "
    "small lateral pereiopod legs (no large pincers), royal blue cape, "
    "electric blue belt with the word ECUAMAN in geometric bold sans-serif, "
    "gold-bordered medallion with the corporate Ecuanutrition E logo, "
    "cyan plasma trident in his right hand, friendly proud smile. "
    "Pixar DreamWorks 3D semi-realistic mascot style, anatomically respectful "
    "of Penaeus vannamei."
)


def submit_task(image_path: Path) -> dict:
    files = {"images": (image_path.name, image_path.open("rb"), "image/png")}
    data = {
        "tier": "Gen-2",
        "prompt": PROMPT,
        "mesh_mode": "Raw",
        "material": "PBR",
        "quality_override": "50000",
    }
    print(f"[submit] image={image_path.name} tier=Gen-2 PBR 50k poly")
    r = requests.post(f"{API_BASE}/rodin", headers=HEADERS_BEARER,
                      files=files, data=data, timeout=120)
    if r.status_code >= 400:
        print(f"[submit] HTTP {r.status_code}: {r.text}")
    r.raise_for_status()
    payload = r.json()
    print(f"[submit] response: {json.dumps(payload, indent=2)[:600]}")
    if payload.get("error"):
        sys.exit(f"ERROR Rodin: {payload['error']}")
    return payload


def poll_status(subscription_key: str, timeout_s: int = 1200) -> dict:
    """Poll the status endpoint until job completes."""
    url = f"{API_BASE}/status"
    deadline = time.time() + timeout_s
    last_status = ""
    while time.time() < deadline:
        r = requests.post(url, headers=HEADERS_BEARER,
                          json={"subscription_key": subscription_key},
                          timeout=30)
        if r.status_code >= 400:
            print(f"[poll] HTTP {r.status_code}: {r.text}")
            time.sleep(10)
            continue
        data = r.json()
        jobs = data.get("jobs", [])
        statuses = [j.get("status", "?") for j in jobs]
        snapshot = ",".join(statuses)
        if snapshot != last_status:
            print(f"[poll] jobs: {snapshot}")
            last_status = snapshot
        if jobs and all(s == "Done" for s in statuses):
            return data
        if any(s == "Failed" for s in statuses):
            sys.exit(f"ERROR jobs failed: {data}")
        time.sleep(10)
    sys.exit("ERROR: poll timeout")


def download_assets(task_uuid: str) -> None:
    url = f"{API_BASE}/download"
    r = requests.post(url, headers=HEADERS_BEARER,
                      json={"task_uuid": task_uuid}, timeout=60)
    if r.status_code >= 400:
        print(f"[download] HTTP {r.status_code}: {r.text}")
    r.raise_for_status()
    data = r.json()
    print(f"[download] response: {json.dumps(data, indent=2)[:500]}")

    items = data.get("list", []) or data.get("items", [])
    saved = []
    for item in items:
        name = item.get("name") or item.get("filename") or "asset.bin"
        link = item.get("url") or item.get("download_url")
        if not link:
            continue
        out = OUTPUT_DIR / name
        print(f"[download] {name} -> {out.relative_to(ROOT)}")
        rr = requests.get(link, timeout=300)
        rr.raise_for_status()
        out.write_bytes(rr.content)
        saved.append(name)

    metadata = OUTPUT_DIR / "task_metadata.json"
    metadata.write_text(json.dumps({"task_uuid": task_uuid,
                                    "download_response": data}, indent=2))
    print(f"\n[done] {len(saved)} archivos guardados en {OUTPUT_DIR.relative_to(ROOT)}")


def main() -> None:
    if not SOURCE_IMAGE.exists():
        sys.exit(f"ERROR: source not found {SOURCE_IMAGE}")

    submission = submit_task(SOURCE_IMAGE)
    sub_key = submission.get("jobs", {}).get("subscription_key") if isinstance(submission.get("jobs"), dict) else None
    if not sub_key and isinstance(submission.get("jobs"), list) and submission["jobs"]:
        sub_key = submission["jobs"][0].get("subscription_key")
    task_uuid = submission.get("uuid")

    if not sub_key or not task_uuid:
        sys.exit(f"ERROR: respuesta sin subscription_key o uuid: {submission}")

    print(f"[task] uuid={task_uuid}, sub_key={sub_key[:10]}...")

    poll_status(sub_key)
    download_assets(task_uuid)


if __name__ == "__main__":
    main()
