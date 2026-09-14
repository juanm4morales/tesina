# Revisión de metodología y sugerencias de incorporación

Fecha: 9 de septiembre de 2026.

## 1. Dictamen y alcance

La revisión de `5-metodologia.tex` incorporó buena parte de los contenidos solicitados, pero su cumplimiento es parcial. Mejoró la descripción de la integración con SUMO, las observaciones, la recompensa vecinal y el objetivo de búsqueda de hiperparámetros. Persisten errores de correspondencia entre texto, código y figuras, decisiones experimentales sin cerrar y una justificación bibliográfica insuficiente para algunas elecciones.

La desviación principal es la afirmación de que Mendoza recibiría una política congelada procedente de los escenarios sintéticos. Esa afirmación fue introducida en la edición anterior y no responde al diseño indicado por el autor. **El escenario Ciudad de Mendoza tendrá ajuste propio de hiperparámetros para MAPPO, HAPPO, IPPO e IDQN, seguido del entrenamiento y evaluación de sus modelos.** Congelar hiperparámetros antes de la evaluación final no implica transferir pesos entre escenarios.

Este documento registra hallazgos y especifica correcciones y figuras futuras. Su creación no aplica esas correcciones a los capítulos, no genera figuras ni modifica el código experimental. Las casillas pendientes describen trabajo por realizar; no acreditan ejecuciones o resultados.

### Base de contraste

- Requisitos originales del autor, incluidos sus 14 puntos y la aclaración sobre Mendoza.
- Diferencia de trabajo de `5-metodologia.tex` frente a HEAD: 157 líneas agregadas y 53 eliminadas al momento de la revisión. Las líneas LaTeX pueden contener párrafos completos; este conteo no mide calidad ni exhaustividad.
- Repositorio de escritura: HEAD `c67d08a`, con modificaciones previas sin confirmar. Repositorio experimental: HEAD `79262e54`; se inspeccionaron archivos del árbol de trabajo. Estos identificadores no sustituyen una captura de los cambios locales.
- Inspección del capítulo y de las dos imágenes incorporadas; contraste dirigido de codificador, recompensas, selección de candidatos, espacio de búsqueda y cálculo de estabilidad.
- `plan-correcciones.md` corresponde a otra revisión general y no constituye una lista de aceptación de los 14 requisitos recientes.

Se distingue entre **evidencia verificada** en los archivos inspeccionados, **contenido declarado** por el capítulo que requiere trazabilidad adicional y **recomendaciones** de esta revisión. La existencia de un script o un notebook no demuestra que todas sus ejecuciones se hayan completado ni que sus salidas correspondan a la configuración definitiva.

### Fuentes locales de consulta

Los anclajes por sección o función son preferibles a números de línea, que cambiarán con futuras ediciones.

| Clave | Fuente | Uso |
|---|---|---|
| E1 | [5-metodologia.tex](5-metodologia.tex) | Texto, ecuaciones, tablas y figuras evaluadas. |
| E2 | [4-marco_teorico.tex](4-marco_teorico.tex) | Coherencia conceptual y frontera entre teoría e implementación. |
| E3 | [encoder.py](/home/juanm4/Dev/marl-tlc/src/marlTLC/utils/encoder.py) | Transformación, redondeo y saturación. |
| E4 | [traffic_light.py](/home/juanm4/Dev/marl-tlc/src/marlTLC/environments/traffic_light.py) | Observaciones, fases, máscara y transiciones. |
| E5 | [reward_functions.py](/home/juanm4/Dev/marl-tlc/src/marlTLC/environments/reward_functions.py) | Fórmulas efectivas de recompensa. |
| E6 | [sumo_env.py](/home/juanm4/Dev/marl-tlc/src/marlTLC/environments/sumo_env.py) | Conexión, reinicio, telemetría y ventanas. |
| E7 | [search_space.py](/home/juanm4/Dev/marl-tlc/experiments/marl_experiments/tuning/shared/search_space.py) | Parámetros fijos y distribuciones por algoritmo. |
| E8 | [protocol.py](/home/juanm4/Dev/marl-tlc/experiments/marl_experiments/tuning/shared/protocol.py) | Presupuesto y estado de incorporación de Mendoza. |
| E9 | [select_candidates.py](/home/juanm4/Dev/marl-tlc/experiments/marl_experiments/tuning/phase1_hpo/select_candidates.py) | Elegibilidad, ordenamiento y recetas congeladas. |
| E10 | [callbacks.py](/home/juanm4/Dev/marl-tlc/src/marlTLC/agents/multi_agent/callbacks.py) | Espera estable y métricas de entrenamiento/evaluación. |
| E11 | [paired_bootstrap.py](/home/juanm4/Dev/marl-tlc/experiments/marl_experiments/tuning/phase2_confirmation/paired_bootstrap.py) | Confirmación pareada. |
| E12 | [mendoza_scenario_design.ipynb](/home/juanm4/Dev/marl-tlc/experiments/mendoza_scenario/mendoza_scenario_design.ipynb) y [vicente_zapata_study.ipynb](/home/juanm4/Dev/marl-tlc/experiments/mendoza_scenario/vicente_zapata_study.ipynb) | Fuentes identificadas para verificar procesamiento, demanda y futuras figuras; sus salidas deberán contrastarse antes de publicarlas. |

## 2. Cobertura de los requisitos originales

“Parcial” significa que existe contenido pertinente pero no alcanza para cerrar el requisito. “Inconsistente” identifica una contradicción que debe resolverse. Los números conservan la correspondencia con el pedido original, no el orden recomendado del capítulo.

| N.º | Requisito | Estado | Evidencia y condición de cierre |
|---|---|---|---|
| 1 | Buenas prácticas científicas y experimentales | Parcial | E1 distingue métricas y semillas; faltan elegibilidad exacta, unidad de réplica, checkpoint y separación entre protocolo y resultados. Cerrar C4–C6. |
| 2 | Claridad, orden y lectura ligera | Parcial | Hay secciones identificables, pero persisten redundancias, identificadores extensos y justificaciones ligadas a incidencias técnicas. Aplicar C8. |
| 3 | Coherencia con el marco teórico | Parcial | Se aclaró la adaptación de MAPPO/HAPPO. Falta revisar recompensa individual frente a Dec-POMDP, observación conjunta frente a estado completo y la afirmación DAG. Cerrar C7. |
| 4 | Figuras y tablas suficientes; trabajos similares | Parcial | Solo hay tres figuras y dos presentan problemas de correspondencia. Ejecutar el programa F0–F10 y completar el contraste bibliográfico. |
| 5 | Modelado, recompensas, integración, algoritmos y máscara | Parcial | E1 y E3–E6 aportan detalles; quedan errores en la máscara, unidades y evidencia de recompensas probadas. Cerrar C2–C3. |
| 6 | Codificador de carriles explícito | Parcial | Se cita E3 y su fórmula. Falta alinear las ilustraciones y representar el vector y la máscara con fidelidad. Cerrar F5–F6. |
| 7 | Métricas relevantes justificadas | Parcial | Espera, pérdida temporal, atención de demanda y equidad están presentes. Precisar población, censura al cierre, denominadores y respaldo bibliográfico. Cerrar C6 y T5. |
| 8 | Hiperparámetros fijos fundamentados en literatura | Parcial | Se declara gamma=0,99, pero la referencia a valores del propio proyecto no acredita exploración del estado del arte. Cerrar C5 y T1. |
| 9 | Diseño completo de HPO sin relatar fracasos | Parcial | Hay espacio PPO/IDQN; falta grad_clip de IDQN, epochs de IPPO, detalle de poda y presupuesto comparable. Retirar alusiones históricas. Cerrar C4–C5. |
| 10 | Presentación de resultados y métricas | Parcial | Existen tablas e intervalos previstos. Falta contrato de agregación y figuras de resultados. Cerrar R1–R4. |
| 11 | Criterio objetivo de selección | Parcial | El objetivo corresponde al callback, pero el desempate y los filtros se describen de forma más amplia que E9. Cerrar C4. |
| 12 | Selección de hiperparámetros finales | Inconsistente | Se describe congelamiento, pero se excluye indebidamente Mendoza. Los valores finales requieren recetas trazables, no pueden inferirse. Cerrar C1, C4 y T4. |
| 13 | Diseño detallado de escenarios, especialmente Mendoza | Parcial | Hay geometría, flujos y limitaciones del aforo. Faltan mapas y trazabilidad de cifras, ventanas, matriz OD y calibración. Cerrar C1, C8 y F1–F4. |
| 14 | Evaluación de modelos ajustados en los escenarios | Inconsistente | La transferencia congelada contradice el ajuste propio de Mendoza. Precisar entrenamiento, evaluación y semillas por algoritmo/escenario. Cerrar C1 y C6. |

## 3. Correcciones y comprobaciones pendientes

### C1. Ajuste propio de Mendoza — prioridad crítica

**Evidencia:** E1, secciones del escenario urbano y selección de configuraciones, afirma transferencia y excluye Mendoza de HPO. E8 registra `blocked_until_synthetic_lock` y `budget: None`; ese estado de implementación no determina el diseño final autorizado por el autor.

- [ ] Sustituir las afirmaciones de transferencia por ajuste, entrenamiento y evaluación propios para los cuatro algoritmos. Texto base: «Cada algoritmo se ajustará y entrenará en cada escenario, incluida la Ciudad de Mendoza. Las configuraciones seleccionadas se congelarán antes de la evaluación final del escenario correspondiente».
- [ ] Mantener la distinción entre calibración de demanda y ajuste del controlador. La escasez de aforos limita la representatividad del escenario, pero no impide realizar HPO dentro de él.
- [ ] Registrar presupuesto, arquitecturas, ventanas y semillas de Mendoza desde su configuración de campaña cuando se establezcan. Hasta entonces, declararlos pendientes, sin copiar automáticamente valores sintéticos.
- [ ] Alinear introducción, flujo general, tablas, selección y evaluación con esta decisión. El entrenamiento de un modelo por escenario no debe presentarse como transferencia de pesos.

**Cierre:** ninguna sección excluye Mendoza de HPO; los cuatro algoritmos figuran en su protocolo y los parámetros aún no fijados se reconocen como pendientes. La sincronización del código experimental es trabajo posterior, no realizado por este documento.

### C2. Observación, codificador y máscara — prioridad alta

**Evidencia:** E3 devuelve índices entre 0 e I−1; E4 implementa `_compute_action_mask` y una observación con campos `obs` y `action_mask`. En E1, la ecuación de logits no contempla la excepción para la fase actual antes del verde mínimo, aunque el párrafo posterior sí la contempla.

- [ ] Formular primero una máscara binaria de admisibilidad y después aplicar el enmascaramiento a logits o valores Q. Incluir explícitamente que conservar la fase actual sigue siendo admisible cuando se impide cambiar de fase.
- [ ] Verificar el comportamiento durante amarillo y el reloj usado para habilitar cambios en E4 antes de fijar una ecuación temporal. No deducir la secuencia solo de los valores nominales de verde y amarillo.
- [ ] Separar el vector numérico observado por el actor del contenedor que transporta la máscara. Indicar orden de carriles, dimensiones por agente y si el índice de fase se normaliza o transforma antes de llegar a la red.
- [ ] Ajustar el texto de saturación: E3 devuelve directamente I−1 si x≥M; para x<M calcula, redondea y limita la salida. Declarar que la fórmula opera con valores numéricos expresados en segundos y revisar su interpretación dimensional.
- [ ] Reemplazar las referencias visuales ambiguas mediante F5 y F6, conservando físicamente los archivos anteriores.

**Cierre:** ecuación, ejemplo gráfico y comportamiento de E3–E4 coinciden, incluida la fase actual durante la restricción de cambio.

### C3. Recompensas: fórmula, evidencia y elección — prioridad alta

**Evidencia:** E5 implementa funciones, pero eso no acredita una comparación experimental entre ellas. `DiffAccWaitingTimeNormalizedReward` divide la diferencia de espera acumulada por `max(vehicle_count,1)`: no produce una cantidad adimensional. `PressureReward` devuelve el negativo del valor absoluto de la diferencia de vehículos detenidos entrantes y salientes.

- [ ] Presentar para cada alternativa fórmula, signo, población vehicular, unidad, comportamiento sin vehículos y referencia al método que la calcula. Separar presión y cola en filas distintas.
- [ ] Adoptar una convención uniforme para suma de tiempos individuales y media por vehículo; no alternar segundos, vehículo·segundo y unidades adimensionales sin explicar el agregado.
- [ ] Añadir una columna de evidencia: implementada, ensayada o seleccionada. Para «ensayada» exigir identificador de ejecución o notebook, configuración, escenario y métrica; si no se localiza, registrar «ensayo no acreditado en esta revisión».
- [ ] Justificar la señal final por su relación con la reducción de espera y la cooperación vecinal. Solo atribuir superioridad empírica si existe una comparación controlada que la sostenga.
- [ ] Explicar que una diferencia del stock de espera de vehículos presentes no equivale automáticamente a minimizar la espera total de todos los viajes: entradas, salidas y reasignación entre carriles afectan esa señal.

**Cierre:** la tabla no confunde disponibilidad con experimentación y la elección final tiene un fundamento explícito acorde con la evidencia.

### C4. Selección, poda y configuración final — prioridad alta

**Evidencia adicional de E9:** `rank_candidates` ordena por `metric_objective` y prioriza `tripinfo/eval_mean_waiting_time_inserted` como segunda clave; usa la espera de entrenamiento como alternativa cuando falta esa clave. La condición `value == value` detecta NaN, pero no descarta explícitamente infinitos. La rutina requiere métricas numéricas, no comprueba directamente los registros XML de TripInfo. Estas limitaciones son hallazgos de esa función, no una demostración de que los errores hayan ocurrido en los resultados.

- [ ] Documentar el desempate exacto y su fuente; retirar «empate práctico» si no existe tolerancia implementada.
- [ ] Separar el requisito científico de métricas finitas y TripInfo válido de las validaciones realmente ejecutadas. Registrar la comprobación explícita de infinitos y procedencia de métricas como mejora necesaria del pipeline, fuera de esta entrega documental.
- [ ] Distinguir candidato de hiperparámetros, receta y checkpoint de pesos. Definir antes de la evaluación final qué checkpoint se utiliza y con qué regla, evitando seleccionarlo sobre las semillas reservadas.
- [ ] Especificar presupuesto nominal y consumido, grace period y reduction factor de ASHA, pruebas podadas, ejecuciones fallidas, completadas y elegibles. Justificar cualquier ampliación de 100 a 150 pruebas con una regla anterior a los resultados.
- [ ] Mostrar que 40 iteraciones no implican necesariamente igual cantidad de muestras cuando cambia `train_batch_episodes`. Informar pasos de entorno y episodios, además del coste computacional.

**Cierre:** un lector puede reconstruir el ranking y la procedencia de cada modelo final sin elegir reglas adicionales.

### C5. Parámetros fijos y espacio de búsqueda — prioridad alta

- [ ] Construir T1 y T2 desde E7 y las configuraciones efectivas; verificar qué parámetros de RLlib quedan en valores predeterminados y registrar versiones exactas, no solo «2.x».
- [ ] Incluir `grad_clip ∈ {0,5; 1; 2; 5; 10}` para IDQN y aclarar que IPPO comparte el rango de 5 a 15 epochs con MAPPO. IDQN posee diez claves ajustables en E7, incluido el coeficiente vecinal.
- [ ] Expresar rangos enteros matemáticos con extremos incluidos y documentar aparte que `tune.randint` usa límite superior excluido: por ejemplo, `randint(4,65)` produce 4,…,64.
- [ ] Aclarar que I sí modifica la representación y se ajusta; por ello no es correcto afirmar que todas las decisiones de representación permanecen fijas. El valor de saturación y la métrica de carril son los elementos fijados.
- [ ] Para gamma, activaciones, arquitectura, optimizador y demás parámetros fijos pertinentes, distinguir evidencia bibliográfica de decisión propia. Registrar fuente, página/tabla, tarea estudiada y valor exacto antes de citarla como fundamento.
- [ ] No atribuir a un artículo de MAPPO o HAPPO un valor sin comprobar su configuración. A igualdad de gamma, explicar el paso temporal usado por este trabajo; no presentar 0,99 como óptimo universal.

**Cierre:** cada valor fijo tiene procedencia y cada dimensión ajustable tiene dominio, distribución y familia algorítmica.

### C6. Evaluación, métricas y estadística — prioridad alta

- [ ] Diferenciar semilla de entrenamiento, realización de demanda, semilla SUMO y episodio de evaluación. Verificar si las rutas contienen partidas ya materializadas o flujos estocásticos: cambiar la semilla SUMO no acredita por sí solo una demanda diferente.
- [ ] Definir la unidad experimental como modelo procedente de un entrenamiento independiente. Si cada modelo se evalúa varias veces, agregar primero por modelo o emplear un remuestreo que respete esa estructura. No tratar sus episodios como entrenamientos independientes.
- [ ] Mantener la confirmación pareada de cooperación separada de la comparación final entre los cuatro algoritmos. No atribuir a IPPO/IDQN una etapa que el ejecutor solo implemente para MAPPO/HAPPO.
- [ ] Precisar para cada métrica población, ventana, numerador, denominador y unidad. Distinguir vehículos insertados en la ventana, vehículos ya presentes tras el calentamiento y demanda aún pendiente de inserción.
- [ ] Explicar que registrar viajes inconclusos evita omitirlos, pero su espera al cierre sigue siendo parcial; no equivale a conocer el tiempo final de esos viajes. Acompañar siempre la espera de IR, CR y completitud de insertados.
- [ ] Definir el manejo de denominadores nulos: una mejora relativa respecto de cero debe informarse como no definida y acompañarse de diferencia absoluta. En tasas, distinguir variación relativa de cambio en puntos porcentuales. Definir también Gini cuando toda la espera sea cero.
- [ ] Mantener la espera física como resultado principal y la penalización temporal de HPO como diagnóstico separado. E10 suma la espera actual a la cola de incrementos recientes; no sustituye el primer término por la media de diez iteraciones. Con diez valores recientes existen hasta nueve incrementos.
- [ ] Declarar el número de réplicas efectivas junto a intervalos bootstrap. Veinte mil remuestreos no compensan una muestra pequeña. Identificar la «probabilidad de mejora» por su estimador concreto; no presentarla automáticamente como probabilidad posterior de superioridad.
- [ ] Documentar ejecuciones faltantes y exclusiones sin filtros post hoc por desempeño. Si se incorporan pruebas de significación, fijar contrastes y tratamiento de comparaciones múltiples previamente.

**Cierre:** las tablas y figuras se pueden calcular sin decisiones posteriores sobre población, agregación o selección.

### C7. Coherencia conceptual — prioridad alta

- [ ] Explicar el alcance de la notación Dec-POMDP cuando la implementación entrega recompensas individuales diferentes. Una intención cooperativa no basta para demostrar equivalencia con una recompensa común.
- [ ] Denominar observación conjunta a la concatenación de observaciones locales del crítico, salvo que se justifique que constituye un estado suficiente. No confundir acceso centralizado con observabilidad completa.
- [ ] Mantener explícita la adaptación de MAPPO/HAPPO y sus ventajas individuales; las garantías de una formulación con ventaja conjunta no se transfieren automáticamente.
- [ ] Sustituir la caracterización del corredor bidireccional como DAG por una descripción de corredor lineal, o definir y comprobar el grafo alternativo para el cual la propiedad sería cierta.

**Cierre:** no se atribuyen propiedades teóricas que el modelo implementado no haya justificado.

### C8. Escenarios, trazabilidad y edición — prioridad media

- [ ] Cambiar «Escenario Urbano Real» por «Escenario urbano de la Ciudad de Mendoza» y mantener visibles las limitaciones de los datos.
- [ ] Verificar con E12 las cifras de días válidos, medias, cobertura y reglas de filtrado. Resolver la relación entre exigir 100 % de intervalos y mencionar un umbral del 95 %.
- [ ] Trazar geometría, flujo nominal, pares OD, ceros, mezcla 60/40 y semillas a los archivos realmente consumidos por cada `.sumocfg`; no elegir por nombre o fecha sin verificar referencias.
- [ ] Distinguir la validación del acceso observado de una validación de toda la matriz OD. Mostrar el GEH solo con aforo, ventana, agregación y ruta compatibles, sin extender su alcance al tránsito completo de Mendoza.
- [ ] Aclarar que los programas fijos generados por SUMO no son necesariamente los planes semafóricos municipales. Documentar esta limitación del comparador.
- [ ] Retirar «la semilla histórica 42 queda prohibida» y la justificación ligada a «objetos no resueltos»; conservar la separación de semillas y el presupuesto por arquitectura con fundamento experimental.
- [ ] Eliminar la repetición de calibración sintética e introducir cada tabla antes de presentarla. Usar minúsculas en «figura», «tabla» y «sección» dentro de una oración.
- [ ] Llevar rutas extensas, versiones internas como «contrato v14», reintentos, puertos y detalles de clúster al apéndice cuando no expliquen una decisión metodológica. Conservar en el cuerpo tiempos, métricas y supuestos necesarios para reproducir el experimento.

## 4. Programa de figuras

### Criterio común de producción

Las figuras deben responder una pregunta del lector, derivarse de datos o procedimientos identificables y conservar fuentes editables. Usar diagramas vectoriales con TikZ y gráficos reproducibles con Matplotlib; extraer mapas de redes mediante SUMO/sumolib y coordenadas verificadas. No usar imágenes generativas para representar geometría, resultados o funciones matemáticas.

Guardar los PDF finales en `imagenes/`; conservar el script o fuente editable y un registro de entradas, parámetros y versiones. Todos los nombres siguientes son **destinos propuestos**, no archivos ya creados. Emplear español, unidades explícitas, colores distinguibles en escala de grises y tipografía legible al ancho final. Los mapas deben atribuir sus datos y declarar escala; las capturas de terceros requieren revisar las condiciones de uso.

La prioridad «esencial» señala una necesidad explicativa, no obliga a reservar una página por figura. Se admiten paneles para evitar repetición. No borrar los binarios actuales al reemplazar referencias.

### F0. Flujo metodológico general — conservar y corregir

- **Pregunta:** ¿cuál es la secuencia completa del estudio?
- **Ubicación:** enfoque y diseño de investigación; conservar `fig:flujo_metodologico_general` y su TikZ actual.
- **Contenido:** escenarios → modelado → integración → algoritmos → HPO → entrenamiento/confirmación → evaluación. Representar la infraestructura como soporte si no constituye una etapa temporal; incluir HPO propio de Mendoza.
- **Fuente y herramienta:** protocolo autorizado, E1 y E8; TikZ existente.
- **Pie propuesto:** «Etapas del diseño experimental y dependencia entre la construcción de escenarios, el aprendizaje y la evaluación».
- **Aceptación:** no llama retorno a la espera física ni presenta etapas futuras como completadas; F8 desarrolla la selección sin duplicar todo el flujo.

### F1. Comparación de redes sintéticas — esencial

- **Pregunta:** ¿qué cambia espacialmente entre 3x1, 3x3 y 4x4_H?
- **Ubicación:** escenarios sintéticos, inmediatamente después de introducir su tabla descriptiva.
- **Contenido:** tres paneles con nodos semaforizados, direcciones de circulación, accesos y número de carriles donde difiera. Usar escala propia declarada por panel, sin sugerir igualdad de dimensiones.
- **Fuente:** redes `.net.xml` referenciadas por las configuraciones de campaña de los tres escenarios; excluir conexiones internas del conteo cuando esa sea la convención de la tabla.
- **Herramienta y salida:** sumolib + Matplotlib, `imagenes/met_escenarios_sinteticos.pdf`; `fig:met_escenarios_sinteticos`.
- **Pie propuesto:** «Topologías de los escenarios sintéticos y localización de sus intersecciones controladas. Las flechas indican los sentidos de circulación».
- **Aceptación:** cantidades de agentes y convenciones de conteo coinciden con la tabla; las diferencias de 4x4_H se perciben sin depender solo del color.

### F2. Mendoza: geometría y cobertura observada — esencial

- **Pregunta:** ¿qué parte de la red se representa y dónde existe información observada?
- **Ubicación:** modelado geoespacial de Mendoza.
- **Contenido:** panel general con perímetro, norte, escala, arterias y agentes; detalle del acceso oriental con cámara 169, dirección observada y enlace de inyección. Diferenciar ubicación física y representación de entrada; no ubicar la cámara artificialmente dentro del dominio.
- **Fuente:** red activa de Mendoza, coordenadas y mapeo contrastados con E12; resolver la red desde `.sumocfg` porque existen varias versiones.
- **Herramienta y salida:** sumolib/transformación de coordenadas + Matplotlib; `imagenes/met_mendoza_cobertura.pdf`; `fig:met_mendoza_cobertura`.
- **Pie propuesto:** «Red modelada de la Ciudad de Mendoza y localización del aforo utilizado para construir la demanda. El enlace de inyección representa el ingreso observado hacia el oeste».
- **Aceptación:** proyección, cámara y enlace son verificables; leyenda explícita: el aforo no cubre la demanda completa de la red.

### F3. Construcción de demanda de Mendoza — esencial

- **Pregunta:** ¿cómo se pasa de un aforo parcial a las rutas simuladas?
- **Ubicación:** después de presentar la posición metodológica y antes del detalle OD.
- **Contenido:** aforo → depuración → perfil temporal; cartografía/conectividad → zonas y pares alcanzables; volumen nominal y supuestos de distribución → combinación OD → generación de rutas → controles operacionales. Distinguir datos, supuestos y transformaciones mediante formas o tipos de borde.
- **Fuente:** E12 y scripts/configuraciones efectivamente referenciados; comprobar allí la mezcla 60/40 antes de rotularla.
- **Herramienta y salida:** TikZ, `imagenes/met_mendoza_demanda.pdf`; `fig:met_mendoza_demanda`.
- **Pie propuesto:** «Construcción de la demanda modelada a partir del perfil observado, la conectividad vial y los supuestos de distribución espacial».
- **Aceptación:** ningún supuesto se presenta como medición; los controles de un acceso y de la red se distinguen.

### F4. Perfil temporal del aforo y demanda modelada — esencial

- **Pregunta:** ¿qué variación temporal está observada y cuál resulta de la expansión?
- **Ubicación:** perfil temporal y factor territorial.
- **Contenido:** panel observado con media por intervalo de 15 minutos y banda de desviación estándar entre días completos válidos; indicar número de días. Panel separado para la demanda expandida y ventanas de simulación. Rotular veh/15 min, o convertir explícitamente a veh/h; usar hora local verificada.
- **Fuente:** registros depurados de cámara 169 y procedimiento reproducible de E12. Si no están accesibles los datos, mantener la figura pendiente, sin reconstruirla a partir de cifras narradas.
- **Herramienta y salida:** Matplotlib, `imagenes/met_mendoza_perfil.pdf`; `fig:met_mendoza_perfil`.
- **Pie propuesto:** «Perfil temporal del aforo disponible y demanda temporal adoptada para la simulación. La banda del panel observado representa variabilidad entre días, no incertidumbre del tráfico total de la ciudad».
- **Aceptación:** volumen integrado y días válidos coinciden con los cálculos; las ventanas se obtienen de las configuraciones y ambos paneles distinguen observación de modelado.

### F5. Intersección, vector de observación y acciones — esencial

- **Pregunta:** ¿qué información de una intersección recibe el agente y qué puede decidir?
- **Ubicación:** observaciones y acciones, referenciada desde ambas subsecciones.
- **Contenido:** una intersección de la red 3x1 con carriles identificados; espera por carril → e(x) → vector con fase; mostrar por separado la máscara. Añadir las fases seleccionables con sus movimientos compatibles y un ejemplo de fase actual única admisible.
- **Fuente:** E3–E4 y conexiones de la intersección elegida; declarar el ID del nodo en el pie. Los números de espera del ejemplo serán didácticos, etiquetados como tales.
- **Herramienta y salida:** TikZ, `imagenes/met_observacion_accion.pdf`; `fig:met_observacion_accion`.
- **Pie propuesto:** «Construcción de la observación local y conjunto de acciones admisibles en una intersección del escenario 3x1. Los valores numéricos ilustran el procedimiento».
- **Aceptación:** dimensiones, orden de carriles, fases y formato coinciden con el entorno; no se concatena información vecinal al actor si la configuración la desactiva.

### F6. Codificación logarítmica-lineal reproducible — esencial; sustituye dos ilustraciones ambiguas

- **Problema actual:** `LaneInfoEncoding.png` muestra una curva, no el armado de un vector. `log_linear_blend_1.png` muestra I=6 con salida hasta 6; la implementación actual usa I−1. No reutilizar esas imágenes sin ajustar su interpretación.
- **Pregunta:** ¿cómo afectan la discretización y la saturación a la espera observada?
- **Ubicación:** después de la fórmula de Encoder; el armado del vector corresponde a F5.
- **Contenido:** dos paneles calculados mediante E3, para I=8 e I=32 y M=1184 s, declarado como ejemplo con la cota citada para 3x1, no como hiperparámetro ganador. Eje x de 0 a 1,2M; indicar M y el máximo I−1. Graficar la salida discreta real; si se añade la expresión continua previa al redondeo, identificarla expresamente.
- **Herramienta y salida:** Matplotlib llamando a Encoder, `imagenes/met_encoder.pdf`; `fig:met_encoder`.
- **Pie propuesto:** «Discretización de la espera por carril para dos resoluciones ilustrativas. El codificador limita la salida al índice I−1 al alcanzar la cota M».
- **Aceptación:** verificar e(0)=0, e(M)=I−1, e(x>M)=I−1, salida entera acotada y monotonía para los parámetros dibujados. No atribuir a estas comprobaciones una prueba para cualquier parámetro.

### F7. Integración SUMO–agentes y aprendizaje — esencial

- **Pregunta:** ¿dónde se calcula cada cantidad y cómo difieren las implementaciones?
- **Ubicación:** arquitectura de integración, con referencia posterior desde implementación algorítmica.
- **Contenido:** SUMO ↔ entorno mediante TraCI/libsumo; entorno entrega observación y máscara a actores y calcula recompensas locales/vecinales. Panel de entrenamiento con observación conjunta → crítico multi-salida en MAPPO/HAPPO; señalar actualización secuencial de HAPPO. Representar IPPO/IDQN como módulos independientes y separar evaluación sin actualización.
- **Fuente:** E4–E6 y módulos/learners activos; verificar las flechas antes de dibujar para no atribuir comunicación directa entre actores.
- **Herramienta y salida:** TikZ, `imagenes/met_integracion_aprendizaje.pdf`; `fig:met_integracion_aprendizaje`.
- **Pie propuesto:** «Intercambio de información entre el simulador, el entorno y los módulos de aprendizaje. El crítico centralizado se utiliza durante el entrenamiento de las variantes correspondientes».
- **Aceptación:** la recompensa sigue siendo un vector individual; las ventajas individuales y adaptación de HAPPO no se reemplazan gráficamente por una ventaja conjunta canónica.

### F8. Selección experimental y evaluación reservada — esencial

- **Pregunta:** ¿qué datos se utilizan para ajustar, seleccionar y evaluar?
- **Ubicación:** final de HPO, antes de evaluación.
- **Contenido:** estudios separados por algoritmo/escenario/arquitectura → candidatos elegibles → selección de receta → entrenamiento/confirmación aplicable → configuración y checkpoint finales → evaluación reservada. Incluir los cuatro escenarios y algoritmos; anotar como pendiente el presupuesto de Mendoza si continúa sin fijarse.
- **Fuente:** E7–E11 y decisión del autor sobre Mendoza.
- **Herramienta y salida:** TikZ, `imagenes/met_hpo_evaluacion.pdf`; `fig:met_hpo_evaluacion`.
- **Pie propuesto:** «Separación de la búsqueda, la selección y la evaluación final por algoritmo y escenario. Las semillas reservadas no intervienen en decisiones de ajuste».
- **Aceptación:** no hay flecha de realimentación desde evaluación final a HPO ni transferencia de pesos entre escenarios; la confirmación de cooperación se identifica solo donde corresponda.

### F9. Cronograma de decisión y transición — complementaria

- **Pregunta:** ¿cómo se relacionan paso de decisión, amarillo y verde mínimo?
- **Ubicación:** ciclo episódico o acciones; si F5 basta para explicar la admisibilidad, llevar al apéndice.
- **Contenido:** secuencia de mantener fase, solicitar cambio, amarillo y nuevo verde, con reloj y máscara. Construir desde una traza verificable de E4, no colocar duraciones sumando supuestos.
- **Herramienta y salida:** TikZ; `imagenes/met_cronograma_semaforo.pdf`; `fig:met_cronograma_semaforo`.
- **Pie propuesto:** «Secuencia ilustrativa de decisiones, transiciones y habilitación de acciones según el entorno implementado».
- **Aceptación:** tiempos y estados coinciden con la traza; la figura no ofrece una garantía de seguridad vial fuera de la simulación.

### F10. Distribución espacial OD de Mendoza — complementaria

- **Pregunta:** ¿cómo se distribuye espacialmente la demanda supuesta?
- **Ubicación:** estructuración OD o apéndice de escenarios.
- **Contenido:** matriz origen-destino ordenada por zonas, con barra de escala y distinción entre pares inalcanzables y pares alcanzables de peso cero; mapa pequeño de zonas para interpretar los ejes. Preferir matriz a cientos de flechas superpuestas.
- **Fuente:** archivo OD activo y conectividad de la red referenciada en la campaña.
- **Herramienta y salida:** Matplotlib, `imagenes/met_mendoza_od.pdf`; `fig:met_mendoza_od`.
- **Pie propuesto:** «Pesos de la demanda OD modelada para Mendoza. Los valores representan una asignación adoptada, no una matriz completa observada».
- **Aceptación:** suma, normalización, ceros y pares alcanzables concuerdan con las entradas del generador; no incluir rótulos ilegibles.

## 5. Tablas y figuras para los resultados

### Tablas metodológicas

| ID | Tabla propuesta | Campos mínimos y condición de cierre |
|---|---|---|
| T1 | Parámetros fijados antes de HPO | Parámetro, valor/unidad, algoritmos, origen en configuración, fundamento bibliográfico o decisión propia. Incluir tiempos del entorno por escenario y evitar atribuirlos a una misma fuente genérica. |
| T2 | Espacio de búsqueda | Parámetro, significado, distribución, dominio inclusivo y algoritmo. Separar familia PPO de IDQN; incluir dimensiones que hoy faltan. |
| T3 | Presupuesto y semillas | Escenario, algoritmo, arquitectura, pruebas, interacción máxima, poda, réplicas de entrenamiento y evaluación; estado previsto/configurado/ejecutado. Presupuesto Mendoza pendiente hasta fijación. |
| T4 | Configuración final | Escenario, algoritmo, arquitectura, parámetros, valor objetivo, estudio/trial, regla de checkpoint y manifiesto. Completar exclusivamente desde recetas y resultados verificables. |
| T5 | Métricas operacionales | Nombre, fórmula, población, ventana, unidad, dirección favorable, fuente, agregado entre réplicas y caso de denominador cero. |
| T6 | Procedencia de escenarios y calibración | Red/rutas, herramientas y versiones, ventana, demanda, controlador fijo, métrica de calibración y evidencia. Separar aforos, supuestos y parámetros derivados. |

### Gráficos del capítulo de resultados

Estos gráficos se especifican ahora y se producirán cuando existan resultados compatibles. No se incorporarán curvas o valores ficticios para llenar el capítulo.

- **R1. Aprendizaje por presupuesto:** eje x en pasos de entorno acumulados, eje y en espera física de evaluación; panel por escenario y curva por algoritmo, con agregación entre entrenamientos independientes. Informar cantidad de réplicas y cobertura en cada punto; si las evaluaciones no coinciden temporalmente, usar una regla de alineación declarada. No comparar recompensas de distinta escala como si fueran desempeño vehicular equivalente.
- **R2. Comparación final:** puntos por entrenamiento independiente, después de agregar sus episodios de evaluación según el protocolo; media e intervalo del 95 %, más línea base fija. Presentar espera y completitud en paneles separados, con unidad y tamaño de muestra. Preferir puntos e intervalos a barras que oculten variabilidad.
- **R3. Diferencias pareadas de cooperación:** candidato menos ancla local por semilla, línea de cero e intervalo pareado, para las familias que implementan ese contraste. No extender automáticamente ese pareamiento a otros algoritmos o escenarios.
- **R4. Equidad espacial:** mapa de espera media por intersección y distribución por nodo para fijo, MAPPO, HAPPO, IPPO e IDQN dentro del mismo escenario. Usar escala común y definir población y agregado; no confundir diferencias estructurales de demanda entre nodos con evidencia suficiente de injusticia del controlador.

## 6. Investigación bibliográfica dirigida

La búsqueda debe responder afirmaciones concretas: selección de métricas, valores fijos, modelado de observaciones y convenciones visuales. Verificar autores, título, año, DOI cuando exista y alcance antes de incorporar nuevas citas. Priorizar fuentes recientes pertinentes; conservar antecedentes anteriores cuando su relación directa justifique su uso. No agregar bibliografía solo por actualidad o cantidad.

### Antecedente visual comprobado

James Ault y Guni Sharon, *Reinforcement Learning Benchmarks for Traffic Signal Control*, NeurIPS Datasets and Benchmarks, 2021 (RESCO). La figura 1 del artículo muestra movimientos/fases de una intersección; el repositorio oficial ofrece además un recurso de mapas de escenarios. Esto respalda usar esquemas de intersecciones y mapas comparables como referencias de presentación. No implica que RESCO utilice las arquitecturas, el codificador o las recompensas de este trabajo.

- [Publicación oficial y metadatos](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/f0935e4cd5920aa6c7c996a5ee53a70f-Abstract-round1.html).
- [Artículo completo](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/f0935e4cd5920aa6c7c996a5ee53a70f-Paper-round1.pdf).
- [Repositorio oficial y mapas](https://github.com/Pi-Star-Lab/RESCO).

Su inclusión aquí se justifica por ser un benchmark directamente dedicado a comparar controladores RL de tránsito. Es una referencia visual verificada, no una revisión exhaustiva de figuras «clásicas». Antes de cerrar la investigación, contrastar al menos un segundo trabajo comparable con su texto completo; no atribuir números de figura basados solo en resúmenes o resultados de búsqueda.

### Comprobaciones bibliográficas por completar

- [ ] Revisar las publicaciones originales ya citadas de MAPPO y HAPPO y sus configuraciones experimentales para sustentar valores concretos, separando convenciones de resultados empíricos.
- [ ] Revisar un trabajo adicional de MARL semafórico con figuras de arquitectura y coordinación; CoLight es un candidato identificado, no una equivalencia metodológica: su comunicación por atención no representa el crítico o la recompensa de este proyecto.
- [ ] Contrastar las definiciones de `waitingTime`, `timeLoss`, viajes inconclusos y contadores con documentación oficial de la versión SUMO utilizada; reemplazar citas generales por secciones específicas cuando sea necesario.
- [ ] Buscar evidencia sobre métricas y evaluación con pocas semillas en RL; justificar el análisis escogido sin atribuir al bootstrap garantías que no tiene.
- [ ] Registrar para cada incorporación la afirmación exacta que sostiene, página/tabla/figura y clave canónica de `bibliografia.bib`. Las entradas nuevas deberán ser compatibles con BibTeX clásico e incluir `language = {spanish}`.

## 7. Orden de incorporación y criterios de aceptación

### Estado posterior a la corrección sin figuras

En esta pasada se corrigió el texto de `5-metodologia.tex` sin crear ni reemplazar figuras. Se incorporó el ajuste independiente de MAPPO, HAPPO, IPPO e IDQN para Mendoza; se eliminó la caracterización del corredor 3x1 como DAG; se aclaró que los programas fijos son una línea base computacional; se ajustaron el criterio de días completos y la descripción de la demanda OD; se reformuló la coordinación como recompensa individual con componente vecinal; se corrigieron la ecuación y la explicación de `action masking`; se alinearon las unidades de las recompensas; se separaron señales implementadas de señales experimentalmente acreditadas; y se precisaron la selección de candidatos, el checkpoint, la unidad experimental, los denominadores y la interpretación del bootstrap.

La compilación posterior con `latexmk` produjo el PDF sin errores, citas indefinidas ni referencias indefinidas. Permanece el aviso de `tracklang` ya conocido y el `Overfull \\hbox` preexistente del glosario. La selección de candidatos del repositorio experimental todavía debe sincronizarse con la comprobación explícita de infinitos y con la campaña propia de Mendoza; la presente edición documenta el criterio metodológico, pero no ejecuta campañas ni modifica ese repositorio.

1. Corregir las contradicciones de Mendoza, máscara, recompensas y selección; completar el contrato experimental aún pendiente. No iniciar la evaluación final con reglas de selección abiertas.
2. Preparar T1–T6 y resolver las comprobaciones bibliográficas. Marcar valores desconocidos como pendientes; no inferir configuraciones ganadoras de resultados históricos no compatibles.
3. Producir primero F1, F2, F5, F6 y F8; continuar con F3, F4 y F7. Conservar F0 corregida. Incorporar F9–F10 solo cuando aporten explicación adicional o colocarlas en el apéndice.
4. Revisar orden pedagógico, terminología, referencias cruzadas y el límite entre teoría, metodología y resultados. Mantener los snapshots teóricos y las figuras previas físicamente intactos.
5. Al integrar cambios LaTeX, ejecutar `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`; si cambia el glosario, ejecutar también `makeglossaries main`. Inspeccionar el registro y las páginas afectadas, sin borrar artefactos versionados.

### Cierre del documento de revisión

- [x] Los 14 requisitos originales tienen estado, evidencia y condición de cierre.
- [x] La decisión del autor sobre HPO propio de Mendoza está registrada.
- [x] Se distingue esta entrega documental de la incorporación futura de correcciones y figuras.
- [x] Cada figura propuesta tiene pregunta, ubicación, contenido, fuente, herramienta, destino, pie e inspección de aceptación.
- [x] Los resultados y decisiones pendientes se identifican sin inventar valores ni dar por concluidas campañas.

### Cierre posterior del capítulo

- [ ] Resolver C1–C8 o justificar expresamente cada pendiente experimental.
- [ ] Incorporar las figuras esenciales con fuentes reproducibles, citas y descripciones coincidentes.
- [ ] Completar la evidencia de recompensas probadas y los fundamentos de parámetros fijos.
- [ ] Vincular recetas y resultados finales con sus manifiestos cuando estén disponibles.
- [ ] Obtener una compilación sin nuevas citas/referencias indefinidas ni desbordamientos y comprobar la diagramación en el PDF. La advertencia externa conocida de `tracklang` no constituye un error de contenido.

La verificación de este documento es documental; no exige compilar la tesina porque su creación no cambia las fuentes LaTeX. La revisión de fuentes y figuras no certifica por sí misma el funcionamiento integral de las campañas experimentales.
