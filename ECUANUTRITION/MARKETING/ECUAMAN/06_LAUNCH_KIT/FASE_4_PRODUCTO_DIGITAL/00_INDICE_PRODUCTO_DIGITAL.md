# PRODUCTO DIGITAL — LA MAREA DE LOS GUARDIANES
### Índice maestro de la plataforma viva de Ecuaman

> Esta es la fase donde Ecuaman deja de ser **mascot publicitario** y se
> convierte en **ecosistema participativo**. La Marea de los Guardianes es
> el motor que transforma seguidores en miembros, contenido en vínculo, y
> campaña en comunidad permanente.

---

## 🎯 QUÉ ES "LA MAREA DE LOS GUARDIANES"

Es la plataforma digital propia de Ecuaman donde:

1. **Cada persona del mundo se registra** con su nombre/email y recibe su
   **Pasaporte de Guardián** (PDF + tarjeta digital + número único).
2. **Cada Pasaporte tiene QR único** que enlaza a perfil público
   (`ecuaman.ec/g/<id>`).
3. **Cada Guardián recibe un avatar Ecuaman único** (variación generada por
   modelo LoRA propio) — su "yo Ecuaman" personal.
4. **La comunidad participa en Asambleas mensuales** (live de Ecuaman donde
   se decide ruta de impacto, manglar a sembrar, causa del mes).
5. **Misiones recurrentes** otorgan medallas (sembrar manglar, comer
   camarón ecuatoriano, compartir contenido, reciclar, etc).
6. **Marketplace de causas** donde los Guardianes pueden donar a proyectos
   reales de manglar/Galápagos/economía local.

**Diferencial:** No es un programa de fidelidad. Es una **identidad cívica
ecuatoriana proyectada al mundo**.

---

## 📋 DOCUMENTOS DE ESTA FASE

| # | Documento | Qué contiene |
|---|---|---|
| 01 | `01_ESPECIFICACION_TECNICA_PLATAFORMA.md` | Stack, arquitectura, base de datos, endpoints, infraestructura |
| 02 | `02_MICROSITE_COPY_UX.md` | Copy final + wireframes + flujo de registro de ecuaman.ec |
| 03 | `03_SISTEMA_QR_PASAPORTE.md` | Diseño del Pasaporte físico/digital + algoritmo de IDs únicos |
| 04 | `04_GENERADOR_AVATARES.md` | Sistema LoRA Ecuaman para crear avatar único de cada Guardián |
| 05 | `05_APP_MOVIL_ESPECIFICACION.md` | Spec funcional + screens + roadmap iOS/Android |

---

## 🗺️ ARQUITECTURA GENERAL DEL ECOSISTEMA

```
┌──────────────────────────────────────────────────────────────────┐
│                  LA MAREA DE LOS GUARDIANES                       │
│                                                                   │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────┐  │
│  │  MICROSITE │   │  APP MÓVIL │   │  WHATSAPP  │   │  QR    │  │
│  │ ecuaman.ec │   │  iOS / And │   │  bot       │   │ físico │  │
│  └─────┬──────┘   └─────┬──────┘   └─────┬──────┘   └────┬───┘  │
│        │                │                │               │      │
│        └────────────────┴────────────────┴───────────────┘      │
│                            │                                     │
│                            ▼                                     │
│              ┌──────────────────────────────┐                   │
│              │    API GATEWAY (Node/Bun)    │                   │
│              └──────────────┬───────────────┘                   │
│                             │                                    │
│            ┌────────────────┼────────────────┐                  │
│            ▼                ▼                ▼                  │
│      ┌──────────┐   ┌──────────────┐  ┌──────────────┐         │
│      │ Postgres │   │  S3 / R2     │  │  Replicate   │         │
│      │ (Neon)   │   │ (avatares)   │  │  (LoRA Ecuaman)│        │
│      └──────────┘   └──────────────┘  └──────────────┘         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 🔧 STACK TECNOLÓGICO RECOMENDADO

| Capa | Elección | Por qué |
|---|---|---|
| Frontend microsite | **Next.js 15 + Tailwind v4** | SSR, SEO, performance |
| App móvil | **React Native (Expo)** | un solo código iOS+Android |
| Backend | **Bun + Hono** | fast, edge-friendly, TypeScript |
| DB | **Postgres (Neon)** + **Redis (Upstash)** | escalable, free tier amplio |
| Storage | **Cloudflare R2** | sin egress, 90% más barato que S3 |
| AI Avatares | **Replicate + LoRA propio** | $0.01-0.05 por avatar |
| Auth | **Clerk** o **Supabase Auth** | OAuth + email + magic link |
| Email | **Resend** | DX excelente, $0 hasta 3k/mes |
| Pagos (donaciones) | **Stripe** + **PayPal** + **PayPhone** (Ecuador) | cobertura mundial+local |
| Analytics | **PostHog self-hosted** | producto + funnels + replays |
| Hosting | **Vercel** (front) + **Fly.io** (workers) | autoscale, baratos |
| CDN | **Cloudflare** | gratis, globales, anti-DDoS |

---

## 💰 PRESUPUESTO ESTIMADO PRIMER AÑO

| Concepto | Costo mensual | Anual | Notas |
|---|---|---|---|
| Vercel Pro | $20 | $240 | front-end |
| Fly.io workers | $30 | $360 | jobs avatares |
| Neon Postgres | $19 | $228 | DB principal |
| Upstash Redis | $10 | $120 | cache + jobs |
| Cloudflare R2 | $5 | $60 | storage avatares |
| Replicate AI | $50-200 | $600-2,400 | depende volumen |
| Resend email | $20 | $240 | comunicación |
| Clerk auth | $25 | $300 | auth |
| Dominios | — | $150 | ecuaman.com/.ec/etc |
| PostHog cloud | $0-50 | $0-600 | free tier hasta 1M events |
| **TOTAL** | **$179-379** | **$2,298-4,698** | hasta 100k Guardianes |

> A 250k Guardianes activos, costo proyectado: $700-1,200/mes.
> A 1M Guardianes activos, costo proyectado: $2,500-4,000/mes.

---

## 🚦 SECUENCIA DE EJECUCIÓN

```
SEMANA 1-2  → Especificación técnica + diseño UX (entregables: docs 01, 02)
SEMANA 3-4  → Diseño Pasaporte + sistema QR (entregable: doc 03)
SEMANA 5-6  → Entrenamiento LoRA Ecuaman + pruebas (entregable: doc 04)
SEMANA 7-10 → Desarrollo microsite (registro, perfil, login)
SEMANA 11-12 → QA + load testing + lanzamiento beta cerrada
SEMANA 13   → LANZAMIENTO PÚBLICO (Día 0 de Fase 5)
SEMANA 14-24 → Desarrollo App móvil (post-lanzamiento)
```

---

## ✅ CRITERIOS DE ÉXITO DE FASE 4

Para cerrar Fase 4 con calidad mundial:

- [ ] Microsite ecuaman.ec en producción con Lighthouse >90 mobile
- [ ] Sistema de Pasaporte: registro → PDF → QR → avatar en <60 segundos
- [ ] LoRA Ecuaman entrenado con 200+ imágenes canónicas, ratio aprobación >85%
- [ ] Capacidad probada de 10,000 registros/hora en stress test
- [ ] Cumplimiento legal: GDPR + LOPDP Ecuador + COPPA (menores)
- [ ] Backup automático diario, RTO <4h, RPO <1h
- [ ] Monitoreo 24/7 con alertas (PostHog + Sentry + UptimeRobot)
- [ ] Documentación API pública + privada
- [ ] Beta cerrada con 200 Guardianes piloto validada

---

## 🛡️ REGLAS NO NEGOCIABLES DE LA PLATAFORMA

1. **Privacidad por diseño.** Ningún dato de menores se publica jamás.
2. **Soberanía del Guardián.** Cada usuario puede borrar su cuenta y datos
   en cualquier momento (botón visible, no flujo oculto).
3. **Sin dark patterns.** Cancelar suscripción es un click.
4. **Cero ads de terceros.** La plataforma se sostiene con productos
   propios y donaciones a causas reales.
5. **Open source los componentes neutros.** El generador de Pasaporte
   PDF, QR, mecánica de medallas — código publicado en GitHub.
6. **Accesibilidad WCAG AA mínimo.** Lectores de pantalla, navegación
   por teclado, contraste, alt text en todo lo visual.
7. **Multi-idioma desde día 1.** Español (Ecuador), Inglés, y al menos
   2 idiomas extra en Año 1 (Portugués, Francés).

---

## 📞 EQUIPO MÍNIMO REQUERIDO PARA EJECUTAR FASE 4

| Rol | Tiempo | Responsabilidad |
|---|---|---|
| Product Lead | 100% por 12 semanas | dueño del producto, prioridades |
| Full-stack Engineer | 100% por 12 semanas | microsite + backend |
| ML Engineer | 50% por 4 semanas | entrenamiento LoRA + pipeline avatares |
| UX/UI Designer | 100% por 4 semanas, 50% después | diseño microsite + app + Pasaporte |
| DevOps | 25% durante todo | infra, CI/CD, monitoreo |
| Mobile Engineer | 100% desde semana 14 | app iOS/Android |
| QA | 50% desde semana 6 | pruebas + automatización |

> Si el equipo interno es más pequeño, contratar **boutique de desarrollo
> en Quito o Guayaquil** con experiencia en producto consumer (no agencias
> de IT corporativo). Presupuesto estimado outsourcing: $40-70k para MVP.

---

*Documento maestro de Fase 4. Cada sub-documento detalla un componente.*
*La Marea no es una campaña. Es una infraestructura cívica viva.*
