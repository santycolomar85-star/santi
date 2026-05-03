# REPORTE v3 — Auditoría honesta y regeneración del master oficial

> **Contexto:** durante la sesión 5 se identificó que el master canónico
> declarado oficial (`00_DAY0_MASTER_HEROIC_VERTICAL_v2.png`) **no cumple
> 14 puntos del checklist de validación** que el propio sistema documenta.
> Este reporte documenta los fallos, la nueva metodología v3, y los
> resultados esperados.

---

## 1. AUDITORÍA HONESTA DE v2 vs CHECKLIST 24 PUNTOS

| # | Checklist | Estado v2 | Evidencia |
|---|---|---|---|
| A1 | Rostrum con dientes dorsales aserrados | ❌ | Pico liso plano, sin los 8 dientes |
| A2 | Cefalotórax como armadura segmentada | ❌ | Torso humano liso pintado naranja |
| A3 | Ojos pedunculados sobre tallos | ❌ | Ojos pegados a la cabeza |
| A4 | Dos antenas largas | ⚠️ | Sí están, pero sin anténulas |
| A5 | Anténulas cortas | ❌ | Ausentes |
| A6 | Seis segmentos abdominales | ❌ | No contables, abdomen humano |
| A7 | Pleópodos visibles | ❌ | Ausentes |
| A8 | Telson + urópodos en abanico | ❌ | Cola decorativa, no abanico |
| A9 | Pereiópodos laterales | ❌ | Ausentes |
| A10 | Curvatura S del cuerpo | ❌ | Postura humana rígida |
| B1 | Borla orden EXACTO | ❌ | Orden invertido + solo 1 antena |
| B2 | Elemento patriótico visible | ⚠️ | Solo parcial |
| B3 | Sin símbolos partidistas | ✅ | OK |
| C1 | Capa azul real `#0046AD` | ✅ | OK |
| C2 | Cinturón azul eléctrico | ⚠️ | Más speedo que cinturón |
| C3 | Texto "ECUAMAN" legible | ⚠️ | Legible pero fuente incorrecta |
| C4 | Medallón con borde dorado y "E" | ⚠️ | "E" sin cola onda |
| C5 | Tridente con halo plasma | ✅ | OK (pero punta central no 10% más larga) |
| D1 | Cuerpo en `#F39A2B` | ✅ | OK |
| D2 | Sin colores fuera de paleta | ✅ | OK |
| D3 | Saturación cinematográfica | ✅ | OK |
| E1 | Sin extremidades extra | ✅ | OK |
| E2 | Sin watermarks | ✅ | OK |
| E3 | Resolución mínima 2048 | ❌ | Actual: 1024×1536 |

**Score real: 8 cumplidos / 24** (no 24/24 como decía el reporte original).

---

## 2. POR QUÉ FALLA EL PROMPT-ONLY

`gpt-image-1` no respeta especificaciones biológicas finas en una sola pasada.
El v2 usó `images.generate` con prompt rico **pero sin ancla visual**, y el modelo:

- Antropomorfiza por defecto (humano + accesorios temáticos).
- Ignora detalles enumerados al final del prompt (sesgo posicional).
- Confunde "shrimp tail at bottom" con "human pose con cola decorativa".

**Las referencias históricas del Drive original (`03_REFERENCIAS/historicas/`)
tienen MEJOR anatomía que el v2** porque fueron retocadas humanamente. Ese
es el punto de partida correcto.

---

## 3. METODOLOGÍA v3 — ANCLA HISTÓRICA + PROMPT QUIRÚRGICO

### Cambios técnicos respecto a v2

| Atributo | v2 | v3 |
|---|---|---|
| API | `images.generate` | `images.edit` con referencia |
| Ancla visual | ninguna | `ECUAMAN_master_vertical_emblem.png` |
| Estructura del prompt | descripción libre | enumeración por bloques anatómicos (10 bloques) |
| Énfasis sesgo posicional | ignorado | crítico al inicio + repeticiones clave |
| Variantes | 1 sola | **3 ortogonales** (heroico vertical, ¾, dinámico nadando) |
| Formato | 1024×1536 | 1024×1536 (limitación del modelo, upscale humano post) |

### Los 10 bloques quirúrgicos del prompt v3

1. **Cabeza**: rostrum con 8 dientes, ojos pedunculados, 2+2 antenas, sin dientes humanos.
2. **Antenas**: ambas con tassel idéntico, orden rojo-amarillo correcto + nudo cuero.
3. **Cefalotórax**: armadura segmentada con relieve muscular, no torso liso.
4. **Brazos**: 2 humanoides, 5 dedos.
5. **Pereiópodos laterales**: 3 pares mínimo decorativos.
6. **Pleópodos**: feathery semi-translúcidos.
7. **Cinturón**: medallón único, "E" con cola onda, "ECUAMAN" Bebas Neue arched.
8. **Capa**: forro interior visible (azul más oscuro `#002D70`).
9. **Tridente**: punta central 10% más larga.
10. **Ambiente**: gradiente Pacífico, god rays, plancton bokeh.

---

## 4. CRITERIO DE ÉXITO v3

| Métrica | Objetivo |
|---|---|
| Score checklist | ≥ 18/24 (vs 8/24 actual) |
| Anatomía vannamei reconocible | sí (no humano disfrazado) |
| Tassels en ambas antenas correctos | sí |
| "ECUAMAN" legible con tipografía geométrica | sí |
| Validación humana | Director de Marca firma o veta |

> **Si v3 alcanza ≥18/24 → es la nueva base hasta producción humana.**
> **Si v3 < 18/24 → admitir que IA-only no basta y acelerar contratación
> de estudio 3D según `06_LAUNCH_KIT/FASE_4_PRODUCTO_DIGITAL/04_GENERADOR_AVATARES_LORA.md`.**

---

## 5. VARIANTES GENERADAS EN v3

Tres candidatos ortogonales para que el equipo elija (no para combinar):

| ID | Pose | Uso primario |
|---|---|---|
| `00_DAY0_MASTER_HEROIC_VERTICAL_v3` | Heroica frontal estática | Branding, packaging, redes |
| `00_DAY0_MASTER_HEROIC_THREEQUARTER_v3` | ¾ con tridente diagonal | Microsite hero, app onboarding |
| `00_DAY0_MASTER_DYNAMIC_SWIM_v3` | Nadando con motion blur | Reels, video opener, animación base |

Todos comparten **idéntica identidad visual** anclada al histórico.

---

## 6. PROCESO DE VALIDACIÓN POST-GENERACIÓN

1. GitHub Actions ejecuta `08_master_v3.json` automáticamente al recibir push.
2. Las 3 imágenes quedan en `auto_generated/` con sufijo `_v3`.
3. Director de Marca audita las 3 con el checklist 24 puntos.
4. Si una pasa ≥18/24 → se promueve a `_OFICIAL_v3` y reemplaza al v2 en
   manuales y comunicaciones.
5. Si ninguna pasa → se acepta que el camino IA-only se agotó y se
   ejecuta el plan de contratación 3D.

---

## 7. COSTO DE ESTA REGENERACIÓN

| Línea | Cantidad | USD |
|---|---|---|
| Generación gpt-image-1 HD 1024×1536 con `images.edit` | 3 | $0.50 |
| Tiempo de cómputo GitHub Actions | ~5 min | $0 (free tier) |
| **TOTAL** | | **$0.50** |

Si necesita reintentos: cada uno son $0.17 adicionales.

---

## 8. LO QUE NO CAMBIA RESPECTO A LA HONESTIDAD ANTERIOR

Aún cuando v3 mejore, **sigue siendo IA-only**. El roadmap correcto sigue
siendo:

> **v3 = base de trabajo aceptable** → **producción 3D humana** = master
> definitivo mundial → **alimenta el LoRA Ecuaman** de FASE 4.

No existe atajo a "calidad Pixar" sin un humano experto en el loop.

---

*Reporte generado: Mayo 2026 · Sesión de continuación ECUAMAN*
