# GENERADOR DE AVATARES — LoRA ECUAMAN
### Sistema de generación de avatar único por Guardián, manteniendo canon visual

> Cada Guardián recibe un **avatar de Ecuaman único en el mundo**.
> No es una foto del personaje genérico — es **su Ecuaman personal**,
> con variaciones controladas que mantienen la coherencia visual del
> canon. Esto requiere entrenar un **modelo LoRA propio** sobre las 34+
> imágenes canónicas que ya tenemos en `07_ASSETS_OFICIALES/`.

---

## 1. POR QUÉ NO BASTA gpt-image-1 / DALL·E / Midjourney CRUDOS

Probamos en Fase 1 generar variantes con prompts crudos. Resultados:

- **Inconsistencia anatómica:** algunas iteraciones humanizan la figura.
- **Drift de color:** la capa pasa de azul real a turquesa o verde.
- **Pérdida del medallón:** el "E" dorado desaparece o cambia forma.
- **Variabilidad de antenas:** a veces no salen, a veces salen 4.

Conclusión: **necesitamos un LoRA propio entrenado con nuestras 34+
imágenes canónicas** + prompts plantilla con control fino.

---

## 2. ENFOQUE TÉCNICO RECOMENDADO

### Stack
- **Modelo base:** SDXL 1.0 (más rápido y barato que SD3, suficiente calidad)
- **Técnica:** **LoRA** (Low-Rank Adaptation) — 8-32 MB, rápido de entrenar
- **Dataset:** 34 imágenes canónicas + 4 que faltan (Midjourney) = **38 imágenes**
- **Augmentación:** flip horizontal, crops centrados, zoom 0.9-1.1×
- **Resolución entrenamiento:** 1024×1024 (SDXL nativo)
- **Steps:** 2.000-3.000 (sweet spot para 38 imágenes)
- **Servicio:** **Replicate** (training + inference) — pago por uso, no requiere GPU propia

### Por qué Replicate
- Training: ~$5-15 por entrenamiento completo
- Inference: $0.0023 por segundo en A40 (≈ $0.01-0.05 por avatar)
- Sin gestión de infra
- Fallback alternativo: RunPod si volumen >5.000 avatares/día

---

## 3. PIPELINE DE ENTRENAMIENTO

### Paso 1 — Curación del dataset (1 día)

```
input/
  ├── 00_DAY0_MASTER_HEROIC_VERTICAL_v2.png   ← MASTER, peso x2
  ├── 10_DAY1_buenos_dias.png
  ├── 11_DAY2_celebration.png
  ├── ...
  └── (38 archivos en total)

caption/  (tu carpeta de captions, una por imagen)
  ├── 00_DAY0_MASTER_HEROIC_VERTICAL_v2.txt
  ├── 10_DAY1_buenos_dias.txt
  └── ...
```

**Caption canónico** (ejemplo de uno de los archivos `.txt`):

```
ecuaman, anatomically accurate Penaeus vannamei superhero shrimp,
royal blue cape, cyan trident, golden E medallion, antennae with
red and yellow Ecuadorian tassels, electric blue belt,
Pixar 3D semi-realistic style, vibrant orange shrimp body
```

**Token único:** `ecuaman` (no usar palabras genéricas como "shrimp" solas).

### Paso 2 — Configuración del entrenamiento

```yaml
# replicate-train-config.yaml
input_images: dataset.zip
trigger_word: ecuaman
training_steps: 2500
lora_rank: 32
learning_rate: 0.0004
batch_size: 1
resolution: 1024
optimizer: adamw8bit
caption_dropout_rate: 0.05  # 5% sin caption para robustez
```

### Paso 3 — Lanzamiento

```bash
replicate train ostris/flux-dev-lora-trainer \
  --input "$(cat replicate-train-config.json)" \
  --destination "ecuanutrition/ecuaman-lora"
```

(O por API desde GitHub Actions, ver workflow al final.)

### Paso 4 — Validación de calidad

Generar **20 imágenes test con prompts canónicos** y validar contra
checklist 24 puntos (`03_REFERENCIAS/CHECKLIST_VALIDACION.md`).

Criterio de aprobación: **>85% pasan checklist completo**.

Si <85%, ajustar:
- subir steps a 3.500
- bajar learning rate a 0.0002
- añadir más imágenes (regenerar las 4 pendientes en Midjourney)

---

## 4. PROMPT TEMPLATE PARA GENERACIÓN DE AVATAR DE GUARDIÁN

```typescript
function buildPrompt(rasgos: GuardianRasgos): string {
  const { capa, accesorio, expresion } = rasgos;

  const capaMap = {
    'azul-real':       'royal blue cape',
    'cian-profundo':   'deep cyan cape',
    'rojo-coral':      'coral red cape',
    'verde-manglar':   'mangrove green cape',
    'dorado-patrimonial': 'royal gold cape with bronze accents',
  };

  const accesorioMap = {
    'tridente':        'cyan trident raised in right hand',
    'lanza-coral':     'coral spear raised in right hand',
    'sin-arma':        'open hand raised, palm forward, no weapon',
  };

  const expresionMap = {
    'heroico':         'heroic determined gaze, slight smile',
    'sereno':          'calm contemplative expression',
    'risueno':         'joyful warm smile, eyes crinkled',
  };

  return `ecuaman, anatomically accurate Penaeus vannamei superhero shrimp,
${capaMap[capa]}, ${accesorioMap[accesorio]}, golden E medallion on chest,
antennae with red and yellow Ecuadorian tassels, electric blue belt with
ECUAMAN text, vibrant orange shrimp body, ${expresionMap[expresion]},
Pacific Ocean dawn background, Pixar 3D semi-realistic style,
heroic portrait, centered composition, neutral background gradient`;
}

const NEGATIVE_PROMPT = `human face, human body, human hands, child,
realistic photo, watermark, signature, text artifacts, deformed anatomy,
extra limbs, blurry, low quality, dark muddy colors, cartoon flat 2D,
multiple shrimp, multiple medallions`;
```

---

## 5. PARÁMETROS DE INFERENCIA

```typescript
const inferenceParams = {
  prompt: buildPrompt(rasgos),
  negative_prompt: NEGATIVE_PROMPT,
  lora_scale: 0.95,         // peso del LoRA Ecuaman
  num_inference_steps: 35,  // sweet spot calidad/velocidad SDXL
  guidance_scale: 7.5,
  width: 1024,
  height: 1024,
  seed: hashGuardianId(guardianId),  // determinismo por Guardián
  scheduler: 'DPMSolverMultistep',
};
```

**Determinismo del seed:**

```typescript
function hashGuardianId(id: string): number {
  // Convierte UUID a int32 estable
  const hash = createHash('sha256').update(id).digest();
  return hash.readUInt32BE(0); // 0 - 2^32-1
}
```

Esto garantiza que **regenerar el avatar con el mismo Guardián + mismos
rasgos da exactamente el mismo resultado** (reproducibilidad legal y
para soporte).

---

## 6. PIPELINE EN PRODUCCIÓN

```
job: avatar.generar
├── 1. Validar input (rasgos Zod)
├── 2. Buscar avatar previo en cache (mismo guardian + rasgos)
│       → si existe, devolver URL
├── 3. POST a Replicate /predictions con prompt + LoRA
├── 4. Polling cada 2s (max 90s timeout)
├── 5. Descargar imagen 1024
├── 6. Generar derivados:
│       - 512 (perfil web)
│       - 256 (thumbnail)
│       - 1024 con crop circular para Pasaporte
├── 7. Subir las 4 versiones a Cloudflare R2
├── 8. INSERT avatares row con URLs + metadata
├── 9. UPDATE pasaportes set version = version (no incrementa por avatar)
├── 10. Trigger pasaporte.regenerar (dependencia)
└── 11. Notificar al frontend vía SSE / WebSocket
```

### Manejo de fallos

| Error | Acción |
|---|---|
| Replicate timeout | retry 1 vez con seed +1 |
| Replicate quota | encolar en Bull con backoff exponencial |
| Imagen no pasa NSFW check | regenerar con seed +7 |
| Imagen no pasa checklist anatómico | regenerar con seed +13 (max 3 intentos) |
| 3 fallos consecutivos | usar avatar fallback (master canónico de la rasgo más cercana) y notificar admin |

### Validación automática post-generación

Detector de calidad simple, basado en CLIP embeddings comparados con
master canónico:

```python
# similarity threshold: 0.78 (calibrar empíricamente)
similarity = clip.cosine(master_embedding, new_avatar_embedding)
if similarity < 0.78:
    return retry_with_new_seed()
```

---

## 7. COSTO POR AVATAR

| Componente | Costo |
|---|---|
| Inferencia Replicate (35 steps SDXL+LoRA) | ~$0.012 |
| Storage R2 (4 versiones × 1 MB ≈ 4 MB) | ~$0.00006 |
| Egress CDN Cloudflare | $0 |
| **Total por avatar generado** | **~$0.012 - $0.015** |
| **Total con regeneración (max 2 por usuario)** | **~$0.04** |

A 100.000 Guardianes: ~$1.500 en costos de generación de avatares.
A 1.000.000 Guardianes: ~$15.000.

---

## 8. ALTERNATIVA / FALLBACK SIN LoRA

Si por algún motivo el LoRA no se entrena a tiempo, **plan B**:

1. Pre-generar **20 avatares canónicos** (combinaciones de capa × expresión × accesorio).
2. Cada Guardián recibe el avatar canónico que coincide con sus rasgos.
3. Personalización adicional sólo en el Pasaporte (color overlay del marco, número).

Esto cambia el discurso ("avatar único" → "avatar de tu rama"), pero
permite lanzar sin bloqueo. Migrar a LoRA en versión 2.0.

---

## 9. GitHub Action — entrenamiento automatizado

```yaml
# .github/workflows/train-lora.yml
name: Train Ecuaman LoRA
on:
  workflow_dispatch:
    inputs:
      version_label:
        description: 'Versión semver del LoRA'
        required: true
        default: '1.0.0'

jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build dataset zip
        run: |
          cd ECUANUTRITION/MARKETING/ECUAMAN/07_ASSETS_OFICIALES/auto_generated
          zip -r dataset.zip *.png ../captions/*.txt
      - name: Upload dataset to R2
        run: |
          aws s3 cp dataset.zip s3://ecuaman-training/${{ inputs.version_label }}/dataset.zip \
            --endpoint-url ${{ secrets.R2_ENDPOINT }}
      - name: Trigger Replicate training
        env:
          REPLICATE_API_TOKEN: ${{ secrets.REPLICATE_API_TOKEN }}
        run: |
          curl -X POST https://api.replicate.com/v1/trainings \
            -H "Authorization: Token $REPLICATE_API_TOKEN" \
            -H "Content-Type: application/json" \
            -d @config/replicate-train-${{ inputs.version_label }}.json
```

---

## 10. CONSIDERACIONES ÉTICAS Y LEGALES

- **Avatares de menores:** los <13 reciben avatar genérico (no identifiable),
  nunca con cara/rasgos personalizables que puedan asociarse con apariencia real.
- **No generar parecidos a celebridades** — prompt template lo evita.
- **Marca de agua invisible** (DCT watermark) en cada avatar para
  trazabilidad si alguien lo usa fuera de contexto.
- **Términos:** el Guardián recibe **licencia personal no transferible**
  para uso del avatar. La propiedad intelectual del modelo y derivados
  permanece en Ecuanutrition.
- **Consentimiento de regeneración:** el Guardián autoriza explícitamente
  el reentrenamiento del LoRA con sus avatares (anonimizados).

---

## 11. CHECKLIST DE LANZAMIENTO DEL GENERADOR

- [ ] Dataset de 38 imágenes curado y etiquetado
- [ ] LoRA v1 entrenado, ratio aprobación ≥85% en muestra test
- [ ] Worker async funcional con retries y fallback
- [ ] Detección de calidad CLIP funcionando, threshold calibrado
- [ ] Carbon footprint del modelo medido y comunicado
- [ ] Watermark invisible aplicado en todos los outputs
- [ ] Política de uso del avatar clara en términos
- [ ] Sandbox público (`/playground` con rate limit) para que prensa pruebe sin registrarse
- [ ] Plan B (avatares canónicos pre-generados) listo como fallback
- [ ] Costo de generación monitoreado en dashboard

---

*El generador de avatares es **el truco mágico** del lanzamiento. Es lo
que convierte "campaña" en "experiencia personal". Vale la pena
invertir tiempo en entrenarlo bien antes de lanzar.*
