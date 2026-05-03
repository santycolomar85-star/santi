# APP MÓVIL — Especificación funcional + técnica
### iOS + Android · "Tu Pasaporte siempre en el bolsillo"

> **Tesis del producto:** la web es la puerta de entrada, **la app es el
> hogar del Guardián**. La app guarda el Pasaporte digital, avisa de la
> Asamblea, recuerda cuántos km has nadado y te conecta con los demás
> Guardianes. Sin sustituir el lazo emocional con el producto físico.

---

## 0. RESUMEN EJECUTIVO

| Atributo | Valor |
|---|---|
| Plataformas v1 | iOS 16+, Android 10+ |
| Framework | **React Native 0.76** + **Expo SDK 52** |
| Distribución | App Store + Google Play (sin sideload) |
| Idiomas v1 | ES, EN |
| Conectividad | Online-first con caché local (SQLite) para ver perfil offline |
| Tamaño binario objetivo | < 35 MB instalado |
| Cold start objetivo | < 1.5 s en device tier medio |

---

## 1. POSICIONAMIENTO DE LA APP

| Lo que la app **HACE** | Lo que la app **NO hace** |
|---|---|
| Guardar el Pasaporte digital | Vender productos |
| Mostrar viajes de camarones consumidos | Comparar precios |
| Notificar Asambleas y Mareas | Enviar publicidad de terceros |
| Permitir votar en Asamblea | Chat 1-a-1 entre Guardianes (v1) |
| Escanear QR sin abrir cámara externa | Generar nuevos QR |
| Compartir avatar en redes | Almacenar datos de pago |

---

## 2. PANTALLAS Y FLUJOS

### 2.1 Tab bar inferior (4 tabs)

```
┌──────────────┬────────────┬────────────┬────────────┐
│   🏠 Inicio   │  🗳️ Asamblea │   🌊 Marea  │   👤 Perfil │
└──────────────┴────────────┴────────────┴────────────┘
```

### 2.2 Tab 🏠 Inicio

**Header:**
> Buenas {hora del día}, **{display_name}** 🔱
> Sigues siendo el **{título}**.

**Cards principales (scrollable):**

1. **Card "Tu última travesía"** — animación viaje camarón consumido más
   reciente, km nadados.
2. **Card "Próxima Asamblea"** — countdown + CTA "Recordarme".
3. **Card "Sello pendiente"** — si tiene QR sin escanear pendiente, recordatorio.
4. **Card "Carta de Ecuaman"** — newsletter del mes, formato 30 segundos
   de lectura.
5. **Card "Datos del Pacífico hoy"** — temperatura del mar Manabí, captura del
   día (web scrap legal o API IDB), tono educativo.

**FAB (Floating Action Button):** ícono de QR — abre escáner directo.

### 2.3 Tab 🗳️ Asamblea

- **Si hay asamblea programada:** banner countdown + lista de temas.
- **Si está en vivo:** stream embed, votación activa, chat moderado (read-only
  v1, posts solo de moderadores y respuestas curadas).
- **Histórico:** lista de asambleas pasadas con resultados y "qué pasó después".

### 2.4 Tab 🌊 Marea

- **Próxima Marea anual:** ciudad, fecha, días restantes, programa.
- **Inscripción:** presencial (si tienes cómo llegar) o streaming.
- **Mapa de Guardianes inscritos:** densidad por ciudad (anonimizado, solo
  ciudad).
- **Diario de Mareas anteriores:** galería de fotos oficiales, video
  resumen 3 min.

### 2.5 Tab 👤 Perfil

- Avatar grande + número + título + país.
- Estadísticas: km nadados totales, productos consumidos, sellos físicos,
  asambleas en las que votaste.
- Botones: descargar avatar (PNG), compartir tarjeta de Guardián,
  solicitar Pasaporte físico, configuración.
- **Configuración:** idioma, notificaciones (granular), privacidad,
  exportar mis datos, cerrar sesión, eliminar cuenta.

### 2.6 Onboarding inicial (primera vez)

3 slides + login:
1. "Bienvenido a tu Pasaporte." (animación tridente)
2. "Aquí escaneas, votas y participas." (mockup app)
3. "Y nunca te perderás La Marea anual." (foto evento)
→ Login con email magic link / Apple / Google.

### 2.7 Escáner QR

- Cámara full screen con marco de captura.
- Fallback: "No me deja escanear" → entrada manual de código.
- Vibración háptica al detectar QR válido.
- Animación de "absorción" del QR hacia el centro de la pantalla y
  redirección a `/redeem` flow nativo.

---

## 3. STACK TÉCNICO

| Componente | Tecnología |
|---|---|
| Framework | React Native 0.76 + Expo SDK 52 |
| Navigation | Expo Router (file-based, RN 0.76 compatible) |
| State management | Zustand + React Query |
| Estilos | NativeWind (Tailwind para RN) |
| Animaciones | Reanimated 3 + Lottie + Skia |
| Mapa | `react-native-maps` con tile server Mapbox |
| Cámara QR | `expo-camera` + `expo-barcode-scanner` |
| Push | Expo Notifications (FCM + APNs detrás) |
| Storage local | MMKV (rápido, encriptado) + SQLite (datos extensos) |
| Auth | Supabase JS SDK (mismo backend) |
| Realtime (Asamblea) | Supabase Realtime |
| Analytics | Plausible + PostHog (sin PII) |
| Crash reporting | Sentry |
| OTA updates | EAS Update (parche sin pasar por store) |

---

## 4. NOTIFICACIONES

### 4.1 Tipos y reglas

| Tipo | Cuándo se envía | Default opt-in |
|---|---|---|
| Bienvenida | Tras alta | ✅ on |
| Avatar listo | Cuando termina generación | ✅ on |
| Asamblea próxima (24h antes) | 24h antes de evento | ✅ on |
| Asamblea próxima (1h antes) | 1h antes | ⬜ opcional |
| Asamblea en vivo | Inicio | ✅ on |
| Marea anual (30 días) | Mensaje épico | ✅ on |
| Marea anual (7 días) | Recordatorio | ✅ on |
| Carta mensual de Ecuaman | 1 vez/mes | ⬜ opcional |
| Promo / cobranding | Eventos especiales | ⬜ opcional |

### 4.2 Política
- **Cero spam.** Si el usuario desactiva 3 categorías seguidas, se hace
  pause de todas las notificaciones por 30 días.
- Quiet hours respetadas (22:00 - 08:00 zona horaria del usuario).
- Cada notificación con CTA claro y deeplink a la pantalla relevante.

---

## 5. OFFLINE-FRIENDLY

| Pantalla | Comportamiento offline |
|---|---|
| Inicio | Caché última versión |
| Perfil | 100% offline (datos cacheados) |
| Avatar | Cacheado |
| Mapa de viaje | Tiles cacheados de las rutas vistas |
| Asamblea en vivo | Requiere conexión (mensaje claro) |
| Voto | Requiere conexión, pero almacena en cola si conexión cae mid-vote |
| Escáner QR | Requiere conexión para validar; muestra "Reintentar cuando vuelvas" |

---

## 6. PRIVACIDAD Y SEGURIDAD MOBILE-ESPECÍFICAS

### 6.1 Permisos solicitados
- **Cámara**: solo para escaneo QR. Justificación clara en string.
- **Notificaciones**: opcional, no se solicita en onboarding (se pregunta
  al primer evento que la requiera).
- **Ubicación**: NO se solicita. La ciudad se rellena manualmente.
- **Galería**: solo si el usuario decide guardar avatar manualmente.

### 6.2 Cifrado local
- MMKV cifrado con clave en Keychain (iOS) / Keystore (Android).
- Datos sensibles (token sesión, email) NUNCA en AsyncStorage plano.

### 6.3 Cumplimiento App Store / Play Store
- Privacy Manifest de Apple (iOS 17+) declarado.
- Data Safety form de Google con divulgación completa.
- Política de privacidad enlazada desde la app y desde la ficha de tienda.
- Apple Sign In ofrecido (obligatorio si hay otros OAuth, política Apple).

---

## 7. ANALÍTICA (sin PII)

Eventos clave (igual que microsite, más algunos mobile-only):

- `app_opened`
- `qr_scanned_success` / `qr_scanned_fail`
- `asamblea_voto_app`
- `marea_inscripcion_app`
- `notification_opened` (con categoría)
- `avatar_shared` (a redes externas)
- `pasaporte_solicitado_app`

**Funnel objetivo:** `app_opened → home_loaded → cualquier acción dentro
de 30 s` (engagement primer contacto).

---

## 8. ACCESIBILIDAD MOBILE

- Tamaño de fuente respeta sistema (Dynamic Type iOS / Font scale Android).
- VoiceOver / TalkBack: labels en todos los elementos.
- Contraste: misma paleta marca, validada AA mínimo.
- Botones tap target mínimo 44 × 44 pt.
- Animaciones desactivadas cuando OS reporta `prefers-reduced-motion`.

---

## 9. PERFORMANCE Y CALIDAD

| Métrica | Objetivo |
|---|---|
| Cold start | < 1.5 s |
| Hot reload (después suspended) | < 600 ms |
| Memoria pico | < 180 MB |
| Tamaño descarga inicial | < 35 MB |
| Crash-free sessions | > 99.5% |
| Frame rate (animaciones) | 60 fps en device tier medio |

Tooling:
- Flipper para debug
- Reactotron para state inspection
- React Profiler en QA
- Sentry Performance traces en producción

---

## 10. DEPLOY Y RELEASE

### 10.1 Pipeline (EAS Build + EAS Update)

| Canal | Trigger | Audiencia |
|---|---|---|
| `dev` | push a `develop` | equipo interno |
| `preview` | tag `rc-*` | TestFlight + Internal Track |
| `prod` | tag `v*` (manual approval) | público |

### 10.2 Versionado
- Semver: `vMAJOR.MINOR.PATCH`
- Build numbers automáticos (CI).
- OTA updates para hotfixes (sin pasar por store) — solo cambios JS.

### 10.3 Rollout gradual
- Día 1: 5% usuarios (Apple/Google staged rollout).
- Día 3: 25% si crash-free > 99.5%.
- Día 7: 100%.

---

## 11. QA Y TESTING

### Tests
- Unit (Jest): hooks, util functions, store reducers.
- Component (React Native Testing Library): pantallas críticas.
- E2E (Detox): onboarding, escaneo QR mock, voto Asamblea.
- Device matrix:
  - iPhone 12 (iOS 17), iPhone 15 Pro (iOS 18)
  - Pixel 6 (Android 13), Samsung A54 (Android 14)
  - 1 device tier bajo (Android 10, 3GB RAM) para validar performance

### Programa beta
- TestFlight + Google Play Internal Track con 50 Guardianes piloto.
- Feedback canalizado vía Instabug embed.
- Iteraciones semanales pre-launch.

---

## 12. RIESGOS Y MITIGACIONES

| Riesgo | Mitigación |
|---|---|
| Apple rechaza por "metadata insuficiente" | Privacy Manifest + screenshots claros + revisar guidelines 5.1 (loyalty) |
| Notificaciones percibidas como spam | Reglas estrictas + opt-in granular + quiet hours |
| App grande > 50 MB (límite cellular download) | Code splitting, assets en R2, eliminar unused libs |
| Performance baja en gama media | Skia en vez de canvas pesado, Reanimated worklets |
| Crash rate alto en Android | Sentry + ANR detection + matriz de testing más agresiva |
| Devs internos sin experiencia RN | Pair programming + estándar Expo (no fork nativo) |

---

## 13. ROADMAP MÓVIL

| Versión | Fecha | Cambios |
|---|---|---|
| v1.0 | Mes 4 (lanzamiento público) | Funcionalidad descrita arriba |
| v1.1 | Mes 5 | Compartir tarjeta de Guardián mejorada (Stories ready) |
| v1.2 | Mes 7 | Apple Wallet + Google Wallet (Pasaporte como pase) |
| v1.3 | Mes 9 | Modo oscuro / claro alternable |
| v2.0 | Año 1 cierre | Chat de Asamblea moderado, perfil de otros Guardianes |
| v2.1 | Año 2 | Realidad aumentada — Ecuaman aparece en tu cocina |
| v3.0 | Año 3 | Asistente conversacional con voz oficial Ecuaman |

---

## 14. CHECKLIST DE ENTREGA

- [ ] Apps iOS y Android publicadas en stores
- [ ] Política de privacidad linkeada y revisada (FASE 3)
- [ ] Privacy Manifest (Apple) + Data Safety (Google) completados
- [ ] EAS Build + EAS Update configurados
- [ ] TestFlight + Play Internal Track con 50 Guardianes piloto
- [ ] Sentry + Plausible + PostHog instrumentados
- [ ] Documentación interna de release process en `/docs/mobile/`
- [ ] Plan de soporte: canal `mobile-support@` SLA 48h
- [ ] Crash-free sessions > 99.5% en pre-launch sostenido 14 días

---

*"La app no es la marca. Es el rincón donde el Guardián vuelve cuando
necesita recordar quién es. Por eso cada notificación tiene que merecer
el bolsillo donde vive."*

— App Móvil · Mayo 2026
