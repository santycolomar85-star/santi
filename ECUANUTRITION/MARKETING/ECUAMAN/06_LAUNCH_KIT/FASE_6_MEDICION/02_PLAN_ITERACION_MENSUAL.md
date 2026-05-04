# PLAN DE ITERACIÓN MENSUAL
### Cómo aprende y mejora el ecosistema Ecuaman cada 30 días

> Sin un ritual disciplinado de aprendizaje, los datos del dashboard
> son **paisaje**. Este documento define el **proceso operativo
> mensual** que convierte datos en decisiones, decisiones en
> experimentos, y experimentos en mejoras estructurales.

---

## 1. RITUAL MENSUAL — VISTA GENERAL

```
DÍA 1-3       Recolección y limpieza de datos del mes anterior
DÍA 4         REUNIÓN MENSUAL DE INTELIGENCIA (90 minutos)
DÍA 5-7       Diseño de experimentos para el mes en curso
DÍA 8         Lanzamiento de experimentos
DÍA 9-28      Ejecución + monitoreo
DÍA 29-30     Cierre + documentación de aprendizajes
```

---

## 2. REUNIÓN MENSUAL DE INTELIGENCIA (90 min)

### Asistentes obligatorios
- Director de Marca (facilita)
- Product Lead
- Comms Lead
- Director de Impacto
- Tech Lead
- CFO (o representante)

### Agenda fija

```
00:00 — 00:10  Apertura + repaso de compromisos del mes anterior
00:10 — 00:25  North Star (MAG): qué hizo, qué la movió
00:25 — 00:40  Embudo: bottlenecks identificados
00:40 — 00:55  Impacto real (manglares, donaciones, asambleas)
00:55 — 01:10  Voz de Guardianes (NPS, comments, soporte)
01:10 — 01:25  Decisiones del mes + experimentos a lanzar
01:25 — 01:30  Cierre + dueños asignados
```

### Reglas de la reunión
1. **Nadie llega sin haber leído el dashboard previo.**
2. **No se usa pantalla con cifras nuevas — eso es leer datos, no analizarlos.**
3. **Cada decisión queda con dueño + fecha de revisión.**
4. **Se prohíbe "hay que hacer X" sin compromiso humano específico.**
5. **Los experimentos tienen hipótesis y métrica antes del kickoff.**

---

## 3. ESTRUCTURA DE LA RETROSPECTIVA

### Capa 1 — Métricas
Para cada métrica clave, responder 4 preguntas:

1. **¿Qué pasó?** (cifra)
2. **¿Por qué pasó?** (hipótesis)
3. **¿Qué aprendimos?** (insight reusable)
4. **¿Qué hacemos al respecto?** (acción concreta)

### Capa 2 — Voz de la comunidad

Cada mes el equipo lee **al azar 30 menciones, 30 mensajes de soporte
y 30 respuestas a NPS**. Se busca:

- Frases que se repiten (positivas y negativas)
- Sorpresas inesperadas
- Solicitudes recurrentes que aún no atendemos

Output: máximo 5 frases textuales que se llevan a la reunión.

### Capa 3 — Voz del equipo

Pregunta única: **"¿Qué fricción te frenó este mes?"**

Recoger anónimo en form con 48h previas. Top 3 fricciones se atienden
con dueño + fecha.

### Capa 4 — Voz del mercado

¿Qué hicieron en el mes:
- otras mascots / marcas-país
- ONGs marinas
- competidores en camarón
- stakeholders de Ecuador (gobierno, exportadores, gremios)

Output: 1 página con observaciones que afectan estrategia Ecuaman.

---

## 4. CICLO DE EXPERIMENTOS

### Formato de hipótesis (template)

```
TÍTULO:
HIPÓTESIS:
  Si [cambiamos X],
  entonces [Y métrica] mejorará [Z%] en [periodo].
  Porque [razón / insight previo que lo sostiene].

DUEÑO:
MÉTRICA PRIMARIA:
MÉTRICA GUARDRAIL (no debe empeorar):
DURACIÓN:
TAMAÑO MUESTRA REQUERIDO (95% conf):
RESULTADO ESPERADO PRE-EXPERIMENTO:
RESULTADO REAL:
DECISIÓN: [adoptar / iterar / matar]
```

### Reglas
- **Máximo 4 experimentos paralelos** (evitar interferencia).
- **Cada experimento dura mínimo 14 días** (con n adecuado).
- **No se mezcla "experimentos" con "fixes"** — los fixes se hacen
  igualmente, pero no entran al ciclo de aprendizaje formal.

### Ejemplos de experimentos típicos primer trimestre

| ID | Título | Hipótesis |
|---|---|---|
| EXP-01 | Onboarding 4→3 pasos | Si reducimos paso 2 fusionando avatar y rasgos, activación ↑12% |
| EXP-02 | Misión "Sembrar marea" con video | Si añadimos video 30s al brief, completion rate ↑20% |
| EXP-03 | Email D7 personalizado | Si enviamos email con el avatar generado al D7, retención D7→D14 ↑8% |
| EXP-04 | Asamblea con voz Don Galo invitado | Si Don Galo participa, asistencia ↑40% |

---

## 5. BITÁCORA DEL DIRECTOR DE MARCA

Cada decisión grande se registra en una **bitácora pública del equipo**
(notion `/bitacora` interna):

```
2026-05-04 · Decisión: aumentar inversión paid en TikTok 2x
  Contexto: CAC TikTok = $1.10 vs Meta $2.30
  Datos: ver dashboard CAC por canal (link)
  Riesgo: saturación de la audiencia, fatigue
  Mitigación: rotación creativa cada 5 días
  Revisión: 2026-06-04
  Resultado: [se llena en revisión]
```

Esto crea **memoria institucional**: en 12 meses se puede saber por
qué se tomó cada decisión, qué pasó, y qué aprendimos.

---

## 6. APRENDIZAJES → MANUAL VIVO

El **Manual de Marca** (`01_MANUAL/`) NO es un libro estático.
Cada mes, los aprendizajes que validan o refutan partes del manual
**actualizan el manual**:

- Si descubrimos que el tono "épico" no resuena en TikTok pero sí
  el tono "humorístico cálido", actualizamos `MANUAL/03_TONO_DE_VOZ.md`.
- Si validamos que las asambleas funcionan mejor a las 19:00 ECT que
  a las 21:00, lo dejamos escrito.
- Cada actualización tiene fecha y razón en commit.

---

## 7. RUTAS DE DECISIÓN

```
Métrica desviada
   │
   ├─ <5% del esperado    → observar 1 mes más, no actuar
   ├─ 5-15% del esperado  → experimento dirigido el mes siguiente
   ├─ 15-30% del esperado → reunión emergencia, plan de respuesta 7 días
   └─ >30% del esperado   → CRISIS: protocolo de respuesta especial
                              (ver doc 03_LEGAL/CRISIS_PLAYBOOK)
```

---

## 8. ANTI-PATRONES A EVITAR

1. **Vanity metrics como argumento** — "tenemos 100k seguidores"
   no es éxito si MAG es 5k.
2. **Datos sin acción** — el dashboard precioso pero nadie cambia nada.
3. **Cherry-picking** — ignorar las métricas que no nos gustan.
4. **Reactividad semanal** — cambiar estrategia cada lunes
   destruye señales de tendencia.
5. **Experimentos eternos** — un test que dura 3 meses sin cierre
   nunca enseña nada.
6. **Decisiones por jerarquía** — el más senior gana sin datos. NO.
7. **Ocultación de fracasos** — si EXP-01 falló, se documenta y se
   aprende. Eso es éxito.

---

## 9. CHECKLIST MENSUAL (template)

- [ ] Datos del mes consolidados al día 3
- [ ] Reunión mensual ejecutada con todos los roles
- [ ] Top 5 frases de Guardianes leídas en sesión
- [ ] Mínimo 1 experimento cerrado y documentado
- [ ] Mínimo 2 experimentos lanzados
- [ ] Reporte público de transparencia publicado el día 10
- [ ] Bitácora del Director actualizada
- [ ] Manual de Marca actualizado con aprendizajes nuevos (si aplica)
- [ ] Plan financiero ajustado a runway real

---

*La iteración disciplinada es lo que separa marcas que duran 1 año
de marcas que duran 50.*
