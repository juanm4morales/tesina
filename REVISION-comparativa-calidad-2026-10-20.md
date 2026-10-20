# Revisión comparativa de calidad de la tesina

Fecha: 20 de octubre de 2026. Estado evaluado: `cbfc94d`, antes de las correcciones de esta revisión. Período: commits del 18 al 20 de octubre; no hay commits del 17 en el historial examinado. Referencia anterior al período: `6f5a95f`, del 15 de octubre.

**Dictamen:** no se puede sostener que cada cambio haya sido para mejor ni que el último commit supere a todos sus antecesores en todos los criterios. La organización general y varias figuras mejoraron. Algunas condensaciones eliminaron información necesaria y algunas reformulaciones introdujeron errores. En varios pasajes, la versión anterior a la refactorización del 20 de octubre resulta más clara y natural.

La base actual es aprovechable. La solución consiste en conservar su organización, recuperar las precisiones necesarias y acortar los pasajes que concentran demasiadas funciones. Una reversión completa también perdería mejoras comprobables.

**Qué se examinó y cómo se justifican los juicios**

Se leyó la metodología y el apéndice completos en el estado evaluado, sus cambios con respecto al estado anterior al período y las modificaciones intermedias de los commits sustantivos. Se contrastaron también resumen, abstract, introducción, pasajes modificados del marco teórico, resultados, glosarios, referencias bibliográficas locales y fuentes de las figuras y tablas pertinentes. Las conclusiones se leyeron para comprobar el alcance realmente desarrollado: siguen siendo un párrafo introductorio.

Se extrajo el texto de siete PDF versionados (`6f5a95f`, `69e5e97`, `548ac97`, `c689959`, `b05da77`, `b5c4683`, `cbfc94d`). Se inspeccionaron visualmente 23 páginas seleccionadas del PDF final, más las tablas A.2 y de dominios a mayor resolución y una tabla anterior en horizontal. La lectura visual fue una muestra dirigida a los cambios; no una inspección de todas las páginas de todos los PDF.

Los juicios distinguen tres situaciones: mejora verificable, resultado mixto y cambio que necesita corrección. Una sustitución es un retroceso cuando cambia el método declarado, elimina una condición necesaria o remite a una explicación ausente. La naturalidad requiere juicio editorial: se evalúan la claridad de los sujetos, la longitud y carga de las oraciones, las repeticiones y las expresiones formularias. Estas características no permiten determinar quién escribió el texto ni demostrar autoría humana o por IA.

**Balance según los seis criterios solicitados**

| Criterio | Evaluación del último commit | Justificación |
|---|---|---|
| Ayuda al lector a comprender | Mejora de estructura; retrocesos locales | Se distinguen mejor las líneas sintética y urbana, y varias figuras hacen visibles decisiones operacionales. Se pierden explicaciones de casos de borde y aparecen remisiones semánticamente desactualizadas. |
| Calidad de redacción | Mixta | Hay títulos y transiciones más informativos, pero también párrafos con muchas subordinadas y sustituciones que vuelven menos directo el texto. |
| Formatos, estilos, cursivas y siglas | Mejora parcial | Se incorpora un estilo gráfico común y se corrigen cursivas de desarrollos ingleses. Persisten variaciones en la notación de redes, identificadores, números y tamaños efectivos de las tablas. Hay duplicaciones causadas por expansiones de siglas. |
| Apéndice más útil y simple | Mejora en selección y navegación; simplificación excesiva en algunos puntos | Se acorta la lista de patrones y se retiran protocolos urbanos que podían confundirse con trabajo ejecutado. La reducción también elimina procedencia y convenciones necesarias. |
| Ausencia de repeticiones innecesarias | Mejora incompleta | Se retiran explicaciones repetidas alrededor de figuras y antecedentes voluminosos. Todavía se repiten las reglas de refinamiento, la delimitación urbana y el alcance conjunto del contraste A/C. |
| Naturalidad de redacción | No hay una mejora uniforme | Varios pasajes anteriores usan sujetos y verbos más directos. La refactorización introduce expresiones como «con el propósito de», «formalmente planteada», «confirma cuantitativamente» y largas enumeraciones dentro de una misma oración. |

La longitud bajó, pero eso no demuestra por sí solo mayor calidad. El PDF pasó de 162 páginas antes del período a 153 en el último commit. El máximo intermedio fue de 170 páginas. El apéndice ocupaba 31 páginas antes del período, 41 en `b05da77` y 29 en `cbfc94d`, contando desde su portada hasta antes de la bibliografía. La metodología pasó de 730 a 547 líneas de fuente entre el comienzo y el final del período; el apéndice, de 799 a 774. Son medidas de extensión, no puntuaciones de calidad.

**Evaluación de todos los commits del período**

| Commit | Cambio | Juicio y fundamento |
|---|---|---|
| `69e5e97` | Revisión según Caro | Mayormente favorable. Aclara qué representa la espera, explica mejor las figuras y distingue la adaptación de HAPPO de su formulación teórica. Acortar pies y trasladar explicaciones al cuerpo evita repetirlas. No resuelve todas las inconsistencias del documento. |
| `548ac97` | Rediseño de figuras | Favorable en conjunto. Los paneles permiten comparar topologías; las líneas temporales de transición y pertenencia al conjunto evaluado aclaran reglas difíciles de seguir solo con prosa. La figura de actores se concentra en MAPPO/HAPPO, por lo que su nuevo alcance debe quedar explícito. |
| `133cd6d` | Dejar de versionar Markdown | No es una mejora de la lectura de la tesina. Afecta el mantenimiento de informes y reglas editoriales. El historial conserva los archivos anteriores, pero los informes nuevos dejan de incorporarse por defecto. |
| `3f28c01` | Composición y procedencia de demanda | Favorable en conjunto. Permite una colocación más flexible de figuras y precisa el carácter parcial de los conteos. Los cambios de colocación no aseguran por sí solos que cada figura quede junto a su explicación. |
| `c689959` | PDF y vistas v17–v19 | Actualización y respaldo de revisión. No añade por sí mismo una mejora textual independiente; incorpora al artefacto las modificaciones anteriores. |
| `3b1e4b1` | Auditorías CSV locales | Cambio de mantenimiento sin efecto directo en el PDF. No se cuenta como mejora de redacción ni de rigor de la tesina. |
| `ce70f15` | Escenario O2/P2 y claridad metodológica | Favorable con costo de extensión. Incorpora evidencia por semilla, separa solicitudes y viajes atendidos y delimita el aprendizaje urbano. El apéndice crece porque conserva muchas etapas históricas; parte de esa historia podía resumirse. |
| `b05da77` | PDF y verificación editorial | Registra el estado anterior a la gran condensación. Es útil como referencia de precisiones posteriormente eliminadas. Sus comprobaciones corresponden a ese PDF, no automáticamente al último. |
| `8273ea3` | Refactorización de metodología | Mixto. Mejora la organización y reduce extensión, pero elimina limitaciones de la señal de espera, reglas para datos incompletos y detalles del alcance inferencial. También introduce párrafos más densos y una descripción de la figura de flujo que anticipa una etapa urbana ausente del dibujo. |
| `19c5984` | Depuración del apéndice y tablas verticales | Mixto. Simplifica la enumeración de patrones y evita girar páginas. A cambio, reduce y vuelve variable el tamaño del texto de las tablas, retira explicaciones útiles y elimina la distinción entre magnitudes físicas y valores numéricos del codificador. |
| `b5c4683` | Actualización del PDF | Actualización del artefacto, sin mejora textual independiente. Refleja también los problemas de las dos refactorizaciones anteriores. |
| `eeed4eb` | Corrección del protocolo refactorizado | Favorable y necesario. Corrige la regla del 10 %, los conjuntos de diez y veinte ensayos, recupera limitaciones y precisa la interpretación de colisiones y recompensas. La descripción exacta del refinamiento sigue duplicada entre cuerpo y apéndice. |
| `5640dcc` | Makefile | Mejora operativa: deja una receta explícita de compilación. No acredita calidad de prosa. Su objetivo `check` informa conteos y no constituye por sí solo una validación editorial completa. |
| `da7888f` | Condensación del aprendizaje urbano | Mixto. Retirar el protocolo antiguo de selección simplifica el apéndice y evita confundirlo con O2/P2. Sin embargo, introduce una afirmación de que el ciclo sintético completo se terminó, que el capítulo de resultados todavía no respalda, y deja una alusión a la «excepción urbana» sin explicación. |
| `8feeaf2` | Eliminación de etiqueta huérfana | Limpieza correcta y de efecto mínimo. Evita conservar un identificador sin función; no cambia la experiencia de lectura por sí sola. |
| `cbfc94d` | Unificación de P2 y retiro de antecedentes | Mixto, con un error conceptual. La tabla A.2 pasa a describir el plan vigente y sus agrupaciones concuerdan con el CSV. La sustitución de duraciones observadas por «demanda relativa» cambia el método declarado; también se debilitan la procedencia de O1 y la identificación de la calibración urbana anterior. |

**Problemas comprobados y correcciones de esta revisión**

1. **El reparto de verdes cambió de significado. Corregido.**

En `cbfc94d`, la metodología y el apéndice sustituyen las duraciones medias observadas por «demanda relativa». El diff conserva la misma ecuación y no incorpora un nuevo procedimiento que justifique reinterpretar su variable. La aclaración del usuario confirma que se usaron duraciones empíricas de una simulación base.

Se restituyó esa definición en ambos lugares. La metodología resume el procedimiento y el apéndice conserva la fórmula y el rango de 121 a 373 ciclos completos observados por controlador. Se describe la calibración sensible al tránsito sin recuperar la historia de los controladores anteriores. Se mantuvieron el plan final P2 y sus tablas. También se reemplazó «se optimizaron» por «se ajustaron» al describir los desfases, para expresar la operación sin atribuir una demostración de optimalidad.

2. **La diferencia entre la señal local y la espera del viaje perdió parte de su explicación. Corregido.**

La distinción no había desaparecido: el último commit todavía mencionaba la memoria finita en la metodología y los 1.000 s en el apéndice. Lo eliminado era la explicación de cómo esa memoria y las atribuciones por carril afectan la señal, incluida una limitación de la versión conservada para A/C.

Se reunieron en el apartado de observaciones la ventana de 1.000 s, el descuento de atribuciones previas y el posible sesgo al vencer la memoria. Se explicó por qué una reducción local puede coincidir con cambios de carril, salida de vehículos o vencimiento de la ventana, sin demostrar menor espera por viaje. La definición de `TripInfo.waitingTime` permanece en ese mismo contexto.

3. **Las reglas para datos incompletos y casos de borde se habían recortado. Corregido.**

Se recuperaron la censura a la derecha de viajes inconclusos, la indefinición de las métricas de viaje con conjunto vacío y de los cocientes con denominador cero, y la convención de Gini cero si todas las medias son nulas. Para el contraste pareado, una referencia de espera cero conserva la diferencia absoluta y deja indefinido el efecto relativo; no habilita la decisión basada en este último.

También se restituyeron los requisitos de pares y evaluaciones completos, la imposibilidad de una decisión favorable con métricas o contadores ausentes y las reglas de los resúmenes de veinte evaluaciones. Los intentos fallidos y cierres anticipados deben permanecer registrados.

No se cambiaron los umbrales estadísticos. Se recuperó una limitación de interpretación: el criterio A/C no impone un volumen mínimo de inserciones ni incluye el retraso externo. Por ejemplo, una variante podría atender menos vehículos y aun conservar una alta completitud entre los que sí ingresan. El propio protocolo anterior explicitaba esta diferencia.

4. **Las expansiones de siglas producían repeticiones locales. Corregido; la hipótesis general necesita matizarse.**

El PDF decía «el estimador estimador de Parzen…» y «una búsqueda en anchura (búsqueda en anchura…)». En el caso de ASHA, se acumulaban «planificador asíncrono» y su desarrollo completo. Se corrigieron las construcciones que rodeaban a las macros, conservando la presentación completa de las siglas.

La búsqueda de apariciones mostró que las llamadas a `\acrfull` eran, en general, la primera presentación de esas siglas en el cuerpo principal. No corresponde sustituirlas indiscriminadamente por `\acrshort`. Presentar las siglas de los algoritmos en el resumen y en el abstract es razonable porque son textos autónomos. También se sustituyó la escritura manual de OD por su macro en un pasaje del apéndice y se retiraron los acentos graves de Markdown que rodeaban a TAZ 28 en el fuente LaTeX.

5. **Había destinos existentes que ya no contenían lo prometido. Corregido.**

El apéndice remitía a la fase 1 para las definiciones de uniforme y loguniforme, eliminadas de ese apartado. Ahora las define donde se consultan las tablas y retira la alusión residual a una excepción urbana ya purgada. Resultados remitía a la metodología para una explicación histórica de la exclusión de 3×3 que ahora está en el apéndice: se corrigió el destino.

La descripción de la figura de flujo decía que mostraba la extensión urbana, aunque no existe ese bloque en el dibujo. Se eliminó esa anticipación. Esto ilustra por qué una compilación sin referencias indefinidas no basta: el enlace puede existir y conducir a un contenido que no cumple la promesa del párrafo.

6. **Una leyenda generalizaba el comportamiento de todas las recompensas. Corregido.**

La leyenda del diagrama de recompensas afirmaba que las subclases combinaban la señal local y la vecinal. La propia explicación identifica una clase local y otra que promedia vecinos. Se precisó que la composición corresponde a `NeighborhoodRelevanceReward`.

7. **La simplificación del codificador borró una convención matemática necesaria. Corregido.**

Antes se distinguían la magnitud física y su valor numérico en veh·s. Después se escribía `L=(I−1)/M_lane`, se lo utilizaba en `1−L` y se afirmaba `0<L<1` bajo condiciones insuficientes: `M_lane>0` e `I≥2` no bastan.

Se aclaró que las ecuaciones usan valores numéricos expresados en veh·s y que los dominios utilizados cumplen `M_lane>I−1`. Se conservaron las ecuaciones y la notación compacta. El problema era de exposición matemática; esta revisión no demuestra un error en las ejecuciones del codificador.

8. **El valor 5.396 perdió su procedencia. Corregido.**

Tras retirar la referencia a v14, el párrafo podía leerse como una calibración de O2/P2. Se recuperaron la identificación de la versión previa, las semillas, el calentamiento, el control y el archivo de respaldo. Se indicó expresamente que debe recalibrarse para usarlo en el escenario vigente. Se retiró la conclusión excesiva de que ese único resultado «confirma cuantitativamente» las necesidades presupuestarias urbanas.

**Otros hallazgos de la comparación y su estado**

9. **La regla detallada de refinamiento se explica dos veces.**

La metodología describe diez y veinte mejores ensayos, expansión del 10 %, cobertura del 70 % y distancia del 5 % a los bordes. El apéndice vuelve a desarrollar esas reglas y añade los casos loguniforme, entero y categórico. La primera explicación debe limitarse al propósito y al recorrido del procedimiento, con una remisión al desarrollo exacto del apéndice. Conservar ambas versiones detalladas aumenta la carga de lectura y el riesgo de que una futura corrección alcance solo a una.

10. **Algunas oraciones se volvieron más difíciles después de la refactorización.**

En el estado evaluado, el párrafo de refinamiento tenía 171 elementos separados por espacios en una sola línea de fuente y varias condiciones anidadas. El de limitaciones urbanas tenía 210 y enlazaba selección adaptativa, semillas reutilizadas, falta de comparación completa, márgenes acumulados, horizonte finito, pendientes y objetivo de búsqueda. Estos conteos incluyen notación LaTeX: sirven para localizar carga textual, no como una medición exacta de palabras del PDF.

El problema es la cantidad de asuntos que el lector debe retener. La solución es asignar un párrafo a cada decisión o límite y retirar del cuerpo las reglas ya documentadas en detalle. Reemplazar «el diseño contempla dos líneas» por «dos líneas metodológicas complementarias» tampoco mejora por sí solo la información.

La expresión «discreción del reloj» era una imprecisión léxica introducida por la refactorización; se corrigió a «discretización». El mínimo de verde se describe ahora como configurado, sin atribuirle una verificación reglamentaria que el documento no presenta.

11. **La delimitación del alcance se repite en la introducción.**

Los párrafos de presentación del escenario, objetivo general y organización del documento vuelven a explicar que el aprendizaje urbano requiere adaptación y que la comprobación fija no evalúa políticas aprendidas. Conviene definir el alcance una vez en la presentación de los objetivos y dejar una remisión breve al describir la estructura del documento.

La repetición entre resumen, abstract y cuerpo sí cumple una función: deben poder leerse por separado. Tampoco toda repetición entre metodología y resultados sobra: el lector necesita saber qué protocolo produjo una tabla. El recorte debe dirigirse a las explicaciones completas que se repiten sin añadir información.

12. **La procedencia de O1 quedó demasiado abreviada.**

La versión anterior describía reescalados e intercambios heurísticos. El último commit los reemplaza por «asignación horaria y balance espacial», sin explicar cómo se obtuvieron las tasas intermedias. La tabla todavía distingue O1 reescalada y O2, y las limitaciones aluden a una redistribución anterior y a márgenes acumulados.

No hace falta recuperar las tablas históricas ni todos los nombres de versiones. Sí hace falta una explicación breve que conecte la asignación de partida, la redistribución heurística y el intercambio final. El archivo `matrices_od_completas.csv` y el registro histórico ayudan a conservar evidencia, pero no sustituyen esa conexión para el lector.

13. **El apéndice declaraba una finalización que los resultados todavía no documentan. Corregido en la redacción.**

La subsección de aprendizaje urbano comienza afirmando que en las redes sintéticas «se completó el ciclo íntegro» de búsqueda, selección y evaluación de los cuatro algoritmos. La metodología presenta parte de ese recorrido como protocolo y el capítulo de resultados mantiene vacíos sus apartados sintéticos. El capítulo de conclusiones tampoco desarrolla hallazgos.

Esto no demuestra que los experimentos no existan; demuestra que la afirmación no está respaldada dentro de la tesina actual. La redacción se cambió a «se especifica un protocolo», que describe lo efectivamente presentado sin atribuir resultados ausentes. La evaluación final se enuncia también como protocolo previsto. Sigue pendiente incorporar la evidencia de ejecución y sus resultados cuando estén disponibles.

14. **Las tablas verticales ahorran giros, con una pérdida de uniformidad tipográfica.**

El cambio de orientación facilita leer el apéndice seguido. Sin embargo, `\adjustbox{max width=\linewidth}` reduce el tamaño según el ancho de cada tabla. El PDF muestra cuerpos efectivos diferentes entre HAPPO, IDQN, IPPO y MAPPO. El texto de la tabla horizontal anterior era mayor.

La conversión conserva todos los números: es una mejora de navegación con un costo de legibilidad. Para resolverlo, conviene redistribuir encabezados o dividir la presentación antes de escalar cada tabla de manera distinta. No se debe considerar automáticamente mejor por ocupar menos páginas.

15. **Quedan convenciones de formato sin unificar.**

La red heterogénea aparece como `4\times4\_H` en la prosa y como `4\times4_{\mathrm{H}}` en encabezados. Las etiquetas h128/h256 y O2/P2 alternan entre texto normal y monoespaciado. Los valores 1184 y 1.184 también alternan entre tablas y cuerpo. Los encabezados de algunas tablas usan negrita y los de otras solo fondo azul.

Ninguna de estas variaciones demuestra un error científico. Sí impiden calificar el formato como completamente coherente. Conviene fijar una convención por clase de elemento y aplicarla en los lugares que el lector compara.

16. **Hay una inconsistencia de arquitectura anterior al período que la revisión de tablas no resolvió.**

La tabla de arquitecturas y semillas asigna h256 a HAPPO en 4×4 heterogénea, mientras que el encabezado de su tabla de dominios declara h128. La discrepancia ya estaba antes de los tres días evaluados; no la introdujo la conversión a vertical. Debe comprobarse contra la configuración efectiva antes de corregir uno de los dos valores. Su persistencia limita la afirmación de que el apéndice ya es plenamente coherente.

**Qué conviene conservar**

- La separación del escenario urbano operativo y las campañas de aprendizaje sintéticas.
- La tabla A.2 del plan P2 vigente: se contrastaron sus cantidades y rangos de verde con los 73 programas del CSV. Las agrupaciones suman 73 y concuerdan con los datos.
- Los diagramas de transición, vehículos evaluados y contraste A/C: aportan ejemplos que complementan las definiciones.
- La lista breve de patrones de diseño y las referencias a tablas completas de programas.
- La separación entre solicitudes esperadas, cargados, insertados y viajes completados en resultados.
- Las correcciones de `eeed4eb` que recuperan las reglas exactas y limitaciones del protocolo.

**Comprobaciones y límites**

El recorrido estático inicial reunió 34 fuentes TeX, 216 etiquetas y 229 usos de referencias: no encontró etiquetas duplicadas, referencias sin destino, citas sin entrada ni claves bibliográficas duplicadas. Los problemas semánticos de remisión descritos arriba existen a pesar de ese resultado correcto.

Los JSON de revisión editorial conservados en `datos/mendoza220k` identifican un PDF de 170 páginas con SHA-256 `07ac508981f5030d9df1a7f9d7599bf74cbea7970853929a6ce59424f116839e`. El PDF de `cbfc94d` tiene 153 páginas y SHA-256 `87f59ff31db37c02085fbc8ec888d79e0f180ee9b7178a2e379ada91fdd2aecb`. Esos registros históricos no deben presentarse como una comprobación del último artefacto.

Las correcciones se aplicaron a los fuentes durante esta revisión, siguiendo las indicaciones del usuario. El juicio sobre los commits de la tabla corresponde a sus estados originales; no se reescribió el historial. La comprobación de compilación del estado corregido se informa al entregar el trabajo.

No se repitieron simulaciones ni entrenamientos, no se verificaron externamente los artículos citados y no se auditó el código experimental de otro repositorio. Se buscó la documentación de semillas en la copia local de `marl-tlc`. La revisión demuestra problemas y mejoras documentales concretos; no certifica por sí sola la validez de los resultados experimentales.

17. **La notación residual estaba en la figura de componentes. Corregido.**

`metodologia_v2_encoder.tex` ya rotulaba el límite como `M_lane`. La referencia residual a `M_num` estaba en `metodologia_v2_componentes_encoder.tex` y en su generador, `metodologia_v2_generar_encoder.py`. La figura definía su relación de unidades, pero esa variable auxiliar dejó de corresponderse con la notación del texto condensado.

Se unificó la anotación con `M_lane`, se hizo explícito el uso de valores numéricos en veh·s y se regeneró la figura de componentes. Se comprobó que el fuente generado de la curva principal permaneciera idéntico. No se alteraron los cálculos ni los parámetros ilustrativos.

18. **Falta la lista efectiva de semillas finales. Pendiente de una fuente verificable.**

La exclusividad declarada literalmente en el texto corresponde a las tres semillas de selección, 950001, 950003 y 950007. La evaluación final prevé veinte semillas nuevas por combinación sintética, hasta 240 episodios; no declara un único panel global de veinte semillas.

El apéndice no lista esas semillas finales. Tampoco se encontró su manifiesto en la tesina ni en los archivos y referencias locales examinados de `marl-tlc`. Se solicitó al usuario la fuente. La metodología explicita ahora esta falta documental, en lugar de atribuir una trazabilidad cerrada. Los números deben recuperarse de los manifiestos efectivos, no generarse para completar una tabla.

19. **Las etiquetas de Mendoza conservaban alias sin uso. Depurado.**

Se comprobaron los usos de las ocho etiquetas de los cuatro subapartados urbanos de la metodología: ninguna recibía una referencia cruzada. Se sustituyeron los tres alias de «Dominio y datos» por un identificador descriptivo y se retiraron los dos alias redundantes de demanda. Quedó una etiqueta por subapartado.

Una etiqueta sin referencias no rompe el PDF ni constituye por sí sola un defecto de lectura. La mejora es de mantenimiento del fuente; no debe confundirse con la corrección de remisiones que conducían a contenido ausente.

**Localización de los casos en los fuentes después de las correcciones**

| Caso | Fuente |
|---|---|
| 1. Reparto de verdes | [5-metodologia.tex:149](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:149) |
| 1. Calibración y ecuación | [8-apendice_arquitectura.tex:256](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:256) |
| 2. Memoria y señal local | [5-metodologia.tex:215](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:215) |
| 3. Censura | [5-metodologia.tex:429](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:429) |
| 3. Gini | [5-metodologia.tex:485](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:485) |
| 3. Efecto relativo | [5-metodologia.tex:512](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:512) |
| 4. Expansiones TPE/ASHA | [5-metodologia.tex:290](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:290) |
| 5. Muestreos y remisiones | [8-apendice_arquitectura.tex:403](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:403) |
| 6. Recompensas del diagrama | [8-apendice_arquitectura.tex:182](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:182) |
| 7. Unidades del codificador | [8-apendice_arquitectura.tex:670](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:670) |
| 8. Calibración urbana anterior | [8-apendice_arquitectura.tex:631](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:631) |
| 9. Refinamiento repetido, cuerpo | [5-metodologia.tex:352](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:352) |
| 9. Refinamiento repetido, apéndice | [8-apendice_arquitectura.tex:620](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:620) |
| 10. Párrafo de limitaciones | [5-metodologia.tex:554](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:554) |
| 11. Alcance repetido | [3-introduccion.tex:58](/home/juanm4morales/Documentos/tesina/3-introduccion.tex:58) |
| 12. Procedencia O1 | [8-apendice_arquitectura.tex:292](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:292) |
| 13. Alcance sintético y urbano | [8-apendice_arquitectura.tex:629](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:629) |
| 14. Escalado de tablas | [imagenes/metodologia_v2_dominios_happo.tex:2](/home/juanm4morales/Documentos/tesina/imagenes/metodologia_v2_dominios_happo.tex:2) |
| 16. Arquitectura en tabla de semillas | [8-apendice_arquitectura.tex:567](/home/juanm4morales/Documentos/tesina/8-apendice_arquitectura.tex:567) |
| 16. Arquitectura en tabla de dominios | [imagenes/metodologia_v2_dominios_happo.tex:6](/home/juanm4morales/Documentos/tesina/imagenes/metodologia_v2_dominios_happo.tex:6) |
| 17. Notación de componentes | [imagenes/metodologia_v2_componentes_encoder.tex:15](/home/juanm4morales/Documentos/tesina/imagenes/metodologia_v2_componentes_encoder.tex:15) |
| 17. Generador de componentes | [imagenes/metodologia_v2_generar_encoder.py:147](/home/juanm4morales/Documentos/tesina/imagenes/metodologia_v2_generar_encoder.py:147) |
| 18. Semillas finales sin listado | [5-metodologia.tex:531](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:531) |
| 19. Etiqueta de dominio y datos | [5-metodologia.tex:131](/home/juanm4morales/Documentos/tesina/5-metodologia.tex:131) |

**Verificación del estado corregido**

Se recompiló `main.pdf` mediante la receta del proyecto y se inspeccionaron once páginas afectadas del PDF resultante. El archivo conserva 153 páginas. El log final registra cero errores LaTeX, referencias y citas indefinidas, etiquetas redefinidas, cajas Overfull y Underfull, y avisos de índices o referencias pendientes de estabilizar. Persisten dos avisos conocidos del entorno: la versión solicitada de LaTeX y el soporte de dialecto español de tracklang.

El recorrido de fuentes corregidos incluye 34 archivos, 212 etiquetas y 227 usos de referencias, sin destinos ausentes ni etiquetas duplicadas. `git diff --check` no detecta problemas de espacios. Se verificó además que el PDF no conserve «demanda relativa», las duplicaciones de TPE y BFS, la alusión a la excepción urbana ni la variable M_num.

SHA-256 del PDF corregido: `0182bf4ba919ed181ef88920bb28aac1308ba4d2d181da4b3c6ebbb35288a5ea`.

El informe y las correcciones se incorporan al historial por solicitud del autor. Aunque las reglas generales excluyen los archivos Markdown, este informe se incluye explícitamente en el seguimiento.
