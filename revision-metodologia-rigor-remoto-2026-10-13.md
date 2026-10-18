# Correcciones de rigor sobre la revisión remota

Fecha: 13 de octubre de 2026.

La base científica revisada es `a534b6dedfa70eeccf99ea34165346ba8011b4c1`. La copia local partía de `464b9121a657e1ab0c2f47e5d1b4f11bbd455e13`. Se incorporaron los dos capítulos de la versión remota y se aplicaron correcciones locales sobre ellos. Se conservaron los documentos de auditoría y las instrucciones locales; no se trasladó la eliminación remota de archivos Markdown ni se modificó el historial de Git.

## Cambios y justificación

| Antes, en la versión remota | Ahora | Justificación |
|---|---|---|
| El criterio A/C exigía el campo nativo `teleports`. | Se exige el conteo de inicios `teleport_starts`, comparado en cada evaluación con la misma semilla dentro de un par. Se explica que cuenta eventos y que no cuenta vehículos distintos. | El analizador y los registros de A/C utilizan ese campo; cambiar su fuente altera el procedimiento descrito. |
| Las cajas del flujo reducían las flechas finales a un espacio casi nulo y heredaban el interlineado del capítulo. | Se aplica interlineado sencillo y se amplían las separaciones. La figura utiliza una única fuente incluida desde `imagenes/metodologia_v2_flujo.tex`. | La inspección del PDF confirma flechas visibles y cajas separadas. Se conserva la estructura remota de dependencias. |
| La apertura introducía las letras A y C y el diseño hablaba del avance de las campañas. | La apertura describe genéricamente la segunda línea. Las condiciones de admisibilidad y de resumen estadístico se expresan como reglas del procedimiento. | Respeta la progresión narrativa y mantiene las condiciones científicas sin incorporar comentarios de avance. |
| La remisión afirmaba que las semillas 950001, 950003 y 950007 figuraban en la tabla. | Remite al apartado de admisibilidad y selección. | La tabla contiene las series 910…, 920… y 930…; el selector contiene las semillas 950…. |
| HAML aparecía solo en metodología y apéndice, sin entrada en el glosario. | Se incorpora al glosario y se coordina su alcance con los párrafos y la tabla del marco teórico. | El artículo de Zhong et al. sitúa HAPPO dentro de HAML; sus garantías dependen de las condiciones del marco, entre ellas el retorno compartido. |
| La explicación de Summary y de los conteos urbanos interrumpía el análisis pareado A/C. | Se sitúa en la procedencia de Mendoza y se corrige la remisión desde las métricas. | La cautela permanece junto al escenario cuyos registros interpreta. |
| La evaluación final reconstruía el entorno sin hacer explícita la verificación de la semilla efectiva. | Se comprueba que SUMO utilice la semilla registrada y se explicita que los parámetros de las políticas permanecen fijos. | Precisa el procedimiento de evaluación sin añadir una implementación experimental. |

La reformulación de la búsqueda de Mendoza conserva la necesidad de definir dominios, presupuestos y semillas propios. No se añadieron cifras urbanas por analogía con las redes sintéticas.

## Evidencia revisada

- `marl-tlc/src/marlTLC/environments/sumo_env.py`: `_collect_teleports` acumula los inicios y finales por separado mediante TraCI.
- `marl-tlc/scripts/analyze_cooperation_multiscenario.py`: obtiene `teleport_starts` y aplica la comparación por evaluación del par.
- `marl-tlc/cooperation_multiscenario_20260920/report/evaluations.csv`: registros definitivos de A/C con los contadores de inicio y fin.
- [Documentación de TraCI](https://sumo.dlr.de/docs/TraCI/Simulation_Value_Retrieval.html): define los eventos de inicio y fin por paso.
- [Zhong et al., JMLR 2024](https://www.jmlr.org/papers/volume25/23-0488/23-0488.pdf): teorema 14 y apéndice F para el alcance de HAML y su relación con HAPPO.

## Verificación

Se compararon las etiquetas, las citas y las ecuaciones de los dos capítulos con la base remota: permanecen iguales. Se conservan las cifras, las semillas y los márgenes de los procedimientos. La evaluación final mantiene veinte simulaciones por combinación, media con igual peso por simulación, desviación estándar muestral y separación entre variación de simulaciones y de entrenamientos.

Se regeneró el glosario con `pdflatex -synctex=1`, `makeglossaries main` y `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`. Se revisaron las páginas afectadas, especialmente el flujo, el criterio de teletransportes, la evaluación final, la procedencia urbana y la remisión de semillas. Se comprobó el destino PDF de HAML. Los identificadores técnicos se ajustaron para evitar desbordamientos. El PDF actualizado se conserva en `main.pdf`.

La compilación final genera 159 páginas y el log conserva únicamente la advertencia conocida de `tracklang`: sin desbordamientos ni citas o referencias indefinidas. El PDF contiene seis acciones GoTo hacia el destino de HAML. `git diff --check` no informa incidencias.
