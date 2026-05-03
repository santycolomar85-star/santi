# GENERADOR DE AVATARES ÚNICOS — LoRA Ecuaman
### Pipeline ML para producir un Ecuaman irrepetible por cada Guardián, manteniendo identidad de marca

> **Tesis:** sin un avatar único, ser Guardián #00471 es solo un número.
> Con un avatar único, eres **TÚ** dentro del universo Ecuaman. Este documento
> define cómo entrenar, desplegar, monitorear y proteger el modelo que
> produce esos avatares.

---

## 0. RESUMEN EJECUTIVO

| Atributo | Valor |
|---|---|
| Modelo base | **SDXL 1.0** (Stable Diffusion XL) |
| Técnica de fine-tuning | **LoRA** (Low-Rank Adaptation) |
| Tamaño LoRA entrenado | ~150 MB |
| Dataset de entrenamiento | 200-300 imágenes canónicas Ecuaman |
| Inferencia productiva | **Replicate** (managed) + fallback **RunPod** |
| Tiempo medio generación | 25-35 segundos por avatar |
| Costo por inferencia | ~$0.04 USD |
| Resolución salida | 1024 × 1024 px |

---

## 1. POR QUÉ LoRA Y NO ALGO MÁS

| Opción | Pros | Contras | Veredicto |
|---|---|---|---|
| Prompt-only (DALL·E 3 / GPT-Image-1) | Rápido, sin training | **Inconsistencia visual brutal** entre generaciones | ❌ Ya probado, falló (ver `07_ASSETS_OFICIALES/REPORTE_FINAL_GENERACION.md`) |
| Fine-tune completo SDXL | Máxima fidelidad | Costo absurdo (~$2-5k cada training), lento | ❌ Sobre-ingeniería |
| **LoRA propio sobre SDXL** | Identidad consistente, costo controlado, rápido reentrenar | Requiere dataset curado | ✅ **Elegida** |
| Midjourney via niji v6 | Estilo épico inmediato | Sin API oficial estable, sin control de identidad | ❌ Solo apoyo manual |
| ControlNet + img2img | Permite forzar pose | Agrega latencia | ✅ Complementario, opcional |

**Decisión:** LoRA Ecuaman entrenado sobre SDXL, complementado con
ControlNet (Canny/Pose) para variaciones únicas controladas por Guardián.

---

## 2. DATASET DE ENTRENAMIENTO

### 2.1 Composición objetivo (300 imágenes)

| Categoría | Cantidad | Fuente |
|---|---|---|
| Master shots Ecuaman (frontal, perfil, 3/4) | 30 | `07_ASSETS_OFICIALES/auto_generated/` curados |
| Poses heroicas (tridente alzado, vuelo, defensa) | 60 | Generación supervisada + retoque |
| Expresiones faciales (sonrisa, foco, asombro, ira) | 40 | Generación supervisada |
| Variaciones de borla, antenas, ojos | 30 | Diseño manual + generación dirigida |
| Ecuaman en contextos (mar, granja, mercado, asamblea) | 60 | Mix |
| Cuerpo completo, recorte y close-up | 30 | Mix |
| Variaciones de iluminación (día, atardecer, neón, tormenta) | 30 | Mix |
| Edge cases negativos (lo que NO debe ser) | 20 | Curado, marcado como "negative" |

### 2.2 Reglas de curación

- ✅ Tridente cyan presente en > 80% de las imágenes (refuerzo de identidad).
- ✅ Capa roja presente en > 70% de las imágenes.
- ✅ Anatomía Penaeus vannamei verificada por brief en
  `03_REFERENCIAS/BRIEF_ANATOMICO_VANNAMEI.md`.
- ❌ Cero humanos. Cero shrimps "young". Cero drones. Cero silhouettes.
  (Lecciones aprendidas en `07_ASSETS_OFICIALES/REPORTE_FINAL_GENERACION.md`).
- ✅ Cada imagen pasa el `CHECKLIST_VALIDACION.md` (24 puntos) antes de
  entrar al dataset.

### 2.3 Etiquetado (captions)

Cada imagen tiene un caption estructurado:

```
ecuamanhero, [pose], [expresion], [contexto], [iluminacion], [encuadre],
holding cyan trident, red cape, golden medallion, anatomically correct shrimp
```

Ejemplo:
```
ecuamanhero, holding trident raised, fierce expression, on Pacific ocean cliff,
dramatic sunset lighting, full body 3/4 shot, holding cyan trident, red cape,
golden medallion, anatomically correct Penaeus vannamei
```

> Token único de identidad: `ecuamanhero` (palabra inventada que el modelo
> aprende a asociar con todo el conjunto visual).

### 2.4 Augmentation

- Flip horizontal: ✅
- Crop variaciones: ✅
- Color jitter ligero: ✅ (pero respetando paleta marca)
- Rotación: ❌ (rompería identidad)

---

## 3. ENTRENAMIENTO

### 3.1 Stack

- Hardware: **1× A100 80GB** (RunPod o Lambda Labs)
- Framework: **kohya_ss** (referencia de la comunidad SDXL)
- Tiempo estimado: 2-4 horas de training para LoRA decente
- Costo por training: **~$8-12 USD**

### 3.2 Hiperparámetros base (punto de partida)

```yaml
base_model: stabilityai/stable-diffusion-xl-base-1.0
network_dim: 64
network_alpha: 32
learning_rate: 1.0e-4
text_encoder_lr: 5.0e-5
unet_lr: 1.0e-4
lr_scheduler: cosine_with_restarts
optimizer: AdamW8bit
train_batch_size: 2
gradient_accumulation_steps: 4
max_train_epochs: 20
mixed_precision: bf16
save_every_n_epochs: 4
sample_every_n_epochs: 2
clip_skip: 2
```

> Sample prompts durante training para validar visualmente:
> - `ecuamanhero, hero pose, golden hour, cinematic`
> - `ecuamanhero portrait, fierce, looking at camera`
> - `ecuamanhero defending coral reef from oil spill`

### 3.3 Validación post-training

| Test | Criterio |
|---|---|
| Identidad consistente | 8/10 jurados internos identifican como "el mismo Ecuaman" |
| Adherencia anatómica | 9/10 imágenes pasan brief Penaeus vannamei |
| Sin humanos accidentales | 10/10 sin humanos generados espontáneamente |
| Tridente y capa | > 90% de imágenes los incluyen sin pedirlo explícito |
| Variabilidad | Diferentes seeds producen poses/expresiones diferentes (no copia exacta) |

### 3.4 Versionado del modelo

- `models/ecuaman-lora/v1.0.safetensors` — primera versión productiva
- `models/ecuaman-lora/v1.1.safetensors` — refinamientos menores
- `models/ecuaman-lora/v2.0.safetensors` — re-entrenamiento mayor

Cada versión con changelog en `models/ecuaman-lora/CHANGELOG.md`.

---

## 4. INFERENCIA EN PRODUCCIÓN

### 4.1 Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│  Backend API                                                  │
│   POST /avatar/generate                                       │
│     • valida Guardián autenticado                             │
│     • recupera guardian_number, title, country                │
│     • construye prompt determinista (ver §4.2)                │
│     • encola job en Redis (Upstash)                           │
│     • responde { jobId }                                      │
└───────────────────────────┬─────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  Worker async                                                 │
│   • toma jobs de la cola                                      │
│   • llama Replicate API con LoRA Ecuaman                      │
│   • timeout 90 s, retry 1 vez                                 │
│   • al completar:                                             │
│     - guarda PNG en R2 (`avatars/{guardian_id}/v{n}.png`)    │
│     - genera versión cuadrada 512×512 para perfil             │
│     - genera versión badge 256×256 para Pasaporte físico      │
│     - actualiza guardians.avatar_url                          │
│     - dispara notificación push si app instalada              │
└───────────────────────────┬─────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  Frontend (microsite/app)                                     │
│   GET /avatar/{jobId} (polling cada 2 s, máx 60 s)           │
│   o WS push al completar                                      │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Prompt determinista por Guardián

Cada Guardián recibe un prompt **derivado de su número y título**, lo que
garantiza que su avatar es único pero reproducible:

```typescript
function buildAvatarPrompt(guardian: Guardian): { prompt: string, negative: string, seed: number } {
  const baseTokens = "ecuamanhero, holding cyan trident, red cape, golden medallion, " +
                     "anatomically correct Penaeus vannamei, cinematic lighting, " +
                     "1024x1024, masterpiece, brand identity consistent";

  // Variaciones derivadas del número (deterministas)
  const poseVariants = ["hero pose front", "side profile heroic", "tridente alzado",
                        "guardian stance", "cape flowing", "leaping forward"];
  const lightVariants = ["golden hour", "blue hour", "stormy ocean light",
                         "sunrise glow", "moonlit pacific", "neon underwater"];
  const ctxVariants  = ["on rocky coast Manabí", "above coral reef",
                        "in mangrove forest", "on shrimp farm dawn",
                        "above Pacific waves", "in marketplace"];
  const accentColors = ["", "subtle teal accent", "subtle purple accent",
                        "subtle gold accent", "subtle silver accent"];

  const i = (n: number, len: number) => n % len;
  const pose   = poseVariants[i(guardian.guardian_number, 6)];
  const light  = lightVariants[i(Math.floor(guardian.guardian_number / 6), 6)];
  const ctx    = ctxVariants [i(Math.floor(guardian.guardian_number / 36), 6)];
  const accent = accentColors[i(Math.floor(guardian.guardian_number / 216), 5)];

  const titleHint = `${guardian.title.toLowerCase()} energy`;

  const prompt = [baseTokens, pose, light, ctx, accent, titleHint].filter(Boolean).join(", ");

  const negative = "low quality, blurry, deformed, extra limbs, human body, " +
                   "young shrimp, drone, silhouette, multiple tridents, missing trident, " +
                   "missing cape, anime, watermark, text, signature";

  // Seed determinista a partir de guardian_number (reproducible)
  const seed = (guardian.guardian_number * 2654435761) >>> 0;

  return { prompt, negative, seed };
}
```

> Combinaciones únicas: 6 × 6 × 6 × 5 = **1.080 variaciones base**, multiplicado
> por seed (≈ 4 × 10⁹) → cada avatar es prácticamente único, pero **reproducible**
> si hay que regenerar.

### 4.3 Configuración de inferencia

```yaml
model: stabilityai/stable-diffusion-xl-base-1.0
lora: ecuaman-lora-v1.safetensors @ weight 0.85
sampler: DPM++ 2M Karras
steps: 32
cfg_scale: 7.5
width: 1024
height: 1024
denoising_strength: 1.0  # text2img puro
clip_skip: 2
```

### 4.4 Post-procesamiento

1. Upscale 2x con **R-ESRGAN** opcional para Pasaporte físico (2048×2048).
2. Auto-crop a 1:1 si la composición lo permite.
3. Compresión: PNG sin pérdida para fuente, WebP/AVIF para web.
4. Sello "Generado oficialmente por Ecuanutrition · {timestamp}" en
   metadata EXIF (no visible).

---

## 5. CONTROL DE CALIDAD AUTOMATIZADO

Antes de entregar al Guardián, el avatar pasa por un **clasificador de calidad**:

| Check | Tecnología | Acción si falla |
|---|---|---|
| ¿Tiene tridente cyan? | CLIP zero-shot | Reintentar con peso LoRA mayor |
| ¿Tiene capa roja? | CLIP zero-shot | Reintentar |
| ¿Cero humanos? | YOLOv8 person detector | Rechazar, regenerar |
| ¿Anatomía vannamei válida? | Clasificador propio (sigue brief) | Reintentar |
| ¿Sin texto/watermark? | OCR Tesseract | Inpaint o reintentar |

Si tras 2 reintentos el avatar no pasa, se entrega un **avatar "ceremonial
fallback"** (uno de 12 prediseñados) y se marca el job en cola para
re-generación nocturna offline.

---

## 6. ALMACENAMIENTO Y CDN

- Bucket: `r2://ecuaman-avatars/`
- Estructura: `/{guardian_id}/v{n}.png` (versionado, no se borra el anterior)
- Versiones derivadas:
  - `original-1024.png`
  - `profile-512.webp`
  - `badge-256.webp`
  - `pasaporte-2048.png` (solo si solicita Pasaporte físico)
- TTL: indefinido. Borrado solo bajo derecho de eliminación GDPR.
- CDN: Cloudflare frente al bucket, caché 1 año.

---

## 7. PROPIEDAD INTELECTUAL Y RIESGOS

### 7.1 Propiedad de los avatares

- Los avatares son **propiedad de Ecuanutrition**.
- El Guardián tiene **licencia de uso personal no comercial** (perfil, foto,
  imprimir, regalar). NO puede vender ni licenciar a terceros.
- Términos cubiertos en `/legal/terminos` y validados por FASE 3.

### 7.2 Riesgo: contenido inapropiado generado

- LoRA propio reduce drásticamente la probabilidad, pero no es 0%.
- **Capa adicional:** moderación NSFW (ej: NudeNet o Replicate moderation).
- Política: reportar avatares dudosos al equipo en 24h. Reentrenamiento
  trimestral con dataset ampliado de "lo que NO debe generarse".

### 7.3 Riesgo: sesgo o representación

- Aunque Ecuaman no es humano, validar que en contextos no se generen
  estereotipos culturales inadecuados (ej: representaciones erróneas de
  comunidades costeras).
- Revisión de muestras aleatorias mensual por equipo de comunidad.

### 7.4 Riesgo: filtración del LoRA

- LoRA almacenado en bucket privado, jamás expuesto al cliente.
- Inferencia siempre server-side. No se distribuye el `.safetensors`
  públicamente.
- Marca de agua estegano-firmada en cada avatar (StegaStamp opcional v2).

---

## 8. EXPERIMENTACIÓN Y EVOLUCIÓN

### Roadmap del modelo

| Versión | Fecha objetivo | Cambios |
|---|---|---|
| v1.0 | Mes 1 (pre-launch) | LoRA base, dataset 200 imgs |
| v1.1 | Mes 3 | Dataset ampliado (300), corrección anatomía |
| v1.2 | Mes 6 | Variaciones estacionales (Navidad, Año Nuevo, Día del Camarón) |
| v2.0 | Año 1 cierre | Re-entrenamiento completo con feedback Guardianes |
| v2.5 | Año 2 | Avatares animados (img2vid básico) |
| v3.0 | Año 3 | Avatar interactivo con voz (TTS Ecuaman) |

### A/B testing
- 5% de Guardianes nuevos reciben avatar de **modelo candidato** (vN+1).
- Encuesta opt-in: "¿qué tan satisfecho estás con tu avatar?" (1-5).
- Promoción a producción si vN+1 supera vN en satisfacción y métricas
  de calidad automatizadas.

---

## 9. OBSERVABILIDAD

### Métricas
- Avatares generados: total, por hora, por país.
- Tiempo medio P50/P95/P99.
- Tasa de éxito (sin reintento, con 1 reintento, fallback).
- Costo acumulado mensual.
- Satisfacción Guardiana (NPS específico de avatar, encuesta tras 7 días).

### Alertas
- Cola > 500 trabajos pendientes → escalar workers.
- Tasa de fallback > 5% → revisar modelo o prompt.
- Costo > $1.500/mes → revisar volumen y optimizaciones.

---

## 10. CHECKLIST DE ENTREGA

- [ ] Dataset 200+ imágenes curadas y aprobadas por Director de Marca
- [ ] LoRA v1.0 entrenado y validado por jurado interno
- [ ] Endpoint `/avatar/generate` funcional con tests
- [ ] Worker de cola con métricas Sentry + Logtail
- [ ] Almacenamiento R2 + CDN configurado
- [ ] Clasificador de calidad automatizado deployado
- [ ] Avatares "fallback ceremonial" diseñados (12)
- [ ] Términos de propiedad de avatar publicados en `/legal/terminos`
- [ ] Procedimiento de reentrenamiento documentado en `/docs/ml/`
- [ ] Plan de monitoreo semanal con review de muestras

---

*"Cada Guardián recibe un Ecuaman que solo existe para él. Esa unicidad
no es un truco técnico — es un acto de respeto. Por eso la máquina aquí
no improvisa: nos sirve, dentro de un manual estricto."*

— Generador de Avatares LoRA · Mayo 2026
