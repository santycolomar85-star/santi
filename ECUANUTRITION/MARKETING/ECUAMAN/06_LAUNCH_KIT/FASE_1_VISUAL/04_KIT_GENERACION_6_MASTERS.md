# KIT DE GENERACIÓN — 6 IMÁGENES MASTER OBLIGATORIAS
### Producción reproducible · Cualquier persona del equipo, mismo resultado

> Este kit garantiza que **cualquier persona** con acceso a Midjourney, DALL·E,
> SDXL o Flux pueda generar las 6 imágenes oficiales canónicas siguiendo
> instrucciones exactas, **sin desviaciones**.

---

## 🎯 LAS 6 PIEZAS OBLIGATORIAS

| # | Nombre archivo final | Aspecto | Resolución | Uso |
|---|---|---|---|---|
| 1 | `ECUAMAN_v2_master_vertical.png` | 2:3 | 4096×6144 | Posters, packaging |
| 2 | `ECUAMAN_v2_master_square.png` | 1:1 | 4096×4096 | Instagram, perfil |
| 3 | `ECUAMAN_v2_master_horizontal.png` | 16:9 | 6144×3456 | Web, video thumbnail |
| 4 | `ECUAMAN_v2_sticker_cutout.png` | 1:1 | 2048×2048 PNG transparente | Stickers |
| 5 | `ECUAMAN_v2_line_art.svg` | escalable | SVG | Bordados, sellos |
| 6 | `ECUAMAN_v2_chibi.png` | 1:1 | 2048×2048 | Reels, emojis |

---

## ⚙️ PARÁMETROS COMUNES (FIJOS PARA LAS 6)

### Plataforma recomendada por pieza

| Pieza | Plataforma primaria | Alternativa |
|---|---|---|
| Master Vertical | **Midjourney v6.1** | Flux Pro 1.1 |
| Master Square | **Midjourney v6.1** | DALL·E 3 |
| Master Horizontal | **Midjourney v6.1** | Flux Pro |
| Sticker Cutout | **DALL·E 3** (mejor con transparencia) | SDXL + remove.bg |
| Line Art | **Adobe Illustrator** (manual) basado en master | Vectorizar con Vector Magic |
| Chibi | **Midjourney v6.1** con prompt chibi | DALL·E 3 |

### Seed strategy

> 🔑 **REGLA DE ORO:** Una vez encontrada la mejor versión de cada pieza,
> **anotar la seed** y reutilizarla siempre para variaciones futuras.

| Pieza | Seed propuesta | Estado |
|---|---|---|
| Master Vertical | `_______` | Por definir en producción |
| Master Square | `_______` | Por definir en producción |
| Master Horizontal | `_______` | Por definir en producción |
| Chibi | `_______` | Por definir en producción |

---

## 1️⃣ MASTER VERTICAL — Prompt completo

### Copy & paste para Midjourney v6.1

```
ECUAMAN heroic mascot of Ecuanutrition, anatomically accurate Penaeus vannamei
Pacific whiteleg shrimp reimagined as Pixar-style underwater superhero, full
body vertical pose, segmented orange carapace forming muscular hero torso with
sculpted six-pack abs visible on shell plates, serrated rostrum with 8 small
dorsal teeth above smiling mouth, large expressive cartoon eyes on short
eyestalks with white sclera and dark blue iris, two extra-long flexible
antennae longer than body curving back ending in feathered tassels with red
ribbon outside and yellow ribbon inside Ecuadorian colors tied with brown
leather knot, two short bifurcated antennules, six clearly defined abdominal
segments with natural ventral curve, fan tail with central pointed telson and
two pairs of lateral uropods open in fan shape, muscular humanoid arms with
detailed muscles holding glowing cyan-aqua energy trident vertical in right
hand with three symmetric prongs central one slightly longer translucent
crystal shaft emitting bioluminescent particles and bright plasma halo, left
arm flexed showing bicep, vibrant golden orange body color #F39A2B with deep
amber #C2691A shadows and golden sun #FFD27A highlights on carapace edges,
royal blue flowing cape #0046AD outer with darker blue #002D70 inner
billowing dramatically to the right in underwater current attached at
shoulders, electric blue belt #1E88E5 with bold white sans-serif text
ECUAMAN clearly legible across the front, circular gold-bordered medallion
with #F2C744 gold ring and white letter E monogram in center on the belt
above the text, deep Pacific Ocean background gradient from #001A3D top to
#003A7D middle to #000814 bottom, three diagonal god rays of sunlight
descending from upper left, drifting plankton and bioluminescent particles
in soft bokeh, cinematic dramatic underwater lighting with cyan rim light
from above warm key light frontal subsurface scattering on the carapace,
DreamWorks Pixar 3D semi-realistic style, ultra detailed, hero pose facing
camera proud confident smile, sharp focus, octane render quality
--ar 2:3 --style raw --stylize 250 --weird 0 --chaos 5 --v 6.1 --quality 2
```

### Configuración técnica
- **Aspect ratio:** 2:3 (`--ar 2:3`)
- **Resolución final:** Upscale 2x → 4096×6144
- **Color profile:** Adobe RGB (1998)
- **Bit depth:** 16-bit
- **Formato:** PNG

### Validación post-generación
1. Pasar checklist 24 puntos
2. Si falla > 4 puntos: regenerar con misma seed y prompt afinado
3. Si pasa: anotar seed, exportar PNG 16-bit, archivar PSD multi-capa

---

## 2️⃣ MASTER CUADRADO — Prompt completo

### Copy & paste para Midjourney v6.1

```
ECUAMAN heroic mascot of Ecuanutrition centered composition perfect for
Instagram, anatomically accurate Penaeus vannamei Pacific whiteleg shrimp as
Pixar-style underwater superhero, [...mismo resto del prompt master vertical
sin cambios...]
--ar 1:1 --style raw --stylize 250 --weird 0 --chaos 5 --v 6.1 --quality 2
```

> Solo cambia: `--ar 1:1` y agrega "centered composition perfect for Instagram"
> al inicio. **NO modifiques otros parámetros.**

---

## 3️⃣ MASTER HORIZONTAL — Prompt completo

### Copy & paste para Midjourney v6.1

```
ECUAMAN heroic mascot of Ecuanutrition cinematic horizontal composition with
character on the right third leaving 60% empty space on left for text overlay,
[...mismo resto del prompt master vertical sin cambios...]
--ar 16:9 --style raw --stylize 250 --weird 0 --chaos 5 --v 6.1 --quality 2
```

> Solo cambia: `--ar 16:9` y agrega "cinematic horizontal composition with
> character on the right third leaving 60% empty space on left for text overlay"
> al inicio.

---

## 4️⃣ STICKER CUTOUT (PNG transparente) — Prompt completo

### Copy & paste para DALL·E 3

```
Create a high-quality sticker version of ECUAMAN, the official mascot of
Ecuanutrition. Full body character only, transparent background (no scenery,
no shadows behind), perfect for WhatsApp and Telegram stickers.

Character must be: an anatomically accurate Penaeus vannamei (Pacific whiteleg
shrimp) reimagined as Pixar 3D superhero with: serrated rostrum with 8 dorsal
teeth, two large expressive cartoon eyes on short eyestalks, two long flexible
antennae with red and yellow Ecuadorian ribbon tassels, segmented carapace
forming muscular hero torso with six-pack abs, six abdominal segments, fan
tail with telson and uropods, muscular humanoid arms.

Costume: royal blue flowing cape (hex #0046AD), electric blue belt (hex
#1E88E5) with white "ECUAMAN" text and gold-bordered medallion with white
"E" letter, glowing cyan trident in right hand.

Body color: vibrant golden orange (hex #F39A2B) with amber shadows and golden
highlights.

Pose: hero standing pose, friendly smile, looking at viewer, both feet (or
abdomen) clearly visible.

Style: 3D Pixar quality, vibrant colors, clean rendering, sharp edges around
the character outline so it can be cut out cleanly, NO background elements,
NO text outside the character.

Aspect ratio: square 1:1.
```

### Post-procesamiento manual obligatorio
1. Verificar transparencia con [remove.bg](https://remove.bg) si DALL·E dejó fondo
2. Refinar bordes con Photoshop "Refine Edge"
3. Exportar PNG-24 con transparencia
4. Validar tamaño 2048×2048

---

## 5️⃣ LINE ART (vector SVG) — Proceso manual

### Paso 1: Generar referencia
Usar Master Vertical aprobado como base.

### Paso 2: Vectorización
**Opción A — Manual (recomendada):**
1. Abrir master en Adobe Illustrator
2. Crear capa nueva sobre la imagen
3. Trazar contornos con herramienta Pluma (Pen Tool)
4. Grosor de línea: 4px en archivo de 2048px
5. Color de línea: `#000000` puro
6. Sin relleno
7. Exportar como SVG optimizado

**Opción B — Automática (rápida pero menos precisa):**
1. Usar Vector Magic o Adobe Illustrator "Image Trace"
2. Configuración: "Line Art", umbral 50%
3. Limpiar trazos manualmente
4. Exportar SVG

### Validación
- Debe ser reconocible como Ecuaman a 32px de tamaño
- Debe imprimirse correctamente en bordado y serigrafía
- Sin trazos < 2px (no se ven al imprimir)

---

## 6️⃣ VERSIÓN CHIBI — Prompt completo

### Copy & paste para Midjourney v6.1

```
ECUAMAN chibi cute version of Ecuanutrition mascot, kawaii style, big head
small body 1:1 head-to-body proportions, anatomically simplified Penaeus
vannamei whiteleg shrimp as adorable mini superhero, big sparkly cartoon
eyes occupying 30% of face, tiny serrated rostrum, simplified short antennae
with red and yellow tassel pom-poms, simplified segmented orange carapace,
chubby muscular tiny torso, mini cape billowing, mini blue belt with E
medallion, holding mini glowing cyan trident, big smile, kawaii expression,
golden orange body #F39A2B, royal blue cape #0046AD, electric blue belt
#1E88E5, deep ocean background with bubbles, 3D Pixar chibi style, soft
rounded shapes, vibrant cute colors
--ar 1:1 --style raw --stylize 400 --weird 0 --chaos 5 --v 6.1 --quality 2
```

### Notas especiales
- `--stylize 400` (más estilizado que masters)
- Mantener TODOS los elementos del canon (capa, belt, tridente, antenas)
- Solo cambian las proporciones, no la identidad

---

## 📋 PROCEDIMIENTO COMPLETO PASO A PASO

### Para cualquier persona del equipo:

#### Día 1 — Preparación
1. Leer `01_MANUAL/MANUAL_DE_MARCA_ECUAMAN.md` (30 min)
2. Leer `06_LAUNCH_KIT/FASE_1_VISUAL/02_BRIEF_VISUAL_DEFINITIVO.md` (45 min)
3. Configurar acceso a Midjourney v6.1 + DALL·E 3
4. Imprimir el `03_REFERENCIAS/CHECKLIST_VALIDACION.md`

#### Día 2 — Producción
5. Generar pieza 1 (Master Vertical):
   - Copiar prompt exacto de este documento (sección 1️⃣)
   - Generar 4 variaciones
   - Elegir la mejor
   - **Anotar seed**
   - Upscale a máxima resolución
6. Generar pieza 2 (Master Square): mismo proceso
7. Generar pieza 3 (Master Horizontal): mismo proceso

#### Día 3 — Stickers y derivados
8. Generar pieza 4 (Sticker) en DALL·E 3
9. Limpiar fondo si necesario (remove.bg)
10. Generar pieza 6 (Chibi)

#### Día 4 — Vector y aprobación
11. Vectorizar pieza 5 (Line Art) en Illustrator
12. Validar las 6 piezas con checklist 24 puntos
13. Exportar en todos los formatos requeridos
14. Subir a `07_ASSETS_OFICIALES/` con nombres oficiales
15. Solicitar aprobación del Director de Marca

#### Día 5 — Backup y documentación
16. Backup en Google Drive carpeta ECUAMAN
17. Backup adicional en disco físico (NAS o USB encriptado)
18. Llenar la tabla de seeds en `02_PROMPTS/PROMPTS_MAESTROS.md`
19. Documentar cualquier desviación o aprendizaje en
    `06_LAUNCH_KIT/FASE_1_VISUAL/notas_produccion.md`

---

## 💰 PRESUPUESTO DE PRODUCCIÓN DE 6 MASTERS

| Concepto | Costo USD |
|---|---|
| Suscripción Midjourney Pro 1 mes | $60 |
| Suscripción ChatGPT Plus 1 mes (DALL·E 3) | $20 |
| Photoshop / Illustrator (suscripción mensual) | $55 |
| 1 ilustrador para retoque y vectorización (3 días) | $300-600 |
| Backup en Drive (gratis) | $0 |
| **Total mínimo** | **$435-735** |

---

## 🎓 GARANTÍA DE REPRODUCIBILIDAD

> Si una nueva persona del equipo recibe este kit y NO logra reproducir las 6
> piezas en máximo 5 días con calidad similar a las referencias actuales,
> el kit tiene un defecto y debe corregirse.

### Indicadores de éxito
- ✅ Las 6 piezas pasan el checklist 24/24
- ✅ Visualmente reconocibles como "el mismo Ecuaman" que las referencias históricas
- ✅ Listas para usarse en producción (resolución, formatos, calidad)
- ✅ La persona puede reproducir variaciones de las piezas en horas, no semanas

### Si la persona se atasca
1. Revisar con `02_BRIEF_VISUAL_DEFINITIVO.md` qué punto está fallando
2. Comparar con `03_REFERENCIAS/historicas/` para identificar diferencia
3. Ajustar prompt manteniendo la estructura
4. Si persiste, escalar al Director Creativo

---

*Este kit se actualiza cada vez que cambia el modelo de IA o se descubren
mejores prácticas. Versión actual: 1.0 — Mayo 2026.*
