#!/usr/bin/env python3
"""
Render multi-angle screenshots of the Meshy v9 .glb without OpenGL.

Uses trimesh's built-in matplotlib path fallback (line drawing) since
pyrender / OpenGL isn't available in this sandbox. Output is silhouette
+ wireframe-style multiview that lets us audit the geometry shape from
6 standard orientations.
"""
from pathlib import Path

import numpy as np
import trimesh
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
import os
MODEL_DIR_NAME = os.environ.get("MODEL_DIR", "v10_meshy")
MODEL_FILE = os.environ.get("MODEL_FILE", f"ecuaman_{MODEL_DIR_NAME.split('_')[0]}_meshy.glb")
MODEL = (
    ROOT
    / "ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/3d_models"
    / MODEL_DIR_NAME
    / MODEL_FILE
)
OUT_DIR = MODEL.parent / "renders"
OUT_DIR.mkdir(exist_ok=True)


def project(points: np.ndarray, axis: str) -> np.ndarray:
    """Orthographic projection of 3D points to 2D depending on view axis."""
    if axis == "front":
        return points[:, [0, 1]] * np.array([1, -1])
    if axis == "back":
        return points[:, [0, 1]] * np.array([-1, -1])
    if axis == "right":
        return points[:, [2, 1]] * np.array([1, -1])
    if axis == "left":
        return points[:, [2, 1]] * np.array([-1, -1])
    if axis == "top":
        return points[:, [0, 2]] * np.array([1, 1])
    if axis == "bottom":
        return points[:, [0, 2]] * np.array([1, -1])
    raise ValueError(axis)


VIEW_DIR = {
    "front":  np.array([0, 0,  1.0]),
    "back":   np.array([0, 0, -1.0]),
    "right":  np.array([ 1.0, 0, 0]),
    "left":   np.array([-1.0, 0, 0]),
    "top":    np.array([0,  1.0, 0]),
    "bottom": np.array([0, -1.0, 0]),
}

LIGHT_DIR = np.array([0.5, 0.7, 0.8])
LIGHT_DIR = LIGHT_DIR / np.linalg.norm(LIGHT_DIR)


def render_view(mesh: trimesh.Trimesh, axis: str, size: int = 800,
                bg=(11, 30, 63), base=(255, 162, 43)) -> Image.Image:
    """Lambert-shaded orthographic view, painters algorithm, full mesh."""
    pts = project(mesh.vertices, axis)
    pmin = pts.min(0)
    pmax = pts.max(0)
    span = (pmax - pmin).max()
    pad = span * 0.08
    scale = (size - 2 * pad) / span
    pts2 = (pts - pmin) * scale + pad

    img = Image.new("RGB", (size, size), bg)
    draw = ImageDraw.Draw(img, "RGB")

    faces = mesh.faces
    normals = mesh.face_normals

    # Cull back-facing
    view_dir = VIEW_DIR[axis]
    n_dot_v = normals @ view_dir
    visible = n_dot_v > 0

    # Painter sort by depth along view axis
    if axis == "front":
        depth = mesh.vertices[:, 2]
        sign = -1
    elif axis == "back":
        depth = mesh.vertices[:, 2]
        sign = 1
    elif axis == "right":
        depth = mesh.vertices[:, 0]
        sign = -1
    elif axis == "left":
        depth = mesh.vertices[:, 0]
        sign = 1
    elif axis == "top":
        depth = mesh.vertices[:, 1]
        sign = -1
    else:  # bottom
        depth = mesh.vertices[:, 1]
        sign = 1

    face_depth = depth[faces].mean(axis=1) * sign
    visible_idx = np.where(visible)[0]
    order = visible_idx[np.argsort(-face_depth[visible_idx])]

    p2 = pts2.astype(int)

    # Lambert shade per face (clamped)
    light = np.clip(normals @ LIGHT_DIR, 0, 1)
    ambient = 0.30

    for fi in order:
        intensity = ambient + (1 - ambient) * light[fi]
        col = tuple(int(c * intensity) for c in base)
        tri = [tuple(p2[v]) for v in faces[fi]]
        draw.polygon(tri, fill=col)

    # Annotate
    label = axis.upper()
    draw.rectangle((10, 10, 130, 50), fill=(0, 0, 0))
    draw.text((20, 22), label, fill=(255, 255, 255))

    return img


def main() -> None:
    print(f"Loading {MODEL.name}...")
    scene = trimesh.load(MODEL)
    if isinstance(scene, trimesh.Scene):
        meshes = list(scene.dump())
        if not meshes:
            raise SystemExit("Empty scene")
        # Concatenate everything into one mesh
        mesh = trimesh.util.concatenate(meshes)
    else:
        mesh = scene

    print(f"Mesh: {len(mesh.vertices)} vertices, {len(mesh.faces)} faces")
    print(f"Bounds: {mesh.bounds}")

    # Center it
    mesh.apply_translation(-mesh.centroid)

    # Generate 6 standard views
    views = ["front", "back", "right", "left", "top", "bottom"]
    images = {}
    for v in views:
        print(f"  rendering {v}...")
        images[v] = render_view(mesh, v)

    # Save individual
    name_prefix = MODEL_DIR_NAME.split("_")[0]
    for v, img in images.items():
        img.save(OUT_DIR / f"{name_prefix}_meshy_{v}.png")

    # Composite 2x3 grid
    cell = 800
    grid = Image.new("RGB", (cell * 3, cell * 2), (8, 24, 50))
    layout = [("front", 0, 0), ("right", 1, 0), ("back", 2, 0),
              ("left", 0, 1), ("top", 1, 1), ("bottom", 2, 1)]
    for name, cx, cy in layout:
        grid.paste(images[name], (cx * cell, cy * cell))
    grid.save(OUT_DIR / f"{name_prefix}_meshy_GRID_6views.png")
    print(f"\nSaved 6 views + grid in {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
