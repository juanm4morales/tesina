# AGENTS.md

## Proyecto
- Repositorio de tesina en LaTeX en español. El punto de entrada es `main.tex`.
- Los capítulos son archivos `*.tex` en la raíz e incluidos desde `main.tex`.
- `4-marco_teorico_2.tex` y `original_marco_teorico.tex` son borradores/snapshots fuera del build; no editarlos salvo pedido explícito.
- No editar `.agents/skills/` salvo que la tarea sea sobre skills.

## Build
- Compilar desde la raíz con `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- La cadena esperada es `pdflatex` + `bibtex main`; no migrar a `biber`/`biblatex` sin cambiar las fuentes.
- La bibliografía usa `babelbib`/`babalpha`: `\bibliographystyle{babalpha}` y `\bibliography{bibliografia}`.
- Para depurar bibliografía: `pdflatex main.tex`, `bibtex main`, `pdflatex main.tex`, `pdflatex main.tex`.

## LaTeX
- Reutilizar las definiciones de `main.tex` para paquetes, colores, estilos, algoritmos, `listings`, glosario y macros `\JM`, `\PJV`, `\ACO`.
- Las imágenes van en `imagenes/` y se referencian con rutas relativas al repositorio.
- Las entradas nuevas o citadas de `bibliografia.bib` deben ser compatibles con BibTeX clásico e incluir `language = {spanish}`.
- Mantener referencias conocidas: `suttonRL` corresponde a Sutton y Barto, 2da edición, MIT Press, 2018; `marlbook` corresponde a Albrecht, Christianos y Schäfer, MIT Press, 2024.

## Redacción
- Mantener tono académico natural en español; evitar prosa genérica o con apariencia de IA.
- Preferir `este trabajo`, `esta investigación` o `el presente trabajo` antes que `tesis`, salvo pedido explícito.
- En ingeniería de tránsito, limitar la teoría a lo necesario para justificar el modelo computacional de control semafórico.
- Usar terminología consistente: `corriente de tránsito`, `condiciones de operación`, `flujo`, `densidad`, `velocidad media espacial`, `movimientos en conflicto`, `corrientes vehiculares incompatibles`, `puntos de conflicto`.
- En SUMO/RL/MARL, vincular variables de tránsito con observaciones, fases con acciones, y demoras/colas/detenciones con recompensas o evaluación.
- Citar afirmaciones técnicas con precisión; evitar pares de citas si una sola fuente sostiene la afirmación.

## Flujo De Trabajo
- Antes de editar, revisar `git status --short`.
- Los artefactos LaTeX están versionados (`*.aux`, `main.pdf`, `main.bbl`, logs, `main.synctex.gz`, etc.); no borrarlos ni hacer limpiezas amplias sin pedido explícito.
- Preferir cambios pequeños y acotados por sección, preservando el estilo existente.
- Después de cambios estructurales, verificar con `latexmk`; una sola pasada de `pdflatex` puede dejar advertencias stale de `hyperref`/TOC.
- Si `main.synctex.gz` queda afectado por una build sin SyncTeX, regenerar con `latexmk -g -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`.
