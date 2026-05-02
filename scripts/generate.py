#!/usr/bin/env python3
"""Generate Ecuaman images via DALL-E 3 HD from JSON manifests."""
import os, json, time, sys
from pathlib import Path
from openai import OpenAI
import requests

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT / "scripts" / "prompts"
OUTPUT_DIR = ROOT / "ECUANUTRITION" / "MARKETING" / "ECUAMAN" / "07_ASSETS_OFICIALES" / "auto_generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = ROOT / "scripts" / "generation_log.json"

_k = os.environ.get("OPENAI_API_KEY", "")
print(f"[DEBUG] OPENAI_API_KEY length={len(_k)} prefix={_k[:8]} suffix={_k[-4:] if len(_k) >= 4 else 'N/A'}")
client = OpenAI()

# Load manifests
items = []
for f in sorted(PROMPTS_DIR.glob("*.json")):
    with open(f) as fp:
        data = json.load(fp)
    if isinstance(data, list):
        items.extend(data)
    else:
        items.append(data)

print(f"Loaded {len(items)} prompts to process")

# Load existing log to skip already-generated
existing_log = []
if LOG_FILE.exists():
    with open(LOG_FILE) as fp:
        existing_log = json.load(fp)
done_ids = {e["id"] for e in existing_log if e.get("status") == "ok"}

new_log = list(existing_log)
generated_count = 0

for item in items:
    if item["id"] in done_ids:
        print(f"  [skip] {item['id']} (already generated)")
        continue

    out_file = OUTPUT_DIR / f"{item['id']}.png"
    if out_file.exists():
        print(f"  [skip] {item['id']} (file exists)")
        continue

    print(f"  [gen]  {item['id']}: {item.get('description', '')[:60]}...")
    try:
        model = item.get("model", "gpt-image-1")
        kwargs = {"model": model, "prompt": item["prompt"], "size": item.get("size", "1024x1024"), "n": 1}
        if model == "dall-e-3":
            kwargs["quality"] = item.get("quality", "hd")
        else:
            kwargs["quality"] = item.get("quality", "high")
        ref_image = item.get("reference_image")
        if ref_image:
            ref_path = ROOT / ref_image
            with open(ref_path, "rb") as imgf:
                resp = client.images.edit(model=model, image=imgf, prompt=item["prompt"],
                                          size=item.get("size", "1024x1024"),
                                          quality=item.get("quality", "high"), n=1)
        else:
            resp = client.images.generate(**kwargs)
        d = resp.data[0]
        revised = getattr(d, "revised_prompt", None) or ""
        if getattr(d, "b64_json", None):
            import base64
            img_data = base64.b64decode(d.b64_json)
        else:
            img_data = requests.get(d.url, timeout=60).content

        with open(out_file, "wb") as fp:
            fp.write(img_data)

        print(f"         saved {out_file.name} ({len(img_data)/1024:.0f} KB)")
        new_log.append({
            "id": item["id"],
            "status": "ok",
            "file": str(out_file.relative_to(ROOT)),
            "size": item.get("size", "1024x1024"),
            "quality": item.get("quality", "hd"),
            "revised_prompt": revised[:500],
            "timestamp": time.time(),
        })
        generated_count += 1
        time.sleep(2)
    except Exception as e:
        err_msg = str(e)[:300]
        print(f"         ERROR: {err_msg}")
        new_log.append({
            "id": item["id"],
            "status": "error",
            "error": err_msg,
            "timestamp": time.time(),
        })

with open(LOG_FILE, "w") as fp:
    json.dump(new_log, fp, indent=2)

print(f"\nGenerated {generated_count} new images")
print(f"Log written to {LOG_FILE}")
