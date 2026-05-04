# APP MÓVIL ECUAMAN — ESPECIFICACIÓN FUNCIONAL
### Roadmap iOS / Android · Pantallas · Funcionalidades · Stack

> La app móvil es la **expansión natural del microsite** post-lanzamiento.
> Permite vivir la identidad Guardián desde el bolsillo: ver pasaporte
> en wallet, completar misiones con cámara, votar en asambleas, recibir
> notificaciones de marea. **No se lanza el día 0** — se lanza en la
> semana 14-18 del calendario maestro, una vez consolidada la base de
> Guardianes web.

---

## 1. POR QUÉ APP MÓVIL (y NO sólo PWA)

| Razón | Detalle |
|---|---|
| Push notifications confiables | Asambleas, mareas urgentes, misiones limitadas |
| Cámara nativa para evidencias | Subir foto de manglar plantado, ceviche cocinado |
| Wallet integrado | Pass del Pasaporte siempre accesible offline |
| App Store discovery | Posicionamiento en App Store + Play Store |
| Modo offline | Pasaporte + última asamblea + medallas accesibles sin conexión |
| Geolocalización | Asignar misiones específicas por país/ciudad |
| Biometría | Acceso rápido sin contraseña (Face ID, fingerprint) |

PWA queda como **fallback para web móvil**, sin perder funcionalidad
core, pero con menos riqueza nativa.

---

## 2. STACK MÓVIL

```
React Native + Expo SDK 52+
├── Navigation: Expo Router (file-based)
├── State: Zustand (compartido con web vía paquete monorepo)
├── Data: TanStack Query
├── Forms: React Hook Form + Zod
├── i18n: i18next (mismo locale del web)
├── UI: Tamagui (cross-platform tokens) + estilos propios
├── Animations: Reanimated 3 + Lottie
├── Auth: Clerk Expo SDK
├── Push: Expo Notifications + EAS Push
├── Camera: Expo Camera + Image Manipulator
├── Wallet: react-native-passkit-wallet (iOS) + Google Wallet API (Android)
├── Maps (futuro v2): react-native-maps con tiles MapTiler
└── Build: EAS Build + EAS Submit
```

---

## 3. PANTALLAS Y NAVEGACIÓN

```
ROOT
├── Onboarding (sólo primera vez)
│   ├── 1. Bienvenida
│   ├── 2. Manifiesto resumido
│   ├── 3. Permisos (notificaciones, cámara opcional)
│   └── 4. Login / Registro
│
├── App principal (tabs bottom)
│   ├── 🏠 INICIO
│   │   ├── Saludo personalizado
│   │   ├── Próxima asamblea (banner)
│   │   ├── Misiones recomendadas (3)
│   │   ├── Tus medallas recientes
│   │   └── Mareas en vivo (post Ecuaman recientes)
│   │
│   ├── 🎫 PASAPORTE
│   │   ├── Avatar + número (full screen)
│   │   ├── QR animado
│   │   ├── Botón: añadir a Apple/Google Wallet
│   │   ├── Detalles: rasgos, fecha, origen
│   │   ├── Compartir → genera carta visual
│   │   └── Re-emitir (max 3/año)
│   │
│   ├── 🛡️ MISIONES
│   │   ├── Activas (filtro)
│   │   ├── Disponibles (filtro)
│   │   ├── Completadas (filtro)
│   │   └── Detalle de misión
│   │       ├── Descripción
│   │       ├── Cómo completar (texto + video)
│   │       ├── Subir evidencia (cámara o galería)
│   │       └── Estado de validación
│   │
│   ├── 🌊 MAREA
│   │   ├── Próxima asamblea + countdown
│   │   ├── Histórico de asambleas + decisiones
│   │   ├── Causas activas + barra progreso
│   │   ├── Donar a causa
│   │   └── Mapa global de Guardianes (v2)
│   │
│   └── 👤 YO
│       ├── Avatar + número + estadísticas
│       ├── Mis medallas (galería)
│       ├── Mis donaciones
│       ├── Configuración
│       │   ├── Idioma
│       │   ├── Notificaciones (granular)
│       │   ├── Tema (auto / claro / oscuro)
│       │   ├── Cambio de email/contraseña
│       │   ├── Borrar mi cuenta (con confirmación)
│       │   └── Acerca de + términos + privacidad
│       └── Cerrar sesión
│
└── Modales globales
    ├── Asamblea en vivo (cuando arranca)
    ├── Notificación push tap → handler
    ├── Sin conexión → modo offline read-only
    └── Actualización requerida (force update)
```

---

## 4. FLUJOS CRÍTICOS

### 4.1 Login express con magic link

```
1. User ingresa email
2. Clerk envía magic link
3. User abre link → app captura deeplink → token → home
```

### 4.2 Subir evidencia de misión (manglar plantado)

```
1. User en pantalla de misión "Sembrar tu marea"
2. Tap "Subir evidencia"
3. Eligir: tomar foto / elegir de galería
4. Imagen → resize a 1080px lado largo + WebP 80% calidad
5. Subir a R2 con upload firmado (presigned URL del backend)
6. POST /api/v1/me/misiones/:id/evidencia con URL
7. Estado misión pasa a "validando"
8. Push cuando admin/sistema valida o rechaza
```

### 4.3 Asamblea en vivo

```
1. 30 min antes: notificación push "Asamblea empieza pronto"
2. Tap → pantalla countdown
3. Hora 0: pantalla cambia a "EN VIVO" con video embed (YouTube Live API)
4. Pregunta de votación aparece como modal cuando admin la envía
5. User vota → confirmación + animación tridente
6. Final: resumen de decisión + medalla "Asistí a la Asamblea N"
```

### 4.4 Modo offline

```
- App al arrancar cachea: pasaporte completo, últimas 5 misiones, próxima asamblea
- Sin conexión: muestra todo lo cacheado, indicador de "modo offline"
- Acciones write se encolan en SQLite local, se sincronizan al recuperar conexión
```

---

## 5. NOTIFICACIONES PUSH

### Categorías (granulares — usuario puede desactivar individualmente)

| Categoría | Frecuencia | Ejemplo |
|---|---|---|
| Asambleas | 2 por mes | "Asamblea 3 inicia en 1 hora" |
| Misiones nuevas | 1 por semana | "Una nueva misión te espera" |
| Misión validada | bajo demanda | "Tu plantación de manglar fue validada" |
| Mareas urgentes | rara, sólo crítico | "Acción urgente por derrame en Esmeraldas" |
| Recordatorios | configurable | "Han pasado 7 días sin tu marea" |
| Marketing | opcional, opt-in | "Nuevo contenido del Episodio 03" |

### Reglas de buen comportamiento
- Nunca >2 push por día por usuario
- Quiet hours respetados (22:00-08:00 local del Guardián)
- Cada push tiene CTA específico, nunca "Toca para ver"
- Idioma del usuario, nunca traducción automática mala

---

## 6. ROADMAP DE LA APP

### v0 (Beta cerrada · semana 14-15)
- Onboarding + login
- Pasaporte (visualización + Wallet pass)
- Tab Inicio básico
- 100 testers, feedback intensivo

### v1 (Lanzamiento público · semana 17-18)
- Misiones core (5 misiones iniciales)
- Asambleas (visualización, vote en vivo)
- Causas y donación (Stripe)
- Notificaciones push
- iOS + Android, ES + EN

### v1.1 (semana 22-24)
- Multi-idioma full (PT, FR)
- Modo offline robusto
- Estadísticas globales animadas
- Compartir pasaporte como tarjeta visual generada

### v2 (mes 6-9)
- Mapa mundial de Guardianes (con privacidad opt-in)
- AR: ver Ecuaman en la cocina cuando preparas camarón
- Mini-juegos educativos sobre el Pacífico
- Social: seguir a otros Guardianes, leaderboard regional opt-in

### v3 (año 2)
- Marketplace de mercancía oficial
- Eventos físicos cercanos (con RSVP)
- Programa Embajadores Junior (edad 13-17 con consentimiento)
- Integración Strava/HealthKit (misiones de movimiento azul)

---

## 7. PERFORMANCE Y CALIDAD

| Métrica | Target |
|---|---|
| App size (release) | < 60 MB iOS, < 35 MB Android |
| Cold start | < 2.5s |
| Time to interactive | < 1s después de cold start |
| Crash-free users | > 99.7% |
| Crash-free sessions | > 99.9% |
| Battery drain (bg) | < 1% por hora idle |
| Memory peak | < 250 MB |

Herramientas:
- **Sentry** para crashes y performance
- **PostHog** para producto y funnels
- **Firebase Performance** opcional para network y rendering

---

## 8. ACCESIBILIDAD MÓVIL

- VoiceOver (iOS) y TalkBack (Android) probados pantalla por pantalla
- Tamaños de fuente Dynamic Type / FontScale respetados (hasta 200%)
- Contraste WCAG AA mínimo
- Áreas tappables ≥44pt (iOS) / 48dp (Android)
- Modo de movimiento reducido respetado (prefersReducedMotion)
- Subtítulos forzados disponibles para video de asambleas

---

## 9. CONSIDERACIONES STORE

### App Store (iOS)
- Categoría primaria: **Lifestyle**, secundaria: **Education**
- Edad recomendada: 4+ (no contenido sensible)
- In-app purchases: NO inicialmente (donaciones via Stripe externa
  si la política de Apple lo permite, fallback Apple Pay con comisión 30%)
- Privacy nutrition label: 100% transparente
- Review notes: explicar el contexto de comunidad cívica para evitar rechazo

### Play Store (Android)
- Categoría: Lifestyle
- Sensitive permissions: Cámara (con justificación), Notificaciones
- Data safety form: completo, claro
- Open testing primero, luego producción

---

## 10. PRESUPUESTO ESTIMADO

| Concepto | Inversión |
|---|---|
| Diseño UI/UX (mobile-first) | $4,000 - $7,000 |
| Desarrollo MVP iOS+Android (8 semanas) | $25,000 - $40,000 (in-house o boutique) |
| EAS Build + Submit | $99/mes |
| Apple Developer Program | $99/año |
| Google Play Developer | $25 una vez |
| Sentry + PostHog | $0-100/mes (free tiers iniciales) |
| Mantenimiento (post-launch) | $2,000-4,000/mes |

---

## 11. CHECKLIST DE LANZAMIENTO DE LA APP

- [ ] Diseño UI completo aprobado (Figma)
- [ ] MVP funcional probado por 100 beta testers (TestFlight + Internal Testing)
- [ ] Crashes <0.5% en beta
- [ ] Performance metrics dentro de targets
- [ ] App Store Connect + Play Console configurados
- [ ] Capturas + descripciones en 4 idiomas
- [ ] Screenshots video preview iOS + Android
- [ ] Política de privacidad enlazada y aprobada por legal
- [ ] Feature flags listos para rollout gradual (1% → 10% → 50% → 100%)
- [ ] Plan de respuesta a crisis de reviews 1 estrella (template + workflow)

---

*La app es el músculo del ecosistema. El microsite trae a la gente. La
app la convierte en hábito.*
