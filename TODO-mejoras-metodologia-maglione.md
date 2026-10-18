# TODO: mejoras de la metodología tras la comparación con Maglione

Fecha: 14 de octubre de 2026. Referencia de la revisión: metodología publicada en el commit `fd3a5fc` y capítulo metodológico de Maglione, páginas impresas 37–66 de `/home/juanm4/Documentos/Tesina_LCC_Maglione.pdf`.

La comparación identifica una metodología de calidad comparable, con fortalezas en la precisión de las métricas y el alcance de las inferencias. Las mejoras se concentran en completar las cifras urbanas y explicar algunas decisiones con mayor sencillez. Se conserva la estructura actual y se aplican cambios locales, justificados y verificables. Este TODO permanece fuera del manuscrito LaTeX.

## Prioridad alta: completar la especificación numérica urbana

- [ ] **MEJ-01 — Completar y alinear los límites de búsqueda de Mendoza.** La metodología ya presenta para fase 1 los límites comunes a los cuatro escenarios. Alinear con ellos el protocolo, el validador y el submitter urbanos. Determinar con evidencia los valores propios de fase 2 y vincular el entrenamiento final con el presupuesto de la búsqueda que aporta la configuración seleccionada. Coordinar con MDZ-04, MDZ-05 y MDZ-09 de [TODO-mendoza-metodologia.md](TODO-mendoza-metodologia.md).

  **Justificación:** el lector necesita conocer las condiciones numéricas para reconstruir el procedimiento. Una remisión al archivo de protocolo no sustituye la presentación de sus parámetros esenciales.

  **Ubicación:** fase 1, fase 2 y entrenamiento final de `5-metodologia.tex`; protocolo urbano de `8-apendice_arquitectura.tex`.

  **Cierre:** los valores coinciden con el protocolo urbano identificado y se presentan con unidad, función y fuente. Las cifras sintéticas conservan su alcance. Los detalles técnicos adicionales se gestionan en el checklist de Mendoza, sin duplicar sus pendientes aquí.

## Prioridad media: hacer visible la razón de las decisiones

- [x] **MEJ-02 — Explicar brevemente los límites de búsqueda y las reglas exploratorias.** Conservar el protocolo común de fase 1 para comparar las configuraciones bajo los mismos límites de propuestas e iteraciones. Explicar el propósito de los márgenes y condiciones de conservación del dominio en el refinamiento urbano. Coordinar con MDZ-07 la justificación del panel común de cinco semillas: hasta 65 simulaciones con la lista máxima de candidatos, conservando la decisión adoptada.

  **Justificación:** Maglione conecta especialmente bien las restricciones de sus datos con la resolución espacial y temporal elegida. Conviene aplicar esa forma de exposición a nuestras propias decisiones, con el respaldo disponible.

  **Ubicación:** búsquedas y selección urbana de `5-metodologia.tex`; reglas detalladas en `8-apendice_arquitectura.tex`.

  **Cierre:** cada decisión relevante tiene una razón concreta, proporcional a la evidencia. Se distingue una restricción operativa de una elección heurística; las cifras no se presentan como óptimos ni como garantías de precisión estadística. Si falta una justificación identificable, registrarla en este TODO y resolverla con el autor o la documentación pertinente, sin inventarla.

## Prioridad media: facilitar la lectura con cambios locales

- [ ] **MEJ-03 — Aligerar párrafos densos y remisiones repetidas.** Revisar consecutivamente apertura, diseño, sistema de control, búsquedas, selección, evaluación y cierre. Dividir párrafos que acumulen varias ideas y abreviar anuncios o remisiones que repitan información inmediata. Mantener una función clara para cada párrafo: propósito, operación, criterio o consecuencia.

  **Justificación:** la precisión actual puede resultar exigente para el lector cuando se acumulan detalles de implementación y cautelas. La mejora debe conservar el razonamiento científico y favorecer una redacción académica natural.

  **Ubicación:** principalmente `5-metodologia.tex`; coordinar las remisiones al apéndice cuando corresponda.

  **Cierre:** el recorrido se entiende en una lectura continua, los sujetos y antecedentes son claros y cada abreviación conserva sus premisas. Permanecen visibles el cierre del episodio, las poblaciones evaluadas, las ponderaciones de las dos medidas locales y el alcance conjunto de A/C. Los desarrollos extensos de código siguen en el apéndice.

## Prioridad baja: desarrollar la notación de las unidades

- [x] **MEJ-04 — Definir vehículos-segundo en su primera aparición.** Desarrollar `veh·s` al introducir la espera acumulada por carril. Explicar que representa la suma de las esperas atribuidas a los vehículos presentes. Comprobar la uniformidad de su escritura en cuerpo, apéndice, glosario, tablas y epígrafes.

  **Justificación:** la notación está documentada en ingeniería de tránsito, pero resulta poco familiar para parte del público de la tesina. Su primera aparición necesita una explicación breve.

  **Ubicación inicial:** observaciones y codificación de la espera en `5-metodologia.tex`.

  **Cierre:** la unidad se entiende sin consultar otra sección y se distingue de la espera media por vehículo y de la normalización por carril. Se mantienen los valores numéricos, las métricas y sus definiciones.

## Verificación al aplicar las mejoras

- [ ] **MEJ-05 — Comprobar coherencia e integridad del manuscrito.** Revisar la versión vigente, `git status --short` y los cambios locales antes de editar; la carpeta principal y la referencia remota tienen historias divergentes. Conservar los identificadores existentes y verificar referencias, citas, unidades y archivos incluidos. Leer el capítulo completo en orden después de los ajustes.

- [ ] **MEJ-06 — Compilar y revisar las páginas afectadas.** Ejecutar desde la raíz `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`. Si cambian entradas o usos del glosario, seguir la secuencia de `AGENTS.md`: `pdflatex`, `makeglossaries main` y `latexmk`. Comprobar el log y revisar visualmente tablas, figuras, epígrafes y cortes de página. Coordinar `main.pdf` con las fuentes definitivas.

## Decisiones que se conservan

La fase 1 de Mendoza comienza después de A–E y A/C y fija recompensa y observación locales, con ρ=0. Comparte los límites de fase 1: 100 propuestas iniciales por estudio, ampliables hasta 150; 40 iteraciones máximas; ASHA con gracia 10 y reducción 4; diagnóstico cada diez iteraciones. A/C modifica conjuntamente observación y recompensa y mantiene su análisis específico de MAPPO en las tres redes sintéticas. La evaluación final conserva veinte simulaciones por combinación, medias con igual peso por simulación y desviación estándar muestral; su dispersión corresponde al modelo evaluado.

Los resultados, las campañas históricas y las definiciones de métricas se conservan. Las mejoras editoriales no incorporan estados de avance al manuscrito ni crean código de evaluación final. La comparación con Maglione orienta la calidad de exposición; sus parámetros y procedimientos no se trasladan a este trabajo por analogía.

Los Markdown se mantienen fuera de los commits del manuscrito, conforme al criterio de publicación vigente.

## Pase autorizado del 14 de octubre de 2026

El autor aprobó explicar las decisiones respaldadas, desarrollar la unidad y dividir los párrafos seleccionados. Las sustituciones de redacción G1–G5 y la eliminación de reiteraciones R1/E1–E5 quedan pendientes. Se conserva la copia local anterior al pase, sin incorporar otros cambios del remoto.

- **MEJ-02, avance anterior:** se explicó el reparto uniforme de propuestas entre arquitecturas y la función de conservar categorías, mantener dominios amplios, imponer un ancho mínimo y ampliar el intervalo observado. La cota de coste del panel de cinco semillas ya figura en la selección y se conserva. En ese pase quedó pendiente la razón del número exacto de 50 propuestas; la aclaración posterior del autor elimina esa diferencia y adopta el protocolo común de fase 1.
- **MEJ-03, aplicación parcial:** se aplican D1–D4 conservando todas sus palabras y se divide el refinamiento urbano según D9. Los demás cortes opcionales y las eliminaciones de reiteraciones siguen pendientes. Se ajustan localmente los saltos de página para evitar comienzos aislados y mantener completa la definición inicial de la unidad.
- **MEJ-04, completado:** la primera definición de espera por carril desarrolla vehículos-segundo y explicita la suma de esperas atribuidas a los vehículos presentes. Las magnitudes, los valores y la notación posterior se conservan.
- **MEJ-01, estado anterior a la aclaración del autor:** las redes sintéticas especifican 40 iteraciones y ASHA 10/4 en fase 1, y 60 iteraciones y ASHA 30/2 en fase 2. El archivo local de preparación urbana conserva 50 propuestas por arquitectura en fase 1 y campos en `null`. La actualización siguiente fija los límites comunes de fase 1 y distingue esa definición del trabajo de alinear los archivos de preparación.

**Verificación del pase:** compilación final con `latexmk`, glosarios regenerados y PDF de 164 páginas. El log conserva únicamente la advertencia conocida de `tracklang`; no hay desbordes ni referencias indefinidas. Los glosarios registran cero entradas rechazadas y cero avisos. Se conservaron las cifras del contenido, las ecuaciones, las tablas y las etiquetas; D1–D4 conservan sus palabras. Se revisaron visualmente las páginas afectadas y los cortes resultantes. `git diff --check` termina sin problemas.

## Aclaración del protocolo común de fase 1 — 14 de octubre de 2026

El autor establece los mismos límites de búsqueda para los cuatro escenarios y mantiene la excepción de ρ=0 en Mendoza por comenzar después de A–E y A/C. La inspección abarcó nueve worktrees, 23 ramas locales y el historial de 116 commits entre el 14 de agosto y el 14 de octubre, tras actualizar las referencias remotas. El programa de fase 1 conserva 100 propuestas iniciales, 40 iteraciones, gracia 10, reducción 4 y diagnóstico cada diez iteraciones en las ramas revisadas; el contrato compartido permite hasta 150 propuestas por estudio. Los archivos locales de preparación urbana con 50 propuestas no están incorporados en el historial de commits consultado.

El capítulo presenta ahora 32 estudios: cuatro algoritmos, dos arquitecturas y cuatro escenarios. Los ocho estudios de Mendoza reúnen 800 propuestas iniciales. Se retira el pendiente de justificar una diferencia de 50 propuestas. Continúan la adaptación de los archivos de preparación a estos valores comunes, las cifras propias de fase 2 y las mejoras de redacción y reiteraciones que el autor dejó pendientes. Los porcentajes del refinamiento se conservan como reglas heurísticas, sin atribuirles optimalidad.

La actualización se verificó mediante compilación, regeneración de glosarios e inspección visual del capítulo y el apéndice. El PDF conserva 164 páginas y el log únicamente la advertencia conocida de `tracklang`. Permanecen las ecuaciones, tablas, citas, etiquetas y usos de glosario; las cifras modificadas corresponden a los 32 estudios y las 800 propuestas urbanas iniciales. El código experimental y los informes históricos se conservan. La expresión «presupuesto sintético» se reemplaza en el texto actual por una referencia explícita a la fase 2 de las redes sintéticas.

## Revisión de coherencia metodológica — 14 de octubre de 2026

La apertura ya no afirma que el sistema de control sea común a las dos líneas; los protocolos A–E y A/C se citan junto con su presentación. La descripción general de búsqueda distingue los límites compartidos de fase 1, la secuencia de Mendoza posterior a A–E y A/C con observación local y ρ=0, y las condiciones que dependen de cada escenario. La búsqueda TPE/ASHA se describe para las búsquedas en general, conforme al ejecutor compartido. En fase 2, la cifra de 100 propuestas y 60 iteraciones queda delimitada a las redes sintéticas. También se sustituyen «La selección elige» y «dispone registrar» por formulaciones directas.

La revisión del código de `marl-tlc` confirma que su protocolo urbano todavía exige 50 propuestas y que el submitter aplica ese valor. La alineación con los límites metodológicos comunes sigue en MDZ-04; los parámetros urbanos propios de fase 2 siguen en MDZ-05. No se trasladan valores sintéticos a esa fase.
