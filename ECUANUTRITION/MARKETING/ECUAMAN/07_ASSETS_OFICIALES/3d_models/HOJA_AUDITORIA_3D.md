# HOJA DE AUDITORÍA — Modelos 3D Meshy v9 y v10
### Comparativa lado a lado + veredicto contra BRIEF v2.0

> Auditoría aplicada al pipeline Meshy AI **image-to-3D** sobre Ecuaman v8 FINAL.
> Dos generaciones con inputs distintos: v9 con fondo oceánico oscuro, v10 con
> fondo blanco limpio (post-threshold de bg).

---

## 1. ESPECIFICACIONES TÉCNICAS

| Atributo | v9 Meshy | v10 Meshy |
|---|---|---|
| Modelo IA | meshy-5 | meshy-5 |
| Input image | v8 FINAL (fondo oceánico) | v8 bgwhite (fondo blanco) |
| Polycount real | 99.553 caras | 99.406 caras |
| Vértices | 65.047 | 63.778 |
| Topología | Quad target | Quad target |
| Material | PBR (4 mapas) | PBR (4 mapas) |
| Formatos exportados | glb, fbx, obj, stl, usdz | glb, fbx, obj, stl, usdz |
| Tamaño .glb | 12.2 MB | 11.5 MB |
| Tamaño total carpeta | 57.7 MB | 56.5 MB |

---

## 2. AUDITORÍA VISUAL (vista frontal del thumbnail)

| Elemento | v9 | v10 | Ganador |
|---|---|---|---|
| Cuerpo naranja | OK | OK | empate |
| Pose ¾ heroica | OK | OK | empate |
| Cefalotórax con musculatura | OK | OK | empate |
| Segmentos abdominales | OK 6 visibles | OK 6 visibles | empate |
| Cola con abanico | OK | OK | empate |
| Cinturón ECUAMAN legible | OK | OK | empate |
| Medallón con logo | OK | OK | empate |
| **Capa azul** | ❌ mancha negra deformada | ⚠️ marrón oscuro estructurado | **v10** |
| **Tridente cian** | ❌ NEGRO deformado, no se reconoce | ✅ NARANJA SÓLIDO bien definido | **v10** |
| **Antenas** | ❌ dreadlocks negros caóticos | ⚠️ aún parecen pelo, mejor estructura | **v10** |
| Cresta cabeza | exagerada, púas | exagerada, púas | empate |
| Expresión | OK sonrisa | OK sonrisa más clara | leve v10 |

**Veredicto visual:** v10 gana 4 categorías, v9 cero, empate en 8.

---

## 3. AUDITORÍA BIOLÓGICA (BRIEF v2.0 — 12 puntos)

| # | Punto BRIEF v2.0 | v9 | v10 |
|---|---|---|---|
| B1 | Rostrum con dientes (8 dorsal + 2 ventral) | ⚠️ | ⚠️ |
| B2 | Ojos pedunculados sobre tallos | ❌ | ❌ |
| B3 | 2 antenas + 2 anténulas bifurcadas | ❌ deformadas | ❌ deformadas |
| B4 | Cefalotórax como armadura segmentada | ✅ volumétrico | ✅ volumétrico |
| B5 | 5 pares pereiópodos sugeridos | ⚠️ | ⚠️ |
| B6 | 6 segmentos abdominales | ✅ | ✅ |
| B7 | Curvatura ventral en "coma" | ✅ | ✅ |
| B8 | Abanico caudal con 5 piezas | ⚠️ | ⚠️ |
| B9 | Pleópodos omitidos | ✅ | ✅ |
| B10 | Pinzas pequeñas | n/a | n/a |
| B11 | Color naranja `#F39A2B` | ✅ | ✅ |
| B12 | Sin elementos prohibidos | ✅ | ✅ |

**Score biológico:** v9 **6/12 (50%)**, v10 **6/12 (50%)** — empatados en biología.

> El score biológico no cambió porque los problemas (ojos no pedunculados,
> anténulas deformadas, abanico caudal sin 5 piezas) son **invariantes
> de Meshy**. Lo que cambió fue la fidelidad al input 2D (capa, tridente).

---

## 4. CONCLUSIÓN COMPARATIVA

### v10 es mejor en producción
- Tridente reconocible (vs negro deformado en v9)
- Capa con estructura (vs mancha en v9)
- Antenas menos caóticas (aunque siguen sin ser anatómicas)

### v10 NO supera el techo de Meshy
- Antenas se generan como pelo, no como filamentos rígidos
- Ojos pedunculados ausentes en ambos
- Abanico caudal sin 5 piezas en ambos
- Color del tridente y capa no se transfieren correctamente al PBR

---

## 5. VEREDICTO FINAL

**v10 Meshy es la mejor base 3D Meshy posible.** Pero NO es producción mundial.

### ¿Para qué sirve v10?
✅ **Validación interna** y demos en presentaciones
✅ **Pipeline de prueba** del viewer 3D del microsite (FASE 4)
✅ **Posing estático** para mockups de packaging y stickers
✅ **Iteración con artistas humanos** que pueden retopologizar/retexturizar

### ¿Para qué NO sirve v10?
❌ **Animación profesional** (rig vendría torcido por las antenas-pelo)
❌ **Empaque final / publicidad nacional**
❌ **Registro de marca 3D**
❌ **Asset oficial mundial**

---

## 6. PRÓXIMO PASO RECOMENDADO

| Camino | Costo | Calidad esperada | Tiempo |
|---|---|---|---|
| **A. Cerrar IA-only.** Aceptar v10 como master 3D provisional + v8 FINAL como master 2D provisional. Contratar estudio 3D humano para producción mundial. | $5k-8k | 100% canon | 4-6 semanas |
| B. Iterar más con Meshy. Probar más prompts, distintos modos (cartoon, realistic). | $0-50 | tope ~10% más | días |
| C. Probar Rodin (Hyper3D) cuando haya presupuesto. | $5-20 | superior a Meshy | 1-2h |
| D. Probar Tripo3D (auto-rigging incluido). | free tier | similar a Meshy | 1h |

**Mi recomendación:** **A — cerrar IA-only y arrancar contratación humana.**

El presupuesto de $5k-8k está dentro del **3% del presupuesto total de FASE 4**
documentado en `06_LAUNCH_KIT/FASE_4_PRODUCTO_DIGITAL/04_GENERADOR_AVATARES_LORA.md`.
La calidad mundial que la marca necesita NO va a salir de IA-only en 2026.

---

## 7. ARTEFACTOS DISPONIBLES EN EL REPO

```
07_ASSETS_OFICIALES/3d_models/
├── COMPARATIVA_v9_vs_v10_thumbnails.png    ← side-by-side
├── HOJA_AUDITORIA_3D.md                     ← este documento
├── v9_meshy/
│   ├── ecuaman_v9_meshy.{glb,fbx,obj,stl,usdz}
│   ├── thumbnail.png
│   ├── texture_0_{base_color,metallic,normal,roughness}.png
│   └── renders/v9_meshy_GRID_6views.png
└── v10_meshy/
    ├── ecuaman_v10_meshy.{glb,fbx,obj,stl,usdz}
    ├── thumbnail.png
    ├── texture_0_{base_color,metallic,normal,roughness}.png
    └── renders/v10_meshy_GRID_6views.png
```

**Para revisar 3D interactivo:** sube cualquier `.glb` a https://gltf-viewer.donmccurdy.com/

---

*Auditoría firmada: Mayo 2026 · Pipeline Meshy AI image-to-3D agotado*
