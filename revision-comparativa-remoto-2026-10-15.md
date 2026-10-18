**Revisión comparativa del remoto y dictamen de tutor — 15 de octubre de 2026**

La versión remota mejora la concisión y el respaldo de algunas afirmaciones técnicas. Sin embargo, todavía no la consideraría una metodología cerrada: la unificación de fase 2 necesita concordar con el protocolo experimental identificable, y Resultados conserva una ambigüedad sobre el tratamiento de la red 3×3. Como tesina completa, el documento requiere desarrollar los resultados y las conclusiones. Esto es un diagnóstico del manuscrito disponible, no una afirmación sobre la inexistencia de experimentos fuera de él.

**1. Versiones, alcance y criterios de esta revisión**

Se actualizaron las referencias mediante `git fetch origin` y se verificaron las puntas con `git ls-remote`. La comparación se fija en estas versiones:

| Versión | Commit | Situación |
|---|---|---|
| `origin/main` | `ecf6182e2fb48f303d8023383327a05c92eceba0` | PDF actualizado el 15/10/2026, 11:46:07, hora de Mendoza |
| Último cambio de fuentes en remoto | `a0e9dbb` | «depurar metodología y unificar condiciones de fase 2», 15/10/2026, 11:45:45 |
| Remoto revisado en el turno anterior | `f884c6e` | PDF de la metodología integrada, 14/10/2026 |
| `main` local y rama remota `coherencia-metodologia-20261014` | `8d1642a61ae6824e542f87ebd1c8e5198975dcf7` | Contienen el pase conservador de coherencia y su PDF |

Los historiales de `main` local y remoto no tienen un ancestro común identificable mediante `git merge-base`. Por ello, los conteos de commits divergentes no miden el cambio intelectual de la tesis. Se compararon directamente sus árboles de archivos y, dentro del historial remoto, el cambio `f884c6e → ecf6182`.

Entre la versión remota actual y la local, las diferencias de fuentes del manuscrito se concentran en `5-metodologia.tex`, `6-resultados.tex`, `8-apendice_arquitectura.tex` y `bibliografia.bib`. También cambia `main.pdf`. Introducción, resúmenes, marco teórico y conclusiones no presentan diferencias entre esas dos puntas. Las diferencias adicionales de skills e informes locales no se interpretan como modificaciones del contenido académico.

Se leyó la metodología remota en continuidad y se contrastaron los pasajes pertinentes del apéndice, Resultados, Introducción, resúmenes y marco teórico. Se consultó, además, la copia local de `marl-tlc` para comprobar dos afirmaciones concretas sobre el protocolo urbano. No se ejecutaron campañas, no se auditó exhaustivamente el software y no se inspeccionó el clúster.

La evaluación utiliza las guías locales `scholar-evaluation` y `scientific-critical-thinking`, adaptadas a una tesina de grado de Ciencias de la Computación. El criterio central es que el trabajo permita reconocer el problema, la contribución implementada, las decisiones, la evidencia y el alcance de las conclusiones. No se exige una innovación algorítmica de nivel doctoral ni una comparación exhaustiva con todo el estado del arte.

Las referencias a líneas remotas de este informe corresponden al commit `ecf6182`, no necesariamente a los archivos de la carpeta de trabajo local.

**2. Qué cambió y qué versión conservaría en cada caso**

| Aspecto | Remoto actual | Versión local | Juicio de tutor |
|---|---|---|---|
| Concisión | Elimina reiteraciones de propósito, cautelas y remisiones | Conserva más explicaciones de alcance | Conservar la depuración cuando la idea necesaria sigue explicada en un lugar fácil de encontrar |
| Señal del crítico | Separa la saturación de la pérdida de su consecuencia sobre el gradiente | Repite parte de la consecuencia en dos párrafos | Preferible la versión remota |
| Citas de HPO | La afirmación sobre búsqueda y separación de semillas cita específicamente a Eimer | Agrupa también fuentes de PPO y MAPPO | Preferible la mayor precisión de la versión remota |
| GEH | Añade una fuente específica de Transport for London y lo denomina estadístico | Remite a una fuente más general | Preferible la versión remota, con el alcance de comprobación ya declarado |
| Summary de SUMO | Añade una referencia directa y distingue `ended` de `arrived` | Conserva una explicación menos respaldada por una cita específica | Preferible la versión remota |
| Fase 2 urbana | Declara reglas y presupuestos comunes a los cuatro escenarios | Distingue las reglas urbanas de las sintéticas | La elección exige resolver la concordancia con el código y la decisión de diseño vigente |
| Tratamiento de 3×3 | Resultados mantiene una exclusión sin sujeto histórico suficientemente claro | Atribuye la separación al informe histórico y afirma el análisis de las tres redes | Preferible la versión local |
| Ventanas urbanas, admisibilidad e incertidumbre | Mantiene párrafos que reúnen funciones distintas | Introduce separaciones pequeñas sin cambiar los procedimientos | Recuperar las separaciones locales que facilitan la lectura |
| Presentación de A/C | Compacta su introducción e integra allí la remisión a las definiciones | Desarrolla más su propósito e integra la remisión en el párrafo sobre diferencias | Ambas soluciones son viables; basta una remisión y debe quedar claro qué contraste se estima |

No corresponde afirmar que el remoto «borró» los commits de coherencia: esos cambios se publicaron en una rama separada y no están integrados en `origin/main`.

La reducción a 161 páginas frente a las 164 del PDF local no constituye por sí sola una mejora ni una pérdida. La diagramación depende también de los saltos de página, las figuras y las aperturas de capítulo.

**3. Hallazgo prioritario: fase 2 urbana y trazabilidad de la especificación**

En [Metodología, línea 467](https://github.com/juanm4morales/tesina/blob/ecf6182e2fb48f303d8023383327a05c92eceba0/5-metodologia.tex#L467), el remoto extiende a los cuatro escenarios hasta 100 propuestas por combinación de algoritmo y escenario, 60 iteraciones, gracia de 30, reducción de 2 y diagnóstico cada 15 iteraciones. El [apéndice, línea 637](https://github.com/juanm4morales/tesina/blob/ecf6182e2fb48f303d8023383327a05c92eceba0/8-apendice_arquitectura.tex#L637) declara comunes las reglas de refinamiento, y su línea 660 atribuye esas reglas a `urban/refinement.py`.

El cambio hace concordar las afirmaciones entre cuerpo y apéndice. El problema es que la concordancia interna no basta para garantizar que describan el programa citado.

La copia experimental local consultada pertenece a `v15-mendoza-fixed-tls-study`, con HEAD `6081522`, y contiene trabajo modificado y no versionado. En esa copia:

| Decisión | Remoto de la tesina | Código o configuración experimental local consultados |
|---|---|---|
| Conservar dominio amplio por dispersión | Amplitud de los veinte mejores disponibles ≥70% del dominio | Amplitud de los diez mejores ≥50% |
| Ampliar un intervalo interior | 10% del ancho original a cada lado | Ancho base mínimo del 10%; ampliación del 25% de ese ancho base a cada lado |
| Variables categóricas | Alternativas de los veinte mejores, con una alternativa adyacente si aparece una sola | Conserva todas las categorías originales |
| Presupuesto urbano de fase 2 | Cifras comunes ya fijadas en el texto | Propuestas, iteraciones, gracia, reducción y frecuencia diagnóstica permanecen en `null` |
| Propuestas urbanas de fase 1 | 100 iniciales por estudio, ampliables a 150; 800 iniciales en ocho estudios | `protocol.json` conserva 50 por arquitectura y `protocol.py` exige exactamente 50 |

La diferencia de fase 1 ya afectaba a la versión local del manuscrito; no fue introducida por el último cambio remoto. La generalización de fase 2 sí es una modificación relevante del remoto reciente.

Un ejemplo aritmético ilustra que las reglas no son equivalentes. En un dominio continuo normalizado `[0,1]`, supóngase que los diez mejores valores están entre 0,40 y 0,60 y que los demás valores considerados no activan la conservación del dominio amplio. La regla descrita en remoto produce `[0,30; 0,70]`. El programa urbano consultado produce `[0,35; 0,65]`. No se trata únicamente de una diferencia de redacción: se obtienen espacios de búsqueda distintos. Este ejemplo es ilustrativo, no un resultado experimental.

**Qué exigiría para cerrar este punto.** Identificar una versión concreta del protocolo y del código que implemente la decisión vigente. Si se decidió unificar los cuatro escenarios, esa decisión puede ser válida, pero debe quedar registrada y reflejada en el programa, los validadores y los artefactos derivados. Si se describe la implementación urbana disponible, deben conservarse sus reglas específicas. Ninguna de estas decisiones autoriza a reinterpretar retrospectivamente campañas anteriores.

También conviene indicar cómo se distribuye el presupuesto de 100 propuestas de fase 2 entre arquitecturas y cómo se cuenta la configuración inicial: dentro del total o como una propuesta adicional. El texto presenta un total por algoritmo y escenario, mientras el protocolo urbano disponible utiliza un campo por arquitectura. La unidad del presupuesto necesita ser inequívoca.

La revisión no permite afirmar que falte una implementación posterior en otro checkout o en el clúster. Sí permite afirmar que el programa al que remite el manuscrito no reproduce, en la copia consultada, la regla común escrita. Hasta identificar otra versión o alinear esta, la trazabilidad está abierta.

**4. Hallazgo de coherencia entre capítulos: red 3×3**

[Resultados, línea 19](https://github.com/juanm4morales/tesina/blob/ecf6182e2fb48f303d8023383327a05c92eceba0/6-resultados.tex#L19) presenta la red 3×3 como excluida del análisis principal después de observar los resultados, sin atribuir con suficiente claridad esa exclusión al informe histórico. En cambio, Metodología establece que la tesina analiza por separado las tres redes y conserva 24 pares por red; el apéndice distingue expresamente ese alcance del criterio de presentación histórico.

La discordancia afecta a la población analizada y a la interpretación de una decisión posterior a observar resultados. Por ello tiene más importancia que un ajuste de estilo. La formulación de nuestra rama de coherencia ya resuelve el problema y debería recuperarse: la tesina analiza las tres redes por separado; el informe histórico es quien apartó 3×3 de su análisis principal.

No recomendaría eliminar la red ni combinar los 72 pares. La corrección consiste en atribuir correctamente la decisión histórica y mantener la correspondencia entre el protocolo de análisis y las tablas que finalmente se presenten.

**5. Valoración del trabajo como tesina de grado**

**Problema y contribución.** El problema está bien delimitado: agentes que controlan fases de semáforos bajo observaciones parciales, con heterogeneidad de geometrías y demanda. La Introducción identifica la comparación de procedimientos, la adaptación de HAPPO, la codificación y la construcción urbana. Son contribuciones de implementación y evaluación pertinentes para Ciencias de la Computación. No hace falta prometer que se creó un algoritmo universalmente superior.

Como tutor, pediría que al cerrar el manuscrito puedan reconocerse dos preguntas empíricas: qué desempeño tuvieron los procedimientos completos bajo el presupuesto definido y qué cambió entre las variantes A y C de MAPPO bajo la configuración fija. La codificación puede defenderse como una decisión implementada y estudiada dentro del sistema; sin ablación, no debe presentarse como la causa demostrada de una mejora. El marco teórico ya reconoce esa limitación.

La comprobación urbana tiene una contribución distinta: preparar y caracterizar un escenario construido con información parcial. Su pertinencia no depende de que una política aprendida mejore el control en Mendoza. Sí depende de que el alcance urbano prometido en los objetivos corresponda con la evidencia que finalmente se entregue.

**Antecedentes y marco teórico.** Los pasajes revisados diferencian mecanismos de coordinación, representación y heterogeneidad y conectan los antecedentes con el proyecto. La distinción entre el HAPPO teórico y la adaptación con recompensas individuales es especialmente importante y está explicitada. La ausencia de una comparación hallada se presenta como límite de la búsqueda, no como prueba de que no existe literatura previa.

La principal tarea pendiente es que esos conceptos se utilicen para interpretar los resultados: por ejemplo, explicar qué significa una diferencia en un escenario heterogéneo sin atribuirla automáticamente a la actualización secuencial. No realizó esta revisión una búsqueda bibliográfica exhaustiva ni una validación de todas las referencias del marco teórico.

**Diseño experimental.** La separación entre búsqueda, selección, entrenamiento desde cero y evaluación es una fortaleza. También lo son los filtros de atención a la demanda, la distinción entre ensayos incompletos y candidatos no admisibles, y la elección anticipada del checkpoint final. Igualar iteraciones no implica igualar pasos de gradiente ni recursos; el manuscrito conserva esa advertencia. Para comparar procedimientos completos puede aceptarse, siempre que se presenten los presupuestos efectivos disponibles y no se afirme una igualdad computacional que no se midió.

La recompensa cambia entre la fase 1 sintética y la búsqueda refinada local. El texto reconoce que las regiones favorables en fase 1 no tienen que seguir siéndolo con la nueva señal. Esto hace defendible la transferencia como orientación exploratoria; no demuestra que el refinamiento sea óptimo ni que se haya aislado el efecto de fijar rho en cero.

La selección urbana exige no empeorar inserciones, completitud y teletransportes en cada una de cinco semillas. Es una regla operativa exigente y explícita. No es una prueba estadística de no inferioridad para toda demanda ni una garantía del modelo final entrenado de nuevo. El manuscrito distingue estas situaciones y contempla que no haya candidatos admisibles. No recomendaría relajar los filtros después de ver resultados para forzar una elección.

**Métricas y validez de las afirmaciones.** Es acertado separar la espera local de memoria finita de la espera por viaje de TripInfo. También lo es definir una cohorte por inserción efectiva, incluir viajes inconclusos y advertir que las políticas pueden atender cohortes distintas. Estas precisiones evitan equiparar una reducción de la señal de recompensa con una reducción demostrada de la demora total de toda la demanda.

La interpretación final debe mantener esa disciplina. Para una variante con menor espera media, deberían poder verse sus inserciones, completitud y, cuando estén disponibles, retrasos de ingreso. El criterio A/C permite una decisión favorable sin un umbral de inserciones; por ello, esa decisión tiene un alcance específico y no equivale por sí sola a una mejora integral de la atención a la demanda. El manuscrito ya lo explica: la tarea principal es reflejarlo en las tablas y en la discusión, no multiplicar la misma cautela en todas las secciones.

El Gini representa desigualdad entre promedios de controladores con cargas distintas; no demuestra por sí solo equidad entre vehículos. La formulación describe esa ponderación. Conviene conservar el nombre y la interpretación restringida cuando se discutan resultados.

**Estadística.** A/C está mejor definido que una comparación basada únicamente en episodios: utiliza 24 pares de entrenamientos por red, promedia primero las cinco evaluaciones de cada política y remuestrea pares completos. Los niveles del 95% y 98,33%, su corrección por tres redes y la sensibilidad con Student están documentados. También se distingue el promedio de cambios relativos del cociente entre medias globales. No se advierte en esas definiciones un motivo para reemplazar todo el análisis.

En cambio, la comparación de los cuatro algoritmos evalúa un modelo final por combinación con veinte simulaciones. Esto describe la variabilidad de ese modelo frente al simulador; no establece la variabilidad entre entrenamientos de cada algoritmo. El texto lo reconoce y debería conservarse una conclusión descriptiva sobre los modelos obtenidos. La literatura citada sobre evaluación de RL respalda la importancia de reportar incertidumbre y evitar conclusiones desproporcionadas con pocas ejecuciones independientes: [Agarwal et al.](https://arxiv.org/abs/2108.13264).

No impondría nuevos entrenamientos como condición automática para una tesina cuyo objetivo se limite a esa comparación descriptiva. Si el objetivo final exige afirmar superioridad general de un algoritmo, debe cambiar la evidencia o reducirse la afirmación. Los paneles no comunes de evaluación final tampoco invalidan automáticamente el diseño; impiden aprovechar un contraste pareado directo por semilla y deben interpretarse de acuerdo con el procedimiento declarado.

**Implementación y teoría.** El documento reconoce dos limitaciones importantes de la versión A/C: el cierre con terminación y truncamiento simultáneos y la atribución de esperas en una memoria finita. Además, explica que la saturación de la pérdida del crítico puede anular el gradiente de una muestra para todas sus salidas. Esta transparencia es una fortaleza de la presentación.

Describir estos comportamientos no cuantifica su efecto en las políticas. En Resultados debe quedar clara la versión de implementación evaluada; una corrección posterior del código no vuelve correctos retrospectivamente los entrenamientos anteriores. Para el alcance actual, no exigiría una campaña nueva solo por haber documentado estas limitaciones. Sí evitaría atribuir el resultado exclusivamente al algoritmo teórico de referencia o afirmar que se verificó un efecto que no se midió.

**Datos urbanos.** La exposición distingue el perfil de generación de 32 días y 260.000 vehículos del resumen histórico de 33 días y 290.000. Conserva las diferencias 60/40 frente a 70/30 y el límite impuesto por la ausencia de las rutas originales. Eso permite defender un escenario de simulación construido con supuestos, sin presentarlo como una reconstrucción validada de toda la movilidad de Mendoza.

La evaluación de doce horas y la selección de dos horas tienen funciones distintas. El cambio de horizonte está declarado, pero el párrafo local separado mejora su visibilidad. Una selección satisfactoria en el recorte matutino no acredita automáticamente un comportamiento diario satisfactorio: ese resultado debe mostrarse cuando exista.

**6. Resultados y conclusiones: principal condición para una entrega final**

En el remoto actual, el capítulo de Resultados conserva subsecciones vacías de consolidación, sensibilidad, selección y desempeño sintético. No presenta todavía los resultados numéricos de A/C que permitirían aplicar el criterio descrito. La discusión contiene una frase introductoria, y Conclusiones consta de un párrafo que anuncia su función.

Por ello distinguiría dos juicios: la metodología es un borrador avanzado que puede cerrarse con correcciones acotadas y trazabilidad; la tesina completa todavía no está lista para entrega final en la versión revisada. Este segundo juicio también se aplica a la versión local.

La tabla urbana es evidencia operacional pertinente, pero no responde las preguntas de desempeño de las políticas aprendidas. Sus tasas son aritméticamente coherentes con los conteos: se comprobaron las seis divisiones correspondientes a CR, IR y CI. Esa comprobación aritmética no valida la identidad de las cohortes ni recupera las rutas ausentes.

La tabla muestra ceros en teletransportes y la prosa posterior aclara que proceden de documentación secundaria del escenario. Recomiendo llevar esa atribución a una nota de tabla o al epígrafe, manteniendo los conteos como están. Así, una lectura aislada de la tabla no convierte un valor informado en un contador primario verificado.

Para completar Resultados, pediría una correspondencia entre pregunta, datos y conclusión. En A/C: resultados por cada red, cantidad efectiva de pares completos, efectos absoluto y relativo, intervalos, diferencia de completitud, teletransportes y diagnóstico de inserciones. En HPO y modelos finales: candidatos realmente evaluados, configuraciones seleccionadas cuando las haya y resultados que existan, distinguiendo incompletos de no admisibles. En Mendoza: mantener aparte la comprobación de programas de referencia y cualquier evaluación posterior de políticas.

No presupongo que haya que ejecutar todo lo planificado para poder defender una tesina de grado. Si alguna línea queda fuera del trabajo concluido, el alcance de los objetivos, el resumen y las conclusiones debe ajustarse de manera explícita y coherente.

**7. Lectura y continuidad: qué recuperaría del pase local**

La depuración remota tiene un criterio útil: evita explicar varias veces la misma cautela. Lo conservaría. Hay, sin embargo, párrafos donde la separación local expresa una distinción metodológica real y merece recuperarse:

| Pasaje | Separación útil para el lector |
|---|---|
| Entorno y cierre | Indicadores de cierre / efecto sobre valores y ventajas |
| Herramientas de búsqueda | Propuestas y ejecución / detención anticipada con ASHA |
| Fases generales | Condiciones de fase 1 / refinamiento de los dominios en fase 2 |
| Selección urbana | Archivos y ventana / condiciones compartidas con la referencia |
| Admisibilidad urbana | Regla de aceptación / evidencia necesaria para poder clasificar |
| Configuración A/C | Procedencia de hiperparámetros / diferencias entre variantes y alcance |
| Evaluación urbana | Entrenamiento de dos horas / evaluación diaria de doce |
| Incertidumbre A/C | Intervalos principales / sensibilidad y límites |
| Apéndice urbano | Presupuesto de búsqueda / pasos que forman el lote de aprendizaje |

Mantendría la formulación local «los dominios de cada escenario se refinan» frente a «cada red se refina», porque identifica exactamente qué cambia. No agregaría conectores ni justificaciones nuevas si solo alargan la exposición. Tampoco restauraría todas las cautelas eliminadas: una advertencia bien ubicada y respetada en Resultados vale más que su repetición constante.

**8. Fuentes nuevas y verificación documental**

La nueva referencia `TfL2021TrafficModelling` corresponde al documento oficial de Transport for London, versión 4.0, septiembre de 2021. Su apéndice II, página impresa 578, presenta el estadístico GEH y su fórmula. La cita es más específica para esa ecuación que una remisión general a un manual. El uso aquí compara el flujo nominal programado con el perfil que intervino en su construcción; el propio manuscrito aclara que no es una validación independiente. [Documento oficial de TfL](https://content.tfl.gov.uk/traffic-modelling-guidelines.pdf).

La documentación oficial de SUMO confirma que `loaded` puede incluir salidas futuras y que `ended` incluye llegadas y otras retiradas, mientras `arrived` identifica llegadas a destino. Es correcta la nueva distinción del apéndice. Esto no demuestra que los conteos históricos provinieran de una salida Summary concreta: el remoto mantiene ese límite. [Documentación de Summary](https://sumo.dlr.de/docs/Simulation/Output/Summary.html).

Las dos entradas nuevas contienen `language = {spanish}` y son aceptadas por la cadena BibTeX del documento. La revisión verificó esas fuentes específicas; no certifica la exactitud de toda la bibliografía.

**9. Prioridades y criterio de cierre**

| Prioridad | Acción | Criterio observable de cierre |
|---|---|---|
| Alta, para cerrar metodología | Resolver la versión del refinamiento y presupuesto urbanos | Texto, código identificado y configuración describen el mismo procedimiento, con unidades de presupuesto claras |
| Alta, para cerrar metodología | Corregir la atribución histórica de 3×3 | Los tres capítulos declaran el mismo conjunto de redes analizadas |
| Alta, para entrega final | Desarrollar Resultados y Conclusiones o ajustar el alcance concluido | Cada objetivo empírico tiene evidencia presentada o una delimitación explícita de lo que no se completó |
| Media | Vincular versiones y artefactos a los procedimientos | Se puede seguir una configuración hasta el modelo, las evaluaciones y la tabla que lo resume |
| Media | Hacer visibles los diagnósticos de demanda y procedencia | Las tablas permiten interpretar esperas, inserciones, completitud y origen de los teletransportes |
| Baja | Recuperar las separaciones de párrafos que aclaran funciones | La lectura distingue entradas, operaciones, criterios y productos sin reiteraciones |

No priorizaría una reescritura general del capítulo ni nuevas ablaciones de todos los componentes. Antes de ampliar experimentos, cerraría el alcance efectivamente defendible y la correspondencia entre especificación, implementación y evidencia.

Mi recomendación para una integración futura es tomar selectivamente la concisión y las citas del remoto y las aclaraciones de coherencia de la rama local. La unificación de fase 2 necesita una resolución propia. Una fusión completa de historiales no resolvería esa decisión científica y añadiría diferencias de archivos ajenas al pase editorial.

**10. Verificaciones y trazabilidad de esta revisión**

Se exportó `origin/main` a `/tmp/tesina-remote-20261015-dx71arrx` sin modificar los capítulos ni el PDF de la carpeta de trabajo. Se preservó el PDF remoto como `main-publicado.pdf` y se compiló desde cero la copia con `pdflatex -synctex=1`, `makeglossaries main` y `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`.

La compilación terminó correctamente. El log final solo contiene la advertencia conocida de `tracklang`; no aparecen citas o referencias indefinidas, etiquetas duplicadas ni desbordes. El PDF publicado y el recompilado tienen 161 páginas y texto extraído idéntico al normalizar espacios. `qpdf --check` no encontró errores sintácticos o de codificación de streams. Se inspeccionaron visualmente las páginas físicas 107, 109, 120, 146 y 147, que incluyen cambios de fase 2, A/C, Resultados y protocolo urbano. La revisión visual fue focalizada, no una inspección exhaustiva de las 161 páginas.

Las fuentes experimentales consultadas para el contraste urbano se identifican por estos hashes SHA-256, porque parte del árbol experimental no está versionada:

| Archivo relativo a `/home/juanm4/Dev/marl-tlc` | SHA-256 |
|---|---|
| `experiments/marl_experiments/tuning/urban/protocol.json` | `97173c72ce5241068ced00731ebbc123fb43a3b714b15c9508a73a05392328c3` |
| `experiments/marl_experiments/tuning/urban/refinement.py` | `338ff113755284cd8dab2e9d3d9a8e44c0a66f2814a2fadc59d2a59e5f4f5eaa` |

No se editaron fuentes del manuscrito, no se fusionaron ramas, no se modificó el repositorio experimental y no se hicieron commits ni push como parte de esta revisión. El único archivo añadido a la carpeta de la tesina es este informe.
