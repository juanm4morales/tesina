# TODO — Observaciones de Caro sobre la tesina

Revisión realizada el **16 de octubre de 2026**. Fuente: [tesina_comentarios_caro.pdf](/home/juanm4/Descargas/tesina_comentarios_caro.pdf), de 123 páginas físicas. Se contrastaron las marcas con los capítulos actualmente incluidos desde `main.tex`. Este documento planifica las correcciones; **no aplica cambios al texto ni certifica el cierre de las observaciones**.

## Alcance, cobertura y lectura

Se identificaron **287 anotaciones de revisión**, todas atribuidas a `carol`: **222 resaltados, 60 tachaduras y 5 notas adhesivas**. **180 tienen comentario escrito y 107 no lo tienen**. Se excluyeron enlaces internos y ventanas emergentes que duplican la presentación de una anotación. Cada marca tiene una ficha propia, C001–C287, incluso cuando varias integran una misma corrección. Así se evita perder tachaduras pequeñas o contar dos veces el mismo pedido como trabajo independiente.

Las anotaciones están en el resumen (página física 2), la introducción (20–23) y el marco teórico (24–77). No se encontraron marcas de revisión en los capítulos posteriores de este PDF. Eso no implica que estén aprobados ni que las observaciones generales carezcan de aplicación allí.

**Cómo localizar:** «PDF» es la página física desde 1; «impresa» es el número que aparece al pie. En el cuerpo de este PDF, la página física es la impresa + 19. El resumen usa numeración romana. Las líneas enlazadas corresponden a los archivos actuales y cambiarán con futuras ediciones. Los números de figuras, tablas y ecuaciones citados por Caro son los del PDF comentado: conservar etiquetas LaTeX y no trasladar esos números a mano.

**Cómo interpretar:** se conserva literalmente el comentario de la anotación, incluidos errores de tipeo. El texto marcado se recuperó por sus coordenadas; en marcas sobre signos o límites entre palabras se añade el contexto de la línea. Las cinco notas adhesivas no tienen una selección textual y se ubicaron por página y posición. Para marcas sin comentario, la acción propuesta es una **interpretación editorial**, no una cita atribuida a Caro. En los resaltados repetidos de referencias, esa interpretación se apoya en sus comentarios explícitos sobre mayúsculas. Las marcas breves C041, C074, C118 y C168 y el comentario incompleto C102 requieren especial atención al contexto.

**Estado:** «Pendiente» indica que el pedido sigue siendo pertinente o requiere decisión editorial; «Parcial o aparentemente atendida» indica cambios visibles en la fuente que aún deben verificarse en conjunto; «Pasaje modificado o retirado» evita aplicar una sustitución sobre un texto que ya cambió; «Atendida en la fuente; verificar PDF» se usa para referencias cuya mayúscula ya se observa en el pasaje actual; «Conservar» corresponde a los dos comentarios favorables. Las casillas quedan abiertas para revisar y cerrar conscientemente cada ficha; no significan que las 287 marcas exijan 287 ediciones distintas.

Se preservó además un [inventario CSV](observaciones-caro.csv) con los 287 registros, texto, comentario, ubicación, estado y acción propuesta. El inventario guarda el objeto PDF de cada anotación para poder rastrearla sin depender del ID editorial.

## Prioridades y correcciones transversales

Las siguientes tareas agrupan las fichas y proponen un orden de resolución. Son una síntesis editorial derivada de las marcas, no comentarios adicionales atribuidos a Caro.

| Prioridad | Trabajo y criterio de cierre | Fichas principales |
| --- | --- | --- |
| Alta | Rehacer resumen: motivación → problema de coordinación → método → alcance/evidencia. Después sincronizar Abstract, sin convertir el diseño de búsqueda en una campaña acreditada. | C001 |
| Alta | Simplificar la introducción: presentar problema, objetivo y contribuciones sin anticipar fórmulas ni repetir la función del crítico; integrar o justificar «Motivación». | C011–C035 |
| Alta | Reescribir aprendizaje profundo: definir neurona, pesos, sesgo y activación; componer capas y red; explicar optimización; cerrar con aplicación semafórica. No alternar ejemplos del tránsito con conceptos todavía indefinidos. | C181–C210 |
| Alta | Ordenar métodos de RL: funciones de valor → estimación TD y Q-learning; después políticas, su objetivo y actor-crítico. Introducir esperanza, siglas y términos antes de usarlos. | C157–C180 |
| Alta | Reunir la introducción e interpretación de cada figura en un bloque próximo y coherente; sacar del epígrafe explicaciones extensas y evitar volver a presentar la misma figura después de una interrupción. El orden de los floats se verifica en PDF. | C003, C076, C092, C100, C107, C114, C154, C166, C178, C250 |
| Alta | Unificar definiciones y ecuaciones de velocidades; suprimir clasificaciones y explicaciones repetidas. Cada ecuación debe aparecer junto a la cantidad que formaliza y sus símbolos. | C079–C080, C104, C197 |
| Alta | Aclarar sujetos y atribución: distinguir antecedentes, decisiones de esta tesina, protocolos documentados y evidencia ejecutada. No usar «este estudio» para cambiar tácitamente de Haddad et al. al trabajo propio. | C244, C256, C268, C278–C280 |
| Alta | Reescribir TRPO/PPO y la comparación de garantías heterogéneas con definiciones previas y sin incisos anidados. Conservar los supuestos y límites de las garantías. | C233–C241, C266–C272 |
| Alta | Redibujar la intersección con sentidos y continuaciones de trayectorias inequívocos; comprobar dibujo, texto, epígrafe y etiqueta. No borrar archivos gráficos al retirar una referencia. | C062 |
| Media | Revisar bibliografía: autoría/edición de Cal y Mayor y Cárdenas; publicación científica de SUMO; referencia de OpenStreetMap; HBEFA solo donde el contenido sobreviva; artículos pertinentes para afirmaciones y aplicaciones. Verificar las publicaciones antes de modificar BibTeX. | C056–C057, C066, C126, C131, C133, C140, C142, C144, C161, C187, C211 |
| Media | Unificar expansión y lengua de siglas: término español y, si procede, término inglés más sigla en un solo paréntesis. Revisar macros existentes y primeras menciones por contexto; no introducir desarrollos largos repetidos en cada frase. | C014, C019, C025–C026, C109, C132–C137, C145, C176, C183, C185, C227, C253, C265 |
| Media | Enlazar términos visibles con el glosario y comprobar el texto producido, su plural y los destinos del PDF. Evitar interpretar `\glsaddall` como enlace desde el cuerpo. | C045, C047–C048, C139, C177, C186, C212, C226 |
| Media | Desambiguar «red» (neuronal/vial), «objetivo» (blanco/pérdida/retorno), «estas transformaciones» y otros demostrativos; traducir lotes/minilotes y desarrollar términos como bootstrapping. | C020, C077, C090, C117–C118, C160, C177, C196, C198–C205, C229 |
| Editorial | Reducir dos puntos, punto y coma, anuncios vacíos e incisos que cortan la lectura. Usar conexiones que expliciten la relación lógica; no convertirlo en una prohibición general de signos necesarios. | C007, C015–C017, C058–C059, C110–C112, C129–C130, C138, C141, C153, C162–C165, C171–C178, C191–C193, C206–C214, C217–C224, C232–C242, C251, C261, C278 |
| Editorial | Normalizar Figura/Tabla/Ecuación/Capítulo/Sección/Apéndice/Algoritmo en referencias singulares numeradas, conforme al criterio pedido. Revisar plurales y menciones genéricas por separado; varias marcas ya están atendidas. | Las 59 fichas identificadas como «Mayúsculas de referencias», además de C051 y C175 |
| Editorial | Uniformar coma decimal y unidades, separar símbolos de unidades y evitar líneas aisladas. Revisar el PDF tras los cambios de prosa y ubicación de figuras. | C006, C071–C075, C082, C085, C098–C099, C252 |
| Conservar | Preservar los pasajes que Caro valora y mantener prudencia al presentar el posicionamiento frente a antecedentes. Acortar cautelas repetidas sin afirmar inexistencia universal ni efectos causales no aislados. | C246, C281–C287 |

## Decisiones de aplicación y dependencias

1. Resolver primero la estructura de resumen, introducción y redes neuronales; las correcciones locales dependen de esa nueva ubicación. C028–C034, C181–C210 y C233–C241 son bloques de reescritura, aunque se mantenga una ficha por marca.
2. «Eliminar elaboración propia» no autoriza a perder la atribución de datos, imágenes o algoritmos ajenos. C004, C106, C147, C216 y C257 requieren diferenciar fórmula editorial redundante y fuente necesaria.
3. Quitar una aclaración repetida no elimina una limitación del método. Mantener la comparación A/C como comparación MAPPO sintética que cambia observación y recompensa; separar recompensas por protocolo; distinguir comprobación estática de Mendoza de evaluación de políticas; conservar los límites de las garantías HAPPO con recompensas individuales. Estas condiciones son restricciones del proyecto que deben respetarse al aplicar las correcciones, no nuevas observaciones del PDF.
4. «Red» debe desambiguarse por significado, sin reemplazos globales. Lo mismo vale para «fase», «transición», «estudio» y sus entradas de glosario. La espera acumulada con memoria finita no equivale a la espera total por viaje.
5. Los pedidos de nuevas fuentes y los enlaces de Caro se registran para su verificación al implementar las correcciones. En este relevamiento no se verificó el contenido de las páginas externas ni se incorporaron fuentes nuevas. No dar por validada la autoría de una publicación solo por el texto de una anotación.
6. Antes de editar cada bloque, revisar el estado de Git. Después, comprobar citas, referencias y glosario. Compilar desde la raíz con `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`; si se añaden entradas/usos de glosario, ejecutar primero el ciclo prescrito de `pdflatex -synctex=1`, `makeglossaries main` y `latexmk -pdf -synctex=1`. Revisar `main.log` y el PDF para detectar desbordes, saltos y líneas aisladas; verificar enlaces de glosario y el PDF versionado. No se compiló para generar este TODO porque no se modificaron las fuentes.

## Índice del relevamiento

| Bloque del PDF comentado | Páginas físicas / impresas | Fichas |
| --- | --- | --- |
| Resumen | 2 / i | C001 |
| Introducción y organización | 20–23 / 1–4 | C002–C044 |
| Marco teórico: apertura, tránsito, variables, arribos y control | 24–35 / 5–16 | C045–C102 |
| Simulación, SUMO, herramientas, archivos y métricas | 35–41 / 16–22 | C103–C133 |
| RL, MDP, valor, política y actor-crítico | 41–48 / 22–29 | C134–C180 |
| Aprendizaje profundo y redes neuronales | 48–51 / 29–32 | C181–C207 |
| DRL, DQN, política, ventaja y PPO | 51–58 / 32–39 | C208–C243 |
| MARL, formalismos, desafíos e independientes | 59–64 / 40–45 | C244–C260 |
| MAPPO y HAPPO | 64–72 / 45–53 | C261–C276 |
| Antecedentes y posicionamiento | 72–77 / 53–58 | C277–C287 |

## Fichas de corrección

### Resumen

#### C001 — Introducción del resumen

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 2, impresa i; [1-resumen.tex:3](/home/juanm4/Documentos/tesina/1-resumen.tex:3). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Text):** Introducción del resumen.
- **Observación literal de Caro:**

  > rehacer resumen
  > considerar presentar una motivación (por ejemplo, La congestión vehicular es una de las principales fuentes de contaminación  en las ciudades). En ciudades que cuentan con un sistema de control semafórico la programación de los ciclos de los semáforos puede ayudar a reducir la contaminación mejorando la fluidez del tráfico vehicular. En lo que respecta a el sistema de control semafórico si bien en las ciudades aún se emplean los de ciclos fijos con el advenimiento de la inteligencia artificial y los sistemas de transporte inteligentes se ha comenzado a trabajar en distintos enfoques para una programación inteligente de los ciclos de los semáforos. En ciudades con gran cantidad de semáforos por zona es necesario que los mismos estén coordinados no solo a nivel de intersección sino también de intersecciones vecinas. Entre los modelos más utilizados para agentes están los de Reinforcement Learning, .....y seguir

- **Corrección y detalle:** Reescribir el resumen con una secuencia clara: problema y motivación, utilidad del control semafórico adaptativo, necesidad de coordinación entre intersecciones, enfoque MARL y alcance del trabajo. Reducir el inventario prematuro de algoritmos y detalles del codificador. Añadir resultados solo si están respaldados; sincronizar después el Abstract. La contaminación propuesta por Caro es un ejemplo de motivación, no un resultado demostrado por la tesina.

### Introducción

#### C002 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 20, impresa 1; [3-introduccion.tex:3](/home/juanm4/Documentos/tesina/3-introduccion.tex:3). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «la figura 1.1) [Aso18, Aso26].».
- **Observación literal de Caro:**

  > Figura se suele poner con la F en mayúscula lo mismo que Tabla. Si están en plural si se pone en minúscula las  figuras 3 y 4 ....las tablas 5 y 6.

- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C003 — La línea y los marcadores representan los valores anuales disponibles; el área sombreada fac…

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 20, impresa 1; [3-introduccion.tex:45](/home/juanm4/Documentos/tesina/3-introduccion.tex:45). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La línea y los marcadores representan los valores anuales disponibles; el área sombreada facilita la lectura de su magnitud.».
- **Observación literal de Caro:**

  > esta explicación debe ponerse en el texto y no en la Figura queda muy grande el tocho de texto del caption de la Figura.

- **Corrección y detalle:** Trasladar la explicación de la línea, los marcadores y el sombreado al párrafo que introduce la figura. Dejar un epígrafe breve que identifique variable, período y unidades, con las citas necesarias para reconocer los datos.

#### C004 — Elaboración propia a partir de reportes de AFAC.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 20, impresa 1; [3-introduccion.tex:45](/home/juanm4/Documentos/tesina/3-introduccion.tex:45). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Elaboración propia a partir de reportes de AFAC.».
- **Contexto del PDF:** «2025, expresada en millones de vehículos. La línea y los marcadores representan los valores anuales disponibles; el área sombreada facilita la lectura de su magnitud. Elaboración propia a partir de reportes de AFAC.».
- **Observación literal de Caro:**

  > se supone que toda figura que no tiene cita es de elaboración tuya. no es necesaria esta frase en la Figura.

- **Corrección y detalle:** Eliminar la fórmula redundante «Elaboración propia», conservando la atribución de los datos a AFAC y sus referencias. Que el gráfico sea propio no vuelve propios los datos de origen.

#### C005 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:48](/home/juanm4/Documentos/tesina/3-introduccion.tex:48). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «Como refleja la figura 1.1, la flota vehicular activa en Argentina experimentó una ex-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C006 — 2,2

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:48](/home/juanm4/Documentos/tesina/3-introduccion.tex:48). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «2,2».
- **Contexto del PDF:** «pansión sostenida entre 1990 y 2025, pasando de aproximadamente 2,2 millones a 15,78».
- **Observación literal de Caro:**

  > ojo con las comas y los puntos. En español se usa coma para los decimales y punto para los miles..... tener mucho cuidado con eso.

- **Corrección y detalle:** Unificar cifras del texto, ejes y tablas: coma decimal y un criterio español consistente para miles. En el pasaje actual ya aparece «2,2»; comprobar también el gráfico y el resto del documento. No sustituir los puntos de coordenadas TikZ, código, DOI o rutas, que tienen otra función.

#### C007 — remolques;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:48](/home/juanm4/Documentos/tesina/3-introduccion.tex:48). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «remolques;».
- **Contexto del PDF:** «circular, excluyendo acoplados y remolques; representa una estimación del parque activo».
- **Observación literal de Caro:**

  > . En otras palabras representa...

- **Corrección y detalle:** Cerrar la definición de flota con punto seguido después de «remolques» y presentar la aclaración como otra oración, por ejemplo «En otras palabras, representa…». Separar exclusiones y alcance para facilitar la lectura.

#### C008 — agudizando

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:48](/home/juanm4/Documentos/tesina/3-introduccion.tex:48). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «agudizando».
- **Contexto del PDF:** «consolidadas que poseen una capacidad física fija, agudizando la formación de colas y».
- **Observación literal de Caro:**

  > provocando

- **Corrección y detalle:** Sustituir «agudizando» por «provocando» o reformular con un verbo conjugado. Revisar que la frase no convierta el aumento de vehículos en una explicación causal suficiente de la congestión sin el respaldo correspondiente.

#### C009 — críticas.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:48](/home/juanm4/Documentos/tesina/3-introduccion.tex:48). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «críticas.».
- **Contexto del PDF:** «demoras en las intersecciones urbanas críticas.».
- **Observación literal de Caro:**

  > en otras palabras congestiones vehiculares.

- **Corrección y detalle:** Explicar con palabras directas que las colas y las demoras describen congestiones vehiculares. Integrar la precisión al cierre del párrafo y evitar acumular «críticas», «presión» y otras formulaciones generales sin aclaración.

#### C010 — Las congestiones vehiculares deterioran las condiciones de operación de la red e in- crement…

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:50](/home/juanm4/Documentos/tesina/3-introduccion.tex:50). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Las congestiones vehiculares deterioran las condiciones de operación de la red e in- crementan las demoras y las detenciones de los vehículos».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Suprimir o condensar la oración tachada si repite la motivación ya expuesta. En la versión actual sobrevive una formulación equivalente («La congestión deteriora…»); evaluar su función en la transición y conservar las citas que sostengan afirmaciones retenidas.

#### C011 — microscópico,

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:50](/home/juanm4/Documentos/tesina/3-introduccion.tex:50). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «microscópico,».
- **Contexto del PDF:** «microscópico, las emisiones de gases como el monóxido de carbono (CO), el dióxido de».
- **Observación literal de Caro:**

  > estas poniendo en la introcción conceptos del marco teórico que aun no has definido. Mejor ponoer algo comoÑ Para evaluar el impacto de las congestiones las emisiones.......

- **Corrección y detalle:** Evitar «modelado microscópico» y conceptos técnicos sobre emisiones antes de definirlos. Expresar aquí el propósito general y reservar el mecanismo para el marco teórico. El pasaje original sobre emisiones ya no está en la introducción actual: verificar la continuidad que dejó su retiro.

#### C012 — restringido por datos:

- [ ] **Editorial · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:50](/home/juanm4/Documentos/tesina/3-introduccion.tex:50). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (StrikeOut):** «restringido por datos:».
- **Contexto del PDF:** «urbano restringido por datos: el microcentro de la Ciudad de Mendoza, delimitado por».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar «restringido por datos:» y reconstruir la descripción del escenario urbano junto con C013; no borrar por ello la limitación real de los conteos parciales, que debe explicarse donde corresponda.

#### C013 — restringido por datos:

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:50](/home/juanm4/Documentos/tesina/3-introduccion.tex:50). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «restringido por datos:».
- **Contexto del PDF:** «urbano restringido por datos: el microcentro de la Ciudad de Mendoza, delimitado por».
- **Observación literal de Caro:**

  > de mediana escala,

- **Corrección y detalle:** Considerar «de mediana escala» para caracterizar el escenario, como propone Caro, solo si se justifica por el tamaño de la red. El texto actual describe información parcial de tránsito; distinguir tamaño y disponibilidad de datos, que no son equivalentes.

#### C014 — (IA)

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:52](/home/juanm4/Documentos/tesina/3-introduccion.tex:52). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(IA)».
- **Contexto del PDF:** «en Inteligencia artificial (Artificial Intelligence) (IA) y en particular el Aprendizaje por».
- **Observación literal de Caro:**

  > si vas a usar Artificial Intelligence poner AI o sea usa abreviaturas en iinglès . O sea o en inglés o en español. Spanglish abstenerse

- **Corrección y detalle:** Adoptar una convención lingüística coherente para nombre y sigla: «inteligencia artificial (IA)» o el desarrollo inglés acompañado de AI. Evitar que «Artificial Intelligence» parezca desarrollar IA. Revisar el formato general de acrónimos sin cambiar siglas internacionales establecidas de manera indiscriminada.

#### C015 — Puntuación de la línea indicada en el contexto

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:52](/home/juanm4/Documentos/tesina/3-introduccion.tex:52). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Highlight):** Puntuación de la línea indicada en el contexto.
- **Contexto del PDF:** «en Inteligencia artificial (Artificial Intelligence) (IA) y en particular el Aprendizaje por».
- **Observación literal de Caro:**

  > falta coma , en particular,

- **Corrección y detalle:** Aislar «en particular» con comas y revisar la construcción completa: «…inteligencia artificial y, en particular, el aprendizaje por refuerzo…», ajustando preposiciones si se conserva «los avances en…».

#### C016 — este enfoque,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:52](/home/juanm4/Documentos/tesina/3-introduccion.tex:52). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «este enfoque,».
- **Contexto del PDF:** «este enfoque, desde algoritmos tabulares aplicados a una sola intersección [Wie00] hasta».
- **Observación literal de Caro:**

  > estos enfoques? o sea AI y RL?

- **Corrección y detalle:** Precisar el antecedente de «este enfoque». Caro pregunta si se refiere a IA y RL; la oración debe identificar la aplicación concreta del aprendizaje por refuerzo al control semafórico y evitar presentar IA y RL como categorías paralelas independientes.

#### C017 — este enfoque

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 21, impresa 2; [3-introduccion.tex:54](/home/juanm4/Documentos/tesina/3-introduccion.tex:54). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «este enfoque».
- **Contexto del PDF:** «Sin embargo, la aplicación simultánea de este enfoque en múltiples intersecciones in-».
- **Observación literal de Caro:**

  > agentes inteligentes (cambiar la frase este enfoque) aparece repetida ojo con las repeticiones

- **Corrección y detalle:** Reemplazar la segunda aparición próxima de «este enfoque» por un sujeto explícito, como «agentes inteligentes» o «aprendizaje por refuerzo en múltiples intersecciones», según el sentido. Evitar el reemplazo mecánico si cambia el referente.

#### C018 — Por esta razón,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:56](/home/juanm4/Documentos/tesina/3-introduccion.tex:56). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Por esta razón,».
- **Contexto del PDF:** «Por esta razón, este trabajo aborda el problema desde el marco del MARL cooperativo.».
- **Observación literal de Caro:**

  > Considerando lo anterior, en este trabajo se aborda.....

- **Corrección y detalle:** Reformular el enlace con el planteo del trabajo, por ejemplo «Considerando lo anterior, en este trabajo se aborda…». Mantener la distinción actual entre finalidad de coordinación, recompensas individuales y protocolos locales o vecinales.

#### C019 — MARL

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:56](/home/juanm4/Documentos/tesina/3-introduccion.tex:56). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «MARL».
- **Contexto del PDF:** «Por esta razón, este trabajo aborda el problema desde el marco del MARL cooperativo.».
- **Observación literal de Caro:**

  > volver a poner el significado mult.... \acrlongfull o algo así es el comando buscarlo.

- **Corrección y detalle:** Desarrollar MARL en esta presentación central del problema mediante una macro adecuada, por ejemplo `\acrfull{acr-marl}`, aunque haya aparecido antes en el resumen. Comprobar la salida real y la política de primeras menciones por capítulo.

#### C020 — red.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:56](/home/juanm4/Documentos/tesina/3-introduccion.tex:56). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «red.».
- **Contexto del PDF:** «además información conjunta de la red. De este modo, cada controlador recibe una señal».
- **Observación literal de Caro:**

  > red de tránsito

- **Corrección y detalle:** Especificar «red de tránsito» o «red vial» donde se habla de información conjunta. Evitar la ambigüedad con redes neuronales y conservar la diferencia entre información disponible durante el entrenamiento y la ejecución.

#### C021 — En este contexto, el

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «En este contexto, el».
- **Contexto del PDF:** «En este contexto, el objetivo general de este trabajo es desarrollar y evaluar un siste-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar el inicio tachado «En este contexto, el» y arrancar directamente con «El objetivo general…». La versión actual ya usa ese comienzo directo; revisar conjuntamente C022–C024 para no duplicar o desarmar el sujeto.

#### C022 — trabajo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «trabajo».
- **Contexto del PDF:** «En este contexto, el objetivo general de este trabajo es desarrollar y evaluar un siste-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar el «trabajo» tachado como parte de la reformulación del objetivo, junto con C024. La marca no implica eliminar toda mención al trabajo: Caro propone especificar su carácter de trabajo final de carrera.

#### C023 — el

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «el».
- **Contexto del PDF:** «En este contexto, el objetivo general de este trabajo es desarrollar y evaluar un siste-».
- **Observación literal de Caro:**

  > El

- **Corrección y detalle:** Usar «El» al comenzar la oración reformulada sobre el objetivo. El comienzo actual ya está en mayúscula; conservarlo al aplicar las otras modificaciones del párrafo.

#### C024 — trabajo

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «trabajo».
- **Contexto del PDF:** «En este contexto, el objetivo general de este trabajo es desarrollar y evaluar un siste-».
- **Observación literal de Caro:**

  > trabajo final de carrera

- **Corrección y detalle:** Precisar «trabajo final de carrera» en la presentación del objetivo si esa es la denominación institucional adoptada. Unificar con «tesina» o «trabajo final de grado» en el resto del documento, evitando alternancias sin propósito.

#### C025 — (MAPPO y HAPPO)

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(MAPPO y HAPPO)».
- **Contexto del PDF:** «peño de algoritmos de entrenamiento centralizado con ejecución descentralizada (MAPPO y HAPPO) con esquemas de aprendizaje independiente (IPPO e IDQN) bajo condiciones».
- **Observación literal de Caro:**

  > poner el Multi... y H.... o sea no poenr las sigals así tiradas.

- **Corrección y detalle:** Presentar los nombres completos de MAPPO y HAPPO antes de emplear sus siglas en la enumeración del objetivo. Reutilizar las entradas de acrónimos y evitar una cadena excesiva de traducciones y paréntesis.

#### C026 — (IPPO e IDQN)

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:58](/home/juanm4/Documentos/tesina/3-introduccion.tex:58). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(IPPO e IDQN)».
- **Contexto del PDF:** «y HAPPO) con esquemas de aprendizaje independiente (IPPO e IDQN) bajo condiciones».
- **Observación literal de Caro:**

  > igual que la observación anterior.

- **Corrección y detalle:** Aplicar a IPPO e IDQN el mismo criterio que a MAPPO y HAPPO: desarrollar las siglas en la presentación de los algoritmos y aclarar su función como esquemas independientes. La marca pertenece al párrafo del objetivo, no a la sección de motivación.

#### C027 — La propuesta incorpora una codificación de la espera acumulada por carril mediante una trans…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:60](/home/juanm4/Documentos/tesina/3-introduccion.tex:60). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «La propuesta incorpora una codificación de la espera acumulada por carril mediante una transformación logarítmico-lineal en I niveles. La resolución no uniforme distingue con mayor detalle valores bajos de esa medida y acota los valores representados a partir de un umbral. La elección de cómo representar el tránsito influye en el problema de aprendizaje y cuenta con antecedentes en control semafórico [GR18]. En este trabajo, la codificación se utiliza en todos los controladores.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar de la introducción el desarrollo detallado de la transformación logarítmico-lineal, niveles y umbral. Conservar, si aporta al objetivo, una mención breve de la representación propuesta y trasladar la explicación técnica a metodología; no atribuir un beneficio experimental aislado al codificador.

#### C028 — También se estudia

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «También se estudia».
- **Contexto del PDF:** «También se estudia una adaptación de HAPPO para intersecciones con distintas geo-».
- **Observación literal de Caro:**

  > Punto seguido a lo que decis que haces en el trabajo final. En este trabajo final de grado además se adapta el modelo HAPPO para......

- **Corrección y detalle:** Integrar la adaptación de HAPPO como otro objetivo o aporte del trabajo en el mismo bloque expositivo. Caro sugiere «En este trabajo final de grado además se adapta…»; mantener claro qué parte se hereda del algoritmo y cuál se modifica.

#### C029 — una adaptación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «una adaptación».
- **Contexto del PDF:** «También se estudia una adaptación de HAPPO para intersecciones con distintas geo-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Resolver la tachadura de «una adaptación» dentro de la reescritura indicada en C028. Se puede pasar de «se estudia una adaptación de…» a «se adapta…», sin negar que el método implementado modifica la formulación original.

#### C030 — de

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «de».
- **Contexto del PDF:** «También se estudia una adaptación de HAPPO para intersecciones con distintas geo-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Suprimir la preposición «de» que queda innecesaria al cambiar «una adaptación de HAPPO» por «se adapta HAPPO». Revisar la oración completa después de aplicar C028 y C029.

#### C031 — esta adaptación los actualiza

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «esta adaptación los actualiza».
- **Contexto del PDF:** «en MAPPO, esta adaptación los actualiza secuencialmente y repondera las ventajas in-».
- **Observación literal de Caro:**

  > aquí se propone actualizar

- **Corrección y detalle:** Reemplazar «esta adaptación los actualiza» por un sujeto y una acción explícitos, como «aquí se propone actualizar…». Aclarar que la actualización secuencial corresponde a los actores; evitar sugerir una actualización secuencial del crítico.

#### C032 — repondera

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «repondera».
- **Contexto del PDF:** «en MAPPO, esta adaptación los actualiza secuencialmente y repondera las ventajas in-».
- **Observación literal de Caro:**

  > se reponderan  palabra repondera no me gusta algún sinónimo?

- **Corrección y detalle:** Sustituir «repondera» por una expresión más transparente, por ejemplo «ajusta la ponderación de las ventajas individuales según…». Mantener la operación matemática que se describe y revisar la concordancia de la oración.

#### C033 — El crítico centralizado incorpora información conjunta durante el entrenamiento. La comparac…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «El crítico centralizado incorpora información conjunta durante el entrenamiento. La comparación con MAPPO, IPPO y IDQN examina el desempeño de procedimientos completos en esos escenarios, sin atribuir de antemano una ventaja a HAPPO ni aislar el efecto de su actualización secuencial.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Condensar o trasladar el bloque tachado sobre crítico y alcance comparativo. Preservar en metodología o en una formulación breve la limitación de que se comparan procedimientos completos y no se aísla el efecto de la actualización secuencial.

#### C034 — El crítico centralizado incorpora información conjunta durante el entrenamiento.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:62](/home/juanm4/Documentos/tesina/3-introduccion.tex:62). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «El crítico centralizado incorpora información conjunta durante el entrenamiento.».
- **Observación literal de Caro:**

  > sacar la frase no aporta nada ....eso lo explicarás en el marco teórico...

- **Corrección y detalle:** Retirar de esta presentación la oración técnica sobre el crítico centralizado, que se desarrollará en el marco teórico. Coordinar con C033 y revisar otras repeticiones próximas de la misma explicación.

#### C035 — 1.1. Motivación

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 22, impresa 3; [3-introduccion.tex:65](/home/juanm4/Documentos/tesina/3-introduccion.tex:65). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «1.1. Motivación».
- **Contexto del PDF:** «1.1. Motivación».
- **Observación literal de Caro:**

  > para mi con todo lo que pusiste antes esta sección ya dejó de tener lugar.

- **Corrección y detalle:** Reevaluar la sección «Motivación»: integrar lo indispensable en los párrafos iniciales y eliminar la sección si solo repite esa justificación. Si se conserva, debe aportar una razón específica o una pregunta de investigación que todavía no esté expuesta.

#### C036 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:76](/home/juanm4/Documentos/tesina/3-introduccion.tex:76). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «guían la investigación. A continuación, el capítulo 2 presenta los fundamentos teóricos».
- **Observación literal de Caro:**

  > Capítulo con mayúscula.... como Figura y Tabla

- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C037 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:78](/home/juanm4/Documentos/tesina/3-introduccion.tex:78). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «siguientes. El capítulo 3 detalla el diseño de la investigación: define la representación de».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C038 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:78](/home/juanm4/Documentos/tesina/3-introduccion.tex:78). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «ción. Luego, el capítulo 4 analiza y discute los resultados obtenidos en las simulaciones,».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C039 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «Finalmente, el capítulo 5 sintetiza las conclusiones principales a la luz de los objetivos».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C040 — delimita

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «delimita».
- **Contexto del PDF:** «propuestos, delimita el alcance y las limitaciones del estudio, y proyecta líneas de trabajo».
- **Observación literal de Caro:**

  > enmarca (delimita limita el limite tendiendo a infinito) tratar de usar sinónimos....

- **Corrección y detalle:** Cambiar «delimita» por «enmarca» u otra formulación natural al describir conclusiones y alcance. Revisar la proximidad con «limitaciones» y evitar repetir la raíz «limit-» sin necesidad.

#### C041 — limitaciones

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «limitaciones».
- **Contexto del PDF:** «propuestos, delimita el alcance y las limitaciones del estudio, y proyecta líneas de trabajo».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar «limitaciones» junto con C040. Es un resaltado sin comentario: el contexto sugiere atención a la repetición léxica, no un pedido de eliminar las limitaciones metodológicas del documento.

#### C042 — apéndice

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «apéndice».
- **Contexto del PDF:** «futuro. Como complemento técnico, el apéndice A expone la arquitectura del framework».
- **Observación literal de Caro:**

  > mayúscula Apéndice

- **Corrección y detalle:** Usar «Apéndice» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C043 — documentando su diseño orientado a objetos mediante diagramas de clases en Lenguaje unificad…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «documentando su diseño orientado a objetos mediante diagramas de clases en Lenguaje unificado de modelado (Unified Modeling Language) (UML) y los patrones apli- cados para modularizar la interacción entre la simulación del tránsito y los algoritmos de aprendizaje.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Suprimir de la organización de la introducción los detalles sobre orientación a objetos, diagramas UML y patrones. Reservar su desarrollo para el apéndice y describir aquí su finalidad general.

#### C044 — marlTLC,

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 23, impresa 4; [3-introduccion.tex:80](/home/juanm4/Documentos/tesina/3-introduccion.tex:80). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «marlTLC,».
- **Contexto del PDF:** «marlTLC, documentando su diseño orientado a objetos mediante diagramas de clases en».
- **Observación literal de Caro:**

  > cita link de la web algo..... sino sacar marlTLC de la galera. O no lo pongas pon edirectamente el Apéndice A explica el framework multiagente creado en este trabajo final de grado. (poner UML y todo eso en la intro no se hace)

- **Corrección y detalle:** Presentar `marlTLC` con una referencia verificable a su repositorio o documentación, o sustituir el nombre por una descripción suficiente del software creado para la tesina. Caro propone explicar qué contiene el apéndice sin introducir UML ni un nombre sin contexto.

### Marco teórico: fundamentos de tránsito

#### C045 — aprendizaje por refuerzo

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:3](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:3). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «aprendizaje por refuerzo».
- **Contexto del PDF:** «tránsito con el aprendizaje por refuerzo para la toma de decisiones secuenciales en redes».
- **Observación literal de Caro:**

  > no olvidarse de conectar el glosario acá

- **Corrección y detalle:** Enlazar el uso visible de «aprendizaje por refuerzo» con su entrada del glosario o de acrónimos, usando una forma que no altere la redacción deseada. La inclusión de la entrada en el glosario no genera por sí sola ese enlace.

#### C046 — (sección

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(sección».
- **Contexto del PDF:** «Primero se introducen los conceptos de ingeniería de tránsito y simulación (sección».
- **Observación literal de Caro:**

  > Sección (mayúscula como Capítulo, Figura, Apéndice...)

- **Corrección y detalle:** Usar «Sección» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C047 — aprendizaje por refuerzo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «aprendizaje por refuerzo».
- **Contexto del PDF:** «2.1). Luego se desarrollan los fundamentos del aprendizaje por refuerzo y su integración».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Enlazar también esta aparición de «aprendizaje por refuerzo» en el recorrido del capítulo. La marca no tiene comentario; se interpreta por proximidad con C045 y C048 como un pedido de conexión con el glosario.

#### C048 — redes neuronales

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «redes neuronales».
- **Contexto del PDF:** «con redes neuronales (sección 2.2), seguidos de su extensión al caso multiagente y de».
- **Observación literal de Caro:**

  > linkear glosario

- **Corrección y detalle:** Enlazar «redes neuronales» con la entrada correspondiente, comprobando el plural visible. Si falta la entrada, definir nombre, texto y plural antes de usarla; verificar después enlaces y destinos del PDF.

#### C049 — (sección

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(sección».
- **Contexto del PDF:** «con redes neuronales (sección 2.2), seguidos de su extensión al caso multiagente y de».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Sección» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C050 — (sección

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(sección».
- **Contexto del PDF:** «los algoritmos MAPPO y HAPPO (sección 2.3). Finalmente, se revisan los antecedentes».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Sección» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C051 — (subsección

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:5](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:5). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(subsección».
- **Contexto del PDF:** «sentación del estado y tratamiento de la heterogeneidad (subsección 2.3.7).».
- **Observación literal de Caro:**

  > Se pone Sección no importa si es subsección.

- **Corrección y detalle:** Usar «Sección» en la referencia aunque el destino sea una subsección. Mantener el enlace mediante `\ref` y evitar números escritos a mano; aplicar el mismo criterio a los demás niveles si se adopta esa convención editorial.

#### C052 — de acuerdo con manuales especializados como el Traffic Engineering Handbook

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:9](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:9). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «de acuerdo con manuales especializados como el Traffic Engineering Handbook».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Acortar la atribución introductoria sobre ingeniería de tránsito: conservar la definición y sus citas, sin narrar que procede de manuales especializados ni repetir el título del libro en la prosa.

#### C053 — viales,

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:9](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:9). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «viales,».
- **Contexto del PDF:** «operación segura y eficiente del tránsito en calles, carreteras y redes viales, de acuerdo con».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la eliminación de «viales,» dentro de la oración completa sobre calles, carreteras y redes. Es una tachadura sin explicación: atender a la economía de expresión y a la puntuación resultante, sin borrar el concepto de red vial necesario para la definición.

#### C054 — [PW16] y con la literatura clásica del área

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:9](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:9). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[PW16] y con la literatura clásica del área».
- **Contexto del PDF:** «manuales especializados como el Traffic Engineering Handbook [PW16] y con la literatura clásica del área [CyMR18]. En este trabajo, sus conceptos se abordan desde la perspectiva».
- **Observación literal de Caro:**

  > poner las citas y chau no poner tanto bla bla bla bla

- **Corrección y detalle:** Reunir al final de la definición las referencias pertinentes y eliminar la explicación redundante sobre «literatura clásica del área». No retirar fuentes que respalden aspectos diferentes de la definición.

#### C055 — En este trabajo, sus conceptos se abordan desde la perspectiva del modelado computacional y …

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 24, impresa 5; [4-marco_teorico.tex:9](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:9). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «En este trabajo, sus conceptos se abordan desde la perspectiva del modelado computacional y la gestión adaptativa. Permiten describir el funcionamiento físico de la red, caracterizar la oferta y la demanda de circulación e identificar las variables sobre las que puede intervenir el sistema de control.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Suprimir o condensar el bloque autorreferencial tachado sobre cómo se abordan los conceptos «en este trabajo». Dar prioridad a las definiciones que el lector necesita y explicar su aplicación donde se formula el sistema concreto.

#### C056 — congestión.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 25, impresa 6; [4-marco_teorico.tex:11](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:11). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «congestión.».
- **Contexto del PDF:** «de la congestión. En áreas urbanas consolidadas, además, modificar el trazado vial re-».
- **Observación literal de Caro:**

  > poner una cite de algún trabajo de revista.

- **Corrección y detalle:** Añadir una referencia de artículo científico que respalde el límite de ampliar infraestructura como respuesta a la congestión. Identificar una fuente que trate esa afirmación concreta; no insertar una cita genérica solo para aumentar la variedad bibliográfica.

#### C057 — semafórico.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 25, impresa 6; [4-marco_teorico.tex:11](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:11). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «semafórico.».
- **Contexto del PDF:** «semafórico.».
- **Observación literal de Caro:**

  > poner cite de trabajos relacionados journals

- **Corrección y detalle:** Respaldar con artículos pertinentes la afirmación sobre estrategias contemporáneas de control dinámico y semafórico. Revisar el párrafo que cierra con «dispositivos de control semafórico» y distinguir la evidencia sobre control de la discusión de capacidad vial de C056.

#### C058 — En este contexto, se emplearán las siguientes nociones:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 25, impresa 6; [4-marco_teorico.tex:21](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:21). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «En este contexto, se emplearán las siguientes nociones:».
- **Contexto del PDF:** «En este contexto, se emplearán las siguientes nociones:».
- **Observación literal de Caro:**

  > En este contexto ya lo usaste demasiado.

- **Corrección y detalle:** Eliminar la transición repetida «En este contexto». Reescribir la introducción de la lista en coordinación con la alternativa de C059, evitando sumar otra frase introductoria equivalente.

#### C059 — Nota junto a la presentación de definiciones

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 25, impresa 6; [4-marco_teorico.tex:21](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:21). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Text):** Nota junto a la presentación de definiciones.
- **Observación literal de Caro:**

  > Entre las definiciones más utilizadas se pueden mencionar:

- **Corrección y detalle:** Introducir la lista con una frase directa, como «Entre las definiciones más utilizadas se pueden mencionar…». La nota adhesiva pertenece a la introducción de la terminología de tránsito; no debe confundirse con una observación sobre todo el capítulo.

#### C060 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 25, impresa 6; [4-marco_teorico.tex:25](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:25). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «intersectan (véase la figura 2.2). Cuando la geometría y la señalización no permiten».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C061 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 26, impresa 7; [4-marco_teorico.tex:29](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:29). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.1 ilustra estos conceptos en una intersección de cuatro accesos. Los nú-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C062 — Calle principal

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 26, impresa 7; [4-marco_teorico.tex:31](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:31). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Calle principal».
- **Contexto del PDF:** «1 6 Calle principal».
- **Observación literal de Caro:**

  > esete dibujo en el libro està bastante feo porque no pone las continuaciones de las flechas a las calles. Fijate que acá por ejemplo está también pero está mejor armado.... https://www.researchgate.net/figure/Four-legged-intersection_fig1_350083634  rehacer considerando esto.... aca otro ejemplo https://www.researchgate.net/figure/Standard-four-legs-intersection_fig3_270393077 porque sino parece que estàs pasando en contramano xD

- **Corrección y detalle:** Redibujar la intersección de cuatro accesos para que las flechas continúen de forma comprensible hacia las calles de salida y no sugieran circulación en contramano. Revisar movimientos rectos, giros, sentido de circulación y cruces peatonales; comprobar visualmente el dibujo completo. Los enlaces de Caro son referencias visuales por consultar, no fuentes ya verificadas ni autorización para copiar las imágenes.

#### C063 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 26, impresa 7; [4-marco_teorico.tex:102](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:102). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.2 presenta tres formas esquemáticas de relación entre trayectorias. Hay».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C064 — coloreados

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 27, impresa 8; [4-marco_teorico.tex:102](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:102). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «coloreados».
- **Contexto del PDF:** «separa en trayectorias diferentes. Los puntos coloreados marcan el lugar de interacción».
- **Observación literal de Caro:**

  > coloreados  ($\color{no se q nombre tiene el color del punto}\dot{}$)

- **Corrección y detalle:** Agregar en la explicación una muestra gráfica del color de los puntos de conflicto o una leyenda inequívoca. Reutilizar el color ya definido y comprobar que texto, leyenda y dibujo permitan reconocer esos puntos también sin depender exclusivamente del color.

#### C065 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 27, impresa 8; [4-marco_teorico.tex:129](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:129). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «patibles entre sí, como resume la figura 2.2. Por ello, su operación requiere ordenar estos».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C066 — distingue

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 27, impresa 8; [4-marco_teorico.tex:135](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:135). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «distingue».
- **Contexto del PDF:** «servables como el flujo, la velocidad y la densidad [PW16]. Cal y Mayor distingue estas».
- **Observación literal de Caro:**

  > distinguen con  N al final son dos personas Rafael Cal y Mayor R. junto con James Cárdenas G. (revisar que el bibtitem de las referencias esté bien)

- **Corrección y detalle:** Corregir la atribución a los autores: Caro señala que el libro corresponde a Rafael Cal y Mayor y James Cárdenas, por lo que debe revisarse «distingue» y la autoría de `calymayor`. Contrastar autor, edición y año con la publicación utilizada antes de modificar BibTeX; no inventar una forma bibliográfica a partir de la sigla de la cita.
- **Archivo adicional:** [bibliografia.bib:392](/home/juanm4/Documentos/tesina/bibliografia.bib:392), entrada `calymayor`, que actualmente solo declara a Rafael Cal y Mayor.

#### C067 — tabla

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 28, impresa 9; [4-marco_teorico.tex:137](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:137). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «tabla».
- **Contexto del PDF:** «escalas se resumen en la tabla 2.1.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Tabla» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C068 — [CyMR18]:

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 28, impresa 9; [4-marco_teorico.tex:139](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:139). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[CyMR18]:».
- **Contexto del PDF:** «[CyMR18]:».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada al introducir las variables macroscópicas. Integrarla en la atribución general del bloque o colocarla donde termine el desarrollo que respalda, evitando repetir una misma referencia antes de cada lista sin necesidad.

#### C069 — [CyMR18]:

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 28, impresa 9; [4-marco_teorico.tex:147](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:147). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[CyMR18]:».
- **Contexto del PDF:** «En el nivel microscópico, las variables asociadas son [CyMR18]:».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Aplicar a la introducción de las variables microscópicas el criterio de C068. Mantener identificable la fuente de las definiciones y resolver la combinación de cita y dos puntos dentro de una oración fluida.

#### C070 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:154](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:154). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.3 complementa estas definiciones con las magnitudes que se miden en el».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C071 — en

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:154](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:154). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «en».
- **Contexto del PDF:** «vehículos consecutivos, también en m. El avance temporal β es el tiempo asociado al».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Suprimir o reacomodar «en» al reemplazar «en m» por una expresión completa. La versión actual dice «también en metros»; revisar junto con C072 si se da por satisfecha la finalidad de claridad.

#### C072 — m.

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:154](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:154). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «m.».
- **Contexto del PDF:** «vehículos consecutivos, también en m. El avance temporal β es el tiempo asociado al».
- **Observación literal de Caro:**

  > expresada en metros

- **Corrección y detalle:** Escribir «expresada en metros» o una forma equivalente que identifique con claridad la unidad del espaciamiento. La fuente actual desarrolla «metros»; mantener la concordancia con «distancia».

#### C073 — s)

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:169](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:169). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «s)».
- **Contexto del PDF:** «s) vehículos sucesivos».
- **Observación literal de Caro:**

  > a s la tenes usada en otra cosa poner seg. si se trata de segundos.

- **Corrección y detalle:** Distinguir el símbolo de espaciamiento `s` de la unidad de tiempo en la tabla. Caro propone «seg.»; el texto actual usa «segundos», que evita la ambigüedad. Si se prefieren símbolos, usar formato de unidad y una convención coherente, sin cambiar el significado matemático de `s`.

#### C074 — Puntuación de la línea indicada en el contexto

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:170](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:170). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (StrikeOut):** Puntuación de la línea indicada en el contexto.
- **Contexto del PDF:** «(s, m) paragolpes homólogos».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la pequeña tachadura de la fila «Espaciamiento simple (s, m)»: afecta la separación tipográfica entre variable y unidad y debe resolverse con C075. La inspección visual confirma su ubicación en esa celda; no hay comentario escrito que autorice otra interpretación.

#### C075 — (s, m)

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:170](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:170). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(s, m)».
- **Contexto del PDF:** «(s, m) paragolpes homólogos».
- **Observación literal de Caro:**

  > s (metros)

- **Corrección y detalle:** Presentar el espaciamiento como símbolo y unidad claramente separados, por ejemplo «s (metros)», siguiendo la propuesta de Caro. El texto actual ya usa «(s, metros)»; comprobar legibilidad y uniformidad con las restantes filas antes de cerrar la tarea.

#### C076 — La figura 2.3 presenta de manera conjunta estas distancias y tiempos entre vehículos, y perm…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 29, impresa 10; [4-marco_teorico.tex:174](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:174). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La figura 2.3 presenta de manera conjunta estas distancias y tiempos entre vehículos, y permite interpretar cómo las magnitudes microscópicas describen la separación y el avance de una corriente.».
- **Observación literal de Caro:**

  > este texto va arriba cuando hablas de la figura... no dividas la expliacciòn de una misma figura e párrafos distintos.

- **Corrección y detalle:** Unificar con la primera explicación de la Figura 2.3 el párrafo que comienza «La figura… presenta de manera conjunta…». Evitar introducir la figura, intercalar una tabla y luego volver a presentarla; conservar una explicación continua antes de su aparición.

#### C077 — Estas variables

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 30, impresa 11; [4-marco_teorico.tex:229](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:229). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Estas variables».
- **Contexto del PDF:** «Estas variables macroscópicas se relacionan de manera directa a través de la ecuación».
- **Observación literal de Caro:**

  > Por su parte las variables macroscópicas.......

- **Corrección y detalle:** Reemplazar «Estas variables» por «Por su parte, las variables macroscópicas…» o un sujeto explícito equivalente. El lector viene de magnitudes microscópicas y necesita reconocer el cambio de escala antes de la ecuación fundamental.

#### C078 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 30, impresa 11; [4-marco_teorico.tex:234](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:234). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «donde q es la tasa de flujo, k es la densidad y v s es la velocidad media espacial. La ecuación».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C079 — La velocidad media temporal (v t ) es la media aritmética de las velocidades observadas en u…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 30, impresa 11; [4-marco_teorico.tex:234](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:234). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La velocidad media temporal (v t ) es la media aritmética de las velocidades observadas en un punto durante un intervalo, mientras que v s , asociada al promedio de las velocidades de una muestra espacial tomada sobre un tramo, se estima en la práctica como media armónica de las velocidades puntuales medidas en una sección durante un intervalo.».
- **Observación literal de Caro:**

  > esto lo tenes definido arriba.... estas como repitiendote...O reorganizas todo para que sean definiciones y ecuaciones todo junto... porque estás todo el tiempo repitiendo cosas.

- **Corrección y detalle:** Reorganizar la definición de velocidades medias y la relación de Wardrop para explicar cada concepto una sola vez. Integrar definición, ecuación, símbolos e interpretación, y evitar repetir en prosa lo que ya se presentó en la lista de variables.

#### C080 — (2.2)

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 30, impresa 11; [4-marco_teorico.tex:236](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:236). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(2.2)».
- **Contexto del PDF:** «v t = v s + σ s 2 v s (2.2)».
- **Observación literal de Caro:**

  > Para mi toda la parte esta que tenes repetida va a continuación de donde definiste las velocidades.

- **Corrección y detalle:** Mover la relación de Wardrop y su interpretación junto a la primera definición de velocidades medias. Mantener la etiqueta existente y actualizar referencias si cambia el orden de las ecuaciones; no duplicar la ecuación para resolver la continuidad.

#### C081 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 30, impresa 11; [4-marco_teorico.tex:239](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:239). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «espacio. La ecuación (2.2) muestra que, dado que la varianza es no negativa (σ s 2 ≥ 0), se».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C082 — N 0

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 31, impresa 12; [4-marco_teorico.tex:261](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:261). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «N 0».
- **Contexto del PDF:** «donde X ∈ N 0 es la variable aleatoria discreta que representa el número de arribos vehicu-».
- **Observación literal de Caro:**

  > naturales unido el cero? \mathbb{N} \cup \{0\}

- **Corrección y detalle:** Definir sin ambigüedad el conjunto de valores del número de llegadas: usar `\mathbb{N}\cup\{0\}` si se adopta la convención de Caro, o declarar expresamente qué significa `\mathbb{N}_0`. Comprobar la coherencia con la definición de naturales empleada en el resto del documento.

#### C083 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 31, impresa 12; [4-marco_teorico.tex:261](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:261). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «base del logaritmo natural. La ecuación (2.3) formaliza esta probabilidad discreta. Bajo el».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C084 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 31, impresa 12; [4-marco_teorico.tex:266](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:266). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «tiempo analizado. La ecuación (2.4) expresa la probabilidad de que el intervalo supere».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C085 — dicho umbral.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:266](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:266). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «dicho umbral.».
- **Contexto del PDF:** «dicho umbral.».
- **Observación literal de Caro:**

  > linea huerfana. Por ahí podes poner punto seguido a la oración que viene más abajo.

- **Corrección y detalle:** Evitar que «dicho umbral» quede como línea aislada. Evaluar unir la explicación con el párrafo siguiente si hay continuidad conceptual o reformular la oración; confirmar el resultado en el PDF después de la reestructuración.

#### C086 — [CyMR18].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:268](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:268). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[CyMR18].».
- **Contexto del PDF:** «de semáforos cercanos en intersecciones precedentes [CyMR18]. El supuesto pierde validez».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Reubicar la cita tachada sobre el supuesto de arribos independientes al cierre del desarrollo que sostiene, junto con C088. No trasladarla de modo que parezca respaldar datos propios o una curva empírica inexistente.

#### C087 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:268](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:268). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «temporal entre arribos consecutivos. La figura 2.4 compara conceptualmente los intervalos».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C088 — particular.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:268](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:268). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «particular.».
- **Contexto del PDF:** «lo tanto, función ilustrativa y no constituyen una distribución empírica particular.».
- **Observación literal de Caro:**

  > poner la cita acá abajo una vez que terminaste de explicar.

- **Corrección y detalle:** Colocar la referencia al terminar de explicar el modelo y la figura conceptual, como pide Caro. Aclarar qué contenido procede de la fuente y qué elementos del esquema son ilustrativos.

#### C089 — En este trabajo,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:270](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:270). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En este trabajo,».
- **Contexto del PDF:** «En este trabajo, la limitación de esos modelos analíticos motiva el uso de simulación».
- **Observación literal de Caro:**

  > En esta tesina final de grado

- **Corrección y detalle:** Reemplazar «En este trabajo» por una denominación institucional consistente, como «En esta tesina de grado», si mejora la identificación del aporte propio. No es necesario alternar todas las variantes propuestas en los comentarios.

#### C090 — esos

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:270](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:270). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «esos».
- **Contexto del PDF:** «En este trabajo, la limitación de esos modelos analíticos motiva el uso de simulación».
- **Observación literal de Caro:**

  > los modemos analíticos

- **Corrección y detalle:** Sustituir «esos» por «los modelos analíticos» para explicitar el antecedente. Corregir también el probable error de tipeo del comentario («modemos») al redactar la versión final.

#### C091 — En

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:270](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:270). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En».
- **Contexto del PDF:** «microscópica para estudiar el control semafórico bajo condiciones variables. En SUMO,».
- **Observación literal de Caro:**

  > Por ejemplo, en el simulador

- **Corrección y detalle:** Reformular «En SUMO…» como ejemplo del uso de simulación microscópica, por ejemplo «Por ejemplo, en el simulador SUMO…». Evitar que una transición ilustrativa se lea como una justificación validada del experimento.

#### C092 — La figura 2.4 se interpreta comparando la forma de ambas curvas. El eje horizontal represent…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:309](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:309). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La figura 2.4 se interpreta comparando la forma de ambas curvas. El eje horizontal representa el intervalo h entre vehículos y el eje vertical la densidad de probabilidad f (h), es decir, la concentración relativa de intervalos alrededor de cada valor. En el modelo exponencial, la densidad disminuye desde el origen y asigna mayor frecuencia relativa a los intervalos breves. En la representación con agrupamientos vehiculares, la densidad comienza después de h mı́n y alcanza un máximo alejado del origen, lo que ilustra que el arribo de un vehículo queda condicionado por la separación y la coordinación con los que lo preceden. La comparación permite reconocer por qué el supuesto de arribos».
- **Observación literal de Caro:**

  > esto tiene que ir seguido a cuando hablas de la fitgura 2.4. o sea si hablas de una figura arrancas y terminas en el mismo lugar. No se mete la figura en el medio. arreglar en todos los lugares donde hayas realizado esto de hablar de figura figura y luego volver a hablar de la figura. Es super raro

- **Corrección y detalle:** Reunir la presentación de la Figura 2.4, el significado de los ejes y la interpretación de las curvas en un único desarrollo antes de la figura. Separar después, si hace falta, la consecuencia para la elección de simulación. Extender este control al resto de las figuras sin imponer que toda explicación deba ser un único párrafo excesivo.

#### C093 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 32, impresa 13; [4-marco_teorico.tex:309](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:309). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.4 se interpreta comparando la forma de ambas curvas. El eje horizontal».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C094 — [CyMR18].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:309](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:309). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[CyMR18].».
- **Contexto del PDF:** «[CyMR18].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada al cierre de la explicación de la Figura 2.4. Resolverla junto con C086 y C088 para no eliminar toda atribución ni repetir la misma cita en tramos contiguos del mismo argumento.

#### C095 — investigación,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:321](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:321). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «investigación,».
- **Contexto del PDF:** «t rojo_todo ) [PW16]. En esta investigación, esos tiempos se consideran restricciones opera-».
- **Observación literal de Caro:**

  > trabajo final de grado

- **Corrección y detalle:** Cambiar «investigación» por la denominación elegida para este trabajo final cuando se alude al tratamiento de los tiempos semafóricos. Mantener en el marco teórico la explicación general y en metodología las restricciones y valores aplicados.

#### C096 — esos

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:321](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:321). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «esos».
- **Contexto del PDF:** «t rojo_todo ) [PW16]. En esta investigación, esos tiempos se consideran restricciones opera-».
- **Observación literal de Caro:**

  > estos

- **Corrección y detalle:** Reemplazar «esos tiempos» por «estos tiempos» o nombrar los intervalos concretos para conservar un antecedente próximo. Asegurar que se comprende qué restricciones operacionales se heredan de los tiempos semafóricos.

#### C097 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:325](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:325). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «fila puede disiparse cuando el movimiento tiene prioridad [FA11]. En la figura 2.5, q máx».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C098 — en

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:325](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:325). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «en».
- **Contexto del PDF:** «tasa de flujo en veh/h. La barra inferior distingue los intervalos de rojo, verde y amarillo,».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar la construcción abreviada «en veh/h» al desarrollar la unidad con palabras. Revisar el resultado conjuntamente con C099 para que no quede una preposición suelta.

#### C099 — veh/h.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 33, impresa 14; [4-marco_teorico.tex:325](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:325). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «veh/h.».
- **Contexto del PDF:** «tasa de flujo en veh/h. La barra inferior distingue los intervalos de rojo, verde y amarillo,».
- **Observación literal de Caro:**

  > medida en vehículos por hora.

- **Corrección y detalle:** Escribir «medida en vehículos por hora» al definir la tasa de flujo de la figura. Conservar el mismo criterio de unidades en ejes, prosa y tabla de variables.

#### C100 — La figura 2.5 debe leerse como una relación temporal: las pérdidas l 1 y l 2 reducen el inte…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 34, impresa 15; [4-marco_teorico.tex:365](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:365). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La figura 2.5 debe leerse como una relación temporal: las pérdidas l 1 y l 2 reducen el intervalo en que la fase puede descargar vehículos a la tasa q máx . Por tanto, el verde efectivo g no equivale necesariamente al verde nominal programado en el controlador.».
- **Observación literal de Caro:**

  > ponerla en su lugar como explique con las otras figuras

- **Corrección y detalle:** Mover la interpretación de pérdidas, tasa máxima y verde efectivo al bloque donde se presenta la Figura 2.5. Explicar allí por qué el verde efectivo difiere del nominal, evitando retomar la misma figura después de interrumpir el argumento.

#### C101 — clásicamente

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 34, impresa 15; [4-marco_teorico.tex:369](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:369). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «clásicamente».
- **Contexto del PDF:** «cular, los controladores de semáforos se clasifican clásicamente en control de tiempo fijo y».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar «clásicamente» si no agrega una distinción histórica necesaria. Presentar directamente la clasificación de controladores de tiempo fijo y accionados, conservando las fuentes pertinentes.

#### C102 — Incluso en los esquemas accionados,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 34, impresa 15; [4-marco_teorico.tex:371](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:371). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Incluso en los esquemas accionados,».
- **Contexto del PDF:** «Incluso en los esquemas accionados, la operación permanece sujeta a parámetros límite».
- **Observación literal de Caro:**

  > esto quedó super

- **Corrección y detalle:** Revisar el inicio «Incluso en los esquemas accionados…» y su enlace con el párrafo anterior. El comentario quedó incompleto («esto quedó super»): no permite atribuir una corrección más específica; evaluar claridad, continuidad y propósito de la comparación.

### Simulación y SUMO

#### C103 — de

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 35, impresa 16; [4-marco_teorico.tex:373](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:373). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «de».
- **Contexto del PDF:** «2.1.4. Simulación de tránsito».
- **Observación literal de Caro:**

  > del

- **Corrección y detalle:** Corregir el título a «Simulación del tránsito» si se adopta la sugerencia «del». Revisar uniformidad con otros títulos y con las denominaciones utilizadas en índice y referencias.

#### C104 — Los modelos macroscópicos describen el tránsito de manera agregada mediante variables como f…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 35, impresa 16; [4-marco_teorico.tex:375](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:375). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Los modelos macroscópicos describen el tránsito de manera agregada mediante variables como flujo, densidad y velocidad; los mesoscópicos representan entidades inter- medias, como agrupamientos vehiculares; y los microscópicos modelan individualmente los vehículos, sus rutas y su evolución dentro de la red. Para esta investigación resulta especialmente relevante este último nivel, pues permite examinar cómo las decisiones se- mafóricas inciden en la formación de colas, las detenciones y las interacciones locales entre vehículos.».
- **Observación literal de Caro:**

  > ya lo explicaste antes no repetirse

- **Corrección y detalle:** Evitar repetir la clasificación de modelos macroscópicos, mesoscópicos y microscópicos ya explicada. Reducir este pasaje a lo necesario para justificar el nivel de simulación y enlazar con SUMO, manteniendo una distinción mínima si el nivel mesoscópico todavía no fue presentado.

#### C105 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 35, impresa 16; [4-marco_teorico.tex:377](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:377). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «estudio. La correspondencia entre el fenómeno y su representación se resume en la figura».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C106 — DLR – Institute of Transportation Systems, SUMO User Documentation

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:382](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:382). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «DLR – Institute of Transportation Systems, SUMO User Documentation».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar la identificación institucional extensa del epígrafe y dejar una atribución bibliográfica compacta. Conservar la fuente real de la imagen y revisar que no se pierdan los requisitos de atribución aplicables.

#### C107 — La figura 2.6 muestra, de forma sintética, la correspondencia entre una escena vial y su rep…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:386](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:386). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La figura 2.6 muestra, de forma sintética, la correspondencia entre una escena vial y su representación microscópica en SUMO.».
- **Observación literal de Caro:**

  > subir al otro párrafo

- **Corrección y detalle:** Integrar «La figura 2.6 muestra…» en el párrafo previo que presenta la correspondencia entre circulación real y simulación. Evitar otra explicación separada después de la imagen.

#### C108 — Su función es ilustrar cómo los vehículos y la infraestructura se transforman en entidades c…

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:386](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:386). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Su función es ilustrar cómo los vehículos y la infraestructura se transforman en entidades computacionales; no constituye una validación del simulador ni una representación del escenario utilizado en este trabajo.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar o condensar la explicación negativa tachada sobre lo que la figura «no constituye». Si es necesario advertir que es un esquema y no una validación, decirlo brevemente sin convertir el epígrafe o el texto en una lista de exclusiones.

#### C109 — pertenece

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:388](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:388). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «pertenece».
- **Contexto del PDF:** «SUMO pertenece a la categoría microscópica descrita por Fernández [FA11]. Es una».
- **Observación literal de Caro:**

  > poner lo que significa SUMO o sea usar el \acrfull

- **Corrección y detalle:** Desarrollar SUMO al comenzar su presentación como simulador microscópico mediante `\acrfull{acr-sumo}` u otra macro coherente. Evitar que la primera definición sustantiva de la herramienta dependa de una expansión previa alejada.

#### C110 — modelo;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:392). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «modelo;».
- **Contexto del PDF:** «función de apoyo para la inspección del escenario y la depuración del modelo; las métricas».
- **Observación literal de Caro:**

  > . seguido

- **Corrección y detalle:** Sustituir el punto y coma posterior a «modelo» por punto seguido y ajustar la mayúscula siguiente. Revisar que las dos oraciones distingan la inspección visual de la obtención de métricas.

#### C111 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:392). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «de control [DLR26]. La interfaz y su función de inspección se muestran en la figura 2.7;».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C112 — 2.7;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:392). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «2.7;».
- **Contexto del PDF:** «de control [DLR26]. La interfaz y su función de inspección se muestran en la figura 2.7;».
- **Observación literal de Caro:**

  > no entiendo el ;

- **Corrección y detalle:** Cambiar el punto y coma después de la referencia a la Figura 2.7 por una construcción clara, coordinada con la eliminación de C113. No dejar una referencia colgante ni una cláusula sin sujeto.

#### C113 — la Interfaz gráfica de usuario (Graphical User Interface) (GUI) no constituye la fuente de l…

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 36, impresa 17; [4-marco_teorico.tex:392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:392). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «la Interfaz gráfica de usuario (Graphical User Interface) (GUI) no constituye la fuente de las métricas ni reemplaza su cálculo operacional.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar la oración tachada sobre que la GUI no es fuente de métricas si repite lo dicho inmediatamente antes. Conservar una explicación positiva y suficiente de dónde se obtienen las métricas en la sección correspondiente.

#### C114 — El panel izquierdo presenta una vista general de la red; el derecho muestra información sobr…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 37, impresa 18; [4-marco_teorico.tex:397](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:397). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «El panel izquierdo presenta una vista general de la red; el derecho muestra información sobre un vehículo particular; el recuadro inferior grafica su velocidad y el superior muestra los valores de sus variables relacionadas.».
- **Observación literal de Caro:**

  > explicalo donde hablas de la figura.

- **Corrección y detalle:** Mover la descripción de paneles de `sumo-gui` desde el epígrafe al texto donde se introduce la figura. Revisar además que la explicación corresponda exactamente a la imagen y no duplique el párrafo que ya describe sus zonas de inspección.

#### C115 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 37, impresa 18; [4-marco_teorico.tex:401](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:401). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.7 reúne cuatro zonas de inspección. A la izquierda se observa la red com-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C116 — [DLR26].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 37, impresa 18; [4-marco_teorico.tex:401](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:401). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[DLR26].».
- **Contexto del PDF:** «[DLR26].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita aislada tachada al final de la descripción de la interfaz. Al reunir el desarrollo, mantener una atribución suficiente y evitar la repetición de la misma referencia sin una nueva afirmación que la requiera.

#### C117 — Esta granularidad

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 37, impresa 18; [4-marco_teorico.tex:403](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:403). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Esta granularidad».
- **Contexto del PDF:** «Esta granularidad vuelve a la simulación microscópica especialmente adecuada para».
- **Observación literal de Caro:**

  > Cuál??? Arrancar oraciones con Esta ESA no sirve más aún porque estas comenzando un párrafo nuevo entonces se comienza con La granularidad ...... (pones a que granularidad te referis) o reescribilo como La simulación microscópica provista por SUMO resulta apropiada ..................... (y ahí enganchas la oración)

- **Corrección y detalle:** Reemplazar «Esta granularidad» por un sujeto explícito, por ejemplo «La simulación microscópica provista por SUMO…». No iniciar otro párrafo con un demostrativo cuyo referente obliga a releer.

#### C118 — vuelve a la simulación microscópica especialmente

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 37, impresa 18; [4-marco_teorico.tex:403](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:403). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «vuelve a la simulación microscópica especialmente».
- **Contexto del PDF:** «Esta granularidad vuelve a la simulación microscópica especialmente adecuada para».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Reformular «vuelve a la simulación microscópica especialmente…» junto con C117 para evitar el giro redundante. Es un resaltado sin comentario adicional y debe leerse como parte de esa misma observación de claridad.

#### C119 — [DLR26].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 38, impresa 19; [4-marco_teorico.tex:407](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:407). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[DLR26].».
- **Contexto del PDF:** «pertenecen a la configuración experimental y se detallan en la metodología [DLR26].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada al final del párrafo sobre seguimiento y cambio de carril. Colocar la referencia junto a los modelos que respalda y trasladar a metodología cualquier decisión experimental concreta.

#### C120 — el simulador de tránsito

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 38, impresa 19; [4-marco_teorico.tex:409](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:409). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «el simulador de tránsito».
- **Contexto del PDF:** «En este contexto, el simulador de tránsito constituye el entorno operativo sobre el cual».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Sustituir el sujeto genérico «el simulador de tránsito» por «SUMO» en este pasaje, coordinando con C121. El lector debe identificar la herramienta concreta antes de la figura de la intersección.

#### C121 — En este contexto,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 38, impresa 19; [4-marco_teorico.tex:409](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:409). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En este contexto,».
- **Contexto del PDF:** «En este contexto, el simulador de tránsito constituye el entorno operativo sobre el cual».
- **Observación literal de Caro:**

  > En este trabajo final de carrera SUMO constituye

- **Corrección y detalle:** Eliminar «En este contexto» y formular directamente el papel de SUMO en el trabajo final. Evitar presentar una transición repetida como si aportara una nueva justificación metodológica.

#### C122 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 38, impresa 19; [4-marco_teorico.tex:409](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:409). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «se formaliza el problema de control semafórico. La figura 2.8 esquematiza la representación».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C123 — [DLR26],

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 38, impresa 19; [4-marco_teorico.tex:409](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:409). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[DLR26],».
- **Contexto del PDF:** «microscópica de una intersección con circulación por la derecha [DLR26], en la que se».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada después de «circulación por la derecha». Distinguir la atribución del esquema propio de la documentación de SUMO y ubicar cada fuente junto a lo que realmente respalda.

#### C124 — y

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 39, impresa 20; [4-marco_teorico.tex:504](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:504). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «y».
- **Contexto del PDF:** «de la intersección y respetar las transiciones y restricciones de seguridad definidas por el».
- **Observación literal de Caro:**

  > sacar esta y y poner -> además de ...

- **Corrección y detalle:** Sustituir la conjunción indicada por «además de…» si mejora la estructura de la oración. Comprobar que queda paralela la enumeración de movimientos y transiciones o restricciones de seguridad.

#### C125 — externas

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 39, impresa 20; [4-marco_teorico.tex:508](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:508). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «externas».
- **Contexto del PDF:** «simulaciones, visualizar sus resultados y controlar la ejecución mediante interfaces externas».
- **Observación literal de Caro:**

  > entre las que es relevante mencionar:

- **Corrección y detalle:** Introducir explícitamente la lista de herramientas externas, por ejemplo «…entre las que es relevante mencionar…». Explicar antes su función común para que la enumeración no aparezca desconectada.

#### C126 — OpenStreetMap

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 39, impresa 20; [4-marco_teorico.tex:512](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:512). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «OpenStreetMap».
- **Contexto del PDF:** «partir de un área seleccionada de OpenStreetMap (OSM). Se considera una alter-».
- **Observación literal de Caro:**

  > falta cita a la página web de openstreetmap

- **Corrección y detalle:** Añadir una referencia al sitio o fuente institucional de OpenStreetMap cuando se introduce como origen cartográfico. Reutilizar o completar una entrada bibliográfica verificable y comprobar que la sigla OSM se desarrolla de forma consistente.

#### C127 — de

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 40, impresa 21; [4-marco_teorico.tex:517](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:517). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «de».
- **Contexto del PDF:** «Desde la perspectiva del modelado computacional, una simulación de SUMO se cons-».
- **Observación literal de Caro:**

  > en

- **Corrección y detalle:** Cambiar «una simulación de SUMO» por «una simulación en SUMO» en el párrafo que presenta los archivos de entrada. Revisar la misma formulación en el epígrafe de la tabla si se adopta ese criterio; no hacer un reemplazo global de la preposición «de».

#### C128 — tabla

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 40, impresa 21; [4-marco_teorico.tex:517](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:517). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «tabla».
- **Contexto del PDF:** «se resumen en la tabla 2.2:».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Tabla» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C129 — 2.2:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 40, impresa 21; [4-marco_teorico.tex:517](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:517). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «2.2:».
- **Contexto del PDF:** «se resumen en la tabla 2.2:».
- **Observación literal de Caro:**

  > reemplazar por un punto .

- **Corrección y detalle:** Cerrar con punto la oración que remite a la Tabla 2.2, en lugar de añadir dos puntos innecesarios. Mantener la tabla introducida y su contenido explicado en el texto.

#### C130 — Puntuación de la línea indicada en el contexto

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:542](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:542). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Highlight):** Puntuación de la línea indicada en el contexto.
- **Contexto del PDF:** «y su relación con la demanda generada permiten distinguir una reducción genuina».
- **Observación literal de Caro:**

  > coma

- **Corrección y detalle:** Revisar la coma indicada dentro del ítem sobre completitud: separar con claridad la cantidad de vehículos que completa el recorrido, su relación con la demanda y la conclusión sobre flujo atendido. La marca está entre «demanda generada» y «permiten»; evitar insertar una coma que separe indebidamente sujeto y verbo y reformular la oración si es necesario.

#### C131 — normalizada.

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:538](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:538). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «normalizada.».
- **Contexto del PDF:** «medida normalizada.».
- **Observación literal de Caro:**

  > cita al manual de HBEFA (contaminantes) https://www.hbefa.net/

- **Corrección y detalle:** El pasaje original pedía citar el manual HBEFA al describir la medida normalizada de emisiones. Esa formulación ya no aparece en el bloque actual de indicadores; comprobar si la explicación se trasladó a metodología u otro apartado y añadir allí la fuente primaria solo si se conserva o utiliza ese indicador. No reintroducir una métrica de emisiones que no se haya evaluado.
- **Ubicación actual:** se enlaza el bloque de indicadores por correspondencia temática; no hay un ítem de emisiones equivalente en ese bloque actual. La referencia HBEFA pedida debe evaluarse donde se describan emisiones, si se conservan.

#### C132 — RL y MARL.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:547](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:547). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «RL y MARL.».
- **Contexto del PDF:** «ritmos de aprendizaje y se desarrollan en las secciones dedicadas a RL y MARL.».
- **Observación literal de Caro:**

  > poner acrfull para cada abreviatura

- **Corrección y detalle:** Desarrollar RL y MARL en la remisión a las secciones de aprendizaje, como propone Caro. Verificar que la expansión no sature el cierre ni repita desarrollos inmediatamente anteriores; usar macros existentes y una política uniforme.

#### C133 — [DLR26].

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:549](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:549). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[DLR26].».
- **Contexto del PDF:** «del aprendizaje por refuerzo en la siguiente sección [DLR26].».
- **Observación literal de Caro:**

  > No es la única cita del universo sobre SUMO hay más

- **Corrección y detalle:** Diversificar las referencias de SUMO: usar su publicación científica para presentar el simulador y la documentación para interfaces, archivos y medidas concretas. Revisar esta cita de cierre en conjunto con C142, sin borrar la documentación donde es la fuente apropiada.

### Aprendizaje por refuerzo

#### C134 — (Machine Learning) (ML)

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:554](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:554). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Machine Learning) (ML)».
- **Contexto del PDF:** «El Aprendizaje automático (Machine Learning) (ML) suele dividirse en tres paradig-».
- **Observación literal de Caro:**

  > En realidad debería decir (Machine Learning, ML) hay demasiados paréntesis que molestan en el texto.

- **Corrección y detalle:** Unificar los paréntesis de término inglés y sigla: «aprendizaje automático (Machine Learning, ML)». Revisar la macro global de acrónimos; corregirla una sola vez si el problema afecta todas las expansiones y comprobar los usos restantes.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C135 — (Supervised Learning) (SL),

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:554](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:554). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Supervised Learning) (SL),».
- **Contexto del PDF:** «mas. En el Aprendizaje supervisado (Supervised Learning) (SL), el modelo se entrena con».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Aplicar el formato de C134 a aprendizaje supervisado: término inglés y SL dentro de un único paréntesis, evitando grupos consecutivos.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C136 — (Unsupervised Learning) (UL),

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:554](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:554). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Unsupervised Learning) (UL),».
- **Contexto del PDF:** «(Unsupervised Learning) (UL), se busca descubrir estructura en datos no etiquetados, por».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Aplicar el formato de C134 a aprendizaje no supervisado: término inglés y UL dentro de un único paréntesis, con el mismo criterio tipográfico y de mayúsculas.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C137 — (Reinforcement Learning) (RL)

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:554](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:554). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Reinforcement Learning) (RL)».
- **Contexto del PDF:** «fuerzo (Reinforcement Learning) (RL) aborda un problema distinto: una entidad aprende».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Aplicar el formato de C134 a aprendizaje por refuerzo: término inglés y RL en un único paréntesis. Revisar también que la macro no produzca una expansión redundante al repetir el término español por fuera.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C138 — central.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 41, impresa 22; [4-marco_teorico.tex:556](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:556). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «central.».
- **Contexto del PDF:** «Esta diferencia es central. En RL no existe, en general, un supervisor que indique cuál».
- **Observación literal de Caro:**

  > sacar punto poner coma. Es una oración muy pequeña ligarla a la que viene después

- **Corrección y detalle:** Integrar «Esta diferencia es central» con la explicación que sigue o reemplazarla por una transición informativa. Evitar una oración breve que solo anuncia importancia sin explicar todavía cuál es la diferencia.

#### C139 — función de valor

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:558](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:558). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «función de valor».
- **Contexto del PDF:** «la función de valor estima la conveniencia de estados o acciones en términos de recom-».
- **Observación literal de Caro:**

  > pusiste cada término en inglés también pone función de valor con su correspondiente uso en inglés.

- **Corrección y detalle:** Añadir el equivalente inglés de «función de valor» en su primera definición, si esa es la convención adoptada para los otros términos del bloque. Enlazar al glosario y evitar repetir la traducción en cada aparición.

#### C140 — Mención explícita de Sutton y Barto

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:558](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:558). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Text):** Mención explícita de Sutton y Barto.
- **Observación literal de Caro:**

  > Sutton y Barto \cite{}

- **Corrección y detalle:** Añadir la cita a Sutton y Barto donde se los menciona explícitamente al distinguir el modelo del entorno. Reutilizar `suttonRL`, verificando que corresponda a la edición de 2018 ya definida.

#### C141 — recompensas;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:558](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:558). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «recompensas;».
- **Contexto del PDF:** «una descripción de sus transiciones y recompensas; cuando no se conoce o no se utiliza».
- **Observación literal de Caro:**

  > punto

- **Corrección y detalle:** Cambiar el punto y coma después de «recompensas» por punto seguido y ajustar «Cuando…». Conservar la relación entre definición de modelo y métodos libres de modelo.

#### C142 — aprendizaje

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:560](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:560). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «aprendizaje».
- **Contexto del PDF:** «y una señal de recompensa que orienta el aprendizaje [DLR26].».
- **Observación literal de Caro:**

  > en la web de sumo dice como citar sumo!!!  esta es la cita de SUMO oficial -> @INPROCEEDINGS{Alvarez2018,
  >   author={Lopez, Pablo Alvarez and Behrisch, Michael and Bieker-Walz, Laura and Erdmann, Jakob and Flötteröd, Yun-Pang and Hilbrich, Robert and Lücken, Leonhard and Rummel, Johannes and Wagner, Peter and Wiessner, Evamarie},
  >   booktitle={2018 21st International Conference on Intelligent Transportation Systems (ITSC)}, 
  >   title={Microscopic Traffic Simulation using SUMO}, 
  >   year={2018},
  >   volume={},
  >   number={},
  >   pages={2575-2582},
  >   keywords={Tools;Microscopy;Roads;Data models;Urban areas;Vehicle dynamics;Mathematical model},
  >   doi={10.1109/ITSC.2018.8569938}
  >   }

- **Corrección y detalle:** Incorporar y verificar la publicación científica oficial de SUMO proporcionada por Caro: «Microscopic Traffic Simulation using SUMO», ITSC 2018, pp. 2575–2582, DOI `10.1109/ITSC.2018.8569938`. Confirmar autores, clave y campos BibTeX antes de incorporarla y citarla en la presentación del simulador. No usarla como evidencia de una aplicación de RL que el artículo no trate.

#### C143 — Para fijar ideas,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:562](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:562). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Para fijar ideas,».
- **Contexto del PDF:** «Para fijar ideas, considérese un par de intersecciones vecinas. El agente observa local-».
- **Observación literal de Caro:**

  > Muy coloquial para un texto de tesina.... Además si no hay figura no sirve. En la Figura ... se observan un par de intersecciones .....................

- **Corrección y detalle:** Reescribir «Para fijar ideas» con un registro académico y un propósito explícito. Si se incorpora una figura de dos intersecciones, introducirla y explicar qué muestra; si se mantiene el ejemplo solo en prosa, presentarlo directamente sin anunciar una figura inexistente.

#### C144 — [SB18].

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:564](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:564). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[SB18].».
- **Contexto del PDF:** «experiencia futura disponible para el aprendizaje [SB18].».
- **Observación literal de Caro:**

  > poner una cita de algun trabajo que use RL para cambiar

- **Corrección y detalle:** Añadir una referencia de aplicación de RL pertinente al ejemplo o a la discusión de exploración y control. Elegir una fuente que respalde esa afirmación concreta y no sustituir automáticamente la referencia fundacional cuando es la que corresponde.

#### C145 — (Markov Decision Process) (MDP).

- [ ] **Editorial · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:568](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:568). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Markov Decision Process) (MDP).».
- **Contexto del PDF:** «de un solo agente es el Proceso de decisión de Markov (Markov Decision Process) (MDP).».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Corregir el desarrollo de MDP para que el término inglés y la sigla compartan paréntesis y no queden dos grupos consecutivos. Revisar su primera aparición y el título opcional de la sección si cambia el comando de acrónimo.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C146 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 42, impresa 23; [4-marco_teorico.tex:568](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:568). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «emite R t+1 ∈ R y transita a S t+1 [LML + 25]. La notación se ilustra en la figura 2.9.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C147 — [SB18].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 43, impresa 24; [4-marco_teorico.tex:593](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:593). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[SB18].».
- **Contexto del PDF:** «Figura 2.9: Interacción agente-entorno en un proceso de decisión de Markov [SB18].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada en el epígrafe de la interacción agente-entorno. Mantener la atribución si el esquema deriva de Sutton y Barto, pero evitar repetición innecesaria al unificar su explicación.

#### C148 — el

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 43, impresa 24; [4-marco_teorico.tex:597](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:597). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «el».
- **Contexto del PDF:** «donde S es el espacio de estados, A el espacio de acciones, P la dinámica de transición».
- **Observación literal de Caro:**

  > falta el verbo es

- **Corrección y detalle:** Completar la definición de `\mathcal{A}` con «es el espacio de acciones». Mantener el paralelismo gramatical con la definición de `\mathcal{S}`.

#### C149 — la

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 43, impresa 24; [4-marco_teorico.tex:597](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:597). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «la».
- **Contexto del PDF:** «donde S es el espacio de estados, A el espacio de acciones, P la dinámica de transición».
- **Observación literal de Caro:**

  > falta el verbo es

- **Corrección y detalle:** Completar la definición de `P` con «es la dinámica de transición probabilística» o una construcción equivalente. No dejar una lista de símbolos sin verbos dentro de una oración que pretende definirlos.

#### C150 — la

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 43, impresa 24; [4-marco_teorico.tex:597](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:597). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «la».
- **Contexto del PDF:** «probabilística, R la función de recompensa y γ ∈ [0, 1) el factor de descuento.».
- **Observación literal de Caro:**

  > falta el verbo es

- **Corrección y detalle:** Completar la definición de `R` con «es la función de recompensa». Mantener la notación consistente con la dinámica conjunta de estados y recompensas explicada después.

#### C151 — el

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 43, impresa 24; [4-marco_teorico.tex:597](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:597). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «el».
- **Contexto del PDF:** «probabilística, R la función de recompensa y γ ∈ [0, 1) el factor de descuento.».
- **Observación literal de Caro:**

  > falta el verbo es

- **Corrección y detalle:** Completar la definición de `\gamma` con «es el factor de descuento». Comprobar que el intervalo del parámetro coincide con el supuesto utilizado en el retorno descontado.

#### C152 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 44, impresa 25; [4-marco_teorico.tex:623](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:623). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.10 representa esta segunda alternativa. A partir del estado observado, la».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C153 — a);

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 44, impresa 25; [4-marco_teorico.tex:623](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:623). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «a);».
- **Contexto del PDF:** «una función de valor de acción Q(s, a); si se utiliza una función de valor de estado V (s), la».
- **Observación literal de Caro:**

  > dejar de usar puntos y comas. Poner más palabras o puntos seguidos.

- **Corrección y detalle:** Sustituir el punto y coma de la comparación entre `Q(s,a)` y `V(s)` por punto seguido o un conector claro. Explicar qué información adicional requiere seleccionar acciones a partir de una función de valor de estado.

#### C154 — Las estimaciones para las acciones disponibles se comparan y se selecciona la alternativa co…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:628](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:628). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Las estimaciones para las acciones disponibles se comparan y se selecciona la alternativa con mayor valor esperado para ejecutarla en el entorno. La exploración puede incorporarse mediante estrategias como la selección ε-greedy [SB18].».
- **Observación literal de Caro:**

  > sacarlo de acá y explicarlo si se requiere en elt exto cuando hablas del la figura.

- **Corrección y detalle:** Sacar del epígrafe la explicación de comparación de valores y exploración ε-greedy. Integrarla en el desarrollo previo de la figura, manteniendo un epígrafe identificatorio y la fuente que corresponda.

#### C155 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:632](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:632). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «de las ecuaciones de Bellman [SB18]. En la notación empleada en la figura 2.10, estas».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C156 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:639](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:639). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «En la ecuación (2.7), la esperanza E promedia las transiciones estocásticas del entorno y».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C157 — E promedia

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:639](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:639). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «E promedia».
- **Contexto del PDF:** «En la ecuación (2.7), la esperanza E promedia las transiciones estocásticas del entorno y».
- **Observación literal de Caro:**

  > en el párrafo anterior también tenes la esperanza y no decis que es la esperanza

- **Corrección y detalle:** Definir la esperanza matemática ya en la primera aparición de `\mathbb{E}_\pi` en las funciones de valor. Aclarar sobre qué resultados se promedia bajo la política y distinguir esa esperanza de la maximización de la ecuación de optimalidad.

#### C158 — En

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:641](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:641). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En».
- **Contexto del PDF:** «En ausencia de un modelo analítico de transición, los métodos de TD aproximan estas».
- **Observación literal de Caro:**

  > setas pasando a otro tipo de métodos .... es que no se entiende este párrafo porque no se cómo engancha con el anterior.

- **Corrección y detalle:** Construir la transición desde las ecuaciones de valor hacia su estimación a partir de experiencia sin modelo conocido. Explicar por qué se introducen diferencias temporales en ese punto y qué problema de cálculo resuelven.

#### C159 — TD

- [ ] **Alta · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:641](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:641). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «TD».
- **Contexto del PDF:** «En ausencia de un modelo analítico de transición, los métodos de TD aproximan estas».
- **Observación literal de Caro:**

  > Esta frase no se cómo engancha con la anterior falta alguna cosa que diga porque empezas a hablar de TD acá ...... además que no está pusto que significa TD \acrfull no se donde etá definido TD para esta altura poner lo que significa... Tampoco se porque salta a Q learning así tirado nomas no conviene escribir como uno de los métodos basados por valor más utilizado es el Q-learning .....

- **Corrección y detalle:** Desarrollar TD cuando se introduce y presentar Q-learning como un método basado en valor que usa ese tipo de actualización. Ordenar definición, propósito y ejemplo antes de mostrar la ecuación; comprobar si `\gls{acr-td}` ya satisface la expansión en el PDF.

#### C160 — bootstrapping.

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 45, impresa 26; [4-marco_teorico.tex:641](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:641). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «bootstrapping.».
- **Contexto del PDF:** «funciones a partir de la experiencia mediante bootstrapping. Un método canónico es Q-».
- **Observación literal de Caro:**

  > ????

- **Corrección y detalle:** Explicar `bootstrapping` inmediatamente: actualizar una estimación mediante otra estimación del valor futuro. El texto actual ya añade esa explicación; verificar que se integra con C158–C159 y no presupone el concepto.

#### C161 — [SB18]:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:641](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:641). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[SB18]:».
- **Contexto del PDF:** «que la tasa de aprendizaje decrezca adecuadamente a lo largo del tiempo [SB18]:».
- **Observación literal de Caro:**

  > me tiene cansada ver esta cita hay muchos libros de RL buscar otro plis

- **Corrección y detalle:** Añadir una fuente específica para Q-learning y sus condiciones de convergencia, si está disponible y resulta pertinente. Reducir la dependencia repetitiva de Sutton y Barto sin sustituirla por referencias que no demuestren lo que se afirma.

#### C162 — off-policy:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:648](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:648). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «off-policy:».
- **Contexto del PDF:** «Q-learning es un algoritmo off-policy: la política que genera los datos de interacción».
- **Observación literal de Caro:**

  > esto significa que la política.....
  > generar menos dos puntos y puntos y comas aflojarle por favor a no ser que sea sumamente necesario. porque es un espacio que corta la lectura no fluye y cuesta leer

- **Corrección y detalle:** Reformular «off-policy:» en una oración continua, por ejemplo «…es off-policy, lo que significa que…». Explicar la diferencia entre política de comportamiento y política objetivo; reducir dos puntos y punto y coma que fragmentan la lectura.

#### C163 — En

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:650](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:650). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En».
- **Contexto del PDF:** «En los métodos basados en política, la regla de decisión se parametriza directamente».
- **Observación literal de Caro:**

  > Por su parte en los ....

- **Corrección y detalle:** Introducir el cambio de familia con una transición explícita, como «Por su parte, en los métodos basados en política…». El lector debe reconocer que ya no se deriva la decisión comparando valores de acción.

#### C164 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:650](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:650). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «acciones posibles [SB18]. La figura 2.11 ilustra este último caso: para el estado observado,».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C165 — caso:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:650](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:650). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «caso:».
- **Contexto del PDF:** «acciones posibles [SB18]. La figura 2.11 ilustra este último caso: para el estado observado,».
- **Observación literal de Caro:**

  > coma

- **Corrección y detalle:** Cambiar los dos puntos posteriores a «caso» por coma o reformular la presentación de la figura con una oración completa. Coordinar con la reubicación de su explicación en C166.

#### C166 — La regla de ejecución puede seleccionar la alternativa de mayor probabilidad o muestrear una…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:655](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:655). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La regla de ejecución puede seleccionar la alternativa de mayor probabilidad o muestrear una acción a partir de dicha distribución [SB18].».
- **Observación literal de Caro:**

  > ponerlo en el texto sobre la figura no acá

- **Corrección y detalle:** Trasladar al cuerpo del texto la regla de ejecución por muestreo o por máxima probabilidad que está dentro del epígrafe. Explicar que la regla depende del modo de ejecución adoptado y dejar un título breve para la figura.

#### C167 — La optimización persigue maximizar el rendimiento esperado J(θ) mediante ascenso

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 46, impresa 27; [4-marco_teorico.tex:659](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:659). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La optimización persigue maximizar el rendimiento esperado J(θ) mediante ascenso».
- **Observación literal de Caro:**

  > párrafo totalmente descolgado es de la figura 2.11 es de RL con política... qué optimización estamos hablando acá....??????????????????

- **Corrección y detalle:** Indicar que `J(\theta)` es el objetivo de la política parametrizada que se acaba de presentar, definirlo antes de hablar de su optimización y enlazar con el ascenso de gradiente. Evitar que parezca otra explicación aislada de la Figura 2.11.

#### C168 — [SB18].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:664](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:664). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[SB18].».
- **Contexto del PDF:** «aquellas fases que conducen a menores demoras en la red [SB18].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la referencia resaltada al final del teorema del gradiente de política junto con C161 y la observación general de variedad bibliográfica. No hay comentario adicional: no se deduce de esta marca que deba borrarse toda cita a Sutton y Barto.

#### C169 — métodos

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:666](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:666). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «métodos».
- **Contexto del PDF:** «Los métodos actor-crítico combinan una política parametrizada con una estimación».
- **Observación literal de Caro:**

  > de qué tipo son? basadois en políticia? entonces reafirmarlo poneidno los métodos basados en política conocidos como ....

- **Corrección y detalle:** Ubicar los métodos actor-crítico en la clasificación que se viene desarrollando: explicar que combinan optimización de una política parametrizada con una estimación de valor. Evitar que aparezcan como otra familia sin relación con las anteriores.

#### C170 — actor-crítico

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:666](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:666). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «actor-crítico».
- **Contexto del PDF:** «Los métodos actor-crítico combinan una política parametrizada con una estimación».
- **Observación literal de Caro:**

  > poner entre paréntesis en inglés como hiciste con el resto de cosas.....(actor-critic)

- **Corrección y detalle:** Introducir el equivalente inglés `actor-critic` junto a «actor-crítico» si se usa esa convención para otros términos técnicos. Mantener una única forma española en el resto del desarrollo y sus enlaces de glosario.

#### C171 — entorno:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:666](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:666). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «entorno:».
- **Contexto del PDF:** «acción. El crítico no controla el entorno: estima, por ejemplo, el valor de estado V ϕ (s) y».
- **Observación literal de Caro:**

  > sacar los dos puntos cambiarlo por "sino que" ir sacando todos los dos puntos rarros y cambiarlo por texto coherente

- **Corrección y detalle:** Reformular «El crítico no controla el entorno: estima…» como una oración ligada, por ejemplo con «sino que estima…». Mantener la distinción funcional entre el actor que elige acciones y el crítico que evalúa.

#### C172 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:673](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:673). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «En la ecuación (2.10), el factor (1 − d t+1 ) anula la contribución del estado siguiente ante».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C173 — ventaja:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:673](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:673). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ventaja:».
- **Contexto del PDF:** «como un estimador de un paso de la ventaja: un valor positivo refleja que la fase ejecutada».
- **Observación literal de Caro:**

  > punto seguido

- **Corrección y detalle:** Cambiar los dos puntos posteriores a «ventaja» por punto seguido. Introducir después la interpretación del signo de `\delta_t`, con un antecedente matemático explícito.

#### C174 — política:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:673](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:673). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «política:».
- **Contexto del PDF:** «de la política:».
- **Observación literal de Caro:**

  > .

- **Corrección y detalle:** Cerrar con punto la explicación que precede a la actualización del actor. Introducir o citar la ecuación en una oración completa en lugar de dejar «de la política:» como apoyo genérico.

#### C175 — regla

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:679](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:679). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «regla».
- **Contexto del PDF:** «En la regla (2.11), α θ > 0 es la tasa de aprendizaje del actor y ∇ θ log π θ (A t | S t ) representa».
- **Observación literal de Caro:**

  > Ecuación y luego decis que se trata de una regla aunque capaz que podes ponerla como ecuación y listo a no ser que sea algo màs que no alcanzo a ver.

- **Corrección y detalle:** Referirse al objeto numerado como «Ecuación», y explicar dentro de la oración que expresa una regla de actualización. Usar la etiqueta existente; evitar dar la impresión de que «regla» es otro objeto distinto.

#### C176 — Estimación

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:679](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:679). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Estimación».
- **Contexto del PDF:** «estimadores de ventaja multipaso como Estimación generalizada de ventaja (Generalized».
- **Observación literal de Caro:**

  > poner cada letra en mayúscula o todas en minúscula queda raro acá esto ....

- **Corrección y detalle:** Normalizar mayúsculas de la expansión de GAE, de acuerdo con la convención de los demás acrónimos. Revisar el campo español de la entrada y el uso de `\Gls` frente a `\gls`; no convertir arbitrariamente todos los sustantivos españoles a mayúsculas.

#### C177 — batches

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:679](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:679). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «batches».
- **Contexto del PDF:** «Advantage Estimation) (GAE) y procesan batches de transiciones en cada actualización,».
- **Observación literal de Caro:**

  > lotes (batches)

- **Corrección y detalle:** Introducir «lotes (batches)» y después usar la forma española o el enlace correspondiente. La fuente actual ya utiliza un término de glosario para el lote; comprobar que la forma visible y el número gramatical son adecuados.

#### C178 — La

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:681](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:681). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La».
- **Contexto del PDF:** «La figura 2.12 sintetiza el flujo operativo entre actor y entorno, así como el circuito de».
- **Observación literal de Caro:**

  > Punto seguido si venis hablando todo de actor-crítico

- **Corrección y detalle:** Integrar la introducción de la Figura 2.12 con el desarrollo de actor-crítico que precede, cuando comparten la misma idea. Evitar que una sola oración de presentación quede como párrafo aislado.

#### C179 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 47, impresa 28; [4-marco_teorico.tex:681](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:681). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.12 sintetiza el flujo operativo entre actor y entorno, así como el circuito de».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C180 — En síntesis,

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:720](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:720). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En síntesis,».
- **Contexto del PDF:** «En síntesis, el estado resume las condiciones de tránsito disponibles para el agente,».
- **Observación literal de Caro:**

  > me parece que en síntesis debería referirse a un resumen d ela sección como claramente no lo es entonces deería decir algo como -> Dado que este trabajo está orientado al problema de mejorar la fluidez del tránsito a partir de semáforos adaptativos podemos decir que el estado.......

- **Corrección y detalle:** Reformular «En síntesis» porque el párrafo aplica los conceptos al control semafórico en lugar de resumir toda la sección. Explicar directamente cómo se interpretan estado, acción y recompensa en el problema estudiado.

### Aprendizaje profundo y redes neuronales

#### C181 — 2.2.3. Aprendizaje profundo y redes neuronales

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:722](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:722). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «2.2.3. Aprendizaje profundo y redes neuronales».
- **Contexto del PDF:** «2.2.3. Aprendizaje profundo y redes neuronales».
- **Observación literal de Caro:**

  > No hay coherencia en esta sección por lo que vas a tener que volver a escribirlo. Primero tenes que definir las cosas y luego dar ejemplos orientados a tu problema. Se debe reescribir.

- **Corrección y detalle:** Reescribir integralmente la sección de aprendizaje profundo con un orden didáctico: neurona artificial, entradas/pesos/sesgo/activación, composición en capas y red, propagación y entrenamiento, y aplicación al control semafórico al final. Coordinar todas las marcas C182–C210 dentro de esa reestructuración para no resolverlas con parches contradictorios.

#### C182 — este desarrollo,

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:724](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:724). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «este desarrollo,».
- **Contexto del PDF:** «Para estructurar este desarrollo, se expone en primer término la unidad neuronal básica».
- **Observación literal de Caro:**

  > ???????????????? descolgadisima frase .... Poner algo como->.En esta sección se introduce el concepto de neurona artificial y su composición.........................

- **Corrección y detalle:** Reemplazar «Para estructurar este desarrollo» por un comienzo que identifique el contenido de la sección. La propuesta de Caro introduce primero la neurona y su composición; evitar anuncios vagos y referencias a un «desarrollo» sin antecedente.

#### C183 — DQN y PPO.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:724](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:724). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «DQN y PPO.».
- **Contexto del PDF:** «DQN y PPO. Cabe destacar que la red neuronal actúa como un aproximador de funciones».
- **Observación literal de Caro:**

  > poner que significa acá abreviaturas sueltas no corresponde..!!!!!

- **Corrección y detalle:** Desarrollar DQN y PPO cuando se anuncian como puntos de llegada de la sección, o posponer las siglas hasta sus apartados. Reutilizar las entradas de acrónimos y no introducir abreviaturas sueltas antes de explicar su función.

#### C184 — El aprendizaje profundo (Deep Learning) se enfoca en el entrenamiento de arquitec- turas con…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:726](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:726). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «El aprendizaje profundo (Deep Learning) se enfoca en el entrenamiento de arquitec- turas con múltiples capas de parámetros ajustables capaces de extraer representaciones jerárquicas y relaciones no lineales directamente de los datos [BB24, GBC16]. En este tra- bajo, esta capacidad se aprovecha para aproximar funciones de valor y políticas de control semafórico donde una formulación tabular resulta impracticable debido a la continuidad y dimensionalidad del estado del tránsito. Aunque la denominación “neuronal” proviene de una analogía simplificada con modelos biológicos iniciales, una red artificial constituye un modelo matemático determinista cuyos parámetros se optimizan a partir de datos y gradientes de pérdida [GBC16].».
- **Observación literal de Caro:**

  > no aporta een este punto introducir primero los conceptos y luego decir paara que los vas a usar en tu problema

- **Corrección y detalle:** Separar la definición general de aprendizaje profundo de su aplicación al tránsito. Llevar el ejemplo de aproximación de valores y políticas al final del desarrollo conceptual; retener solo la explicación biológica o matemática que ayude realmente a comprender la red.

#### C185 — Learning)

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:726](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:726). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Learning)».
- **Contexto del PDF:** «El aprendizaje profundo (Deep Learning) se enfoca en el entrenamiento de arquitec-».
- **Observación literal de Caro:**

  > (Deep Learning, DL)

- **Corrección y detalle:** Presentar la sigla DL junto a `Deep Learning` si se va a usar: «aprendizaje profundo (Deep Learning, DL)». Si no se necesita la sigla, evitar añadir una abreviatura sin uso posterior y mantener la convención decidida para los demás términos.

#### C186 — aprendizaje profundo (Deep

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 48, impresa 29; [4-marco_teorico.tex:726](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:726). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «aprendizaje profundo (Deep».
- **Contexto del PDF:** «El aprendizaje profundo (Deep Learning) se enfoca en el entrenamiento de arquitec-».
- **Observación literal de Caro:**

  > falta linkear con su glosario

- **Corrección y detalle:** Enlazar la primera definición visible de aprendizaje profundo con el glosario, usando una entrada léxica o un acrónimo conforme al criterio de C185. Comprobar que el enlace no duplica el término inglés ya escrito.

#### C187 — [SB18].

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:732](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:732). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[SB18].».
- **Contexto del PDF:** «todos tabulares resultan impracticables [SB18]. La aproximación de funciones resuelve».
- **Observación literal de Caro:**

  > basta de la misma referencia ya te había pasado otras sobre redes neuronales haykin etc por favor no usar siempre lo mismo

- **Corrección y detalle:** Revisar la referencia usada para introducir aproximación neuronal: priorizar una fuente de redes neuronales pertinente, como las ya disponibles, y valorar la sugerencia de Haykin solo después de identificar la obra y edición reales. No añadir una referencia indeterminada.

#### C188 — unidad neuronal

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:734](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:734). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «unidad neuronal».
- **Contexto del PDF:** «La unidad neuronal artificial constituye el bloque computacional básico de estas ar-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Cambiar la expresión «unidad neuronal artificial» por «neurona artificial», como propone C189, y mantener el término de forma consistente entre texto, título de figura, ecuación y glosario.

#### C189 — artificial

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:734](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:734). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «artificial».
- **Contexto del PDF:** «La unidad neuronal artificial constituye el bloque computacional básico de estas ar-».
- **Observación literal de Caro:**

  > neurona artificial

- **Corrección y detalle:** Usar «neurona artificial» como nombre del bloque básico y definirlo antes de hablar de redes multicapa. Coordinar la modificación con C188 y la reestructuración general de C181.

#### C190 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:736](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:736). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.13 ilustra este procesamiento: la transformación afín z = w ⊤ x+b integra las».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C191 — procesamiento:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:736](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:736). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «procesamiento:».
- **Contexto del PDF:** «La figura 2.13 ilustra este procesamiento: la transformación afín z = w ⊤ x+b integra las».
- **Observación literal de Caro:**

  > basta de dos puntos

- **Corrección y detalle:** Reformular la introducción del procesamiento de la neurona para presentar la ecuación sin dos puntos innecesarios. Identificar explícitamente entradas, pesos, sesgo y activación antes de pasar a las consecuencias de la no linealidad.

#### C192 — una red multicapa se reduciría a una transformación afín simple, imposibilitando la captura …

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:736](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:736). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «una red multicapa se reduciría a una transformación afín simple, imposibilitando la captura de patrones de congestión complejos.».
- **Observación literal de Caro:**

  > pero si no explicaste que es una red.... Rehacer toda la subsección es un ida y venida que marea totalmente.. A ver es fácil primero neurona artificial luego definición de red neuronal luego lo instancias en tránsito o qué modela del tránsito no vas mezclando. no se entiende nada lo que queres decir. No esta explicado que es un peso que es un sesgo que es una fucnion de activación o sea...

- **Corrección y detalle:** Definir primero cada componente y después la red multicapa. Mover la afirmación sobre composición afín y patrones de congestión a un lugar donde el lector ya entienda capas y activación; evitar que pesos y sesgo se nombren sin explicar su función y dimensiones.

#### C193 — artificial:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:769](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:769). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «artificial:».
- **Contexto del PDF:** «Figura 2.13: Operaciones de una unidad neuronal artificial: suma ponderada de las entra-».
- **Observación literal de Caro:**

  > basta de dos puntos

- **Corrección y detalle:** Revisar los dos puntos del epígrafe de la neurona y convertir la enumeración en una formulación fluida. Mantener breve el epígrafe y llevar la explicación del cálculo al cuerpo del texto.

#### C194 — puede recibir las métricas de demora de una in- tersección y emitir estimaciones de calidad …

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:773](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:773). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «puede recibir las métricas de demora de una in- tersección y emitir estimaciones de calidad o probabilidades sobre las fases admisibles, orientando la asignación del verde hacia las aproximaciones más críticas.».
- **Observación literal de Caro:**

  > bajarlo si aun no hablaste de una red neuronal bajarlo al final cuando termines de hablar de las redes neuronales como concepto.

- **Corrección y detalle:** Mover el ejemplo semafórico después de completar la definición y el entrenamiento de una red neuronal. Explicar allí qué variables entran y qué produce la salida según el algoritmo, sin atribuir probabilidades a una neurona aislada.

#### C195 — Como ejemplo conceptual,

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:773](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:773). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Como ejemplo conceptual,».
- **Contexto del PDF:** «Como ejemplo conceptual, la red puede recibir las métricas de demora de una in-».
- **Observación literal de Caro:**

  > ejemplo conceptual?¡?¡?? what? En el caso del problema de mejorar el flujo a través de la programación de los semáforos dinámica la red nueronal podría, por ejemplo, recibir las demoras de los vehículos en una intersección..................

- **Corrección y detalle:** Reemplazar «Como ejemplo conceptual» por una introducción concreta al problema de control semafórico. Identificar entradas y salidas del ejemplo y distinguir una ilustración posible de la arquitectura efectivamente implementada.

#### C196 — red

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:773](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:773). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «red».
- **Contexto del PDF:** «Como ejemplo conceptual, la red puede recibir las métricas de demora de una in-».
- **Observación literal de Caro:**

  > que red ?????? hablas de red sin decir si es de tránsito  o neuronal. Eso pasa un monton a ver decis red en este trabajo tenes dos términos redes uno de red de tránsito y otro de red neuronal entonces no podes poner red tirado solo tenes que decir qué red

- **Corrección y detalle:** Especificar «red neuronal» en este ejemplo y auditar los usos próximos de «red». Distinguirla siempre de la red vial cuando el contexto admite ambas interpretaciones.

#### C197 — En una red multicapa, la operación para una unidad u dentro de la capa k se formaliza median…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 49, impresa 30; [4-marco_teorico.tex:775](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:775). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En una red multicapa, la operación para una unidad u dentro de la capa k se formaliza mediante la ecuación (2.12) [BB24, GBC16]:».
- **Observación literal de Caro:**

  > esto va arriba como vas a hablar de la red neuronal sin definirla antes!

- **Corrección y detalle:** Mover la definición formal de la neurona/capa antes de los ejemplos que dependen de ella y situarla donde se introduce la arquitectura. Mantener la etiqueta existente y explicar los índices de capa y unidad junto a la ecuación.

#### C198 — redes

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 50, impresa 31; [4-marco_teorico.tex:789](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:789). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «redes».
- **Contexto del PDF:** «Las redes feedforward encadenan estas transformaciones en capas acíclicas sucesivas».
- **Observación literal de Caro:**

  > que redes las redes neuronales

- **Corrección y detalle:** Escribir «redes neuronales feedforward» al introducir el encadenamiento de capas. Definir la dirección de propagación y evitar que «redes» pueda leerse como infraestructura de tránsito.

#### C199 — estas transformaciones

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 50, impresa 31; [4-marco_teorico.tex:789](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:789). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «estas transformaciones».
- **Contexto del PDF:** «Las redes feedforward encadenan estas transformaciones en capas acíclicas sucesivas».
- **Observación literal de Caro:**

  > qué transformaciones?

- **Corrección y detalle:** Reemplazar «estas transformaciones» por las operaciones concretas que se componen: transformación afín y función de activación de cada capa. El lector debe poder seguir el recorrido desde las entradas hasta las salidas sin reconstruir el antecedente.

#### C200 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 50, impresa 31; [4-marco_teorico.tex:799](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:799). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.14 esquematiza esta composición con dos capas ocultas conectadas en».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C201 — ancha, puede aproximar una función continua sobre un dominio compacto con una preci- sión ar…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:854](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:854). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ancha, puede aproximar una función continua sobre un dominio compacto con una preci- sión arbitraria. El teorema no proporciona por sí mismo un procedimiento para encontrar los parámetros, no garantiza un entrenamiento eficiente, una buena generalización ni un buen desempeño práctico sobre datos no observados. La profundidad puede ofrecer repre- sentaciones jerárquicas y una mayor eficiencia expresiva para ciertas familias de funciones, pero agregar capas o neuronas no garantiza por sí solo un menor error de prueba».
- **Observación literal de Caro:**

  > y que relacion tiene con lo que vos estas trabajando?¡?¡? o este texto está acá tirado nomas si no aporta sacalo

- **Corrección y detalle:** Justificar qué aporta el teorema de aproximación universal al razonamiento del trabajo o retirarlo si queda como una digresión. Si se conserva, mantener sus límites: existencia de aproximación no demuestra entrenamiento eficiente, generalización ni mejora del control semafórico.

#### C202 — la red

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:858](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:858). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «la red».
- **Contexto del PDF:** «Durante el entrenamiento, la red procesa las observaciones mediante propagación hacia».
- **Observación literal de Caro:**

  > qué red

- **Corrección y detalle:** Precisar «red neuronal» al comenzar la explicación del entrenamiento. Separar el cálculo de sus salidas del ajuste de sus parámetros y no depender de un «la red» ambiguo.

#### C203 — objetivo

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:858](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:858). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «objetivo».
- **Contexto del PDF:** «adelante y contrasta su respuesta frente a un objetivo mediante una función de pérdida».
- **Observación literal de Caro:**

  > objetivo a optimizar (mejorar)

- **Corrección y detalle:** Aclarar qué es el objetivo a optimizar y cómo la función de pérdida cuantifica la discrepancia. Distinguir el blanco de entrenamiento, la función de pérdida y el objetivo de control para que «objetivo» no cambie de significado sin aviso.

#### C204 — minibatches

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:867](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:867). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «minibatches».
- **Contexto del PDF:** «se ejecuta habitualmente sobre subconjuntos estocásticos denominados minibatches y se».
- **Observación literal de Caro:**

  > minilotes (........)

- **Corrección y detalle:** Introducir «minilotes (minibatches)» y utilizar luego una forma consistente. Explicar que son subconjuntos de muestras utilizados para estimar el gradiente en una actualización.

#### C205 — objetivo

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:869](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:869). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «objetivo».
- **Contexto del PDF:** «salida con una etiqueta externa fija—, en RL el objetivo se deriva de las recompensas».
- **Observación literal de Caro:**

  > el objetivo a optimizar

- **Corrección y detalle:** Precisar a qué objetivo se refiere el párrafo sobre RL: blancos que se construyen con recompensas y estimaciones futuras, y objetivo de retorno que orienta la política. Evitar sugerir que todos los objetivos de RL son etiquetas externas fijas o que todos cambian de la misma manera.

#### C206 — simulador,

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:869](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:869). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «simulador,».
- **Contexto del PDF:** «y transiciones producidas por la interacción con el simulador, y cambia a medida que la».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar la coma tachada después de «simulador» para enlazar correctamente «y cambia…», o dividir la oración si se distinguen dos ideas. Revisar el sujeto de «cambia» después de aclarar el objetivo en C205.

#### C207 — comportamiento.

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:869](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:869). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «comportamiento.».
- **Contexto del PDF:** «política mejora su comportamiento.».
- **Observación literal de Caro:**

  > luego de todo esto tendrías que poner como párrafo aparte todo lo de semáforos que quedó colgado en el medio de la sección.....

- **Corrección y detalle:** Reunir al final de la explicación general un párrafo propio sobre el uso de redes neuronales en los semáforos. Mover allí los ejemplos dispersos de entradas de espera/colas, salidas Q o de política y relación con recompensas.

### DRL, DQN y PPO

#### C208 — red;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:873](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:873). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «red;».
- **Contexto del PDF:** «alimentar la red; sus salidas pueden representar valores de acción o parámetros de una».
- **Observación literal de Caro:**

  > basta de ;

- **Corrección y detalle:** Cambiar el punto y coma después de «red» por punto seguido y mantener un sujeto claro para la oración sobre salidas. Coordinar con la nota adhesiva C209, que señala ese mismo corte.

#### C209 — Puntuación junto a «alimentar la red; sus salidas…»

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:873](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:873). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Text):** Puntuación junto a «alimentar la red; sus salidas…».
- **Observación literal de Caro:**

  > poner .

- **Corrección y detalle:** Aplicar el punto solicitado en la nota adhesiva situada junto a «alimentar la red; sus salidas…» en la introducción a DRL. Es otra marca sobre el mismo corte de C208, no una observación nueva sobre la subsección de optimización.

#### C210 — política;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 51, impresa 32; [4-marco_teorico.tex:873](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:873). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «política;».
- **Contexto del PDF:** «política; y las recompensas asociadas con demoras, detenciones y colas orientan la función».
- **Observación literal de Caro:**

  > basta de ; reescribir

- **Corrección y detalle:** Reformular el punto y coma posterior a «política» para completar la explicación del recorrido observación → red neuronal → salidas → aprendizaje. Puede convenir separar el flujo de ejecución del cálculo de la pérdida.

#### C211 — [SB18].

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 52, impresa 33; [4-marco_teorico.tex:883](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:883). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[SB18].».
- **Contexto del PDF:** «inestabilidad [SB18].».
- **Observación literal de Caro:**

  > cambiar cita por otra hay miles de ejemplos en revistas de utilización de otras de mecanismos podes buscar en tus mismas referencias pero ese libro pareciera que es lo único que has leído

- **Corrección y detalle:** Añadir o sustituir con una referencia pertinente sobre estabilización o aplicaciones de aprendizaje profundo la cita resaltada de Sutton y Barto. El pasaje original de inestabilidad fue reorganizado; localizar las afirmaciones conservadas antes de cambiar su fuente.

#### C212 — Deep Q-Network (DQN):

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 52, impresa 33; [4-marco_teorico.tex:885](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:885). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Deep Q-Network (DQN):».
- **Contexto del PDF:** «Deep Q-Network (DQN): aproximación neuronal de valores de acción».
- **Observación literal de Caro:**

  > glosario

- **Corrección y detalle:** Enlazar/desarrollar DQN en el título o en su primera definición mediante la entrada existente. Si se usa una macro en el título, proporcionar texto opcional plano para los marcadores PDF.

#### C213 — ejecutar;

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:895](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:895). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ejecutar;».
- **Contexto del PDF:** «y una regla ϵ exp -greedy selecciona la fase a ejecutar; la transición resultante se almacena».
- **Observación literal de Caro:**

  > y

- **Corrección y detalle:** Reemplazar «ejecutar; la transición…» por una coordinación con «y» u otra oración fluida. Mantener claro que primero se selecciona y ejecuta la acción y después se almacena su transición.

#### C214 — Párrafo de selección de acciones y almacenamiento DQN

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:895](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:895). Pasaje actual o bloque al que pertenece la marca.
- **Anclaje (Text):** Párrafo de selección de acciones y almacenamiento DQN.
- **Observación literal de Caro:**

  > basta de ;

- **Corrección y detalle:** Revisar el punto y coma en el párrafo operativo de DQN señalado por esta nota adhesiva. La nota está junto a la línea inicial del párrafo de selección y almacenamiento; resolverla junto con C213, verificando la puntuación completa.

#### C215 — (figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:895](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:895). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(figura».
- **Contexto del PDF:** «parámetros θ − se sincronizan solo de forma periódica (figura 2.15).».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C216 — Elaboración propia a partir del algoritmo descrito por Mnih et al. [MKS + 15].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:937](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:937). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Elaboración propia a partir del algoritmo descrito por Mnih et al. [MKS + 15].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar «Elaboración propia a partir del algoritmo descrito…» del epígrafe y mantener una atribución compacta a Mnih et al. cuando corresponde. No convertir la supresión de una fórmula editorial en la pérdida de procedencia del algoritmo.

#### C217 — (2.15):

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:941](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:941). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(2.15):».
- **Contexto del PDF:** «figura 2.15, es la de la ecuación (2.15):».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Cambiar la introducción de la pérdida DQN para citar la ecuación dentro de una oración completa y retirar los dos puntos tachados. Coordinar con C219 y conservar la etiqueta actual.

#### C218 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:941](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:941). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «figura 2.15, es la de la ecuación (2.15):».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C219 — es la de la

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:941](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:941). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «es la de la».
- **Contexto del PDF:** «figura 2.15, es la de la ecuación (2.15):».
- **Observación literal de Caro:**

  > se define en la Ecuación (2.15).

- **Corrección y detalle:** Usar «se define en la Ecuación…» en vez de «es la de la…». Identificar con nombre la función de pérdida antes de mostrar su expresión matemática.

#### C220 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:941](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:941). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «figura 2.15, es la de la ecuación (2.15):».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C221 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:950](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:950). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «En la ecuación (2.15), la esperanza se evalúa empíricamente promediando sobre un mini-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C222 — pseudocódigos:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 53, impresa 34; [4-marco_teorico.tex:952](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:952). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «pseudocódigos:».
- **Contexto del PDF:** «Los cuatro bloques numerados como algoritmos en este capítulo son pseudocódigos:».
- **Observación literal de Caro:**

  > ,

- **Corrección y detalle:** Reemplazar los dos puntos después de «pseudocódigos» por una oración con coma u otra construcción continua. Explicar su función como descripción abstracta de operaciones, sin convertir el aviso en una digresión repetida.

#### C223 — algoritmo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 54, impresa 35; [4-marco_teorico.tex:954](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:954). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «algoritmo».
- **Contexto del PDF:** «muestreados del replay buffer . El algoritmo 1 especifica este procedimiento:».
- **Observación literal de Caro:**

  > A con mayúscula

- **Corrección y detalle:** Usar «Algoritmo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C224 — procedimiento:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 54, impresa 35; [4-marco_teorico.tex:954](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:954). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «procedimiento:».
- **Contexto del PDF:** «muestreados del replay buffer . El algoritmo 1 especifica este procedimiento:».
- **Observación literal de Caro:**

  > .

- **Corrección y detalle:** Cerrar con punto la oración que introduce el procedimiento DQN en el Algoritmo 1. Mantener el algoritmo citado antes de su aparición y su relación con el texto operativo.

#### C225 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 55, impresa 36; [4-marco_teorico.tex:985](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:985). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «exploración) se desarrolla en el capítulo 3.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C226 — MDP,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 55, impresa 36; [4-marco_teorico.tex:988](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:988). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «MDP,».
- **Contexto del PDF:** «mediante una red neuronal π(a|s; θ) [ACS24]. Bajo la formulación MDP, en un problema».
- **Observación literal de Caro:**

  > glosario

- **Corrección y detalle:** Usar el enlace de glosario o acrónimo para MDP en la formulación de la red de política. Comprobar si se requiere desarrollar la sigla o solo enlazar su uso visible por estar ya definida cerca.

#### C227 — Dec-POMDP.

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 55, impresa 36; [4-marco_teorico.tex:993](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:993). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Dec-POMDP.».
- **Contexto del PDF:** «te mediante Dec-POMDP. La acción puede muestrearse de esa distribución durante el».
- **Observación literal de Caro:**

  > \acrfull

- **Corrección y detalle:** Desarrollar Dec-POMDP cuando se introduce la formulación parcialmente observable. Distinguir el formalismo teórico de recompensa compartida de la implementación con señales individuales; la expansión de la sigla no debe ocultar esa diferencia.

#### C228 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 55, impresa 36; [4-marco_teorico.tex:995](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:995). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.16 muestra este recorrido para un controlador semafórico. A diferencia».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C229 — log-probabilidad

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 55, impresa 36; [4-marco_teorico.tex:995](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:995). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «log-probabilidad».
- **Contexto del PDF:** «la log-probabilidad de la acción observada.».
- **Observación literal de Caro:**

  > probabilidad logarítmica? escribirlo completo no hace falta achicar nada

- **Corrección y detalle:** Reemplazar «log-probabilidad» por «logaritmo de la probabilidad» o una expresión española completa y consistente, también en el epígrafe de la figura. Mantener el significado de `\log\pi` y evitar invertirlo como si fuera otra distribución.

#### C230 — [SB18]:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 56, impresa 37; [4-marco_teorico.tex:1032](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1032). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[SB18]:».
- **Contexto del PDF:** «basal del estado [SB18]: .».
- **Observación literal de Caro:**

  > como se observa en la Ecuación (2.17).

- **Corrección y detalle:** Introducir la definición de ventaja con una remisión explícita a la ecuación correspondiente, como pide Caro para la Ecuación (2.17) del PDF comentado. La numeración actual puede variar: usar la etiqueta `eq:funcion_ventaja`, no copiar el número del PDF antiguo.

#### C231 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 56, impresa 37; [4-marco_teorico.tex:1051](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1051). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «Â t es la ventaja estimada mediante GAE. Como esquematiza la figura 2.16, la dirección».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C232 — paso:

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 56, impresa 37; [4-marco_teorico.tex:1055](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1055). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «paso:».
- **Contexto del PDF:** «magnitud de la tasa de paso: una actualización excesiva en el espacio de parámetros».
- **Observación literal de Caro:**

  > .

- **Corrección y detalle:** Reescribir la introducción a PPO para explicar que se controla el tamaño de la actualización y cerrar la oración con punto. El pasaje original sobre «tasa de paso» ya cambió; comprobar el nuevo enlace con TRPO antes de aplicar una sustitución literal.

#### C233 — (Optimización de política por región de confianza (Trust Region Policy Optimization) (TRPO)

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1057](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1057). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(Optimización de política por región de confianza (Trust Region Policy Optimization) (TRPO)».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar la inserción parentética recargada de TRPO y presentarlo como sujeto o complemento explícito de una oración. Mantener su nombre completo, la sigla y la atribución a los autores sin varios paréntesis anidados.

#### C234 — 15])

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1057](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1057). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «15])».
- **Contexto del PDF:** «(Trust Region Policy Optimization) (TRPO) [SLA + 15]) formularon métodos de región de».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Resolver el cierre tachado de la cita y los paréntesis de TRPO como parte de C233. La extracción solo recoge un fragmento del marcador bibliográfico; no corresponde tratar «15])» como texto independiente que deba buscarse literalmente en LaTeX.

#### C235 — formularon métodos de región de confianza. En el análisis teórico de TRPO, bajo los supuesto…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1057](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1057). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «formularon métodos de región de confianza. En el análisis teórico de TRPO, bajo los supuestos del modelo y una actualiza- ción que respete la región de confianza basada en la divergencia de Kullback–Leibler (KL, una medida probabilística que cuantifica la discrepancia estadística entre la nueva política y la previa [GBC16, SLA + 15]), la maximización exacta de la cota sustituta produce una política con retorno esperado no decreciente:».
- **Observación literal de Caro:**

  > esta muy cortado este parrafo volver a escribirlo más fluido. introduci bien los términos porque los usas abajo.. Adem{as sacale los dos puntos al final y cita la ecuación en la oración.

- **Corrección y detalle:** Reescribir el párrafo de región de confianza en un orden claro: propósito, definición de TRPO/KL, supuestos y garantía. Citar la ecuación de mejora en la oración y reducir incisos y dos puntos, conservando la diferencia entre garantía teórica y aproximación práctica.

#### C236 — confianza.

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1057](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1057). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «confianza.».
- **Contexto del PDF:** «confianza. En el análisis teórico de TRPO, bajo los supuestos del modelo y una actualiza-».
- **Observación literal de Caro:**

  > acá se pone la cita

- **Corrección y detalle:** Colocar la referencia de los métodos de región de confianza al terminar su presentación, antes del análisis de la garantía. Evitar que una cita incrustada en una explicación de KL vuelva difícil reconocer qué fuente respalda cada afirmación.

#### C237 — práctico

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1062](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1062). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «práctico».
- **Contexto del PDF:** «El algoritmo práctico de TRPO aproxima este procedimiento mediante ventajas estima-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar «práctico» si solo vuelve vaga la distinción, o explicitar qué aproximación implementable se describe. Mantener la separación entre resolución exacta del planteo teórico y uso de estimaciones y optimización numérica.

#### C238 — aproxima este procedimiento

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1062](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1062). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «aproxima este procedimiento».
- **Contexto del PDF:** «El algoritmo práctico de TRPO aproxima este procedimiento mediante ventajas estima-».
- **Observación literal de Caro:**

  > aproxima la región de confianza? si es así pone eso no pongas palabras vagas que no sabemos de donde salen...

- **Corrección y detalle:** Reemplazar «aproxima este procedimiento» por la operación concreta que se aproxima. Revisar si se trata del problema restringido de TRPO, su divergencia promedio o su optimización; no adoptar «aproxima la región» sin comprobar que sea técnicamente preciso.

#### C239 — Definiendo

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1064](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1064). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Definiendo».
- **Contexto del PDF:** «Definiendo la razón de probabilidad entre la política actual y la previa:».
- **Observación literal de Caro:**

  > punto seguido a la oración anterio porque supongo que estás definiendo lo de arriba y luego poner la cita de la ecauación sacar los dos puntos.

- **Corrección y detalle:** Integrar «Definiendo la razón…» con la oración anterior o convertirlo en «La razón… se define en la Ecuación…». Evitar una frase subordinada sola y conservar explícitas las políticas actual y recolectora del lote.

#### C240 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1074](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1074). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «En la ecuación (2.22), ϵ clip > 0 delimita el margen de recorte permitido para la razón».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C241 — práctica,

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 57, impresa 38; [4-marco_teorico.tex:1076](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1076). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «práctica,».
- **Contexto del PDF:** «En la arquitectura actor-crítico práctica, este objetivo de política se integra de forma».
- **Observación literal de Caro:**

  > ?

- **Corrección y detalle:** Precisar qué significa «arquitectura actor-crítico práctica»: qué términos combina el objetivo y para qué sirve cada uno. Si «práctica» no aporta una distinción con la formulación previa, eliminarlo.

#### C242 — entrenamiento:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 58, impresa 39; [4-marco_teorico.tex:1083](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1083). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «entrenamiento:».
- **Contexto del PDF:** «distribucional. El algoritmo 2 describe este ciclo de entrenamiento:».
- **Observación literal de Caro:**

  > .

- **Corrección y detalle:** Cerrar con punto la presentación del ciclo de entrenamiento PPO. La ecuación del objetivo y el algoritmo deben quedar enlazados por su función, sin recurrir a dos puntos como transición genérica.

#### C243 — algoritmo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 58, impresa 39; [4-marco_teorico.tex:1083](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1083). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «algoritmo».
- **Contexto del PDF:** «distribucional. El algoritmo 2 describe este ciclo de entrenamiento:».
- **Observación literal de Caro:**

  > A

- **Corrección y detalle:** Usar «Algoritmo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

### MARL y formalismos

#### C244 — (sección 3.5.3).

- [ ] **Alta · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 59, impresa 40; [4-marco_teorico.tex:1114](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1114). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «(sección 3.5.3).».
- **Contexto del PDF:** «junto con el estado de sus nodos inmediatamente adyacentes (sección 3.5.3).».
- **Observación literal de Caro:**

  > No entiendo que pongas una referenica a una sección más adelante sin decir nada al respecto. Tndría que decir algo como Esto se verá en la Sección 3.5.3 para la metodología adoptada en este trabajo. O algo así !

- **Corrección y detalle:** Sustituir la remisión parentética aislada a metodología por una oración que indique qué se desarrolla allí y por qué. El texto actual ya cambió y remite a recompensas locales/vecinales; conservar la distinción entre finalidad cooperativa y retorno individual.

#### C245 — (sección

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 59, impresa 40; [4-marco_teorico.tex:1114](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1114). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(sección».
- **Contexto del PDF:** «junto con el estado de sus nodos inmediatamente adyacentes (sección 3.5.3).».
- **Observación literal de Caro:**

  > S mayúsucula

- **Corrección y detalle:** Usar «Sección» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C246 — [ACS24].

- [ ] **Conservar · Conservar; sin corrección solicitada.**
- **Ubicación:** PDF 59, impresa 40; [4-marco_teorico.tex:1118](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1118). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «[ACS24].».
- **Contexto del PDF:** «neo por Albrecht et al. [ACS24].».
- **Observación literal de Caro:**

  > Esta oración está bárbara!!!

- **Corrección y detalle:** Conservar la oración que vincula los juegos estocásticos de Shapley con su tratamiento contemporáneo por Albrecht et al. Caro la valora positivamente; usar su claridad y atribución como referencia al reescribir pasajes vecinos.
- **Cierre:** no requiere reescritura por esta marca; comprobar que las correcciones vecinas preserven la cualidad valorada.

#### C247 — tupla:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 60, impresa 41; [4-marco_teorico.tex:1134](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1134). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «tupla:».
- **Contexto del PDF:** «definido por la tupla:».
- **Observación literal de Caro:**

  > que se muestra en la Ecuación (2.26).

- **Corrección y detalle:** Introducir la tupla Dec-POMDP mediante una remisión integrada a su ecuación, en lugar de acabar en «tupla:». Reutilizar `eq:dec_pomdp` y conservar la definición de todos los símbolos próximos a la expresión.

#### C248 — [AOS20].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 60, impresa 41; [4-marco_teorico.tex:1139](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1139). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[AOS20].».
- **Contexto del PDF:** «[AOS20]. El estado global s es una variable del modelo que no tiene por qué ser accesible a».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la cita tachada al final de la definición de observaciones del Dec-POMDP. Mantener la fuente del formalismo, pero colocarla donde cubra de manera clara la definición sin repetición innecesaria.

#### C249 — (figura 2.17).

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 60, impresa 41; [4-marco_teorico.tex:1139](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1139). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(figura 2.17).».
- **Contexto del PDF:** «con s (figura 2.17).».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar la remisión parentética repetida a la Figura 2.17 si el párrafo siguiente ya la presenta y explica. Mantener una única introducción bien enlazada con el formalismo y con las observaciones locales.

#### C250 — La

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 60, impresa 41; [4-marco_teorico.tex:1141](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1141). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La».
- **Contexto del PDF:** «La figura 2.17 esquematiza este acoplamiento: cada agente procesa su observación local».
- **Observación literal de Caro:**

  > Parráfo seguido al anterior no bajar de línea.

- **Corrección y detalle:** Integrar el párrafo de introducción de la Figura 2.17 con la explicación previa cuando forma una misma idea. Evitar un salto de párrafo que deje aislada la relación entre observaciones, acciones y estado global.

#### C251 — acoplamiento:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 60, impresa 41; [4-marco_teorico.tex:1141](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1141). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «acoplamiento:».
- **Contexto del PDF:** «La figura 2.17 esquematiza este acoplamiento: cada agente procesa su observación local».
- **Observación literal de Caro:**

  > .

- **Corrección y detalle:** Cambiar los dos puntos posteriores a «acoplamiento» por punto seguido o una oración relativa que explique el flujo multiagente. Mantener la correspondencia entre texto, agentes del dibujo y recompensas individuales.

#### C252 — En

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 61, impresa 42; [4-marco_teorico.tex:1221](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1221). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En».
- **Contexto del PDF:** «En juegos competitivos o de suma cero como Piedra, Papel o Tijera, el aprendizaje».
- **Observación literal de Caro:**

  > ponelo seguido al atnterio para no tener líneas huérfanas

- **Corrección y detalle:** Evaluar la unión del ejemplo Piedra, Papel o Tijera con la explicación previa de no estacionariedad. Evitar líneas aisladas y revisar el PDF tras reescribir; la unión debe mantener una idea de párrafo reconocible.

#### C253 — (Win or Learn Fast Policy Hill-Climbing) (WoLF-PHC) (Win or Learn Fast Policy Hill-Climbing)

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 61, impresa 42; [4-marco_teorico.tex:1221](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1221). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(Win or Learn Fast Policy Hill-Climbing) (WoLF-PHC) (Win or Learn Fast Policy Hill-Climbing)».
- **Observación literal de Caro:**

  > queda super raro

- **Corrección y detalle:** Eliminar la expansión repetida de WoLF-PHC: mostrar una sola vez el nombre desarrollado y su sigla, usando la macro existente. La fuente actual ya usa `\gls{acr-wolf-phc}`; verificar el resultado renderizado antes de marcarlo cerrado.
- **Comprobación adicional:** revisar las macros de expansión en [main.tex:189](/home/juanm4/Documentos/tesina/main.tex:189) y las entradas de [glosario_abreviaturas.tex](/home/juanm4/Documentos/tesina/glosario_abreviaturas.tex).

#### C254 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 61, impresa 42; [4-marco_teorico.tex:1221](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1221). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «figura 2.18. En el control semafórico, la no estacionariedad se manifiesta cuando un».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C255 — [ACS24].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 62, impresa 43; [4-marco_teorico.tex:1225](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1225). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[ACS24].».
- **Contexto del PDF:** «local sobre el desempeño del sistema resulta complejo [ACS24]. Una acción local».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Reubicar o reducir la cita tachada en la definición de asignación de crédito, manteniendo su respaldo. Coordinar con la explicación posterior de recompensas vecinales y evitar presentar esas recompensas como identificación causal de contribuciones individuales.

#### C256 — El diseño de recompensas individuales compuestas (sección 3.5.3) aborda este desafío aisland…

- [ ] **Alta · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 62, impresa 43; [4-marco_teorico.tex:1225](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1225). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «El diseño de recompensas individuales compuestas (sección 3.5.3) aborda este desafío aislando la contribución de la intersección y su vecindario inmediato.».
- **Observación literal de Caro:**

  > la misma observación sobre seccioones de metodología que te hice antes

- **Corrección y detalle:** Explicar en prosa qué cuestión de metodología se anticipa al remitir al diseño de recompensas. El texto actual ya distingue mezcla local/vecinal y reconoce que no identifica contribuciones causales; conservar esa precisión aunque se acorte o mueva la referencia.

#### C257 — Adaptado de [BV02, ACS24].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 62, impresa 43; [4-marco_teorico.tex:1231](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1231). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Adaptado de [BV02, ACS24].».
- **Contexto del PDF:** «durante el entrenamiento y los marcadores centrales destacan la política convergida en el equilibrio de Nash (π ∗ (a) = 1/3 para cada acción). Adaptado de [BV02, ACS24].».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la eliminación de «Adaptado de…» en el epígrafe de WoLF-PHC: abreviar o trasladar la atribución, conservando la procedencia de una figura adaptada. No borrar las fuentes de Bowling y Veloso y del libro MARL sin reemplazar su atribución donde corresponda.

#### C258 — (MAPPO y HAPPO),

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 63, impresa 44; [4-marco_teorico.tex:1246](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1246). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(MAPPO y HAPPO),».
- **Contexto del PDF:** «do (MAPPO y HAPPO), esta investigación establece dos líneas de base de aprendizaje».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Evaluar la supresión de la enumeración parentética de MAPPO y HAPPO al presentar las bases independientes. Conservar la comparación entre paradigmas y evitar volver a enumerar siglas ya presentadas sin necesidad.

#### C259 — [TMK + 17].

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 63, impresa 44; [4-marco_teorico.tex:1249](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1249). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «[TMK + 17].».
- **Contexto del PDF:** «tersección mantiene su propia red Q i (o i , a i ) [TMK + 17]. Al operar off-policy con un».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar la referencia tachada en la descripción de IDQN. Mantener una fuente adecuada para el aprendizaje Q independiente y distinguir la definición general del método de una decisión de implementación propia.

#### C260 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 63, impresa 44; [4-marco_teorico.tex:1253](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1253). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «La figura 2.19 resume esta partición operativa entre ambas etapas.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

### MAPPO y HAPPO

#### C261 — agentes:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 64, impresa 45; [4-marco_teorico.tex:1314](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1314). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «agentes:».
- **Contexto del PDF:** «PPO sobre los n agentes:».
- **Observación literal de Caro:**

  > aflojarle a los dos puntos

- **Corrección y detalle:** Reformular la introducción del objetivo MAPPO sin los dos puntos tras «agentes». Integrar la ecuación en una oración que explique qué objetivo local se optimiza y qué información aporta el crítico.

#### C262 — algoritmo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 65, impresa 46; [4-marco_teorico.tex:1334](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1334). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «algoritmo».
- **Contexto del PDF:** «El algoritmo 3 especifica el ciclo computacional de MAPPO bajo el paradigma CTDE.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Algoritmo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C263 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 66, impresa 47; [4-marco_teorico.tex:1360](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1360). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «las redes se detallan en el capítulo 3.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C264 — (HAPPO)

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 67, impresa 48; [4-marco_teorico.tex:1364](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1364). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(HAPPO)».
- **Contexto del PDF:** «(HAPPO)».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Eliminar el «(HAPPO)» redundante en la presentación de la familia heterogénea cuando repite una sigla ya utilizada. Revisar conjuntamente C265 para desarrollar el nombre una vez de manera legible.

#### C265 — HAPPO

- [ ] **Media · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 67, impresa 48; [4-marco_teorico.tex:1368](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1368). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «HAPPO».
- **Contexto del PDF:** «Trust Region Policy Optimization) (HATRPO) y HAPPO emplean una actualización se-».
- **Observación literal de Caro:**

  > \acrfull

- **Corrección y detalle:** Desarrollar HAPPO en la introducción de los algoritmos heterogéneos, mediante `\acrfull` u otra macro coherente. Evitar la repetición de HAPPO al corregir el paréntesis señalado en C264.

#### C266 — debe interpre- tarse

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 67, impresa 48; [4-marco_teorico.tex:1368](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1368). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «debe interpre- tarse».
- **Contexto del PDF:** «práctica HAPPO sustituye la restricción KL por un objetivo recortado y debe interpre- tarse como una aproximación [KCW + 22, ZKF + 24].».
- **Observación literal de Caro:**

  > se interpreta

- **Corrección y detalle:** Cambiar «debe interpretarse» por «se interpreta», manteniendo claro que el recorte de HAPPO se presenta como aproximación y no como herencia automática de garantías de HATRPO.

#### C267 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 68, impresa 49; [4-marco_teorico.tex:1392](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1392). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «En la ecuación (2.32), Q π i 1:m (s, a i 1:m−1 , a i m ) evalúa el retorno esperado fijando las acciones».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C268 — extremo

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 68, impresa 49; [4-marco_teorico.tex:1394](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1394). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «extremo».
- **Contexto del PDF:** «extremo que Chu et al. respaldan con evidencia empírica en redes extensas [CWCL19], y».
- **Observación literal de Caro:**

  > ???????????????? observación

- **Corrección y detalle:** Reemplazar «extremo que Chu et al. respaldan…» por una oración directa, como «Chu et al. aportan evidencia…». Aclarar que la evidencia se refiere a dificultades de asignación de crédito con recompensas globales, y separar ese hecho de las decisiones propias sobre recompensas locales o vecinales.

#### C269 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 68, impresa 49; [4-marco_teorico.tex:1396](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1396). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «Bajo retornos desacoplados, la identidad aditiva de la ecuación (2.31) no se traduce en».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C270 — (a diferencia de las condiciones de factoriza- ción IGM de arquitecturas como Redes de desco…

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 68, impresa 49; [4-marco_teorico.tex:1398](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1398). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «(a diferencia de las condiciones de factoriza- ción IGM de arquitecturas como Redes de descomposición de valor (Value-Decomposition Networks) (VDN) [SLG + 18] o Red de mezcla de valores Q (Q-Mixing Network ) (QMIX) [RSDW + 18]).».
- **Observación literal de Caro:**

  > no poner entre parentesis armar una oración coherente se pierde la lectura con tanta cita y texto y parentesis

- **Corrección y detalle:** Sacar del paréntesis la comparación con factorización IGM, VDN y QMIX. Presentar el significado de esos términos antes de utilizarlos y distribuir las citas en oraciones legibles, conservando el alcance exacto de la identidad y sus supuestos cooperativos.

#### C271 — ecuación

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 70, impresa 51; [4-marco_teorico.tex:1442](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1442). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «ecuación».
- **Contexto del PDF:** «recortado CLIP de primer orden de la ecuación (2.34).».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Ecuación» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C272 — [KCW + 22, ZKF + 24].

- [ ] **Media · Pasaje modificado o retirado; revisar correspondencia.**
- **Ubicación:** PDF 70, impresa 51; [4-marco_teorico.tex:1444](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1444). Correspondencia temática: el pasaje original fue modificado o retirado.
- **Texto marcado (Highlight):** «[KCW + 22, ZKF + 24].».
- **Contexto del PDF:** «[KCW + 22, ZKF + 24]. Además, en redes urbanas con señales de recompensa local-vecinales,».
- **Observación literal de Caro:**

  > juntar con las referencias que vienen más abajo para que no queden tantas referencias sueltas

- **Corrección y detalle:** Reunir las citas de las garantías de algoritmos heterogéneos con las referencias posteriores que sostienen el mismo argumento. La redacción actual fue reorganizada; determinar qué afirmación respalda cada fuente y no acumular referencias de garantías diferentes como si fueran intercambiables.

#### C273 — figura

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 70, impresa 51; [4-marco_teorico.tex:1444](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1444). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «figura».
- **Contexto del PDF:** «concurrentes [WZK + 23, ZKF + 24]. La figura 2.20 resume este esquema de propagación».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Figura» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C274 — algoritmo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 70, impresa 51; [4-marco_teorico.tex:1487](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1487). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «algoritmo».
- **Contexto del PDF:** «El algoritmo 4 presenta la secuencia completa de optimización de HAPPO.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Algoritmo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C275 — (sección 3.5.3),

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 71, impresa 52; [4-marco_teorico.tex:1518](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1518). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «(sección 3.5.3),».
- **Contexto del PDF:** «a partir de las señales de recompensa compuestas (sección 3.5.3), propagándolos median-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Retirar la remisión parentética aislada a metodología dentro de la adaptación HAPPO o convertirla en una explicación útil del destino. Conservar el contraste entre ventajas individuales de la implementación y retorno compartido del lema original.

#### C276 — tabla

- [ ] **Editorial · Atendida en la fuente; verificar PDF.**
- **Ubicación:** PDF 72, impresa 53; [4-marco_teorico.tex:1520](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1520). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «tabla».
- **Contexto del PDF:** «MARL, la tabla 2.3 sintetiza sus principales propiedades operativas, arquitectónicas y».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Tabla» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

### Antecedentes y posicionamiento

#### C277 — recientes

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 72, impresa 53; [4-marco_teorico.tex:1541](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1541). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «recientes».
- **Contexto del PDF:** «2.3.7. Antecedentes recientes del control semafórico multiagen-».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar el adjetivo «recientes» tachado en el título de antecedentes. Dado que se incluyen trabajos fundacionales y recientes, elegir un título que represente el contenido o justificar temporalmente la selección sin prometer novedad uniforme.

#### C278 — trabajo:

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 74, impresa 55; [4-marco_teorico.tex:1557](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1557). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «trabajo:».
- **Contexto del PDF:** «de escalabilidad, pero no es equivalente a la formulación de este trabajo: aquí la ejecución».
- **Observación literal de Caro:**

  > dado que

- **Corrección y detalle:** Sustituir los dos puntos de «este trabajo: aquí…» por una conexión como «dado que…», reajustando la sintaxis. Explicar de forma continua la diferencia entre la arquitectura distribuida del antecedente y los mecanismos de esta tesina.

#### C279 — implementan

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 74, impresa 55; [4-marco_teorico.tex:1559](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1559). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «implementan».
- **Contexto del PDF:** «En este estudio, IPPO e IDQN implementan el paradigma de aprendizaje independiente».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Revisar el verbo «implementan» tachado junto con C280. Identificar si se describe una decisión de diseño, una implementación disponible o una campaña efectivamente ejecutada, y elegir el verbo y el tiempo que la evidencia sostenga.

#### C280 — En este estudio,

- [ ] **Alta · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 74, impresa 55; [4-marco_teorico.tex:1559](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1559). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En este estudio,».
- **Contexto del PDF:** «En este estudio, IPPO e IDQN implementan el paradigma de aprendizaje independiente».
- **Observación literal de Caro:**

  > en cual estudio????? Hadad et al impilementan? OESTAS HABLANDO DE TU TRABAJO ???? reescribir bien estas hablando en presente de algo que aun no hiciste. No se entiende esta frase. Creo que se refiere a la tesina así que yo pondría algo como: Para esta tesina IPPO e IDQN utilizan el ......

- **Corrección y detalle:** Distinguir explícitamente el estudio de Haddad et al. de esta tesina. Reemplazar «En este estudio» por «En esta tesina…» o una fórmula inequívoca y separar los resultados ajenos de las decisiones propias. La fuente actual dice «…de este estudio» y todavía requiere esa precisión; no convertir un protocolo refinado documentado en prueba de ejecución.

#### C281 — Posicionamiento del proyecto

- [ ] **Media · Pendiente.**
- **Ubicación:** PDF 76, impresa 57; [4-marco_teorico.tex:1579](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1579). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «Posicionamiento del proyecto».
- **Contexto del PDF:** «Posicionamiento del proyecto».
- **Observación literal de Caro:**

  > Posicionamiento del presente trabajo

- **Corrección y detalle:** Cambiar «Posicionamiento del proyecto» por «Posicionamiento del presente trabajo». Mantener coherencia con la denominación del documento y revisar la entrada del índice tras compilar.

#### C282 — sugiere

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 76, impresa 57; [4-marco_teorico.tex:1581](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1581). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «sugiere».
- **Contexto del PDF:** «La selección analizada sugiere que el desempeño del control semafórico multiagente».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Reformular el verbo tachado «sugiere» junto con C283 para presentar una inferencia explícita de la revisión de antecedentes. Evitar que el cambio aumente la fuerza de una conclusión más allá de las fuentes seleccionadas.

#### C283 — La selección analizada

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 76, impresa 57; [4-marco_teorico.tex:1581](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1581). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «La selección analizada».
- **Contexto del PDF:** «La selección analizada sugiere que el desempeño del control semafórico multiagente».
- **Observación literal de Caro:**

  > Del estado del arte se puede inferir

- **Corrección y detalle:** Comenzar con una formulación como «Del estado del arte se puede inferir…» y vincularla con los tres ejes analizados. Hacer reconocible el paso desde la descripción de publicaciones a la interpretación propia.

#### C284 — En las fuentes consul- tadas hasta septiembre de 2026

- [ ] **Alta · Parcial o aparentemente atendida; verificar cierre.**
- **Ubicación:** PDF 76, impresa 57; [4-marco_teorico.tex:1583](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1583). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «En las fuentes consul- tadas hasta septiembre de 2026».
- **Contexto del PDF:** «como equivalentes ni como evidencia de que HAPPO sea superior. En las fuentes consul- tadas hasta septiembre de 2026 no se localizó una evaluación conjunta de IDQN, IPPO,».
- **Observación literal de Caro:**

  > Hasta donde se tiene conocimiento, no existen reportes previos sobre una evaluación .....

- **Corrección y detalle:** Reformular la afirmación de novedad con alcance prudente: «Hasta donde se tiene conocimiento, no se localizaron reportes…», identificando el conjunto o fecha de búsqueda si se dispone de ellos. No afirmar la inexistencia universal de evaluaciones similares ni omitir una aplicación encontrada posteriormente.

#### C285 — Esta observación delimita la búsqueda realizada y no permite concluir que tales estudios no …

- [ ] **Alta · Pendiente.**
- **Ubicación:** PDF 76, impresa 57; [4-marco_teorico.tex:1583](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1583). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (StrikeOut):** «Esta observación delimita la búsqueda realizada y no permite concluir que tales estudios no existan.».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Condensar la cautela tachada sobre los límites de la búsqueda si repite lo que ya expresa C284. Preservar su contenido epistemológico en una sola formulación: una revisión acotada no demuestra que no existan estudios previos.

#### C286 — capítulo

- [ ] **Editorial · Pendiente.**
- **Ubicación:** PDF 77, impresa 58; [4-marco_teorico.tex:1591](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1591). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «capítulo».
- **Contexto del PDF:** «tratar agentes heterogéneos. El capítulo 3 describe cómo se concreta esta propuesta en el».
- **Observación:** sin comentario escrito; la acción siguiente interpreta la marca en su contexto.
- **Corrección y detalle:** Usar «Capítulo» con mayúscula inicial al remitir a un elemento numerado, según la convención editorial solicitada por Caro. Mantener la referencia con su macro y etiqueta; revisar esta aparición concreta y las equivalentes sin reemplazar usos genéricos o plurales indiscriminadamente.

#### C287 — experimental.

- [ ] **Conservar · Conservar; sin corrección solicitada.**
- **Ubicación:** PDF 77, impresa 58; [4-marco_teorico.tex:1591](/home/juanm4/Documentos/tesina/4-marco_teorico.tex:1591). Pasaje actual o bloque al que pertenece la marca.
- **Texto marcado (Highlight):** «experimental.».
- **Contexto del PDF:** «diseño experimental.».
- **Observación literal de Caro:**

  > me gusta el análisis final que has realizado te quedó muy bien

- **Corrección y detalle:** Conservar el análisis final de posicionamiento, comparación de procedimientos completos y límites de atribución causal. Caro lo valora positivamente; al abreviar o reorganizar, mantener la distinción entre propuesta, evidencia y necesidad de experimentos de retirada de componentes.
- **Cierre:** no requiere reescritura por esta marca; comprobar que las correcciones vecinas preserven la cualidad valorada.

## Control de integridad

Las fichas cubren las 287 anotaciones de revisión, sin fusionar sus identificadores. Los comentarios favorables son C246 y C287; las restantes 285 fichas registran correcciones, verificaciones o decisiones editoriales, algunas ya parcialmente resueltas. Las notas adhesivas son C001, C059, C140, C209 y C214. C208/C209 y C213/C214 se refieren a cortes próximos o coincidentes; C012/C013, C021–C024, C028–C031, C068–C069, C071–C075 y C233–C234 deben resolverse de forma conjunta. La coincidencia de acciones no implica que falte una anotación.

Se revisaron visualmente las páginas físicas 29, 42 y 51 para precisar la pequeña tachadura de la tabla y la ubicación de las notas junto a Sutton y Barto y la puntuación de DRL. Las demás ubicaciones proceden de los objetos de anotación del PDF, sus coordenadas y el contraste con las fuentes actuales. La revisión visual de la diagramación completa se realizará al aplicar las correcciones, no se presume completada por este inventario.

Identificación de la fuente: SHA-256 `5744bcd65e0637108baf1724d374973f249c058da6be9d01a4e7bfec19612065`. Las líneas de este TODO reflejan el estado local del repositorio al generar el relevamiento.


## Seguimiento de figuras de metodología — 2026-10-18

El [informe del rediseño de figuras](INFORME-redisenio-figuras-metodologia.md) registra las decisiones, fuentes, integración y comprobaciones de las doce figuras principales y los dos traslados al apéndice. Este bloque aplica especialmente R08–R12, R17 y R24; no modifica el estado de las 287 fichas de revisión anteriores.


### Revisión posterior de las figuras

Las observaciones del usuario sobre utilidad, simetría y superposiciones motivaron una [segunda revisión con justificación por figura](REVISION-figuras-metodologia-criterio-y-verificacion.md). Sustituye la aprobación visual del informe v05: se retiran el panel «fase activa: 2», el inserto urbano y recorridos redundantes, se rehacen las calzadas sintéticas y se separa la recompensa de la entrada del actor en A/C. No se modifican por ello los estados de las fichas anteriores.

En una revisión posterior, el usuario pidió explicitar los nombres de las formulaciones A y C, ampliar la variedad de recursos visuales y mantener en inglés el término de RLlib *Learner*. La Figura 3.12 pasó de un flujo a una matriz que hace visibles las filas de entrenamiento emparejadas, las cinco evaluaciones comunes y la unidad remuestreada. La Figura 3.5 y su explicación usan *Learner*. Se compilaron y revisaron las páginas completas y ambas figuras en color y escala de grises.


En la revisión v16, el usuario pidió justificar las figuras 3.8, 3.11 y 3.12 y explicar previamente toda notación. Se descartó la matriz de «w» y se simplificó el pareo a dos filas de episodios; se conservaron los casos de inclusión vehicular y la línea temporal de la máscara por su función metodológica explícita. Se corrigió el salmón del estado amarillo y se retiró el panel de inicialización. La revisión de las doce introducciones añadió las convenciones que faltaban, conforme a R01, R05, R09, R10, R12 y R24. Las decisiones actuales están en el informe de revisión; las notas de v14 describen el estado histórico.
