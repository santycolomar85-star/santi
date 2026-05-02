# MASTER CANONICAL · ECUAMAN — REFERENCIA VISUAL ÚNICA
### Aprobado: 2026-05-02 · v3 (paleta oficial Ecuanutrition)

> ⚠️ **Estos 4 archivos son la fuente única de verdad para todo asset visual de ECUAMAN.**
> Cualquier nueva imagen debe usarlos como `reference_image` (parámetro de OpenAI `images.edit`).
> Cualquier divergencia visual debe corregirse contra estos archivos. **NO modificar.**

---

## Los 4 Masters bloqueados

| Archivo | Origen | Función | Cuándo usar |
|---|---|---|---|
| `ECUAMAN_MASTER_HERO_ACTION.png` | `MASTER_A_HEROIC_FRONTAL_v3` | Pose heroica vertical con tridente | Toda pieza institucional, posters, IG feed hero, banners donde ECUAMAN es protagonista |
| `ECUAMAN_MASTER_HERO_WELCOMING.png` | `MASTER_B_HEROIC_THREE_QUARTER_v3` | Pose 3/4 brazos abiertos, bienvenida | Hero web, landing pages, contenido invitacional, bienvenidas |
| `ECUAMAN_MASTER_PODCAST.png` | `MASTER_C_PODCAST_HOST_v3` | Sentado en estudio, micro, ON AIR | Todo asset del canal YouTube "ECUAMAN HABLA": banners, intro, episodios |
| `ECUAMAN_MASTER_AVATAR.png` | `MASTER_D_BUST_PORTRAIT_v3` | Busto cinematográfico cuadrado | Avatar canal YouTube, foto de perfil redes, thumbnails Reels/Shorts |

---

## Reglas de uso (no negociables)

1. **NO regenerar ECUAMAN desde cero**. Toda nueva escena (post, sticker, ilustración) debe usar uno de los 4 masters arriba como `reference_image` en `images.edit` para forzar continuidad visual.
2. **Elegir el master correcto según función** (ver tabla):
   - Acción heroica → HERO_ACTION
   - Bienvenida cálida → HERO_WELCOMING
   - YouTube/podcast → PODCAST
   - Avatar/thumbnail → AVATAR
3. **Si una nueva pose se repite >5 veces** (ej: ECUAMAN sentado tipo C pero comiendo), generarla 1 vez con max calidad y agregarla aquí como nuevo master canonical (`ECUAMAN_MASTER_<NOMBRE>.png`).
4. **NO mezclar masters anteriores** (`00_DAY0_MASTER_HEROIC_VERTICAL.png` y `_v2.png` son obsoletos: paleta vieja `#0046AD`). Migrarlos progresivamente.

---

## Paleta canónica usada en estos masters

- Capa: **Azul Marino `#295071`** ✅
- Cinturón: **Azul Marino `#295071`** ✅
- Tridente glow: **Celeste Fresco `#7CBFF6`** ✅
- Acentos / "On-Air": **Rojo Coral `#FF6E6E`** ✅
- Borla antenas: **Rojo Ecuador `#CE1126` + Amarillo Ecuador `#FFDD00`** ✅
- Cuerpo vannamei: `#F39A2B` base / `#C2691A` sombra / `#FFD27A` highlight ✅
- Emblema cinturón: `e` minúscula Cormorant Light Azul Marino con punto Celeste arriba-derecha (isotipo Ecuanutrition) ✅
- Texto cinturón: "ECUAMAN" Figtree Bold blanco + tagline "AQUACULTURE PRODUCTS" ✅

---

## Workflow de generación de nuevas piezas

```python
# Ejemplo: nuevo sticker con ECUAMAN saludando
{
  "id": "STICKER_NEW_HOLA_v2",
  "model": "gpt-image-1",
  "size": "1024x1024",
  "quality": "high",
  "reference_image": "ECUANUTRITION/MARKETING/00_BRAND_OFICIAL/MASTER_CANONICAL/locked/ECUAMAN_MASTER_HERO_ACTION.png",
  "prompt": "Same exact ECUAMAN character as the reference image, but [DESCRIBIR LA NUEVA POSE/ESCENA]. Mantain identical costume, palette, anatomy, proportions."
}
```

El script `scripts/generate.py` ya soporta `reference_image` y usa `client.images.edit()`.

---

**Archivos de referencia adicionales (solo Master HERO_ACTION):**
- `MASTER_CANONICAL/turnaround/TURNAROUND_5VIEWS_v1.png` — 5 vistas (front/3-4L/side/back/3-4R) para usar como referencia anatómica multivista cuando se necesite ángulo no-frontal.

---

**Última actualización**: 2026-05-02 · Aprobación del usuario (Santiago).
