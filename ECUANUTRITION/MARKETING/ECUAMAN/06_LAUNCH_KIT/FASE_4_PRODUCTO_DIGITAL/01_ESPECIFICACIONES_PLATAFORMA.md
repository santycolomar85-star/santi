# ESPECIFICACIONES DE PLATAFORMA — La Marea de los Guardianes
### Backend, base de datos, APIs, infraestructura, seguridad y observabilidad

> Documento técnico de **referencia única** (single source of truth) para
> el equipo de ingeniería. Detalla decisiones, alternativas, y el "por qué"
> de cada elección. Reemplaza a varias reuniones técnicas iniciales.

---

## 0. RESUMEN EJECUTIVO TÉCNICO

| Decisión | Elección | Por qué |
|---|---|---|
| Cloud principal | Supabase (Postgres) + Vercel (Edge) + Cloudflare R2 | Time-to-market, costo, soporte LATAM |
| Lenguaje backend | TypeScript (Node 22, Bun aceptable) | Mismo equipo full-stack; ecosistema maduro |
| Auth | Supabase Auth (magic link + OAuth Google/Apple) | Sin password = menos fricción, menos riesgo |
| Pagos | **Ninguno**. La Marea es gratuita. | Cero monetización directa por diseño |
| Pipeline IA | Replicate (inferencia) + RunPod (training) + LoRA propio | Costo controlado, sin lock-in |
| Realtime (Asamblea) | Supabase Realtime + Pusher fallback | Asambleas con miles de votantes simultáneos |
| Observabilidad | Sentry + Logtail + Grafana Cloud | Stack completo en tier free/low-cost |

---

## 1. ARQUITECTURA LÓGICA

### 1.1 Diagrama de componentes

```
┌─────────────────────────────────────────────────────────────────┐
│  CLIENTES                                                         │
│  • Microsite (Next.js 15, React 19)                              │
│  • App móvil (React Native + Expo SDK 52)                        │
│  • Panel admin (Next.js — solo equipo Ecuanutrition)             │
└────────────────────────┬────────────────────────────────────────┘
                         │ HTTPS + WSS
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  EDGE / CDN                                                       │
│  • Vercel Edge Functions (rutas globales, latencia <100 ms LATAM)│
│  • Cloudflare R2 (assets estáticos, avatares servidos)            │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  API LAYER (Node 22)                                              │
│  • REST: /api/v1/* para CRUD                                      │
│  • WebSocket: /ws/asamblea para votos en vivo                     │
│  • Webhooks: Scantrust, Mapbox, Replicate                         │
└──┬───────────────┬─────────────────┬────────────────┬────────────┘
   │               │                 │                │
   ▼               ▼                 ▼                ▼
┌───────┐    ┌──────────┐     ┌──────────┐    ┌──────────────┐
│Postgres│   │  Redis   │     │ S3 / R2  │    │  Servicios   │
│Supabase│   │  Upstash │     │ Avatares │    │  externos    │
│        │   │  cola+   │     │  Mapas   │    │  (Replicate, │
│        │   │  cache   │     │          │    │   Scantrust) │
└───────┘    └──────────┘     └──────────┘    └──────────────┘
```

### 1.2 Servicios internos (módulos del backend)

| Módulo | Responsabilidad | Endpoints clave |
|---|---|---|
| `auth` | Magic link, OAuth, sesiones, MFA opcional | `POST /auth/magic-link`, `POST /auth/oauth/:provider/callback` |
| `guardian` | Alta, asignación de número y título, perfil | `POST /guardian/register`, `GET /guardian/me`, `PATCH /guardian/me` |
| `qr` | Validación de QR, vinculación lote↔guardián | `POST /qr/redeem` |
| `lote` | Trazabilidad granja → puerto → tienda | `GET /lote/:id`, `GET /lote/:id/journey` |
| `avatar` | Encolar generación, polling, almacenamiento | `POST /avatar/generate`, `GET /avatar/:jobId` |
| `asamblea` | Programación, votos, resultados | `GET /asamblea/proxima`, `POST /asamblea/:id/voto` |
| `marea` | Inscripción evento anual, sellos | `POST /marea/inscripcion`, `GET /marea/sellos` |
| `notifications` | Email + push (FCM/APNs) | `POST /notifications/test` (admin) |
| `admin` | Moderación, métricas, exportación | namespace `/admin/*` con RBAC |

---

## 2. ESQUEMA DE BASE DE DATOS (PostgreSQL 16)

### 2.1 Tablas principales

```sql
-- Guardianes
CREATE TABLE guardians (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  guardian_number bigint UNIQUE NOT NULL,            -- ej: 471
  display_name    text NOT NULL,
  email           citext UNIQUE NOT NULL,
  city            text,
  country_iso2    char(2),
  title           text NOT NULL,                     -- ej: "El Defensor del Coral"
  title_seed      bigint NOT NULL,                   -- semilla para reproducir título
  avatar_url      text,                              -- en R2
  avatar_seed     bigint NOT NULL,                   -- semilla para reproducir avatar
  founder         boolean NOT NULL DEFAULT false,    -- true para los primeros 1000
  level           int    NOT NULL DEFAULT 1,         -- 1 base, 2 dorado (50+ productos)
  language        text   NOT NULL DEFAULT 'es',
  marketing_opt_in boolean NOT NULL DEFAULT false,
  created_at      timestamptz NOT NULL DEFAULT now(),
  deleted_at      timestamptz                        -- soft delete (GDPR right to erasure)
);

CREATE INDEX idx_guardians_number ON guardians(guardian_number);
CREATE INDEX idx_guardians_country ON guardians(country_iso2);

-- Lotes de camarón
CREATE TABLE lotes (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  lote_code     text UNIQUE NOT NULL,               -- código interno producción
  granja        text NOT NULL,                      -- ej: "Granja San Mateo, Manabí"
  granja_geo    geography(Point, 4326),
  cosecha_at    date NOT NULL,
  puerto_salida text,
  puerto_geo    geography(Point, 4326),
  barco         text,
  ruta_geojson  jsonb,                              -- ruta completa para Mapbox
  destino       text,                               -- ej: "Carrefour Madrid Centro"
  destino_geo   geography(Point, 4326),
  llegada_at    date,
  created_at    timestamptz NOT NULL DEFAULT now()
);

-- QR únicos
CREATE TABLE qr_codes (
  code          text PRIMARY KEY,                    -- 12 chars alfanuméricos
  lote_id       uuid REFERENCES lotes(id),
  redeemed_by   uuid REFERENCES guardians(id),
  redeemed_at   timestamptz,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX idx_qr_lote ON qr_codes(lote_id);

-- Productos consumidos por Guardián (para nivel y sellos)
CREATE TABLE guardian_products (
  guardian_id   uuid REFERENCES guardians(id),
  qr_code       text REFERENCES qr_codes(code),
  redeemed_at   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (guardian_id, qr_code)
);

-- Asambleas
CREATE TABLE asambleas (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  fecha         timestamptz NOT NULL,
  titulo        text NOT NULL,
  estado        text NOT NULL CHECK (estado IN ('programada','en_vivo','cerrada')),
  stream_url    text,
  created_at    timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE asamblea_votaciones (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  asamblea_id   uuid REFERENCES asambleas(id),
  pregunta      text NOT NULL,
  opciones      jsonb NOT NULL,                      -- [{id,label,desc}]
  abre_at       timestamptz NOT NULL,
  cierra_at     timestamptz NOT NULL
);

CREATE TABLE asamblea_votos (
  votacion_id   uuid REFERENCES asamblea_votaciones(id),
  guardian_id   uuid REFERENCES guardians(id),
  opcion_id     text NOT NULL,
  voted_at      timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (votacion_id, guardian_id)
);

-- La Marea (evento anual)
CREATE TABLE marea_eventos (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  anio          int  UNIQUE NOT NULL,
  fecha         date NOT NULL DEFAULT '2027-02-15',
  ciudad        text NOT NULL,
  capacidad     int  NOT NULL
);

CREATE TABLE marea_inscripciones (
  guardian_id   uuid REFERENCES guardians(id),
  evento_id     uuid REFERENCES marea_eventos(id),
  modo          text CHECK (modo IN ('presencial','streaming')),
  inscrito_at   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (guardian_id, evento_id)
);

-- Auditoría inmutable (append-only)
CREATE TABLE audit_log (
  id            bigserial PRIMARY KEY,
  actor_id      uuid,
  actor_type    text,                                -- 'guardian','admin','system'
  action        text NOT NULL,
  target_type   text,
  target_id     text,
  payload       jsonb,
  created_at    timestamptz NOT NULL DEFAULT now()
);
```

### 2.2 Asignación de número de Guardián

- **Estrategia:** secuencia `bigint` global, asignación atómica en `INSERT`.
- Para los **primeros 1.000 (Fundadores):** flag `founder = true`. Nunca se
  reasignan números aunque el Guardián elimine su cuenta (GDPR: el número
  pasa a estado "retirado", visible como "Guardián #00471 (retirado)").
- **Anti-race-condition:** uso de `nextval('guardians_number_seq')` en una
  función `SQL` invocada desde transacción `SERIALIZABLE`.

### 2.3 Asignación de título único

- **Pool de títulos:** ~500 combinaciones (sustantivo + adjetivo + entorno),
  ej: "El Defensor del Coral", "La Vigía del Manglar", "El Heraldo del Amanecer".
- **Algoritmo determinista:** `title = pool[hash(guardian_number || title_seed) % len(pool)]`
- `title_seed` es global y se rota cada 100k Guardianes para evitar agotamiento.
- Pool de títulos versionado en `/data/titles/v1.json`, mantenido por
  Director de Marca.

---

## 3. SEGURIDAD

### 3.1 Autenticación
- **Sin password.** Magic link (email) + OAuth (Google, Apple).
- Sesiones JWT cortas (15 min) + refresh token (30 días) en cookie `httpOnly`,
  `Secure`, `SameSite=Lax`.
- Rate limit: 5 magic links / email / hora; 100 req/min por IP en endpoints
  públicos.

### 3.2 Autorización (RBAC)
| Rol | Capacidades |
|---|---|
| `guardian` | Leer su perfil, votar, inscribirse a Marea, descargar avatar |
| `moderador` | Moderar mensajes en Asamblea, marcar Guardián destacado |
| `admin` | Crear Asambleas, exportar datos, deshabilitar cuentas |
| `system` | Webhooks internos firmados |

### 3.3 Datos sensibles
- Email: cifrado en reposo (Supabase encryption-at-rest activado).
- Geolocalización del Guardián: nunca se almacena coordenada cruda, solo
  ciudad + país.
- Eliminación: endpoint `DELETE /guardian/me` ejecuta soft delete + purga
  asíncrona en 30 días (GDPR).

### 3.4 Anti-fraude en QR
- Cada QR es **single-use**. Una vez canjeado, queda bloqueado.
- Si un mismo email intenta canjear >50 QRs/día → flag manual review.
- Si un mismo IP/device-fingerprint abre >100 cuentas/24h → bloqueo
  automático + notificación a `security@ecuanutrition.com`.

### 3.5 Auditoría legal-ready
- Tabla `audit_log` registra: alta/baja Guardián, voto, redención QR,
  inscripción Marea, cambios admin.
- Append-only via `REVOKE UPDATE, DELETE` para rol app.
- Backup diario a Cloudflare R2 (retención 7 años — alineado con FASE 3 legal).

---

## 4. DISPONIBILIDAD Y RENDIMIENTO

### 4.1 SLOs objetivo

| Métrica | Objetivo |
|---|---|
| Disponibilidad mensual API pública | 99.5% |
| Disponibilidad durante Asamblea | 99.95% |
| P95 latencia `/qr/redeem` | < 400 ms |
| P95 latencia `/asamblea/voto` | < 250 ms |
| Tiempo generación avatar (cola) | < 30 s P95, < 90 s P99 |

### 4.2 Capacidad
- Diseño para **1M Guardianes año 1** (objetivo año 3 según roadmap).
- Pico esperado en Asamblea mensual: **30k votantes en ventana de 60 s**.
- Estrategia: pre-warm de funciones edge 30 min antes; escalado horizontal
  automático en API.

### 4.3 Backups y DR
- DB: backups continuos (point-in-time recovery 7 días) + snapshot diario
  (retención 30 días).
- Avatares R2: versionado activo.
- RPO objetivo: 5 min. RTO objetivo: 1 hora.

---

## 5. INFRAESTRUCTURA Y COSTO

### 5.1 Stack y costo mensual estimado (año 1)

| Servicio | Plan | USD / mes |
|---|---|---|
| Supabase Pro | Pro + add-ons | $50 |
| Vercel | Pro + analytics | $40 |
| Cloudflare R2 + CDN | 1 TB egress/mes | $30 |
| Upstash Redis | Pay-as-you-go | $25 |
| Replicate (avatares) | ~10k inferencias/mes | $400 |
| Resend (email) | 100k emails/mes | $80 |
| Sentry | Team | $26 |
| Logtail | Pro | $20 |
| Mapbox | Pay-as-you-go | $200 |
| Scantrust | Plataforma | $300 |
| **TOTAL** | | **$1,171** |

> Año 2 escala a ~$3.5k/mes con 250k Guardianes activos.

### 5.2 Entornos

| Entorno | Propósito | URL |
|---|---|---|
| `local` | Desarrollo | `http://localhost:3000` |
| `dev` | Branch deploys | `*.dev.ecuaman.ecuanutrition.com` |
| `staging` | UAT pre-release | `staging.ecuaman.ecuanutrition.com` |
| `prod` | Público | `ecuaman.ecuanutrition.com` |

### 5.3 CI/CD
- GitHub Actions: lint + typecheck + tests + Playwright en cada PR.
- Deploy automático: `dev` por push, `staging` por etiqueta `rc-*`,
  `prod` con aprobación manual.

---

## 6. PRIVACIDAD Y CUMPLIMIENTO

### 6.1 Bases legales (GDPR + LOPDP Ecuador)
| Tratamiento | Base legal |
|---|---|
| Crear cuenta Guardián | Consentimiento explícito + ejecución contractual |
| Trazabilidad lote | Interés legítimo (transparencia) |
| Email transaccional | Ejecución contractual |
| Email marketing | Consentimiento opt-in separado |
| Avatar generado | Consentimiento explícito (clic activo) |

### 6.2 Política de cookies
- Solo cookies estrictamente necesarias por defecto.
- Banner "ajustar / aceptar todas" sin pre-marcado.
- Sin trackers de terceros en el funnel de alta.

### 6.3 Derechos ARCO (acceso, rectificación, cancelación, oposición)
- Endpoint `GET /guardian/me/export` devuelve JSON portable.
- Endpoint `DELETE /guardian/me` con confirmación 2-factor.
- Plazo respuesta: 30 días.

### 6.4 Menores
- Edad mínima: 14 años (alineado con LOPDP Ecuador).
- 14-17 años: requiere checkbox de tutor legal + email de tutor verificado.

---

## 7. OBSERVABILIDAD

### 7.1 Logs estructurados (JSON)
Cada request genera log con: `request_id`, `actor_id`, `route`, `latency_ms`,
`status`, `country` (de IP, anonimizada).

### 7.2 Métricas de negocio
Dashboards Grafana con paneles:
- Guardianes registrados (total, hoy, esta semana, por país)
- QRs canjeados (total, % de QRs producidos)
- Avatares generados (cola, éxito, fallos, tiempo medio)
- Asistencia Asambleas (registrados, conectados pico, votantes únicos)
- Inscripciones Marea (presencial / streaming)

### 7.3 Alertas (PagerDuty / on-call rotativo)
| Alerta | Umbral | Severidad |
|---|---|---|
| API 5xx > 1% en 5 min | sostenido | P1 |
| Cola avatares > 1000 trabajos | 10 min | P2 |
| DB CPU > 80% | 15 min | P2 |
| Webhook Scantrust falla > 5 veces | 5 min | P1 |
| Asamblea en vivo y stream caído | inmediato | P1 |

---

## 8. PLAN DE TESTING

### 8.1 Niveles
- **Unit:** Vitest (cobertura mínima 70%, módulo `auth` y `qr` 90%).
- **Integration:** tests con DB real en CI (Supabase local).
- **E2E:** Playwright (flujo onboarding completo + voto Asamblea).
- **Carga:** k6, escenario "Asamblea pico" (30k usuarios concurrent).
- **Seguridad:** OWASP ZAP semanal en staging + pentest pre-launch.

### 8.2 Datos de prueba
- Generador `seed_guardians.ts` con 50k registros sintéticos.
- Lotes de prueba con rutas reales Manta → Madrid, Manta → Miami, Manta → Shanghái.

---

## 9. INTEGRACIONES EXTERNAS

| Proveedor | Uso | Tipo de auth | Webhook |
|---|---|---|---|
| Scantrust | Generación + validación QR | API key | `POST /webhooks/scantrust` |
| Replicate | Inferencia LoRA Ecuaman | Bearer token | `POST /webhooks/replicate/avatar` |
| Mapbox | Mapas + rutas animadas | Public token (frontend) | n/a |
| Resend | Email transaccional | API key | `POST /webhooks/resend/bounces` |
| FCM / APNs | Push móvil | Service account | n/a |
| StreamYard | Asamblea live | OAuth | `POST /webhooks/streamyard/events` |

> Todas las claves rotables; almacenadas en Vercel/Supabase environment
> secrets. Nunca en repo.

---

## 10. LO QUE **NO** HACEMOS EN V1

Para evitar feature-creep y entregar a tiempo:
- ❌ No marketplace de productos
- ❌ No e-commerce directo
- ❌ No NFT, no blockchain, no token
- ❌ No login con Twitter/X (riesgo reputacional cambiante)
- ❌ No chat 1-a-1 entre Guardianes (modera demasiado costoso v1)
- ❌ No internacionalización completa: v1 ES + EN. ZH/FR llegan en año 3.
- ❌ No app web "instalable" (PWA): la app móvil es la app móvil.

---

## 11. DECISIONES ARQUITECTÓNICAS REGISTRADAS (ADRs)

Carpeta `/docs/adr/` con un archivo por decisión. Plantilla:

```
# ADR-NNN: <título>
- Estado: aceptada | reemplazada por ADR-XXX
- Fecha: YYYY-MM-DD
- Contexto: ...
- Decisión: ...
- Consecuencias: ...
- Alternativas consideradas: ...
```

ADRs iniciales planificados:
- ADR-001: Supabase como BaaS principal
- ADR-002: Sin password, magic link + OAuth
- ADR-003: LoRA propio vs API genérica de imágenes
- ADR-004: PostgreSQL `bigint` para `guardian_number`, no UUID
- ADR-005: Cloudflare R2 vs S3 (egress costs)

---

## ✅ CHECKLIST DE ENTREGA

- [ ] Esquema DB migrado en staging
- [ ] APIs documentadas en OpenAPI 3.1 (`openapi.yaml`)
- [ ] Postman collection publicada
- [ ] Política de Privacidad y Términos validados por legal (FASE 3)
- [ ] Pentest sin findings P1/P2 abiertos
- [ ] Runbook on-call escrito
- [ ] Dashboards Grafana provisionados como código

---

*"La arquitectura no es lo que aguanta el lanzamiento. Es lo que aguanta
el éxito cuando llegue."*

— Especificaciones Plataforma · Mayo 2026
