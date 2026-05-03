# SISTEMA QR + PASAPORTE DEL GUARDIÁN
### Generación, impresión, vinculación lote↔código y producción del pasaporte físico

> El QR es la **bisagra entre el mundo físico y la mitología digital**. Si
> el QR falla — fallamos. Si el QR brilla — La Marea respira. Este documento
> define cómo se generan, se imprimen, se canjean, se monitorean y cómo se
> produce el Pasaporte físico opcional que llega por correo.

---

## 0. RESUMEN EJECUTIVO

| Atributo | Valor |
|---|---|
| Proveedor QR único serializado | **Scantrust** (alternativa: Snowdrop) |
| Volumen año 1 | 1.000.000 códigos |
| Densidad estimada de canje | 30-45% (industria: 5-15%) |
| Costo unitario QR | $0.005 USD/código |
| Pasaporte físico | Cartilla 9×14 cm, 16 páginas, papel offset 150g |
| Costo unitario Pasaporte | $1.20 USD impreso + $0.80 envío Ecuador |

---

## 1. CICLO DE VIDA DE UN QR

```
┌────────────────────────────────────────────────────────────┐
│  1. GENERACIÓN  → Scantrust crea código alfanum. único     │
│        ↓                                                     │
│  2. ASIGNACIÓN A LOTE en planta de empaque                  │
│     (cada lote tiene N QRs, vinculados en DB ANTES de salir)│
│        ↓                                                     │
│  3. IMPRESIÓN en empaque (etiqueta interior premium)        │
│        ↓                                                     │
│  4. DISTRIBUCIÓN al supermercado                            │
│        ↓                                                     │
│  5. COMPRA por el cliente                                   │
│        ↓                                                     │
│  6. ESCANEO con cámara móvil → URL ecuaman.ec…/r/{code}    │
│        ↓                                                     │
│  7. VALIDACIÓN backend:                                     │
│     • código existe                                          │
│     • código no canjeado                                     │
│     • lote vinculado                                         │
│        ↓                                                     │
│  8. CANJE: registra Guardián, marca QR como redeemed        │
│        ↓                                                     │
│  9. AUDIT: log inmutable + métrica de tasa de canje         │
└────────────────────────────────────────────────────────────┘
```

---

## 2. ESPECIFICACIÓN TÉCNICA DEL QR

### 2.1 Formato del código

- **Longitud:** 12 caracteres alfanuméricos (sin caracteres ambiguos: sin
  `0/O`, `1/I/l`).
- **Alfabeto válido:** `23456789ABCDEFGHJKLMNPQRSTUVWXYZ` (32 chars).
- **Espacio total:** 32¹² ≈ 1.15 × 10¹⁸ (suficiente para milenios).
- **Ejemplo:** `K7M2-PXQA-9NHT`
- **URL impresa:** `ecuaman.ec/r/K7M2PXQA9NHT` (13 chars de ruta).

### 2.2 Imagen del QR

- Versión QR 4 (33×33 módulos), corrección error nivel `H` (30%).
- Tamaño impreso: **mínimo 18×18 mm** sobre el empaque para legibilidad.
- En el centro del QR: **logo Ecuaman monocromo** (5×5 mm) — verificado que
  no rompe legibilidad por la corrección H.
- Color: tinta cyan `#00C2D7` sobre fondo blanco mate.

### 2.3 Anti-falsificación

- Cada QR de Scantrust incluye un **patrón "Copy Detection Pattern" (CDP)**
  invisible al ojo humano. Si alguien fotografía/copia el QR e imprime,
  Scantrust detecta el ataque al escanear.
- Endpoint `/qr/redeem` valida con Scantrust API antes de aceptar el canje.

---

## 3. INTEGRACIÓN CON LA PLANTA DE EMPAQUE

### 3.1 Flujo operativo en planta

1. La planta produce un **lote** (ej: lote `LOT-2026-0517-001`, 5.000
   bandejas de camarón).
2. El backend Ecuanutrition genera **5.000 QRs** vía API Scantrust y los
   pre-vincula al lote en `qr_codes(code, lote_id)`.
3. La planta imprime las etiquetas con QR (impresora Domino Ax-Series
   o equivalente) en línea de producción.
4. Al sellar el empaque, un **escáner de visión** verifica que cada QR sea
   legible. Códigos defectuosos se descartan y se marca el QR como `voided`.
5. El lote sale con un **manifiesto digital** (CSV/JSON) firmado, enviado
   al backend confirmando que esos N códigos están "live in market".

### 3.2 Trazabilidad del lote

Cada lote registra en `lotes`:
- Granja origen + coordenadas
- Fecha cosecha
- Puerto de salida + barco
- Ruta a destino (geojson)
- Destino final (supermercado/distribuidor)
- Fecha llegada estimada (actualizable por logística)

> **Realtime:** la ruta se actualiza con webhook de la naviera (cuando
> esté disponible) o manualmente por el equipo de exportación.

### 3.3 Reglas de canje

| Regla | Comportamiento |
|---|---|
| Código no existe | 404 + "Código inválido. Verifica que escribiste bien." |
| Código existe, no canjeado | Inicia flujo `/redeem` |
| Código ya canjeado por mismo Guardián | Redirige a perfil con mensaje "Este lote ya está en tu pasaporte" |
| Código ya canjeado por OTRO Guardián | "Este código ya fue activado. Si crees que es un error, escribe a guardianes@ecuanutrition.com" |
| Código `voided` | "Este empaque tiene un código defectuoso. Escríbenos para enviarte un código de cortesía." |
| Lote anterior a 365 días | Permite canje pero muestra aviso "Este es un producto con más de 1 año, gracias por reportarlo" |

---

## 4. EL PASAPORTE FÍSICO

### 4.1 Por qué existe

El Pasaporte físico es **el objeto totémico** de La Marea. Materializa la
pertenencia. No es obligatorio (la mayoría de Guardianes lo tendrán solo
digital), pero quien lo solicita demuestra **alto compromiso** y se vuelve
el mejor embajador de marca.

### 4.2 Especificaciones físicas

| Atributo | Valor |
|---|---|
| Formato | 9 × 14 cm (estilo pasaporte real) |
| Páginas | 16 + cubiertas |
| Papel interior | Offset crema 150 g/m² |
| Cubierta | Cartulina rígida con foil dorado para Fundadores, mate para resto |
| Acabado | Cosido + grapado central |
| Caja regalo | Sobre kraft con sello cera (para Fundadores) |

### 4.3 Estructura de páginas

| Página | Contenido |
|---|---|
| Portada | Logo Ecuaman dorado + "PASAPORTE DEL GUARDIÁN" |
| 1 | Datos del titular: nombre, número, título, ciudad, fecha alta |
| 2 | Avatar Ecuaman impreso en alta calidad |
| 3-4 | Manifiesto oficial impreso |
| 5-6 | Mapa de Ecuador con costa marcada |
| 7-12 | **Espacios para sellos** — un sello por producto Ecuanutrition consumido (12 sellos = nivel 2 dorado) |
| 13 | Calendario de Asambleas anuales |
| 14 | Inscripción a "La Marea" anual |
| 15 | "Notas del Guardián" — espacio en blanco |
| Contraportada | QR personal del pasaporte (lleva al perfil del Guardián) |

### 4.4 Sistema de sellos físicos

- En las **3 ciudades anfitrionas año 1** (Manta, Quito, Guayaquil) hay
  **kioscos físicos** Ecuanutrition donde los Guardianes pueden recibir
  sellos de tinta marítima en su pasaporte.
- En la **Marea anual**, todos los inscritos presenciales reciben un sello
  exclusivo del año + ciudad.
- Pasaporte digital se actualiza paralelamente: cada sello físico se asocia
  al QR canjeado correspondiente o al evento Marea.

### 4.5 Logística de envío

- **Solicitud:** desde `/me/pasaporte` el Guardián completa dirección.
- **Verificación:** OTP por email para evitar errores tipográficos.
- **Producción:** lote semanal (mínimo 50 unidades para optimizar imprenta).
- **Envío Ecuador:** Servientrega o Laar, $0 al usuario (subsidiado por marca).
- **Envío internacional año 1:** solo bajo solicitud especial, costo a cargo
  del Guardián. Año 2 se incluye gratis para Fundadores.
- **Tiempo de entrega:** 7-15 días hábiles dentro de Ecuador, 15-30 días
  internacional.

---

## 5. PRESUPUESTO QR + PASAPORTE AÑO 1

| Línea | Cantidad | USD |
|---|---|---|
| QRs Scantrust | 1.000.000 | $5.000 |
| Impresión etiquetas en planta | 1M (incluido en costo empaque) | — |
| Verificación visión en planta (HW + integración) | Setup inicial | $8.000 |
| Pasaportes físicos (proyección 30k canjes año 1, 10% solicitan físico = 3.000) | 3.000 | $3.600 |
| Caja regalo Fundadores (1.000) | 1.000 | $2.500 |
| Logística Ecuador | 3.000 envíos | $2.400 |
| **TOTAL año 1** | | **$21.500** |

---

## 6. SISTEMA DE FALLBACK (si el QR no escanea)

> Realidad: empaques se mojan, se rasgan, las cámaras varían. Necesitamos
> caminos alternativos.

1. **Código manual debajo del QR:** misma cadena de 12 chars en texto
   legible. El microsite acepta `?code=...` por entrada manual.
2. **NFC opcional v2:** evaluar tag NFC adhesivo para empaques premium
   (costo +$0.04/unidad, evaluar año 2).
3. **Canal de soporte:** `guardianes@ecuanutrition.com` y WhatsApp
   `+593-XXX-XXXXXX` para reclamos. SLA: respuesta en 24h, resolución en 72h.
4. **Códigos de cortesía:** los moderadores admin pueden emitir códigos
   "cortesía" canjeables 1 sola vez para casos justificados.

---

## 7. MONITOREO Y MÉTRICAS

### Dashboard "Salud del QR"

| Métrica | Cálculo | Alerta si |
|---|---|---|
| % canje por lote | canjes / QRs producidos | < 10% en lote >30 días → revisar punto de venta |
| Códigos `voided` en planta | voided / producidos | > 2% en un lote → revisar impresora |
| Códigos rechazados (CDP fail) | intentos rechazados Scantrust | > 50 / día → posible falsificación |
| Tasa de canje global | canjes acum / producidos acum | objetivo: 30-45% año 1 |
| Tiempo medio QR→canje | timestamp lote_salida → canje | tracking benchmark |

### Reporte semanal automático
Excel + dashboard con:
- Lotes activos en mercado
- Top 10 ciudades por canje
- Distribución de hora de canje (cuándo escanean)
- Funnel `escaneo → onboarding → ceremonia → guardián activo`

---

## 8. POLÍTICA DE CALIDAD DEL QR (NO NEGOCIABLE)

1. **Tolerancia cero a códigos duplicados.** Test automatizado en cada
   manifiesto entrante.
2. **Tolerancia cero a códigos vinculados a lote inexistente.** Validación
   estricta.
3. **Lote no sale de planta sin manifiesto digital firmado.** Sin
   manifiesto, el código se rechaza al canje.
4. **Auditoría mensual** de muestra física: 50 empaques al azar de tiendas
   reales se compran y se intenta canjear. Tasa de éxito ≥ 99%.
5. **Plan de retiro:** si se detecta lote con > 5% de códigos defectuosos,
   se notifica retiro voluntario a tiendas y se compensa con codes cortesía.

---

## 9. RIESGOS Y MITIGACIONES

| Riesgo | Mitigación |
|---|---|
| Tasa de canje muy baja (< 10%) | Refuerzo punto de venta + QR más visible + cartel "ESCANÉAME" |
| Falsificación masiva de QR | Scantrust CDP + endpoint con rate-limit por IP |
| Saturación pico de canjes (Black Friday) | Pre-warm capacidad + cola gracefull degradation |
| Pasaporte físico no llega | Tracking + reenvío gratuito una vez |
| GDPR — datos del Guardián expuestos por mal manejo de QR | Auth obligatorio antes de mostrar perfil |
| Costo Scantrust sube por volumen | Cláusula de revisión anual + plan B con Snowdrop o solución propia |

---

## 10. CHECKLIST DE ENTREGA

- [ ] Cuenta Scantrust enterprise activa con tenant Ecuanutrition
- [ ] API Scantrust integrada y testeada (sandbox + prod)
- [ ] Endpoint `/qr/redeem` con tests E2E (incluido CDP fail)
- [ ] Manifiesto digital implementado (firma HMAC-SHA256)
- [ ] Línea de impresión Domino calibrada y validada en planta piloto
- [ ] Verificación visión en planta operativa (≥ 99% lectura)
- [ ] Diseño Pasaporte físico aprobado y proveedor de imprenta cerrado
- [ ] Tracking Servientrega/Laar integrado en backend
- [ ] FAQ específico de QR publicado en `/preguntas`
- [ ] Plan de monitoreo activo con alertas configuradas

---

*"Un QR es un puente. Si el puente cruje, nadie cruza. Por eso aquí no
imprimimos QRs: imprimimos puentes."*

— Sistema QR + Pasaporte · Mayo 2026
