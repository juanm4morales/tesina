# Revisión integral de metodología y de los cambios acumulados

Fecha: 17 de octubre de 2026. Capítulo revisado: `5-metodologia.tex`, completo. Base de comparación: `HEAD` y una copia del estado del trabajo tomada antes de esta segunda revisión. Se revisaron también el diff de los cambios asociados en marco teórico, apéndice, bibliografía, generadores y tabla de dominios, y su representación en el PDF.

## Criterio y resultado

Se releyeron `AGENTS.md`, las reglas R01–R26 y el inventario de las 287 anotaciones C001–C287, incluidos los 180 comentarios escritos por Caro. Las 107 marcas sin comentario se trataron como indicios que requieren contexto, no como instrucciones textuales adicionales. Se consultaron los destinos de las remisiones pertinentes y el código conservado cuando la precisión del pasaje lo exigía.

Los cambios acumulados mejoran principalmente el orden de exposición, la proximidad de las explicaciones a las figuras y la distinción entre diseño, implementación y ejecuciones documentadas. Se conservan. No se considera que todas las reformulaciones sean correcciones obligatorias de Caro: por ejemplo, «El diseño compara» es una elección editorial aceptada, no la única forma académicamente válida de presentar la comparación.

Esta lectura detectó tres precisiones adicionales de prosa y terminología y una mejora opcional de interpretación gráfica. Se explicaron antes de aplicarlas, bajo la autorización general del usuario, y se registraron como fichas 25–28. No fue necesario modificar ecuaciones, datos, presupuestos, semillas, figuras, epígrafes ni restricciones metodológicas.

## Evaluación de los cambios anteriores

| Bloque examinado | Evaluación y resolución |
| --- | --- |
| Apertura y dos líneas de trabajo | Conservar. Presenta el problema de control, distingue la comparación de cuatro algoritmos del contraste A/C y permite reconocer el carácter de diseño del primer procedimiento. No se infiere ausencia de ejecuciones a partir de resultados todavía no redactados. |
| Referencias y vocabulario | Conservar las mayúsculas singulares y «Sección» para destinos internos del apéndice. Se preservan las etiquetas; las menciones plurales y genéricas se distinguen de las remisiones singulares. «Ejecución» no sustituye literales de código ni identificadores. |
| Flujo experimental | Conservar el traslado de la explicación al cuerpo. La figura distingue las ramas del diseño; la prosa precisa el alcance sintético de A–E/A/C y advierte que las flechas no fijan toda la cronología de campañas. No se convierte un esquema de dependencias en prueba de ejecuciones. |
| Programas semafóricos | Conservar las convenciones V, A y R y la particularidad de C4. Las secuencias tabuladas suman 90 segundos y coinciden con las barras. Las duraciones de referencia y las del control aprendido están diferenciadas. |
| Topologías sintéticas | Conservar los tres traslados. Cada descripción queda próxima a la figura correspondiente. La explicación de 3×3 al final de la página impresa 63 y su figura en la 64 mantienen la continuidad, sin otro desarrollo interpuesto. |
| Mendoza y zonas de tránsito | Conservar las convenciones de tramos celestes y recuadros, la diferencia entre programas de referencia y políticas aprendidas y las limitaciones de procedencia. La aclaración de redondeo temporal sí necesitaba la precisión de la ficha 25. |
| Integración SUMO–entorno–aprendizaje | Conservar la explicación funcional del cuerpo y el epígrafe identificatorio. El almacenamiento del estado se distingue del intercambio de datos de aprendizaje. La cita de PyTorch respalda la herramienta descrita. |
| Señal de espera y codificación | Conservar el orden fuente → atribución por carril → limitaciones → codificador → observaciones. Las dimensiones y la función e(x) se explican antes de aplicarlas. El ejemplo con I=22 sigue separado de A/C con I=17. |
| Glosario | Conservar los enlaces visibles de m_i, K_i, época y distribuciones. Se comprobaron anotaciones y destinos del PDF, además de la forma visible; no se interpreta glsadd como sustituto de un enlace. |
| Controladores y HAPPO | Conservar la distinción teoría/adaptación y las operaciones comprobadas. Se precisaron el módulo asociado al agente y el sujeto que calcula la razón de probabilidades, y se explicó la convención de las flechas de la Figura 3.10. |
| Búsqueda, selección y evaluación final | Conservar las definiciones de distribuciones, las remisiones a dominios y los sujetos que atribuyen condiciones a protocolos. Las reglas comunes de refinamiento están efectivamente declaradas en el destino; no se las juzga por un informe histórico anterior. |
| Métricas e incidencias | Conservar la cohorte de insertados, los viajes inconclusos, los denominadores nulos y la separación entre espera por viaje y señal local de memoria finita. El apartado de incidencias evita presentar un contador transversal como si fuera una medida de equidad espacial. |
| Análisis por pares | Conservar la unidad de 24 pares por red, las cinco evaluaciones promediadas, la identificación de percentiles y t, el alcance de Bonferroni y las limitaciones sobre cobertura e inserciones. La explicación del diagrama precede al objeto. |
| Miles y generadores | Conservar la convención de punto de miles y coma decimal. La comparación del texto extraído del codificador solo difiere en el agrupador; sus funciones de cálculo son idénticas a HEAD. Los cambios de dominios son tipográficos, no modificaciones de sus alternativas. |
| Ampliaciones en marco teórico y bibliografía | Conservar la distinción local del orden del crítico y la corrección de Fanglei Sun. Las dos entradas bibliográficas modificadas se contrastaron nuevamente con fuentes primarias, con la precisión sobre Köpf indicada más abajo. |

## Correcciones adicionales aplicadas

| Ficha | Pasaje y diagnóstico | Cambio y fundamento |
| --- | --- | --- |
| 25 | «Los conteos se depuraron y redondearon al intervalo de 15 minutos…» confundía la magnitud contada con el tiempo. | Se distinguen registros depurados, marcas temporales redondeadas y conteos agregados. R06/R18, por extensión de las observaciones sobre referentes y magnitudes. El apéndice confirma explícitamente que se redondearon los tiempos. |
| 26 | «RLlib vincula un módulo de aprendizaje con cada agente» no distinguía el módulo de política/valores del aprendiz que coordina las actualizaciones. | «RLlib asocia a cada agente un módulo que calcula su política o sus valores de acción». R01/R06/R23. El archivo conservado algo_factory.py distingue especificaciones de módulos y clases Learner. |
| 27 | La frase ampliada en la ficha 9 decía «Tras actualizar un actor, para cada muestra calcula…», con un sujeto implícito poco claro. | Se nombra «el componente de aprendizaje». R06/R23. Se conserva la razón de probabilidades y su aplicación a los factores pendientes. |
| 28 | Las líneas continuas y discontinuas del esquema de controladores no tenían una explicación explícita en la prosa. | Se añade qué representa cada tipo de flecha. Es una mejora editorial opcional bajo R09/R12, no una observación literal de Caro sobre esta figura. |

No se añaden usos de glosario ni citas en estas cuatro intervenciones; sus secuencias son idénticas a las del inicio de esta revisión. Cada cambio se compiló y se revisó sobre su página antes de continuar.

## Hipótesis examinadas y descartadas

| Hipótesis inicial | Comprobación y decisión |
| --- | --- |
| La remisión sobre duración de memoria de espera no contiene el dato. | Descartada. El destino general es la Sección A.4 y contiene, dentro de A.4.1.1, el parámetro waiting_time_memory y su duración. La remisión es amplia pero válida. Se conserva. El error preliminar se corrigió expresamente en la comunicación al usuario. |
| La página impresa 93 comienza con una línea viuda. | Descartada. La extracción y la imagen muestran dos líneas de continuación del mismo párrafo. Se conserva la paginación; no se añaden penalidades ni saltos sobre la base de la miniatura. |
| La grafía Köpf podría contradecir el índice de NeurIPS. | Descartada tras contrastar las fuentes. El índice HTML muestra Kopf, pero el PDF publicado y su texto completo contienen Köpf. La grafía con diéresis de la bibliografía es correcta y se conserva. |

La ficha oficial y los metadatos confirman los 21 autores, el año y las páginas de la publicación de PyTorch; la portada publicada respalda la diéresis de Köpf. [NeurIPS: ficha](https://proceedings.neurips.cc/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract.html), [metadatos y texto completo](https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Metadata.json), [PDF](https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf).

La ficha y la portada de la publicación de HAPPO respaldan el nombre Fanglei Sun; la corrección anterior se conserva. [Fuente primaria](https://arxiv.org/abs/2109.11251).

## Comprobación de R01–R26

| Regla | Aplicación comprobada en esta revisión |
| --- | --- |
| R01 | Fuente y definición de e(x) antes de la observación; precisión del componente asociado a cada agente. |
| R02 | Detalle operativo necesario en metodología y desarrollos extensos en el apéndice; se conservan las premisas y limitaciones necesarias. |
| R03 | Recorrido escenarios → control → búsqueda/variantes → evaluación → alcance; propósitos reconocibles antes de las operaciones. |
| R04 | Párrafos con función identificable; no se unen por razones de espacio ni se fragmentan para aparentar una mejora. |
| R05 | Definiciones reunidas y repetición de CI recortada sin perder su significado; cautelas posteriores conservadas cuando cumplen una función nueva. |
| R06 | Referentes de red vial, red neuronal y operaciones precisados; correcciones 25–27. |
| R07 | Antecedentes, protocolo de la tesina y campañas documentadas mantienen sujetos y alcances distintos. |
| R08 | A/C no aísla observación y recompensa; Mendoza de referencia no evalúa políticas aprendidas; los protocolos no acreditan ejecuciones por sí solos. |
| R09 | Doce figuras revisadas con sus párrafos, epígrafes y posición efectiva en el PDF. |
| R10 | Los epígrafes identifican; la prosa conserva operaciones, convenciones y límites indispensables. |
| R11 | Citas y procedencias conservadas al mover o abreviar; no se elimina la atribución de un dato o método. |
| R12 | Siete fuentes TikZ pasan el control estático y se revisan visualmente; ficha 28 explicita una convención de flechas. |
| R13 | Doce ecuaciones conservadas, con magnitudes, índices y unidades próximos; las definiciones preceden a su uso. |
| R14 | Siglas revisadas por contexto y función; se conservan desarrollos sustantivos y no se expanden todas las repeticiones. |
| R15 | Terminología española estable, conservando nombres de bibliotecas, claves y rutas. |
| R16 | 150 enlaces de glosario/siglas en metodología hacia 48 destinos distintos, existentes; comprobación de anotaciones GoTo y destinos. |
| R17 | Se preservan las etiquetas y se comprueba el tipo de objeto, sin cambiar referencias plurales o genéricas por un reemplazo ciego. |
| R18 | Cifras y unidades conservadas; miles y decimales uniformes en las familias revisadas. Ficha 25 evita atribuir una operación temporal al conteo. |
| R19 | Atribución de PyTorch y pertinencia de las fuentes de los cambios bibliográficos conservadas; no se impone una cuota de fuentes. |
| R20 | Autorías modificadas contrastadas con fuentes primarias, incluida la diferencia entre transliteración del índice y grafía del PDF. |
| R21 | Se mantienen los signos útiles para listas, fórmulas y relaciones lógicas; no se aplica una prohibición de dos puntos o punto y coma. |
| R22 | Destinos consultados por su contenido y jerarquía, no solo por existir; se descarta la falsa alarma sobre la duración de memoria. |
| R23 | Sujetos y operaciones directos; cambios 25–27. No se sustituyen términos especializados por sinónimos que alteren el método. |
| R24 | Revisión de 37 páginas del capítulo y ocho páginas de cambios asociados; solo tres páginas cambian visualmente en esta pasada. |
| R25 | Se comprueba el alcance de los anuncios del método; no se revisan ni se dan por aprobados resumen y Abstract mediante esta pasada. |
| R26 | Se distingue corrección confirmada, mejora opcional y conservación. Las hipótesis retiradas y las comprobaciones efectivas quedan registradas. |

## Verificación técnica y visual

- Se compararon las doce ecuaciones y los seis cuerpos de tabla de metodología con HEAD y con el inicio de esta pasada: son idénticos. Se conservan las doce figuras y los datos numéricos del capítulo.
- Las secuencias de citas, remisiones, etiquetas y usos de glosario de metodología no cambian en esta pasada. La estructura incluida conserva las 199 etiquetas únicas comprobadas; las 114 remisiones del capítulo mantienen sus destinos.
- Los otros archivos con cambios acumulados conservan sus hashes del inicio de esta pasada. La revisión no revirtió modificaciones anteriores del usuario.
- El PDF tiene 162 páginas. Metodología ocupa las páginas físicas 83–119, impresas 59–95. Se renderizaron las 37 páginas antes y después y se inspeccionaron cinco hojas de contacto y las doce figuras individualmente.
- La comparación de los PNG solo detecta cambios en las páginas físicas 91, 101 y 102, impresas 67, 77 y 78. Las otras 34 páginas del capítulo mantienen una imagen idéntica en la renderización comparada. Las páginas afectadas se revisaron individualmente y en contexto.
- Se inspeccionaron también las páginas físicas 76, 77, 130, 131, 137, 144, 158 y 160, correspondientes a los cambios asociados de marco teórico, tablas y bibliografía.
- Los siete archivos TikZ de metodología pasan check_tikz_safety.py. Se siguió la habilidad tikz-diagrams para el control semántico y visual. Pillow y PyMuPDF no están disponibles en el Python del sistema: no se ejecutó el comprobador visual automático que depende de ellos. Se utilizó Poppler para renderizar, ImageMagick para las hojas de contacto e inspección manual de las imágenes. Esta limitación no se presenta como una prueba automática superada.
- Resultado de la crítica de las doce figuras: conservar. Las figuras de flujo y controladores son esquemas de operaciones; las barras temporales corresponden a las secuencias declaradas y la curva del codificador conserva su cálculo. No se atribuyen efectos experimentales a sus flechas o colores.
- Cada intervención se compiló con latexmk y SyncTeX. El log final solo presenta el aviso externo conocido de tracklang para español; no hay citas o referencias indefinidas ni desbordes. qpdf --check y git diff --check terminan correctamente.

La revisión es editorial, semántica y de integridad de los cambios. Incluye los contrastes documentales y de código identificados; no equivale a repetir campañas, recuperar rutas históricas ausentes ni validar de nuevo todos los experimentos. Los hallazgos históricos de otros capítulos mantienen su alcance y requieren su propia revisión.
