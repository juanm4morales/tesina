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
- Con la configuración actual, `tracklang` emite `No 'datatool' support for dialect 'spanish'`; es una advertencia externa inocua y puede permanecer si no hay otros avisos de compilación.

## LaTeX
- Reutilizar las definiciones de `main.tex` para paquetes, colores, estilos, algoritmos, `listings`, glosario y macros `\JM`, `\PJV`, `\ACO`.
- Si un título de sección contiene `\gls`, `\acrshort` u otros comandos de formato, proporcionar un título opcional en texto plano para los marcadores PDF; así se evitan advertencias de cadenas PDF de `hyperref`.
- Las imágenes van en `imagenes/` y se referencian con rutas relativas al repositorio.
- Una figura requiere coordinar el archivo binario en `imagenes/` con su entorno, `caption` y `label` en el capítulo; comprobar ambos lados antes de concluir que fue agregada o retirada.
- Los binarios no versionados (`??`) no aparecen en `git diff`; inspeccionar siempre `git status --short` antes de eliminar una imagen y distinguir entre retirar la referencia LaTeX y borrar el archivo físico.
- Mantener el glosario durante la redacción, incluyendo términos y variables; en `main.tex` debe aparecer después de los índices y antes del cuerpo principal.
- Después de modificar `glosario.tex` o `glosario_abreviaturas.tex`, ejecutar `makeglossaries main` antes de la compilación final: `latexmk` puede dejar `main.gls` desactualizado.
- Las entradas nuevas o citadas de `bibliografia.bib` deben ser compatibles con BibTeX clásico e incluir `language = {spanish}`.
- Mantener referencias conocidas: `suttonRL` corresponde a Sutton y Barto, 2da edición, MIT Press, 2018; `marlbook` corresponde a Albrecht, Christianos y Schäfer, MIT Press, 2024.

## Redacción
- Mantener tono académico natural en español; evitar prosa genérica o con apariencia de IA.
- Preferir `este trabajo`, `esta investigación` o `el presente trabajo` antes que `tesis`, salvo pedido explícito.
- En ingeniería de tránsito, limitar la teoría a lo necesario para justificar el modelo computacional de control semafórico.
- Usar terminología consistente: `corriente de tránsito`, `condiciones de operación`, `flujo`, `densidad`, `velocidad media espacial`, `movimientos en conflicto`, `corrientes vehiculares incompatibles`, `puntos de conflicto`.
- En SUMO/RL/MARL, vincular variables de tránsito con observaciones, fases con acciones, y demoras/colas/detenciones con recompensas o evaluación.
- En CTDE, denominar `etapas` al entrenamiento y la ejecución para no confundirlas con fases semafóricas; no presentarlas como `offline/online` salvo que el procedimiento descrito realmente tenga esa propiedad.
- En la primera aparición, escribir el término en español, su equivalente en inglés y la sigla; aplicar el criterio también a paradigmas, POMDP, CTDE y familias algorítmicas.
- Usar `ejecución` o `ejecuciones` para las corridas experimentales y reservar `Ciudad de Mendoza` para el escenario urbano modelado; no sustituirlo por `Gran Mendoza`.
- Toda figura, tabla, algoritmo o ecuación debe introducirse y explicarse en el texto, tener `label` si se referencia y no quedar como un elemento aislado.
- Definir cada símbolo y parámetro de una ecuación antes o inmediatamente después de usarlo; no introducir variables nuevas sin explicar su significado y unidad.
- Presentar las redes neuronales en orden pedagógico (entrada, neurona, capa, activación y red), con una cita específica de aprendizaje profundo o redes neuronales, evitando reutilizar una única fuente para todo.
- Verificar que cada cita sostenga la afirmación exacta y reutilizar una clave bibliográfica canónica cuando dos entradas representan la misma fuente; no mantener duplicados como `suttonRL` y `RL_Definition_Barto`.
- Distinguir garantías teóricas de sus supuestos y de las implementaciones prácticas: una garantía de TRPO no debe atribuirse automáticamente a PPO o HAPPO con recorte.
- Citar afirmaciones técnicas con precisión; evitar pares de citas si una sola fuente sostiene la afirmación.
- No introducir afirmaciones, métodos, arquitecturas ni resultados que no estén explícitamente respaldados por la fuente citada. Antes de redactar un antecedente, comprobar el título, año, autores, DOI y el alcance exacto de lo que el artículo afirma.
- Evitar paráfrasis vagas o más amplias que la evidencia. Por ejemplo, no describir un trabajo como basado en “controladores asistidos por teoría de juegos” si la fuente solo permite afirmar que propone métodos concretos como Nash-A2C y Nash-A3C; nombrar el método y explicar con precisión qué componente incorpora.
- Cuando una interpretación sea una inferencia del análisis propio, marcarla como tal y separarla de los resultados reportados por la fuente. No atribuir a un artículo comparaciones, garantías o componentes de implementación que pertenecen a este trabajo.
- Para bibliografía nueva, priorizar fuentes de 2024--2026 cuando sean pertinentes. Si una fuente de 2022--2023 es fundamental o especialmente relevante, justificar su inclusión por su relación directa con RL, MARL, CTDE, Heterogeneous MARL o Cooperative MARL y por su impacto académico verificable. No agregar referencias solo para aumentar la cantidad.
- Mantener en inglés los términos del marco teórico que no tienen una traducción académica oficial o estable. En particular, usar `epoch` y `minibatch` de forma consistente, definiéndolos en español la primera vez que aparezcan.
- Toda revisión de literatura debe distinguir con claridad el mecanismo del antecedente y el mecanismo de este trabajo: no presentar como equivalentes la coordinación distribuida, la transferencia de información a la pérdida, CTDE, la recompensa compartida, los críticos centralizados o los equilibrios de Nash.

## Flujo De Trabajo
- Antes de editar, revisar `git status --short`.
- En revisiones solicitadas por etapas, explicar al usuario las modificaciones previstas antes de cada paso y solicitar confirmación explícita; no ejecutar el paso siguiente sin esa confirmación.
- Después de incorporar una fuente nueva, verificar que la cita aparezca en el texto, que la entrada BibTeX sea coherente con la publicación real y que la compilación no produzca citas indefinidas ni referencias duplicadas.
- Los artefactos LaTeX están versionados (`*.aux`, `main.pdf`, `main.bbl`, logs, `main.synctex.gz`, etc.); no borrarlos ni hacer limpiezas amplias sin pedido explícito.
- Preferir cambios pequeños y acotados por sección, preservando el estilo existente.
- En `4-marco_teorico.tex` conservar las figuras y la descripción general de herramientas y archivos de SUMO; reservar para `5-metodologia.tex` los valores experimentales, semillas, calentamiento, pasos de decisión, tiempos de fases, calibración y fórmulas aplicadas.
- Después de cambios estructurales, verificar con `latexmk`; una sola pasada de `pdflatex` puede dejar advertencias stale de `hyperref`/TOC.
- Si `main.synctex.gz` queda afectado por una build sin SyncTeX, regenerar con `latexmk -g -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`.
