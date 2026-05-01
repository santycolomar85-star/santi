# PROMPTS MAESTROS — ECUAMAN
### Para reproducción consistente en cualquier IA generativa

> ⚠️ **REGLA DE ORO:** Nunca modifiques las secciones marcadas como `[FIJO]`.
> Solo se puede cambiar lo marcado como `[VARIABLE]`.
> Esto garantiza que Ecuaman se vea idéntico en cualquier generación.

---

## 1. PROMPT MAESTRO UNIVERSAL (versión narrativa, base para todos)

```text
ECUAMAN — official mascot of Ecuanutrition. Anatomically accurate Penaeus vannamei
(Pacific whiteleg shrimp) reimagined as a heroic underwater superhero.

ANATOMY (mandatory): articulated cephalothorax with segmented carapace forming a
muscular hero torso with sculpted pectorals and six-pack abs visible on the shell
plates; serrated rostrum with 8 dorsal teeth above the smiling mouth; two large
expressive cartoon eyes on short eyestalks; two long flexible antennae longer
than his body, ending in feathered tassels in Ecuadorian flag order
(yellow on top, blue middle, red tip); two short bifurcated antennules; six
clearly defined abdominal segments with natural ventral curve; five pairs of
pleopods (swimmerets) under the abdomen; tail fan with central pointed telson
flanked by two pairs of uropods opening like a fan; muscular humanoid arms
emerging from the first pair of pereiopods, the others stylized as small
side appendages with tiny chelae.

COSTUME: royal blue flowing cape (#0046AD outer, #002D70 inner) attached at the
shoulders billowing in the current; bright electric blue trunks/belt (#1E88E5)
with the word "ECUAMAN" in bold white sans-serif across the front; circular
gold-bordered medallion (#F2C744 ring, #1E88E5 fill) centered on the belt
displaying a stylized white letter "E" monogram with a wave-like tail.

PROP: glowing cyan-aqua energy trident (#00D9FF core, #7DF9FF inner halo,
#00BFFF outer halo), three symmetric prongs with the central one slightly
longer, translucent crystal shaft, bioluminescent particles flowing off the
points, held vertically in his right hand.

COLOR PALETTE (body — Iconic Export version): vibrant Vannamei orange (#F39A2B)
dorsal base, deep amber (#C2691A) ventral shading, golden sun (#FFD27A) highlights
on the carapace edges, warm coral (#E8553A) accents on the chela tips.

LIGHTING: cinematic underwater scene, deep Pacific Ocean background gradient
from #001A3D top to #003A7D middle, three to five diagonal god rays from
upper-left, plankton particles in bokeh, cyan rim-light from above, warm
key-light frontal, subtle caustics dancing on the shell.

STYLE: 3D semi-realistic Pixar/DreamWorks quality, clean professional rendering,
Subsurface scattering on the carapace, expressive friendly hero face, confident
heroic smile, proud patriotic stance.

ASPECT: [VARIABLE — vertical 2:3 / square 1:1 / horizontal 16:9]
ACTION: [VARIABLE — heroic pose / flying with cape / saluting / battle stance / floating peacefully]
SCENE EXTRAS: [VARIABLE — none / Ecuadorian flag in background / mangrove silhouette / shrimp farm horizon]
```

---

## 2. MIDJOURNEY v6 / v6.1 / v7

### 2.1 Comando completo (copiar y pegar)

```
/imagine prompt: ECUAMAN heroic mascot, anatomically accurate Penaeus vannamei
whiteleg shrimp as Pixar-style underwater superhero, segmented carapace forming
muscular hero torso with six-pack abs, serrated rostrum with 8 dorsal teeth,
large expressive cartoon eyes on short eyestalks, two extra-long flexible
antennae ending in Ecuadorian flag tassels (yellow top, blue middle, red tip),
six abdominal segments, fan tail with telson and uropods, muscular humanoid
arms with small chela tips, vibrant orange body (#F39A2B) with golden highlights
and amber shadows, royal blue flowing cape, electric blue belt with "ECUAMAN"
text and gold-bordered "E" medallion, glowing cyan-aqua energy trident with
plasma halo, deep Pacific Ocean background, god rays, cyan caustics,
bioluminescent particles, cinematic 3D render, DreamWorks quality, subsurface
scattering, hero pose ::1
--ar 2:3 --style raw --stylize 250 --weird 0 --chaos 5 --v 6.1 --quality 2
```

### 2.2 Parámetros FIJOS

| Parámetro | Valor | Por qué |
|---|---|---|
| `--style` | `raw` | Evita el "look Midjourney" estilizado, mantiene fidelidad |
| `--stylize` | `250` | Balance entre creatividad e instrucción |
| `--weird` | `0` | Sin distorsiones |
| `--chaos` | `5` | Mínima variación entre las 4 generaciones |
| `--v` | `6.1` o superior | Mejor anatomía y comprensión |
| `--quality` | `2` | Máximo detalle |

### 2.3 Parámetros VARIABLES

| Parámetro | Opciones | Uso |
|---|---|---|
| `--ar` | `2:3` (poster) / `1:1` (Instagram) / `16:9` (web) / `9:16` (Reels) | Según destino |
| `--seed` | Cualquier número entero | **Anótalo** para reproducir exacto |

### 2.4 Comando para variantes consistentes (usa una seed fija)

```
/imagine prompt: [...mismo prompt anterior...] --ar 1:1 --style raw --stylize 250 --v 6.1 --seed 42852
```

> 💡 **Tip:** Genera la primera imagen master, anota la seed que aparece (clic derecho → Show Job ID), y reúsala con `--seed N` para todas las variantes futuras.

---

## 3. DALL·E 3 (ChatGPT / API)

DALL·E 3 reescribe el prompt internamente, así que hay que ser explícito y dar instrucciones que no pueda ignorar.

```text
Generate an image of ECUAMAN, the official mascot of Ecuanutrition. Do not change
any of the following details — they are part of an established brand identity:

CHARACTER: An anatomically accurate Penaeus vannamei (Pacific whiteleg shrimp)
reimagined as a heroic underwater superhero in Pixar 3D style. He must have:
(1) a serrated rostrum/beak with about 8 small teeth on top above his smiling
mouth; (2) two large expressive cartoon eyes on short eyestalks;
(3) TWO very long flexible antennae longer than his body, each ending in a
feathered tassel colored in the Ecuadorian flag order — YELLOW on top, BLUE in
the middle, RED at the tip; (4) a segmented shrimp carapace that simultaneously
forms a muscular hero torso with sculpted six-pack abs;
(5) six clearly defined abdominal segments curving naturally;
(6) a tail fan with a central pointed telson and lateral uropods;
(7) muscular humanoid arms; (8) small side legs (pereiopods) with tiny pincers.

COSTUME: A royal blue flowing cape (#0046AD), bright electric blue trunks
(#1E88E5) with the word "ECUAMAN" written in white bold letters, and a circular
gold-bordered medallion in the center of the belt with a stylized white letter
"E" inside it.

PROP: He holds a glowing cyan-aqua energy trident in his right hand, with three
symmetric prongs and a bright plasma halo.

COLOR: His body is vibrant golden orange (#F39A2B) with amber shadows and
golden highlights — like the iconic export-grade Ecuadorian shrimp.

SCENE: Deep Pacific Ocean background, dark blue gradient, diagonal god rays of
sunlight from above, soft bioluminescent particles, cinematic underwater
lighting with cyan rim-light and warm front lighting.

POSE: [VARIABLE — heroic pose facing forward / saluting with raised hand /
flying with cape billowing / battle stance with trident / proud thumbs up].

STYLE: 3D semi-realistic Pixar/DreamWorks quality, friendly heroic expression,
proud patriotic Ecuadorian energy. Vertical 2:3 aspect ratio.
```

---

## 4. GOOGLE VEO 3 / SORA (video)

Estructura cinemática para 5–10 segundos.

### 4.1 Plantilla base

```text
Cinematic underwater shot, 5 seconds, 24fps, anamorphic lens.

SUBJECT: ECUAMAN — anatomically accurate Penaeus vannamei whiteleg shrimp
reimagined as a Pixar-style heroic superhero. Segmented orange carapace
(#F39A2B) forming muscular hero torso, serrated rostrum with 8 dorsal teeth,
two long flexible antennae trailing behind with Ecuadorian flag tassels
(yellow-blue-red), royal blue cape billowing in the current, electric blue
belt with white "ECUAMAN" text and golden "E" medallion, glowing cyan trident
in his right hand emitting bioluminescent particles.

ACTION: [VARIABLE — slowly emerges from a god-ray of sunlight / swims forward
toward camera with cape trailing / raises trident as it bursts with cyan plasma /
plants Ecuadorian flag on the ocean floor and salutes].

CAMERA: [VARIABLE — slow dolly-in / orbital arc 90° / push-in close-up on face /
crane down from surface to character].

ENVIRONMENT: Deep Pacific Ocean, dark blue gradient #001A3D to #003A7D,
3 visible god rays descending from upper left, drifting plankton particles,
soft caustics dancing on his shell, distant silhouette of mangrove roots.

LIGHTING: Cinematic, cyan rim-light from above, warm key-light frontal,
subsurface scattering on the carapace, lens flare on the trident glow.

STYLE: DreamWorks/Pixar 3D quality, photoreal underwater physics with stylized
character, no text overlays.
```

### 4.2 Negative cues (Veo / Sora)
```
no distorted anatomy, no extra limbs, no missing antennae, no wrong flag order,
no lobster claws, no fish tail, no realistic horror, no logos other than "E"
medallion, no text artifacts.
```

---

## 5. STABLE DIFFUSION XL / FLUX

### 5.1 Prompt positivo

```text
masterpiece, best quality, ultra detailed, 3D pixar style, ECUAMAN superhero
mascot, anatomically accurate Penaeus vannamei whiteleg shrimp, segmented
orange carapace forming muscular hero torso, six-pack abs visible on shell
plates, serrated rostrum with 8 dorsal teeth, large expressive cartoon eyes
on short eyestalks, TWO very long flexible antennae with Ecuadorian flag
tassels (yellow blue red top to tip), six abdominal segments, fan tail with
telson and uropods, muscular humanoid arms, small side pereiopods with tiny
chelae, vibrant orange body F39A2B, golden FFD27A highlights, amber C2691A
shadows, royal blue 0046AD flowing cape, electric blue 1E88E5 belt with
ECUAMAN text in white, gold bordered F2C744 medallion with white E monogram,
glowing cyan 00D9FF energy trident with plasma halo, deep Pacific Ocean
background 001A3D, god rays, bioluminescent particles, cinematic underwater
lighting, cyan rim light, warm key light, subsurface scattering, dramatic
heroic pose, dynamic composition, sharp focus, octane render, 8k
```

### 5.2 Prompt negativo

```text
lowres, bad anatomy, missing antennae, wrong flag colors, lobster claws,
crab body, fish tail, realistic horror, scary, blood, gore, extra limbs,
extra fingers, deformed, mutation, ugly, blurry, watermark, text overlay,
signature, jpeg artifacts, oversaturated, undersaturated, flat lighting,
cartoon child drawing, low quality, monochrome, sepia
```

### 5.3 Parámetros recomendados
| Parámetro | Valor |
|---|---|
| Sampler | DPM++ 2M Karras |
| Steps | 35 |
| CFG Scale | 7.5 |
| Resolution | 1024 × 1536 (vertical) o 1024 × 1024 |
| Seed | **FIJAR** una vez encontrada la mejor versión |
| LoRA opcional | Pixar3D LoRA + Underwater LoRA |

---

## 6. RUNWAY / KLING / LUMA (video corto)

```text
A heroic Pixar-style anthropomorphic Penaeus vannamei shrimp called ECUAMAN
swims forward through deep blue ocean. Orange segmented carapace, royal blue
cape billowing, two long antennae with Ecuadorian flag tassels (yellow-blue-red)
trailing behind, glowing cyan trident in right hand, electric blue belt with
white ECUAMAN text and golden E medallion. God rays from above, bioluminescent
particles. Cinematic underwater lighting, smooth fluid motion, no camera shake.
Duration: 4 seconds.
```

---

## 7. PROMPT PARA CHAT-IMAGE EDITING (img2img / inpainting)

Cuando ya tienes una imagen base y solo quieres ajustar:

```text
Refine this ECUAMAN illustration while keeping his identity intact.
Fix only: [VARIABLE — antennae proportions / flag tassel colors / belt text
clarity / trident glow intensity / facial expression]. Do NOT change: body
color, costume, anatomy of Penaeus vannamei, pose, or background composition.
Maintain Pixar 3D quality.
```

---

## 8. TABLA DE SEEDS APROBADAS (a llenar por el equipo)

| Seed | Plataforma | Uso aprobado | Aprobado por | Fecha |
|---|---|---|---|---|
| `_______` | Midjourney v6.1 | Master vertical poster | __________ | __________ |
| `_______` | Midjourney v6.1 | Master cuadrado IG | __________ | __________ |
| `_______` | DALL·E 3 | Stickers WhatsApp | __________ | __________ |
| `_______` | SDXL + Pixar LoRA | Versión chibi | __________ | __________ |

> 📌 Cada vez que se valide una nueva pieza maestra, anotar aquí la seed.

---

## 9. CHECKLIST POST-GENERACIÓN

Antes de exportar la imagen como definitiva, verificar:

- [ ] Las 2 antenas terminan en borla **amarillo-azul-rojo** (en ese orden)
- [ ] Rostrum visible con dientes en la parte superior
- [ ] 6 segmentos abdominales claros
- [ ] Abanico caudal con telson central y urópodos
- [ ] Color de cuerpo dentro del rango `#F39A2B` ± 5%
- [ ] Capa azul `#0046AD` o muy próximo
- [ ] Texto "ECUAMAN" legible en el cinturón
- [ ] Medallón "E" centrado con borde dorado
- [ ] Tridente con halo cian-aqua activo
- [ ] Iluminación oceánica con god rays
- [ ] Sin extremidades extra ni deformidades
- [ ] Sin texto basura / watermarks / firmas

Si algún punto falla → regenerar con mismo seed + ajuste de prompt.
