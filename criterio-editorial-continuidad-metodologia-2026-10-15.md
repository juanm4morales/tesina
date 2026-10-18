**Criterio editorial para integrar los cambios de la metodología — 15/10/2026**

La mejor versión debe conservar el recorrido actual del capítulo, incorporar las supresiones del remoto que eliminan repeticiones y recuperar únicamente las aclaraciones locales que evitan una interpretación equivocada. Hay, además, algunos enlaces con el marco teórico que requieren precisión. La longitud de un párrafo o la cantidad de palabras eliminadas no permiten, por sí solas, decidir qué versión se lee mejor.

Esta revisión compara `origin/main` en `ecf6182` con la versión local y la rama de coherencia en `8d1642a`. Se releyeron los pasajes pertinentes del marco teórico, que coincide en ambas versiones, y del glosario. Es una evaluación y una propuesta de redacción; no se aplicaron estos cambios a las fuentes LaTeX.

**1. El criterio para aceptar una modificación**

Un cambio está justificado cuando permite que el lector identifique con menos esfuerzo qué se hace, sobre qué objeto y con qué consecuencia. Debe conservar las condiciones necesarias para interpretar el procedimiento. Una frase repetida puede eliminarse cuando la explicación permanece cerca y el lector no necesita reconstruir una distinción importante. Una explicación breve debe mantenerse cuando conecta una decisión concreta con el concepto que la fundamenta.

La metodología puede apoyarse en lo que el marco teórico ya explicó: agente, observación, acción, política, recompensa, crítico, ventaja, iteración y entrenamiento centralizado. Su tarea es concretar esos conceptos: qué recibe aquí el actor, qué recibe aquí el crítico, cómo se calcula aquí la señal y cómo se seleccionan y evalúan las políticas. HPO requiere una presentación operativa propia: en el marco teórico los hiperparámetros están introducidos, pero no se desarrollan Optuna, TPE ni ASHA.

**2. Decisiones sobre los cambios concretos**

| Pasaje | Decisión | Justificación desde la lectura |
|---|---|---|
| Apertura y organización general | Conservar | La apertura ya identifica el problema y las dos líneas, y el recorrido escenarios → sistema → entrenamiento → evaluación sigue las dependencias del trabajo. Reorganizarlo obligaría a reconstruir referencias sin resolver un problema claro. |
| Diseño experimental: frases eliminadas sobre búsqueda, selección y evaluación | Mantener la supresión remota | El párrafo de apertura inmediatamente anterior ya explica esa secuencia. Repetirla al comienzo de Diseño experimental retrasa la entrada a las dos fases y a A/C. El diagrama conserva la visión conjunta. |
| Una remisión al apéndice tras cada red sintética | Mantener la remisión conjunta remota | Los tres párrafos forman un bloque comparativo. Una referencia al final, que indique expresamente que cubre las tres redes, evita tres interrupciones con el mismo destino. |
| «Las referencias conservan esos programas» en la descripción urbana | Mantener la supresión remota | El pasaje ya dice que los programas se utilizan como referencias. La conservación de su funcionamiento vuelve a precisarse donde se compara con las políticas; allí sí es una condición relevante. |
| «Estos valores describen el perfil registrado…» | Mantener la supresión | El comienzo de la sección limita la cobertura de los conteos y la demanda diaria se declara como supuesto. La frase añade otra cautela general sin una nueva consecuencia para el procedimiento. Las diferencias entre perfiles históricos deben permanecer. |
| Presentación de la recompensa | Preferir el párrafo compacto remoto | «Se define primero la señal… y luego…» anuncia el orden que ya muestran los párrafos y ecuaciones inmediatos. Al suprimirlo, la explicación llega directamente a la cantidad que se calcula. |
| Pérdida del crítico | Preferir la versión remota | El primer párrafo describe la operación y el segundo explica la consecuencia sobre el gradiente. La versión anterior anticipaba y repetía esa consecuencia. La distinción con el recorte convencional de valores debe permanecer: enlaza teoría e implementación. |
| Herramientas de búsqueda | Conservar la formulación remota y separar antes de ASHA | El remoto evita repetir «basadas en el historial» y «en las búsquedas». La separación propuesta distingue dos funciones: proponer y ejecutar configuraciones, y detener ensayos. TPE y ASHA son contenidos nuevos para este lector y merecen explicaciones completas. |
| Excepción urbana de fase 1 repetida en las condiciones generales | Mantener la supresión remota | La excepción sigue anunciada en las condiciones generales y se desarrolla en Fase 1. No hace falta explicar dos veces su cronología y rho. |
| «Cada red se refina» | Sustituir por la formulación local sobre los dominios | La red de tráfico no se modifica en esta operación. Nombrar los dominios como objeto evita una interpretación equivocada y mantiene la correspondencia con la fase 1. |
| Final de la explicación de fase 1: sus resultados orientan fase 2 | Mantener la supresión remota | La dependencia se presenta en Diseño experimental y en la apertura de las dos fases. La repetición no aporta un criterio nuevo. |
| Selección urbana: escenario, archivos y comparación | Recuperar la separación local | El primer párrafo identifica las entradas y la ventana. El siguiente explica qué condiciones comparten candidato y referencia. Son dos preguntas distintas que el lector necesita resolver. |
| Admisibilidad urbana | Recuperar la separación local y mantener juntos regla y alcance | Primero se debe entender qué candidato cumple. Después, qué información permite decidirlo. Así se distingue evidencia incompleta de un resultado desfavorable. La frase sobre criterios relativos a la referencia pertenece a la regla de aceptación. |
| Introducción de A/C | Sustituir la primera oración, sin anteponer otra introducción | La versión remota avanza con rapidez, pero elimina la pregunta específica de la sección. El propósito breve y la condición común de hiperparámetros reemplazan la oración inicial existente; después se conservan las definiciones de A y C. |
| Relación entre A–E y A/C | Preferir la oración breve remota | Indicar que la comparación ampliada estuvo precedida por una prueba preliminar establece la relación necesaria. Los detalles se desarrollan enseguida en sus subsecciones. |
| Remisión a observaciones y recompensas de A/C | Integrarla una sola vez, al final del párrafo que define el contraste | Evita un párrafo compuesto únicamente por una referencia y mantiene unidas las definiciones de A y C y la consecuencia de modificar dos componentes. No pondría la remisión entre esa descripción y su consecuencia. |
| Configuración histórica de A/C y tamaño de entrada | Separar procedencia de hiperparámetros y diferencias entre variantes | Primero el lector necesita saber qué se mantuvo fijo. Después debe reconocer qué cambia con C y cómo limita la interpretación. |
| «Esta diferencia de capacidad forma parte de la comparación…» | No recuperar la frase local completa | La oración anterior ya explica que C tiene más pesos y la introducción de A/C ya declara el cambio conjunto de observación y recompensa. Es suficiente conservar ambos hechos, separados con claridad, sin volver a enumerarlos. |
| «Por ello, este cierre temporal forma parte de la interpretación…» | Mantener su supresión | La consecuencia concreta sobre valores y ventajas ya está expresada. La frase añade una conclusión abstracta que no aclara cómo cambia el aprendizaje. Conviene definir los indicadores, no añadir otra advertencia general. |
| Dos horas frente a doce horas | Recuperar la separación local | Cambian el horizonte, el calentamiento y la función de la corrida. La evaluación diaria debe abrir un párrafo y conservar a su lado el propósito de examinar condiciones horarias distintas. |
| Intervalos principales y sensibilidad | Recuperar la separación local | Bonferroni y los niveles de confianza forman el procedimiento principal; Student es una comprobación complementaria. La separación permite reconocer su jerarquía sin quitar las cautelas. |
| Presupuesto urbano y tamaño del lote | Recuperar la separación local | La cantidad de propuestas describe la búsqueda. Los pasos por episodio y el tamaño del lote describen el trabajo del aprendiz. Compartir unidades numéricas no los convierte en una misma idea. |
| Explicación extensa de las citas de HPO | Preferir la formulación remota | Basta identificar qué afirmación apoya la literatura y señalar que rangos y presupuestos son decisiones del diseño. Las justificaciones concretas, cuando existan, deben acompañar sus decisiones; una defensa genérica adicional no las sustituye. |

Estas decisiones modifican mi recomendación anterior: no recuperaría automáticamente todas las explicaciones locales ni todas las frases eliminadas. Las separaciones de párrafos se justifican por un cambio de función, no por una preferencia por párrafos cortos.

**3. Continuidad con el marco teórico: puntos que sí necesitan atención**

**Observación y estado.** El marco distingue el estado global de la observación accesible a cada agente. La metodología concreta esa distinción al explicar que el crítico concatena observaciones y no recibe el estado físico completo. Mantendría esa aclaración: evita leer el diagrama teórico de CTDE como una especificación literal del programa. No repetiría la definición de estado ni introduciría otra tupla matemática en la metodología.

También conservaría la explicación de que los actores no comparten parámetros. El marco presenta la compartición como una posibilidad de MAPPO; la metodología indica la elección concreta. Esta repetición parcial tiene una función: resolver una alternativa que la teoría dejó abierta.

**Recompensa individual y recompensa compuesta.** Hay una discontinuidad real. El marco explica correctamente, en su presentación general y su cierre, que los procedimientos utilizan señales diferentes. Sin embargo, en las líneas 1362 y 1518 describe la implementación mediante «recompensa individual compuesta» y «señales de recompensa compuestas». Esa redacción puede hacer que el lector suponga que MAPPO y HAPPO siempre mezclan información local y vecinal.

Para los pasajes generales propondría sustituir «recompensas compuestas» por «recompensas individuales»; el tipo de señal se concreta por procedimiento en la metodología. En el marco, la mención a una señal «compuesta local-vecinal» al comparar con Wu —línea 1557— también necesita atribuirse a la variante correspondiente. En la explicación de asignación de crédito —línea 1225— se puede conservar la mezcla como ejemplo del diseño vecinal, identificando ese alcance. El término «compuesta» no debe generalizarse ni desaparecer de los lugares donde sí designa la mezcla. Estas correcciones sustituyen expresiones existentes: no añaden otra explicación de las recompensas ni repiten la tabla de procedimientos.

**HAPPO teórico y adaptación.** El marco expone una secuencia donde los actores se actualizan antes del crítico. La metodología dice que la implementación actualiza primero el crítico y luego los actores, y el apéndice explica la regla de ordenación. La expresión del marco «la secuencia conserva esta estructura de permutación y actualización sucesiva» —línea 1518— puede sugerir una coincidencia más amplia de la que se documenta.

Recomendaría acotar esa correspondencia a lo que se conserva: la actualización sucesiva de actores y la reponderación después de cada actualización. La metodología ya precisa el orden del crítico, y el apéndice desarrolla la elección de actores; conservaría esas explicaciones en sus lugares actuales. Basta sustituir la expresión demasiado amplia del marco. No hace falta desarrollar otra vez el lema de descomposición ni cambiar los pseudocódigos teóricos para que parezcan el código experimental.

**Bootstrapping y bootstrap.** El marco define *bootstrapping* como actualizar una estimación de valor usando otra estimación —línea 641—, pero en GAE utiliza también *bootstrap* —línea 1044—. En el análisis estadístico, *bootstrap* designa remuestreo con reemplazo, y ese es el significado de su entrada del glosario.

Mantendría *bootstrapping* para la estimación de valores en el marco, sustituyendo la variante *bootstrap* de la explicación de GAE. En el cierre de episodios de la metodología puede bastar «incorporación del valor estimado del estado final», con la referencia a GAE. La incertidumbre ya presenta el remuestreo con reemplazo y el término *bootstrap*: conservaría esa presentación. No añadiría una advertencia que vuelva a definir ambos términos. Las sustituciones propuestas distinguen las operaciones sin sumar explicaciones.

**Métricas operacionales.** El marco introduce demora, completitud, equidad y teletransportes como categorías; la metodología define sus medidas concretas. Esa distribución funciona. Mantendría las definiciones de espera por viaje, cohorte y Gini donde se calculan. No repetiría la lista general de indicadores al comienzo de cada procedimiento. La recompensa y la métrica de evaluación deben seguir nombrándose por separado.

**4. Vocabulario que conviene estabilizar**

| Término | Uso recomendado | Confusión que se evita |
|---|---|---|
| Búsqueda refinada / fase 2 | Presentarlas como dos denominaciones de la misma etapa; usar «búsqueda refinada» después | «Búsqueda informada», presente en el marco, puede parecer otro procedimiento si no se identifica con fase 2 |
| Configuración | Valores elegidos para entrenar; señalar qué incluye según el procedimiento | Confundir los hiperparámetros con los pesos aprendidos |
| Configuración histórica aplicada a otras redes | Explicar que se reutilizan los mismos hiperparámetros | «Configuración transferida» puede sugerir transferencia de un modelo ya entrenado |
| Ensayo y estudio de HPO | Un ensayo entrena una configuración; un estudio reúne ensayos para algoritmo, escenario y arquitectura | Contar episodios, ensayos y estudios como si fueran repeticiones equivalentes |
| Configuración inicial de fase 2 | Preferirla a «configuración de referencia» cuando solo inicia la búsqueda | Confundirla con el programa semafórico de referencia o con una línea de base |
| Política y modelo final | Conservar sus usos actuales y el contexto por algoritmo, escenario y agente | La sección de agentes ya explica los módulos por agente y la ausencia de parámetros compartidos; no se justifica añadir esa explicación en el entrenamiento final |
| Estado guardado del modelo (*checkpoint*) | Elegir una denominación y mantenerla, distinguiéndola del estado guardado de SUMO | Alternar «punto de control», «modelo de la última» y «archivo de estado» sin dejar claro el objeto |
| Seguimiento diagnóstico, selección y evaluación final | Mantener el complemento que identifica la función | Leer todos los episodios sin exploración como una evaluación final independiente |
| Paso de decisión y segundo de simulación | Precisar la escala cuando se cambia de aprendizaje a medición o calibración | Confundir decisiones cada cinco segundos con muestras registradas cada segundo |
| Red de tráfico y red neuronal | Añadir el complemento cuando ambos referentes están próximos | «Refinar la red» o «inicializar sus redes» puede referirse a objetos distintos |

No propondría reemplazos globales: «referencia», «modelo», «fase» y «red» tienen varios usos legítimos. El complemento debe aparecer donde el contexto no baste. Tampoco impondría una nueva terminología para lote, minibatch o epoch en este pase: el marco y el glosario ya los presentan. Si se decide usar siempre las formas españolas, debe coordinarse el glosario, porque algunas macros muestran actualmente las formas inglesas.

**5. Dos formulaciones concretas para evaluar la integración**

Estas propuestas ilustran el criterio. No sustituyen una revisión del párrafo completo con sus macros y referencias.

Para fase 2, conservaría:

> En la fase 2, los dominios de cada escenario se refinan a partir de los resultados de su fase 1.

El sujeto identifica exactamente el objeto que cambia. Las condiciones numéricas y las reglas urbanas deben decidirse con la evidencia del protocolo; no corresponde escogerlas por la brevedad que permitan.

Para abrir A/C, recuperaría un propósito breve:

> Esta comparación examina si la variante vecinal de MAPPO mejora el desempeño respecto de la variante local. La campaña contrastó A y C con una configuración de hiperparámetros común y fija.

Estas dos oraciones sustituyen la primera oración de la sección; no se añaden delante de ella. Después deben conservarse las definiciones de A y C, los valores de rho y la explicación de que el contraste modifica conjuntamente observación y recompensa. La remisión a sus fórmulas puede cerrar ese párrafo. La procedencia histórica de los valores se desarrolla en Entrenamiento de las variantes. Así se evita que «transferida» sugiera reutilización de pesos y se recupera una pregunta específica sin repetir toda la apertura del capítulo.

Retiro la propuesta anterior de explicar aquí que el modelo final reúne las políticas de los agentes. Leído junto con la sección de agentes y con la apertura de Evaluación, el uso actual de «modelo final» tiene contexto suficiente. La aclaración repetiría la organización ya descrita sin resolver una ambigüedad comprobada en ese pasaje.

**6. Comprobación específica de redundancias**

Se contrastaron las aclaraciones propuestas con sus párrafos vecinos y con los pasajes relacionados del marco. El resultado distingue las operaciones que cambian la presentación de las que modifican el texto:

| Intervención | Operación mínima | Contenido que no debe volver a explicarse |
|---|---|---|
| Separaciones de párrafos | Insertar un corte; en admisibilidad, trasladar la frase de alcance junto a la regla | Los mismos criterios, ventanas, funciones y cautelas ya presentes |
| «Cada red se refina» | Sustituir el sujeto por los dominios del escenario | La dependencia entre fase 1 y fase 2, ya presentada |
| Apertura de A/C | Sustituir su primera oración | No conservar además la oración inicial remota ni reintroducir otra descripción completa de las dos líneas del capítulo |
| Capacidad de C y cierre temporal | Conservar las consecuencias concretas existentes | No recuperar «esta diferencia forma parte de la comparación» ni «por ello, este cierre forma parte de la interpretación» |
| Señales de recompensa | Corregir el alcance del término en el marco | No añadir en la metodología otra lista de señales ni repetir la distinción local/vecinal fuera de su explicación y tabla |
| Adaptación de HAPPO | Precisar qué estructura se conserva en el pasaje del marco | No duplicar la secuencia de actualización ni la advertencia sobre garantías teóricas |
| Bootstrapping y bootstrap | Estabilizar las denominaciones y conservar la definición estadística existente | No añadir una nota explicativa que vuelva a definir ambos procedimientos |
| Modelo final | Mantener el párrafo actual | No volver a explicar los módulos por agente y la ausencia de parámetros compartidos |

La revisión debe comparar ideas, no solo coincidencias literales: una paráfrasis puede repetir la misma afirmación. Una remisión puede sustituir una segunda explicación cuando el lector necesita consultar el detalle; no debe sustituir una condición indispensable para entender el procedimiento que está leyendo. La corrección histórica de 3×3 también debe sustituir la atribución ambigua existente, sin añadir dos versiones del mismo alcance.

**7. Orden de una futura intervención**

Primero corregiría las ambigüedades entre capítulos: alcance de las recompensas compuestas, rasgos heredados de HAPPO y los dos sentidos de bootstrap. Después estabilizaría el vocabulario dentro de la metodología y aplicaría las decisiones de párrafo de la tabla. Finalmente leería cada sección completa para comprobar antecedentes, remisiones y continuidad con la siguiente.

La operación editorial no debería convertir en comunes procedimientos distintos ni alterar valores, semillas, ecuaciones o condiciones. El desacuerdo entre la especificación remota de fase 2 y el protocolo identificado permanece como una cuestión de contenido independiente. Esta revisión deja justificadas las opciones de lectura sin resolver ese desacuerdo mediante una simplificación verbal.
