# Reglas editoriales derivadas de la revisión de Caro

Estas reglas se aplican a la redacción y revisión de la tesina. Complementan `AGENTS.md`; no sustituyen sus restricciones de alcance, evidencia, glosario y compilación. Antes de redactar o modificar prosa, títulos, epígrafes, tablas, ecuaciones o diagramas, leer las reglas pertinentes y comprobarlas al terminar el bloque.

Origen: las 287 anotaciones del PDF de Caro, relevadas en [TODO-comentarios-caro.md](TODO-comentarios-caro.md) e inventariadas en [observaciones-caro.csv](observaciones-caro.csv). Los identificadores C remiten a ese relevamiento. La [auditoría de aplicación](revision-reglas-caro-2026-10-16.md) registra otras instancias del mismo tipo de problema en las fuentes actuales. Fecha de formalización: 16 de octubre de 2026.

## Alcance de la inferencia

- **Pedido explícito:** una anotación formula el criterio; puede extenderse a casos equivalentes.
- **Regla inferida:** varias correcciones locales permiten reconocer un principio; se indica ese carácter y se aplica con las excepciones aquí descritas.
- **Extensión operativa:** traduce el principio a una comprobación concreta del proyecto. No debe atribuirse a Caro como cita literal ni presentarse como norma universal de escritura.

Los ejemplos de reformulación sugeridos por Caro no son texto obligatorio. Una tachadura sin comentario no autoriza a suprimir indiscriminadamente todos los usos de esa palabra. Las convenciones particulares de mayúsculas se adoptan para esta tesina y no se presentan como reglas generales del español. Las búsquedas de patrones localizan candidatos: la decisión editorial requiere leer el contexto.

## Organización y recorrido del argumento

### R01. Definir antes de aplicar

**Origen explícito:** C181, C184, C192, C194 y C197.

Desarrollar las dependencias conceptuales en orden: componente, operación, composición y aplicación. Para redes neuronales, introducir neurona, entradas, pesos, sesgo y activación antes de capas/redes y antes de ejemplos de semáforos. Para algoritmos, explicar la cantidad estimada y el problema que se resuelve antes de la actualización. Una definición disponible solo en el glosario no reemplaza la explicación necesaria para seguir el argumento del cuerpo.

**Control y excepción:** releer la primera aparición sustantiva desde la perspectiva de un lector nuevo. Se permite una anticipación breve para orientar la sección, siempre que no exija comprender conceptos todavía no desarrollados.

### R02. Ajustar el detalle a la función del apartado

**Origen explícito e inferido:** C011, C027, C034 y C043–C044.

La introducción presenta motivación, problema, objetivos y contribuciones; el marco teórico desarrolla fundamentos generales; metodología explica decisiones y operaciones efectivamente adoptadas; resultados presenta observaciones y su interpretación; el apéndice conserva especificaciones extensas. No adelantar UML, detalles del crítico, niveles del codificador o registros internos si no ayudan a entender el problema en ese punto.

**Control y excepción:** justificar qué necesita saber el lector para avanzar. Una premisa o limitación necesaria para interpretar el método no se relega al apéndice solo para acortar el cuerpo. Respetar la distribución de contenidos de SUMO ya fijada en `AGENTS.md`.

### R03. Explicar las transiciones entre temas y la pertinencia de cada desarrollo

**Origen explícito:** C158–C159, C163, C167, C180, C182 y C201.

Al cambiar de escala, familia de métodos o etapa, indicar qué cambia y por qué se introduce. Identificar el objetivo concreto antes de hablar de «la optimización». Un teorema o antecedente debe cumplir una función reconocible en el razonamiento; si no la cumple, abreviar, reubicar o retirar. «En síntesis» introduce un resumen real; una aplicación al tránsito debe presentarse como aplicación.

**Control y excepción:** preguntar qué relación tiene el párrafo con el anterior y qué aporta al siguiente. No reemplazar un anuncio vacío por otro con palabras distintas.

### R04. Construir párrafos con una idea y continuidad interna

**Origen explícito:** C138, C178, C207, C250 y C252.

Integrar una oración introductoria breve con el desarrollo que le da contenido cuando forman una sola idea. Separar conceptos generales, ejemplos y decisiones propias cuando cambie su función. Evitar párrafos aislados que solo anuncian importancia, una figura o una optimización sin sujeto identificable.

**Control y excepción:** no unir todo en un párrafo largo para eliminar saltos o líneas aisladas. La unidad conceptual tiene prioridad; el ajuste de página se verifica después.

### R05. Definir una vez y evitar repeticiones sin función nueva

**Origen explícito:** C017, C035, C079–C080 y C104.

Reunir definición, ecuación y explicación de una magnitud donde se introduce. Evitar repetir la clasificación de modelos, la función del crítico, las relaciones de una figura o una misma limitación en párrafos contiguos. Una segunda aparición debe aportar una aplicación, una precisión o una remisión útil.

**Control y excepción:** comparar los párrafos vecinos y el destino de las remisiones. Es legítimo resumir una especificación del apéndice en el cuerpo; conservar allí la premisa necesaria y reservar abajo el detalle, sin copiar ambos desarrollos completos.

## Referentes, autoría y alcance

### R06. Usar sujetos y antecedentes inequívocos

**Origen explícito:** C016, C020, C077, C090, C117, C196 y C198–C205.

Precisar «red neuronal» o «red vial/de tránsito» cuando ambas lecturas sean posibles. Identificar la operación o cantidad a la que remiten «este procedimiento», «estas transformaciones», «ese objetivo» o «ambas etapas». Distinguir objetivo de control, función objetivo, blanco de entrenamiento y pérdida. Al abrir un párrafo, evitar un demostrativo que obligue a reconstruir un antecedente remoto.

**Control y excepción:** un pronombre con antecedente inmediato y único es correcto. No añadir calificadores repetitivos a cada aparición de «red» cuando el significado ya es inequívoco.

### R07. Separar la voz de las fuentes de la del trabajo propio

**Origen explícito:** C280 y C283; modelo positivo en C246.

Al pasar de un antecedente a esta tesina, nombrar el cambio: «En esta tesina…», «Para el protocolo aquí definido…». Reservar «el estudio de X» para la publicación identificada y «este ensayo/estudio de HPO» para su unidad metodológica real. Atribuir a los autores los resultados que informan; señalar como inferencia propia la lectura del estado del arte.

**Control y excepción:** comprobar quién realiza cada acción y a quién pertenece cada resultado. No cambiar el nombre de una publicación ni enlazar «estudio» a HPO cuando se habla de toda la investigación.

### R08. Distinguir propuesta, implementación, ejecución y evidencia

**Origen explícito e inferido:** C028–C034, C238, C280 y C284; aplicación sujeta a las restricciones metodológicas de `AGENTS.md`.

Elegir sujeto, verbo y tiempo que describan el estado acreditado: un diseño contempla; una configuración especifica; una implementación realiza una operación comprobada; una ejecución conservada permite informar observaciones. La existencia de código, presupuesto, semilla o manifiesto no demuestra por sí sola una campaña. Una comparación de procedimientos completos no aísla causalmente un componente. Acotar novedad y garantías a las fuentes, supuestos y búsquedas realmente considerados.

**Control y excepción:** conservar las diferencias entre teoría y adaptación, los protocolos de recompensa, los alcances sintético/urbano y las limitaciones de procedencia. No debilitar una limitación necesaria para hacer más fluida una oración ni fortalecer una afirmación solo por eliminar una cautela repetida.

## Figuras, tablas y ecuaciones

### R09. Explicar cada figura en un bloque coherente y próximo

**Origen explícito y generalizable:** C076, C092, C100, C107, C154, C166 y C250.

Introducir la figura y explicar qué permite reconocer, cómo se leen sus elementos y qué conclusión aporta dentro de un desarrollo continuo, preferentemente antes de ella. Evitar presentar el objeto, intercalar una tabla, otra sección o un desarrollo distinto y volver a empezar su explicación después. Aplicar el mismo criterio funcional a tablas y diagramas de arquitectura.

**Control y excepción:** una referencia posterior con una interpretación nueva es válida; no es lo mismo volver a usar una figura que volver a presentarla. «Bloque coherente» puede contener varios párrafos. El orden visual de los objetos flotantes debe comprobarse en el PDF, no solo en LaTeX.

### R10. Reservar los epígrafes para identificar e interpretar lo indispensable

**Origen explícito:** C003, C114, C154 y C166.

Dar al epígrafe un título descriptivo, las unidades, la identificación de paneles o convenciones mínimas y la atribución necesaria. Llevar al cuerpo las operaciones, decisiones, explicaciones de funcionamiento y limitaciones que forman parte del argumento. No repetir en el epígrafe un desarrollo que ya está en la prosa.

**Control y excepción:** no fijar un máximo arbitrario de palabras. Una leyenda breve puede ser indispensable para que la figura sea interpretable por sí misma; el problema es desplazar el razonamiento o duplicarlo, no su longitud aislada.

### R11. Abreviar atribuciones sin perder la procedencia

**Origen explícito e inferido:** C004, C054, C088, C106, C133 y C142; cautela de aplicación en las tachaduras C216 y C257.

Evitar «Elaboración propia» repetido cuando no informa nada adicional, y la narración innecesaria de títulos de manuales. Conservar las fuentes de datos, imágenes adaptadas, algoritmos y afirmaciones. Colocar cada cita donde termine o se identifique el contenido que respalda. Distinguir datos ajenos representados en una figura propia de contenido original.

**Control y excepción:** no borrar una cita porque se suprima la fórmula «adaptado de» o porque otra oración cercana cite la misma obra. La atribución debe seguir siendo localizable y suficiente.

### R12. Verificar la semántica y la legibilidad de los diagramas

**Origen explícito:** C062 y C064; extensión operativa a los restantes diagramas.

En figuras viales, hacer inequívocos sentidos, continuidad de trayectorias, accesos, conflictos y leyenda. En flujos y diagramas de clases, explicar qué significan flechas, tipos de relación, multiplicidades y agrupaciones. Los rótulos deben caber sin invadir otros elementos; las etiquetas y colores deben coincidir con el texto. No usar solo el color si una forma o etiqueta puede identificar el elemento.

**Control y excepción:** revisar fuente, figura compilada, epígrafe y párrafo como una unidad. Un esquema ilustrativo no necesita reproducir todos los detalles de la implementación, pero debe declarar su alcance y no sugerir relaciones falsas. No retirar binarios sin la autorización prevista en `AGENTS.md`.

### R13. Introducir y nombrar las expresiones matemáticas con precisión

**Origen explícito:** C148–C151, C157, C175, C197, C219, C230, C235 y C247.

Presentar la cantidad o relación antes de su ecuación; definir símbolos, índices, conjuntos, operadores y unidades cerca de la primera aparición. Definir la esperanza cuando se usa por primera vez y aclarar sobre qué se promedia. Usar oraciones completas al desarrollar una tupla. Referir una expresión numerada como «Ecuación» y, si aporta, explicar que expresa una regla de actualización.

**Control y excepción:** reutilizar las etiquetas existentes, no números copiados de un PDF anterior. Una lista de símbolos puede usar una estructura elíptica uniforme; no alternar inadvertidamente definiciones completas con fragmentos que dependen de un verbo ausente. Los dos puntos son válidos cuando introducen de forma necesaria una expresión, no como sustituto de explicar su función.

## Terminología, siglas y enlaces

### R14. Desarrollar las siglas en su presentación sustantiva

**Origen explícito:** C019, C025–C026, C109, C132, C159, C183, C227 y C265.

Desarrollar cada sigla cuando el lector necesita comprenderla por primera vez y reintroducirla si aparece en un bloque autónomo o muy alejado. El resumen y el Abstract deben poder leerse por sí mismos. No suponer que la lista inicial de siglas reemplaza su presentación en el cuerpo. Comprobar el comportamiento de `\gls`, `\acrfull` y `\acrshort` antes de elegir la macro.

**Control y excepción:** no expandir una sigla en cada párrafo ni convertir todas las celdas de tablas en desarrollos largos. Se pueden presentar las expansiones en la prosa anterior. Si una sigla solo añade carga y no vuelve a usarse, valorar escribir únicamente el término completo.

### R15. Mantener una convención bilingüe y un vocabulario estables

**Origen explícito:** C014, C134–C137, C139, C170, C176–C177, C185, C189, C204, C229 y C253.

Usar, cuando corresponda, «término español (término inglés, SIGLA)», con un único grupo de paréntesis. Identificar qué idioma desarrolla la sigla: no hacer pasar IA por iniciales de *Artificial Intelligence*. Conservar siglas internacionales cuando sean las empleadas por la bibliografía. Usar «neurona artificial», «lote», «minilote», «época» y «logaritmo de la probabilidad» como formas españolas de referencia, presentando el inglés una vez si ayuda al lector.

**Control y excepción:** no traducir nombres de funciones, claves, rutas, modelos o productos de software dentro de identificadores. No añadir siglas o traducciones inglesas a todas las palabras. Al cambiar una convención, revisar prosa, pseudocódigo, glosario y epígrafes sin alterar literales del código.

### R16. Enlazar términos del glosario sin alterar su significado

**Origen explícito:** C045, C048, C186, C212 y C226; extensión operativa según `AGENTS.md`.

Enlazar la definición o un uso pertinente del término visible mediante la entrada adecuada. Verificar `name`, `text`, plural y forma visible antes de sustituir texto por una macro; crear o ajustar una entrada si no representa la forma necesaria. Mantener definiciones suficientes en la prosa y comprobar destinos y anotaciones del PDF.

**Control y excepción:** `\glsaddall` o `\glsadd` no sustituyen el enlace desde la palabra visible. No es necesario enlazar cada repetición. No confundir *bootstrapping* de RL con *bootstrap* estadístico, fase semafórica con fase de búsqueda ni red neuronal con red vial.

### R17. Uniformar las referencias y nombrar el tipo real de destino

**Origen explícito:** C002, C036, C042, C046, C051 y C223; extensión operativa para comprobar destinos.

En referencias singulares a objetos numerados, usar «Figura», «Tabla», «Ecuación», «Capítulo», «Sección», «Apéndice» y «Algoritmo». Usar «Sección» también si el destino es una subsección, según la convención pedida por Caro. Para una sección interna del apéndice, escribir «Sección A.x del Apéndice A» o «Sección A.x», según lo que necesite el lector; «Apéndice A» designa la unidad completa. Verificar el destino en las fuentes, no inferir su tipo del prefijo de la etiqueta.

**Control y excepción:** los usos genéricos van en minúscula; para plurales, mantener el criterio indicado por Caro («las figuras…», «las tablas…»), sin sustituciones globales. Conservar `\ref`/`\eqref`, corregir referencias ambiguas y explicar qué encontrará el lector en una remisión lejana.

### R18. Mantener cifras, símbolos y unidades consistentes

**Origen explícito:** C006, C072–C075, C082 y C099.

Usar coma decimal y un criterio español uniforme de agrupación de miles en prosa y tablas. Distinguir el símbolo de una variable de la unidad física, desarrollar la unidad cuando evita ambigüedad y especificar unidades de ejes y magnitudes. Definir convenciones de conjuntos como `\mathbb{N}_0` en vez de presumir que todos incluyen el cero en los naturales.

**Control y excepción:** «segundos» resuelve la colisión entre el espaciamiento `s` y su unidad temporal; no es obligatorio sustituir toda unidad SI `s` por «seg.». No cambiar separadores dentro de código, coordenadas, versiones, semillas, identificadores, DOI ni archivos. No inferir una cantidad experimental distinta a partir de un cambio tipográfico.

## Fuentes, estilo y cierre de la revisión

### R19. Elegir las fuentes por su pertinencia

**Origen explícito:** C056–C057, C126, C131, C133, C140, C142, C144, C161, C187 y C211.

Respaldar definiciones y teoremas con fuentes de fundamento; aplicaciones y resultados con investigaciones pertinentes; herramientas con su publicación o documentación oficial; datos con su origen. Diversificar cuando una única obra está sosteniendo asuntos para los que existen fuentes más directas. Añadir una cita real cuando se nombra una obra como autoridad.

**Control y excepción:** no imponer cuotas de fuentes, prohibir Sutton y Barto ni sustituir una referencia correcta solo por variar. Una entrada en `.bib` no equivale a una cita visible. Verificar la publicación y su contenido antes de incorporarla; no suponer esa verificación a partir de este archivo de reglas.

### R20. Revisar autoría bibliográfica y concordancia en prosa

**Origen explícito:** C066.

Al atribuir una definición o resultado, comprobar autores, edición y año de la obra consultada. Ajustar el sujeto y el verbo a esa autoría y conservar registros BibTeX coherentes. La clave de una entrada o su etiqueta abreviada en el PDF no identifica necesariamente a todos sus autores.

**Control y excepción:** no agregar o eliminar autores de memoria ni tomar una sugerencia de una anotación como verificación de la edición real. Mantener los datos conocidos de `suttonRL` y `marlbook` fijados en `AGENTS.md`.

### R21. Usar la puntuación para expresar relaciones, no para suplirlas

**Origen explícito:** C007, C015, C110, C112, C138, C141, C153, C162, C165, C171–C174, C191, C208–C210, C235 y C278.

Reformular cadenas de dos puntos y punto y coma que acumulen definición, ejemplo, resultado y cambio de tema. Preferir un conector preciso o punto seguido cuando hagan explícita la relación. Revisar comas de incisos y oraciones largas sin separar sujeto y verbo. Distribuir incisos, citas y siglas en oraciones legibles.

**Control y excepción:** no prohibir `:` ni `;`. Son necesarios o útiles en definiciones, enumeraciones, intervalos, código y matemáticas. Una marca de coma se aplica revisando la sintaxis completa, no insertando un signo mecánicamente en su coordenada.

### R22. Construir remisiones útiles en vez de delegar la explicación

**Origen explícito:** C244 y C256; regla inferida aplicable también a remisiones hacia atrás.

Al remitir a otro apartado, decir qué se desarrolla allí y qué necesita recuperar el lector. No usar un número entre paréntesis como reemplazo de una premisa o definición necesaria en la oración actual. Comprobar que el destino contiene realmente lo que se le atribuye.

**Control y excepción:** una remisión breve basta si el texto ya explica su función. No convertir cada referencia en un anuncio largo ni repetir en el cuerpo toda una especificación del apéndice.

### R23. Mantener un registro natural y preciso

**Origen explícito e inferido:** C008, C017, C032, C040, C054, C058, C143, C182 y C195.

Preferir sujetos y verbos concretos a anuncios vacíos, intensificadores o fórmulas coloquiales. Evitar repeticiones próximas de «En este contexto», «este enfoque» y expresiones equivalentes cuando no identifican una relación. Explicar una operación especializada si su nombre resulta opaco; por ejemplo, «ajusta la ponderación de…» puede aclarar «repondera».

**Control y excepción:** «delimitar», «reponderar» o «conceptual» no son palabras prohibidas. No sustituir términos técnicos por sinónimos que cambien su sentido, ni alterar el nombre de la tesina por aplicar todas las variantes locales de «trabajo final» sugeridas en el PDF.

### R24. Verificar la lectura de página después de la lectura conceptual

**Origen explícito:** C085 y C252; extensión operativa de los controles de build del proyecto.

Revisar en el PDF líneas aisladas, títulos, continuidad de párrafos, figuras, leyendas, tablas y desbordes después de reorganizar la prosa. No dar por buena la diagramación por una compilación exitosa ni deducir un defecto visual solo de una línea del `.tex`.

**Control y excepción:** conservar la unidad de los párrafos antes de añadir ajustes de espacio o penalidades. No declarar resuelta una observación de página del PDF antiguo sin comprobar la versión nueva.

### R25. Hacer autónomos y veraces el resumen y el Abstract

**Origen explícito:** C001; extensión operativa al Abstract y al resto de los anuncios del documento.

Presentar problema y motivación, propósito, enfoque y alcance; incorporar resultados únicamente cuando estén documentados. Mantener correspondencia entre resumen español, Abstract, objetivos y capítulos efectivamente desarrollados. Reducir detalles internos y evitar siglas sin presentación que obliguen a consultar otros capítulos.

**Control y excepción:** una motivación ambiental no demuestra mejoras en emisiones. Si resultados o conclusiones están incompletos, identificarlos como pendientes y ajustar los anuncios; no inventar evidencia para completar la estructura.

### R26. Aplicar las observaciones con trazabilidad y criterio

**Origen inferido:** la coexistencia de correcciones locales, marcas sin texto, el comentario incompleto C102 y las valoraciones positivas C246/C287.

Para cada corrección, identificar regla, pasaje actual, problema de lectura y criterio de cierre. Distinguir incumplimiento confirmado, decisión editorial y comprobación pendiente. Resolver juntas las marcas que pertenecen a una misma oración o reestructuración. Preservar los pasajes valorados y los cambios previos del usuario.

**Control y excepción:** no equiparar cantidad de coincidencias con cantidad de errores; no convertir cada sugerencia en una prohibición; no marcar capítulos sin anotaciones como aprobados. Un archivo de reglas reduce recurrencias, pero no reemplaza la revisión del significado y del PDF.

## Control antes de dar por terminado un bloque

1. **Recorrido:** se entiende qué se presenta, para qué y con qué conceptos previos; los ejemplos aparecen donde se los puede interpretar.
2. **Referentes y alcance:** cada acción tiene sujeto; se distingue fuente, propuesta, implementación y ejecución; se conservan supuestos y limitaciones.
3. **Elementos técnicos:** figuras y ecuaciones están introducidas, explicadas y enlazadas; sus leyendas, unidades y símbolos coinciden con la prosa.
4. **Consistencia:** no hay definiciones repetidas sin función nueva; siglas, términos, referencias y glosario siguen una convención única.
5. **Fuentes y verificación:** las citas respaldan lo que se afirma; el destino de cada remisión contiene lo prometido; se cumple el ciclo de compilación/glosario aplicable y se revisa el PDF si se modificaron las fuentes.

Registrar como pendiente cualquier comprobación no realizada. Estas reglas no agregan un requisito de autorización: se aplican dentro del alcance ya autorizado por el usuario y del flujo de trabajo de `AGENTS.md`.
