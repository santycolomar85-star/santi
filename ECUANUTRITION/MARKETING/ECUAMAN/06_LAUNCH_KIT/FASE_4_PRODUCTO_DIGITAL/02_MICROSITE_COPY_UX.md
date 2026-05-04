# MICROSITE ECUAMAN.EC — COPY FINAL Y FLUJO UX
### Texto listo para publicación + wireframes + flujo de registro de Guardián

> Esta es la **puerta de entrada al ecosistema Ecuaman**. Si esta página
> no convierte y emociona en los primeros 7 segundos, todo el resto de la
> campaña pierde el 60% de su potencia. Cada palabra, cada clic, cada
> animación está pensada para que **el visitante se vuelva Guardián**.

---

## 1. ARQUITECTURA DE INFORMACIÓN

```
ecuaman.ec
├── /                      Home (hero + CTA Únete a la Marea)
├── /quien-soy             Historia, manifiesto, valores
├── /la-marea              Qué es ser Guardián
├── /pasaporte             Detalle del Pasaporte + galería pública
├── /asambleas             Próxima asamblea + archivo histórico
├── /causas                Causas activas + impacto
├── /tienda                (futuro) merchandising oficial
├── /prensa                Press kit + historia de marca
├── /faq                   Preguntas frecuentes
├── /legal                 Términos + privacidad + COPPA
├── /unete                 Flujo de registro
├── /g/:qr                 Perfil público de un Guardián
└── /admin                 Backoffice (privado)
```

URL del subdominio para producto digital: **`ecuaman.ec`** y alias
`ecuaman.ecuanutrition.com`.

---

## 2. HOMEPAGE (`/`)

### Wireframe (vertical, mobile-first)

```
┌─────────────────────────────────────┐
│  [Logo Ecuaman]   ES ▾   [Únete]    │  ← navbar sticky
├─────────────────────────────────────┤
│                                     │
│         🎬 Hero video loop          │  ← Ecuaman emergiendo
│         (autoplay, sin sonido)      │     del océano, 6s loop
│                                     │
│   "El Pacífico tiene un Guardián.   │  ← H1 (poppins 600, 56px desk)
│         ¿Vas a estar de su lado?"   │
│                                     │
│   Subtitle: Únete a La Marea de los │
│   Guardianes. Pasaporte gratis.     │
│   Avatar único. Comunidad mundial.  │
│                                     │
│   [ ÚNETE A LA MAREA → ]            │  ← CTA primario, naranja
│                                     │
│   Más de XXX,XXX Guardianes en      │  ← contador en vivo
│   YYY países                        │
│                                     │
├─────────────────────────────────────┤
│  Sección: ¿Quién es Ecuaman?         │
│  3 columnas con video corto + texto │
├─────────────────────────────────────┤
│  Sección: ¿Qué hace un Guardián?     │
│  Iconos (Sembrar, Defender, Comer    │
│   responsable, Difundir)             │
├─────────────────────────────────────┤
│  Sección: Tu Pasaporte               │
│  Mockup 3D del Pasaporte + CTA       │
├─────────────────────────────────────┤
│  Sección: Asamblea próxima           │
│  Countdown + tema + CTA "Voy"        │
├─────────────────────────────────────┤
│  Sección: Causas activas             │
│  3 tarjetas con barra de progreso    │
├─────────────────────────────────────┤
│  Sección: La Marea en cifras         │
│  Counters animados                   │
├─────────────────────────────────────┤
│  Footer: links, redes, idiomas       │
└─────────────────────────────────────┘
```

### Copy final del Hero

**Variante A (cinematográfica — recomendada para lanzamiento):**

> ## El Pacífico tiene un Guardián.
> ## ¿Vas a estar de su lado?
>
> Cada minuto el océano pierde un pedazo de manglar.
> Cada minuto un río llega más sucio al mar.
> Cada minuto Ecuador exporta el camarón que protege al mundo.
>
> **Ecuaman es ecuatoriano. La Marea es de todos.**
> Únete gratis. Recibe tu Pasaporte. Encuentra tu rol.
>
> [ ÚNETE A LA MAREA → ]
>
> *Más de **47.382 Guardianes** en **63 países**.*

**Variante B (directa — para campañas paid):**

> ## Sé Guardián del Pacífico.
> ## En 60 segundos. Gratis.
>
> Pasaporte oficial. Avatar único de Ecuaman. Comunidad mundial.
>
> [ EMPEZAR →  ]

---

## 3. SECCIÓN "¿QUIÉN ES ECUAMAN?"

```
┌────────────────┬────────────────┬────────────────┐
│  📜 ORIGEN      │  🛡️ MISIÓN      │  🌊 IDENTIDAD   │
├────────────────┼────────────────┼────────────────┤
│ Nacido del     │ Defender el    │ Es Penaeus     │
│ Pacífico       │ Pacífico, los  │ vannamei.      │
│ ecuatoriano    │ manglares y la │ Es ecuatoria-  │
│ donde nace el  │ economía azul  │ no. Es de la   │
│ camarón más    │ ecuatoriana    │ humanidad      │
│ noble del      │ con la fuerza  │ entera que     │
│ mundo, Ecuaman │ silenciosa de  │ come y         │
│ es la voz del  │ los que crecen │ respeta el     │
│ océano vivo.   │ al borde.      │ océano.        │
│                │                │                │
│ [Leer más]     │ [Leer más]     │ [Leer más]     │
└────────────────┴────────────────┴────────────────┘
```

---

## 4. SECCIÓN "¿QUÉ HACE UN GUARDIÁN?"

```
🌱 SEMBRAR        Plantar manglar (real o simbólico)
🛡️ DEFENDER       Reportar, hablar, educar
🍤 COMER BIEN     Camarón ecuatoriano trazable
📣 DIFUNDIR       Llevar a Ecuaman al mundo
⚖️ DECIDIR        Votar en Asambleas mensuales
💚 DONAR          Apoyar causas reales del Pacífico
```

Cada ítem expande con tooltip y enlaza a misión correspondiente.

---

## 5. FLUJO DE REGISTRO (`/unete`)

### UX en 4 pasos · TIEMPO TOTAL OBJETIVO < 60 SEGUNDOS

#### Paso 1 — Identidad (15s)

```
┌─────────────────────────────────────┐
│  Empecemos por lo básico            │
│                                     │
│  Nombre o cómo quieres aparecer     │
│  [_________________________]        │
│                                     │
│  País                               │
│  [Ecuador ▾]   (autodetectado)      │
│                                     │
│  Email                              │
│  [_________________________]        │
│                                     │
│  ¿Tienes 13 años o más?             │
│  ( ) Sí  ( ) No                     │
│                                     │
│           [ Continuar → ]           │
└─────────────────────────────────────┘
```

**Lógica:**
- Si `< 13`: pedir email del tutor + flujo COPPA aparte (ver `03_LEGAL/`).
- País se autodetecta por geolocalización IP, editable.

#### Paso 2 — Personalización del avatar (15s)

```
┌─────────────────────────────────────┐
│  Tu Ecuaman es único.               │
│  Elige los rasgos que más te        │
│  representan.                       │
│                                     │
│  COLOR DE CAPA                      │
│  ( ) Azul real (estándar)           │
│  ( ) Cian profundo                  │
│  ( ) Rojo coral                     │
│  ( ) Verde manglar                  │
│  ( ) Dorado patrimonial             │
│                                     │
│  ACCESORIO                          │
│  ( ) Tridente (estándar)            │
│  ( ) Lanza coral                    │
│  ( ) Guardián sin arma              │
│                                     │
│  EXPRESIÓN                          │
│  ( ) Heroico (estándar)             │
│  ( ) Sereno                         │
│  ( ) Risueño                        │
│                                     │
│  Vista previa: [silueta animada]    │
│                                     │
│  [Atrás]      [ Generar avatar → ]  │
└─────────────────────────────────────┘
```

#### Paso 3 — Generación (15-30s)

```
┌─────────────────────────────────────┐
│       Forjando tu Pasaporte…        │
│                                     │
│   [animación Lottie: Ecuaman        │
│    emergiendo + tridente brilla]    │
│                                     │
│   ✓ Generando tu avatar único       │
│   ✓ Imprimiendo tu Pasaporte        │
│   ⟳ Asignando tu número             │
│                                     │
│   "Cada Guardián tiene un número.   │
│    Tú serás el #47.383."            │
└─────────────────────────────────────┘
```

#### Paso 4 — Bienvenida y entrega

```
┌─────────────────────────────────────┐
│   ¡Bienvenido, Guardián #47.383!    │
│                                     │
│   [ AVATAR GRANDE GENERADO ]        │
│                                     │
│   Te enviamos a [email]:            │
│   ✓ Tu Pasaporte oficial (PDF)      │
│   ✓ Tu kit de bienvenida            │
│   ✓ Cómo ingresar a la Asamblea     │
│                                     │
│   Tu QR de Guardián:                │
│   [ QR único ]                      │
│                                     │
│   [Compartir tu Ecuaman →]          │
│   [Ir a tu panel →]                 │
│                                     │
│   Tu primera misión te espera:      │
│   "Sembrar tu primera marea"        │
└─────────────────────────────────────┘
```

---

## 6. PANEL DEL GUARDIÁN (`/me` o `/dashboard`)

```
┌──────────────────────────────────────────────────────────┐
│  Hola, [Nombre] · Guardián #47.383       [Cerrar sesión] │
├──────────────────────────────────────────────────────────┤
│  ┌────────────┐    Tu impacto                            │
│  │ AVATAR     │    🌱 0 manglares                         │
│  │ del usuario│    🛡️ 0 misiones                          │
│  │            │    🏅 0 medallas                          │
│  └────────────┘    💚 $0 donados                          │
│                                                          │
│  [Descargar Pasaporte PDF]   [Ver tu QR]                 │
├──────────────────────────────────────────────────────────┤
│  Misiones disponibles                                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐      │
│  │ Sembrar      │ │ Compartir    │ │ Comer trazable│     │
│  │ tu marea     │ │ tu Pasaporte │ │ camarón ECU   │     │
│  │ +50 puntos   │ │ +20 puntos   │ │ +30 puntos    │     │
│  │ [Empezar]    │ │ [Empezar]    │ │ [Empezar]     │     │
│  └──────────────┘ └──────────────┘ └──────────────┘      │
├──────────────────────────────────────────────────────────┤
│  Próxima asamblea                                        │
│  [Banner: Asamblea #2 — 24 de mayo · 19:00 ECT]          │
│  [ Recordarme ]                                          │
├──────────────────────────────────────────────────────────┤
│  Causas activas                                          │
│  [3 tarjetas]                                            │
└──────────────────────────────────────────────────────────┘
```

---

## 7. PERFIL PÚBLICO (`/g/:qr_token`)

URL pública compartible. Lo que aparece cuando alguien escanea un QR:

```
┌─────────────────────────────────────┐
│       [Avatar grande del Guardián]  │
│                                     │
│       SANTI COLOMAR                 │
│       Guardián #47.383              │
│       Quito, Ecuador  · desde 2026  │
│                                     │
│       🌱 12 manglares plantados     │
│       🛡️ 8 misiones completadas     │
│       🏅 5 medallas ganadas         │
│                                     │
│       Capa cian · Tridente clásico  │
│                                     │
│       [Únete a La Marea →]          │
└─────────────────────────────────────┘
```

> **Privacidad:** este perfil es público SIEMPRE. El Guardián elige al
> registrarse si su nombre real aparece o un alias. Nunca se muestra su
> email, edad exacta, ciudad sin su confirmación.

---

## 8. COMPONENTES DE INTERFAZ (DESIGN SYSTEM)

### Paleta

| Color | Hex | Uso |
|---|---|---|
| Naranja Ecuaman | #F39A2B | CTA primario, héroe |
| Azul Pacífico | #0046AD | fondo, capa |
| Cian Tridente | #00D9FF | acentos, link hover |
| Amarillo Ecuador | #FFD600 | highlight bandera |
| Rojo Ecuador | #C8102E | crítico, alertas |
| Manglar oscuro | #0A2540 | textos, footer |
| Marfil | #F8F4EC | fondo claro |

### Tipografía

- **Display (titulares):** Poppins 700/600, ajuste -2% letterspacing
- **Cuerpo:** Inter 400/500, line-height 1.6
- **Acento ecuatoriano:** Domine 600 (cuando se cita herencia patrimonial)
- **Numerales contadores:** Space Grotesk 700 tabular-nums

### Componentes esenciales
- Botón primario (naranja → cian hover)
- Botón ghost (transparente con borde cian)
- Card de causa (con barra progreso)
- Card de misión (con icon + puntos)
- Modal de generación (con Lottie)
- Toast (success/error)
- Stepper (4 pasos del registro)

---

## 9. PERFORMANCE Y SEO

### Performance objetivos (Lighthouse mobile)
- LCP < 2.0s
- INP < 200ms
- CLS < 0.05
- Total page weight < 1.2 MB
- Imágenes Next/Image con AVIF + WebP fallback
- Fonts self-hosted con `font-display: swap`

### SEO
- Meta tags Open Graph + Twitter Card por ruta
- Schema.org JSON-LD: `Organization`, `Person` (Guardián), `Event` (Asamblea)
- Sitemap.xml generado en build
- robots.txt amigable a bots éticos, bloquea AI scrapers comerciales
- Canonical URLs

---

## 10. COPY MICRO-INTERACCIONES (mensajes del sistema)

| Situación | Copy |
|---|---|
| Email duplicado | "Ya hay un Guardián con ese correo. ¿Quieres ingresar?" |
| Avatar generándose | "Forjando tu Pasaporte... no cierres esta ventana, faltan segundos." |
| Avatar fallido | "El océano se agitó por un momento. Vuelve a intentar tu generación." |
| Pasaporte listo | "Bienvenido al frente, Guardián." |
| Sin conexión | "Perdiste señal. La Marea espera. Recarga." |
| Logout | "Hasta la próxima marea, Guardián." |
| Confirmación borrar cuenta | "Si te vas, tu nombre vuelve al océano. ¿Estás seguro?" |
| Donación exitosa | "Gracias. Tu marea ya está moviéndose." |
| Misión completada | "Una medalla más en tu pasaporte. El Pacífico te ve." |

---

## 11. CHECKLIST DE LANZAMIENTO DEL MICROSITE

- [ ] Lighthouse mobile ≥90 en performance, accesibilidad, SEO, best-practices
- [ ] Compatible Safari iOS 15+, Chrome Android 100+, Edge desktop
- [ ] Probado en pantallas 320px (iPhone SE) hasta 4K
- [ ] WCAG AA: contraste, navegación teclado, lectores pantalla
- [ ] Multi-idioma ES (default), EN, PT, FR cargando dinámicamente
- [ ] Cookie banner conforme RGPD + LOPDP Ecuador
- [ ] Política de privacidad + términos publicados y enlazados
- [ ] Formulario de contacto con captcha + rate limit
- [ ] Cuenta admin lista, 2FA obligatoria
- [ ] Sentry + PostHog conectados, eventos clave instrumentados
- [ ] Email transaccional probado en Gmail, Outlook, iCloud, Yahoo
- [ ] PDF Pasaporte abre correctamente en iOS, Android, escritorio
- [ ] Compartir en WhatsApp/IG/X genera vista previa correcta
- [ ] Domain redirects: ecuaman.com → ecuaman.ec; ecuaman.com.ec → ecuaman.ec
- [ ] HTTPS A+ en SSL Labs
- [ ] Sitemap, robots, RSS si aplica

---

*Copy bloqueado para producción. Cualquier cambio post-lanzamiento pasa
por A/B test con muestra mínima 5,000 usuarios y resultado significativo
estadísticamente (95%).*
