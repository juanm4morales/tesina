# Comparación de la organización de las metodologías

## Documentos y alcance

Se comparó la metodología publicada de la tesina en `fc1669f` (`/tmp/tesina-continuidad-20261015/5-metodologia.tex`) con `/home/juanm4/Documentos/Tesina_LCC_Maglione.pdf`. Este PDF contiene únicamente las 30 páginas de la metodología de Maglione: la primera página física es la impresa 37 y la última es la 66. Las páginas indicadas a continuación son las impresas.

La revisión se concentra en la jerarquía de títulos, la continuidad del procedimiento y la función de los párrafos. No evalúa la validez de los experimentos de Maglione ni vuelve a auditar el código de la tesina. Se consultaron los principios de organización, claridad y unidad temática de `scientific-writing`, y se inspeccionaron visualmente los ejemplos breves de ambas metodologías.

## Dictamen

La metodología de la tesina presenta una fragmentación evitable en algunos puntos. La subsección «Seguimiento diagnóstico del entrenamiento» es el caso más claro: unas 70 palabras reciben un apartado numerado propio entre la función objetivo y la fase 1. El contenido permite entender el entrenamiento, pero puede leerse como parte de sus condiciones generales. También conviene simplificar el único subapartado de «Agentes y algoritmos de aprendizaje»: la actualización de actores y crítico continúa la explicación de esos agentes.

Un título con un solo párrafo no es, por sí mismo, una deficiencia. Importa si delimita un procedimiento con entidad propia, si facilita su consulta y si su posición ayuda al lector. También se deben distinguir los apartados completos de un párrafo de las aperturas breves que introducen varias subsecciones. Añadir texto o cortar un párrafo para alcanzar una longitud mínima no corrige una jerarquía innecesaria.

Los títulos de `ecf6182` y `fc1669f` son idénticos. El pase editorial anterior separó párrafos y corrigió expresiones, pero conservó una jerarquía que requería esta revisión adicional. La conservación del contenido científico y una compilación correcta no acreditaban por sí solas que toda la organización fuera adecuada.

## Lo que muestra Maglione

En las páginas 37–39, Maglione define la tarea y luego presenta el flujo del proyecto. La definición identifica la entrada, la predicción buscada y la salida de la aplicación; la sección de flujo conecta la recolección, la preparación, el entrenamiento, la evaluación y la aplicación. El diagrama sirve para orientar el desarrollo posterior. La tesina ya dispone de una apertura y de un diagrama que cumplen una función comparable; no hace falta repetirlos al abrir cada etapa.

La preparación del conjunto de datos, en las páginas 38–51, se desarrolla como una etapa extensa: fuentes, exploración, preprocesamiento y resultado preparado para los modelos. Los temas secundarios de ese procedimiento se presentan también con encabezados menores. Lo aprovechable es que el lector puede reconocer qué se recibe y qué se obtiene antes de pasar a las arquitecturas.

En la página 51, «Arquitectura de los modelos» tiene una introducción de una sola oración antes de RiskViT y CNN-LSTM. Esa sección no termina en esa oración: contiene ambos desarrollos. Es un caso comparable a las aperturas de «Escenarios de simulación», «Observación, acciones y recompensas» o «Métricas de desempeño y vehículos evaluados» de la tesina. Sus introducciones breves no justifican eliminar esos títulos.

Las arquitecturas se describen mediante sus entradas, transformaciones y salidas, acompañadas por figuras (páginas 51–54). La configuración de hiperparámetros se resume mediante tablas y se conecta con la búsqueda (páginas 56–58). En la tesina, los apartados de escenarios, entorno, observaciones, acciones y recompensas siguen una dependencia semejante. La existencia de dos líneas experimentales y varias señales de recompensa exige más distinciones; copiar la extensión de Maglione no resolvería esas diferencias.

Maglione también contiene apartados completos de un párrafo. En la página 58, «Early Stopping» describe la condición de detención y «Optimizador» identifica Adam. En la página 66, «Entrenamiento automático» ocupa un solo párrafo. La estrategia de búsqueda, en las páginas 57–58, también se desarrolla en un párrafo. Estos ejemplos impiden sostener que una tesina de grado deba prohibir los apartados de un párrafo. Para esta revisión resulta más útil valorar cuánto aporta cada título a la lectura.

## Revisión de los casos de la tesina

| Pasaje | Evaluación | Propuesta concreta |
|---|---|---|
| Seguimiento diagnóstico del entrenamiento, actual 3.4.3 | Es un apartado completo de un párrafo; interrumpe la entrada a las dos fases para describir una condición transversal. | Integrar su párrafo en las condiciones generales de simulación y entrenamiento, antes de la función objetivo. Conservar cómo se eligen acciones y la distinción entre diagnóstico y evaluación independiente. |
| Actualización de los actores y del crítico | Es el único subapartado dentro de «Agentes y algoritmos»; continúa el mismo tema. | Integrar sus párrafos directamente en «Agentes y algoritmos de aprendizaje», con sus remisiones y limitaciones. |
| Aperturas de Escenarios, Observación/acciones/recompensas, Selección y Métricas | Introducen varios desarrollos posteriores. El contenido del apartado incluye esos desarrollos. | Conservar esos títulos y sus aperturas breves. |
| Construcción de la demanda | Incluye definiciones, dos ecuaciones, unidades y supuestos. Contar los párrafos sin los elementos matemáticos subestima su contenido. | Conservar el apartado, que desarrolla una operación identificable. |
| Métricas locales | Incluye definiciones, una lista con dos medidas y una ecuación. No es una sección de un único párrafo sin desarrollo. | Conservar la separación respecto de las métricas de viaje. |
| Evaluación de variantes de MAPPO | Es breve, pero especifica un procedimiento de evaluación distinto del entrenamiento y de los modelos finales. | Conservar el apartado; su función metodológica justifica la separación. |
| Entrenamiento y evaluación de modelos finales | Reúne once párrafos, varios muy breves. La cantidad de cortes no equivale a mayor claridad. | Como revisión posterior, considerar reunir la regla de iteraciones/checkpoint con la receta de entrenamiento. Mantener el corte entre las ventanas urbanas de dos y doce horas. |

## Organización propuesta

En el bloque de agentes, «Agentes y algoritmos de aprendizaje» contendría tanto la organización de los módulos y el crítico como sus actualizaciones. Se retiraría únicamente el subtítulo «Actualización de los actores y del crítico».

En el bloque de búsqueda, la primera subsección podría titularse «Condiciones de simulación y entrenamiento» e incluir horizontes, decisiones, semillas y seguimiento diagnóstico. Le seguirían «Función objetivo de la búsqueda», «Fase 1: búsqueda amplia», «Fase 2: búsqueda con dominios reducidos» y «Criterios de selección de configuraciones». Se retiraría el título independiente del seguimiento. La referencia que actualmente remite a ese apartado debe apuntar al bloque que lo incorpora.

Estas dos intervenciones reducen los niveles de títulos y reúnen contenidos que el lector necesita comprender juntos. No requieren añadir explicaciones para rellenar apartados. Las etiquetas existentes deben conservarse como destinos coherentes o actualizarse junto con sus remisiones al implementar la propuesta.

## Estado de esta revisión

Este informe y la propuesta de organización son el resultado de la comparación solicitada. No se modificaron las fuentes LaTeX, el PDF publicado ni Git. La propuesta debe distinguirse de los cambios ya publicados en `78342b5` y `fc1669f`.

## Aplicación posterior de la propuesta

Tras la autorización del usuario, se aplicaron los dos ajustes sobre `fc1669f`: el párrafo de seguimiento se incorporó a «Condiciones de simulación y entrenamiento» y se retiró el subtítulo de actualización de actores y crítico. Las etiquetas de ambos contenidos se conservaron como destinos de los apartados que los incorporan. Los párrafos y las ecuaciones se conservaron literalmente; no se añadieron frases de enlace ni explicaciones.

La revisión visual detectó una línea aislada al comenzar una página. Se reservó espacio antes de «Función objetivo de la búsqueda» con la macro existente `\Needspace`, para mantener el título y su primer párrafo juntos. Se inspeccionaron las páginas físicas 101–107 y la página 6 del índice. El PDF conserva 161 páginas.

La compilación con `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` terminó correctamente. El log solo contiene la advertencia conocida de `tracklang`: no hay desbordes, citas o referencias indefinidas ni etiquetas duplicadas. Se comprobaron los destinos y las anotaciones GoTo de las referencias afectadas; `qpdf --check` y `git diff --check` no informaron errores.

Se publicaron mediante push normal a `main` los commits `cf3d947` (fuente) y `9b12dbc` (PDF). Solo cambiaron `5-metodologia.tex` y `main.pdf`. El PDF publicado, el diff y los archivos de comprobación se guardaron en `respaldo-estructura-20261015/`, junto con la versión anterior. El checkout original en `8d1642a` permanece preservado.
