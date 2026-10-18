# Auditoría de recurrencias de las observaciones de Caro

Revisión del **16 de octubre de 2026**, sobre las fuentes locales actuales. Documento complementario de [TODO-comentarios-caro.md](TODO-comentarios-caro.md); no reemplaza ni da por cerradas sus 287 fichas. Las reglas persistentes están en [REGLAS_EDITORIALES_CARO.md](REGLAS_EDITORIALES_CARO.md), enlazadas desde [AGENTS.md](AGENTS.md).

## Resultado y alcance

Se formalizaron **26 reglas** y se registraron **34 grupos de hallazgos o puntos de revisión adicionales**: **21 confirmados**, **11 decisiones editoriales** y **2 verificaciones pendientes**. «Confirmado» significa que la evidencia local demuestra el problema descrito respecto del criterio adoptado; no implica que cada caso requiera una edición independiente. Los dos estados restantes no deben presentarse como errores técnicos ya probados.

Las recurrencias más numerosas son verificables por referencia:

- **136 referencias singulares numeradas en minúscula**, de las cuales **102 están fuera de las líneas del inventario anterior**. Las otras 34 coinciden con líneas que tenían alguna marca, aunque no necesariamente con el fragmento seleccionado por Caro.
- **40 referencias que nombran «apéndice» pero apuntan a una sección interna del único apéndice incluido**. Las 40 están contenidas en las 136 anteriores; no se suman como otras 40 referencias independientes.
- **4 construcciones plurales con «Figuras»/«Tablas» en mayúscula**, contrarias a la convención particular pedida en C002. Están fuera del inventario de referencias singulares.

El [inventario de referencias CSV](auditoria-referencias-caro.csv) reúne las **140 ocurrencias** singulares/plurales detectadas para estos controles, con destino, tipo real y coincidencia por línea con el TODO anterior. No pretende ser una lista de todas las referencias correctas del proyecto.

Además de las recurrencias de formato, se encontraron desarrollos de figuras fragmentados, explicaciones repetidas en epígrafes y prosa, una remisión que atribuye al destino definiciones que están en el glosario, siglas no presentadas y términos inconsistentes. El capítulo de resultados y el de conclusiones contienen apartados todavía sin desarrollar; ese estado de redacción debe distinguirse de la existencia o ausencia de ejecuciones externas.

**No se modificaron los capítulos, las imágenes, la bibliografía, el glosario ni `main.pdf`**. Se añadieron reglas, diagnóstico e inventario y se actualizó `AGENTS.md` para que las reglas sean leídas en futuras tareas. `AGENTS.md` está excluido por `.gitignore`: su modificación existe en disco, aunque no aparece en `git diff`. El archivo independiente de reglas no está ignorado y puede versionarse junto al diagnóstico. No se hizo una nueva compilación porque no se modificaron las fuentes de la tesina.

## Método y límites

1. Se releyeron los 180 comentarios escritos y las interpretaciones de las 107 marcas sin comentario, usando el inventario y el TODO previo. Se agruparon pedidos explícitos, principios inferidos y extensiones operativas. No se convirtió una corrección léxica local en una palabra prohibida.
2. Se usó la lista real de `\include` de `main.tex`: portada, resumen/Abstract, agradecimientos, introducción, marco teórico, metodología, resultados, conclusiones y apéndice. Se revisaron además las macros de acrónimos, entradas pertinentes de glosario y bibliografía. `2-resumen.tex`, `4-marco_teorico_2.tex` y `original_marco_teorico.tex` quedaron fuera del diagnóstico del texto activo. No se modificaron skills ni archivos ajenos.
3. Se combinaron lectura de los desarrollos y búsquedas dirigidas por regla. Para referencias, se inspeccionaron las declaraciones reales de capítulo, sección y entornos de destino. Se excluyeron comentarios LaTeX del recuento y no se identificó el tipo de objeto solo por su prefijo de etiqueta.
4. Se contrastaron las localizaciones con el inventario anterior. «Fuera de las líneas anteriores» es un criterio conservador de recurrencia; no equivale a demostrar que cada pasaje nunca fue visto por Caro. Algunas fichas amplían un problema a otro término dentro de una línea ya marcada y así se indica.
5. Se consultó el texto extraído del `main.pdf` existente, de **162 páginas físicas**, y se inspeccionaron visualmente las páginas físicas **85 y 126** (impresas **61 y 102**) para el flujo metodológico, la referencia «apéndice A.4» y la figura UML del entorno. No se hizo una inspección visual integral ni se certifican todas las páginas, los enlaces de glosario o las líneas aisladas.
6. Las citas breves de las fichas se comprobaron contra la línea indicada de la fuente. No se verificaron publicaciones ni código externo en esta auditoría editorial. Los casos que necesitan esa evidencia se dejaron como pendientes; no se afirma que una referencia o un algoritmo sean falsos solo por no haberlos contrastado aquí.

Los hallazgos corresponden a una fotografía del árbol de trabajo: sus líneas cambiarán al editar. La ausencia de una nueva ficha para una regla no constituye aprobación de todos sus usos; varios problemas importantes ya están detallados en el TODO original.

## Cómo se deben interpretar las reglas

| Inferencia que sí se sostiene | Generalización que se evita |
| --- | --- |
| Definir conceptos antes de usarlos para razonar. | Prohibir toda anticipación orientativa. |
| Dar continuidad a la lectura de una figura. | Exigir un único párrafo para toda figura o impedir volver a citarla con otra función. |
| Reducir epígrafes que contienen el argumento o lo repiten. | Imponer un máximo de palabras o quitar leyendas indispensables. |
| Sustituir signos cuando ocultan relaciones entre ideas. | Prohibir dos puntos, punto y coma o elipsis correctas. |
| Desarrollar siglas en una presentación sustantiva. | Expandirlas en cada repetición o traducir nombres de funciones. |
| Dar sujetos y antecedentes claros. | Prohibir demostrativos o reemplazar todos los usos de «red». |
| Elegir fuentes adecuadas y atribuir autoría correctamente. | Prohibir Sutton y Barto, imponer cuotas de citas o completar una autoría de memoria. |
| Abreviar fórmulas editoriales redundantes de procedencia. | Eliminar fuentes de imágenes, algoritmos o datos ajenos. |
| Simplificar cautelas repetidas conservando su contenido. | Afirmar causalidad, optimalidad, ejecución o inexistencia de antecedentes sin evidencia. |
| Aplicar una convención uniforme de referencias y unidades. | Presentar la convención de Caro como norma universal o cambiar literales de código y versiones. |
| Usar glosario con entradas semánticamente pertinentes. | Enlazar cada palabra, equiparar bootstrap estadístico con bootstrapping de RL o confiar solo en glsaddall. |
| Registrar estados incompletos de redacción. | Inferir que no hubo ejecuciones fuera de la evidencia examinada o completar resultados inventados. |

## Fichas de hallazgos adicionales

En cada ficha se registra evidencia, efecto sobre la lectura, corrección propuesta y criterio de cierre. Las ubicaciones son fuentes actuales. Las referencias a C identifican el origen de la regla, no una observación literal de Caro sobre este nuevo pasaje.

### H01. Referencias singulares numeradas en minúscula

- [ ] **Confirmado · Prioridad editorial.** Reglas: R17.
- **Origen:** C002, C036, C042, C046, C223. **Relación con el relevamiento anterior:** Recurrencia transversal; incluye coincidencias con fichas anteriores.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:253](/home/juanm4/Documentos/tesina/5-metodologia.tex:253): `ecuación \ref{eq:gae}`.
  - [8-apendice_arquitectura.tex:732](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:732): `ecuación \eqref{eq:encoder_mezcla_convexa}`.
  - [4-marco_teorico.tex:1504](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1504): `ecuación \eqref{eq:happo_objetivo_clip}`.
- **Problema y alcance:** El inventario completo detecta 136 referencias singulares con nombre en minúscula; 102 están fuera de las líneas del TODO anterior. Es una discrepancia con la convención editorial pedida, no una regla universal del español. Las otras 34 ocurrencias comparten línea con una o más fichas anteriores y no necesariamente con su selección exacta.
- **Corrección propuesta:** Revisar cada ocurrencia del inventario A y aplicar la mayúscula; tratar «subsección» como «Sección». Resolver antes el tipo de destino de H02, para no convertir una referencia mal nombrada en otra igual de ambigua pero con mayúscula.
- **Criterio de cierre:** Cada referencia singular coincide con el tipo y convención del objeto; las 102 ocurrencias fuera de líneas anteriores tienen decisión documentada.

### H02. Secciones internas presentadas como apéndices distintos

- [ ] **Confirmado · Prioridad media.** Reglas: R17, R22.
- **Origen:** C042, C051, C244. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:41](/home/juanm4/Documentos/tesina/5-metodologia.tex:41): `apéndice \ref{sec:parametros_sumo}`.
  - [5-metodologia.tex:282](/home/juanm4/Documentos/tesina/5-metodologia.tex:282): `apéndice \ref{subsec:codificacion_espera_apendice}`.
  - [6-resultados.tex:45](/home/juanm4/Documentos/tesina/6-resultados.tex:45): `apéndice \ref{sec:procedencia_mendoza}`.
- **Problema y alcance:** Se comprobaron 40 referencias con «apéndice» cuyo destino real es una sección, subsección o subsubsección de 8-apendice_arquitectura.tex. El PDF actual muestra, por ejemplo, «apéndice A.4» en la página física 85, impresa 61. La etiqueta no está rota: el problema es cómo se nombra la unidad. La auditoría inspeccionó las declaraciones estructurales, no solo prefijos sec:/subsec:.
- **Corrección propuesta:** Usar «Sección A.x» o «Sección A.x del Apéndice A». Si se quiere remitir al apéndice completo, usar su etiqueta de capítulo y precisar la materia sin cambiar el destino específico por accidente.
- **Criterio de cierre:** Las 40 ubicaciones del inventario B remiten al objeto nombrado; los números se generan con las etiquetas existentes.

### H03. Mayúsculas en referencias plurales que contradicen la convención pedida

- [ ] **Confirmado · Prioridad editorial.** Reglas: R17.
- **Origen:** C002. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:83](/home/juanm4/Documentos/tesina/5-metodologia.tex:83): `Las Figuras`.
  - [5-metodologia.tex:453](/home/juanm4/Documentos/tesina/5-metodologia.tex:453): `en las Tablas`.
  - [8-apendice_arquitectura.tex:416](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:416): `Las Tablas`.
  - [8-apendice_arquitectura.tex:610](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:610): `Las Tablas`.
- **Problema y alcance:** Caro distinguió el singular numerado con mayúscula del plural «las figuras/las tablas» con minúscula. Estas cuatro construcciones plurales no siguen ese criterio. No son parte de las 136 referencias singulares de H01.
- **Corrección propuesta:** Cambiar únicamente el sustantivo referido en estas cuatro construcciones, manteniendo «Las» al comienzo de oración y las etiquetas LaTeX.
- **Criterio de cierre:** Las cuatro referencias plurales siguen la convención particular de la tesina, sin alterar títulos ni nombres genéricos.

### H04. Explicación de la figura UML del entorno antes, dentro y después del dibujo

- [ ] **Confirmado · Prioridad alta.** Reglas: R05, R09, R10.
- **Origen:** C076, C092, C114. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:26](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:26): `La Figura`.
  - [8-apendice_arquitectura.tex:110](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:110): `En cada clase se muestran sus principales atributos y métodos.`.
  - [8-apendice_arquitectura.tex:114](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:114): `se organiza desde la abstracción general hacia las entidades de la red.`.
- **Problema y alcance:** El texto explica convenciones antes del dibujo, enumera relaciones en el epígrafe y vuelve a presentar la figura y sus clases después. Hay contenido útil, pero su distribución reproduce el recorrido fragmentado que Caro pidió corregir. Se verificó la página física 126 del PDF actual, impresa 102.
- **Corrección propuesta:** Reunir las convenciones y la lectura de clases/relaciones antes de la figura, en párrafos coherentes; acortar el epígrafe y evitar la segunda presentación. Mantener la advertencia de que el UML es una especificación, no un inventario exacto del código.
- **Criterio de cierre:** El lector puede interpretar el dibujo con un bloque próximo; epígrafe y prosa no repiten las mismas relaciones.

### H05. Explicación de la figura UML de recompensas repartida a ambos lados

- [ ] **Confirmado · Prioridad alta.** Reglas: R05, R09, R10.
- **Origen:** C076, C092, C114. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:123](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:123): `La Figura`.
  - [8-apendice_arquitectura.tex:192](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:192): `Las clases inferiores realizan la interfaz`.
  - [8-apendice_arquitectura.tex:196](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:196): `sitúa la clase abstracta`.
- **Problema y alcance:** La figura se presenta con la relación de composición; el epígrafe vuelve a describir las clases y el párrafo posterior reinicia la explicación desde su posición en el dibujo. Son las mismas entidades y relación, no una interpretación posterior diferente.
- **Corrección propuesta:** Mover la lectura de la jerarquía y del cálculo a un desarrollo antes del dibujo. Conservar la distinción entre herencia y uso de otra clase; dejar en el epígrafe identificación y convenciones mínimas.
- **Criterio de cierre:** Una sola presentación continua explica las relaciones sin perder el papel de cada clase.

### H06. El epígrafe del flujo metodológico concentra parte del argumento

- [ ] **Confirmado · Prioridad alta.** Reglas: R02, R09, R10.
- **Origen:** C003, C114. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:24](/home/juanm4/Documentos/tesina/5-metodologia.tex:24): `muestra cómo los escenarios preparados alimentan las dos líneas.`.
  - [5-metodologia.tex:29](/home/juanm4/Documentos/tesina/5-metodologia.tex:29): `Las flechas representan dependencias, no el orden cronológico de las campañas; la selección final utiliza los resultados de la búsqueda.`.
- **Problema y alcance:** La prosa introduce el esquema con una frase breve, mientras que el epígrafe desarrolla alcance de las dos líneas, escenarios, configuración fija y sentido temporal. Se verificó la página física 85, impresa 61: el epígrafe ocupa varias líneas y contiene la principal aclaración sobre cómo interpretar el flujo.
- **Corrección propuesta:** Explicar en el cuerpo qué líneas usan los escenarios, qué significa la dependencia y qué relación tiene con la cronología. Mantener en el epígrafe una leyenda breve de flechas si resulta necesaria para interpretar el esquema de forma autónoma.
- **Criterio de cierre:** La distinción entre dependencia y cronología sigue siendo explícita y no queda delegada al epígrafe.

### H07. El epígrafe de los controladores repite y prolonga su explicación

- [ ] **Confirmado · Prioridad media.** Reglas: R05, R09, R10.
- **Origen:** C003, C154, C166. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:365](/home/juanm4/Documentos/tesina/5-metodologia.tex:365): `distingue la información utilizada durante el entrenamiento y la ejecución.`.
  - [5-metodologia.tex:377](/home/juanm4/Documentos/tesina/5-metodologia.tex:377): `Cada algoritmo y agente tiene su propia política;`.
- **Problema y alcance:** La sección ya desarrolla actores propios, crítico centralizado y observación vecinal. El epígrafe repite esas operaciones y agrega una formulación poco precisa («cada algoritmo y agente»). La presentación de la figura además queda separada de su aparición por explicaciones adicionales de aprendizaje.
- **Corrección propuesta:** Concentrar la lectura de la figura inmediatamente antes de ella, precisar que cada agente dispone de su política según el algoritmo y reducir el epígrafe a la distinción que muestra. No borrar detalles de máscara u observación que sean necesarios para distinguir entrenamiento y ejecución.
- **Criterio de cierre:** El texto expresa sin ambigüedad quién recibe cada información y evita duplicar esa explicación en el epígrafe.

### H08. Presentación anticipada de la figura de componentes del codificador

- [ ] **Decisión editorial · Prioridad media.** Reglas: R09, R22.
- **Origen:** C076, C092. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:723](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:723): `La Figura`.
  - [8-apendice_arquitectura.tex:727](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:727): `la mezcla escalada`.
  - [8-apendice_arquitectura.tex:737](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:737): `Ejemplo ilustrativo`.
- **Problema y alcance:** La figura se anuncia antes de explicar las claves del código y de completar la equivalencia algebraica; aparece después de ese desarrollo. No se ha probado una ruptura de lectura tan marcada como en las dos figuras UML: la materia sigue siendo el codificador.
- **Corrección propuesta:** Evaluar mover la introducción de la figura al final del desarrollo algebraico o ampliar la frase de anuncio para explicar su relación con la demostración que sigue. Conservar la distinción entre ejemplo I=22 y comparación A/C I=17.
- **Criterio de cierre:** La ubicación elegida se justifica por la continuidad del argumento; no se mueve solo por contar líneas entre referencia y figura.

### H09. Rótulo de relación comprimido entre las clases UML

- [ ] **Confirmado · Prioridad media.** Reglas: R12, R24.
- **Origen:** C062, C064; extensión a diagramas de arquitectura. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:106](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:106): `1..* contiene`.
- **Problema y alcance:** En la página física 126 del PDF actual, el rótulo horizontal «1..* contiene» ocupa más espacio que el hueco entre BaseSumoEnvironment y TrafficLight y toca/invade sus bordes. La fuente usa cajas de 6,2 cm separadas por 1,2 cm y coloca el texto sin ancho ni salto de línea. El problema se observó en el renderizado; no se deduce solo de esa configuración.
- **Corrección propuesta:** Ajustar la separación, acortar/distribuir el rótulo o colocarlo en otro tramo. Conservar el significado de la relación y la multiplicidad, y revisar la página completa después de compilar.
- **Criterio de cierre:** El rótulo es legible sin tocar cajas, otros textos o flechas, manteniendo tamaño de fuente suficiente.

### H10. Repetición inmediata del propósito del patrón Strategy

- [ ] **Decisión editorial · Prioridad media.** Reglas: R05.
- **Origen:** C035, C079, C104. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:119](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:119): `permite sustituir la métrica de optimización sin modificar el bucle principal de simulación.`.
  - [8-apendice_arquitectura.tex:196](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:196): `permite sustituir la formulación de la recompensa sin cambiar el bucle de simulación.`.
  - [8-apendice_arquitectura.tex:206](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:206): `encapsular los algoritmos de recompensa para intercambiarlos sin modificar el módulo que aplica las señales.`.
- **Problema y alcance:** El propósito de intercambiar la recompensa sin modificar el bucle se explica en la presentación del patrón, al cerrar la lectura de la figura y de nuevo en la lista siguiente. La lista posterior declara una función de resumen y puede ser útil para consulta. Conviene decidir si esa función justifica repetir el propósito o si bastaría con la referencia a la interfaz; la repetición textual está comprobada, su supresión requiere criterio editorial.
- **Corrección propuesta:** Mantener una definición completa y convertir las apariciones restantes en aplicaciones concretas o remisiones breves. No quitar el enlace entre patrón, interfaz y clase utilizada.
- **Criterio de cierre:** Cada reaparición aporta una responsabilidad o relación nueva y no repite el mismo beneficio con sinónimos.

### H11. Advertencia repetida sobre las semillas TPE alrededor de la tabla

- [ ] **Decisión editorial · Prioridad editorial.** Reglas: R05, R10.
- **Origen:** C079, C104, C114. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:565](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:565): `las semillas de`.
  - [8-apendice_arquitectura.tex:589](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:589): `Ninguna sustituye una réplica de entrenamiento.`.
- **Problema y alcance:** El epígrafe advierte que las semillas TPE no son réplicas de entrenamiento y la prosa inmediatamente posterior vuelve a distinguirlas de las de SUMO y repite esa advertencia. La cautela es necesaria. Su repetición puede justificarse si se busca autonomía de la tabla; debe decidirse si el epígrafe necesita conservarla o si la prosa próxima la hace redundante.
- **Corrección propuesta:** Reunir función y límite de cada semilla en la prosa que presenta la tabla y dejar un epígrafe identificatorio. Conservar la diferencia entre propuestas, simulaciones y réplicas independientes.
- **Criterio de cierre:** La limitación permanece una vez, en un lugar visible y con referente claro.

### H12. API aparece sin desarrollo en su primera presentación operativa

- [ ] **Confirmado · Prioridad media.** Reglas: R14, R15.
- **Origen:** C019, C025, C183. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:9](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:9): `\acrshort{acr-api}`.
- **Problema y alcance:** La fuente usa únicamente la sigla y la entrada existente no se desarrolla en los capítulos anteriores del cuerpo. La página física 124, impresa 100, muestra «API libsumo / traci». Su presencia en la lista de siglas inicial no sustituye esta presentación sustantiva.
- **Corrección propuesta:** Desarrollar interfaz de programación de aplicaciones y su sigla antes de describir la integración, usando una macro que produzca la forma deseada. Evitar repetir el desarrollo completo en cada patrón.
- **Criterio de cierre:** El primer uso operativo es comprensible sin consultar la lista de siglas.

### H13. VF en VF-MAPPO depende de una sigla no desarrollada en el pasaje

- [ ] **Decisión editorial · Prioridad media.** Reglas: R14, R15.
- **Origen:** C025, C183. **Relación con el relevamiento anterior:** Nueva instancia dentro de un bloque de antecedentes ya revisado; sin comentario específico sobre VF.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1575](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1575): `\acrshort{acr-vf}-\acrshort{acr-mappo}`.
- **Problema y alcance:** El nombre del método se construye con dos siglas cortas y VF no se desarrolla en el cuerpo del pasaje. La entrada VF declara «función de valor/Value Function», pero esta auditoría no comprobó si ese desarrollo corresponde al nombre exacto de la variante de Liu et al. La marca anterior de ese bloque no señalaba VF.
- **Corrección propuesta:** Verificar el nombre del método en la publicación y presentarlo con una explicación breve si se conserva. No expandir automáticamente VF a partir de la entrada actual sin esa comprobación.
- **Criterio de cierre:** El nombre coincide con la fuente y el lector comprende el calificativo de la variante; queda registrada la fuente usada para resolverlo.

### H14. CL, EP, AS y FP se acumulan como abreviaturas locales

- [ ] **Decisión editorial · Prioridad media.** Reglas: R01, R14, R15.
- **Origen:** C025, C183, C235. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1330](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1330): `$CL: s = (o_1, \dots, o_n)$`.
  - [4-marco_teorico.tex:1330](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1330): `$AS_i = EP \cup o_i$`.
  - [4-marco_teorico.tex:1330](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1330): `($FP$)`.
- **Problema y alcance:** Las categorías ya están descritas en español, por lo que no se las considera conceptos completamente indefinidos. Se agregan cuatro abreviaturas de la clasificación del antecedente sin desarrollar sus nombres de origen; corresponde evaluar si son necesarias y si conviene explicarlas como etiquetas locales. Se mezclan nombres de representaciones, notación de un estado y filtrado en el mismo ítem. No se afirma que la taxonomía esté equivocada.
- **Corrección propuesta:** Conservar solo las abreviaturas que se utilicen después, desarrollar las necesarias y separar las alternativas del filtrado opcional. Si se requiere compararlas, usar una tabla con nombre, información utilizada y alcance, manteniendo la cita al estudio.
- **Criterio de cierre:** Cada abreviatura conservada tiene desarrollo y función; las eliminadas no dejan referencias huérfanas.

### H15. Softmax tiene entrada de glosario pero su definición visible no la enlaza

- [ ] **Confirmado · Prioridad editorial.** Reglas: R16.
- **Origen:** C045, C048, C186. **Relación con el relevamiento anterior:** Ampliación: término diferente en una línea que ya tenía otra marca.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:988](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:988): `\textit{softmax}`.
  - [glosario.tex:355](/home/juanm4/Documentos/tesina/glosario.tex:355): `\newglossaryentry{softmax}`.
- **Problema y alcance:** La presentación de la función usa texto en cursiva, aunque ya existe una entrada con nombre, texto y descripción. Se trata de una ocurrencia distinta del MDP señalado en esa misma línea por C226. El problema comprobado es la falta de macro de enlace en esta definición, no la ausencia de la entrada.
- **Corrección propuesta:** Enlazar esa primera presentación con la entrada existente y revisar la forma visible. Mantener la ecuación y el desarrollo en el cuerpo; no asumir que glsaddall genera el enlace desde la palabra.
- **Criterio de cierre:** La definición tiene el enlace correcto y se verifica su destino en el PDF después del ciclo de glosario.

### H16. La remisión sobre distribuciones promete una definición que no está en el destino

- [ ] **Confirmado · Prioridad media.** Reglas: R01, R16, R22.
- **Origen:** C159, C186, C244. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:416](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:416): `Uniforme continua y loguniforme tienen el significado explicado en la sección`.
  - [5-metodologia.tex:453](/home/juanm4/Documentos/tesina/5-metodologia.tex:453): `Las distribuciones loguniformes permiten explorar varias escalas de magnitudes positivas;`.
  - [glosario.tex:404](/home/juanm4/Documentos/tesina/glosario.tex:404): `\newglossaryentry{distribucion_uniforme_continua}`.
  - [glosario.tex:408](/home/juanm4/Documentos/tesina/glosario.tex:408): `\newglossaryentry{distribucion_loguniforme}`.
- **Problema y alcance:** El destino subsec:hpo_phase1 describe la finalidad de una distribución loguniforme, pero no define la uniforme continua ni explica que la uniformidad es en escala logarítmica. Las definiciones sí están en el glosario, y la frase del apéndice no enlaza esos términos. No corresponde afirmar que falten de todo el documento.
- **Corrección propuesta:** Explicar brevemente ambas distribuciones donde se introduce su uso o remitir de forma exacta al glosario con enlaces semánticos. Ajustar la remisión para que no atribuya al destino un contenido inexistente.
- **Criterio de cierre:** El destino contiene lo prometido, o la oración nombra y enlaza la ubicación que realmente lo contiene.

### H17. Minibatches y epochs reaparecen tras adoptar formas españolas

- [ ] **Confirmado · Prioridad editorial.** Reglas: R15.
- **Origen:** C177, C204. **Relación con el relevamiento anterior:** Propagación incompleta de C177/C204; incluye ubicaciones y usos adicionales.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:892](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:892): `\textit{minibatches}`.
  - [4-marco_teorico.tex:895](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:895): `\textit{minibatches}`.
  - [4-marco_teorico.tex:952](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:952): `se conservan los términos`.
  - [4-marco_teorico.tex:1083](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1083): `\textit{epochs}`.
  - [4-marco_teorico.tex:1107](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1107): `\textit{epochs}`.
  - [4-marco_teorico.tex:1331](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1331): `\textit{epochs}`.
  - [4-marco_teorico.tex:1350](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1350): `\textit{minibatches}`.
  - [8-apendice_arquitectura.tex:697](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:697): `\gls{mini_lote}`.
- **Problema y alcance:** La corrección de minilotes no se propaga al resto del capítulo: se alternan palabras inglesas con lote, minilote y época, y el párrafo de la línea 952 anuncia expresamente conservar varios términos ingleses. El apéndice ya usa las formas españolas. El problema es la convención contradictoria, no que esté prohibido mencionar el inglés.
- **Corrección propuesta:** Adoptar la forma española en la prosa y pseudocódigo descriptivo, presentar el inglés una vez y dejar intactas claves como num_epochs/minibatch_size. Revisar también 4-marco_teorico.tex:954 y :1097.
- **Criterio de cierre:** Prosa, glosario, pseudocódigo y epígrafes siguen el mismo vocabulario sin modificar literales de implementación.

### H18. La forma abreviada log-probabilidad sobrevive en el epígrafe

- [ ] **Confirmado · Prioridad editorial.** Reglas: R15.
- **Origen:** C229. **Relación con el relevamiento anterior:** Nueva ubicación de una formulación ya señalada en la prosa.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1028](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1028): `log-probabilidad`.
- **Problema y alcance:** C229 señala la formulación de la prosa en la línea 995; el epígrafe mantiene la misma forma y debe coordinarse con su corrección. No se trata de otra operación matemática: se refiere al logaritmo de la probabilidad de la acción.
- **Corrección propuesta:** Usar la forma completa elegida para log π también en el epígrafe, y revisar si la explicación de su gradiente pertenece al cuerpo conforme a R10.
- **Criterio de cierre:** El término visible es consistente y mantiene el significado de la ecuación.

### H19. Alternancia de ejecuciones y corridas

- [ ] **Confirmado · Prioridad editorial.** Reglas: R15, R23.
- **Origen:** C017, C189, C196; extensión al vocabulario del proyecto. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:207](/home/juanm4/Documentos/tesina/5-metodologia.tex:207): `esas corridas.`.
  - [5-metodologia.tex:691](/home/juanm4/Documentos/tesina/5-metodologia.tex:691): `En cada corrida`.
  - [6-resultados.tex:27](/home/juanm4/Documentos/tesina/6-resultados.tex:27): `tasas de las corridas`.
  - [6-resultados.tex:47](/home/juanm4/Documentos/tesina/6-resultados.tex:47): `estas dos corridas;`.
  - [8-apendice_arquitectura.tex:278](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:278): `originales de las corridas;`.
  - [8-apendice_arquitectura.tex:299](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:299): `por las corridas.`.
  - [8-apendice_arquitectura.tex:328](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:328): `produjera las corridas.`.
- **Problema y alcance:** Estas apariciones alternan con «ejecuciones» para la misma actividad. plan-correcciones.md ya registra la preferencia por «ejecuciones». Es un problema de estabilidad léxica del proyecto, no una incorrección universal de «corrida».
- **Corrección propuesta:** Uniformar a «ejecución» cuando designe una simulación o trabajo ejecutado; conservar textos literales de documentos o identificadores si fueran citas o nombres.
- **Criterio de cierre:** La prosa propia usa una denominación coherente y no cambia los identificadores conservados.

### H20. Agrupación de miles diferente para los mismos tipos de cantidades

- [ ] **Confirmado · Prioridad editorial.** Reglas: R18.
- **Origen:** C006. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:153](/home/juanm4/Documentos/tesina/5-metodologia.tex:153): `25.175,84`.
  - [5-metodologia.tex:181](/home/juanm4/Documentos/tesina/5-metodologia.tex:181): `260.000`.
  - [8-apendice_arquitectura.tex:289](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:289): `25\,175,84`.
  - [8-apendice_arquitectura.tex:291](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:291): `260\,000`.
- **Problema y alcance:** La prosa usa punto de miles y la tabla del apéndice agrupa con espacio fino cantidades comparables. Ambos formatos son interpretables; su coexistencia contradice la uniformidad pedida. Esto no debe mezclarse con los puntos de versiones, semillas u otras cadenas técnicas.
- **Corrección propuesta:** Elegir y documentar un criterio para prosa y tablas, respetando coma decimal; conservar la exactitud numérica y las excepciones técnicas. Revisar ejemplos de la misma familia en 8-apendice_arquitectura.tex:299 y :654.
- **Criterio de cierre:** Las cantidades comparables tienen formato uniforme y los identificadores y valores no cambiaron.

### H21. Métrica de optimización usada para describir una función de recompensa

- [ ] **Decisión editorial · Prioridad media.** Reglas: R06, R15.
- **Origen:** C203, C205. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:119](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:119): `sustituir la métrica de optimización`.
  - [8-apendice_arquitectura.tex:121](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:121): `RewardFn`.
  - [5-metodologia.tex:427](/home/juanm4/Documentos/tesina/5-metodologia.tex:427): `la espera agregada por las inserciones agregadas.`.
- **Problema y alcance:** El patrón se aplica a RewardFn, pero la oración lo denomina «métrica de optimización». En metodología se distingue recompensa, objetivo de búsqueda y métricas de evaluación. El uso genérico de «métrica» puede deshacer esa separación; no se ha comprobado aquí el comportamiento del código externo.
- **Corrección propuesta:** Precisar «sustituir la formulación de la recompensa» si ese es el componente intercambiado, y reservar «función objetivo de búsqueda» para J y «métrica» para la medida evaluada.
- **Criterio de cierre:** El término designa el mismo objeto en diseño, metodología y glosario; no se confunden las tres cantidades.

### H22. Catálogo de claves de implementación acumulado en un párrafo

- [ ] **Decisión editorial · Prioridad media.** Reglas: R04, R06, R21.
- **Origen:** C148–C151, C162, C235. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:645](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:645): `En las redes sintéticas,`.
  - [8-apendice_arquitectura.tex:645](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:645): `el horizonte del valor objetivo temporal;`.
- **Problema y alcance:** El párrafo reúne conversión de episodios a lote, varios contadores IDQN, programación de exploración y cota de pérdida, con una sucesión de punto y coma y definiciones elípticas. La tabla de claves de la línea 508 identifica nombres, pero no sustituye la explicación funcional de estas cantidades.
- **Corrección propuesta:** Separar cálculo del lote, contadores de IDQN y cota del crítico. Si conviene una tabla, usar columnas de función, clave y unidad/contador, sin copiar de nuevo todos los dominios. No tratar la elipsis gramatical como error por sí sola.
- **Criterio de cierre:** El lector localiza qué cuenta cada parámetro y en qué unidad sin recorrer una cadena heterogénea de claves.

### H23. Reglas de refinamiento presentadas como un bloque denso de condiciones

- [ ] **Decisión editorial · Prioridad media.** Reglas: R01, R04, R21.
- **Origen:** C158, C192, C235. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:641](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:641): `Se conserva el dominio original si`.
  - [8-apendice_arquitectura.tex:641](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:641): `En parámetros categóricos`.
- **Problema y alcance:** La descripción combina numéricos, excepciones para mantener el dominio, redondeo de enteros y tratamiento categórico dentro de un solo párrafo. La información es necesaria en un apéndice; el riesgo es perder el orden entre regla principal y excepciones, no que el detalle deba retirarse.
- **Corrección propuesta:** Presentar una secuencia por tipo de variable y colocar cada excepción junto a la operación que modifica. Conservar los porcentajes, la escala logarítmica y la exclusión del extremo superior.
- **Criterio de cierre:** Puede reconstruirse el procedimiento sin decidir a qué rama pertenece cada condición; los valores y decisiones metodológicas permanecen iguales.

### H24. Procedencia, alcance y notación de dominios mezclados en la introducción de tablas

- [ ] **Confirmado · Prioridad media.** Reglas: R04, R05, R22.
- **Origen:** C054, C138, C235. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [8-apendice_arquitectura.tex:610](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:610): `Los valores corresponden al archivo`.
  - [8-apendice_arquitectura.tex:610](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:610): `La columna «Muestreo»`.
  - [8-apendice_arquitectura.tex:610](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:610): `En el muestreo entero,`.
- **Problema y alcance:** El párrafo pasa de identificar las doce combinaciones y su archivo a distinguir Mendoza, definir la columna de muestreo, explicar extremos de intervalos, llaves y lectura de columnas. Tiene varias funciones que el lector necesita consultar por separado.
- **Corrección propuesta:** Dividir la introducción en procedencia/alcance, convención de muestreo y guía de lectura. Conservar una sola explicación común de la notación y remitir a ella sin promesas de contenido inexistente como en H16.
- **Criterio de cierre:** Cada párrafo tiene una función reconocible y las tablas siguen introducidas antes de aparecer.

### H25. Ambos carece de un antecedente suficientemente preciso en el análisis de intervalos

- [ ] **Confirmado · Prioridad media.** Reglas: R06.
- **Origen:** C117, C199. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:656](/home/juanm4/Documentos/tesina/5-metodologia.tex:656): `Se informan intervalos percentiles del 95\% y del 98,33\%.`.
  - [5-metodologia.tex:658](/home/juanm4/Documentos/tesina/5-metodologia.tex:658): `Ambos son aproximaciones con 24 pares`.
- **Problema y alcance:** Antes de «Ambos» se mencionan dos niveles de intervalo percentil y se introduce un intervalo t. El sentido parece ser comparar procedimientos percentil y t, pero la concordancia permite leer que se habla de dos intervalos entre tres posibilidades.
- **Corrección propuesta:** Nombrar «los procedimientos percentil y t» o «ambos métodos de construcción de intervalos», y aclarar qué niveles se calculan con cada uno. Mantener la cautela sobre cobertura.
- **Criterio de cierre:** El lector identifica sin inferencia qué dos procedimientos se consideran aproximaciones.

### H26. Indicador global de teletransportes al cierre del apartado de equidad local

- [ ] **Decisión editorial · Prioridad media.** Reglas: R02, R03, R04.
- **Origen:** C158, C207. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:607](/home/juanm4/Documentos/tesina/5-metodologia.tex:607): `Métricas locales por agente y equidad espacial`.
  - [5-metodologia.tex:620](/home/juanm4/Documentos/tesina/5-metodologia.tex:620): `Los teletransportes se utilizan como indicador de incidencias operacionales severas.`.
- **Problema y alcance:** El indicador de incidencias y sus contadores se desarrolla después del Gini y antes de la evaluación A/C, dentro del apartado de métricas locales. Es transversal a selección y evaluación y no corresponde únicamente a equidad por agente. La ubicación puede hacer perder su alcance.
- **Corrección propuesta:** Crear un párrafo o subapartado claramente identificado de incidencias operacionales, o ubicarlo con las medidas globales de atención a la demanda. Mantener la distinción entre eventos de inicio y contador nativo Summary.
- **Criterio de cierre:** El lector encuentra el indicador bajo un título compatible y entiende en qué procedimientos se registra.

### H27. El capítulo de resultados anuncia análisis que todavía no desarrolla

- [ ] **Confirmado · Prioridad alta.** Reglas: R08, R25.
- **Origen:** C001, C280; extensión a coherencia de anuncios y contenido. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [6-resultados.tex:3](/home/juanm4/Documentos/tesina/6-resultados.tex:3): `Este capítulo organiza los resultados por procedimiento:`.
  - [6-resultados.tex:11](/home/juanm4/Documentos/tesina/6-resultados.tex:11): `Estado de la consolidación y de las búsquedas`.
  - [6-resultados.tex:13](/home/juanm4/Documentos/tesina/6-resultados.tex:13): `Resultados del ajuste y análisis de sensibilidad`.
  - [6-resultados.tex:21](/home/juanm4/Documentos/tesina/6-resultados.tex:21): `Criterios de evaluación y métricas de comparación`.
  - [6-resultados.tex:23](/home/juanm4/Documentos/tesina/6-resultados.tex:23): `Desempeño en escenarios sintéticos:`.
  - [6-resultados.tex:51](/home/juanm4/Documentos/tesina/6-resultados.tex:51): `En esta sección se integran los resultados presentados`.
- **Problema y alcance:** Los apartados de consolidación, sensibilidad, selección, criterios y desempeño sintético no contienen desarrollo; la discusión es una frase de anuncio. La evidencia sustantiva presente se concentra en la comprobación operacional de Mendoza. Es un estado incompleto del borrador, no prueba de que las ejecuciones anunciadas no existan.
- **Corrección propuesta:** Marcar estos desarrollos como pendientes y ajustar los anuncios al estado de la redacción. Completar posteriormente solo con resultados verificables y manteniendo sus procedimientos separados.
- **Criterio de cierre:** Los anuncios describen contenido efectivamente presentado; los apartados pendientes están identificados sin inventar resultados.

### H28. Conclusiones contiene únicamente el anuncio de sus futuras funciones

- [ ] **Confirmado · Prioridad alta.** Reglas: R03, R08, R25.
- **Origen:** C001, C180, C280; extensión al cierre del documento. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [7-conclusiones.tex:3](/home/juanm4/Documentos/tesina/7-conclusiones.tex:3): `Este capítulo sintetiza los hallazgos del estudio`.
- **Problema y alcance:** El capítulo contiene una sola oración ampliada que anuncia hallazgos, limitaciones y trabajo futuro, pero todavía no los desarrolla. Escribir «sintetiza» no equivale a realizar esa síntesis y la organización de la introducción lo presenta como un capítulo cumplido.
- **Corrección propuesta:** Registrar el estado pendiente y completar las conclusiones cuando la evidencia del capítulo anterior esté consolidada. Ajustar mientras tanto las descripciones de organización; no derivar conclusiones de planes o configuraciones.
- **Criterio de cierre:** Hay conclusiones sustentadas o el borrador declara inequívocamente su estado pendiente; resumen, organización y cierre son consistentes.

### H29. El Abstract no presenta sus siglas de manera autónoma

- [ ] **Confirmado · Prioridad media.** Reglas: R14, R25.
- **Origen:** C001, C019, C025–C026. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [1-resumen.tex:7](/home/juanm4/Documentos/tesina/1-resumen.tex:7): `\acrshort{acr-mappo}`.
  - [1-resumen.tex:7](/home/juanm4/Documentos/tesina/1-resumen.tex:7): `\acrshort{acr-happo}`.
  - [1-resumen.tex:7](/home/juanm4/Documentos/tesina/1-resumen.tex:7): `\acrshort{acr-ippo}`.
  - [1-resumen.tex:7](/home/juanm4/Documentos/tesina/1-resumen.tex:7): `\acrshort{acr-idqn}`.
  - [1-resumen.tex:7](/home/juanm4/Documentos/tesina/1-resumen.tex:7): `\acrshort{acr-sumo}`.
- **Problema y alcance:** El Abstract utiliza las siglas cortas de algoritmos y simulador sin desarrollar sus nombres allí. C001 anclaba el resumen español; la reescritura debe revisar esta unidad inglesa por sí misma. La macro de expansión española no se debe trasladar sin comprobar el idioma de salida.
- **Corrección propuesta:** Reducir las siglas que no sean necesarias y desarrollar en inglés las conservadas en el Abstract. Mantener correspondencia con el resumen español sin arrastrar explicaciones técnicas que se quiere simplificar.
- **Criterio de cierre:** El Abstract es comprensible independientemente del resumen español y las expansiones están en el idioma correcto.

### H30. Los ceros documentales de teletransportes no se distinguen dentro de la tabla

- [ ] **Decisión editorial · Prioridad media.** Reglas: R08, R10, R11.
- **Origen:** C003, C088, C280; extensión de atribución y alcance. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [6-resultados.tex:38](/home/juanm4/Documentos/tesina/6-resultados.tex:38): `Teletransportes`.
  - [6-resultados.tex:39](/home/juanm4/Documentos/tesina/6-resultados.tex:39): `0 \\`.
  - [6-resultados.tex:40](/home/juanm4/Documentos/tesina/6-resultados.tex:40): `0 \\`.
  - [6-resultados.tex:47](/home/juanm4/Documentos/tesina/6-resultados.tex:47): `los ceros de la tabla están informados en la documentación del escenario`.
- **Problema y alcance:** La limitación está expresamente aclarada en la prosa posterior y no debe reportarse como ausencia total de advertencia. Sin embargo, la tabla presenta los ceros con el mismo formato que los conteos primarios, por lo que al leerse aislada no distingue su procedencia documental.
- **Corrección propuesta:** Valorar una nota inmediata bajo la tabla o un marcador junto a esos valores que explique su fuente. No reemplazar automáticamente cero por «no disponible»: hay un dato documental, aunque no un contador primario conservado.
- **Criterio de cierre:** La tabla permite distinguir datos primarios y documentales aun en una lectura aislada, manteniendo la advertencia y los valores atribuidos correctamente.

### H31. La ecuación no identifica qué parte de la formulación teórica resume

- [ ] **Confirmado · Prioridad media.** Reglas: R06, R13, R22.
- **Origen:** C175, C219, C244. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1362](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1362): `por tanto, la ecuación resume el paradigma`.
- **Problema y alcance:** La aclaración aparece después de dos ecuaciones (objetivo MAPPO y pérdida del crítico), una lista y un algoritmo. El singular «la ecuación» no identifica cuál se contrasta con el código; además, el párrafo se refiere a diferencias que afectan la formulación anterior como conjunto.
- **Corrección propuesta:** Nombrar la formulación teórica o citar las etiquetas concretas que se comparan. Indicar por separado la ventaja conjunta de la exposición y los objetivos por agente de la implementación, sin declarar una identidad entre ecuación y código.
- **Criterio de cierre:** Cada contraste teoría/implementación tiene un objeto identificado y su remisión lleva al desarrollo pertinente.

### H32. El cambio de orden de actualización del crítico no queda explícito al presentar la adaptación

- [ ] **Verificación pendiente · Prioridad media.** Reglas: R01, R07, R08, R22.
- **Origen:** C028–C034, C238, C280. **Relación con el relevamiento anterior:** Ampliación del contraste teoría/implementación, con comparación de pasajes adicionales.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1516](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1516): `Tras optimizar sucesivamente a los`.
  - [4-marco_teorico.tex:1518](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1518): `La adaptación para control semafórico de este trabajo conserva`.
  - [5-metodologia.tex:369](/home/juanm4/Documentos/tesina/5-metodologia.tex:369): `actualiza primero el crítico y después los actores`.
  - [8-apendice_arquitectura.tex:701](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:701): `el crítico se actualiza al comienzo`.
- **Problema y alcance:** El marco teórico describe el ajuste del crítico después de los actores y el apéndice describe la adaptación con actualización al comienzo de la época. Estas dos descripciones pueden corresponder legítimamente a procedimientos distintos; no se afirma una contradicción del código. La presentación de la adaptación destaca ventajas individuales, pero no explicita allí este cambio de orden.
- **Corrección propuesta:** Contrastar ambas descripciones con las versiones que cada una pretende documentar y añadir una remisión o distinción breve si corresponde. No mover operaciones del algoritmo para hacer coincidir dos formulaciones que se presentan con distinto alcance.
- **Criterio de cierre:** El lector reconoce qué orden es teórico y cuál se implementó; cualquier corrección técnica se respalda con la fuente o código correspondiente.

### H33. La explicación de observabilidad parcial generaliza una restricción local

- [ ] **Decisión editorial · Prioridad media.** Reglas: R06, R08, R15.
- **Origen:** C020, C196, C238. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [4-marco_teorico.tex:1223](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1223): `basa su inferencia exclusivamente en detectores locales`.
  - [5-metodologia.tex:276](/home/juanm4/Documentos/tesina/5-metodologia.tex:276): `añade a esa entrada un valor por cada vecino directo`.
- **Problema y alcance:** El ítem del marco teórico habla de «cada semáforo» exclusivamente con detectores locales; la formulación vecinal C incorpora información de otros agentes. La lectura puede confundir una configuración local ilustrativa con la propiedad general de observabilidad parcial. La auditoría no revalida aquí la definición formal del Dec-POMDP en fuentes externas.
- **Corrección propuesta:** Precisar qué configuración se está describiendo y distinguir información parcial de disponibilidad exclusiva de sensores propios. Vincular con observación local y vecinal sin cambiar el alcance de los formalismos ni suponer recompensa compartida.
- **Criterio de cierre:** La descripción permite comprender ambas variantes y separa el ejemplo local de los supuestos formales.

### H34. PyTorch se presenta como herramienta sin una cita asociada en el cuerpo

- [ ] **Verificación pendiente · Prioridad media.** Reglas: R19, R20.
- **Origen:** C044, C126, C133, C142. **Relación con el relevamiento anterior:** Nueva ubicación respecto del relevamiento anterior.
- **Evidencia y ubicación:**
  - [5-metodologia.tex:233](/home/juanm4/Documentos/tesina/5-metodologia.tex:233): `PyTorch es la biblioteca que calcula y actualiza las redes neuronales.`.
  - [8-apendice_arquitectura.tex:21](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:21): `PyTorch`.
  - [bibliografia.bib:202](/home/juanm4/Documentos/tesina/bibliografia.bib:202): `@article{pytorch,`.
- **Problema y alcance:** La entrada pytorch existe, pero no se encontró una cita a esa clave en los capítulos activos. La presencia de una herramienta en una tabla no obliga por sí sola a citarla en cada aparición; el punto a revisar es su atribución al presentarla como parte del sistema, siguiendo el criterio aplicado a SUMO y RLlib. Los metadatos de esa entrada tampoco se verificaron externamente en esta auditoría.
- **Corrección propuesta:** Comprobar la referencia adecuada para presentar la herramienta y citarla en el lugar pertinente si se conserva ese criterio. Completar/verificar sus metadatos e idioma antes de usar la entrada, sin inferir que la ficha existente ya está validada.
- **Criterio de cierre:** La política de atribución de herramientas es coherente y las citas incorporadas tienen metadatos comprobados.

## Aplicaciones que ya están bien encaminadas y deben conservarse

La revisión no consiste en borrar todas las coincidencias con una palabra o un signo. Estos pasajes muestran límites correctos que las correcciones de estilo deben preservar:

- [5-metodologia.tex:247](/home/juanm4/Documentos/tesina/5-metodologia.tex:247): La diferencia de inicialización entre programas de referencia y políticas se explicita y se reconoce como condición de comparación. No debe desaparecer al acortar.
- [5-metodologia.tex:278](/home/juanm4/Documentos/tesina/5-metodologia.tex:278): La señal con memoria finita se distingue de la espera por viaje y se nombran mecanismos que pueden reducirla sin mejorar el viaje.
- [5-metodologia.tex:427](/home/juanm4/Documentos/tesina/5-metodologia.tex:427): La espera usada por el objetivo de búsqueda se define con su población y agregación; la recompensa se distingue más adelante del objetivo. Es una distinción que debe mantenerse.
- [5-metodologia.tex:523](/home/juanm4/Documentos/tesina/5-metodologia.tex:523): El contraste A/C identifica los dos cambios conjuntos y declara que no aísla el efecto de cada uno. No convertir «cooperación» en una causa identificada por separado.
- [5-metodologia.tex:676](/home/juanm4/Documentos/tesina/5-metodologia.tex:676): La interpretación de una decisión favorable exige revisar inserciones y retrasos previos al ingreso; acortar el párrafo no autoriza a declarar una mejora integral solo a partir de CI.
- [8-apendice_arquitectura.tex:370](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:370): La restauración de un estado vehicular se separa de la restauración del generador aleatorio; se distinguen A/C y protocolo urbano.
- [8-apendice_arquitectura.tex:705](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:705): La falta de retorno común se identifica como límite para trasladar garantías, sin presentar las ventajas por agente como diferencia suficiente por sí sola.
- [main.tex:185](/home/juanm4/Documentos/tesina/main.tex:185): La expansión de acrónimos ya dispone de una estructura de término inglés y sigla en un solo paréntesis. Revisar la salida antes de reescribir esta macro por un problema del PDF antiguo.

Las citas repetidas a una misma fuente no se clasificaron automáticamente como errores; tampoco se consideraron incorrectos todos los párrafos con punto y coma, todos los epígrafes de más de una oración ni todas las apariciones sin enlace de glosario. Para autoría de Cal y Mayor, la reconstrucción del resumen y los problemas originales de redes neuronales, se conserva la trazabilidad del TODO anterior sin volver a contarlos como nuevos por completo.

## Inventario A. Referencias singulares en minúscula

Cada fila corresponde a una ocurrencia, no a un error independiente de las demás reglas. «C previa» indica únicamente que la misma línea tenía una o más fichas anteriores. «Fuera» identifica las 102 ocurrencias fuera de esas líneas. En H02 y el inventario B se revisa además si «apéndice» nombra el tipo correcto.

### 3-introduccion.tex — 6 ocurrencias

| Ubicación | Nombre usado | Etiqueta | Relación con el TODO anterior |
| --- | --- | --- | --- |
| [50](/home/juanm4/Documentos/tesina/3-introduccion.tex:50) | sección | `sec:diseno_escenarios` | C010, C011, C012, C013 |
| [76](/home/juanm4/Documentos/tesina/3-introduccion.tex:76) | capítulo | `cap:marco_teorico` | C036 |
| [78](/home/juanm4/Documentos/tesina/3-introduccion.tex:78) | capítulo | `capitulo:metodologia` | C037, C038 |
| [78](/home/juanm4/Documentos/tesina/3-introduccion.tex:78) | capítulo | `capitulo:resultados` | C037, C038 |
| [80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80) | capítulo | `conclusiones` | C039, C040, C041, C042, C043, C044 |
| [80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80) | apéndice | `apendice:arquitectura_software` | C039, C040, C041, C042, C043, C044 |
### 4-marco_teorico.tex — 30 ocurrencias

| Ubicación | Nombre usado | Etiqueta | Relación con el TODO anterior |
| --- | --- | --- | --- |
| [5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5) | sección | `sec:ingenieria_transito` | C046, C047, C048, C049, C050, C051 |
| [5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5) | sección | `sec:rl` | C046, C047, C048, C049, C050, C051 |
| [5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5) | sección | `sec:marl` | C046, C047, C048, C049, C050, C051 |
| [5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5) | sección | `subsec:antecedentes_marl_tsc` | C046, C047, C048, C049, C050, C051 |
| [234](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:234) | ecuación | `eq:flujo_fundamental` | C078, C079 |
| [239](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:239) | ecuación | `eq:relacion_wardrop` | C081 |
| [261](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:261) | ecuación | `eq:proceso_poisson` | C082, C083 |
| [266](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:266) | ecuación | `eq:intervalo_exponencial` | C084, C085 |
| [639](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:639) | ecuación | `eq:bellman_optimalidad` | C156, C157 |
| [673](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:673) | ecuación | `eq:actor_critic_td` | C172, C173, C174 |
| [775](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:775) | ecuación | `eq:neurona_artificial` | C197 |
| [941](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:941) | ecuación | `eq:perdida_dqn` | C217, C218, C219, C220 |
| [950](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:950) | ecuación | `eq:perdida_dqn` | C221 |
| [954](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:954) | algoritmo | `alg:dqn` | C223, C224 |
| [985](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:985) | capítulo | `capitulo:metodologia` | C225 |
| [1074](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1074) | ecuación | `eq:objetivo_clip_ppo` | C240 |
| [1083](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1083) | algoritmo | `alg:ppo` | C242, C243 |
| [1114](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1114) | sección | `subsec:recompensa_coordinacion` | C244, C245 |
| [1139](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1139) | sección | `sec:formulacion_dec_pomdp` | C248, C249 |
| [1225](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1225) | sección | `subsec:recompensa_coordinacion` | C255, C256 |
| [1334](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1334) | algoritmo | `alg:mappo` | C262 |
| [1360](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1360) | capítulo | `capitulo:metodologia` | C263 |
| [1362](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1362) | sección | `subsec:recompensa_coordinacion` | Fuera |
| [1392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1392) | ecuación | `eq:happo_ventaja_marginal` | C267 |
| [1396](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1396) | ecuación | `eq:happo_descomposicion_ventaja` | C269 |
| [1442](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1442) | ecuación | `eq:happo_objetivo_clip` | C271 |
| [1487](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1487) | algoritmo | `alg:happo` | C274 |
| [1504](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1504) | ecuación | `eq:happo_objetivo_clip` | Fuera |
| [1518](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1518) | sección | `subsec:recompensa_coordinacion` | C275 |
| [1591](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1591) | capítulo | `capitulo:metodologia` | C286, C287 |
### 5-metodologia.tex — 75 ocurrencias

| Ubicación | Nombre usado | Etiqueta | Relación con el TODO anterior |
| --- | --- | --- | --- |
| [22](/home/juanm4/Documentos/tesina/5-metodologia.tex:22) | subsección | `sec:metricas_evidencia` | Fuera |
| [24](/home/juanm4/Documentos/tesina/5-metodologia.tex:24) | subsección | `subsec:escenario_mendoza` | Fuera |
| [41](/home/juanm4/Documentos/tesina/5-metodologia.tex:41) | apéndice | `sec:parametros_sumo` | Fuera |
| [63](/home/juanm4/Documentos/tesina/5-metodologia.tex:63) | subsección | `subsec:ciclo_episodico` | Fuera |
| [81](/home/juanm4/Documentos/tesina/5-metodologia.tex:81) | apéndice | `subsec:detalles_redes_sinteticas` | Fuera |
| [108](/home/juanm4/Documentos/tesina/5-metodologia.tex:108) | subsección | `sec:stack_tecnologico` | Fuera |
| [136](/home/juanm4/Documentos/tesina/5-metodologia.tex:136) | apéndice | `subsec:detalles_redes_sinteticas` | Fuera |
| [143](/home/juanm4/Documentos/tesina/5-metodologia.tex:143) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [154](/home/juanm4/Documentos/tesina/5-metodologia.tex:154) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [161](/home/juanm4/Documentos/tesina/5-metodologia.tex:161) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [176](/home/juanm4/Documentos/tesina/5-metodologia.tex:176) | apéndice | `sec:parametros_sumo` | Fuera |
| [181](/home/juanm4/Documentos/tesina/5-metodologia.tex:181) | ecuación | `eq:factor_expansion_mendoza` | Fuera |
| [186](/home/juanm4/Documentos/tesina/5-metodologia.tex:186) | ecuación | `eq:demanda_red_horaria` | Fuera |
| [205](/home/juanm4/Documentos/tesina/5-metodologia.tex:205) | apéndice | `subsec:procedimiento_demanda_mendoza` | Fuera |
| [211](/home/juanm4/Documentos/tesina/5-metodologia.tex:211) | ecuación | `eq:intervalo_exponencial` | Fuera |
| [211](/home/juanm4/Documentos/tesina/5-metodologia.tex:211) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [218](/home/juanm4/Documentos/tesina/5-metodologia.tex:218) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [220](/home/juanm4/Documentos/tesina/5-metodologia.tex:220) | subsección | `sec:metricas_evidencia` | Fuera |
| [222](/home/juanm4/Documentos/tesina/5-metodologia.tex:222) | apéndice | `sec:parametros_sumo` | Fuera |
| [224](/home/juanm4/Documentos/tesina/5-metodologia.tex:224) | ecuación | `eq:geh` | Fuera |
| [233](/home/juanm4/Documentos/tesina/5-metodologia.tex:233) | apéndice | `sec:apendice_uml_entorno` | Fuera |
| [251](/home/juanm4/Documentos/tesina/5-metodologia.tex:251) | apéndice | `sec:apendice_uml_entorno` | Fuera |
| [253](/home/juanm4/Documentos/tesina/5-metodologia.tex:253) | ecuación | `eq:gae` | Fuera |
| [270](/home/juanm4/Documentos/tesina/5-metodologia.tex:270) | ecuación | `eq:observacion_local_metodologia` | Fuera |
| [276](/home/juanm4/Documentos/tesina/5-metodologia.tex:276) | apéndice | `subsec:calibraciones_cooperacion` | Fuera |
| [278](/home/juanm4/Documentos/tesina/5-metodologia.tex:278) | apéndice | `sec:parametros_sumo` | Fuera |
| [282](/home/juanm4/Documentos/tesina/5-metodologia.tex:282) | apéndice | `subsec:codificacion_espera_apendice` | Fuera |
| [289](/home/juanm4/Documentos/tesina/5-metodologia.tex:289) | subsección | `subsec:protocolo_urbano_mendoza` | Fuera |
| [306](/home/juanm4/Documentos/tesina/5-metodologia.tex:306) | apéndice | `subsec:mascara_acciones_apendice` | Fuera |
| [308](/home/juanm4/Documentos/tesina/5-metodologia.tex:308) | subsección | `subsec:ciclo_episodico` | Fuera |
| [315](/home/juanm4/Documentos/tesina/5-metodologia.tex:315) | ecuación | `eq:recompensa_local` | Fuera |
| [323](/home/juanm4/Documentos/tesina/5-metodologia.tex:323) | ecuación | `eq:recompensa_vecinal` | Fuera |
| [332](/home/juanm4/Documentos/tesina/5-metodologia.tex:332) | ecuación | `eq:recompensa_compuesta` | Fuera |
| [369](/home/juanm4/Documentos/tesina/5-metodologia.tex:369) | apéndice | `sec:apendice_detalles_aprendizaje` | Fuera |
| [369](/home/juanm4/Documentos/tesina/5-metodologia.tex:369) | sección | `subsec:happo` | Fuera |
| [371](/home/juanm4/Documentos/tesina/5-metodologia.tex:371) | ecuación | `eq:perdida_valor_marl_tlc` | Fuera |
| [393](/home/juanm4/Documentos/tesina/5-metodologia.tex:393) | apéndice | `subsec:protocolo_urbano_mendoza` | Fuera |
| [398](/home/juanm4/Documentos/tesina/5-metodologia.tex:398) | subsección | `subsubsec:mendoza_validacion_operacional` | Fuera |
| [417](/home/juanm4/Documentos/tesina/5-metodologia.tex:417) | apéndice | `subsec:calibraciones_cooperacion` | Fuera |
| [419](/home/juanm4/Documentos/tesina/5-metodologia.tex:419) | subsección | `subsec:seleccion_phase2` | Fuera |
| [427](/home/juanm4/Documentos/tesina/5-metodologia.tex:427) | subsección | `subsec:ciclo_episodico` | Fuera |
| [431](/home/juanm4/Documentos/tesina/5-metodologia.tex:431) | ecuación | `eq:objetivo_estable_espera` | Fuera |
| [453](/home/juanm4/Documentos/tesina/5-metodologia.tex:453) | apéndice | `subsec:espacio_busqueda_fase1` | Fuera |
| [459](/home/juanm4/Documentos/tesina/5-metodologia.tex:459) | subsección | `subsec:mecanismos_algoritmos` | Fuera |
| [464](/home/juanm4/Documentos/tesina/5-metodologia.tex:464) | apéndice | `subsec:dominios_refinados` | Fuera |
| [469](/home/juanm4/Documentos/tesina/5-metodologia.tex:469) | apéndice | `subsec:protocolo_refinado_apendice` | Fuera |
| [471](/home/juanm4/Documentos/tesina/5-metodologia.tex:471) | apéndice | `subsec:dominios_refinados` | Fuera |
| [473](/home/juanm4/Documentos/tesina/5-metodologia.tex:473) | apéndice | `subsec:dominios_refinados` | Fuera |
| [473](/home/juanm4/Documentos/tesina/5-metodologia.tex:473) | subsección | `subsec:protocolo_urbano_mendoza` | Fuera |
| [491](/home/juanm4/Documentos/tesina/5-metodologia.tex:491) | apéndice | `subsec:criterios_admisibilidad_hpo` | Fuera |
| [493](/home/juanm4/Documentos/tesina/5-metodologia.tex:493) | apéndice | `subsec:criterios_admisibilidad_hpo` | Fuera |
| [495](/home/juanm4/Documentos/tesina/5-metodologia.tex:495) | ecuación | `eq:tasa_completitud` | Fuera |
| [503](/home/juanm4/Documentos/tesina/5-metodologia.tex:503) | subsección | `subsec:protocolo_urbano_mendoza` | Fuera |
| [505](/home/juanm4/Documentos/tesina/5-metodologia.tex:505) | apéndice | `sec:parametros_sumo` | Fuera |
| [507](/home/juanm4/Documentos/tesina/5-metodologia.tex:507) | subsección | `sec:stack_tecnologico` | Fuera |
| [545](/home/juanm4/Documentos/tesina/5-metodologia.tex:545) | apéndice | `subsec:comprobaciones_preliminares` | Fuera |
| [550](/home/juanm4/Documentos/tesina/5-metodologia.tex:550) | apéndice | `subsec:receta_ac_apendice` | Fuera |
| [554](/home/juanm4/Documentos/tesina/5-metodologia.tex:554) | subsección | `sec:formulacion_dec_pomdp` | Fuera |
| [558](/home/juanm4/Documentos/tesina/5-metodologia.tex:558) | apéndice | `subsec:receta_ac_apendice` | Fuera |
| [560](/home/juanm4/Documentos/tesina/5-metodologia.tex:560) | subsección | `sec:evaluacion_variantes_mappo` | Fuera |
| [598](/home/juanm4/Documentos/tesina/5-metodologia.tex:598) | subsección | `subsec:escenario_mendoza` | Fuera |
| [605](/home/juanm4/Documentos/tesina/5-metodologia.tex:605) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [626](/home/juanm4/Documentos/tesina/5-metodologia.tex:626) | apéndice | `subsec:receta_ac_apendice` | Fuera |
| [635](/home/juanm4/Documentos/tesina/5-metodologia.tex:635) | ecuación | `eq:contrastes_pareados` | Fuera |
| [658](/home/juanm4/Documentos/tesina/5-metodologia.tex:658) | apéndice | `subsec:detalle_analisis_pareado` | Fuera |
| [671](/home/juanm4/Documentos/tesina/5-metodologia.tex:671) | ecuación | `eq:tasa_completitud` | Fuera |
| [678](/home/juanm4/Documentos/tesina/5-metodologia.tex:678) | subsección | `sec:metricas_evidencia` | Fuera |
| [680](/home/juanm4/Documentos/tesina/5-metodologia.tex:680) | apéndice | `subsec:detalle_analisis_pareado` | Fuera |
| [697](/home/juanm4/Documentos/tesina/5-metodologia.tex:697) | apéndice | `sec:procedencia_mendoza` | Fuera |
| [697](/home/juanm4/Documentos/tesina/5-metodologia.tex:697) | subsección | `subsec:seleccion_mendoza` | Fuera |
| [712](/home/juanm4/Documentos/tesina/5-metodologia.tex:712) | apéndice | `sec:apendice_reproduccion` | Fuera |
| [712](/home/juanm4/Documentos/tesina/5-metodologia.tex:712) | subsección | `subsec:escenario_mendoza` | Fuera |
| [719](/home/juanm4/Documentos/tesina/5-metodologia.tex:719) | apéndice | `sec:infraestructura_apendice` | Fuera |
| [728](/home/juanm4/Documentos/tesina/5-metodologia.tex:728) | apéndice | `sec:apendice_detalles_aprendizaje` | Fuera |
| [730](/home/juanm4/Documentos/tesina/5-metodologia.tex:730) | subsección | `subsec:escenario_mendoza` | Fuera |
### 6-resultados.tex — 4 ocurrencias

| Ubicación | Nombre usado | Etiqueta | Relación con el TODO anterior |
| --- | --- | --- | --- |
| [19](/home/juanm4/Documentos/tesina/6-resultados.tex:19) | sección | `sec:experimentos_evaluacion` | Fuera |
| [27](/home/juanm4/Documentos/tesina/6-resultados.tex:27) | sección | `subsubsec:mendoza_validacion_operacional` | Fuera |
| [27](/home/juanm4/Documentos/tesina/6-resultados.tex:27) | sección | `sec:procedencia_mendoza` | Fuera |
| [45](/home/juanm4/Documentos/tesina/6-resultados.tex:45) | apéndice | `sec:procedencia_mendoza` | Fuera |
### 8-apendice_arquitectura.tex — 21 ocurrencias

| Ubicación | Nombre usado | Etiqueta | Relación con el TODO anterior |
| --- | --- | --- | --- |
| [278](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:278) | subsección | `subsec:protocolo_urbano_mendoza` | Fuera |
| [297](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:297) | subsección | `subsec:procedimiento_demanda_mendoza` | Fuera |
| [381](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:381) | subsección | `subsec:infraestructura_hpc` | Fuera |
| [396](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:396) | subsección | `subsec:screening_vecinal` | Fuera |
| [414](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:414) | subsección | `subsec:protocolo_urbano_mendoza` | Fuera |
| [416](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:416) | sección | `subsec:hpo_phase1` | Fuera |
| [418](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:418) | sección | `sec:apendice_detalles_aprendizaje` | Fuera |
| [561](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:561) | subsección | `subsec:criterios_admisibilidad_hpo` | Fuera |
| [596](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:596) | subsección | `subsec:seleccion_mendoza` | Fuera |
| [603](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:603) | subsección | `sec:evaluacion_modelos_finales` | Fuera |
| [652](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:652) | subsección | `subsec:seleccion_mendoza` | Fuera |
| [652](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:652) | subsección | `sec:stack_tecnologico` | Fuera |
| [656](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:656) | subsección | `subsec:hpo_phase1` | Fuera |
| [660](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:660) | subsección | `subsec:protocolo_refinado_apendice` | Fuera |
| [662](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:662) | subsección | `subsec:dominios_refinados` | Fuera |
| [695](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:695) | subsección | `subsec:mecanismos_algoritmos` | Fuera |
| [723](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:723) | sección | `subsec:observaciones_encoder` | Fuera |
| [727](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:727) | sección | `subsec:observaciones_encoder` | Fuera |
| [732](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:732) | ecuación | `eq:encoder_mezcla_convexa` | Fuera |
| [732](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:732) | ecuación | `eq:encoder_saturacion` | Fuera |
| [754](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:754) | ecuación | `eq:recompensa_compuesta` | Fuera |

## Inventario B. Referencias a secciones internas denominadas «apéndice»

Estas 40 filas son un subconjunto del inventario A. El destino existe; se propone ajustar el nombre de la unidad, conservando su enlace. La columna de destino enlaza la declaración de la etiqueta y registra su nivel real en la fuente. La forma habitual de corrección es «Sección \ref{etiqueta} del Apéndice \ref{apendice:arquitectura_software}», abreviada si el contexto ya identifica el apéndice.

| Origen | Etiqueta de destino | Tipo estructural y ubicación real |
| --- | --- | --- |
| [5-metodologia.tex:41](/home/juanm4/Documentos/tesina/5-metodologia.tex:41) | `sec:parametros_sumo` | section, [8-apendice_arquitectura.tex:243](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:243) |
| [5-metodologia.tex:81](/home/juanm4/Documentos/tesina/5-metodologia.tex:81) | `subsec:detalles_redes_sinteticas` | subsection, [8-apendice_arquitectura.tex:399](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:399) |
| [5-metodologia.tex:136](/home/juanm4/Documentos/tesina/5-metodologia.tex:136) | `subsec:detalles_redes_sinteticas` | subsection, [8-apendice_arquitectura.tex:399](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:399) |
| [5-metodologia.tex:143](/home/juanm4/Documentos/tesina/5-metodologia.tex:143) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:154](/home/juanm4/Documentos/tesina/5-metodologia.tex:154) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:161](/home/juanm4/Documentos/tesina/5-metodologia.tex:161) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:176](/home/juanm4/Documentos/tesina/5-metodologia.tex:176) | `sec:parametros_sumo` | section, [8-apendice_arquitectura.tex:243](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:243) |
| [5-metodologia.tex:205](/home/juanm4/Documentos/tesina/5-metodologia.tex:205) | `subsec:procedimiento_demanda_mendoza` | subsubsection, [8-apendice_arquitectura.tex:333](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:333) |
| [5-metodologia.tex:211](/home/juanm4/Documentos/tesina/5-metodologia.tex:211) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:218](/home/juanm4/Documentos/tesina/5-metodologia.tex:218) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:222](/home/juanm4/Documentos/tesina/5-metodologia.tex:222) | `sec:parametros_sumo` | section, [8-apendice_arquitectura.tex:243](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:243) |
| [5-metodologia.tex:233](/home/juanm4/Documentos/tesina/5-metodologia.tex:233) | `sec:apendice_uml_entorno` | section, [8-apendice_arquitectura.tex:7](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:7) |
| [5-metodologia.tex:251](/home/juanm4/Documentos/tesina/5-metodologia.tex:251) | `sec:apendice_uml_entorno` | section, [8-apendice_arquitectura.tex:7](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:7) |
| [5-metodologia.tex:276](/home/juanm4/Documentos/tesina/5-metodologia.tex:276) | `subsec:calibraciones_cooperacion` | subsection, [8-apendice_arquitectura.tex:791](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:791) |
| [5-metodologia.tex:278](/home/juanm4/Documentos/tesina/5-metodologia.tex:278) | `sec:parametros_sumo` | section, [8-apendice_arquitectura.tex:243](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:243) |
| [5-metodologia.tex:282](/home/juanm4/Documentos/tesina/5-metodologia.tex:282) | `subsec:codificacion_espera_apendice` | subsection, [8-apendice_arquitectura.tex:709](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:709) |
| [5-metodologia.tex:306](/home/juanm4/Documentos/tesina/5-metodologia.tex:306) | `subsec:mascara_acciones_apendice` | subsection, [8-apendice_arquitectura.tex:742](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:742) |
| [5-metodologia.tex:369](/home/juanm4/Documentos/tesina/5-metodologia.tex:369) | `sec:apendice_detalles_aprendizaje` | section, [8-apendice_arquitectura.tex:686](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:686) |
| [5-metodologia.tex:393](/home/juanm4/Documentos/tesina/5-metodologia.tex:393) | `subsec:protocolo_urbano_mendoza` | subsection, [8-apendice_arquitectura.tex:648](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:648) |
| [5-metodologia.tex:417](/home/juanm4/Documentos/tesina/5-metodologia.tex:417) | `subsec:calibraciones_cooperacion` | subsection, [8-apendice_arquitectura.tex:791](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:791) |
| [5-metodologia.tex:453](/home/juanm4/Documentos/tesina/5-metodologia.tex:453) | `subsec:espacio_busqueda_fase1` | subsection, [8-apendice_arquitectura.tex:412](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:412) |
| [5-metodologia.tex:464](/home/juanm4/Documentos/tesina/5-metodologia.tex:464) | `subsec:dominios_refinados` | subsection, [8-apendice_arquitectura.tex:608](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:608) |
| [5-metodologia.tex:469](/home/juanm4/Documentos/tesina/5-metodologia.tex:469) | `subsec:protocolo_refinado_apendice` | subsection, [8-apendice_arquitectura.tex:553](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:553) |
| [5-metodologia.tex:471](/home/juanm4/Documentos/tesina/5-metodologia.tex:471) | `subsec:dominios_refinados` | subsection, [8-apendice_arquitectura.tex:608](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:608) |
| [5-metodologia.tex:473](/home/juanm4/Documentos/tesina/5-metodologia.tex:473) | `subsec:dominios_refinados` | subsection, [8-apendice_arquitectura.tex:608](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:608) |
| [5-metodologia.tex:491](/home/juanm4/Documentos/tesina/5-metodologia.tex:491) | `subsec:criterios_admisibilidad_hpo` | subsubsection, [8-apendice_arquitectura.tex:592](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:592) |
| [5-metodologia.tex:493](/home/juanm4/Documentos/tesina/5-metodologia.tex:493) | `subsec:criterios_admisibilidad_hpo` | subsubsection, [8-apendice_arquitectura.tex:592](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:592) |
| [5-metodologia.tex:505](/home/juanm4/Documentos/tesina/5-metodologia.tex:505) | `sec:parametros_sumo` | section, [8-apendice_arquitectura.tex:243](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:243) |
| [5-metodologia.tex:545](/home/juanm4/Documentos/tesina/5-metodologia.tex:545) | `subsec:comprobaciones_preliminares` | subsection, [8-apendice_arquitectura.tex:392](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:392) |
| [5-metodologia.tex:550](/home/juanm4/Documentos/tesina/5-metodologia.tex:550) | `subsec:receta_ac_apendice` | subsection, [8-apendice_arquitectura.tex:757](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:757) |
| [5-metodologia.tex:558](/home/juanm4/Documentos/tesina/5-metodologia.tex:558) | `subsec:receta_ac_apendice` | subsection, [8-apendice_arquitectura.tex:757](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:757) |
| [5-metodologia.tex:605](/home/juanm4/Documentos/tesina/5-metodologia.tex:605) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:626](/home/juanm4/Documentos/tesina/5-metodologia.tex:626) | `subsec:receta_ac_apendice` | subsection, [8-apendice_arquitectura.tex:757](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:757) |
| [5-metodologia.tex:658](/home/juanm4/Documentos/tesina/5-metodologia.tex:658) | `subsec:detalle_analisis_pareado` | subsection, [8-apendice_arquitectura.tex:675](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:675) |
| [5-metodologia.tex:680](/home/juanm4/Documentos/tesina/5-metodologia.tex:680) | `subsec:detalle_analisis_pareado` | subsection, [8-apendice_arquitectura.tex:675](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:675) |
| [5-metodologia.tex:697](/home/juanm4/Documentos/tesina/5-metodologia.tex:697) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |
| [5-metodologia.tex:712](/home/juanm4/Documentos/tesina/5-metodologia.tex:712) | `sec:apendice_reproduccion` | section, [8-apendice_arquitectura.tex:374](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:374) |
| [5-metodologia.tex:719](/home/juanm4/Documentos/tesina/5-metodologia.tex:719) | `sec:infraestructura_apendice` | subsection, [8-apendice_arquitectura.tex:379](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:379) |
| [5-metodologia.tex:728](/home/juanm4/Documentos/tesina/5-metodologia.tex:728) | `sec:apendice_detalles_aprendizaje` | section, [8-apendice_arquitectura.tex:686](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:686) |
| [6-resultados.tex:45](/home/juanm4/Documentos/tesina/6-resultados.tex:45) | `sec:procedencia_mendoza` | subsection, [8-apendice_arquitectura.tex:274](/home/juanm4/Documentos/tesina/8-apendice_arquitectura.tex:274) |

## Orden de corrección recomendado

1. Resolver la estructura pendiente de resultados/conclusiones y el alcance de sus anuncios, sin inventar datos. En paralelo, decidir la organización de las explicaciones de figuras UML y del flujo metodológico.
2. Resolver las remisiones y los referentes: contenido atribuido a cada destino, nombres de objetos, cantidades y contraste teoría/implementación. Verificar las fuentes que se necesitan para las decisiones técnicas pendientes.
3. Aplicar la convención de siglas, términos y enlaces semánticos al cuerpo y a sus epígrafes. Conservar los identificadores del código y coordinar con las entradas existentes.
4. Aplicar mayúsculas/plurales y el criterio de cifras a las ocurrencias inventariadas. Estos cambios no sustituyen las decisiones estructurales ni deben hacerse sobre código con reemplazos indiscriminados.
5. Compilar y revisar las páginas afectadas y sus referencias. Si hubo cambios de glosario, completar el ciclo indicado en AGENTS.md. Cerrar cada ficha con evidencia de la comprobación que corresponda; no asumir que la generación de este informe corrige el manuscrito.

## Verificación de esta entrega

- Las reglas R01–R26 tienen origen identificado, alcance, criterio de aplicación y excepciones; AGENTS.md exige su lectura para las próximas modificaciones editoriales.
- Las 34 fichas H tienen reglas asociadas y citas breves comprobadas contra la línea indicada de una fuente local. Se preserva el significado de los estados: 21 confirmados, 11 decisiones editoriales y 2 verificaciones pendientes.
- Los recuentos 136/102/40/4 se contrastaron con los inventarios y el CSV. Las intersecciones están declaradas; no se suma el conjunto de 40 como si fueran referencias nuevas adicionales.
- Los archivos de fuentes, glosario, bibliografía y PDF se comprobaron por SHA-256 antes y después del trabajo para verificar que no cambiaron. No se ejecutaron cambios editoriales en el manuscrito ni una compilación nueva.

Inventario de comentarios utilizado: SHA-256 `16dcb5cdcb7830666714c30b4e312326374efafc101c87e70907f550aa5629f4`. El archivo de reglas es normativo para el flujo del proyecto; este diagnóstico es fechado y debe revalidarse después de las correcciones.
