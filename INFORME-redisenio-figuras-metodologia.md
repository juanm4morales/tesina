# Rediseño de figuras de metodología

> Informe histórico de la entrega v05, observada por el usuario. Sus verificaciones no fueron suficientes para acreditar la calidad visual. La revisión vigente y sus criterios están en [REVISION-figuras-metodologia-criterio-y-verificacion.md](REVISION-figuras-metodologia-criterio-y-verificacion.md). Las decisiones de abajo describen la versión anterior.

## Alcance y estado inicial

Se implementó el plan de rediseño integral sobre el árbol de trabajo existente. Al comenzar ya había cambios en `5-metodologia.tex`, `PLAN-revision-metodologia-caro.md`, `bibliografia.bib`, cinco fuentes/generadores de figuras, los dos PDF del codificador y `main.pdf`. Se conservaron como base. No se editaron los borradores excluidos del build ni se eliminaron capturas.

El capítulo conserva doce figuras principales. Las fuentes están en `imagenes/`; las vistas aisladas, PDF y hojas de contacto se conservan en `imagenes/revision-metodologia/`. Las revisiones v01 y v02 documentan las primeras inspecciones; v05 corresponde al diseño revisado.

## Hoja de decisiones y aceptación

| Fuente / etiqueta | Decisión y función | Ubicación | Criterio de aceptación |
|---|---|---|---|
| `metodologia_v2_flujo.tex` / `fig:flujo_metodologico_general` | Sustituir: dos recorridos, cuatro algoritmos y variantes MAPPO | Diseño experimental | Distingue protocolo y ejecución urbana; dependencia discontinua sin cronología implícita |
| `metodologia_redes_sinteticas.tex` / `fig:topologias_sinteticas` | Consolidar tres capturas en paneles vectoriales | Redes sintéticas | XML, sentidos, carriles y agentes coherentes; enlaces ausentes sin líneas ficticias |
| `metodologia_construccion_urbana.tex` / `fig:construccion_urbana` | Incorporar: cartografía y conteos convergen en simulación | Inicio de Mendoza | Diferencia datos y decisiones; comprobación con programas de referencia |
| `metodologia_red_mendoza.tex` / `fig:dominio_mendoza` | Conservar cartografía y anotar calles, acceso e inserto | Red de Mendoza | Norte, escala del mapa principal, TAZ 28 y cámara exterior sin posición inventada |
| `metodologia_v2_integracion.tex` / `fig:integracion_marl_tlc` | Sustituir: interacción, aprendizaje y persistencia | Sistema de control | Estado guardado/cargado separado de escritura de viajes |
| `metodologia_observaciones.tex` y `metodologia_v2_encoder.pdf` / `fig:codificacion_carriles` | Conservar curva y añadir ejemplos calculados | Observación | Fase sin transformar; niveles reproducibles; máximo distinto del límite de escala |
| `metodologia_controladores.tex` / `fig:informacion_controladores` | Simplificar estructura compartida y detallar secuencia HAPPO | Algoritmos | Entrenamiento centralizado separado de ejecución; factores para pendientes, orden fijo |
| `metodologia_cambio_mascara.tex` / `fig:cambio_mascara` | Incorporar: amarillo y verde sobre rejilla de decisiones | Ciclo episódico | Proporciones 0–4–5–9–10; mínimo de verde y comprobación discretizada distintos |
| `metodologia_v2_protocolo.tex` / `fig:protocolo_informado_v2` | Sustituir cajas de parámetros por productos del refinamiento | Búsqueda refinada | Diez mejores para dominios, cinco para inicio; Mendoza separado |
| `metodologia_contraste_ac.tex` / `fig:contraste_ac` | Incorporar comparación local/vecinal | Variantes MAPPO | Cambian observación, recompensa y entrada; sin atribución aislada |
| `metodologia_cohorte.tex` / `fig:cohorte_evaluacion` | Incorporar: cuatro trayectorias y cohorte | Métricas globales | Inserción efectiva determina pertenencia; inconclusos incluidos; `departDelay` separado |
| `metodologia_analisis_pareado.tex` / `fig:analisis_pareado` | Sustituir: ramas y cinco evaluaciones alineadas | Análisis por pares | Unidad independiente: par entrenado; remuestreo de pares completos por red |
| `metodologia_tiempos_semaforicos.tex` / `fig:tiempos_semaforicos_base` | Trasladar y conservar | Vistas documentales del apéndice | Tabla permanece en el cuerpo; remisión actualizada |
| Captura TAZ / `fig:mendoza_taz` | Trasladar y conservar | Vistas documentales del apéndice | Explica tramos y recuadros, sin atribuir límites territoriales |

Las etiquetas de los dos paneles sintéticos retirados se sustituyeron por remisiones a la figura consolidada. Las demás etiquetas mantienen su función. Se aplicaron R01–R26, especialmente R08–R12, R17 y R24: alcance documental, explicación próxima, epígrafes breves y revisión del PDF. Este informe registra el bloque de figuras; no declara cerradas observaciones ajenas de `TODO-comentarios-caro.md` ni actualiza retrospectivamente la auditoría fechada.

## Reproducción

Desde la raíz:

```bash
python3 imagenes/metodologia_generar_redes.py --proyecto /ruta/al/repositorio/experimental
python3 imagenes/metodologia_v2_generar_encoder.py
python3 imagenes/metodologia_verificar_figuras.py --skill /ruta/a/tikz-diagrams --version v05
pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
bibtex main
makeglossaries main
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

El verificador requiere Pillow únicamente para las hojas de contacto; trabaja en un directorio temporal externo. Los PDF del codificador también tienen sus fuentes standalone generadas. Las redes registran hashes SHA-256 en `imagenes/metodologia_redes_procedencia.json`. El repositorio experimental se utilizó en lectura.

## Comprobaciones numéricas y de significado

- Agentes/tramos/carriles externos, contrastados automáticamente con XML: 3/20/40, 9/48/96 y 16/71/166. Las flechas siguen el orden de puntos de cada carril; los grosores discretos dependen de la cantidad de carriles del tramo dirigido.
- TAZ 28 contrastada con el XML de zonas: tramo `93904440#0`, denominado José Vicente Zapata en la red. El inserto amplía la captura conservada. Los rótulos identifican corredores, no límites catastrales; la escala corresponde al mapa principal.
- Codificador: comparación con `cooperation_multiscenario_20260920/frozen_v5/src/marlTLC/utils/encoder.py`, 1.265 puntos incluidos umbrales, sin discrepancias. Ejemplos: 0 → 0; 120 → 10; 600 → 18. Nivel 21 para valores superiores a aproximadamente 943,742516 veh·s; límite de escala 1.136 veh·s. La función numérica se conserva.
- Máscara: amarillo [0,4), un segundo de verde en t=5, cinco segundos en t=9 y seis en t=10. La siguiente comprobación admisible se sitúa en t=10.
- A/C: modificaciones conjuntas y aumento de entradas explícitos. La figura no generaliza la normalización de C a fase 1.
- Cohorte: ventana semiabierta; viajes inconclusos incluidos con observación parcial. No se equipara la espera de memoria finita por carril con `TripInfo.waitingTime`.
- Pares: cinco simulaciones por política, 24 pares por red y 20.000 remuestreos; intervalos percentiles 95 % y 98,33 %. Las redes se analizan por separado.

## Verificación visual y compilación

Se ejecutó el control estático de TikZ sobre las doce fuentes principales y se compilaron aisladas con pdflatex y el script de la skill. Se generaron PNG a 150 dpi, versiones en gris y hojas de contacto. Las primeras inspecciones motivaron correcciones de títulos, llamadas, flechas, rótulos y detalle de actualización HAPPO. Se revisó además la composición en las páginas del capítulo compilado.

El control automático de colisiones de la skill requiere PyMuPDF, ausente en el entorno. No se instalaron dependencias: se usaron Poppler, ImageMagick y revisión visual de los renders como comprobación alternativa. Esa limitación no se presenta como una prueba automática aprobada.

Resultado final: doce figuras principales, catorce fuentes TikZ comprobadas (incluidas las dos curvas generadas), compilación completa con BibTeX y glosario, sin referencias/citas indefinidas ni desbordes horizontales o verticales. Permanece únicamente la advertencia externa conocida de `tracklang` sobre `spanish`. `git diff --check` no informa errores. El PDF completo tiene 166 páginas y conserva SyncTeX.

SHA-256 del PDF entregado: `2b1fccfbaac5669196fde84ae6f6a7dd1c396efa8db6d754c331eff00c734979`.
