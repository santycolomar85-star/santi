# HOJA DE AUDITORÍA — Master v7 vs BRIEF ANATÓMICO v2.0
### Validación científica del master IA-only `00_DAY0_MASTER_HEROIC_THREEQUARTER_v7_FINAL.png`

> Esta auditoría aplica el **BRIEF_ANATOMICO_VANNAMEI v2.0** (verificado con
> FAO, SERC Smithsonian, NOAA, WoRMS) para separar limpiamente:
> - ❗ **Errores biológicos** (violan anatomía real del *Penaeus vannamei*)
> - 🎨 **Licencias artísticas** (decisiones de marca aceptadas)
> - ✅ **Aciertos** (cumplen brief)

---

## 1. RESULTADO POR LOS 12 PUNTOS BIOLÓGICOS

| # | Punto del BRIEF v2.0 | v7 | Veredicto |
|---|---|---|---|
| B1 | Rostrum visible con dientes (8 dorsal + 2 ventral) | ⚠️ | Rostrum presente pero dientes no claramente aserrados, lisos |
| B2 | Ojos pedunculados (sobre tallos) | ❌ | Pegados a la cabeza, no hay tallos visibles |
| B3 | 2 antenas largas + 2 anténulas cortas bifurcadas | ❌ | Solo se ven las 2 antenas largas. Anténulas ausentes |
| B4 | Carapacho cefalotórax como armadura segmentada | ✅ | Bien visible, con relieve muscular |
| B5 | 5 pares pereiópodos sugeridos (3 con pinzas pequeñas) | ⚠️ | Dos brazos heroicos OK; pereiópodos laterales sugeridos pero sin pinzas visibles |
| B6 | 6 segmentos abdominales contables | ✅ | Se cuentan claramente |
| B7 | Curvatura ventral del abdomen en "coma" | ✅ | Curvatura natural |
| B8 | Abanico caudal con 5 piezas (telson + 2 pares urópodos) | ⚠️ | Se ve abanico al final, pero las 5 piezas no están bien diferenciadas |
| B9 | Pleópodos omitidos (licencia v6) o plumosos | ✅ | Omitidos limpio (decisión Director de Marca) |
| B10 | Pinzas (quelas) PEQUEÑAS, no de bogavante | n/a | Brazos humanizados (licencia art.); las quelas reales no aplican |
| B11 | Color cuerpo dentro del rango canon `#F39A2B` | ✅ | Correcto |
| B12 | Sin elementos prohibidos del §11 BRIEF | ✅ | Sin pinzas grandes, sin cola de pez, sin caparazón cangrejo |

**Score biológico v7:** **6 ✅ + 4 ⚠️ + 2 ❌ = aprox 8/12** (66%).

---

## 2. CRUCE CON CHECKLIST 24 PUNTOS DEL MANUAL

| Punto | v7 | Notas |
|---|---|---|
| A1 Rostrum aserrado | ⚠️ | Dientes no nítidos |
| A2 Cefalotórax armadura | ✅ | OK |
| A3 Ojos pedunculados | ❌ | Pegados |
| A4 Dos antenas largas | ✅ | OK |
| A5 Anténulas cortas | ❌ | Ausentes |
| A6 Seis segmentos abdominales | ✅ | OK |
| A7 Pleópodos | ✅ | Omitidos válidamente |
| A8 Telson + urópodos | ⚠️ | No 5 piezas distinguibles |
| A9 Pereiópodos laterales | ✅ | Pequeñas patas visibles |
| A10 Curvatura S | ✅ | Sí |
| B1 Borla TRICOLOR ambas antenas | ❌ | Solo en una antena |
| B2 Patriótico | ✅ | Tassel cuenta |
| B3 Sin partidista | ✅ | OK |
| C1 Capa azul real | ✅ | OK |
| C2 Cinturón azul eléctrico | ✅ | OK |
| C3 Texto ECUAMAN legible | ✅ | OK |
| C4 Medallón con E | ✅ | Logo Ecuanutrition oficial compositado |
| C5 Tridente con halo | ✅ | OK |
| D1-D3 Paleta + saturación | ✅✅✅ | OK |
| E1 Sin extremidades extra | ✅ | OK |
| E2 Sin watermarks | ✅ | OK |
| E3 Resolución ≥ 2048 | ❌ | 1024×1536 |

**Score checklist v7:** **18-19/24** (vs v2: 8/24, vs v3: 16/24, vs v4: 18/24).

---

## 3. SEPARACIÓN ESTRICTA: ERROR BIOLÓGICO vs LICENCIA ARTÍSTICA

### ❗ Errores biológicos a corregir en v8 (no son licencias)
1. **Ojos no pedunculados** — viola anatomía real
2. **Anténulas cortas bifurcadas ausentes** — viola anatomía real
3. **Rostrum sin dientes nítidos** — viola anatomía real (deben verse 8 dorsal)
4. **Abanico caudal sin 5 piezas distinguibles** — viola anatomía real

### 🎨 Licencias artísticas válidas (NO corregir)
- Brazos humanoides (antropomorfismo necesario para mascot)
- Postura bípeda heroica (mascot, no espécimen)
- Color naranja cocido en lugar de translúcido (decisión de marca para reconocibilidad)
- Pleópodos omitidos bajo cinturón (decisión v6 Director de Marca)
- Capa, tridente, cinturón (lenguaje superhéroe universal)

### 🟡 Decisiones pendientes (ni error ni licencia clara)
- **Tassel solo en una antena:** debería estar en ambas según canon v2.1 — corregir en v8
- **Resolución 1024×1536:** limitación API, requiere upscale post-producción

---

## 4. RECOMENDACIONES PARA v8

### Cambios quirúrgicos a aplicar
| # | Cambio | Cómo |
|---|---|---|
| 1 | Ojos sobre tallos cortos visibles | Prompt: "round eyes mounted on short visible eyestalks emerging from the head, not flat on the head" |
| 2 | Anténulas cortas bifurcadas | Prompt: "in addition to the two long antennae, two shorter bifurcated antennules with two small branches each, in front of the longer antennae" |
| 3 | Rostrum con 8 dientes dorsales nítidos | Prompt: "rostrum like a tiny saw with 8 small triangular dorsal teeth clearly visible on top edge, plus 2 small ventral teeth on the bottom edge" |
| 4 | Abanico caudal con 5 piezas | Prompt: "tail fan with FIVE distinct flat pieces: one central pointed telson plus two pairs of lateral flat uropods" |
| 5 | Tassel tricolor en AMBAS antenas | Prompt: "both antenna tips end in IDENTICAL tricolor tassel, yellow-blue-red flat ribbons with brown leather knot" |

### Mantener (no tocar)
- Pose ¾ heroica
- Capa azul, tridente cian
- Cinturón ECUAMAN
- Color naranja cocido
- Pleópodos omitidos (decisión v6)

### Post-producción aún necesaria
- Recompositar logo Ecuanutrition oficial sobre el medallón
- Upscale R-ESRGAN 2x para llegar a 2048+ px

---

## 5. VEREDICTO FINAL v7

**v7 es la mejor base IA-only que se puede sacar sin v8.**

- Score biológico: 8/12 (con BRIEF v2.0 corregido).
- Score checklist marca: 18-19/24.
- Errores biológicos restantes son **arreglables vía prompt mejorado en v8**.

> **Antes de declarar "master oficial" se debe pasar por v8 y eventualmente
> producción 3D humana** según el plan documentado en
> `06_LAUNCH_KIT/FASE_4_PRODUCTO_DIGITAL/04_GENERADOR_AVATARES_LORA.md`.

---

*Auditoría firmada: Mayo 2026 · Aplicando BRIEF v2.0 con fuentes científicas*
