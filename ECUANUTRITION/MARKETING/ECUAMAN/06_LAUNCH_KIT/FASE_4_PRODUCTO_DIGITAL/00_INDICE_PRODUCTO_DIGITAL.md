# PRODUCTO DIGITAL — Índice maestro
### La plataforma viva donde "La Marea de los Guardianes" se vuelve real

> **Tesis operativa:** Sin plataforma digital, La Marea es solo un manifiesto.
> Con ella, cada producto Ecuanutrition se convierte en la puerta de entrada
> a una hermandad mundial. Esta fase entrega las **especificaciones técnicas
> ejecutables** para construirla — no una idea, un brief de implementación.

---

## 🎯 OBJETIVO DE FASE 4

Convertir la campaña maestra `05_ESTRATEGIA/05_CAMPANA_MAESTRA_LA_MAREA.md`
en un **producto digital construible**, con specs suficientes para que un
equipo técnico (interno o agencia) pueda cotizar, planificar e iniciar
desarrollo sin más reuniones estratégicas.

> **Criterio de cierre de fase:** un CTO externo lee esta carpeta y dice
> *"Tengo todo lo que necesito para cotizar y arrancar mañana."*

---

## 🧱 LOS 5 COMPONENTES DEL PRODUCTO DIGITAL

| # | Componente | Documento | Responsable de build |
|---|---|---|---|
| 1 | Backend + arquitectura | `01_ESPECIFICACIONES_PLATAFORMA.md` | Lead Backend |
| 2 | Microsite público | `02_MICROSITE_COPY_UX.md` | Frontend + Copy |
| 3 | Sistema QR + Pasaporte | `03_SISTEMA_QR_PASAPORTE.md` | Backend + Producción empaque |
| 4 | Generador avatares IA | `04_GENERADOR_AVATARES_LORA.md` | ML Engineer |
| 5 | App móvil | `05_APP_MOVIL_ESPECIFICACION.md` | Mobile Lead |

---

## 🗺️ FLUJO DEL GUARDIÁN — END-TO-END

```
┌──────────────────────────────────────────────────────────────────┐
│  1. COMPRA en supermercado físico/online                          │
│     ↓                                                              │
│  2. ESCANEA QR único en el empaque                                │
│     ↓                                                              │
│  3. ATERRIZA en microsite ecuaman.ecuanutrition.com               │
│     ↓                                                              │
│  4. REGISTRO en 3 pasos (nombre, email, ciudad)                   │
│     ↓                                                              │
│  5. ASIGNACIÓN automática:                                        │
│     • Número de Guardián (ej: #00471)                             │
│     • Título único algorítmico (ej: "El Defensor del Coral")      │
│     • Avatar Ecuaman personalizado (LoRA, 30 segundos)            │
│     ↓                                                              │
│  6. REVELACIÓN del viaje del camarón comprado (animación 45 s)   │
│     ↓                                                              │
│  7. INVITACIÓN a:                                                 │
│     • Próxima Asamblea (fecha visible)                            │
│     • Próxima Marea anual (15 feb)                                │
│     • Descarga del Pasaporte físico (opcional, $0 envío Ecuador)  │
│     ↓                                                              │
│  8. APP MÓVIL — descarga opcional para gamificación continua      │
└──────────────────────────────────────────────────────────────────┘
```

**Tiempo objetivo end-to-end (paso 2 → paso 7):** ≤ **90 segundos**.

---

## 🏛️ ARQUITECTURA EN 4 CAPAS

```
┌────────────────────────────────────────────────────────────┐
│  CAPA 1 — INTERFACES                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  Microsite   │  │  App móvil   │  │  Asamblea live  │  │
│  │   (Next.js)  │  │ (React Native)│  │  (StreamYard +  │  │
│  │              │  │              │  │   webhook votos) │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
├────────────────────────────────────────────────────────────┤
│  CAPA 2 — API + LÓGICA                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  REST + WebSocket (Node.js / Bun)                   │   │
│  │  • Auth (Supabase Auth + magic link)                │   │
│  │  • Asignación de número/título                      │   │
│  │  • Trazabilidad lote ↔ Guardián                     │   │
│  │  • Servicio de avatares (cola async)                │   │
│  │  • Voto Asamblea (con bloqueo anti-fraude)          │   │
│  └─────────────────────────────────────────────────────┘   │
├────────────────────────────────────────────────────────────┤
│  CAPA 3 — DATOS                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  PostgreSQL  │  │     S3 /     │  │   Redis (cola   │  │
│  │  (Supabase)  │  │  Cloudflare  │  │  + cache QR)    │  │
│  │              │  │     R2       │  │                 │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
├────────────────────────────────────────────────────────────┤
│  CAPA 4 — INTEGRACIONES                                     │
│  ┌──────────┐ ┌─────────┐ ┌───────────┐ ┌──────────────┐ │
│  │ Scantrust│ │ Mapbox  │ │ Stable    │ │  Resend /    │ │
│  │  (QR)    │ │ (rutas) │ │ Diffusion │ │  Postmark    │ │
│  │          │ │         │ │ (avatares)│ │  (email)     │ │
│  └──────────┘ └─────────┘ └───────────┘ └──────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

## 🚦 RUTA CRÍTICA DE BUILD (12 SEMANAS)

| Semana | Hito | Responsable |
|---|---|---|
| 1 | Infra base (Supabase + Vercel + dominios) | DevOps |
| 2 | Esquema DB + auth | Backend |
| 3 | Endpoint asignación Guardián + título algorítmico | Backend |
| 4 | Pipeline LoRA Ecuaman entrenado y deployable | ML |
| 5 | Microsite landing + onboarding 3 pasos | Frontend |
| 6 | Integración Scantrust (QR únicos) + ingesta lotes | Backend + Producción |
| 7 | Visualización viaje del camarón (Mapbox + Lottie) | Frontend |
| 8 | Sistema voto Asamblea + dashboard moderador | Full-stack |
| 9 | App móvil — MVP (login, perfil, viaje) | Mobile |
| 10 | App móvil — push, notificaciones Marea | Mobile |
| 11 | QA + tests carga (10k registros simultáneos) | QA |
| 12 | UAT con 50 Guardianes piloto + ajustes | Producto |

> **Lanzamiento público objetivo:** semana 14 (sprint de buffer + soft launch).

---

## 💰 PRESUPUESTO DE BUILD AÑO 1

| Línea | USD |
|---|---|
| Equipo dedicado (12 semanas, 4 FTE blended) | $96,000 |
| Infra cloud año 1 (Supabase Pro + Vercel + Cloudflare R2) | $4,800 |
| Scantrust QR únicos (1M códigos) | $5,000 |
| Mapbox enterprise tier | $3,600 |
| Compute GPU para avatares (RunPod / Replicate) | $12,000 |
| Servicios email/SMS (Resend + Twilio) | $2,400 |
| Auditoría seguridad pre-launch | $4,500 |
| Buffer 15% | $19,200 |
| **TOTAL build año 1** | **$147,500** |

> Encaja dentro del presupuesto plataforma de la campaña maestra
> (`05_CAMPANA_MAESTRA_LA_MAREA.md` §"stack técnico" — $25k plataforma +
> $10k avatares + buffer del rollout).

---

## 🛡️ REGLAS NO NEGOCIABLES DE FASE 4

1. **Cero dark patterns.** El alta es opt-in real, sin casillas pre-marcadas.
2. **Privacidad por diseño.** GDPR + LOPDP Ecuador desde el día 0.
3. **Accesibilidad WCAG 2.1 AA.** No es opcional.
4. **Sin crypto, sin tokens financieros.** El Pasaporte es identidad, no activo.
5. **Costo cero para el Guardián.** Gratis siempre. Punto.
6. **Datos de menores:** registro mínimo 14 años (con consentimiento parental hasta 18).
7. **Toda decisión técnica se documenta** en ADRs (Architecture Decision Records).
8. **Testing pre-lanzamiento:** mínimo 50 Guardianes piloto firman conformidad escrita.

---

## ✅ DEFINICIÓN DE "FASE 4 COMPLETA"

- [ ] Los 5 documentos de esta carpeta entregados y validados
- [ ] Stack técnico cotizado por al menos 2 proveedores
- [ ] Mockups (Figma) del microsite aprobados
- [ ] LoRA Ecuaman entrenado con dataset propio (≥200 imágenes canónicas)
- [ ] Plan de producción de QR coordinado con planta de empaque
- [ ] Roadmap mensual aprobado por Director de Marca + CTO
- [ ] Aprobación legal (FASE 3) sobre Términos y Política de Privacidad

> Solo cuando esto esté completo, pasamos a Fase 5 (Primer Mes de Contenido).

---

## 📚 CONTENIDO DE ESTA CARPETA

| Archivo | Contenido |
|---|---|
| `00_INDICE_PRODUCTO_DIGITAL.md` | Este índice |
| `01_ESPECIFICACIONES_PLATAFORMA.md` | Backend, DB, APIs, infra, seguridad |
| `02_MICROSITE_COPY_UX.md` | Sitemap, copy listo, wireframes, prompts UI |
| `03_SISTEMA_QR_PASAPORTE.md` | Generación, impresión, vinculación, pasaporte físico |
| `04_GENERADOR_AVATARES_LORA.md` | Pipeline ML, dataset, entrenamiento, inferencia |
| `05_APP_MOVIL_ESPECIFICACION.md` | Spec funcional + técnica iOS/Android |

---

*"Una idea bonita sin plataforma es un poema. Una plataforma sin idea bonita
es un formulario. Aquí están las dos, listas para encontrarse."*

— FASE 4 · Producto Digital · Mayo 2026
