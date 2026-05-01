# CÓMO SUBIR IMÁGENES Y VIDEOS AL REPOSITORIO
### Guía paso a paso · Repo: `santycolomar85-star/santi`

---

## 📋 ANTES DE SUBIR — REGLAS

### Tamaños recomendados por tipo

| Tipo | Tamaño máximo recomendado | Si excede → |
|---|---|---|
| Imagen PNG/JPG | 5 MB | Comprimir con [TinyPNG](https://tinypng.com) |
| Imagen master alta resolución | 10 MB | Subir, pero usar Git LFS |
| Video corto (<10s) | 25 MB | Subir directo |
| Video largo (>10s) | 100 MB | **Usar Git LFS** o dejar en Drive con link |
| Cualquier archivo > 100 MB | — | **OBLIGATORIO Git LFS** (GitHub bloquea sin él) |

### Estructura de carpetas (respetar siempre)

```
ECUANUTRITION/MARKETING/ECUAMAN/
├── 01_MANUAL/                   ← Solo .md (manual)
├── 02_PROMPTS/                  ← Solo .md (prompts)
├── 03_REFERENCIAS/
│   ├── historicas/              ← Imágenes canónicas
│   ├── campanas_estacionales/   ← Imágenes de campañas puntuales
│   ├── nuevas_propuestas/       ← Borradores nuevos (creas tú)
│   └── videos/                  ← Videos cortos (si son <100MB)
├── 04_USO_REDES/                ← Plantillas de contenido
└── 05_ESTRATEGIA/               ← Documentos estratégicos
```

### Convención de nombres

```
ECUAMAN_<tipo>_<descripcion>_<version>.<ext>

Ejemplos:
ECUAMAN_master_vertical_v3.png
ECUAMAN_sticker_saludo_v1.png
ECUAMAN_video_reel_motivacional_v2.mp4
ECUAMAN_poster_dia_camaron_v1.png
```

❌ Evitar nombres como `IMG_1234.png`, `Untitled.jpg`, `WhatsApp Image...png`

---

## 🚀 OPCIÓN A — Subir desde GitHub Web (LA MÁS FÁCIL)

Ideal si tienes **pocos archivos** (1-10) y son **menores de 25 MB cada uno**.

1. Ve al repo: <https://github.com/santycolomar85-star/santi>
2. Asegúrate de estar en la rama correcta (la que estés trabajando, ej:
   `claude/improve-ecuanutrition-branding-C0oTN` o `main`).
3. Navega hasta la carpeta donde quieres subir:
   `ECUANUTRITION/MARKETING/ECUAMAN/03_REFERENCIAS/historicas/`
4. Clic en **"Add file" → "Upload files"**.
5. Arrastra tus archivos o selecciónalos.
6. Escribe un mensaje de commit, ej: *"Add new Ecuaman master images v3"*.
7. Clic en **"Commit changes"**.

✅ Listo. Los archivos aparecen en el repo en menos de 1 minuto.

---

## 🖥️ OPCIÓN B — Subir desde tu computadora con Git (recomendado para muchos archivos)

### B1. Configura Git (solo la primera vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### B2. Clona el repo (solo la primera vez)
```bash
git clone https://github.com/santycolomar85-star/santi.git
cd santi
```

### B3. Cada vez que quieras subir nuevos archivos:
```bash
# 1. Asegúrate de estar al día
git pull

# 2. Copia tus archivos a la carpeta correcta, por ejemplo:
cp ~/Descargas/mi_nueva_imagen.png ECUANUTRITION/MARKETING/ECUAMAN/03_REFERENCIAS/historicas/ECUAMAN_pose_nueva_v1.png

# 3. Stage los archivos nuevos
git add ECUANUTRITION/MARKETING/ECUAMAN/03_REFERENCIAS/

# 4. Commit con mensaje descriptivo
git commit -m "Add new Ecuaman pose reference (v1)"

# 5. Sube al repositorio
git push
```

---

## 📦 OPCIÓN C — Para archivos grandes (>100 MB) usa Git LFS

Si subes videos largos o imágenes muy pesadas, GitHub te obliga a usar **Git LFS**
(Large File Storage). Sin esto, el push fallará.

### C1. Instala Git LFS (una sola vez)
- Mac: `brew install git-lfs`
- Windows: descarga desde <https://git-lfs.com/>
- Linux: `sudo apt install git-lfs`

### C2. Activa LFS en el repo (una sola vez)
```bash
cd santi
git lfs install
git lfs track "*.mp4"
git lfs track "*.mov"
git lfs track "*.psd"
git lfs track "*.ai"
git lfs track "*.tiff"
git add .gitattributes
git commit -m "Configure Git LFS for media files"
git push
```

### C3. Después subes archivos como siempre — LFS los maneja automático.

> ⚠️ GitHub free incluye **1 GB de LFS y 1 GB/mes de transferencia**. Si pasas
> ese límite, considera dejar los videos pesados en Drive y solo poner el link
> en el repo.

---

## 🌐 OPCIÓN D — Mantener videos pesados en Google Drive (recomendado)

Para **videos > 100 MB**, lo más práctico es:

1. Dejarlos en tu carpeta Drive **ECUAMAN** (ya tienes la estructura).
2. En el repo, crear un archivo `.md` con la lista de videos y sus enlaces:

```markdown
# Videos pesados — Drive

| Nombre | Drive Link |
|---|---|
| Reel motivacional Lunes v1 | https://drive.google.com/file/d/XXXX/view |
| Mini-episodio Origen | https://drive.google.com/file/d/YYYY/view |
```

3. Comparte la carpeta Drive con el equipo (permiso de lector mínimo).

✅ Esto ya está aplicado en `03_REFERENCIAS/CATALOGO_REFERENCIAS.md` para tus
9 videos actuales.

---

## 🤖 OPCIÓN E — Pedirme a mí que los suba (más fácil para ti)

Si me das **enlaces de Google Drive públicos** o me indicas **archivos en tu Drive
ECUAMAN**, puedo:

1. Descargarlos.
2. Renombrarlos con la convención correcta.
3. Subirlos al repo en la carpeta apropiada.
4. Hacer el commit y push.

Solo dime: *"Sube esta imagen al repo en `nuevas_propuestas/` con nombre X"* y
yo lo hago. Para Drive, necesito que el archivo esté en una carpeta que ya
pueda acceder, o que me compartas el enlace.

---

## ✅ CHECKLIST RÁPIDO ANTES DE CADA SUBIDA

- [ ] ¿El archivo respeta el manual de marca? (Manual §1-§7)
- [ ] ¿Pasó el checklist de validación 24 puntos? (`03_REFERENCIAS/CHECKLIST_VALIDACION.md`)
- [ ] ¿Está en la carpeta correcta?
- [ ] ¿Tiene nombre descriptivo según convención?
- [ ] ¿Es < 100 MB? (si no → Git LFS o Drive link)
- [ ] ¿El commit message describe lo que se sube?

---

## 🆘 SI ALGO FALLA

| Error | Solución |
|---|---|
| `error: file is too large` | Activa Git LFS o usa Drive link |
| `Permission denied (publickey)` | Configura SSH o usa HTTPS con token |
| `failed to push some refs` | Haz `git pull` antes de hacer `git push` |
| El push se queda colgado | Tu archivo es enorme. Comprime o usa LFS |
| GitHub muestra "binary file" en lugar de imagen | Es normal para PSD/AI; las PNG/JPG sí se ven |

---

*Para cualquier duda técnica, escríbeme y resuelvo. Lo importante es que el
**activo más valioso** (las imágenes de Ecuaman) esté **respaldado y versionado**.*
