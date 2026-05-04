# ESPECIFICACIÓN TÉCNICA — PLATAFORMA "LA MAREA DE LOS GUARDIANES"
### Stack, arquitectura, modelo de datos y endpoints, listo para entregar a desarrollo

> Este documento es el **brief técnico que un equipo de ingeniería puede
> ejecutar sin más conversación**. Define stack, datos, endpoints, jobs,
> seguridad, escalado y observabilidad.

---

## 1. ARQUITECTURA DE ALTO NIVEL

```
                            ┌──────────────────────┐
                            │  CDN Cloudflare      │
                            │  (cache estático,    │
                            │   imágenes, fonts)   │
                            └──────────┬───────────┘
                                       │
      ┌────────────────────────────────┼────────────────────────────┐
      │                                │                            │
┌─────▼──────┐                ┌────────▼────────┐         ┌─────────▼────────┐
│  WEB       │                │   APP iOS       │         │   APP Android    │
│  Next.js   │                │   React Native  │         │   React Native   │
│  Vercel    │                │   Expo          │         │   Expo           │
└─────┬──────┘                └────────┬────────┘         └─────────┬────────┘
      │                                │                            │
      └────────────────────────────────┼────────────────────────────┘
                                       │
                              ┌────────▼─────────┐
                              │  API GATEWAY     │
                              │  Bun + Hono      │
                              │  Edge functions  │
                              └────────┬─────────┘
                                       │
   ┌──────────────┬──────────────┬─────┴──────────┬──────────────┐
   │              │              │                │              │
┌──▼──┐     ┌─────▼────┐    ┌────▼────┐     ┌─────▼────┐    ┌────▼────┐
│ DB  │     │  Redis   │    │  R2     │     │ Replicate│    │ Resend  │
│Neon │     │ Upstash  │    │ Cloud-  │     │  LoRA    │    │ Email   │
│PG   │     │ (cache + │    │ flare   │     │ Avatares │    │         │
│     │     │  queues) │    │ (assets)│     │          │    │         │
└─────┘     └──────────┘    └─────────┘     └──────────┘    └─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │  Workers Fly.io  │
                              │  (jobs async:    │
                              │  PDF, avatar,    │
                              │  email, QR)      │
                              └──────────────────┘
```

---

## 2. STACK DEFINITIVO

### Frontend Web (microsite ecuaman.ec)
- **Framework:** Next.js 15 (App Router, RSC, Server Actions)
- **Estilos:** Tailwind CSS v4 + custom theme (paleta Ecuaman)
- **Animación:** Framer Motion + Lottie (animaciones específicas Ecuaman)
- **Forms:** React Hook Form + Zod
- **Estado:** Zustand (cliente) + TanStack Query (server state)
- **i18n:** next-intl (ES, EN, PT, FR)
- **Hosting:** Vercel Pro

### Backend / API
- **Runtime:** Bun ≥1.1
- **Framework:** Hono (edge-friendly, fast)
- **Validación:** Zod compartido con frontend
- **ORM:** Drizzle ORM
- **Auth:** Clerk (OAuth Google/Apple/Facebook + email + magic link)
- **Hosting API gateway:** Vercel Edge / Fly.io según latencia

### Base de datos
- **Primary:** Postgres 16 en Neon (autoscale, branching para dev/prod)
- **Cache + colas:** Redis en Upstash (BullMQ-compatible)
- **Search:** Postgres full-text inicialmente, migrar a Meilisearch a >100k Guardianes

### Storage
- **Imágenes y PDFs:** Cloudflare R2 (sin egress)
- **CDN:** Cloudflare propio frente a R2

### Servicios externos
- **AI Avatares:** Replicate con LoRA propio (ver `04_GENERADOR_AVATARES.md`)
- **PDF Pasaporte:** PDFKit (Node) en worker Fly.io
- **QR:** `qrcode` npm en worker
- **Email:** Resend
- **Pagos:** Stripe + PayPal + PayPhone (Ecuador)
- **SMS (opcional):** Twilio (recovery + alertas)

### Mobile
- **Framework:** React Native con Expo SDK 52+
- **Navegación:** Expo Router (file-based)
- **Estado:** mismo Zustand del web (paquete compartido)
- **Push:** Expo Notifications
- **Build:** EAS Build + EAS Submit

### DevOps
- **CI/CD:** GitHub Actions
- **Repos:** monorepo con Turborepo (apps/web, apps/mobile, apps/api,
  packages/ui, packages/db, packages/types)
- **Secrets:** Vercel Env + Doppler
- **Monitoring:** PostHog + Sentry + UptimeRobot
- **Logs:** Axiom (200GB/mes free)

---

## 3. MODELO DE DATOS (POSTGRES)

```sql
-- ====== USUARIOS Y GUARDIANES ======

CREATE TABLE guardianes (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  numero          BIGSERIAL UNIQUE NOT NULL, -- número de Guardián correlativo
  email           VARCHAR(255) UNIQUE NOT NULL,
  nombre          VARCHAR(120) NOT NULL,
  pais_iso        CHAR(2) NOT NULL,
  ciudad          VARCHAR(120),
  fecha_registro  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  fecha_nacimiento DATE, -- para gating de menores (COPPA)
  es_menor        BOOLEAN GENERATED ALWAYS AS
                  (fecha_nacimiento IS NOT NULL AND
                   AGE(fecha_nacimiento) < INTERVAL '13 years') STORED,
  consentimiento_tutor_email VARCHAR(255), -- requerido si es_menor
  estado          VARCHAR(20) NOT NULL DEFAULT 'activo'
                  CHECK (estado IN ('activo','pausado','baja','baneado')),
  preferencias    JSONB NOT NULL DEFAULT '{}'::jsonb,
  ip_registro     INET,
  user_agent      TEXT,
  metadata        JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_guardianes_pais ON guardianes(pais_iso);
CREATE INDEX idx_guardianes_estado ON guardianes(estado);
CREATE INDEX idx_guardianes_fecha ON guardianes(fecha_registro);

-- ====== PASAPORTES ======

CREATE TABLE pasaportes (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guardian_id     UUID NOT NULL REFERENCES guardianes(id) ON DELETE CASCADE,
  serial          VARCHAR(20) UNIQUE NOT NULL, -- formato ECM-AAAA-NNNNNN
  qr_token        VARCHAR(64) UNIQUE NOT NULL, -- token hash para perfil público
  pdf_url         TEXT, -- en R2
  emitido_en      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  vigencia        VARCHAR(20) NOT NULL DEFAULT 'vitalicio',
  versión         INTEGER NOT NULL DEFAULT 1, -- por re-emisión
  metadata        JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE UNIQUE INDEX idx_pasaportes_guardian ON pasaportes(guardian_id);

-- ====== AVATARES ======

CREATE TABLE avatares (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guardian_id     UUID NOT NULL REFERENCES guardianes(id) ON DELETE CASCADE,
  url_512         TEXT NOT NULL,
  url_1024        TEXT NOT NULL,
  url_pasaporte   TEXT NOT NULL, -- recortado para pasaporte
  prompt_seed     INTEGER NOT NULL,
  lora_version    VARCHAR(20) NOT NULL,
  rasgos          JSONB NOT NULL DEFAULT '{}'::jsonb, -- color cape, accesorios
  costo_centavos  INTEGER NOT NULL DEFAULT 0,
  generado_en     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  aprobado        BOOLEAN NOT NULL DEFAULT TRUE,
  motivo_rechazo  TEXT
);

CREATE INDEX idx_avatares_guardian ON avatares(guardian_id);

-- ====== MISIONES Y MEDALLAS ======

CREATE TABLE misiones (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  codigo          VARCHAR(60) UNIQUE NOT NULL,
  titulo          VARCHAR(160) NOT NULL,
  descripcion     TEXT NOT NULL,
  categoria       VARCHAR(40) NOT NULL, -- manglar, alimentación, comunidad
  puntos          INTEGER NOT NULL DEFAULT 0,
  medalla_url     TEXT,
  vigente_desde   DATE NOT NULL DEFAULT CURRENT_DATE,
  vigente_hasta   DATE,
  metadata        JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE misiones_completadas (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guardian_id     UUID NOT NULL REFERENCES guardianes(id) ON DELETE CASCADE,
  mision_id       UUID NOT NULL REFERENCES misiones(id),
  evidencia_url   TEXT,
  validado_por    UUID, -- moderador
  validado_en     TIMESTAMPTZ,
  completada_en   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(guardian_id, mision_id)
);

CREATE INDEX idx_misiones_completadas_g ON misiones_completadas(guardian_id);

-- ====== ASAMBLEAS ======

CREATE TABLE asambleas (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  numero          INTEGER UNIQUE NOT NULL,
  titulo          VARCHAR(200) NOT NULL,
  fecha           TIMESTAMPTZ NOT NULL,
  agenda          TEXT NOT NULL,
  decision_final  TEXT,
  video_url       TEXT,
  participantes   INTEGER DEFAULT 0,
  estado          VARCHAR(20) NOT NULL DEFAULT 'programada'
                  CHECK (estado IN ('programada','en_vivo','cerrada','cancelada'))
);

CREATE TABLE asamblea_votos (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  asamblea_id     UUID NOT NULL REFERENCES asambleas(id) ON DELETE CASCADE,
  guardian_id     UUID NOT NULL REFERENCES guardianes(id) ON DELETE CASCADE,
  opcion          VARCHAR(60) NOT NULL,
  votado_en       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  UNIQUE(asamblea_id, guardian_id)
);

-- ====== DONACIONES Y CAUSAS ======

CREATE TABLE causas (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug            VARCHAR(100) UNIQUE NOT NULL,
  titulo          VARCHAR(200) NOT NULL,
  descripcion     TEXT NOT NULL,
  meta_centavos   BIGINT NOT NULL,
  recaudado_centavos BIGINT NOT NULL DEFAULT 0,
  imagen_url      TEXT,
  abierta         BOOLEAN NOT NULL DEFAULT TRUE,
  abre_en         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  cierra_en       TIMESTAMPTZ
);

CREATE TABLE donaciones (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  guardian_id     UUID REFERENCES guardianes(id) ON DELETE SET NULL,
  causa_id        UUID NOT NULL REFERENCES causas(id),
  monto_centavos  BIGINT NOT NULL CHECK (monto_centavos > 0),
  moneda          CHAR(3) NOT NULL DEFAULT 'USD',
  metodo_pago     VARCHAR(40) NOT NULL,
  stripe_payment_intent_id TEXT,
  estado          VARCHAR(20) NOT NULL DEFAULT 'pendiente'
                  CHECK (estado IN ('pendiente','confirmada','reembolsada','fallida')),
  creado_en       TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- ====== EVENTOS Y AUDITORÍA ======

CREATE TABLE eventos (
  id              BIGSERIAL PRIMARY KEY,
  guardian_id     UUID REFERENCES guardianes(id) ON DELETE SET NULL,
  tipo            VARCHAR(60) NOT NULL,
  payload         JSONB NOT NULL DEFAULT '{}'::jsonb,
  ip              INET,
  ocurrido_en     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_eventos_tipo_fecha ON eventos(tipo, ocurrido_en);
CREATE INDEX idx_eventos_guardian ON eventos(guardian_id, ocurrido_en);
```

---

## 4. ENDPOINTS DE LA API (REST + tRPC opcional)

### Públicos (sin auth)

```
GET   /api/v1/healthz                  → 200 si todo ok
GET   /api/v1/stats/publico            → totales: guardianes, manglares, países
GET   /api/v1/g/:qr_token              → perfil público de un Guardián
GET   /api/v1/causas                   → lista de causas activas
GET   /api/v1/causas/:slug             → detalle de causa
POST  /api/v1/auth/register            → crear Guardián (rate-limited)
POST  /api/v1/auth/login               → login
POST  /api/v1/auth/magic-link          → magic link
POST  /api/v1/donaciones/intent        → crear payment intent (Stripe)
POST  /api/v1/webhooks/stripe          → webhook pagos
```

### Privados (Bearer token Clerk)

```
GET   /api/v1/me                       → datos del Guardián actual
PATCH /api/v1/me                       → actualizar nombre/ciudad/preferencias
DELETE /api/v1/me                      → derecho al olvido (RGPD)
GET   /api/v1/me/pasaporte             → URL del PDF + datos
POST  /api/v1/me/pasaporte/regenerar   → re-emitir pasaporte (max 3/año)
GET   /api/v1/me/avatar                → URLs del avatar
POST  /api/v1/me/avatar/regenerar      → regenerar avatar (max 2)
GET   /api/v1/me/medallas              → medallas obtenidas
POST  /api/v1/me/misiones/:id/evidencia → subir evidencia para mision
GET   /api/v1/asambleas/proxima        → próxima asamblea
POST  /api/v1/asambleas/:id/voto       → emitir voto
```

### Admin (rol admin en Clerk)

```
GET   /admin/guardianes                → listado paginado
GET   /admin/guardianes/:id            → detalle + auditoría
POST  /admin/misiones                  → crear misión
PATCH /admin/misiones/:id              → editar
POST  /admin/asambleas                 → crear asamblea
POST  /admin/causas                    → crear causa
GET   /admin/dashboard                 → métricas en vivo
POST  /admin/moderar/:guardian_id      → banear/restaurar
```

### Rate limits (Upstash Redis)

| Endpoint | Límite | Ventana |
|---|---|---|
| `POST /auth/register` | 3 | 1h por IP |
| `POST /auth/login` | 10 | 15min por IP |
| `POST /me/avatar/regenerar` | 1 | 24h por usuario |
| `POST /donaciones/intent` | 30 | 1h por usuario |
| Cualquier otro | 100 | 1min por usuario |

---

## 5. JOBS ASYNC (BullMQ en Redis)

```
job: pasaporte.generar
  → input: { guardian_id }
  → output: pasaportes.pdf_url
  → SLA: <60s (p95)

job: avatar.generar
  → input: { guardian_id, prompt_seed?, rasgos? }
  → output: avatares row + 3 URLs en R2
  → SLA: <90s (p95) (depende de Replicate)

job: email.bienvenida
  → input: { guardian_id }
  → output: enviar email con pasaporte + login
  → SLA: <30s

job: qr.preview
  → input: { guardian_id }
  → output: PNG QR en R2

job: estadisticas.snapshot.diario
  → cron: 00:00 UTC
  → output: snapshot en Postgres para dashboards públicos

job: backup.diario
  → cron: 02:00 UTC
  → output: dump a R2 cifrado

job: cleanup.evidencias_pendientes
  → cron: cada 6h
  → output: notificar moderadores de evidencias >24h sin revisar
```

---

## 6. SEGURIDAD

### Aplicación

- **OWASP Top 10:** auditoría obligatoria pre-lanzamiento (npm audit + Snyk + checklist manual).
- **Zod en todo input.** Cero `any`, cero coerción implícita.
- **CSP estricta.** `default-src 'self'` + nonce en scripts.
- **CORS:** lista blanca (web propio + apps móviles).
- **Helmet en API.** HSTS, X-Frame-Options, etc.
- **CSRF:** doble token en formularios server actions.

### Datos

- **Cifrado at rest:** Postgres con `pgcrypto` para email + nombre + IP.
- **Cifrado en tránsito:** TLS 1.3 mínimo, HTTPS-only.
- **Secretos:** Doppler + rotación trimestral.
- **PII de menores:** *jamás* en logs ni en eventos analytics.
- **Consentimiento padres COPPA:** doble email-confirm + verificación humana.

### Operaciones

- **Logs sin PII.** Reglas Pino + redact.
- **Backups cifrados** en R2 (clave en KMS), retención 30 días.
- **Plan de respuesta a incidente** (`SECURITY_INCIDENT_PLAYBOOK.md` —
  pendiente, lo crea legal en Fase 3 ampliada).
- **Pen-test externo** anual (presupuesto: $5-10k).

### Auth

- **MFA opcional para Guardianes**, obligatoria para admins.
- **Sessions:** Clerk JWT, expiración 24h sliding, refresh rotation.
- **Lockout:** 5 intentos fallidos → 15 min bloqueo + email alerta.

---

## 7. OBSERVABILIDAD

- **Logs:** Pino → Axiom. Retención 30 días.
- **Métricas:** OpenTelemetry → Grafana Cloud (free tier).
- **Errores:** Sentry (front + back + mobile).
- **Producto:** PostHog (self-hosted o cloud).
- **Uptime:** UptimeRobot 1min interval, alerta a Slack + SMS.
- **SLOs:**
  - API p95 latencia < 300 ms
  - Disponibilidad > 99.9% (8.7h downtime/año máximo)
  - Errores 5xx < 0.1%

---

## 8. ESCALADO

| Hito Guardianes | Acción |
|---|---|
| 0 - 50k | Stack base. Vercel + Neon free + R2 + Replicate. |
| 50k - 250k | Activar lecturas réplica Postgres. Cache CDN agresivo. |
| 250k - 1M | Mover API a Fly.io multi-región. Migrar search a Meilisearch. |
| 1M - 10M | Particionar tabla `eventos` por mes. Avatares pre-cacheados en CDN. |
| 10M+ | Considerar Aurora / planet-scale. Equipo de plataforma dedicado. |

---

## 9. ENTORNOS

```
local      → docker-compose con PG + Redis. Replicate stub mock.
preview    → Vercel preview por PR. Neon branch. Replicate dev token.
staging    → ecuaman-staging.ec. Datos sintéticos. Auth real.
producción → ecuaman.ec. Backups + alertas activas.
```

---

## 10. ENTREGABLES TÉCNICOS DE FASE 4

- [ ] Repo monorepo creado y CI/CD verde
- [ ] Schema Postgres aplicado en preview
- [ ] Endpoints públicos funcionales con tests >80% cov
- [ ] Endpoints privados con auth Clerk integrada
- [ ] Worker de pasaporte generando PDF válido
- [ ] Worker de avatar conectado a Replicate
- [ ] Microsite con pantallas: home, registro, login, dashboard, perfil
- [ ] Plan de respaldo + disaster recovery documentado
- [ ] Pruebas de carga: 1000 usuarios concurrentes sin degradación
- [ ] Reporte de seguridad (audit + escaneo) entregado a Director

---

*Documento técnico canónico. Cualquier cambio requiere PR + revisión Tech Lead.*
