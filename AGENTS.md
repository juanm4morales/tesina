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
- Una figura requiere coordinar el archivo binario en `imagenes/` con su entorno, `caption` y `label` en el capítulo; comprobar ambos lados antes de concluir que fue agregada o retirada.
- Los binarios no versionados (`??`) no aparecen en `git diff`; inspeccionar siempre `git status --short` antes de eliminar una imagen y distinguir entre retirar la referencia LaTeX y borrar el archivo físico.
- Mantener el glosario durante la redacción, incluyendo términos y variables; en `main.tex` debe aparecer después de los índices y antes del cuerpo principal.
- Las entradas nuevas o citadas de `bibliografia.bib` deben ser compatibles con BibTeX clásico e incluir `language = {spanish}`.
- Mantener referencias conocidas: `suttonRL` corresponde a Sutton y Barto, 2da edición, MIT Press, 2018; `marlbook` corresponde a Albrecht, Christianos y Schäfer, MIT Press, 2024.

## Redacción
- Mantener tono académico natural en español; evitar prosa genérica o con apariencia de IA.
- Preferir `este trabajo`, `esta investigación` o `el presente trabajo` antes que `tesis`, salvo pedido explícito.
- En ingeniería de tránsito, limitar la teoría a lo necesario para justificar el modelo computacional de control semafórico.
- Usar terminología consistente: `corriente de tránsito`, `condiciones de operación`, `flujo`, `densidad`, `velocidad media espacial`, `movimientos en conflicto`, `corrientes vehiculares incompatibles`, `puntos de conflicto`.
- En SUMO/RL/MARL, vincular variables de tránsito con observaciones, fases con acciones, y demoras/colas/detenciones con recompensas o evaluación.
- En la primera aparición, escribir el término en español, su equivalente en inglés y la sigla; aplicar el criterio también a paradigmas, POMDP, CTDE y familias algorítmicas.
- Usar `ejecución` o `ejecuciones` para las corridas experimentales y reservar `Ciudad de Mendoza` para el escenario urbano modelado; no sustituirlo por `Gran Mendoza`.
- Toda figura, tabla, algoritmo o ecuación debe introducirse y explicarse en el texto, tener `label` si se referencia y no quedar como un elemento aislado.
- Definir cada símbolo y parámetro de una ecuación antes o inmediatamente después de usarlo; no introducir variables nuevas sin explicar su significado y unidad.
- Presentar las redes neuronales en orden pedagógico (entrada, neurona, capa, activación y red), con una cita específica de aprendizaje profundo o redes neuronales, evitando reutilizar una única fuente para todo.
- Verificar que cada cita sostenga la afirmación exacta y reutilizar una clave bibliográfica canónica cuando dos entradas representan la misma fuente; no mantener duplicados como `suttonRL` y `RL_Definition_Barto`.
- Distinguir garantías teóricas de sus supuestos y de las implementaciones prácticas: una garantía de TRPO no debe atribuirse automáticamente a PPO o HAPPO con recorte.
- Citar afirmaciones técnicas con precisión; evitar pares de citas si una sola fuente sostiene la afirmación.

## Flujo De Trabajo
- Antes de editar, revisar `git status --short`.
- Los artefactos LaTeX están versionados (`*.aux`, `main.pdf`, `main.bbl`, logs, `main.synctex.gz`, etc.); no borrarlos ni hacer limpiezas amplias sin pedido explícito.
- Preferir cambios pequeños y acotados por sección, preservando el estilo existente.
- En `4-marco_teorico.tex` conservar las figuras y la descripción general de herramientas y archivos de SUMO; reservar para `5-metodologia.tex` los valores experimentales, semillas, calentamiento, pasos de decisión, tiempos de fases, calibración y fórmulas aplicadas.
- Después de cambios estructurales, verificar con `latexmk`; una sola pasada de `pdflatex` puede dejar advertencias stale de `hyperref`/TOC.
- Si `main.synctex.gz` queda afectado por una build sin SyncTeX, regenerar con `latexmk -g -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`.
