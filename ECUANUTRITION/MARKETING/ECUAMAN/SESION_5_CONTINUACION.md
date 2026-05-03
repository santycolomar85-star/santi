# SESIÓN 5 — Continuación tras subida del logo oficial

> Breve nota de continuidad entre las sesiones 1–4 (sistema completo de marca
> ECUAMAN ya producido) y el siguiente bloque de trabajo, ahora que el
> isotipo oficial PNG de Ecuanutrition ya está en el repositorio.

---

## ✅ ESTADO HEREDADO DE LAS SESIONES 1–4

| Bloque | Estado | Carpeta |
|---|---|---|
| Manual de marca | Completo | `01_MANUAL/` |
| Prompts maestros 7 plataformas | Completo | `02_PROMPTS/` |
| Brief anatómico vannamei + checklist 24 puntos | Completo | `03_REFERENCIAS/` |
| Plantillas de contenido | Completo | `04_USO_REDES/` |
| Estrategia + biblia + calendario + saga + campaña 5 años | Completo | `05_ESTRATEGIA/` |
| Launch Kit fases 1, 2, 3, 5 | Completo | `06_LAUNCH_KIT/` |
| **38 / 38 imágenes canónicas** | Completo | `07_ASSETS_OFICIALES/auto_generated/` |
| 5 docs publicación-listos | Completo | `08_PUBLICACION_LISTA/` |

Las 4 imágenes que el modelo `gpt-image-1` no lograba (silueta, tres
cristales, ep2 poster, multitud playa) fueron resueltas por subida manual
del fundador.

---

## 🆕 LO QUE DESBLOQUEÓ LA SESIÓN 5

El fundador subió al repo, en commit `97c84c6`, los activos oficiales que
hasta ahora se aproximaban con prompt:

```
03_REFERENCIAS/
├── Ecuanutrition_Isotipo_Azul.png       ← NUEVO CANON
├── Ecuanutrition_Isotipo_blanco.png
├── Ecuanutrition_Logo_ fAzul.png
├── Ecuanutrition_Logo_ fBlanco1.png
├── Ecuanutrition_Outlook_64x64.png
├── Ecuanutrition_Outlook_128x128.png
└── Ecuanutrition_Outlook_256x256.png
```

Hasta esta sesión, el emblema en el medallón del cinturón y en los broches
de los hombros era una *descripción textual* en el prompt (E serif + dos
curvas + punto cian). Eso producía variantes razonables pero nunca el
isotipo exacto. Con el PNG oficial ahora se puede usar `images.edit` y
forzar consistencia visual real con la marca.

---

## 🔧 CAMBIO TÉCNICO INTRODUCIDO EN ESTA SESIÓN

Se añadió el campo `reference_image` al prompt master:

```
scripts/prompts/00_day0_master.json
  id: 00_DAY0_MASTER_HEROIC_VERTICAL_v6_OFFICIAL_LOGO
  reference_image: ECUANUTRITION/MARKETING/ECUAMAN/03_REFERENCIAS/
                   Ecuanutrition_Isotipo_Azul.png
```

`scripts/generate.py` ya soporta `reference_image` (líneas 56–62):
cuando está presente, llama a `client.images.edit(...)` en lugar de
`client.images.generate(...)`, pasando el PNG oficial como ancla visual.

**Generación auto-disparada en este push.** La condición de la pausa
(`f6a8c43`) era *"hasta tener logo oficial PNG en repo"*. Ya está. Por
tanto, en esta sesión re-habilité el trigger automático en `push` para
que el push de la rama `claude/continue-ecuaman-sessions-aRTBU` produzca
el master v6 sin que el fundador tenga que tocar nada.

Costo previsto: **una sola imagen 1024×1536 HD ≈ $0.17**.

---

## ▶️ LO QUE DEBERÍA PASAR AUTOMÁTICAMENTE TRAS ESTE PUSH

1. GitHub Actions detecta el cambio en `scripts/prompts/**` +
   `.github/workflows/generate-ecuaman.yml`
2. Lanza `Generate Ecuaman Images` en la rama
3. `scripts/generate.py` ve que `00_DAY0_MASTER_HEROIC_VERTICAL_v6_OFFICIAL_LOGO`
   no está en el log → llama a `client.images.edit(...)` pasando
   `Ecuanutrition_Isotipo_Azul.png` como ancla visual
4. Guarda
   `07_ASSETS_OFICIALES/auto_generated/00_DAY0_MASTER_HEROIC_VERTICAL_v6_OFFICIAL_LOGO.png`
5. Commitea y pushea de vuelta a la misma rama

Tras eso, queda lista para validar contra el checklist 24 puntos
(`03_REFERENCIAS/CHECKLIST_VALIDACION.md`). Si pasa, **queda como canon
definitivo de avatar de lanzamiento** y reemplaza al actual `v5_ICONIC`
en perfiles de redes, video de lanzamiento y press kit.

### ⚠️ Si en 10 min no aparece el auto-commit en la rama

Esperé el commit `Auto-generated Ecuaman images [skip ci]` durante 10
minutos y no apareció. Posibles causas (revisar en este orden):

1. **GitHub → Actions** → ¿está deshabilitado a nivel repo? Activarlo.
2. **GitHub → Settings → Secrets and variables → Actions** → confirmar
   que `OPENAI_API_KEY` existe y no expiró.
3. **GitHub → Actions → Generate Ecuaman Images** → revisar la última
   ejecución; si falló, el log muestra la causa exacta (billing, key
   inválida, rate limit).
4. **Disparar manualmente**: Actions → Generate Ecuaman Images →
   Run workflow → branch `claude/continue-ecuaman-sessions-aRTBU`.

El prompt v6 ya está commiteado y listo. Solo falta que el job
de Actions corra una vez con éxito.

Si el resultado no convence, alternativas baratas (1 imagen cada una):
- Cambiar `reference_image` a `Ecuanutrition_Isotipo_blanco.png` (mejor
  contraste sobre fondos azul-marino del escenario submarino)
- Probar con el lockup completo `Ecuanutrition_Logo_ fAzul.png` para
  variantes de banner / firmas

---

## 🚦 ESTADO DEL WORKFLOW DE GENERACIÓN

`/.github/workflows/generate-ecuaman.yml` → **auto-trigger en push
re-activado** (paths: `scripts/prompts/**`, `scripts/generate.py`,
el propio workflow) + `workflow_dispatch` manual disponible.

Razón: la pausa fue para no quemar créditos sin tener el isotipo
oficial. Ya lo tenemos. El log (`scripts/generation_log.json`) actúa
como freno natural: cada `id` ya generado se salta automáticamente, así
que solo se cobra por prompts NUEVOS.

---

## 💬 RESUMEN EN 3 LÍNEAS

> Sesiones 1–4 dejaron el sistema de marca completo y las 38 imágenes
> canónicas en repo. Sesión 5 conecta el isotipo oficial PNG (recién
> subido por el fundador) al pipeline y dispara la generación del
> master v6 brand-true automáticamente al pushear. Coste: ~$0.17.

---

*Sesión 5 — 3 Mayo 2026 · Branch `claude/continue-ecuaman-sessions-aRTBU`*

---

## ✅ DECISIÓN FINAL DEL FUNDADOR — Avatar facturación

Tras iterar 11 versiones, el fundador eligió **v10 ENVELOPE_INVOICE**:

- Sobre navy abierto + factura blanca emergiendo con el logo Ecuanutrition
  impreso en el header navy + título "FACTURA · INVOICE" + filas de items
  en gris claro
- Paleta sin oro: navy `#002D70` / electric blue `#1E88E5` / cyan logo
  `#7AAFD3` / papel ivory `#F8F4ED`
- Estética 3D corporativa premium

**Archivo canónico oficial**:
`07_ASSETS_OFICIALES/EMAIL_PFP_INVOICE_OFICIAL_FINAL.png`

(Copia de `auto_generated/EMAIL_PFP_INVOICE_OFICIAL_v10_ENVELOPE_INVOICE.png`,
elevada a la raíz de `07_ASSETS_OFICIALES/` para fácil acceso.)

**Uso**: subir como foto de perfil de `invoce@ecuanutrition.com` en
Outlook / Gmail / Workspace. Los 64×64 / 128×128 / 256×256 ya existentes
en `03_REFERENCIAS/Ecuanutrition_Outlook_*.png` se mantienen como avatar
genérico de la cuenta corporativa principal.

**Variantes descartadas** (quedan en `auto_generated/` por si vuelves a
necesitarlas o quieres usarlas en contextos distintos): v1 (errata
"FACTURACIOION"), v2 PEN, v3 WAX_SEAL, v4 LEDGER_BOOK, v5 BALANCE_SCALE,
v6 DUO, v7 LAUREL_CREST, v8 EMBOSSED_COIN, v9 CORPORATE_INVOICE, v11
RECEIPT_SCROLL_3D.
