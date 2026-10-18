# Registro de decisiones de la revisión de metodología según las reglas de Caro

Fecha de apertura: 17 de octubre de 2026. Alcance inicial: `5-metodologia.tex` y este registro, con las ampliaciones acotadas documentadas en las fichas 10 y 18–23. La revisión avanza cambio por cambio, con explicación previa y ficha independiente. Las primeras resoluciones se confirmaron individualmente; la autorización posterior «Autorizo todo» permite continuar las intervenciones descritas sin nuevas confirmaciones intermedias. La aplicación de un cambio y una compilación exitosa no constituyen, por sí solas, una aprobación del usuario.

Referencias vigentes: [reglas R01–R26](REGLAS_EDITORIALES_CARO.md), [observaciones originales](TODO-comentarios-caro.md) y [auditoría fechada del 16 de octubre](revision-reglas-caro-2026-10-16.md). Las reglas se aplican por significado. La modalidad de aprobación responde a las instrucciones del usuario y al flujo de `AGENTS.md`; no se atribuye a Caro.

## Alcance y antecedentes

La revisión busca resolver dificultades identificables de comprensión, precisión o consistencia. Conservar un pasaje es una resolución válida si no se acredita una mejora suficiente. La apertura del capítulo se examinará en contexto, sin recomendar un nuevo sujeto por sí mismo ni inferir ausencia de ejecuciones a partir de resultados aún no redactados.

El alcance editorial inicial comprendió metodología y su registro. Las fichas específicas documentan su ampliación a la bibliografía de PyTorch y HAPPO, al párrafo que presenta la adaptación de HAPPO en el marco teórico y al formato numérico del apéndice y de la tabla generada de IDQN. Estas ampliaciones resuelven los pendientes identificados durante la revisión. Se conservan las limitaciones de HAPPO, las diferencias entre protocolos de recompensa, el alcance conjunto y sintético de A/C y las limitaciones documentales de Mendoza. Las correcciones técnicas o factuales se respaldan con las fuentes o el código indicados en cada ficha.

El registro anterior se conserva al final como **antecedente del 16 de octubre de 2026**. Sus casillas, ubicaciones, recuentos y comprobaciones describen lo declarado para aquella entrega; no certifican el estado actual ni constituyen aprobaciones de esta revisión. El procedimiento vigente se describe al comienzo de este documento y refleja las autorizaciones posteriores del usuario. El antecedente no autoriza nuevas ediciones ni ampliaciones del alcance.

## Estados y ficha de cada resolución

Los tres estados se registran por separado:

| Estado | Significado | Evidencia necesaria |
| --- | --- | --- |
| Aplicado | La intervención está incorporada en los archivos. | Diff acotado al cambio autorizado. |
| Verificado | Se realizaron las comprobaciones pertinentes. | Resultado, fecha y pendientes concretos; la compilación no sustituye la revisión semántica o visual. |
| Aprobado | El usuario aceptó explícitamente la resolución de esa ficha. | Decisión y alcance de la aprobación. No se deduce de los otros estados. |

Cada ficha incluye ubicación estable (sección, etiqueta LaTeX y pasaje exacto; línea auxiliar), diagnóstico (problema confirmado, mejora editorial opcional o verificación pendiente), fundamento (regla y observación original pertinente, distinguiendo su extensión a metodología), comparación exacta entre texto actual y propuesta, alternativa de conservar, justificación y cierre. Un traslado desde un epígrafe al párrafo próximo puede constituir una sola intervención coherente; otras figuras o pasajes requieren fichas separadas.

Después de cada edición aprobada se comprobarán el diff y los elementos técnicos afectados. Se compilará con `latexmk` y SyncTeX hasta estabilizar las referencias y se revisarán el log y la página modificada. Si cambian usos de glosario, se completará su ciclo y se comprobarán los enlaces del PDF. Una ficha de conservación registrará las comprobaciones que correspondan, sin simular una edición. El cierre final contrastará ecuaciones, tablas, etiquetas, citas y archivos de figuras con el estado inicial de esta revisión.

La revisión siguió este orden: 0, actualización del registro; 1, apertura del capítulo; 2, referencias y vocabulario; 3, flujo experimental; 4, programas semafóricos y escenarios; 5, integración, codificación y controladores; 6, adaptación HAPPO; 7, búsqueda y selección; 8, métricas e incidencias; 9, análisis pareado; 10, formato y página. Los bloques avanzaron mediante fichas individuales; las fichas 18–23 completan después los pendientes transversales identificados.

### Estado actual de los pendientes asociados

| Hallazgo | Resolución y alcance comprobado | Fichas |
| --- | --- | --- |
| H16 | Resuelto: metodología define uniforme continua y loguniforme, y la remisión del apéndice encuentra el contenido anunciado. | 12 |
| H20 | Resuelto para las ocurrencias inventariadas: punto en las cantidades agrupadas y coma decimal; formato uniforme en los contadores comparables de IDQN. La búsqueda en las 22 fuentes incluidas no encuentra agrupaciones de miles con espacio fino. Se respetan las excepciones técnicas. | 17, 19–22 |
| H32 | Resuelto: se distingue localmente el orden del pseudocódigo de referencia y el de la implementación; se contrastaron los artículos y la versión congelada conservada. No se generaliza la comprobación a otras versiones ni campañas. | 9, 18 |
| H34 | Resuelto: atribución de PyTorch citada y metadatos de su publicación comprobados. | 10 |

Este estado corresponde a la revisión actual y sus ampliaciones documentadas. La auditoría general del 16 de octubre mantiene su carácter de diagnóstico fechado; sus otros hallazgos deben revalidarse antes de considerar nuevas ediciones.

## Ficha 0 — Sustituir el enfoque de entrega completa por decisiones individuales

- **Ubicación:** apertura de `PLAN-revision-metodologia-caro.md`, línea 3 anterior a esta revisión; sin etiqueta LaTeX por tratarse de un registro Markdown. La intervención comprende la nueva organización del registro y la identificación del contenido previo como antecedente fechado.
- **Diagnóstico:** problema confirmado de procedimiento. La instrucción anterior permite ejecutar todos los bloques sin aprobaciones intermedias y no distingue aplicación, verificación y aprobación.
- **Fundamento:** R26, regla inferida de trazabilidad, y el flujo por etapas de `AGENTS.md`. C102 exige cautela ante una marca incompleta y C246/C287 valoran pasajes que deben conservarse; ninguna de esas observaciones pide aprobaciones intermedias. Ese requisito procede de la revisión solicitada.
- **Texto actual anterior a esta revisión:**

  > Fecha: 16 de octubre de 2026. Alcance: `5-metodologia.tex` y su representación en `main.pdf`, con un ajuste de formato numérico en la figura del codificador y su generador. Se aplica el pedido de revisión como una entrega completa; los bloques siguientes organizan el trabajo y su verificación, sin establecer una aprobación separada entre ellos.

- **Propuesta exacta para la apertura:**

  > Fecha de apertura: 17 de octubre de 2026. Alcance: `5-metodologia.tex` y este registro. La revisión se realiza cambio por cambio: antes de aplicar o revertir una intervención se presenta su ficha y se solicita aprobación explícita. Cada aprobación autoriza únicamente esa intervención. No se avanza a la ficha siguiente sin aprobar la resolución de la actual, incluso cuando se recomiende conservar el pasaje. Las modificaciones previas y las compilaciones exitosas no equivalen a aprobación.

- **Cambios documentales dependientes:** renombrar el documento como registro de decisiones, separar los tres estados, establecer las fichas y sus comprobaciones, y conservar los bloques y comprobaciones anteriores bajo el encabezado de antecedente fechado. No aplicar ni revertir cambios al manuscrito mediante esta ficha.
- **Alternativa de conservar:** mantener íntegro el documento actual. No se recomienda porque su instrucción de ejecución conjunta contradice el procedimiento solicitado.
- **Justificación:** permite identificar qué resolución fue aceptada y qué se comprobó realmente, sin convertir comprobaciones históricas en validación actual. No altera afirmaciones metodológicas ni elimina los antecedentes; añade estructura administrativa para mantener esa distinción.
- **Comprobación previa:** el 17 de octubre se contrastó la fuente con Git: se conservan doce ecuaciones y seis cuerpos `tabular` idénticos a `HEAD`, doce figuras y 111 referencias con etiquetas existentes, sin etiquetas duplicadas en las fuentes incluidas. Esto no valida aún el contenido prometido por cada remisión. El log existente solicita otra pasada; no se declara estabilizada la compilación. No se compiló para preparar esta propuesta documental.
- **Aplicado:** sí. Se incorporó la actualización documental propuesta, incluida la conservación del plan anterior como antecedente.
- **Verificado:** sí. El registro coincide con la propuesta aprobada y conserva el contenido previo como antecedente; solo cambia el nivel de sus encabezados. La comprobación de hashes confirma que las fuentes LaTeX, el PDF y los demás archivos controlados permanecen como en la preparación.
- **Aprobado:** sí. El usuario confirmó «Ok» para la ficha 0; la aprobación cubre únicamente esta actualización del registro.
- **Criterio de cierre:** aprobación de esta actualización, incorporación exclusiva del cambio documental y verificación de su alcance. Solo entonces se presentará la ficha 1.

## Ficha 1 — Apertura: conservar la presentación de las líneas de trabajo

- **Ubicación:** `5-metodologia.tex`, segundo y tercer párrafos del capítulo (líneas auxiliares 7–9 al abrir la ficha).
- **Estado:** decisión editorial opcional; no se confirmó un defecto que justifique reescribirlos.
- **Fundamento:** R06, R08 y R23. Las observaciones C280/C284 se refieren al marco teórico; se aplican aquí como criterio inferido para distinguir diseño, ejecución y evidencia, no como pedido literal de Caro sobre metodología.
- **Texto actual y resolución propuesta:** conservar sin cambios estos dos párrafos:

  > El diseño compara implementaciones de `\acrshort{acr-mappo}` y una adaptación de `\acrshort{acr-happo}`, con `\acrshort{acr-ippo}` e `\acrshort{acr-idqn}` como referencias. La actualización secuencial de los actores de `\acrshort{acr-happo}` motiva su comparación con `\acrshort{acr-mappo}` en escenarios heterogéneos, como `$4\times4\_H$` y la red parcial de Mendoza.
  >
  > El diseño contempla dos líneas de estudio. La primera establece un procedimiento común para comparar los cuatro algoritmos en cada escenario mediante la búsqueda de hiperparámetros, la selección de configuraciones admisibles y el entrenamiento desde cero de las políticas que se evaluarán. La segunda estudia, con `\acrshort{acr-mappo}`, el efecto conjunto de incorporar información vecinal a la observación y a la recompensa.

- **Justificación:** «El diseño» identifica el sujeto; el segundo párrafo precisa las dos líneas y diferencia las políticas que se evaluarán del procedimiento descrito. Sustituirlo por «La metodología establece una comparación» cambiaría el sustantivo, sin aclarar mejor quién compara ni qué evidencia se informa.
- **Aprobado:** sí, el usuario respondió «Sí» a la resolución de conservar ambos párrafos.
- **Aplicado:** no hubo edición de `5-metodologia.tex`; se registró la resolución aprobada.
- **Verificado:** los párrafos coinciden con la fuente consultada. No se compiló porque no cambió ninguna fuente LaTeX.
- **Cierre:** ficha resuelta como conservación aprobada. La siguiente ficha revisa una remisión distinta.

## Ficha 2 — Remisión a los protocolos A–E y A/C: conservar

- **Ubicación:** `5-metodologia.tex`, párrafo que presenta las dos líneas de trabajo, línea auxiliar 20.
- **Diagnóstico:** remisión comprobada; el plural genérico y los destinos corresponden a lo anunciado.
- **Fundamento:** R17 para nombrar el objeto y R22 para comprobar el contenido efectivo del destino. La comprobación del destino es una extensión operativa; Caro no anotó esta remisión concreta.
- **Texto actual y resolución:** conservar: «Sus protocolos se detallan en las secciones `\ref{subsec:screening_vecinal}` y `\ref{sec:comparacion_local_vecinal}`, respectivamente».
- **Comprobación:** `subsec:screening_vecinal` está en «Prueba preliminar de formulaciones» y describe A–E; `sec:comparacion_local_vecinal` está en «Comparación local y vecinal de MAPPO» y describe A/C.
- **Aprobado:** sí; el usuario respondió «Sí» a conservar esta remisión.
- **Aplicado:** no se modificó `5-metodologia.tex`; se registró la conservación aprobada.
- **Verificado:** etiquetas, encabezados y contenido de ambos destinos comprobados en la fuente. No se compiló porque no hubo cambio LaTeX.
- **Cierre:** ficha resuelta como conservación aprobada.

## Ficha 3 — Explicación del corredor 3×1 junto a su figura

- **Ubicación:** `5-metodologia.tex`, subsección «Redes de tráfico sintéticas», párrafo del corredor y Figura `fig:topologias_sinteticas` (Figura 3.3 en el PDF compilado).
- **Diagnóstico:** problema de continuidad confirmado. La descripción específica del corredor aparecía después de las tres figuras y de la tabla comparativa, separada de la figura que ayuda a interpretar.
- **Fundamento:** C076 pide situar la explicación junto a la figura; C092 solicita evitar intercalar otros elementos antes de retomar su explicación. R09 generaliza ese criterio a explicaciones funcionalmente equivalentes en metodología; no se atribuye a Caro una observación directa sobre este capítulo.
- **Cambio aprobado:** se trasladó el párrafo inmediatamente antes de la Figura 3.3 y se añadió «La Figura `\ref{fig:topologias_sinteticas} muestra…» para identificar el objeto. El resto del párrafo —cruces B1, C1 y D1, distribución del 75 % del flujo y propósito de estudiar la coordinación longitudinal— se conservó.
- **Aprobado:** sí; el usuario respondió «Sí» a la propuesta exacta del primer cambio.
- **Aplicado:** sí; el cambio se limitó al traslado del párrafo y a la referencia explícita a la figura.
- **Verificado:** sí. El diff frente al estado fuente previo a esta intervención contiene únicamente el traslado descrito. `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` terminó correctamente. En el PDF, página física 87 (impresa 63), el párrafo aparece seguido por el diagrama y su epígrafe; la inspección visual confirma que ambos quedan en la misma página. No se detectaron nuevos `Overfull \hbox`; permanece la advertencia conocida de `tracklang` para español.
- **Cierre:** ficha resuelta, aplicada y verificada. La próxima intervención del plan requiere su propia propuesta y aprobación.

## Ficha 4 — Explicación de la red 3×3 junto a su figura

- **Ubicación:** `5-metodologia.tex`, subsección «Redes de tráfico sintéticas», párrafo de la red 3×3 y Figura `fig:red_sintetica_3x3` (Figura 3.4 en el PDF compilado).
- **Diagnóstico:** problema de continuidad confirmado. La descripción específica de la cuadrícula estaba después de las figuras y de la tabla comparativa, separada de la figura que permite reconocerla.
- **Fundamento:** C076 pide situar la explicación junto a la figura; C092 solicita evitar intercalar otros elementos antes de retomarla. R09 generaliza ese criterio funcional a metodología; Caro no anotó directamente este pasaje.
- **Cambio aprobado:** se trasladó el párrafo inmediatamente antes de la Figura 3.4 y se añadió «La Figura `\ref{fig:red_sintetica_3x3} muestra…». Se conservaron la comparación con el corredor y la explicación de la coordinación bidimensional.
- **Aprobado:** sí; el usuario respondió «Sí» a la propuesta exacta del cambio 2.
- **Aplicado:** sí; el diff frente a la propuesta del cambio 1 coincide exactamente con el traslado aprobado.
- **Verificado:** sí. `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` terminó correctamente y mantuvo 162 páginas. En el PDF, el párrafo termina al pie de la página impresa 63 y la Figura 3.4 aparece en la página impresa 64; no hay otro desarrollo entre ambos. La inspección visual confirma el orden de lectura. El log no presenta nuevos `Overfull \hbox`; permanece la advertencia conocida de `tracklang` para español.
- **Cierre:** ficha resuelta, aplicada y verificada. La próxima intervención del plan requiere su propia propuesta y aprobación.

## Ficha 5 — Explicación de la red 4×4_H junto a su figura

- **Ubicación:** 5-metodologia.tex, subsección «Redes de tráfico sintéticas», párrafo de la red 4×4_H y Figura fig:red_sintetica_4x4_h (Figura 3.5 en el PDF compilado).
- **Diagnóstico:** problema de continuidad confirmado. La descripción específica de heterogeneidad, carriles y acciones aparecía después de las figuras y de la tabla, separada de la figura que permite reconocer esa topología.
- **Fundamento:** C076 pide situar la explicación junto a la figura; C092 solicita evitar intercalar otros elementos antes de retomarla. R09 generaliza ese criterio funcional a metodología; Caro no anotó directamente este pasaje.
- **Cambio aprobado:** se trasladó la descripción antes de la Figura 3.5 y se añadió «La Figura \ref{fig:red_sintetica_4x4_h} muestra…». Se conservaron los datos sobre carriles, sentidos, acciones e heterogeneidad. La remisión común a las tres redes quedó al final de la subsección, después de la tabla.
- **Aprobado:** sí; el usuario respondió «Sí» a la propuesta exacta del cambio 3.
- **Aplicado:** sí; el diff frente a la propuesta del cambio 2 coincide exactamente con la intervención aprobada.
- **Verificado:** sí. latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex terminó correctamente y mantuvo 162 páginas. En el PDF, página física 89 (impresa 65), la explicación aparece antes del diagrama y su epígrafe en la misma página. La inspección visual confirma su legibilidad y orden. El log no presenta nuevos Overfull \hbox; permanece la advertencia conocida de tracklang para español.
- **Cierre:** ficha resuelta, aplicada y verificada. La próxima intervención del plan requiere su propia propuesta y aprobación.

## Ficha 6 — Orden de la fuente y las limitaciones de la señal de espera

- **Ubicación:** 5-metodologia.tex, subsubsección «Observaciones y codificación de la espera», etiqueta subsec:observaciones_encoder.
- **Diagnóstico:** la fuente y la ventana finita de la señal se explicaban después de la observación local y vecinal que ya la utilizaban; la limitación de A/C y la distinción con la espera total de TripInfo también aparecían más adelante.
- **Fundamento:** C192 y C197 piden definir conceptos antes de aplicarlos; R01 extiende el criterio al orden de exposición metodológica. Caro no anotó este pasaje de metodología.
- **Cambio aplicado:** se ordenó el bloque para presentar primero la fuente y ventana de SUMO, luego la atribución por carril, la limitación de atribución de A/C, la diferencia con TripInfo y sus consecuencias para interpretar la señal, y finalmente las observaciones local y vecinal. Se conservaron ecuaciones, símbolos, citas, unidades y cautelas.
- **Aprobado:** sí; el usuario respondió «Autorizo todo» para las intervenciones del plan.
- **Aplicado:** sí.
- **Verificado:** sí. latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex terminó correctamente; el PDF conserva 162 páginas. La extracción de la página impresa 74 confirma el orden nuevo y que la señal está explicada antes de la observación local y vecinal. No hay errores de compilación ni nuevos Overfull \hbox; permanece la advertencia conocida de tracklang para español.
- **Cierre:** ficha resuelta, aplicada y verificada.

## Ficha 7 — Definición del codificador antes de la observación local

- **Ubicación:** 5-metodologia.tex, subsubsección «Observaciones y codificación de la espera», etiqueta subsec:observaciones_encoder.
- **Diagnóstico:** la observación local utilizaba e(x) antes de definir la función; la explicación de los niveles I y del límite M_{\mathrm{lane}} aparecía después de las observaciones local y vecinal.
- **Fundamento:** C192 y C197 piden definir antes de aplicar. R01 extiende ese orden al método; R05 orienta a evitar la repetición de la definición de e(x). Caro no anotó directamente este pasaje metodológico.
- **Cambio aplicado:** se adelantó la definición del codificador, su escala y la selección de I a la ecuación de observación local. Se eliminó la oración que repetía que e(x) transforma la espera en un nivel entero y se mantuvo la explicación completa. La observación vecinal, las calibraciones y la figura conservan su contenido.
- **Aprobado:** sí; queda comprendido en «Autorizo todo», autorización expresa del usuario para aplicar el plan completo.
- **Aplicado:** sí. Durante la revisión visual, el párrafo vecinal comenzaba con una sola línea al pie de página; se añadió \Needspace{6\baselineskip} antes de ese párrafo para mantenerlo unido en la página siguiente.
- **Verificado:** sí. latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex terminó correctamente con 162 páginas. La página física 98 (impresa 74) muestra definiciones y ecuación local; la página física 99 (impresa 75) inicia con el párrafo vecinal completo y contiene la figura. El diff de esta ficha no modifica ecuaciones, cifras ni citas. git diff --check no informa errores; el único aviso de compilación es el ya conocido de tracklang para español.
- **Cierre:** ficha aplicada y verificada. La siguiente intervención requiere una ficha independiente.

## Ficha 8 — Alcance explícito de la ejecución sin interfaz gráfica

- **Ubicación:** 5-metodologia.tex, subsección «Entorno de simulación» y Sección 3.7.1 «Entorno de cómputo y envío de trabajos».
- **Diagnóstico:** «Las ejecuciones se realizaron sin interfaz gráfica» estaba al final de un párrafo sobre truncamiento y objetivos de valor. El antecedente de «las ejecuciones» podía confundirse con todos los procedimientos o con el comportamiento del entorno.
- **Fundamento:** R06 pide sujetos y antecedentes inequívocos; R08 distingue la descripción de una configuración del alcance de las ejecuciones documentadas. Es una precisión de referentes aplicada a metodología, no una corrección literal anotada por Caro.
- **Cambio aplicado:** se trasladó la oración al apartado de infraestructura y se identificó su alcance: «Las ejecuciones de la comparación A/C se realizaron sin interfaz gráfica». El texto sobre terminación y truncamiento quedó dedicado a esa operación.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** sí; se movió y precisó el sujeto de la oración, sin cambiar el dato.
- **Verificado:** sí. El diff de esta ficha contiene solo el traslado y la precisión de alcance. latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex terminó correctamente con 162 páginas. La página física 118 (impresa 94) sitúa la afirmación en el apartado de infraestructura, junto a la información sobre Toko; la inspección visual confirma que el párrafo se lee de forma continua. No hay avisos nuevos; permanece el aviso conocido de tracklang para español. git diff --check no informa errores.
- **Cierre:** ficha aplicada y verificada. La siguiente intervención requiere una ficha independiente.

## Ficha 9 — Explicitar cómo se reponderan los factores de HAPPO

- **Ubicación:** 5-metodologia.tex, subsección «Agentes y algoritmos de aprendizaje», etiqueta subsección mecanismos_algoritmos.
- **Diagnóstico:** «ajusta la ponderación de los factores» no explicaba qué operación modifica esos factores ni cómo se relaciona con las actualizaciones de los actores.
- **Fundamento:** la observación C032 de Caro pide una expresión más transparente que «repondera», como «ajusta la ponderación [...] según»; se refiere a la introducción y se aplica aquí por analogía, no como comentario directo a metodología. R01 pide explicar la operación antes de remitir al detalle; R23 pide aclarar los términos especializados. El apéndice A.6 documenta que la razón de probabilidades multiplica los factores pendientes y que no produce otro paso de gradiente para esos actores.
- **Cambio aplicado:** se especificó que el crítico se actualiza al inicio de cada época; después, cada actor recibe un paso de gradiente sobre el lote completo. Los factores parten de ventajas individuales estandarizadas. Tras actualizar un actor, la razón de probabilidad de cada acción bajo la política actualizada y bajo la política que generó la muestra multiplica los factores pendientes; se aclara que no se actualizan por gradiente esos actores en ese momento. Se mantuvieron las remisiones y la cautela sobre la diferencia entre adaptación y formulación teórica.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** sí. Se presentó la forma española «época» mediante \glsdisp{epoca_entrenamiento}{época}, conservando el enlace y sin alterar la entrada del glosario.
- **Verificado:** sí. Se ejecutaron pdflatex con SyncTeX, makeglossaries y latexmk con SyncTeX; la salida final tiene 162 páginas y el glosario contiene la entrada. La página física 102 (impresa 78) se revisó visualmente. qpdf confirma que el enlace de «época» apunta a glo:epoca_entrenamiento. El log final solo contiene el aviso conocido de tracklang para español; git diff --check no informa errores.
- **Cierre:** ficha aplicada y verificada. La siguiente intervención requiere una ficha independiente.

## Ficha 10 — Citar y completar la referencia de PyTorch

- **Ubicación:** 5-metodologia.tex, Sección «Sistema de control multiagente», y la entrada pytorch de bibliografia.bib.
- **Diagnóstico:** el texto atribuía a PyTorch el cálculo de las salidas de las redes y la actualización de sus parámetros, pero no citaba la fuente; la entrada existente omitía la mayoría de los autores y los datos de publicación.
- **Fundamento:** R19 pide respaldar las herramientas con su publicación o documentación oficial; R20 pide comprobar autoría y datos bibliográficos. H34 estaba pendiente de verificación. Caro no anotó directamente esta afirmación.
- **Verificación de fuente:** la ficha oficial de NeurIPS identifica el título, los 21 autores, el volumen de Advances in Neural Information Processing Systems y las páginas 8026–8037. Su resumen describe PyTorch como biblioteca de aprendizaje automático. Fuente: https://proceedings.neurips.cc/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract.html
- **Cambio aplicado:** se agregó \cite{pytorch} junto a la afirmación y se convirtió la entrada de artículo incompleta en un registro @inproceedings clásico con autores completos, título, volumen, páginas, año, idioma y enlace oficial. Esta ficha amplía el alcance al archivo bibliográfico, conforme a H34 y a la autorización general del usuario.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** sí; el cambio se limitó a la oración de atribución y a la entrada pytorch.
- **Verificado:** sí. latexmk ejecutó BibTeX y produjo un PDF de 162 páginas; main.blg informa cero advertencias. No hay citas indefinidas ni errores nuevos en main.log, y qpdf --check no encuentra errores de sintaxis o de flujo. Se revisaron visualmente la página física 96 (uso y cita) y la 160 (entrada bibliográfica); la lista no presenta desbordes. git diff --check no informa errores. Permanece el aviso conocido de tracklang para español.
- **Cierre:** ficha aplicada y verificada; H34 queda resuelto para la atribución de PyTorch en metodología.

## Ficha 11 — Apertura de búsqueda y definición del ensayo: conservar

- **Ubicación:** 5-metodologia.tex, Sección «Entrenamiento y búsqueda de hiperparámetros», etiqueta sec:experimentos_hiperparametros.
- **Diagnóstico:** no se confirma un problema de comprensión o alcance que requiera una reformulación.
- **Fundamento:** R01 y R03 orientan a presentar la tarea y su recorrido; R08 distingue el diseño y los procedimientos documentados de la evidencia de ejecución. Caro no anotó directamente este pasaje metodológico.
- **Texto actual y resolución propuesta:** conservar el párrafo:

  > Con los agentes, las acciones y las señales de aprendizaje definidos, la \acrfull{acr-hpo} explora combinaciones de valores que regulan el entrenamiento y produce configuraciones candidatas para comparar los algoritmos. El espacio de búsqueda fija los rangos y las opciones permitidos. Cada \gls{ensayo_hpo} entrena una configuración propuesta; el presupuesto limita la cantidad de ensayos y su duración máxima, medida en \glspl{iteracion_entrenamiento}. Una iteración puede incluir varios episodios o fragmentos y no equivale necesariamente a una simulación completa.

- **Justificación:** el párrafo identifica las entradas disponibles, el producto de la búsqueda, el significado del ensayo y los límites del presupuesto. Los párrafos siguientes asignan funciones distintas a Optuna, Ray Tune y ASHA. Las menciones posteriores a fase 1 y fase 2 se formulan como diseño o protocolo, no como prueba autónoma de que todas las campañas se ejecutaron.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** no se modificó 5-metodologia.tex; se registra la conservación propuesta.
- **Verificado:** sí. La fuente coincide con el texto citado y se revisó en el PDF vigente, páginas físicas 103–104 (impresas 79–80). La extracción y la inspección visual confirman que la definición de la tarea y el ensayo se lee antes de describir el calendario de las fases. No se requiere compilación adicional porque no cambió ninguna fuente.
- **Cierre:** decisión de conservar registrada. La siguiente ficha revisa por separado las distribuciones de los dominios.

## Ficha 12 — Definiciones de uniforme continua y loguniforme: conservar

- **Ubicación:** 5-metodologia.tex, subsección «Fase 1: búsqueda amplia», etiqueta subsec:hpo_phase1.
- **Diagnóstico:** las distribuciones se definen antes de remitir a los dominios y la remisión promete contenido que efectivamente existe.
- **Fundamento:** R01 pide definir antes de aplicar; R16 y R22 requieren que los enlaces visibles y sus destinos sean útiles. La extensión a este pasaje no corresponde a una anotación directa de Caro.
- **Texto actual y resolución propuesta:** conservar: «Una distribución uniforme continua asigna la misma probabilidad a intervalos de igual longitud dentro del rango permitido. Una distribución loguniforme es uniforme en la escala logarítmica de una variable positiva y asigna la misma probabilidad a intervalos con igual razón entre sus extremos; permite explorar distintas escalas de magnitud. Los rangos completos, las alternativas y los factores fijos figuran en las tablas \ref{tab:dominios_fase1_ppo}, \ref{tab:dominios_fase1_idqn} y \ref{tab:factores_fase1} de la Sección \ref{subsec:espacio_busqueda_fase1}».
- **Justificación:** la primera definición expresa la uniformidad por longitud; la segunda, por razón multiplicativa. La Sección A.5.4 contiene las tres tablas indicadas y explica sus dominios; los usos enlazados del glosario llevan a sus entradas.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** no se modificó 5-metodologia.tex; se registra la conservación propuesta.
- **Verificado:** sí. En la fuente y en la página física 106 (impresa 82) se comprobó el orden y la lectura del bloque. qpdf confirma que los usos visibles enlazan con glo:distribucion_uniforme_continua y glo:distribucion_loguniforme. Las etiquetas tabulares existen en la Sección A.5.4. No se requiere recompilación porque no cambió ninguna fuente.
- **Cierre:** decisión de conservar registrada. La siguiente ficha revisa por separado el alcance de diseño, protocolo y ejecución.

## Ficha 13 — Distinguir campañas documentadas de entrenamiento previsto: conservar

- **Ubicación:** Secciones «Entrenamiento de las variantes en las tres redes sintéticas» (etiqueta subsec:cooperacion_multiescenario) y «Entrenamiento y evaluación de los modelos finales» (etiqueta sec:evaluacion_modelos_finales).
- **Diagnóstico:** no se confirma una confusión entre lo ejecutado y lo previsto en estos pasajes.
- **Fundamento:** Caro pide en C280 identificar de qué estudio se habla y no redactar como realizado un procedimiento aún no ejecutado; C284 limita las afirmaciones a las fuentes consultadas. Son anotaciones del marco teórico, aplicadas aquí por analogía mediante R07/R08, no pedidos directos sobre estas secciones.
- **Texto actual y resolución propuesta:** conservar los tiempos y sujetos actuales. La campaña A/C se informa en pasado: «La comparación ampliada utilizó MAPPO…» y «Se entrenaron 24 pares por red»; para los modelos finales, el texto distingue el diseño con «el protocolo prevé entrenar» y «El protocolo contempla veinte simulaciones…», condicionado a que haya configuraciones seleccionadas.
- **Justificación:** las remisiones a la receta histórica acompañan los datos de A/C; el protocolo final no se presenta como una campaña realizada y cuantifica sus 320 simulaciones como condicionales. Cambiar ambos bloques al mismo tiempo verbal borraría esa diferencia probatoria.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** no se modificó 5-metodologia.tex; se registra la conservación de la distinción.
- **Verificado:** sí. La inspección de la fuente y del PDF confirma los pasados de A/C en la página física 111 (impresa 87) y el condicional del entrenamiento final en la página física 117 (impresa 93). Ambos bloques se leen completos; no se requiere recompilación porque no hubo cambio de fuentes.
- **Cierre:** decisión de conservar registrada. La siguiente ficha revisa por separado los criterios de selección.

## Ficha 14 — Atribuir las condiciones urbanas al protocolo de selección

- **Ubicación:** 5-metodologia.tex, subsección «Mendoza» dentro de «Criterios de selección de configuraciones», etiqueta subsec:seleccion_mendoza.
- **Diagnóstico:** «Las ejecuciones usan el escenario v14…» podía leerse como confirmación de una campaña urbana ejecutada. El párrafo describe condiciones definidas en el protocolo y no documenta resultados de esas ejecuciones.
- **Fundamento:** R07/R08 separan diseño, procedimiento y evidencia. AGENTS.md advierte que una configuración o protocolo no acredita una campaña urbana ejecutada. No se afirma que no haya habido ejecuciones; se precisa qué establece la fuente citada.
- **Texto actual y cambio aplicado:** se sustituyó «La selección compara cada candidato… Las ejecuciones usan…» por «El protocolo urbano de selección compara cada candidato con los programas semafóricos conservados en la red de Mendoza, tanto fijos como accionados (Sección \ref{sec:parametros_sumo}). Para esas comparaciones, especifica el escenario v14, el archivo de flujos congelado … y la configuración …». La ventana, el calentamiento y los archivos se conservaron.
- **Justificación:** hace explícito que el pasaje resume las condiciones del protocolo sin convertirlas en evidencia de corridas. También mantiene claro que el punto de comparación son los programas de referencia.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** sí; se modificó únicamente la atribución de esas condiciones.
- **Verificado:** sí. El diff de esta ficha contiene solo la precisión de sujeto y alcance. latexmk con SyncTeX terminó correctamente con 162 páginas. La página física 109 (impresa 85) se revisó visualmente; conserva los parámetros y el flujo de lectura. El log no presenta avisos nuevos y git diff --check no informa errores.
- **Cierre:** ficha aplicada y verificada. La siguiente ficha revisa por separado las métricas y las incidencias.

## Ficha 15 — Nombrar los registros de incidencias antes de equipararlos

- **Ubicación:** `5-metodologia.tex`, subsubsección «Incidencias de la simulación», etiqueta `subsec:incidencias_simulacion` (línea auxiliar 633).
- **Diagnóstico:** mejora de claridad y precisión. «Su correspondencia» no nombraba qué registros se compararían; además, la relación entre el contador nativo y el conteo TraCI debe comprobarse para cada procedimiento antes de sustituir uno por otro.
- **Fundamento:** R06, para nombrar los antecedentes de forma inequívoca, y R08, para distinguir una fuente disponible de una equivalencia empírica verificada. La aplicación a este pasaje es una extensión metodológica: no se encontró una anotación de Caro sobre estos contadores concretos. R13 respalda que la métrica se presente con una definición y un alcance claros, sin alterar sus valores.
- **Texto anterior:** «Los inicios de teletransporte se utilizan como indicador de incidencias operacionales. En la selección de candidatos, el análisis A/C y la evaluación final se cuentan sus inicios mediante TraCI durante la ventana de control; un vehículo puede contribuir con más de un evento. La salida Summary de `\acrshort{acr-sumo}` dispone de un contador nativo `\texttt{teleports}`. Antes de sustituir un registro por otro, debe comprobarse su correspondencia».
- **Texto propuesto y aplicado:** «Los inicios de teletransporte se utilizan como indicador de incidencias operacionales. En la selección de candidatos, el análisis A/C y la evaluación final se cuentan sus inicios mediante TraCI durante la ventana de control; un vehículo puede contribuir con más de un evento. Antes de usar el contador nativo `\texttt{teleports}` de la salida Summary de `\acrshort{acr-sumo}` en lugar de los inicios registrados mediante TraCI, debe comprobarse que ambos registros sean equivalentes para el procedimiento correspondiente».
- **Alternativa de conservar:** mantener la frase anterior; se descarta porque «su correspondencia» deja implícitos los dos registros y el nivel al que se exige la comprobación.
- **Justificación:** nombra explícitamente el contador Summary y los inicios registrados mediante TraCI, y limita la equivalencia al procedimiento pertinente. No afirma que se hayan comparado ni que sean equivalentes; tampoco modifica el método de conteo, sus ventanas ni sus cifras.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** sí; se cambió únicamente la formulación de la comprobación de equivalencia en el párrafo de incidencias.
- **Verificado:** sí. El diff de la intervención afecta solo ese párrafo; `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` terminó correctamente y el PDF conserva 162 páginas. La página física 114 (impresa 90) se inspeccionó visualmente: el párrafo y su relación con las secciones siguientes se leen con claridad. `git diff --check` no informa errores; el único aviso del log es el conocido de `tracklang` para español.
- **Cierre:** ficha aplicada y verificada. La ficha siguiente revisa por separado la presentación del análisis pareado.

## Ficha 16 — Análisis pareado e identificación de intervalos: conservar

- **Ubicación:** subsección «Análisis por pares y criterio de decisión», etiqueta `sec:experimentos_evaluacion`, en particular la explicación de la Figura `fig:analisis_pareado` y los dos párrafos de intervalos (líneas auxiliares 644–676).
- **Diagnóstico:** no se confirma una dificultad de lectura que justifique reformular. La figura presenta el flujo de pareo y remuestreo; la prosa distingue los intervalos percentiles del intervalo basado en *t* de Student.
- **Fundamento:** R05/R09/R10 para mantener conectados el procedimiento, el diagrama y su explicación; R06 para identificar cada procedimiento estadístico; R08 para conservar las cautelas sobre su cobertura. Las observaciones de Caro que sustentan estas reglas se refieren al marco teórico y se aplican aquí por analogía; no se encontró un comentario suyo sobre este análisis específico.
- **Texto actual y resolución propuesta:** conservar la Figura 3.12 y los párrafos: «Se informan intervalos percentiles del 95\% y del 98,33\%. Este último aplica la corrección de Bonferroni a los tres contrastes A/C, uno por cada red, para cada medida por separado; no ajusta simultáneamente todas las métricas. También se calcula un intervalo basado en la distribución $t$ de Student como análisis de sensibilidad. Los procedimientos percentil y $t$ son aproximaciones con 24 pares y su cobertura no está garantizada. Se conservan los valores extremos y se revisa su influencia».
- **Alternativa de cambio:** aclarar o abreviar estos pasajes solo si se identifica una ambigüedad concreta; no se identificó ninguna que compense el riesgo de debilitar las cautelas o la distinción entre procedimientos.
- **Justificación:** la prosa ya nombra cada método, precisa el alcance del ajuste de Bonferroni y limita la interpretación de la cobertura; la figura permite seguir desde los pares hasta el remuestreo. La página es densa, pero la inspección visual no mostró solapamientos, cortes ni texto ilegible.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** no se modificó `5-metodologia.tex`; se registra la conservación de la figura, su explicación y las cautelas estadísticas.
- **Verificado:** sí. La fuente y las páginas físicas 115–116 (impresas 91–92) se comprobaron. La Figura 3.12 representa los 24 pares, las cinco evaluaciones compartidas, el promedio por política, la diferencia C–A y los 20.000 remuestreos; la prosa separa los intervalos percentiles del intervalo *t*. No se requiere recompilación para esta decisión de conservación.
- **Cierre:** resolución de conservación registrada. La ficha siguiente verificará en el PDF el formato numérico del codificador y los ajustes de página visibles.

## Ficha 17 — Formato del codificador y saltos de página: conservar

- **Ubicación:** Figura `fig:codificacion_carriles` en `5-metodologia.tex` y `imagenes/metodologia_v2_encoder.pdf`; además, los controles de paginación de metodología con `\Needspace`, `\clubpenalty` y `\widowpenalty`.
- **Diagnóstico:** verificación visual pendiente al abrir la ficha. En la versión actual no se observa un defecto que justifique modificar el separador de miles ni los controles de página.
- **Fundamento:** R12/R18/R24 exigen consistencia de formato, evaluación visual de la página y lectura sin fragmentos u orfandades. No se encontró una observación directa de Caro sobre esta figura o estos saltos; la revisión aplica esas reglas al PDF actual.
- **Texto/elemento actual y resolución propuesta:** conservar la Figura 3.9, con valores del eje `0, 100, …, 900, 1.000, 1.100, 1.200, 1.300`, y la leyenda `M_{\mathrm{lane}}=1136` veh·s. Conservar también la distinción entre el ejemplo ilustrativo con `I=22` y el uso de `I=17` en A/C. No se propone cambiar coordenadas, cifras, parámetros, tamaño ni los controles de paginación.
- **Alternativa de cambio:** modificar el formato del eje o los saltos solo si la inspección mostrara un valor mal agrupado, ilegible, cortado o separado de la explicación; no se encontró ese caso.
- **Justificación:** el punto agrupa correctamente los millares en el formato español y se distingue de la coma decimal. La figura conserva sus valores y permite leer con claridad el umbral 1136. Los controles de página dejan títulos con desarrollo, fórmulas junto a sus definiciones y párrafos sin líneas huérfanas; el espacio en blanco al final de la página física 119 corresponde al cierre del capítulo y no separa contenido relacionado.
- **Aprobado:** sí; queda comprendido en «Autorizo todo».
- **Aplicado:** no se modificó `5-metodologia.tex`, la figura ni el generador; se registra la conservación de los elementos inspeccionados.
- **Verificado:** sí. Se revisó el PDF actual de 162 páginas. La Figura 3.9 se inspeccionó en la página física 99 (impresa 75). También se revisaron las páginas físicas 83, 95, 98, 104, 107, 109, 112–116 y 119, que contienen los controles de paginación del capítulo. No se vieron cortes, superposiciones ni huérfanas en esos puntos. La compilación final no requiere repetirse por esta conservación; el log presenta solo el aviso conocido de `tracklang`.
- **Cierre:** bloque de formato y página resuelto mediante conservación. Se completará una verificación final del diff, las referencias estructurales y la compilación estabilizada.

## Ficha 18 — Explicitar en el marco teórico el orden implementado de HAPPO (H32)

- **Ubicación:** `4-marco_teorico.tex`, párrafo de la adaptación semafórica posterior al Algoritmo `alg:happo`, dentro de la Sección `subsec:happo`. Ampliación acotada del alcance para resolver H32, autorizada mediante «Autorizo todo» y «Continuar» después de identificar este pendiente.
- **Diagnóstico:** metodología y apéndice especifican que el crítico se actualiza antes de los actores; el párrafo que presenta la adaptación en el marco teórico omitía esa diferencia respecto del pseudocódigo que acaba de mostrar.
- **Fundamento:** R01/R07/R08/R22, por extensión de C028–C034, C238 y C280. Esas observaciones piden distinguir la propuesta propia, sus operaciones y la formulación tomada de las fuentes; no ordenan hacer idénticos los dos procedimientos. R04 justifica separar la operación y sus límites; R17 exige «Sección» en la remisión numerada.
- **Comprobación documental:** el Algoritmo 3 de Kuba et al. (ICLR 2022), apéndice D.4, página 24, actualiza los actores y después la red de valor; el Algoritmo 4 del artículo de Zhong et al. (JMLR 2024), apéndice C.4, mantiene ese orden. Fuentes: [ICLR](https://arxiv.org/pdf/2109.11251#page=24) y [JMLR](https://www.jmlr.org/papers/v25/23-0488.html); copia local de JMLR en `Papers/HAPPO.pdf`.
- **Comprobación del código:** se inspeccionó `cooperation_multiscenario_20260920/frozen_v5/src/marlTLC/agents/multi_agent/happo/torch/happo_torch_learner.py` en el proyecto local `marl-tlc`: el bucle de épocas llama a `_update_critic` antes de inicializar los factores y recorrer los actores (líneas 246–278). Su SHA-256 es `a412cf79912384fb62d01a6394be64f53bab63d94444049e90823978a034c570`. El contraste acredita el orden de esa versión conservada, no el código de cualquier campaña histórica.
- **Texto anterior:** tras la explicación de las ventajas individuales, el párrafo pasaba directamente a «Esta adaptación utiliza ventajas individuales, mientras que la demostración teórica parte de una recompensa global compartida».
- **Propuesta exacta y cambio aplicado:** añadir «A diferencia del Algoritmo \ref{alg:happo}, la implementación actualiza el crítico al comienzo de cada época, antes de los actores (Sección \ref{subsec:mecanismos_algoritmos})». Separar en el párrafo siguiente la cautela existente sobre recompensa compartida y garantías. Se corrigió «sección» a «Sección» en la remisión del mismo pasaje.
- **Alternativa de conservar:** mantener la distinción únicamente en metodología; se descarta porque el marco teórico anuncia una adaptación inmediatamente después de un pseudocódigo con otro orden y omite esa diferencia localmente.
- **Justificación:** permite al lector distinguir el pseudocódigo de referencia del procedimiento implementado. Se conserva íntegra la cautela sobre garantías; no se cambia el algoritmo, su fórmula ni la implementación. Tras observar una línea viuda en la primera compilación, se añadió una protección local de párrafo con `\widowpenalty=10000` y se verificó su efecto.
- **Aprobado:** sí, mediante la autorización general y el pedido de continuar con H32.
- **Aplicado:** sí, únicamente en el pasaje indicado del marco teórico y en este registro.
- **Verificado:** sí. Dos ciclos de `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` terminaron correctamente; el segundo comprueba el ajuste de paginación observado. Se inspeccionaron las páginas físicas 76–77 (impresas 52–53); las referencias conducen al Algoritmo 4 y a la Sección 3.3.3. El PDF mantiene 162 páginas y el log solo presenta el aviso conocido de `tracklang`, sin referencias indefinidas ni desbordes nuevos.
- **Cierre:** H32 resuelto para la correspondencia entre el pseudocódigo presentado y la versión congelada inspeccionada. No se generaliza la comprobación a otras versiones o campañas.

## Ficha 19 — Unificar los miles en la tabla de procedencia de Mendoza (parte de H20)

- **Ubicación:** `8-apendice_arquitectura.tex`, Tabla `tab:fuentes_mendoza`, Sección `sec:procedencia_mendoza`, líneas auxiliares 289–293. Ampliación acotada al apéndice para resolver el pendiente H20.
- **Diagnóstico:** la tabla agrupaba con espacio fino cantidades que metodología presenta con punto de miles. Ambos formatos se comprenden, pero su alternancia para los mismos datos incumple la convención adoptada en R18.
- **Fundamento:** R18, derivada de C006. La observación original pide uniformar cifras; el uso concreto de punto de miles con coma decimal es la convención ya adoptada en metodología, no una norma universal atribuida a Caro.
- **Propuesta exacta y cambio aplicado:** `25\,283,85` → `25.283,85`; `25\,175,84` → `25.175,84`; `2\,316,54` → `2.316,54`; `290\,000` → `290.000`; `260\,000` → `260.000`; `16\,744` → `16.744`; `14\,986` → `14.986`.
- **Alternativa de conservar:** mantener espacios finos. Se descarta para esta tabla porque repetiría los mismos datos de Mendoza con una convención distinta de la prosa metodológica; no se considera incorrecto el espacio fino por sí mismo.
- **Justificación:** uniforma la lectura de cantidades comparables, sin cambiar su valor, precisión, unidad ni procedencia. Los perfiles de 33/32 días, 290.000/260.000 vehículos diarios y sus factores de expansión siguen separados.
- **Aprobado:** sí, mediante la autorización general y el pedido de continuar con H20.
- **Aplicado:** sí; siete separadores de miles en cuatro filas de una única tabla.
- **Verificado:** sí. El diff frente a `/tmp/h20-tabla-antes.tex` contiene solo las sustituciones enumeradas. `latexmk` con SyncTeX terminó correctamente; se inspeccionó la Tabla A.3 en la página física 130 (impresa 106), con columnas alineadas y cifras legibles. No hay avisos nuevos, referencias indefinidas ni desbordes; permanece el aviso conocido de `tracklang`.
- **Cierre:** resuelto el formato de la tabla. La prosa que menciona el flujo del archivo y los dominios de IDQN requieren fichas separadas antes de cerrar H20.

## Ficha 20 — Unificar los miles del flujo citado en la prosa del apéndice (parte de H20)

- **Ubicación:** `8-apendice_arquitectura.tex`, Sección `sec:procedencia_mendoza`, párrafo «Los logs canónicos…», línea auxiliar 299.
- **Diagnóstico y fundamento:** la tabla ya usa el punto de miles; el párrafo conserva espacios finos en dos valores de la misma familia. R18, derivada de C006, exige una convención uniforme para estas cantidades comparables.
- **Texto anterior y propuesta exacta:** «el encabezado del archivo declara 14\,986,32 vehículos por hora. El registro de generación informa 14\,986 vehículos por hora redondeados» → «el encabezado del archivo declara 14.986,32 vehículos por hora. El registro de generación informa 14.986 vehículos por hora redondeados».
- **Alternativa de conservar:** mantener el espacio fino en la prosa; se descarta porque reinstalaría la alternancia de separadores junto a la tabla corregida.
- **Justificación:** unifica el formato y conserva tanto la precisión diferente de las dos cifras como la advertencia de que pertenecen a artefactos distintos y no prueban qué ruta consumieron las ejecuciones originales.
- **Aprobado:** sí, mediante la autorización general y el pedido de continuar.
- **Aplicado:** sí, únicamente los dos separadores de miles de ese párrafo.
- **Verificado:** sí. El diff frente a `/tmp/h20-flujo-antes.tex` contiene solo las dos sustituciones; `git diff --check` no informa errores. `latexmk` con SyncTeX terminó correctamente y se revisó visualmente la página física 131 (impresa 107). Las cifras y su alcance se leen completos; el log solo presenta el aviso conocido de `tracklang`, sin desbordes nuevos ni referencias indefinidas.
- **Cierre:** prosa de procedencia corregida. Se continúa con los dominios tabulares de IDQN como intervención independiente.

## Ficha 21 — Agrupar los contadores de miles de IDQN en fase 1 (parte de H20)

- **Ubicación:** `8-apendice_arquitectura.tex`, Tabla `tab:dominios_fase1_idqn`, filas de actualización de red objetivo, reducción de exploración y pasos antes de aprender (líneas auxiliares 469–473).
- **Diagnóstico:** los mismos tipos de contadores se muestran sin agrupación en esta tabla y con agrupación mediante espacio fino en la tabla refinada. La comparación entre ambas se facilita con una presentación uniforme.
- **Fundamento:** R18 y C006, aplicadas a valores de dominios comparables, respetando las excepciones para versiones, semillas e identificadores.
- **Propuesta exacta y cambio aplicado:** `{500; 1000; 2000; 5000}` → `{500; 1.000; 2.000; 5.000}`; `{5000; 10000; 20000}` → `{5.000; 10.000; 20.000}`; `{1000; 2000; 5000}` → `{1.000; 2.000; 5.000}`. En matemáticas LaTeX se escribe `{.}` para el punto de agrupación y se conserva `\,` después de cada punto y coma entre alternativas.
- **Alternativa de conservar:** mantener estos contadores sin agrupar y normalizar solo los separadores ya presentes. Se prefiere agruparlos para que los mismos valores se lean igual en las dos tablas de IDQN.
- **Justificación:** uniforma tres familias de contadores sin modificar sus valores, alternativas, unidades ni tipo de muestreo. No se extiende la agrupación a literales de código, versiones o semillas.
- **Aprobado:** sí, mediante la autorización general y el pedido de continuar.
- **Aplicado:** sí; nueve separadores añadidos en tres filas de una tabla.
- **Verificado:** sí. Al retirar de la propuesta únicamente los nueve grupos `{.}`, el bloque fuente vuelve a ser idéntico al anterior. `latexmk` con SyncTeX terminó correctamente y la Tabla A.6 se revisó visualmente en la página física 137 (impresa 113): las celdas caben y las alternativas se distinguen. El log solo presenta el aviso conocido de `tracklang`.
- **Cierre:** formato de la tabla inicial resuelto. La tabla refinada y su generador requieren una intervención dependiente separada.

## Ficha 22 — Unificar los miles de los dominios refinados de IDQN y su generador (cierre de H20)

- **Ubicación:** Tabla `tab:dominios_idqn_v2`, incluida desde `imagenes/metodologia_v2_dominios_idqn.tex` en el apéndice; función `latex_number` de `imagenes/metodologia_v2_generar_dominios.py`.
- **Diagnóstico:** tres filas de contadores usaban espacio fino como agrupador de miles, distinto del punto adoptado para cantidades comparables y para los dominios iniciales de IDQN. El generador debía conservar el mismo criterio en futuras regeneraciones.
- **Fundamento:** R18, derivada de C006, y R26 para mantener reproducible el formato del artefacto generado. La intervención en generador y tabla es una unidad dependiente: editar solo la tabla permitiría reintroducir el formato anterior.
- **Propuesta exacta y cambio aplicado:** en las filas de reducción de exploración, pasos antes de aprender y actualización de la red objetivo se sustituyen las agrupaciones `1\,000`, `2\,000`, `5\,000`, `10\,000` y `20\,000` por `1{.}000`, `2{.}000`, `5{.}000`, `10{.}000` y `20{.}000`, respectivamente, en sus 22 apariciones. El generador sustituye el agrupador entero `r"\,"` por `r"{.}"`; permanecen los espacios después del punto y coma entre alternativas.
- **Alternativa de conservar:** mantener espacio fino en esta tabla o cambiar solo el archivo generado. Se descartan porque la primera opción conserva la inconsistencia y la segunda no mantiene la corrección al regenerar.
- **Justificación:** permite comparar contadores entre fase 1 y fase 2 con el mismo formato. El agrupador entre llaves es tipográfico; los valores de los dominios y las reglas de muestreo no cambian.
- **Comprobación de origen:** se utilizó el manifiesto `experiments/marl_experiments/tuning/phase2_refined/informed_domains_rho0_v3.json` de la copia `phase2-cluster`. SHA-256: `41c816c13779115996e6f7def042553d8d3c1ee29051e8d6383a113333d98221`. Antes de editar se comprobó que la tabla IDQN correspondía a su salida, salvo saltos de línea. Después, la comparación de las doce celdas algorítmicas por escenario verificó que solo cambia el agrupador, con iguales valores, extremos, alternativas y muestreos.
- **Aprobado:** sí, mediante la autorización general y el pedido de continuar con H20.
- **Aplicado:** sí; una línea del generador y las tres filas correspondientes de la tabla IDQN, regeneradas manteniendo la disposición previa de la fuente.
- **Verificado:** sí. La salida actual de la función de generación para IDQN coincide con el archivo de tabla salvo espacios de fuente. `latexmk` con SyncTeX terminó correctamente; la Tabla A.12 se inspeccionó en la página física 144 (impresa 120), con todas las columnas legibles y sin solapamientos. El PDF mantiene 162 páginas; el log solo presenta el aviso conocido de `tracklang` y `git diff --check` no informa errores.
- **Cierre:** H20 resuelto para las ocurrencias inventariadas en metodología, apéndice y tablas generadas. El criterio es punto en las cantidades agrupadas y coma decimal, con la misma agrupación en los contadores comparables de IDQN. No se aplica a versiones, rutas, semillas, identificadores ni literales de código; tampoco obliga a agrupar cada parámetro de cuatro cifras.

## Ficha 23 — Corregir un nombre de autor en la fuente de HAPPO

- **Ubicación:** `bibliografia.bib`, campo `author` de `kuba2021trust`, línea auxiliar 499. Hallazgo concreto de la comprobación de fuentes de H32; ampliación bibliográfica acotada bajo la autorización general y el pedido de continuar.
- **Diagnóstico:** la entrada atribuye el artículo a «Fuchun Sun», mientras que la portada de la publicación y su ficha identifican a «Fanglei Sun».
- **Fundamento:** R20, derivada de C066, exige contrastar la autoría con la publicación consultada. Es una corrección factual comprobada, no una decisión de estilo ni un pedido literal de Caro sobre esta entrada.
- **Fuente:** [Kuba et al., ICLR 2022, página 1](https://arxiv.org/pdf/2109.11251#page=1) y su [ficha de arXiv](https://arxiv.org/abs/2109.11251).
- **Propuesta exacta y cambio aplicado:** sustituir `Sun, Fuchun` por `Sun, Fanglei` en ese campo.
- **Alternativa de conservar:** mantener la autoría incorrecta; se descarta porque el nombre no coincide con la fuente primaria.
- **Justificación:** identifica correctamente a un coautor de la publicación utilizada para el contraste de HAPPO. Se conserva la clave de cita, el año, el título, el resto de autores y la compatibilidad de BibTeX clásico.
- **Aprobado:** sí; autorización general y continuación de la verificación documental de H32.
- **Aplicado:** sí, un nombre propio en una única entrada bibliográfica.
- **Verificado:** sí. El diff frente a `/tmp/h32-bibliografia-antes.bib` contiene únicamente esa sustitución. `latexmk` con SyncTeX ejecutó BibTeX y estabilizó las referencias; `main.bbl` y la entrada impresa muestran «Fanglei Sun». Se inspeccionó la página física 158 (impresa 134), sin cortes ni desbordes. El PDF conserva 162 páginas; BibTeX no informa advertencias y el único aviso de LaTeX es el conocido de `tracklang`. `qpdf --check main.pdf` y `git diff --check` terminan correctamente.
- **Cierre:** error de autoría corregido y verificado. No se presenta esta comprobación de una entrada como validación de toda la bibliografía.

## Ficha 24 — Actualizar alcance, autorización y estado de cierre del registro

- **Ubicación:** apertura, alcance y resumen de pendientes de este registro.
- **Diagnóstico:** el resumen seguía presentando H20, H32 y H34 como pendientes después de las fichas que los resolvieron; el alcance y la modalidad de aprobación iniciales tampoco reflejaban las ampliaciones autorizadas y la instrucción posterior «Autorizo todo».
- **Fundamento:** R26 exige distinguir el diagnóstico histórico de lo aplicado y comprobado; la modalidad de autorización corresponde a instrucciones del usuario, no a una observación de Caro.
- **Texto anterior y propuesta:** sustituir las declaraciones «H20 sigue pendiente», «H32 requiere contrastar» y «H34 requiere verificar» por el cuadro de estado actual con alcance y fichas de respaldo. Precisar que el alcance fue inicialmente metodológico y que las ampliaciones están documentadas; registrar la autorización general posterior y mantener las fichas iniciales como historia de decisiones.
- **Alternativa de conservar:** mantener el resumen inicial y obligar al lector a reconstruir el estado a partir de las fichas. Se descarta porque presentaría como pendientes tareas ya aplicadas y verificadas.
- **Justificación:** permite distinguir las resoluciones de esta revisión de los antecedentes fechados y de una auditoría general aún no actualizada. No modifica fuentes de la tesina.
- **Aprobado:** sí; autorización general y pedido de continuar con la actualización del registro.
- **Aplicado:** sí, en la apertura, el alcance y el cuadro de estado actual de este documento.
- **Verificado:** las fichas respaldan los cuatro estados y las ampliaciones enumeradas. El antecedente del 16 de octubre se conserva íntegro. Esta modificación documental no requiere recompilar LaTeX.
- **Cierre:** registro actualizado. No quedan pendientes H16, H20, H32 o H34 dentro del alcance comprobado de esta revisión; los hallazgos de otros capítulos no se dan por resueltos mediante este cierre.

## Ficha 25 — Distinguir redondeo temporal y agregación de conteos

- **Ubicación:** `5-metodologia.tex`, etiqueta `subsubsec:mendoza_preprocesamiento_datos`, línea auxiliar 156.
- **Diagnóstico:** precisión confirmada. «Los conteos se depuraron y redondearon al intervalo…» atribuye al conteo una operación que corresponde al tiempo del registro.
- **Fundamento:** R06/R18, por extensión de las observaciones de Caro sobre referentes y magnitudes; no existe una anotación directa de Caro sobre este pasaje de metodología. El apéndice, en `subsec:procedimiento_demanda_mendoza`, confirma que se redondearon los tiempos.
- **Texto anterior:** «Los conteos se depuraron y redondearon al intervalo de 15 minutos más cercano, y se agregaron por cámara, intervalo, zona y clase vehicular».
- **Propuesta aplicada:** «Los registros se depuraron y sus marcas temporales se redondearon al intervalo de 15 minutos más cercano. Después, los conteos se agregaron por cámara, intervalo, zona y clase vehicular».
- **Alternativa de conservar:** exige reconstruir qué se redondeó a partir de una unidad temporal; se descarta por la ambigüedad concreta.
- **Justificación:** distingue operaciones y magnitudes sin modificar cifras, procedencia ni criterios de depuración.
- **Aprobado:** autorización general y pedido de revisión integral; explicado antes de editar.
- **Aplicado:** sí, exclusivamente en la oración indicada.
- **Verificado:** diff acotado; latexmk con SyncTeX estabilizado y página física 91, impresa 67, inspeccionada. Sin avisos nuevos ni cambios numéricos.
- **Cierre:** precisión aplicada y verificada.

## Ficha 26 — Precisar la función del módulo asociado a cada agente

- **Ubicación:** `5-metodologia.tex`, primera oración de `subsec:mecanismos_algoritmos`, línea auxiliar 365.
- **Diagnóstico:** ambigüedad terminológica confirmada entre módulo de política/valores y componente que coordina el aprendizaje.
- **Fundamento:** R01/R06/R23, por extensión de los pedidos de definir componentes y aclarar sujetos. No se atribuye a Caro una instrucción literal sobre la API de RLlib.
- **Texto anterior:** «RLlib vincula un módulo de aprendizaje con cada agente».
- **Propuesta aplicada:** «RLlib asocia a cada agente un módulo que calcula su política o sus valores de acción».
- **Alternativa de conservar:** mantener un nombre genérico que puede confundirse con Learner; se descarta porque la adaptación actualiza varios módulos desde un aprendiz.
- **Justificación y respaldo:** el archivo congelado `experiments/marl_experiments/tuning/core/algo_factory.py` define módulos asociados a los identificadores de agente; `HAPPOConfig` distingue su especificación RLModule de la clase Learner, cuyo bucle actualiza los actores. Se describe la función sin introducir detalles de API innecesarios en el cuerpo.
- **Aprobado:** autorización general y pedido de revisión integral; explicado antes de editar.
- **Aplicado:** sí, una oración.
- **Verificado:** latexmk con SyncTeX estabilizado; página física 101, impresa 77, revisada sin líneas aisladas ni desbordes nuevos. Se preservan los parámetros y la independencia de actores ya descritos.
- **Cierre:** terminología aplicada y verificada.

## Ficha 27 — Nombrar quién calcula la razón de probabilidades de HAPPO

- **Ubicación:** `5-metodologia.tex`, párrafo de HAPPO ampliado en la ficha 9, etiqueta `subsec:mecanismos_algoritmos`, línea auxiliar 375.
- **Diagnóstico:** referente poco claro en «Tras actualizar un actor, para cada muestra calcula…».
- **Fundamento:** R06/R23, aplicadas por significado a la identificación del responsable de una operación.
- **Texto anterior y propuesta aplicada:** «Tras actualizar un actor, para cada muestra calcula la razón…» → «Tras actualizar un actor, el componente de aprendizaje calcula para cada muestra la razón…».
- **Alternativa de conservar:** aceptar el sujeto omitido; se descarta porque el actor y el procedimiento de aprendizaje son referentes distintos en el mismo párrafo.
- **Justificación:** hace explícito el componente que ejecuta el cálculo comprobado en el aprendiz congelado. Se preservan las ventajas iniciales, la razón postactualización y su aplicación a los factores de los actores pendientes.
- **Aprobado:** autorización general y pedido de revisión integral; explicado antes de editar.
- **Aplicado:** sí, únicamente se explicita el sujeto.
- **Verificado:** latexmk con SyncTeX estabilizado y página física 102, impresa 78, inspeccionada. No cambian fórmulas, cifras ni limitaciones; no aparecen avisos nuevos.
- **Cierre:** precisión aplicada y verificada.

## Ficha 28 — Explicar las flechas del esquema de controladores

- **Ubicación:** `5-metodologia.tex`, párrafo previo a `fig:informacion_controladores`, línea auxiliar 381.
- **Diagnóstico:** mejora editorial opcional. La convención de líneas continuas y discontinuas podía inferirse de las cajas, pero no estaba explicada expresamente.
- **Fundamento:** R09/R12, extensión operativa del criterio de Caro sobre proximidad de explicaciones y convenciones visuales. No se presenta como comentario literal de Caro sobre esta figura.
- **Texto anterior:** la primera oración identifica la información de entrenamiento y ejecución de la Figura 3.10, sin nombrar la convención de las flechas.
- **Propuesta exacta aplicada:** añadir después de esa oración «Las flechas continuas muestran el flujo de datos. Las discontinuas indican el uso de las estimaciones del crítico para actualizar los actores».
- **Alternativa de conservar:** dejar la convención implícita; es interpretable, pero se prefiere explicitarla porque permite leer el diagrama sin adivinar la función de cada estilo de línea.
- **Justificación:** completa la lectura del esquema en su bloque de prosa, manteniendo el epígrafe identificatorio y el dibujo existente.
- **Aprobado:** autorización general y pedido de revisión integral; explicado antes de editar.
- **Aplicado:** sí, dos oraciones en el párrafo próximo a la figura.
- **Verificado:** fuente y figura contrastadas, control estático TikZ superado, latexmk con SyncTeX estabilizado y páginas físicas 102–103, impresas 78–79, inspeccionadas. No cambia el gráfico ni su semántica; no hay desbordes nuevos.
- **Cierre:** mejora aplicada y verificada. La revisión integral, incluidas las conservaciones y las hipótesis descartadas, está en [revision-integral-metodologia-caro-2026-10-17.md](revision-integral-metodologia-caro-2026-10-17.md).

## Verificación de cierre de la revisión actual

- Las doce ecuaciones y los seis cuerpos de tabla de metodología son idénticos a `HEAD`; se conservan sus doce figuras y sus archivos referenciados.
- Los algoritmos del marco teórico y las ecuaciones del apéndice son idénticos al inicio de esta continuación. El apéndice completo, normalizados únicamente los separadores de miles, es idéntico a su estado inicial.
- Los doce dominios por algoritmo y escenario mantienen sus valores, extremos, alternativas y muestreos. Las tablas de procedencia conservan los datos y sus limitaciones documentales.
- Se inspeccionaron las 22 fuentes LaTeX incluidas desde `main.tex`: sus 199 etiquetas son únicas y las remisiones comprobadas tienen destino. La búsqueda contextual de miles con espacio fino no encuentra casos pendientes en esas fuentes.
- La compilación con BibTeX y SyncTeX está estabilizada y el PDF tiene 162 páginas. `main.log` solo conserva el aviso conocido de `tracklang`; no hay citas o referencias indefinidas ni desbordes. BibTeX no informa advertencias.
- Se revisaron visualmente las páginas afectadas por cada ficha de esta continuación. `qpdf --check main.pdf` no detecta errores de sintaxis ni de flujo; `git diff --check` no informa errores.
- La inspección documental y del código acredita las versiones identificadas en cada ficha. El cierre editorial no acredita nuevas campañas experimentales ni elimina las limitaciones de inferencia descritas en la tesina.

### Segunda lectura integral del 17 de octubre

Se releyeron metodología completa, los cambios acumulados y las observaciones originales de Caro. Se aplicaron únicamente las fichas 25–28. El informe integral detalla el control de R01–R26, los cambios conservados, las hipótesis descartadas y la limitación del comprobador gráfico automático no disponible.

El PDF mantiene 162 páginas. Se inspeccionaron las 37 páginas de metodología y ocho páginas de cambios asociados; la comparación renderizada solo cambia las páginas físicas 91, 101 y 102. Las doce ecuaciones, seis cuerpos de tabla, doce figuras, cifras y secuencias de citas, remisiones y usos de glosario de metodología se conservan. Se verificaron 150 enlaces a 48 destinos de glosario/siglas. No se modificaron otros archivos de la tesina en esta segunda lectura.

## Antecedente del 16 de octubre de 2026

Título original: «Plan de aplicación de las reglas de Caro a metodología». El contenido siguiente se conserva como antecedente fechado. Las expresiones «actual», «completada» o «pendiente» de este bloque pertenecen al registro anterior; no se trasladan automáticamente al estado de esta revisión.

Referencias de trabajo: [reglas R01–R26](REGLAS_EDITORIALES_CARO.md), [auditoría H01–H34](revision-reglas-caro-2026-10-16.md) y [observaciones originales](TODO-comentarios-caro.md). Este plan registra el estado de metodología; no cierra hallazgos que también afectan otros capítulos.

### Límites y condiciones que deben conservarse

- Editar la fuente de metodología. Como excepción acotada, corregir el separador de miles del eje del codificador en `imagenes/metodologia_v2_generar_encoder.py` y regenerar únicamente `imagenes/metodologia_v2_encoder.pdf`, sin cambiar coordenadas ni parámetros. Consultar marco teórico, apéndice, bibliografía y glosario para comprobar destinos y definiciones; registrar aparte los cambios que necesitarían esos archivos.
- Conservar las doce ecuaciones, sus etiquetas y sus expresiones; las doce figuras y seis tablas, sus archivos y sus datos; las semillas, presupuestos, ventanas, umbrales y parámetros del protocolo. El ajuste de una leyenda o del formato de una cifra no altera su valor.
- Mantener A/C como comparación de MAPPO en las tres redes sintéticas que modifica conjuntamente observación y recompensa; preservar las diferencias entre búsqueda amplia, refinada y comparación vecinal.
- Conservar las cautelas sobre recompensas individuales y garantías HAPPO, memoria finita de espera, viajes inconclusos, selección adaptativa, inicialización y límites de inferencia.
- En Mendoza, distinguir especificación canónica, registro de generación y comprobaciones con programas de referencia. Preservar las diferencias 60/40 y 70/30 y las limitaciones de rutas y contadores primarios.
- Describir los procedimientos planificados como parte del diseño. No inferir ejecución a partir de configuraciones ni ausencia de ejecución a partir de falta de evidencia en esta revisión editorial.

### Bloques de trabajo

#### P1. Referencias y convenciones

- [x] Revisar las 75 referencias singulares en minúscula del inventario y aplicar la convención de Figura, Tabla, Ecuación y Sección (R17; H01).
- [x] Corregir las 39 menciones a «apéndice» cuyo destino es una sección interna. Conservar cada etiqueta y nombrar el objeto real (R17/R22; parte de H02).
- [x] Aplicar minúscula a los dos plurales «Figuras»/«Tablas» inventariados en el capítulo y revisar las referencias plurales a subsecciones (R17; parte de H03).
- [x] Uniformar «ejecución» y comprobar cifras/unidades, sin reemplazos sobre código, rutas ni semillas (R15/R18/R23; parte de H19/H20).

#### P2. Diseño experimental y presentación de escenarios

- [x] Llevar al texto la explicación de dependencias, alcance y cronología del flujo metodológico; dejar un epígrafe identificatorio (R02/R09/R10/R12; H06).
- [x] Reunir la explicación del diagrama temporal y la particularidad de C4 antes de los objetos que ilustran esos conceptos. Conservar los valores de los programas y distinguirlos del control aprendido (R09/R10).
- [x] Revisar la lectura de topologías y zonas de Mendoza: introducir los objetos, explicar leyendas pertinentes y evitar explicaciones extensas o repetidas en sus epígrafes (R06/R09/R10).
- [x] Mantener próximas las limitaciones de procedencia y el carácter interno del contraste con los conteos. No incorporar resultados a la descripción del método (R07/R08/R11).

#### P3. Sistema multiagente y representación

- [x] Aclarar el flujo simulador–entorno–aprendizaje en la prosa y reducir la repetición del epígrafe de integración (R01/R06/R09/R10).
- [x] Reunir la lectura de la figura de controladores inmediatamente antes de ella; distinguir política/valores de acción y uso del crítico en entrenamiento y ejecución (R05/R06/R09/R10; H07).
- [x] Conservar explícito que la adaptación HAPPO actualiza primero el crítico y después los actores, sin equipararla a la descripción teórica externa (R07/R08; parte de H32).
- [x] Enlazar las definiciones visibles de dimensiones de control con sus entradas existentes y comprobar los nuevos enlaces. Mantener la distinción de señales de espera y protocolos de recompensa (R13/R16).

#### P4. Búsqueda, selección y alcance documental

- [x] Explicar en el cuerpo las distribuciones uniforme continua y loguniforme, usando sus entradas existentes: la remisión del apéndice debe encontrar en metodología el contenido que promete (R01/R16/R22; parte de H16).
- [x] Separar principios de búsqueda, configuración de cada fase y criterios de selección. Reducir encadenamientos de siglas y signos solo donde dificulten la lectura (R03/R04/R14/R21).
- [x] Aclarar la diferencia entre diseño de búsqueda, ejecución documentada y evaluación final prevista. Conservar todos los límites de presupuestos, arquitecturas y selección (R07/R08/R19).
- [x] Mantener unidos presentación y lectura del esquema de búsqueda en dos fases, con un epígrafe breve (R09/R10).

#### P5. Métricas y análisis

- [x] Dar a las incidencias de simulación un apartado propio dentro de las métricas; distinguir eventos de inicio y contador nativo, conservando su alcance por procedimiento (R02/R03/R06; H26).
- [x] Sustituir «Ambos» por los procedimientos concretos de construcción de intervalos. Conservar niveles, corrección por multiplicidad y cautelas de cobertura (R06; H25).
- [x] Revisar el recorrido cohorte → métricas → unidad pareada → incertidumbre → decisión y evaluación final. Mantener denominadores, viajes inconclusos y límites de atención a la demanda (R01/R03/R08/R13).
- [x] Trasladar al texto las explicaciones procedimentales del epígrafe del análisis pareado y conservar una identificación suficiente del esquema (R09/R10).

#### P6. Comprobación y cierre

- [x] Contrastar ecuaciones, etiquetas, referencias, imágenes, tablas, cifras y citas con el estado anterior; comprobar que los cambios no alteraron los procedimientos descritos.
- [x] Ejecutar el ciclo completo de glosario requerido por los nuevos usos y compilar con SyncTeX, sin procesos simultáneos.
- [x] Revisar el log y las páginas afectadas del PDF para comprobar desbordes, continuidad, figuras y enlaces de glosario (R12/R16/R24).
- [x] Comprobar que las fuentes de los otros capítulos, el glosario, la bibliografía y los archivos de imágenes conservan su identidad, salvo el generador y la figura del codificador expresamente incluidos en el alcance. Actualizar este plan con resultados y pendientes concretos (R26).

### Dependencias fuera del alcance

- **H16:** el contenido prometido por la remisión puede completarse en metodología. La redacción y los enlaces del propio apéndice quedan fuera de esta entrega.
- **H20:** se conserva el punto de miles del texto de metodología y se corrige la coma de miles encontrada en el eje del codificador. La agrupación con espacio fino de las tablas del apéndice necesita una revisión de ese archivo; no se dará por resuelta la uniformidad global.
- **H32:** se conserva y precisa el orden de actualización descrito en metodología. Su contraste con el pseudocódigo teórico requiere comprobar las fuentes o versiones que ese otro apartado pretende documentar.
- **H34:** verificar y, si corresponde, completar la referencia de PyTorch requiere revisar la entrada bibliográfica. No se agregará una cita a una ficha no verificada ni se modificará `bibliografia.bib` dentro de una revisión limitada al capítulo.
- Los hallazgos exclusivos de resumen, introducción, marco teórico, resultados, conclusiones y figuras UML del apéndice no forman parte de este plan.

### Registro de ejecución y validación

Aplicación completada el 16 de octubre de 2026. Las casillas representan la revisión editorial y sus comprobaciones, no las campañas experimentales descritas por la tesina. No certifican que todos los hallazgos de la auditoría general estén resueltos.

#### Ubicaciones y resultado de cada bloque

| Bloque | Ubicación en la fuente actual | Resultado |
|---|---|---|
| P1 | Todo [el capítulo](5-metodologia.tex); dimensiones del control, línea 109 | Se normalizaron las 75 referencias singulares del inventario, incluidos 39 destinos internos presentados como apéndices. Se corrigieron los dos plurales inventariados y se uniformó «ejecución». También se ajustó la referencia al capítulo de resultados. |
| P2 | [Diseño experimental](5-metodologia.tex#L14), [programas de referencia](5-metodologia.tex#L38) y [distribución OD](5-metodologia.tex#L194) | La lectura del flujo, las barras temporales y las zonas de Mendoza se concentra en el cuerpo, junto a sus figuras. Se conservaron la excepción de C4 y los límites documentales de Mendoza. |
| P3 | [Integración](5-metodologia.tex#L228), [codificación](5-metodologia.tex#L267) y [algoritmos](5-metodologia.tex#L359) | Se separaron explicación e identificación de figuras; se precisaron la salida de cada controlador y el uso del crítico. Se explicitó la secuencia de actualización HAPPO. El ejemplo del codificador se distingue de la configuración A/C. |
| P4 | [Búsqueda](5-metodologia.tex#L386), [fase 1](5-metodologia.tex#L448), [fase 2](5-metodologia.tex#L467) y [evaluación final](5-metodologia.tex#L691) | Se explican las distribuciones de muestreo y se distingue lo que define el protocolo de lo que acredita una ejecución documentada. Se mantienen presupuestos, semillas y condiciones por escenario. |
| P5 | [Métricas](5-metodologia.tex#L573), [incidencias](5-metodologia.tex#L626) y [análisis pareado](5-metodologia.tex#L639) | Los teletransportes tienen un apartado propio; se conservan sus límites de medición. Se identifican explícitamente los procedimientos percentil y t, y se lleva al texto la explicación del esquema pareado. |
| P6 | Fuente, glosarios generados y [PDF compilado](main.pdf) | Se completaron las comprobaciones de integridad, enlaces, compilación y diagramación descritas abajo. |

Las ubicaciones corresponden a esta entrega y pueden desplazarse con ediciones posteriores. Las etiquetas LaTeX identifican los apartados de forma estable.

#### Integridad y alcance

- Las doce expresiones entre `\begin{equation}` y `\end{equation}` y los seis cuerpos `tabular` se contrastaron con la copia anterior: permanecen idénticos, carácter por carácter.
- Se conservan las doce figuras, todos los destinos de referencias y citas, y las rutas de `\input` y `\includegraphics`. Se mantuvieron las etiquetas anteriores y se añadió únicamente `subsec:incidencias_simulacion`.
- La revisión del diff conserva datos, semillas, presupuestos, ventanas, umbrales y limitaciones. La aplicación es editorial; no verifica de nuevo las campañas experimentales ni acredita ejecuciones adicionales.
- La comparación SHA-256 con el estado previo confirma que las fuentes de los demás capítulos, `main.tex`, bibliografía, glosarios y demás imágenes permanecen intactas. Las dos excepciones previstas son el generador del codificador y su PDF de metodología. La figura de componentes del apéndice no se regeneró ni cambió.
- En el generador solo se añadió la opción que imprime el punto de miles. Se comprobó que las 1.203 coordenadas, las funciones, los parámetros ilustrativos I = 22 y M = 1136 veh·s, la discretización y la geometría permanecen iguales. El punto se protege del cambio de separador decimal de `babel` mediante `\mbox{.}`.
- La comparación de patrones ya no encuentra las referencias singulares numeradas en minúscula ni los plurales y usos de «corrida» inventariados en el capítulo. Esto complementa la lectura contextual; no sustituye una revisión semántica.

#### Compilación, enlaces y páginas

Se ejecutó sin compilaciones simultáneas el ciclo requerido por los nuevos usos del glosario:

```sh
pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
makeglossaries main
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

Después de los ajustes de página y de la figura, se volvió a ejecutar `latexmk` con esos mismos parámetros. La salida final contiene 162 páginas. No hay citas o referencias indefinidas, etiquetas duplicadas ni avisos de cajas desbordadas o insuficientemente llenas; permanece la advertencia conocida de `tracklang` para `spanish`.

Se verificaron destinos con `pdfinfo -dests` y anotaciones `GoTo` con `qpdf --json`. Los cuatro enlaces nuevos —carriles controlados, número de acciones, distribución uniforme continua y distribución loguniforme— aparecen en el cuerpo y apuntan a destinos existentes del glosario. Los dos primeros se encuentran en la página física 90 y los restantes en la 106.

Se revisaron visualmente las páginas físicas 84, 85, 86, 90, 94, 96, 99, 102, 106, 107, 114 y 115, correspondientes a las presentaciones, figuras y transiciones afectadas. Se ajustaron dos cortes de párrafo y una línea aislada; se comprobó también la figura del codificador incrustada en su tamaño final. Esta comprobación se refiere a esas páginas, no a una nueva inspección visual exhaustiva de los demás capítulos.

Para el ajuste de la figura se aplicó la skill `tikz-diagrams`: comprobación estática de la fuente TikZ, compilación autónoma con `pdflatex`, renderización y revisión visual manual. No se ejecutó el verificador visual basado en PyMuPDF, ausente en el entorno; la comprobación manual y la igualdad de coordenadas cubren este cambio de formato. La curva es una representación discretizada mediante muestras, no una nueva demostración analítica de los umbrales.

#### Pendientes que no bloquean esta entrega

Las dependencias H16, H20, H32 y H34 listadas arriba continúan abiertas en cuanto requieren cambios o verificaciones fuera de metodología. El contenido metodológico de las distribuciones y el formato de miles del gráfico sí quedaron atendidos. La auditoría general permanece como diagnóstico fechado y no se marca íntegramente como resuelta.

