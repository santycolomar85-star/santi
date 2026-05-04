# SISTEMA QR + PASAPORTE DEL GUARDIÁN
### Diseño físico-digital del Pasaporte oficial · Algoritmo de IDs únicos · Plantilla PDF imprimible

> El **Pasaporte del Guardián** es la pieza más simbólica del ecosistema.
> Es objeto, identidad y prueba de pertenencia. Debe ser **bello, único,
> reproducible y verificable**. Cada Pasaporte es válido para toda la
> vida del Guardián.

---

## 1. CONCEPTO

El Pasaporte es:

- **Un PDF descargable** (1 página A4 vertical, también disponible en formato A6 para imprimir como tarjeta de bolsillo).
- **Una tarjeta digital** (Apple Wallet + Google Wallet pass).
- **Una credencial verificable** vía QR único que lleva al perfil público.
- **Coleccionable y compartible** (formato listo para redes y para imprimir en casa o en imprenta).

> No es un certificado, no es un boleto. Es la **partida de identidad
> cívica** del Guardián.

---

## 2. ANATOMÍA DEL PASAPORTE (lado A — primario)

```
┌────────────────────────────────────────────────────┐
│  [bandera EC + tridente sello]    PASAPORTE        │
│                                   DEL GUARDIÁN     │
│                                                    │
│  GUARDIÁN N.°                                      │
│  ECM-2026-047383                                   │
│                                                    │
│         ┌────────────────────┐                     │
│         │                    │                     │
│         │   AVATAR ÚNICO     │   Nombre:           │
│         │   DEL GUARDIÁN     │   SANTI COLOMAR     │
│         │   (1024x1024)      │                     │
│         │                    │   Origen:           │
│         │                    │   Quito, Ecuador    │
│         │                    │                     │
│         └────────────────────┘   Desde:            │
│                                  04 mayo 2026      │
│                                                    │
│  CAPA: Cian profundo                               │
│  TRIDENTE: Coral guardián                          │
│  EXPRESIÓN: Sereno                                 │
│                                                    │
│                          ┌─────────────┐           │
│  Juro defender el         │             │          │
│  Pacífico, la verdad      │   QR ÚNICO  │          │
│  del manglar y la         │             │          │
│  honestidad del camarón.  │             │          │
│                           └─────────────┘          │
│                                                    │
│  [Firma simbólica de Ecuaman]                      │
│  Emitido por La Marea de los Guardianes            │
│                                                    │
│  ecuaman.ec/g/47383                                │
└────────────────────────────────────────────────────┘
```

### Lado B — secundario (opcional)

Mapa estilizado de Ecuador con el manglar marcado como punto de origen,
tabla de medallas obtenidas (vacía al inicio), y sello de re-emisión.

---

## 3. SISTEMA DE NUMERACIÓN

### Formato del Serial: `ECM-AAAA-NNNNNN`

| Segmento | Significado | Ejemplo |
|---|---|---|
| `ECM` | "ECuaMan" — fijo | ECM |
| `AAAA` | Año del registro | 2026 |
| `NNNNNN` | Número correlativo del año (6 dígitos zero-padded) | 047383 |

**Reglas:**
- El correlativo se reinicia cada 1 de enero a `000001`.
- Los primeros 1.000 Guardianes del año reciben distinción "Marea Temprana".
- Los Guardianes 0-100 reciben Pasaporte físico de cortesía (ver `tienda` futura).

### Algoritmo del QR Token

```typescript
import { createHmac } from 'crypto';

function generarQrToken(guardianId: string, secret: string): string {
  // 32 bytes hex (256 bits) — colisión imposible en la práctica
  return createHmac('sha256', secret)
    .update(guardianId + ':' + Date.now())
    .digest('hex')
    .slice(0, 32); // 32 chars
}
```

- **Token QR:** 32 caracteres hex (32 bytes, prácticamente único).
- **URL pública:** `https://ecuaman.ec/g/<qr_token>`.
- **NO se exponen** ni el `id` UUID interno ni el email del Guardián en el QR.
- **Re-emisión** genera nuevo token y deprecia el anterior (siguiendo
  permitido leer el viejo durante 30 días con redirect al nuevo).

### Generación del PDF — pipeline

```
job: pasaporte.generar
  1. fetch guardian + avatar URLs
  2. cargar template Handlebars del Pasaporte
  3. inyectar: nombre, número, país, fecha, avatar, QR data URL
  4. renderizar con PDFKit (Node) o Puppeteer (HTML→PDF, fallback)
  5. firmar PDF con certificado emisor (PAdES B-B level)
  6. subir a R2 → URL CDN cifrada
  7. UPDATE pasaportes SET pdf_url = ...
  8. enviar email con adjunto + link descarga
```

### Fuente de verdad
- El campo `pasaportes.serial` es **inmutable** una vez emitido.
- El campo `qr_token` puede rotar (re-emisión).
- El campo `version` se incrementa en cada re-emisión (max 3 por año).

---

## 4. TARJETAS DIGITALES (WALLET)

### Apple Wallet (.pkpass)

```json
{
  "formatVersion": 1,
  "passTypeIdentifier": "pass.ec.ecuaman.guardian",
  "serialNumber": "ECM-2026-047383",
  "teamIdentifier": "ECUANUTRITION_TEAM_ID",
  "organizationName": "Ecuanutrition",
  "description": "Pasaporte del Guardián de Ecuaman",
  "logoText": "Ecuaman",
  "foregroundColor": "rgb(255,255,255)",
  "backgroundColor": "rgb(0,70,173)",
  "labelColor": "rgb(255,214,0)",
  "generic": {
    "primaryFields": [
      { "key": "name", "label": "GUARDIÁN", "value": "SANTI COLOMAR" }
    ],
    "secondaryFields": [
      { "key": "number", "label": "N.°", "value": "ECM-2026-047383" },
      { "key": "since", "label": "DESDE", "value": "04 MAY 2026" }
    ],
    "auxiliaryFields": [
      { "key": "country", "label": "ORIGEN", "value": "ECUADOR" }
    ],
    "backFields": [
      { "key": "oath", "label": "JURAMENTO",
        "value": "Juro defender el Pacífico, la verdad del manglar y la honestidad del camarón." },
      { "key": "url", "label": "PERFIL",
        "value": "https://ecuaman.ec/g/<qr_token>" }
    ]
  },
  "barcode": {
    "format": "PKBarcodeFormatQR",
    "message": "https://ecuaman.ec/g/<qr_token>",
    "messageEncoding": "iso-8859-1"
  }
}
```

**Recursos requeridos** (subir al `.pkpass`):
- `icon.png` (29×29) + @2x + @3x
- `logo.png` (160×50) + @2x
- `thumbnail.png` (90×90 con avatar) + @2x

### Google Wallet (Generic Pass)

Usar API JWT-based con clase `genericClass` propia.
Misma estructura semántica, branded igual.

---

## 5. PLANTILLA HTML→PDF (referencia)

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <style>
    @page { size: A4; margin: 0; }
    body {
      margin: 0;
      font-family: 'Inter', sans-serif;
      background: linear-gradient(180deg, #0046AD 0%, #0A2540 100%);
      color: #F8F4EC;
      width: 210mm; height: 297mm;
      position: relative;
      overflow: hidden;
    }
    .marca { position: absolute; top: 24mm; left: 20mm; display: flex; gap: 8mm; align-items: center; }
    .titulo { font-family: 'Poppins'; font-weight: 700; font-size: 24pt; letter-spacing: -1px; }
    .serial { position: absolute; top: 50mm; left: 20mm; font-family: 'Space Grotesk'; font-size: 18pt; color: #00D9FF; }
    .avatar { position: absolute; top: 70mm; left: 20mm; width: 80mm; height: 80mm; border-radius: 4mm; box-shadow: 0 0 20mm rgba(0,217,255,0.3); }
    .datos { position: absolute; top: 70mm; left: 110mm; }
    .datos h2 { font-family: 'Poppins'; font-size: 22pt; margin: 0 0 8mm; }
    .datos .campo { margin-bottom: 6mm; }
    .datos .campo label { color: #FFD600; font-size: 8pt; letter-spacing: 2px; text-transform: uppercase; }
    .datos .campo span { display: block; font-size: 14pt; }
    .juramento { position: absolute; bottom: 40mm; left: 20mm; max-width: 110mm; font-style: italic; line-height: 1.5; }
    .qr { position: absolute; bottom: 30mm; right: 20mm; width: 40mm; height: 40mm; background: white; padding: 3mm; border-radius: 2mm; }
    .firma { position: absolute; bottom: 18mm; left: 20mm; font-family: 'Domine'; font-size: 10pt; color: #FFD600; }
    .footer { position: absolute; bottom: 8mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; font-size: 8pt; color: rgba(248,244,236,0.5); }
  </style>
</head>
<body>
  <div class="marca">
    <img src="{{logo_pasaporte_b64}}" width="40mm" />
    <span class="titulo">PASAPORTE DEL GUARDIÁN</span>
  </div>

  <div class="serial">{{serial}}</div>

  <img class="avatar" src="{{avatar_url}}" />

  <div class="datos">
    <h2>{{nombre_publico}}</h2>
    <div class="campo"><label>Origen</label><span>{{ciudad}}, {{pais}}</span></div>
    <div class="campo"><label>Desde</label><span>{{fecha_registro}}</span></div>
    <div class="campo"><label>Capa</label><span>{{rasgo_capa}}</span></div>
    <div class="campo"><label>Acento</label><span>{{rasgo_accesorio}}</span></div>
  </div>

  <div class="juramento">
    "Juro defender el Pacífico, la verdad del manglar y la honestidad del
    camarón. Mi marea suma con la marea de todos los Guardianes del mundo."
  </div>

  <img class="qr" src="{{qr_data_url}}" />

  <div class="firma">— Ecuaman, Guardián del Pacífico</div>

  <div class="footer">
    <span>ecuaman.ec/g/{{qr_token}}</span>
    <span>v{{version}} · emitido {{ahora}}</span>
  </div>
</body>
</html>
```

---

## 6. FORMATO IMPRIMIBLE FÍSICO (opcional)

### Versión tarjeta (formato CR80, 85.6 × 53.98 mm — tamaño tarjeta de crédito)

- Material: PVC laminado mate, espesor 0.76 mm.
- Frente: avatar + nombre + número + sello dorado en relieve.
- Reverso: QR + bandera EC + URL del perfil.
- Color predominante: azul Pacífico con borde naranja Ecuaman.
- Costo unitario por mayor en Ecuador: $0.80 - $1.20.
- Casos de uso: kit influencers, eventos, asamblea cero, embajadores.

### Versión póster A3 imprimible

Para colecciones, eventos físicos, "Wall of Guardians".

---

## 7. SISTEMA DE QR — DETALLES TÉCNICOS

### Especificación
- **Versión QR:** 7-10 (capacidad media-alta)
- **ECC level:** Q (25% de redundancia, sobrevive logo overlay)
- **Tamaño módulo:** ≥6mm × 6mm en impresión (para escaneabilidad fiable)
- **Centro con logo:** medallón "E" Ecuaman dorado, ≤20% del área
- **Color:** módulos azul Pacífico, fondo blanco (mejor escaneabilidad que invertido)

### Validación al escaneo
1. URL de destino lee `qr_token`.
2. Backend valida token vs DB.
3. Si válido y vigente → render del perfil público + log evento.
4. Si revocado o inexistente → página "Pasaporte no válido" con CTA registrarse.
5. Si vigente pero re-emitido → redirect 301 al nuevo perfil.

### Anti-fraude
- Cada escaneo se loguea en `eventos` con IP + user agent.
- Detección de >100 escaneos/min de un mismo QR → throttle automático.
- Reporte semanal de QRs sospechosos al admin.

---

## 8. DERECHO AL OLVIDO (RGPD/LOPDP)

Cuando un Guardián pide borrar su cuenta:

1. `pasaportes`: el row se conserva 30 días con `revocado = true`,
   luego se borra (cumple obligaciones contables/auditoría).
2. `avatares`: imágenes se borran de R2 inmediatamente.
3. URL pública pasa a 410 Gone con copy: "Este Guardián volvió al océano".
4. El QR físico (si lo imprimieron) deja de funcionar — no hay forma de
   "des-imprimir", advertir esto en términos.
5. Email de confirmación de borrado al usuario.

---

## 9. PRESUPUESTO DEL SUBSISTEMA

| Concepto | Estimación |
|---|---|
| Diseño plantilla PDF (vector + html) | $800 - $1.500 (una vez) |
| Diseño tarjeta CR80 + póster A3 | $500 (una vez) |
| Apple Developer Account (para Wallet) | $99/año |
| Google Wallet (Generic Pass) | $0 |
| Certificado firma PDF (PAdES) | $50-200/año |
| Generación PDF runtime | ~$0.001 por pasaporte (Fly.io) |
| Tarjetas físicas en lote 1.000 unidades | $850 (PVC + impresión) |

---

## 10. CHECKLIST DE LANZAMIENTO DEL SUBSISTEMA

- [ ] Plantilla PDF aprobada por Director de Marca
- [ ] Pruebas de generación con 100 muestras: 100% legibles, todas con QR funcional
- [ ] Apple Wallet `.pkpass` válido en iPhone con iOS 17+
- [ ] Google Wallet pass válido en Android 10+
- [ ] Re-emisión funciona, mantiene historial de versiones
- [ ] Borrado RGPD probado end-to-end
- [ ] QR físico de prueba escaneable a >50cm con cámara estándar
- [ ] Tarjetas CR80 piloto producidas y aprobadas
- [ ] Política de privacidad menciona perfil público + retención de logs

---

*El Pasaporte es la pieza más visible del ecosistema. Si emociona y
funciona, todo lo demás se vuelve creíble.*
