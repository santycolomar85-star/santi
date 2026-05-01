# RECREATOR'S KIT — Cualquier miembro del equipo crea Ecuaman en 2 horas
### El "manual de instrucciones" más completo del mundo para reproducir un mascot

> **Promesa de este documento:** Si alguien de tu equipo nunca ha visto a
> Ecuaman, lee SOLO este documento, y en **2 horas** produce una versión
> 100% canónica del mascot que pasa el checklist 24/24.
>
> Sin este documento, la marca depende de personas. Con este documento,
> la marca pertenece al sistema.

---

## ⏱️ TIEMPO ESTIMADO POR ETAPA

| Etapa | Tiempo | Acumulado |
|---|---|---|
| 1. Lectura y comprensión | 30 min | 0:30 |
| 2. Setup técnico (cuentas IA) | 15 min | 0:45 |
| 3. Generación primera pieza | 30 min | 1:15 |
| 4. Validación con checklist | 15 min | 1:30 |
| 5. Generación variantes (5 más) | 25 min | 1:55 |
| 6. Backup y documentación | 5 min | 2:00 |

**Total: 2 horas exactas.**

---

## 📚 PARTE 1 — LECTURA OBLIGATORIA (30 minutos)

Lee en este orden EXACTO:

### Lectura 1 (10 min): Quién es Ecuaman
Abre: `05_ESTRATEGIA/01_BIBLIA_DEL_PERSONAJE.md`
Lee secciones 1, 2, 4 (Identidad, Personalidad, Backstory). NO necesitas memorizar todo, pero debes terminar entendiendo:
- Es un langostino vannamei (no cangrejo, no langosta, no gamba)
- Es un superhéroe (no un personaje cómico)
- Representa Ecuador y Ecuanutrition

### Lectura 2 (10 min): Cómo se ve Ecuaman
Abre: `06_LAUNCH_KIT/FASE_1_VISUAL/02_BRIEF_VISUAL_DEFINITIVO.md`
Lee solo:
- Sección 1 (Anatomía Pixel-Perfect)
- Sección 2 (Paleta de Color)
- Sección 4 (Pose Canónica)
- Sección 7 (Lo que nunca debe pasar)

### Lectura 3 (5 min): Mira referencias
Abre la carpeta: `03_REFERENCIAS/historicas/`
Mira las 9 imágenes. Tu objetivo es producir algo del mismo nivel o mejor.

### Lectura 4 (5 min): Conoce el checklist
Abre: `03_REFERENCIAS/CHECKLIST_VALIDACION.md`
Imprímelo o ten una pestaña abierta. Lo usarás 6 veces.

---

## 🛠️ PARTE 2 — SETUP TÉCNICO (15 minutos)

### Cuentas necesarias

| Plataforma | Para qué | Costo | Cómo obtenerla |
|---|---|---|---|
| **Midjourney** | Masters principales | $30/mes Pro | Discord + suscripción en midjourney.com |
| **ChatGPT Plus** | Sticker DALL·E 3 | $20/mes | chatgpt.com |
| **remove.bg** | Limpieza de fondos | Gratis (50 imgs/día) | remove.bg |

### Setup Midjourney (paso a paso)
1. Crear cuenta Discord en discord.com
2. Ir a midjourney.com → suscribirse a Pro Plan
3. Discord → unirse al servidor Midjourney
4. Buscar canal "newbies" o crear servidor propio
5. Invitar el bot Midjourney a tu servidor: `/imagine` para iniciar
6. Test rápido: escribir `/imagine prompt: a cat --v 6.1`
   Si funciona → estás listo.

### Setup DALL·E 3
1. Suscribirse a ChatGPT Plus
2. En ChatGPT, escribir "genera una imagen de prueba" para confirmar acceso
3. Listo.

---

## 🎨 PARTE 3 — GENERAR LA PRIMERA PIEZA (30 min)

### Pieza objetivo: Master Vertical (la más importante)

#### Paso 3.1 — Abrir el prompt maestro (1 min)
Abre: `06_LAUNCH_KIT/FASE_1_VISUAL/04_KIT_GENERACION_6_MASTERS.md`
Sección **1️⃣ MASTER VERTICAL**.

#### Paso 3.2 — Copiar el prompt EXACTO (1 min)
Selecciona TODO el bloque de código del prompt (incluye los `--ar 2:3 --style raw...`).
Cópialo. **No modifiques nada.**

#### Paso 3.3 — Pegar en Midjourney (1 min)
En Discord, en el canal donde tengas el bot:
- Escribir `/imagine prompt:` 
- Pegar el prompt completo
- Enter

#### Paso 3.4 — Esperar generación (1-2 min)
Midjourney genera 4 variaciones. Aparecen en cuadrícula.

#### Paso 3.5 — Elegir la mejor (5 min)
Mira las 4. Compara con las referencias en `03_REFERENCIAS/historicas/`.
Elige la que más se parezca al canon. Criterios:
- ¿Tiene rostrum aserrado?
- ¿Tiene 2 antenas con borla rojo+amarillo?
- ¿Tiene 6 segmentos abdominales?
- ¿Tiene capa azul, cinturón ECUAMAN, medallón "E"?
- ¿Tiene tridente cian?
- ¿Está en pose heroica?

Si NINGUNA cumple → escribir `🔄` (Reroll) o regenerar.

#### Paso 3.6 — Upscale (1 min)
Sobre la mejor, clic en `U1`, `U2`, `U3` o `U4` según su posición. Esto la
hace alta resolución.

#### Paso 3.7 — Anotar seed (2 min)
Después del upscale, clic derecho en la imagen → "Show Job ID" o usar
comando `/info`. Verás un seed (número como `1234567890`).
**Anótalo en una hoja con el nombre de la pieza.**

#### Paso 3.8 — Descargar (1 min)
Clic derecho sobre la imagen final → Guardar como.
Nombrar: `ECUAMAN_v2_master_vertical_seedXXXXX.png`
Carpeta destino: `07_ASSETS_OFICIALES/mascot_mark/`

---

## ✅ PARTE 4 — VALIDAR CON CHECKLIST (15 min)

Abre `03_REFERENCIAS/CHECKLIST_VALIDACION.md`.
Examina la imagen y marca cada uno de los 24 puntos.

### Resultado esperado
| Puntuación | Acción |
|---|---|
| **24/24** | ✅ Pieza aprobada → continuar a Parte 5 |
| **20-23** | ⚠️ Refinar con DALL·E 3 (img2img) o regenerar con prompt ajustado |
| **<20** | ❌ Regenerar con misma seed + ajuste de prompt; si persiste, escalar a Director Creativo |

### Cómo refinar si falla un punto

**Si fallan las antenas (sin borla rojo+amarillo):**
Agregar al prompt: `BIG ATTENTION: each long antenna MUST end in a tassel
with one red ribbon and one yellow ribbon, in Ecuadorian flag colors`

**Si falla el rostrum (no aserrado):**
Agregar: `IMPORTANT: visible serrated saw-like rostrum beak with at least
8 small teeth on top, characteristic of Penaeus vannamei`

**Si fallan los segmentos abdominales (no se ven 6):**
Agregar: `the abdomen MUST clearly show six distinct segments`

**Si el tridente no es cian:**
Agregar: `trident MUST be glowing cyan-aqua color (hex #00D9FF), not gold,
not red, not any other color`

---

## 🔁 PARTE 5 — GENERAR LAS OTRAS 5 PIEZAS (25 min)

### Pieza 2: Master Cuadrado (5 min)
Mismo prompt que Master Vertical, pero cambiar `--ar 2:3` por `--ar 1:1`.
Idealmente, usa la **misma seed** que la vertical para consistencia:
agregar `--seed XXXXX` (donde XXXXX es la seed que anotaste).
Validar con checklist.

### Pieza 3: Master Horizontal (5 min)
Mismo prompt, cambiar a `--ar 16:9`. Misma seed.
Validar.

### Pieza 4: Sticker (PNG transparente) (5 min)
Ir a ChatGPT (DALL·E 3).
Copiar el prompt completo de la sección **4️⃣** del KIT_6_MASTERS.
DALL·E genera 1 imagen.
Si tiene fondo blanco u otro: subir a remove.bg → descargar PNG transparente.
Validar.

### Pieza 5: Line Art (vector) (5 min)
Esta requiere herramienta vectorial (Illustrator, Inkscape gratis).

**Versión rápida (sin Illustrator):**
1. Subir Master Vertical a [Vector Magic](https://vectormagic.com)
2. Configurar: "Logo" mode, alta calidad, blanco y negro
3. Descargar SVG resultante
4. Limpiar nodos sobrantes en Inkscape (gratis)
5. Exportar SVG final

### Pieza 6: Chibi (5 min)
Copiar prompt de la sección **6️⃣** del KIT.
Generar en Midjourney.
Validar.

---

## 💾 PARTE 6 — BACKUP Y DOCUMENTACIÓN (5 min)

### Estructura final esperada en tu carpeta:
```
07_ASSETS_OFICIALES/
├── mascot_mark/
│   ├── ECUAMAN_v2_master_vertical_seed12345.png
│   ├── ECUAMAN_v2_master_square_seed12345.png
│   ├── ECUAMAN_v2_master_horizontal_seed12345.png
│   └── ECUAMAN_v2_chibi_seed67890.png
├── stickers/
│   └── ECUAMAN_v2_sticker_cutout.png
└── line_art/
    └── ECUAMAN_v2_line.svg
```

### Subir a Drive
Carpeta Drive: `ECUAMAN/Producción_Oficial_v2/[fecha]/`
Subir las 6 piezas + un archivo de texto `seeds.txt` con todas las seeds.

### Subir al repo
Si tienes acceso al repo, hacer push a la carpeta correspondiente.
Si no, enviar a quien tenga acceso.

### Reportar
Enviar email/mensaje al Director de Marca:
```
Asunto: Lote nuevo Ecuaman v2 — [tu nombre] — [fecha]
Cuerpo:
- 6 piezas generadas y validadas
- Seeds documentadas
- Subidas a Drive en [carpeta]
- Subidas al repo en [rama] (o pendiente)
- Solicito aprobación final
```

---

## 🆘 PROBLEMAS COMUNES Y SOLUCIONES

### Problema 1: "Midjourney genera algo que parece más cangrejo que langostino"
**Solución:** Agregar al inicio del prompt: `Penaeus vannamei whiteleg shrimp,
NOT a crab NOT a lobster NOT a generic shrimp, specifically a vannamei with
its characteristic anatomy`

### Problema 2: "El cinturón no dice ECUAMAN o el texto sale mal"
**Solución:** DALL·E 3 maneja mejor el texto que Midjourney.
Generar primero en MJ sin texto, luego usar DALL·E 3 con inpainting:
*"Add the text ECUAMAN in white bold sans-serif font on the blue belt"*

### Problema 3: "Las antenas salen como pelos de mosquito"
**Solución:** Reforzar: `two THICK robust flexible antennae each as long as
the entire body, ending in clearly visible feathered tassels`

### Problema 4: "El tridente sale dorado en vez de cian"
**Solución:** Repetir 3 veces en el prompt: `glowing CYAN BLUE trident,
glowing CYAN BLUE trident, glowing CYAN BLUE trident, color hex #00D9FF`

### Problema 5: "El personaje sale girado o en pose rara"
**Solución:** Agregar: `front view, three-quarter angle facing camera,
heroic standing pose, full body visible from rostrum to tail`

### Problema 6: "Sale demasiado realista (parece foto)"
**Solución:** Agregar: `Pixar 3D animation style, NOT photorealistic, NOT a
real photograph, stylized cartoon character`

### Problema 7: "Sale demasiado caricatura (estilo niño)"
**Solución:** Agregar: `professional DreamWorks Pixar quality, sophisticated
3D rendering, NOT a child drawing, NOT a simple cartoon`

### Problema 8: "El borde del sticker no es limpio"
**Solución:** Subir a remove.bg → si aún tiene halos, usar Photoshop
"Refine Edge" → "Decontaminate Colors"

---

## 🎓 EVALUACIÓN DE COMPETENCIA

Después de completar este kit, evalúa tu nivel:

| Nivel | Criterios | Habilitación |
|---|---|---|
| 🟢 **Aprendiz** | Generaste las 6 piezas en >3 horas, 4-5 pasaron checklist | Producir bajo supervisión |
| 🟡 **Junior** | Generaste las 6 en 2-3 horas, todas pasaron checklist 22+/24 | Producir piezas estándar autónomamente |
| 🔵 **Senior** | Generaste las 6 en <2 horas, todas pasaron 24/24 | Producir piezas master + entrenar a otros |
| 🟣 **Lead** | Puedes generar campañas completas siguiendo manual sin consultas | Aprobar trabajo de otros |

Documentar tu nivel en `06_LAUNCH_KIT/equipo_certificado.md`.

---

## 📞 ESCALAMIENTO

Si después de seguir este kit no logras resultados aceptables:

1. **Primero:** revisa que estés en la versión más nueva del Manual de Marca
2. **Segundo:** consulta `06_LAUNCH_KIT/FASE_1_VISUAL/02_BRIEF_VISUAL_DEFINITIVO.md`
   sección 7 "Lo que nunca debe pasar"
3. **Tercero:** habla con un colega que ya esté certificado nivel Senior+
4. **Cuarto:** escala al Director Creativo: __________________

---

## 🏆 EL CONTRATO QUE ACEPTAS AL USAR ESTE KIT

Al usar este kit y producir piezas oficiales de Ecuaman, te comprometes a:

1. ✅ Respetar el manual sin desviaciones creativas no autorizadas
2. ✅ Validar con checklist 24 puntos en cada pieza
3. ✅ Documentar las seeds para reproducibilidad futura
4. ✅ No publicar piezas que no hayan pasado aprobación
5. ✅ Reportar bugs o defectos del kit para que se corrija
6. ✅ No compartir el kit fuera del equipo Ecuanutrition (es propiedad intelectual)

---

*"Una marca que cualquier miembro del equipo puede recrear bien es una marca
que vivirá 100 años. Una marca que solo su creador entiende muere con él."*

— Filosofía del Recreator's Kit
