# Informe de acciones recomendadas para la metodología

Fecha: 13 de octubre de 2026.

Base de revisión: `464b9121a657e1ab0c2f47e5d1b4f11bbd455e13` y modificaciones locales presentes al preparar este informe. Las ubicaciones corresponden a esa copia de trabajo; pueden desplazarse después de editar.

## Alcance y diagnóstico

La metodología actual es una mejor base que las primeras versiones del período revisado. Explica con mayor precisión las observaciones, las recompensas, las implementaciones algorítmicas y las unidades de evaluación. Conviene conservar su organización general y realizar ajustes acotados, principalmente en la orientación del lector, las dependencias entre etapas y la presentación de las métricas.

Este informe reúne las acciones recomendadas sobre `5-metodologia.tex` y su relación con el marco teórico, la introducción, el resumen, el apéndice y las figuras. Resultados y Conclusiones quedan fuera de la revisión: están en elaboración y su desarrollo pendiente no constituye una objeción al método. Las acciones descritas aquí son propuestas; no se aplicaron al manuscrito.

Las prioridades expresan el orden de intervención. **P1** identifica ambigüedades que afectan la comprensión del procedimiento; **P2**, mejoras de exposición y lectura; **P3**, coordinación formal y verificación. Las acciones que requieren evidencia deben resolverse consultando las configuraciones o el código correspondiente, sin completar los datos por analogía ni convertir una intención en una ejecución acreditada.

| Grupo | Acciones | Propósito |
|---|---|---|
| Estructura y recorrido | A01–A05 | Aclarar la tarea, las dos líneas experimentales y sus dependencias. |
| Escenarios y control | A06–A10 | Conectar la construcción de escenarios con el sistema de aprendizaje. |
| Búsqueda y selección | A11–A15 | Precisar qué datos alimentan cada decisión y qué producto obtiene cada etapa. |
| Comparación y evaluación | A16–A21 | Facilitar la lectura de las variantes, las métricas y el análisis. |
| Coordinación y validación | A22–A25 | Mantener consistencia entre texto, glosario, figuras y apéndice. |

## Estructura y recorrido del capítulo

### A01. Distribuir la información de la apertura — P2

**Ubicación:** `5-metodologia.tex:5`, apertura del capítulo.

El primer párrafo reúne la tarea del agente, la geometría, la demanda, las escalas de evaluación, los cuatro algoritmos y la motivación de HAPPO. Aunque sus afirmaciones son pertinentes, exige retener demasiados asuntos antes de conocer el recorrido.

Recomiendo separar la presentación de la tarea de la justificación algorítmica. Primero explicar qué recibe el sistema, qué decide y qué se busca obtener; después presentar los procedimientos comparados y la motivación asociada a la heterogeneidad. El párrafo siguiente puede conservar la distinción entre las dos líneas experimentales. Evitar repetir allí todas las métricas o adelantar las letras A y C antes de que resulten necesarias.

**Criterio de cierre:** al terminar la apertura, el lector puede explicar qué controla cada agente, cuál es el objetivo operacional y cuáles son las dos preguntas del diseño.

### A02. Explicitar qué pregunta responde cada línea experimental — P1

**Ubicación:** `5-metodologia.tex:7` y `5-metodologia.tex:16`.

La separación entre comparación de procedimientos completos y contraste local/vecinal está bien planteada. Falta presentar con igual claridad qué permanece fijo, qué cambia y cuál es el producto de cada línea.

Recomiendo formular una pregunta por línea y agregar una tabla breve con cuatro columnas: pregunta, elementos comparados, condiciones comunes y producto. En la primera, distinguir configuraciones seleccionadas de modelos reentrenados; en la segunda, identificar el contraste conjunto de observación y recompensa bajo una configuración de aprendizaje fija. La tabla debe sustituir parte de la enumeración actual, para no aumentar innecesariamente la extensión.

**Criterio de cierre:** el lector comprende por qué ambas líneas pueden coexistir y por qué A/C no responde la comparación de los cuatro algoritmos ni separa el efecto de observación y recompensa.

### A03. Uniformar la redacción del protocolo y de las ejecuciones descritas — P1

**Ubicación:** diseño experimental; `5-metodologia.tex:430`, `5-metodologia.tex:445`, `5-metodologia.tex:581`; `4-marco_teorico.tex:1589`.

No recomiendo recuperar automáticamente una tabla de avance. El objetivo es que el método se entienda sin convertir el capítulo en un informe de seguimiento.

Recomiendo introducir una convención breve: el presente describe reglas del procedimiento; el pasado identifica ejecuciones concretas que se documentan. Revisar después expresiones como «la fase 1 realiza» y «se realizan veinte simulaciones» para que su antecedente indique si se expone un protocolo o una campaña determinada. Si se necesita precisar la ejecución de alguna etapa, hacerlo una sola vez, con su respaldo documental. Coordinar la frase del marco teórico que anuncia una distinción entre campañas y protocolos con lo que efectivamente presente la metodología.

**Criterio de cierre:** una regla de evaluación no se interpreta como prueba de que todas sus simulaciones ya se realizaron. Esta acción no depende de que Resultados esté terminado.

### A04. Completar la rama A/C del diagrama de flujo — P1

**Ubicación:** `imagenes/metodologia_v2_flujo.tex` y su presentación y epígrafe en `5-metodologia.tex:22`.

El flujo de búsqueda y selección es legible, pero A–E y A/C aparecen en una caja sin conexiones. Esa disposición expresa separación, aunque no explica sus entradas ni sus productos.

Recomiendo mostrar dos recorridos desde los escenarios preparados. El primero conserva búsqueda amplia, búsqueda refinada, selección, reentrenamiento y evaluación. El segundo distingue la prueba preliminar y la comparación A/C, e incluye entrenamiento, evaluación y análisis por pares. Si el espacio resulta insuficiente, mostrar solo sus etapas principales y remitir al diagrama específico del análisis pareado. Situar la comprobación operacional urbana dentro de la preparación del escenario. Las flechas deben representar dependencias; no añadir una flecha desde A/C hacia la selección de HPO sin evidencia de esa dependencia.

**Criterio de cierre:** cada rama tiene una entrada y un producto comprensibles, y el epígrafe coincide con las flechas dibujadas. La configuración fija de A/C debe quedar identificada como entrada; su procedencia histórica puede explicarse en el texto.

### A05. Reforzar las transiciones mediante los productos de las etapas — P2

**Ubicación:** cierres de Escenarios, Sistema de control, Búsqueda y Comparación local/vecinal.

Recomiendo revisar esos cierres para conectar el producto obtenido con su uso siguiente: red y demanda alimentan el entorno; observaciones, acciones y recompensas definen la interacción; la búsqueda aporta candidatos; la selección aporta una configuración; el reentrenamiento produce una política evaluable. Agregar una oración de enlace únicamente donde la relación no sea evidente.

**Criterio de cierre:** la exposición avanza por dependencias del método y evita cerrar secciones con anuncios que solo repiten títulos.

## Escenarios y sistema de control

### A06. Orientar la lectura del desarrollo de Mendoza — P2

**Ubicación:** `5-metodologia.tex:141` y cierre de la subsección urbana.

La construcción urbana introduce datos parciales, geometría, expansión del perfil, distribución OD y comprobación operacional. Ese desarrollo es necesario, pero puede hacer perder de vista su función en el estudio.

Recomiendo anticipar en dos oraciones el recorrido: los conteos aportan un perfil temporal, los supuestos completan la demanda espacial y nominal, y la red y las rutas resultantes constituyen entradas de simulación. Al cerrar, explicar qué queda preparado para el control y bajo qué supuestos. Esta síntesis debe conservar la diferencia entre la comprobación histórica y las configuraciones de aprendizaje.

**Criterio de cierre:** el lector entiende qué aporta Mendoza al método y por qué sus conteos parciales no identifican la demanda total de la ciudad.

### A07. Mantener una explicación central de la procedencia urbana — P2

**Ubicación:** `5-metodologia.tex:151`, `5-metodologia.tex:185`, `5-metodologia.tex:204`, `5-metodologia.tex:221`; `8-apendice_arquitectura.tex:280`.

Recomiendo concentrar la comparación detallada de versiones en las tablas y explicaciones del apéndice. En el cuerpo, conservar junto a cada decisión la limitación necesaria para interpretarla: el volumen diario es nominal; la regla 60/40 y el registro 70/30 describen especificaciones diferentes; no está acreditada la identidad de las rutas históricas mediante el hash del archivo congelado.

Reducir las reiteraciones documentales extensas mediante remisiones precisas. Mantener separados los perfiles de 33 y 32 días, los volúmenes de 290.000 y 260.000 vehículos diarios y los valores de `camera_retention`. Esta propuesta ordena la información y no autoriza a unificar esas versiones.

**Criterio de cierre:** las limitaciones necesarias permanecen en el cuerpo y la reconstrucción detallada tiene una ubicación central en el apéndice.

### A08. Identificar las especificaciones propias de la búsqueda urbana — P1; requiere evidencia

**Ubicación:** `5-metodologia.tex:376`, fases 1 y 2; `8-apendice_arquitectura.tex:607`.

El diseño incluye ambas fases en Mendoza, pero las tablas detalladas corresponden a las redes sintéticas. Recomiendo comprobar qué especificaciones urbanas están efectivamente definidas e identificar su fuente: dominios, arquitecturas, presupuesto, semillas y condiciones particulares. Si ya existen, resumirlas en el apéndice y enlazarlas desde las fases correspondientes. Si alguna permanece por definir, distinguir ese componente del protocolo ya especificado.

No es necesario cerrar una campaña ni presentar sus resultados para documentar un protocolo. Tampoco debe inferirse una ejecución a partir de la existencia de una configuración.

**Criterio de cierre:** el lector puede localizar la especificación urbana o reconocer con precisión qué elemento del diseño sigue pendiente, sin trasladar valores sintéticos.

### A09. Explicar la diferencia entre programas de referencia y control aprendido — P2

**Ubicación:** `5-metodologia.tex:39`, `5-metodologia.tex:61`, `5-metodologia.tex:230`, `5-metodologia.tex:398`.

Las duraciones nominales de los programas de referencia y las reglas temporales del entorno aprendido aparecen en apartados distintos. Recomiendo añadir una conexión breve que explique sus funciones: los primeros describen la operación de referencia; durante el control aprendido el agente solicita fases bajo la máscara y las restricciones temporales del entorno. Conservar la diferencia entre los amarillos de referencia y el amarillo configurado para las campañas de aprendizaje.

**Criterio de cierre:** el lector no interpreta que las barras de ciclos de 90 segundos describen necesariamente la ejecución de una política aprendida. En Mendoza debe conservarse la distinción entre programas fijos y accionados.

### A10. Ordenar la presentación de observación, codificador y recompensa — P2

**Ubicación:** `5-metodologia.tex:258`, `5-metodologia.tex:272`, `5-metodologia.tex:298`.

Recomiendo mantener el siguiente orden conceptual: medida de espera atribuida al carril, vector recibido por el agente, transformación que codifica esa medida, extensión vecinal y uso del cambio de espera en la recompensa. Revisar las transiciones para que quede claro que codificar la observación y calcular la recompensa son operaciones diferentes.

Conservar en el cuerpo la memoria temporal finita, la posible subestimación de atribuciones, el redondeo hacia arriba, la saturación y la dependencia de la transformación respecto de los niveles. El desarrollo algebraico extenso puede seguir en el apéndice. No cambiar los parámetros ilustrativos para hacerlos coincidir artificialmente con A/C.

**Criterio de cierre:** el lector distingue la magnitud medida, su representación y la señal de aprendizaje, sin atribuir a la codificación una mejora que no fue evaluada por separado.

## Búsqueda, implementación y selección

### A11. Coordinar la formulación teórica con la implementación concreta — P1

**Ubicación:** `5-metodologia.tex:345`, `5-metodologia.tex:356`; marco teórico de HAPPO; `8-apendice_arquitectura.tex:670`.

Recomiendo presentar explícitamente la secuencia «formulación de referencia → adaptación utilizada → alcance». Mantener la explicación de recompensas individuales, valores por agente y crítico centralizado de múltiples salidas. En el apéndice, revisar «Estas reglas caracterizan el procedimiento de HAPPO»: resulta más preciso identificar las reglas de la implementación inspeccionada, porque la tesina utiliza una adaptación.

Conservar la diferencia entre la descomposición teórica de una ventaja conjunta y las ventajas calculadas con recompensas específicas. Mantener la precisión reciente sobre HAML; no reducirla a una afirmación general de ausencia de garantías para todo HAPPO.

**Criterio de cierre:** las propiedades de la teoría y del código se distinguen, y la heterogeneidad no se presenta como una ventaja demostrada de antemano.

### A12. Precisar de dónde provienen las mediciones del objetivo de HPO — P1; requiere evidencia

**Ubicación:** `5-metodologia.tex:407` y Seguimiento diagnóstico.

El texto diferencia el historial del objetivo de los episodios diagnósticos, pero no deja completamente visible qué ejecución produce cada `w_r` ni cómo se agrega antes de incorporarse al historial.

Recomiendo consultar el programa y los callbacks de la versión pertinente y explicitar la procedencia: episodio de entrenamiento, agregado de episodios u otra medición; frecuencia de registro; y significado de «medición válida». Aclarar qué pasa cuando todavía no hay historial suficiente para producir una puntuación utilizable, si ese comportamiento está definido en el código. Distinguir los cinco registros descartados del calentamiento temporal.

**Criterio de cierre:** el lector puede seguir el recorrido desde TripInfo hasta `w_r`, la penalización y el objetivo, sin confundirlo con el seguimiento diagnóstico.

### A13. Hacer visible el presupuesto de la búsqueda refinada — P2; requiere cotejo documental

**Ubicación:** `5-metodologia.tex:445`, `5-metodologia.tex:465`; `8-apendice_arquitectura.tex:557`, `8-apendice_arquitectura.tex:594`.

La selección exige 60 iteraciones, mientras que el apartado de fase 2 remite varios parámetros al apéndice. Recomiendo verificar y presentar juntos el máximo de iteraciones por ensayo, el presupuesto de propuestas y la gracia de ASHA. El requisito de admisibilidad no debe ser la única vía para descubrir la duración completa de un ensayo.

Conservar la advertencia sobre la herencia de dominios al cambiar la recompensa y distinguir la búsqueda refinada de la confirmación histórica de MAPPO/HAPPO. No interpretar los presupuestos declarados como cantidades completadas.

**Criterio de cierre:** se comprende qué presupuesto se asigna, qué puede detener ASHA y qué duración se exige al candidato seleccionado.

### A14. Separar los distintos sentidos de «referencia» en la selección — P2

**Ubicación:** `5-metodologia.tex:467`; `8-apendice_arquitectura.tex:596`.

En pocos renglones aparecen una configuración construida con los mejores ensayos históricos y una referencia empírica de inserciones. Además, Mendoza utiliza programas semafóricos de referencia. Recomiendo adoptar denominaciones completas y estables: «configuración de referencia derivada de fase 1», «referencia de inserciones» y «programas semafóricos de referencia».

Dividir el párrafo de selección sintética en preparación de candidatos, evaluación y filtros. Enlazar después la configuración seleccionada con el reentrenamiento. La tabla de arquitecturas debe seguir identificando preferencias previstas, sin dar por disponibles ambas arquitecturas en toda combinación.

**Criterio de cierre:** cada uso de «referencia» tiene un antecedente inequívoco y el lector distingue configurar, evaluar, filtrar y seleccionar.

### A15. Documentar la elección inicial de candidatos y el umbral de inserciones — P1; requiere evidencia

**Ubicación:** `5-metodologia.tex:467`; `8-apendice_arquitectura.tex:596` y `8-apendice_arquitectura.tex:598`.

Recomiendo precisar cómo se pasa de los ensayos técnicamente admisibles a los «hasta tres candidatos»: criterio de ordenamiento, tratamiento de arquitecturas y lugar de la configuración derivada de fase 1. También identificar el conjunto inicial que fija el máximo empírico de inserciones y cuándo queda congelado ese umbral.

Estas precisiones deben salir del selector o del contrato documental vigente. Si una regla no está definida, registrarla como una decisión metodológica pendiente; no inventarla durante la corrección editorial. Conservar los filtros y desempates documentados.

**Criterio de cierre:** otra persona puede reconstruir qué candidatos se evalúan y de qué episodios proviene la referencia, sin decisiones discrecionales ocultas.

## Variantes, métricas y evaluación

### A16. Nombrar A–E como formulaciones de observación y recompensa — P2

**Ubicación:** `5-metodologia.tex:16`, `5-metodologia.tex:489`, `5-metodologia.tex:496`.

La expresión «cinco formulaciones de cooperación mediante recompensa» describe de manera incompleta una prueba que también modifica observaciones y que incluye otra recompensa local en E. Recomiendo usar «prueba preliminar de formulaciones de observación y recompensa» y explicar inmediatamente qué alternativas locales y vecinales reúne.

Conservar que C y D comparten recompensa y difieren en observación, y que la prueba no es un barrido del coeficiente. Explicar el paso hacia A/C sin afirmar que la elección de C demuestra que sea la mejor formulación vecinal.

**Criterio de cierre:** el nombre del procedimiento coincide con los factores de la tabla A–E y con el alcance del contraste ampliado.

### A17. Anticipar la población de evaluación antes de introducir las siglas — P2

**Ubicación:** `5-metodologia.tex:18` y `5-metodologia.tex:534`.

Recomiendo explicar en el diseño, con una oración breve, que la espera se calcula para los vehículos que ingresan durante la ventana, incluyendo lo observado de viajes inconclusos. Luego introducir las medidas complementarias por su función: cuántos ingresan y qué proporción termina. Dejar la notación y las fórmulas para Métricas.

Distinguir desde esa presentación los conteos de cohorte usados en políticas y los conteos agregados de las comprobaciones urbanas. No presentar CR e IR como criterios de decisión de A/C si ese análisis no los utiliza así.

**Criterio de cierre:** el lector entiende quiénes entran en el promedio antes de encontrarse con tres siglas y múltiples denominadores.

### A18. Introducir una tabla compacta de métricas y usos — P2

**Ubicación:** `5-metodologia.tex:530`.

Recomiendo una tabla con medida, población o escala, unidad y función. Debe separar espera por viaje, inserciones, CI de cohorte, tasas agregadas de la comprobación urbana, pérdida temporal, señales locales, Gini e incidencias. Para evitar duplicación, no repetir las fórmulas ni los argumentos de interpretación en cada celda.

La columna de función debe distinguir objetivo de búsqueda, filtro de selección, criterio A/C y diagnóstico. Si una medida cumple varios papeles, indicar los procedimientos concretos.

**Criterio de cierre:** el lector puede localizar rápidamente qué representa cada indicador y dónde interviene, manteniendo la separación entre señales de aprendizaje y evaluación operacional.

### A19. Dividir las definiciones de métricas en unidades de lectura — P2

**Ubicación:** `5-metodologia.tex:534` y `5-metodologia.tex:551`.

Recomiendo separar el párrafo de cohorte en definición de población, tratamiento del cierre y registro de viajes. Considerar sustituir la lista extensa por párrafos identificados o pequeños apartados sin añadir niveles innecesarios al índice. Presentar primero la espera, después inserciones y completitud; mantener las tasas agregadas urbanas como un bloque identificado.

La limitación de viajes inconclusos y la exclusión del retraso previo al ingreso deben seguir junto a la definición de espera. La correspondencia con campos de salida puede detallarse en el apéndice cuando no sea necesaria para interpretar una ecuación.

**Criterio de cierre:** cada definición permite reconocer magnitud, población, unidad e interpretación sin recorrer varias excepciones dentro de una sola viñeta.

### A20. Dar una denominación breve a la medida local y contrastarla con el Gini — P2

**Ubicación:** `5-metodologia.tex:566` y `5-metodologia.tex:568`.

Recomiendo conservar «cociente local acumulado por observación de vehículo» como definición técnica y acompañarlo de una forma breve, por ejemplo «espera local ponderada por presencia vehicular», siempre que se explique su ponderación. Su denominador sigue contando observaciones de vehículos, no viajes distintos.

Añadir una comparación breve con la media utilizada para el Gini: el cociente agregado pondera los pasos por presencia vehicular; la media temporal da igual peso a los pasos. Mantener el tratamiento de pasos vacíos y la interpretación del Gini como desigualdad entre controladores, influida también por sus cargas estructurales.

**Criterio de cierre:** ambos promedios dejan de parecer intercambiables y la denominación abreviada no los confunde con TripInfo ni con equidad entre vehículos.

### A21. Simplificar la exposición de la evaluación y del criterio A/C — P2

**Ubicación:** `5-metodologia.tex:581`, `5-metodologia.tex:605`, `5-metodologia.tex:631`.

Recomiendo ordenar la evaluación final como configuración seleccionada, reentrenamiento, modelo de última iteración, simulaciones con parámetros fijos y resumen descriptivo. Expresar las 320 simulaciones como el total del diseño si las dieciséis combinaciones aportan una configuración seleccionada. Conservar los veinte valores válidos por métrica y la separación entre variación de simulaciones y de entrenamientos.

En A/C, mantener el recorrido evaluación por política, promedio, diferencia por par y remuestreo. Antes de los tres requisitos formales, explicar su sentido: reducción práctica de espera, margen admitido de completitud y ausencia de incremento de inicios de teletransporte. Explicar que el margen de CI admite un deterioro pequeño; no equivale a exigir una mejora de CI. Mantener las tres redes separadas y el alcance condicionado a las semillas compartidas.

**Criterio de cierre:** el lector comprende qué unidad se resume o remuestrea y puede interpretar cada requisito antes de leer sus desigualdades. Esta acción no cambia semillas, tamaños, márgenes, métricas ni paneles entre algoritmos.

## Coordinación editorial y validación

### A22. Reducir reiteraciones conservando las limitaciones donde importan — P2

**Ubicación:** apartados de espera, recompensa, A/C, reproducibilidad y alcance.

Recomiendo asignar a cada distinción una explicación central: memoria local frente a espera por viaje junto a la observación; efecto conjunto de observación y recompensa al presentar A/C; retorno individual frente a cooperación canónica al explicar la adaptación; procedencia urbana en Mendoza y su apéndice. Las apariciones posteriores pueden remitir brevemente a esa explicación.

Conservar cerca de cada operación las consecuencias que cambian su interpretación, en particular saturación de la pérdida, cierre temporal y atribución de espera. La sección final debe reunir restricciones transversales y no repetir extensamente las locales.

**Criterio de cierre:** se eliminan duplicaciones completas, pero ninguna fórmula o decisión queda privada de una premisa necesaria.

### A23. Coordinar el cuerpo con el marco teórico y el apéndice — P2

**Ubicación:** final del marco teórico, introducción del sistema multiagente y apéndice de reproducción.

Recomiendo conservar en el marco teórico los conceptos generales, antecedentes y garantías bajo sus supuestos; en metodología, las decisiones adoptadas y sus consecuencias; en el apéndice, dominios, semillas, fuentes y desarrollos extensos. Revisar introducción y resumen solo en los pasajes que deban acompañar cambios de alcance o denominación.

Mantener explícito que los UML representan el diseño inicial y no un inventario exhaustivo del código ejecutado. Para especificaciones dispersas, agregar remisiones concretas a sus tablas o apartados. No es necesario ampliar la arquitectura de software para resolver una dificultad narrativa.

**Criterio de cierre:** las remisiones llevan a la explicación prometida y cada detalle aparece en el lugar que corresponde a su función.

### A24. Uniformar vocabulario, siglas, notación y epígrafes — P3

**Ubicación:** capítulo de metodología, glosarios, figuras y pasajes relacionados.

Recomiendo revisar manualmente pares cercanos: configuración y política; evaluación diagnóstica, selección y evaluación final; controlador y agente; fase semafórica y fase de búsqueda. Evitar reemplazos globales. Usar «red vial» o «red de tráfico» cuando exista riesgo de confusión con una red neuronal; no repetir el calificativo donde el contexto ya sea claro.

Mantener una forma coherente para puntos de control/checkpoints, minilotes y términos extranjeros. Comprobar siglas en su primera aparición pertinente, plurales del glosario, unidades, separadores decimales, símbolos, títulos opcionales para PDF y correspondencia de captions con lo dibujado. Las figuras ilustrativas deben seguir diferenciadas de los parámetros efectivos de A/C.

**Criterio de cierre:** un concepto mantiene su nombre a lo largo del método y sus representaciones en texto, tabla, figura y glosario coinciden.

### A25. Verificar las modificaciones en el documento completo — P3

**Ubicación:** fuentes incluidas desde `main.tex` y PDF compilado.

Después de implementar una intervención, revisar su diff para comprobar que conserva las cifras y reglas del procedimiento. Buscar etiquetas existentes antes de crear nuevas, verificar referencias y coordinar figura, fuente y epígrafe. Para figuras generadas, actualizar el generador y su fuente cuando corresponda, en lugar de editar únicamente una salida que luego se sobrescribirá.

La compilación de verificación debe conservar SyncTeX:

```bash
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

Cuando cambien entradas o usos de glosario, ejecutar antes una pasada completa y regenerar sus índices:

```bash
pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
makeglossaries main
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

Revisar el log y las páginas afectadas del PDF: apertura, flujo, tablas, métricas y límites de página. La advertencia conocida de `tracklang` puede permanecer; deben resolverse citas o referencias indefinidas y nuevos desbordamientos. Si se cambian enlaces del glosario, comprobar también destinos y anotaciones. Mantener `main.pdf` como producto versionado y los artefactos intermedios ignorados.

**Criterio de cierre:** el documento compila, las páginas intervenidas se leen correctamente y la verificación técnica acompaña la revisión editorial.

## Orden recomendado de implementación

| Intervención | Acciones principales | Producto revisable |
|---|---|---|
| 1. Resolver dependencias y precisiones | A02, A03, A08, A11–A15 | Decisiones documentadas sobre las dos líneas, las fuentes del objetivo y la selección. |
| 2. Revisar apertura y recorrido | A01, A04–A06, A16 | Apertura y flujo coordinados con las preguntas del método. |
| 3. Mejorar lectura técnica | A07, A09, A10, A17–A22 | Escenarios, métricas y evaluación con párrafos más fáciles de seguir. |
| 4. Coordinar y verificar | A23–A25 | Texto, apéndice, glosario y figuras consistentes; PDF comprobado. |

Las acciones basadas en código deben resolverse antes de redactar afirmaciones que dependan de ellas. Las modificaciones de lectura que no dependan de esos datos pueden prepararse por separado. Este orden propone unidades de trabajo; no ejecuta ni autoriza automáticamente la modificación de los capítulos.

## Criterios de conservación

La revisión debe preservar la estructura general y las mejoras de rigor ya incorporadas. En particular, mantener la comparación A/C limitada a MAPPO y a las tres redes sintéticas; la diferencia de capacidad de entrada entre A y C; las recompensas específicas de cada procedimiento; el carácter individual de los retornos; los límites de la adaptación de HAPPO; la distinción entre señal local y espera por viaje; las poblaciones de evaluación; y los contadores de incidencias propios de cada procedimiento.

Las acciones editoriales no requieren modificar el diseño experimental, añadir ablaciones, cambiar paneles de semillas, alterar márgenes estadísticos ni corregir retrospectivamente el código de campañas ya realizadas. La frecuencia de saturación de la pérdida y otros diagnósticos no cuantificados pueden conservarse como límites reconocidos. Si se decidiera ampliar la experimentación, sería una tarea metodológica separada de este informe.

## Comprobación del informe

Se cotejaron las recomendaciones con las fuentes actuales y las instrucciones del repositorio. Se conservó el informe local previo sobre correcciones de rigor remoto. La comparación histórica fundamenta el diagnóstico general, pero las acciones se refieren a la copia de trabajo actual; no se trasladaron observaciones ya corregidas ni se incluyeron tareas sobre Resultados o Conclusiones. No se modificaron archivos LaTeX, figuras, glosarios ni `main.pdf`, y no se ejecutó una nueva compilación para crear este informe Markdown.
