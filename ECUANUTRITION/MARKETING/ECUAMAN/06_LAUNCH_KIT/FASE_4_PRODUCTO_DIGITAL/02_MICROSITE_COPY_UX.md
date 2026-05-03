# MICROSITE — Copy + UX
### ecuaman.ecuanutrition.com — Sitemap, copy listo para producción y wireframes

> **Principio rector:** el microsite NO vende camarón. **Convierte una compra
> en un acto de pertenencia.** Cada palabra y cada interacción tiene una sola
> misión: que en 90 segundos el comprador deje de ser cliente y se convierta
> en Guardián.

---

## 0. RESUMEN EJECUTIVO

| Atributo | Valor |
|---|---|
| Dominio | `ecuaman.ecuanutrition.com` |
| Idiomas v1 | Español (ES), Inglés (EN) |
| Stack | Next.js 15 + Tailwind 4 + Framer Motion |
| Tipografía | Heading: **Migra Italic** · Body: **Inter** · Acento: **Ranchers** |
| Paleta | Primaria #00C2D7 (cyan tridente) · Secundaria #FF6B35 (langostino) · Fondo #0B1E3F (azul Pacífico nocturno) |
| Performance | Lighthouse ≥ 95 en todas las categorías |

---

## 1. SITEMAP

```
/
├── /             (Home — explica La Marea, dos CTA: "Tengo QR" / "Conocer más")
├── /redeem       (Flujo principal: pega/escanea QR → onboarding 3 pasos → ceremonia)
├── /me           (Perfil del Guardián logueado)
│   ├── /me/viaje      (Animación viaje del camarón comprado)
│   ├── /me/avatar     (Tu avatar Ecuaman + descarga)
│   ├── /me/sellos     (Productos consumidos, niveles, próximo logro)
│   └── /me/pasaporte  (Solicitar pasaporte físico)
├── /asamblea     (Próxima asamblea + archivo de votaciones pasadas)
├── /marea        (Info de La Marea anual + inscripción)
├── /historia     (Lore oficial de Ecuaman, los 7 actos resumidos)
├── /preguntas    (FAQ extendido con buscador)
├── /legal/
│   ├── /legal/terminos
│   ├── /legal/privacidad
│   └── /legal/cookies
└── /admin        (Restringido — equipo Ecuanutrition)
```

---

## 2. COPY POR PANTALLA

### 2.1 `/` — HOME (no logueado)

**Hero (above the fold)**

> **El Pacífico te está buscando.**
>
> Cada producto Ecuanutrition esconde un código. Escánealo y descubre tu
> nombre, tu número y tu lugar dentro de **La Marea de los Guardianes** —
> la primera hermandad mundial de defensores del Pacífico.
>
> [ TENGO MI QR ] [ Conocer más ↓ ]

**Sección 2 — Lo que pasa cuando entras**

> En 90 segundos:
> 1. Recibes un nombre que el mar te entrega.
> 2. Conoces el viaje real de tu camarón, desde la granja en Manabí.
> 3. Tu avatar Ecuaman queda inmortalizado en la mitología.

**Sección 3 — Diferenciador (3 cards)**

| Card | Texto |
|---|---|
| 🔱 **No es un programa de puntos** | Es identidad. No vienes a ahorrar. Vienes a pertenecer. |
| 🌊 **No es un club cualquiera** | Cada decisión de marca pasa por la Asamblea de los Guardianes. Tu voto cuenta. |
| 🏝️ **No es virtual** | Cada año, los Guardianes nos reunimos en una playa de Ecuador. Tú eres invitado. |

**Sección 4 — Prueba social (cuando exista)**

> "Ya somos **{guardianesActivos}** Guardianes en **{paises}** países."
>
> *Una ola que crece sin pedir permiso.*

**Sección 5 — Footer CTA**

> El primer paso es escanear el QR.
> [ EMPEZAR ]

---

### 2.2 `/redeem` — FLUJO DE ALTA

#### Paso 0 — Llegada (con QR ya en URL)

> *Animación: tridente cyan bajando del centro de la pantalla, al fondo se
> vislumbra una silueta de Ecuaman.*
>
> **El mar te ha visto.**
> Estás a un paso de convertirte en Guardián.
>
> [ COMENZAR LA CEREMONIA → ]

#### Paso 1 — Email (pantalla 1 de 3)

> **¿Cómo te llamamos?**
>
> Tu email solo lo usaremos para tu Pasaporte y para avisarte de la Asamblea.
> Nunca para vender nada. Nunca a terceros.
>
> [ Email ]
> [ Nombre con el que firmas ]
>
> [ ] *Quiero recibir las cartas mensuales de Ecuaman* (opcional)
>
> [ SIGUIENTE ]
>
> *Microcopy bajo el botón:* Al continuar aceptas nuestros [términos](/legal/terminos)
> y [política de privacidad](/legal/privacidad).

#### Paso 2 — Origen (pantalla 2 de 3)

> **¿Desde qué orilla nos lees?**
>
> [ Ciudad ]
> [ País ▼ ]
> [ Idioma ▼ ]
>
> [ SIGUIENTE ]

#### Paso 3 — Promesa (pantalla 3 de 3)

> **La promesa de Guardián**
>
> Antes de recibir tu nombre, una sola pregunta:
>
> *"¿Te comprometes a hablar bien del Pacífico cuando puedas, a defender
> lo que se hace bien, y a participar de la Marea cuando te toque?"*
>
> [ JURO POR EL TRIDENTE ]
> [ Aún no estoy listo ]

#### Paso 4 — Ceremonia (revelación)

*Animación de ~12 s:*
1. Olas del Pacífico se abren.
2. Aparece tu **número** ("Guardián #00471") con efecto sello.
3. Aparece tu **título** ("El Defensor del Coral").
4. Aparece tu **avatar** Ecuaman personalizado emergiendo del agua.
5. Música cierra. Frase final:

> **Eres parte de La Marea. Y La Marea no se detiene.**
>
> [ DESCUBRIR EL VIAJE DE MI CAMARÓN → ]

#### Paso 5 — Viaje del camarón

*Mapa Mapbox con animación Lottie:*
- Pin de origen: Granja "{granja}" en {coordenadas Manabí}
- Línea animada hasta puerto de salida
- Línea hasta destino final
- Tu avatar Ecuaman nada la ruta en tiempo real
- Contador: "Has nadado {N} km del Pacífico"

> [ GUARDAR MI AVATAR ] [ ENTRAR A MI PERFIL → ]

---

### 2.3 `/me` — PERFIL DEL GUARDIÁN

**Header**

> Hola, **{display_name}**.
> Eres **{título}** · Guardián #{number} · {país} · Nivel {1|2}
>
> [Avatar grande] · [Compartir mi pasaporte]

**Tarjetas (grid 2x2)**

1. **Tu viaje** — última ruta consumida + total de km nadados.
2. **Tus sellos** — N productos sellados este mes / total / nivel siguiente.
3. **Próxima Asamblea** — fecha, tema, botón "Recordarme".
4. **La Marea {año+1}** — días para el evento, ciudad anfitriona, botón "Inscribirme".

**Banda inferior**

> *"Yo no soy un dibujo. Soy lo que pasa cuando una familia, un mar y un país
> deciden hacer las cosas bien durante generaciones. Yo soy Ecuaman, y
> mientras tú confíes, yo seguiré nadando."*

---

### 2.4 `/asamblea`

**Estado: programada**

> **Próxima Asamblea: {fecha} · {hora local}**
>
> Tema: *"¿Qué causa apoyamos en {mes}?"*
>
> Tres opciones serán votadas en vivo. Tu voto cuenta igual que el de
> cualquier Guardián, sin importar tu nivel.
>
> [ AGREGAR A MI CALENDARIO ] [ AVISARME 1H ANTES ]

**Estado: en vivo**

> *Stream embed (YouTube + IG simultáneo)*
>
> **Estás votando como Guardián #{number}.**
>
> [Pregunta activa: "{pregunta}"]
> ( ) {opción A — descripción}
> ( ) {opción B — descripción}
> ( ) {opción C — descripción}
>
> [ EMITIR VOTO ]
>
> *Cierra en {countdown}*

**Estado: cerrada (archivo)**

> **Asamblea de {mes} {año}**
>
> Tema: "{tema}"
> Decisión votada por {N} Guardianes: **"{opción ganadora}"** ({%}).
>
> Lo que **hicimos** con esa decisión: {actualización con fotos}.

---

### 2.5 `/marea`

> # LA MAREA DE LOS GUARDIANES
> ### {Día} de febrero · {Ciudad de Ecuador}
>
> Una vez al año, los Guardianes que pueden viajar se reúnen en una playa
> rotativa de Ecuador. Los que no pueden viajar, se conectan en vivo desde
> cualquier orilla del mundo.
>
> **{N} Guardianes ya están inscritos**
>
> [ INSCRIBIRME PRESENCIAL ] [ INSCRIBIRME EN STREAMING ]
>
> ## Programa del día
> - 06:00 · Ritual del amanecer (los Fundadores se reúnen primero)
> - 09:00 · Plantación colectiva de manglares
> - 12:00 · Gastronomía: el plato del Pacífico
> - 15:00 · Concierto / actos culturales
> - 17:00 · Ola humana — formación del tridente vista por dron
> - 20:00 · Asamblea Anual en vivo
>
> ## ¿Cómo llego?
> [ Mapa con vuelos sugeridos a {ciudad} ]
> [ Hospedaje recomendado por la organización ]

---

### 2.6 `/historia`

> # ECUAMAN — Los 7 actos
>
> *Pulsa cada acto para escuchar el fragmento narrado.*
>
> 1. **El Huevo Bajo el Manglar** — *(audio 1:20)*
> 2. **La Travesía del Joven Langostino** — *(audio 1:40)*
> 3. **El Encuentro con la Marea Turbia** — *(audio 2:00)*
> 4. **La Forja del Tridente Pacífico** — *(audio 1:30)*
> 5. **El Juramento del Pacífico** — *(audio 1:00)*
> 6. **El Llamado a los Guardianes** — *(audio 2:10)*
> 7. **La Marea Eterna** — *(audio en construcción — los Guardianes la escriben)*
>
> [ LEER LA HISTORIA COMPLETA → /05_ESTRATEGIA/04_HISTORIA_DE_VIDA_ECUAMAN ]

---

### 2.7 `/preguntas` (FAQ)

> # Preguntas que te haces antes de entrar
>
> *(Buscador en la parte superior)*
>
> ### Sobre ser Guardián
> - ¿Cuesta algo? → **No.** Y no costará nunca.
> - ¿Puedo perder mi número? → **No.** Es vitalicio.
> - ¿Puedo darme de baja y volver? → Sí, pero pierdes tu número original.
>
> ### Sobre el QR
> - ¿Y si pierdo el empaque? → No hay forma de recuperar ese código. Pero
>   en tu próximo producto tienes uno nuevo.
> - ¿Y si el QR no funciona? → [Reportar aquí](mailto:guardianes@ecuanutrition.com)
>
> ### Sobre la Asamblea
> - ¿Tengo que conectarme en vivo? → No, puedes votar dentro de una ventana
>   de 24 horas en algunas asambleas.
> - ¿Mi voto vale lo mismo que un Fundador? → **Sí. Siempre.**
>
> ### Sobre privacidad
> - ¿Qué hacen con mi email? → Solo enviamos lo de Asambleas y Marea, salvo
>   que actives marketing opcional.
> - ¿Puedo borrar mi cuenta? → Sí, en `/me/configuracion → Eliminar cuenta`.

---

### 2.8 Páginas legales (`/legal/*`)

Contenido validado por **FASE 3 LEGAL**. Plantillas base:

- **/legal/terminos** — Versión 1.0, alineada con LOPDP Ecuador y GDPR UE.
- **/legal/privacidad** — Política completa, datos recogidos, bases legales,
  derechos ARCO, contactos del DPO.
- **/legal/cookies** — Lista de cookies estrictamente necesarias + opcionales.

---

## 3. WIREFRAMES (descripción para Figma)

> *Diseñador: usar este briefing como base para los frames. No fijar
> tipografías exactas hasta validación con Director de Marca.*

### Frame 01 — Home Hero
- Background: gradiente vertical `#0B1E3F → #0E2C57`
- Centro: tridente animado en SVG (Lottie), 320×320 px en mobile
- Tipografía hero: **Migra Italic 64/72** desktop, 40/48 mobile
- CTA primaria: pill `#00C2D7`, texto `#0B1E3F`
- CTA secundaria: link subrayado en `#FFFFFF` sobre fondo

### Frame 02 — Ceremonia (revelación)
- Pantalla full bleed
- Stage 1 (3s): número del Guardián aparece con sello dorado
- Stage 2 (3s): título aparece con onda
- Stage 3 (4s): avatar aparece subiendo desde el "agua" (gradient mask)
- Stage 4 (2s): pull-quote con frase oficial
- Música: 12s, custom (fade-in, beat dramático en stage 3)

### Frame 03 — Viaje del camarón (mapa)
- Mapa Mapbox custom-styled (paleta marca)
- Pin origen: ícono manglar
- Pin destino: ícono carrito
- Línea animada de origen→destino (Lottie + Mapbox-GL animations)
- HUD inferior: km nadados, días en tránsito, embarcación

### Frame 04 — Perfil
- Header sticky: avatar + número + título
- Cards 2x2 desktop, stack en mobile
- Bottom nav (mobile): Inicio · Asamblea · Marea · Perfil

### Frame 05 — Asamblea en vivo
- Top: stream embed (16:9 responsive)
- Middle: pregunta activa con countdown
- Bottom: botones de voto, animación de "ola" al votar

---

## 4. ACCESIBILIDAD (WCAG 2.1 AA — obligatorio)

- Contraste mínimo 4.5:1 en texto, 3:1 en componentes UI
- Toda interacción por teclado (focus visible)
- Animaciones desactivables vía `prefers-reduced-motion`
- Alt text en todas las imágenes (incluido el avatar generado:
  *"Tu avatar Ecuaman: figura de langostino con capa, tridente cyan,
  variación única según tu número"*)
- Estructura semántica HTML5 (header/main/nav/footer correctos)
- Skip-link "Saltar al contenido"

---

## 5. SEO + OPEN GRAPH

| Página | Title | Description |
|---|---|---|
| `/` | Ecuaman · La Marea de los Guardianes | Hermandad mundial de defensores del Pacífico. Cada producto Ecuanutrition es una puerta. |
| `/redeem` | Ceremonia del Guardián | Convierte tu QR en tu lugar dentro de La Marea. |
| `/historia` | La historia de Ecuaman | Los 7 actos de la mitología del Pacífico. |
| `/marea` | La Marea anual | El día en que los Guardianes vuelven al mar. |

**Open Graph default:**
- Image: render del tridente sobre fondo Pacífico (1200×630)
- Site name: Ecuaman
- Type: website

**Sitemap.xml** generado automáticamente, prioridad 1.0 para `/`, 0.8 para
`/redeem` y `/historia`.

---

## 6. PERFORMANCE

| Métrica | Objetivo |
|---|---|
| LCP | < 2.0 s |
| INP | < 200 ms |
| CLS | < 0.1 |
| TTFB | < 600 ms |
| Bundle JS inicial | < 150 KB gzipped |

Estrategias:
- Imágenes en AVIF + WebP fallback (Next.js `<Image>`)
- Fonts subset + `font-display: swap`
- Animaciones críticas inline; secundarias en chunks lazy
- ISR (Incremental Static Regeneration) para `/historia`, `/preguntas`, `/marea`

---

## 7. ANALÍTICA (privacy-friendly)

- **Plausible** (sin cookies) para métricas agregadas.
- Eventos custom (sin PII):
  - `qr_redeemed`
  - `onboarding_step_{n}_completed`
  - `avatar_generated`
  - `viaje_visualizado`
  - `asamblea_voto_emitido`
  - `marea_inscripcion`
- Embudo principal: `home_visited → redeem_started → step_1 → step_2 → step_3 → ceremonia → viaje → perfil`.

---

## 8. DESIGN TOKENS (TailwindCSS extension)

```js
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        pacifico: {
          900: '#0B1E3F',
          700: '#0E2C57',
          500: '#1B4F8A',
        },
        tridente: {
          DEFAULT: '#00C2D7',
          dark:    '#008DA0',
        },
        langostino: {
          DEFAULT: '#FF6B35',
          light:   '#FF9166',
        },
        marea: {
          arena: '#F5E6CB',
          espuma: '#FFFFFF',
        },
      },
      fontFamily: {
        display: ['"Migra Italic"', 'serif'],
        body:    ['Inter', 'sans-serif'],
        accent:  ['Ranchers', 'cursive'],
      },
    },
  },
};
```

---

## 9. COMPONENTES REUTILIZABLES (Storybook)

- `<Tridente />` — animación Lottie ajustable
- `<GuardianBadge number title />`
- `<AvatarFrame avatarUrl founder />`
- `<JourneyMap origen destino />`
- `<AssemblyVoteCard pregunta opciones />`
- `<MareaCountdown fecha />`
- `<CeremonyStage step />` — gestiona los 4 stages animados

Cada componente con tests Playwright + variantes documentadas.

---

## 10. CHECKLIST DE ENTREGA DE MICROSITE

- [ ] Todas las pantallas implementadas y aprobadas en Figma
- [ ] Copy validado por Director de Marca + revisión legal
- [ ] Lighthouse ≥ 95 en mobile y desktop
- [ ] Auditoría a11y con axe-core sin issues serios
- [ ] Tests E2E del flujo `/redeem` pasando en CI
- [ ] OG cards generados y validados con [opengraph.xyz](https://opengraph.xyz)
- [ ] DNS + SSL configurados (`ecuaman.ecuanutrition.com`)
- [ ] Plausible instalado y verificando eventos clave

---

*"La página de aterrizaje no es un display de producto. Es un altar.
Cada visitante decide en 8 segundos si quedarse para siempre o cerrar
la pestaña. Por eso aquí no perdemos ni una palabra."*

— Microsite UX · Mayo 2026
