# DASHBOARD DE KPIs — ECUAMAN
### Métricas, queries SQL, umbrales de alarma, dashboards operativos

> Este documento define **qué se mide, dónde, con qué fórmula, quién es
> dueño, qué pasa si la métrica se desvía**. Es el manual operativo
> del equipo de Inteligencia de Marca.

---

## 1. JERARQUÍA DE MÉTRICAS

```
NORTH STAR
  └─ Guardianes Activos Mensuales (MAG)

    ├─ INPUTS DE MAG (qué lo mueve)
    │   ├─ Adquisición → registros nuevos
    │   ├─ Activación → primer pasaporte + primera misión
    │   ├─ Retención → segunda y tercera visita
    │   └─ Resurrección → reactivación de inactivos
    │
    ├─ INDICADORES DE IMPACTO
    │   ├─ Manglares plantados (real validados)
    │   ├─ Asambleas: asistencia + decisión cumplida
    │   └─ Donaciones recibidas + ejecutadas
    │
    ├─ INDICADORES DE MARCA
    │   ├─ Alcance medios + redes
    │   ├─ Sentimiento (análisis de menciones)
    │   ├─ Earned media value
    │   └─ NPS Guardianes
    │
    └─ INDICADORES OPERATIVOS
        ├─ Costo de adquisición por Guardián (CAC)
        ├─ LTV por Guardián
        ├─ Disponibilidad plataforma
        └─ Quejas / soporte volumen
```

---

## 2. DICCIONARIO DE MÉTRICAS

### 2.1 NORTH STAR — Guardianes Activos Mensuales (MAG)

```sql
SELECT COUNT(DISTINCT g.id) AS guardianes_activos_30d
FROM guardianes g
WHERE g.estado = 'activo'
  AND EXISTS (
    SELECT 1 FROM eventos e
    WHERE e.guardian_id = g.id
      AND e.tipo IN ('login','mision_completada','asamblea_voto',
                     'pasaporte_compartido','donacion_completada')
      AND e.ocurrido_en >= NOW() - INTERVAL '30 days'
  );
```

**Umbral de alarma:** caída >15% mes a mes → reunión emergencia.
**Dueño:** Director de Marca + Product Lead.
**Visualización:** línea de tiempo diaria con MA-7d.

### 2.2 Adquisición — Registros nuevos / día

```sql
SELECT DATE(fecha_registro) AS dia,
       COUNT(*) AS nuevos_guardianes,
       COUNT(*) FILTER (WHERE pais_iso = 'EC') AS de_ecuador,
       COUNT(*) FILTER (WHERE pais_iso != 'EC') AS internacional
FROM guardianes
WHERE fecha_registro >= NOW() - INTERVAL '90 days'
GROUP BY DATE(fecha_registro)
ORDER BY dia DESC;
```

**Umbral:** mínimo 100 registros/día post-lanzamiento estabilizado.
**Dueño:** Comms Lead.
**Visualización:** barras diarias + comparación semana actual vs anterior.

### 2.3 Activación — Tasa de Pasaporte + 1ª misión

```sql
WITH cohort AS (
  SELECT id, fecha_registro
  FROM guardianes
  WHERE fecha_registro >= NOW() - INTERVAL '7 days'
    AND fecha_registro < NOW() - INTERVAL '24 hours'
)
SELECT COUNT(*) FILTER (
    WHERE EXISTS (SELECT 1 FROM pasaportes p WHERE p.guardian_id = c.id)
      AND EXISTS (SELECT 1 FROM misiones_completadas mc WHERE mc.guardian_id = c.id)
  )::DECIMAL / NULLIF(COUNT(*),0) AS tasa_activacion
FROM cohort c;
```

**Umbral:** >70%. Si <55%, hay friction en el flujo onboarding.
**Dueño:** Product Lead + UX.

### 2.4 Retención — D1 / D7 / D30

```sql
-- Retención D7 cohorte específica
SELECT
  COUNT(DISTINCT c.id) AS cohorte_size,
  COUNT(DISTINCT c.id) FILTER (
    WHERE EXISTS (
      SELECT 1 FROM eventos e
      WHERE e.guardian_id = c.id
        AND e.ocurrido_en BETWEEN c.fecha_registro + INTERVAL '6 days'
                              AND c.fecha_registro + INTERVAL '8 days'
    )
  ) AS retornaron_d7
FROM guardianes c
WHERE DATE(c.fecha_registro) = '2026-05-04';
```

**Umbrales esperados primer trimestre:**
- D1 ≥ 40%
- D7 ≥ 22%
- D30 ≥ 12%

**Dueño:** Product Lead.

### 2.5 Engagement — Misiones / Guardián / mes

```sql
SELECT
  AVG(misiones_count) AS prom_misiones_por_guardian
FROM (
  SELECT g.id, COUNT(mc.id) AS misiones_count
  FROM guardianes g
  LEFT JOIN misiones_completadas mc
    ON mc.guardian_id = g.id
   AND mc.completada_en >= NOW() - INTERVAL '30 days'
  WHERE g.fecha_registro <= NOW() - INTERVAL '30 days'
  GROUP BY g.id
) t;
```

**Umbral:** >1.5 misiones promedio/Guardián/mes.
**Dueño:** Comms + Product.

### 2.6 Impacto — Manglares plantados (validados)

```sql
SELECT COUNT(*) AS manglares_plantados
FROM misiones_completadas mc
JOIN misiones m ON m.id = mc.mision_id
WHERE m.codigo = 'sembrar_manglar'
  AND mc.validado_en IS NOT NULL;
```

**Umbral Año 1:** 50.000 manglares.
**Dueño:** Director de Impacto + ONG aliada.
**Validación:** evidencia foto + GPS + ONG verifica en lote semanal.

### 2.7 Asambleas — asistencia + cumplimiento de decisión

```sql
-- Asistencia
SELECT a.numero, a.titulo, a.participantes,
       a.participantes::DECIMAL / (
         SELECT COUNT(*) FROM guardianes WHERE estado='activo'
       ) AS tasa_participacion
FROM asambleas a
WHERE a.estado = 'cerrada'
ORDER BY a.numero DESC;

-- Cumplimiento (lo lleva el Director de Impacto manualmente como
-- "decisión cumplida sí/no" en metadata de la asamblea)
SELECT a.numero,
       a.decision_final,
       (a.metadata ->> 'cumplida')::BOOLEAN AS cumplida,
       a.metadata ->> 'evidencia_url' AS evidencia
FROM asambleas a
WHERE a.estado = 'cerrada';
```

**Umbral:** participación ≥10% del MAG en asambleas.
**Cumplimiento de decisión:** **100%** — no negociable. Si no se puede
cumplir, comunicar transparentemente el bloqueo.

### 2.8 Donaciones

```sql
SELECT
  c.titulo,
  c.recaudado_centavos / 100.0 AS recaudado_usd,
  c.meta_centavos / 100.0 AS meta_usd,
  (c.recaudado_centavos::DECIMAL / NULLIF(c.meta_centavos,0)) AS progreso
FROM causas c
ORDER BY c.creado_en DESC;
```

**Dueño:** CFO + Director de Impacto.
**Transparencia:** monto recaudado y monto ejecutado a la causa real
publicado mensualmente.

### 2.9 Marca — Sentimiento

```
INPUT: feed de menciones desde Brand24 / Mention.com / Talkwalker
TRANSFORM: análisis NLP por categoría sentimiento
OUTPUT en dashboard:
  - Volumen menciones (línea diaria)
  - Net Sentiment Score = (positivos - negativos) / total
  - Top frases positivas / negativas
  - Mapa geográfico
```

**Umbral:** Net Sentiment > +40 en estado estable.

### 2.10 Marca — NPS

Encuesta in-app cada 90 días al Guardián:
> "En una escala de 0 a 10, ¿qué tan probable es que recomiendes ser Guardián de Ecuaman a un amigo?"

```sql
SELECT
  COUNT(*) FILTER (WHERE puntaje >= 9)::DECIMAL / COUNT(*) - 
  COUNT(*) FILTER (WHERE puntaje <= 6)::DECIMAL / COUNT(*) AS nps
FROM nps_responses
WHERE creado_en >= NOW() - INTERVAL '90 days';
```

**Umbral:** NPS > 50.

### 2.11 CAC — Costo de adquisición de Guardián

```
CAC = (gasto en marketing pagado del periodo) / (Guardianes nuevos del periodo)
```

Tracked via UTMs + atribución last-click + multi-touch (Año 2+).

**Umbrales:**
- CAC orgánico: <$0.50
- CAC paid: <$3.00 (early), <$1.50 (estado estable)

### 2.12 LTV — Valor de vida de Guardián

```
LTV = Σ (donaciones + revenue de merch + valor de earned media generado por el Guardián)
       a lo largo de su vida activa
```

Año 1: estimación basada en cohortes pequeñas.
Año 2: modelo predictivo con datos reales.

**Umbral healthy:** LTV / CAC > 3.

### 2.13 Disponibilidad plataforma

- API uptime: >99.9% (SLO)
- Web LCP p75 mobile: <2.5s
- Crash-free sessions app: >99.9%

Tracked via UptimeRobot + Sentry + Vercel Analytics.

### 2.14 Soporte — volumen y tiempo de respuesta

- Tiempo a primera respuesta: <12h hábiles
- Tiempo a resolución: <72h
- Volumen tickets / 1.000 Guardianes / mes: <8

---

## 3. STACK DE BI Y DASHBOARDS

```
FUENTES
├── Postgres (Neon)         → métricas de producto y comunidad
├── PostHog                 → eventos de uso, funnels, replays
├── Sentry                  → calidad técnica
├── Brand24/Mention         → menciones y sentimiento
├── Stripe / PayPal         → revenue
└── Hojas Google manuales   → impacto físico (manglares verificados)

PROCESAMIENTO
├── Materialized views Postgres (refresh cada 1h)
├── PostHog Insights y Dashboards
└── Metabase self-hosted (SQL libre para equipo)

VISUALIZACIÓN
├── Metabase                → dashboards internos
├── Notion                  → reporte mensual ejecutivo
├── ecuaman.ec/transparencia → vista pública de impacto
└── Slack alerts            → métricas críticas en canal #pulso-ecuaman
```

---

## 4. DASHBOARDS OPERATIVOS

### Dashboard 1 — "Pulso Diario"
- MAG hoy + variación 7d
- Registros últimas 24h por país (heat map)
- Misiones completadas hoy
- Eventos críticos / errores 5xx
- Disponibilidad plataforma

**Audiencia:** equipo full, en pantalla en sala de operaciones.

### Dashboard 2 — "Cohorte Marca"
- Embudo: visita → registro → pasaporte → 1ª misión → 2ª visita
- Retención D1 / D7 / D30 por cohorte semanal
- Top fuentes de tráfico orgánico
- Top creadores que envían tráfico
- Sentimiento neto últimos 7d

**Audiencia:** Comms + Director de Marca.

### Dashboard 3 — "Impacto Real"
- Manglares plantados (mapa Ecuador)
- Donaciones recibidas + ejecutadas
- Asambleas: histórico + decisiones + cumplimiento
- Causas: progreso barras

**Audiencia:** público (`ecuaman.ec/transparencia`).

### Dashboard 4 — "Salud Financiera"
- CAC por canal (gráfico)
- LTV cohorte
- Burn rate mensual
- Runway proyectado
- Revenue acumulado por línea (donaciones, merch, licencias)

**Audiencia:** CFO + Director General.

---

## 5. ALERTAS AUTOMÁTICAS

```yaml
alerts:
  - name: caida_registros_24h
    query: nuevos_guardianes_24h < 50
    canal: slack #alertas
    severidad: alta
    
  - name: caida_mag_semanal
    query: MAG_actual / MAG_semana_pasada < 0.85
    canal: slack #alertas + email director
    severidad: critica
    
  - name: error_rate_5xx
    query: errores_5xx_5min > 10
    canal: slack #ingenieria + pager
    severidad: critica
    
  - name: causa_meta_alcanzada
    query: causa.recaudado >= causa.meta
    canal: slack #celebraciones + email director impacto
    severidad: positiva
    
  - name: sentimiento_negativo_pico
    query: net_sentiment_24h < -10 OR menciones_negativas_1h > 50
    canal: slack #comms + email director
    severidad: alta
    
  - name: backup_fallido
    query: ultimo_backup > 25h
    canal: slack #ingenieria + pager
    severidad: critica
```

---

## 6. RITMO DE REPORTES

| Reporte | Frecuencia | Audiencia | Formato |
|---|---|---|---|
| Pulso Diario | diario | equipo | Slack auto + dashboard pantalla |
| Reporte Semanal | lunes 10am | leadership | Notion 1 página + reunión 30min |
| Reporte Mensual | día 5 mes siguiente | leadership + advisors | Notion 4-6 páginas + reunión 90min |
| Transparencia Pública | mensual día 10 | Guardianes y prensa | Web + email a comunidad |
| Reporte Trimestral | día 15 mes post-Q | board + inversionistas | PDF formal + sesión 2h |
| Reporte Anual | 30 enero | público | Documento web + PDF descargable |

---

## 7. POLÍTICA DE DATOS

- **Retención de eventos brutos:** 24 meses, luego agregados.
- **Datos personales (PII) en analytics:** prohibidos. Sólo IDs anónimos.
- **Acceso a datos crudos:** equipo BI + Director Tech, log de auditoría.
- **Anonimización antes de compartir** con partners/investigadores académicos.
- **Consentimiento explícito** para analytics de comportamiento profundo (replays).
- **Derecho al olvido:** borrar elimina identidad y enlaza eventos a "anónimo histórico".

---

*Sin medir, no aprendemos. Sin aprender, no crecemos. Sin crecer, no
servimos a la comunidad como prometimos.*
