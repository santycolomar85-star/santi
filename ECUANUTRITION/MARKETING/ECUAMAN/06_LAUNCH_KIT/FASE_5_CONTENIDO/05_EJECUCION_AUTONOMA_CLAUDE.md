# EJECUCIÓN AUTÓNOMA — Cómo Claude puede generar y publicar solo
### Stack técnico para que el sistema funcione sin intervención humana diaria

> **Visión:** Una vez configurado este sistema, Claude (en sesiones
> futuras o en un agente desplegado) puede generar las imágenes,
> redactar el copy contextual, programar las publicaciones, responder
> comentarios — todo bajo aprobación humana del Brand Manager.
>
> **Este documento es el plano técnico para construirlo.**

---

## 🛠️ LO QUE CLAUDE PUEDE HACER HOY (sin nuevo setup)

| Capacidad | Estado actual | Notas |
|---|---|---|
| Escribir copy y captions | ✅ Disponible | Usando Banco de Voz |
| Generar prompts para IA visual | ✅ Disponible | Listos en este repo |
| Gestión de archivos del repositorio | ✅ Disponible | Bash + Edit + Write |
| Lectura de Drive | ✅ Disponible | MCP Drive activo |
| Gestión GitHub (PRs, issues, comentarios) | ✅ Disponible | MCP GitHub activo |
| Búsqueda web (lectura) | ✅ Disponible | WebFetch + WebSearch |
| Lectura/análisis de imágenes | ✅ Disponible | Read tool acepta imágenes |
| Comunicación con usuario | ✅ Disponible | Texto |

## ⚠️ LO QUE CLAUDE NO PUEDE HACER HOY (necesita herramientas adicionales)

| Capacidad | Lo que falta | Solución |
|---|---|---|
| Generar imágenes en Midjourney directamente | Tool / API de Midjourney | Setup vía Discord bot + API |
| Generar imágenes en DALL·E 3 directamente | API key de OpenAI conectada como tool | Setup vía API |
| Generar videos en Veo / Sora | API correspondiente | Pendiente disponibilidad de API |
| Publicar en Instagram | Meta Graph API + tool | Setup vía API empresarial |
| Publicar en TikTok | TikTok API + tool | Setup vía API empresarial |
| Publicar en YouTube | YouTube Data API + tool | Setup vía API |
| Publicar en X / Twitter | X API + tool | Setup vía API |

---

## 📐 ARQUITECTURA TÉCNICA RECOMENDADA

```
┌─────────────────────────────────────────────────────────────┐
│                    BRAND MANAGER (humano)                   │
│            Aprobación final de todo antes de publicar       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE AGENT                             │
│              (orchestrator del sistema)                     │
│  • Lee calendario editorial                                 │
│  • Genera prompts                                           │
│  • Llama APIs de generación                                 │
│  • Llama APIs de publicación                                │
│  • Reporta resultados                                       │
└──┬───────────┬────────────┬───────────┬───────────┬────────┘
   │           │            │           │           │
   ▼           ▼            ▼           ▼           ▼
┌──────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  ┌────────┐
│ Mid  │  │ DALL·E 3 │  │ Veo /    │  │ Meta   │  │ TikTok │
│ jour │  │  (API)   │  │ Sora     │  │ Graph  │  │  API   │
│ ney  │  │          │  │ (API)    │  │ API    │  │        │
└──────┘  └──────────┘  └──────────┘  └────────┘  └────────┘
   │           │            │           │           │
   ▼           ▼            ▼           ▼           ▼
              GENERA                    PUBLICA
                ↓                          ↓
         ┌─────────────┐            ┌──────────┐
         │ Drive /     │            │  Redes   │
         │  Repo       │            │  sociales│
         └─────────────┘            └──────────┘
```

---

## 🔧 STACK TÉCNICO POR COMPONENTE

### 1. Generación de imágenes — 3 opciones

#### Opción A — Midjourney vía Discord bot
- **Cómo funciona:** Discord no tiene API oficial de Midjourney, pero
  hay servicios que actúan como puente:
  - [GoAPI.ai Midjourney](https://www.goapi.ai/) — pago, ~$0.05/imagen
  - [ImagineAPI](https://imagineapi.dev/) — pago
  - [ApiFrame](https://www.apiframe.pro/) — pago
- **Setup:** suscripción + API key + tool MCP custom
- **Costo:** ~$50-100/mes según volumen

#### Opción B — DALL·E 3 vía OpenAI API (RECOMENDADA)
- **Cómo funciona:** OpenAI tiene API oficial limpia
- **Endpoint:** `https://api.openai.com/v1/images/generations`
- **Modelo:** `dall-e-3` (alta calidad)
- **Costo:** $0.04/imagen estándar, $0.08/imagen HD
- **Ventaja:** integración directa, autorizada, estable

#### Opción C — Stable Diffusion / Flux self-hosted
- **Cómo funciona:** modelo entrenado con LoRA Ecuaman propio
- **Hosting:** Replicate, Modal, RunPod, o servidor propio
- **Costo:** ~$0.01/imagen una vez entrenado el LoRA
- **Ventaja:** control total + consistencia garantizada de marca

### 2. Generación de videos — 2 opciones

#### Opción A — Veo (Google) o Sora (OpenAI)
- **Estado:** ambas APIs estaban en preview limitado
- **Cuándo:** verificar disponibilidad
- **Costo:** estimado $0.50-$2.00 por video corto

#### Opción B — Runway Gen-3 / Luma Dream Machine / Pika
- **APIs disponibles:**
  - Runway: api.runwayml.com
  - Luma: lumalabs.ai/api
  - Pika: pika.art/api
- **Costo:** $0.10-$0.50 por video corto

#### Opción C — Manual con animador humano
- Para episodios mini-serie de calidad cinematográfica
- Costo: $1,500-$8,000 por episodio

### 3. Publicación en redes — APIs oficiales

#### Meta (Instagram + Facebook)
- **API:** Meta Graph API
- **Requisito:** Business Account verificada + App de desarrollo aprobada
- **Capacidades:**
  - Publicar en feed
  - Publicar Reels (con limitaciones)
  - Programar publicaciones
  - Leer comentarios y responder
  - Acceso a métricas

#### TikTok
- **API:** TikTok for Business + Content Posting API
- **Requisito:** cuenta empresarial + aprobación
- **Capacidades:** publicar videos, leer métricas

#### YouTube
- **API:** YouTube Data API v3
- **Requisito:** cuenta de Google Cloud + OAuth
- **Capacidades:** subir videos, programar, gestionar comentarios

#### X / Twitter
- **API:** X API v2 (suscripción Basic $100/mes o superior)
- **Capacidades:** publicar tweets, threads, leer/responder

---

## 📂 ESTRUCTURA DE REPOSITORIO PARA AUTOMATIZACIÓN

```
ECUANUTRITION/MARKETING/ECUAMAN/
├── 08_AUTOMATION/
│   ├── claude_agent_config.json       Configuración del agente
│   ├── posting_schedule.json          Calendario en formato máquina
│   ├── content_pipeline/
│   │   ├── 01_to_generate/            Pendientes de generar
│   │   ├── 02_in_review/              En revisión humana
│   │   ├── 03_approved/               Aprobados, listos para publicar
│   │   └── 04_published/              Ya publicados con métricas
│   ├── api_keys.env (NO COMMITTED)    Variables de entorno
│   ├── scripts/
│   │   ├── generate_image.py
│   │   ├── post_to_instagram.py
│   │   ├── post_to_tiktok.py
│   │   ├── post_to_youtube.py
│   │   ├── post_to_twitter.py
│   │   └── monitor_engagement.py
│   └── reports/                       Reportes diarios automatizados
```

---

## 📜 SCRIPT EJEMPLO — Generación de imagen con DALL·E 3

```python
# scripts/generate_image.py

import os
import requests
import json
from datetime import datetime
from pathlib import Path

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
ECUAMAN_BASE_PROMPT = open('prompts/master_ecuaman.txt').read()

def generate_image(scenario_prompt: str, output_dir: str) -> str:
    """
    Genera una imagen de Ecuaman para un escenario específico.

    Args:
        scenario_prompt: descripción específica del momento (e.g., "saludando al amanecer")
        output_dir: ruta donde guardar la imagen

    Returns:
        path del archivo generado
    """
    full_prompt = f"{ECUAMAN_BASE_PROMPT}\n\nESCENA ESPECÍFICA: {scenario_prompt}"

    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={'Authorization': f'Bearer {OPENAI_API_KEY}'},
        json={
            'model': 'dall-e-3',
            'prompt': full_prompt,
            'size': '1024x1024',
            'quality': 'hd',
            'n': 1
        }
    )

    if response.status_code != 200:
        raise Exception(f"Generation failed: {response.text}")

    image_url = response.json()['data'][0]['url']
    image_data = requests.get(image_url).content

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = Path(output_dir) / f'ecuaman_{timestamp}.png'

    with open(output_path, 'wb') as f:
        f.write(image_data)

    return str(output_path)


# Uso:
if __name__ == '__main__':
    path = generate_image(
        scenario_prompt="Ecuaman saludando con la mano en el primer amanecer de Manabí, modo cálido",
        output_dir="content_pipeline/02_in_review/"
    )
    print(f"Generated: {path}")
```

---

## 📜 SCRIPT EJEMPLO — Publicación a Instagram

```python
# scripts/post_to_instagram.py

import os
import requests
from datetime import datetime

META_ACCESS_TOKEN = os.environ['META_ACCESS_TOKEN']
INSTAGRAM_ACCOUNT_ID = os.environ['INSTAGRAM_ACCOUNT_ID']

def post_image_to_instagram(image_url: str, caption: str) -> dict:
    """
    Publica una imagen en Instagram via Meta Graph API.

    Args:
        image_url: URL pública de la imagen (ya subida a CDN)
        caption: caption con hashtags

    Returns:
        respuesta del API
    """
    # Paso 1: crear container
    container_response = requests.post(
        f'https://graph.facebook.com/v21.0/{INSTAGRAM_ACCOUNT_ID}/media',
        params={
            'image_url': image_url,
            'caption': caption,
            'access_token': META_ACCESS_TOKEN
        }
    )
    container_id = container_response.json()['id']

    # Paso 2: publicar el container
    publish_response = requests.post(
        f'https://graph.facebook.com/v21.0/{INSTAGRAM_ACCOUNT_ID}/media_publish',
        params={
            'creation_id': container_id,
            'access_token': META_ACCESS_TOKEN
        }
    )

    return publish_response.json()


# Uso:
if __name__ == '__main__':
    result = post_image_to_instagram(
        image_url='https://cdn.ecuanutrition.com/ecuaman_dia1.png',
        caption='Buenos días, mareas. ☀️🌊\n\n#LaMarea #Ecuaman'
    )
    print(f"Posted: {result}")
```

---

## 🔁 FLUJO DIARIO AUTOMATIZADO

### Cada noche 22:00 (cron job)

```
1. Claude Agent lee posting_schedule.json
2. Identifica posts a publicar mañana
3. Para cada post:
   a) Lee el copy del calendario
   b) Genera imagen/video con prompt asignado
   c) Sube a 02_in_review/
   d) Notifica al Brand Manager por email/Slack
4. Brand Manager revisa antes de las 8:00 AM
5. Si aprueba → Claude publica a hora programada
6. Si rechaza → Claude regenera con feedback
7. Post-publicación: monitorea métricas en tiempo real
8. Reporta a final del día
```

### Aprobación del Brand Manager

Sistema simple:
- Email con thumbnail + caption + botones "Aprobar" / "Regenerar"
- Slack workflow con vista previa
- Microsite admin con calendario visual
- Tiempo límite: 2 horas para aprobar (si no, falla en seguro)

---

## 🔐 SEGURIDAD Y APROBACIÓN

### Reglas inquebrantables del agente

```
1. NUNCA publicar sin aprobación explícita del Brand Manager
2. NUNCA cambiar el manual de marca sin autorización escrita
3. NUNCA responder a temas políticos partidistas
4. NUNCA usar el personaje en contextos contrarios a la biblia
5. NUNCA exceder presupuesto de paid media sin autorización
6. SIEMPRE registrar cada acción en log auditable
7. SIEMPRE escalar dudas al Brand Manager
8. SIEMPRE pasar checklist 24 puntos antes de publicar imagen
```

### Auditoría

```
LOG diario en formato JSON:
{
  "date": "2026-06-15",
  "actions": [
    {
      "time": "22:01",
      "action": "generate_image",
      "prompt": "...",
      "output_path": "...",
      "approved_by": "brand_manager_id",
      "approved_at": "2026-06-16T07:30",
      "published_at": "2026-06-16T11:00",
      "platform": "instagram",
      "post_url": "...",
      "engagement_24h": {...}
    },
    ...
  ]
}
```

---

## 💰 COSTO MENSUAL ESTIMADO DEL SISTEMA AUTOMATIZADO

| Componente | Costo/mes |
|---|---|
| OpenAI API (DALL·E 3) — 100 imgs/mes | $4-8 |
| Anthropic API (Claude para textos) — moderado | $30-100 |
| Runway / Luma video — 30 videos/mes | $30-150 |
| Hosting infraestructura (Vercel + workers) | $20-100 |
| Meta Business / TikTok / X APIs (cuotas) | $0-200 |
| Slack / monitoring (alertas) | $0-50 |
| Storage (Drive + S3 backup) | $10-50 |
| **TOTAL mensual** | **$94-658** |

ROI: si la automatización ahorra 1 FTE de community manager senior
(~$2,000-3,500/mes) + acelera ejecución, el ROI es 3-30x.

---

## 🚀 ROADMAP DE IMPLEMENTACIÓN

### Mes 1 — Fundación
- [ ] Setup OpenAI API + DALL·E 3
- [ ] Setup Meta Graph API + Instagram Business Account
- [ ] Test de generación + publicación manual
- [ ] Aprobación legal del flujo automatizado

### Mes 2 — Pilot
- [ ] Configurar agente Claude con tools MCP custom
- [ ] Pilot con 5 posts/semana totalmente automatizados (con aprobación humana)
- [ ] Métricas y ajustes

### Mes 3 — Expansión
- [ ] Agregar TikTok publishing
- [ ] Agregar YouTube publishing
- [ ] Agregar X publishing
- [ ] Llegar a 30 posts/mes automatizados con aprobación

### Mes 4-6 — Optimización
- [ ] LoRA Ecuaman entrenado para SDXL (control total)
- [ ] Generación de Reels automatizada con Runway
- [ ] Sistema de respuestas a comentarios con aprobación

### Mes 7+ — Autonomía supervisada
- [ ] Brand Manager solo aprueba lo que la confianza humana requiera
- [ ] El resto del flujo es completamente automático
- [ ] Reportes ejecutivos mensuales generados por el agente

---

## 📞 LO QUE NECESITO DEL USUARIO (santycolomar85-star) PARA EJECUTAR

Si quieres que yo (Claude) empiece a ejecutar este sistema en sesiones
futuras, configura una de estas vías:

### Vía rápida (recomendada para empezar)
- **OpenAI API key** (para DALL·E 3 + Claude API)
- **Meta Graph API** access token (para publicar en IG/FB)
- **Microsoft / Anthropic MCP server** custom donde estos accesos
  estén configurados como tools

### Vía intermedia
- Suscripción a servicio puente Midjourney (GoAPI.ai o ImagineAPI)
- API keys de cada plataforma de redes
- Drive con permisos de escritura

### Vía completa
- Stack técnico completo descrito en este documento
- Servidor con cron jobs corriendo
- Slack/email para aprobaciones del Brand Manager

---

## ✅ DECLARACIÓN HONESTA

> En la sesión actual de Claude (Mayo 2026), **NO tengo herramientas
> directas de Midjourney, DALL·E, Veo o publicación en redes.**
>
> Lo que SÍ tengo:
> - Acceso a Drive (para leer tus archivos)
> - GitHub (para gestionar el repo)
> - Bash / Edit / Write (para crear y modificar archivos)
> - WebFetch / WebSearch (para leer la web)
>
> Lo que necesitas para que ejecute generación + publicación
> autónomamente: configurar las APIs descritas arriba como **tools MCP**
> en una próxima sesión, o desplegarme como agente con esas tools
> conectadas.
>
> Mientras tanto: yo genero todos los **prompts perfectos**, todo el
> **copy listo para publicar**, y toda la **estructura de archivos**.
> Tu equipo ejecuta el último paso (cargar prompts en Midjourney,
> publicar en redes) — o configuramos el sistema autónomo descrito
> aquí.

---

*Versión 1.0 — Mayo 2026*
*Implementación recomendada: tras validar el primer mes manualmente*
