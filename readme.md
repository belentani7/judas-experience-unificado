# THE JUDAS EXPERIENCE // UNIFICADO

Artefacto rojo que **unifica** las piezas dispersas del universo Belentani / Judas en una sola
experiencia web inmersiva. Donde el código divergía, **prevalece el más sofisticado**; donde el
lore divergía, **se compila en uno solo**.

## Qué se ha unificado

| Fuente | Aporte | Estado |
|---|---|---|
| `OMEGA_LIVING_UNIVERSE_MAX_1.html` | **Motor Three.js** (elegido como base por ser el más sofisticado): planeta vivo procedural, **llave dorada PBR** y **diamante físico** (IOR 2.417), máquina orgánica, bloom, postproducción cinematográfica, audio procedural, telemetría. | **Prevalece** |
| `06_planeta_rojo.html` | Reliquias `KEY` / `DIAMOND` / `PLANET` en Three.js. | Integrado (motivos) |
| `belentani-lore-web/*` | Los **6 nodos** (Portal → Belentani → Artista → Neon Glass → Judas → Omega) y la cronología del lore. | Integrado |
| `Belentani/frontend` (React `Judas.tsx`) | El "The Judas Experience" original: capítulos **Betrayal / Trial / Revelation / Redemption**. | Integrado (mapeado a las gemas) |
| `belentani-judas-experience-os-unificado.html` | Paleta neón rojo `#ff073a`, anillo/HUD, "Crónica de la Llave Dorada". | Integrado |
| Antigua web **buildai.space** (`judas-experience-13898`) | Concepto "Era Judas": Inicio, Música, Era Judas, Herramientas AI, Sobre, Contacto/Fan Zone. | Archivado como nodo |
| `BELENTANI-JUDAS-BUILDAI-ANALYSIS.md` | Protocolo de los **5 Elementos**, nodo `JUDAS-CORE-07`, 432 Hz, Oráculo/Agente, 4 estados. | Integrado |


## Sesiones del artista

La experiencia canónica expone nueve sesiones desde el botón SESSIONS de la barra superior: **Home**, **The Artist**, **Music**, **Judas**, **The Experience**, **AI Lab**, **Art Gallery**, **Contact** y **Music Studio**. El hub vive en core/session-hub.js y mantiene la escena Three.js como núcleo visual.

## Estructura

```
judas-experience-unificado/
├── index.html      # Experiencia unificada (motor 3D + Códice de lore)
├── assets/
│   ├── judas-key-art-planeta-diamante.png   # key art: planeta + llave dorada + diamante
│   └── lore-portal-preview.png              # preview del portal de lore
├── README.md
└── LORE_UNIFICADO.md
```

## Cómo abrirlo

- **Doble clic** en `index.html` (o `Abrir.bat`). Necesita **conexión a internet** la primera vez:
  el motor carga Three.js desde CDN (`cdn.jsdelivr.net`). El Códice y la maquetación funcionan igual.
- Si el 3D no arranca, aparece un aviso; abre con un servidor local:
  ```powershell
  cd <carpeta>
  python -m http.server 8080     # luego abre http://localhost:8080
  ```
- Controles: **clic** en planeta / llave / diamante / máquina para enfocar la cámara; rueda del
  dock inferior para cambiar de objetivo; botón **LORE** (arriba o en el dock) abre el Códice.

## Qué cubre

- **Motor 3D**: planeta vivo (superficie procedural + pulso bioeléctrico), máquina orgánica
  (anillos + iris + placas instanciadas), llave dorada PBR, diamante con transmisión/dispersión,
  nebulosa procedural, campo de estrellas GPU, bloom y *color grading* con aberración + grano.
- **Lore unificado**: 6 eras/nodos, las 4 gemas, los 5 Elementos, reliquias, Oráculo/Agente,
  4 estados del sistema, registro del viaje y arca sonora.
- **UI**: HUD de telemetría (GPU / BIO PULSE / FPS reales), panel lateral, dock, etiquetas 3D→HTML.
- **Robustez**: *fallback* CSS si no hay WebGL, mensaje de error controlado, `prefers-reduced-motion`,
  modo de calidad (AUTO / ECO / ULTRA), pantalla completa, audio opcional tras gesto.

## Cómo editarlo

- **Textos del lore** → bloque `<section id="codex">` en `index.html`.
- **Colores** → variables CSS en `:root` (`--red: #ff003c`, `--gold`, `--void-*`).
- **Planeta / llave / diamante** → shaders y geometrías en el `<script type="module">`
  (`planetMaterial`, `keyMesh`, `createBrilliantGeometry`).
- **Objetos y focos de cámara** → `focusPresets` y los botones `data-focus`.
- **Puntos de anclaje del lore** → `titles` dentro de `setFocus()`.

## Verificación

- Estructura comprobada: HTML bien formado (secciones y `<script>` balanceados), 95 KB.
- La maquetación y el Códice funcionan sin red; el 3D requiere CDN de Three.js.
- No verificado en navegador headless en este entorno: si el 3D no aparece, revisa conexión y
  aceleración por hardware (o usa el servidor local indicado).
