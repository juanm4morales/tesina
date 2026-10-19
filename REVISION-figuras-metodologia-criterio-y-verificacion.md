# Revisión de las figuras tras las observaciones del usuario

Esta revisión sustituye la entrega v05. La revisión anterior pasó la compilación, pero ese resultado no acreditaba utilidad ni calidad visual. El panel «fase activa: 2» era redundante; las flechas y líneas de las redes eran demasiado próximas; varios diagramas mezclaban su propósito con detalles accesorios. La comprobación visual inicial fue insuficiente.

## Referencias visuales realmente inspeccionadas

Se descargaron los PDF y se renderizaron páginas concretas, no solo sus índices:

- [El-Tantawy, Universidad de Toronto, 2012](https://www.collectionscanada.gc.ca/obj/thesescanada/vol2/OTU/TC-OTU-67269.pdf): figuras 4-3 y 4-4, página impresa 83; Figura 4-6, página 93; Figura 4-11, página 103. La comparación de vecindarios mantiene geometría y alineación; el proceso OD separa entradas, procedimiento y productos. Se retienen esos criterios, sin copiar la densidad, los fondos extensos ni las capturas de código.
- [Zhang, Georgia Tech, 2019](https://repository.gatech.edu/server/api/core/bitstreams/325863b0-529c-42df-af32-90919c742c95/content): Figura 3.1, página 11, y figuras 4.1–4.3, página 17. La arquitectura distingue observaciones, acciones y aprendizaje; las redes muestran calzadas reconocibles. La aplicación aquí consiste en separar los intercambios y representar carriles mediante franjas, evitando los pares de trazos casi coincidentes.
- [Chakrabarti, Trinity College Dublin, 2022](https://publications.scss.tcd.ie/theses/diss/2022/TCD-SCSS-DISSERTATION-2022-032.pdf): figuras 3.3 y 3.5–3.6, páginas 28 y 30. El contraste entre una escena y su representación numérica tiene un contenido verificable. En esta tesina se conserva la curva de codificación y se retira el ejemplo arbitrario de fase, cuya repetición no explicaba una transformación.

Estas son referencias de composición de figuras específicas, no una aprobación de todos los aspectos de esas tesis. No se añaden como antecedentes científicos a la bibliografía.

El conjunto revisado combina representaciones distintas según la pregunta: planos de redes viales, una curva cuantitativa, líneas temporales, comparación paralela de formulaciones y un esquema de evaluaciones emparejadas. Los flujos se conservan donde hacen falta para mostrar dependencias entre etapas o intercambios entre componentes.

## Justificación y decisión por figura

| Figura | Pregunta que justifica incluirla | Decisión en esta revisión |
|---|---|---|
| Diseño experimental | ¿Cuáles son las dos comparaciones y qué operaciones dependen de otras? | Dos bandas alineadas; se retira la conexión discontinua que cruzaba zonas de rótulos. La relación metodológica se explica en prosa. |
| Redes sintéticas | ¿Cómo cambian geometría, capacidad y conectividad entre escenarios? | Calzadas separadas por sentido y franjas por carril; cruces despejados, flechas desplazadas longitudinalmente, mismos criterios de dibujo en los paneles. |
| Construcción urbana | ¿Qué entradas distintas deben converger para poder simular el escenario? | Dos ramas de igual ancho y filas alineadas, con unión explícita; se retira la leyenda que repetía operaciones ya rotuladas. |
| Mapa de Mendoza | ¿Cuál es el dominio y dónde se representa el acceso de referencia? | Se deja una única vista cartográfica, con nombres fuera del trazado y llamadas a sus avenidas, y se destaca TAZ 28; se retira el inserto que repetía un fragmento del mapa y la caja sobre la cámara. Su localización exterior permanece en el texto. |
| Integración | ¿Qué intercambia cada componente durante interacción y aprendizaje? | Cuatro nodos y conexiones ortogonales. Guardado, recarga y salidas de viajes permanecen descritos en prosa; se eliminan sus recorridos largos de esta figura. |
| Codificador | ¿Cómo se distribuyen los niveles y dónde se satura la codificación? | Se conserva solo la curva. Se retira el panel superior completo, incluida «fase activa: 2». Los puntos corresponden a valores comprobados y se explican junto a la curva. |
| MAPPO/HAPPO | ¿Qué cambia en la dependencia entre las actualizaciones de actores? | Paneles con entradas, crítico, ventajas y actores alineados. Se acota la figura a esta comparación; IPPO e IDQN se explican en el texto. Flechas horizontales discontinuas: factores acumulados. |
| Máscara | ¿Por qué cinco segundos mínimos de verde permiten otro cambio recién en la decisión de los diez segundos? | Conservar y simplificar: una sola barra proporcional con amarillo y verde; se retira el panel de inicialización. El cuerpo define el origen, las flechas y el corchete antes de la figura. |
| Refinamiento | ¿Cómo se derivan dos productos diferentes de los ensayos previos? | Bifurcación y convergencia simétricas, con puntos de unión explícitos. Se eliminan flechas superpuestas hacia la entrada de fase 2. Se aclara el alcance sintético en la presentación. |
| A/C | ¿Qué información y recompensa cambian conjuntamente? | Componentes locales del mismo tamaño; los vecinos añaden celdas. La recompensa ocupa una fila separada, sin conectarse al actor como si fuera observación. |
| Cohorte | ¿Qué vehículos integran las métricas, especialmente los inconclusos y los que no ingresan? | Conservar: cuatro casos numerados vinculados con su explicación. Antes de la figura se definen ventana, marcas y trazos; las longitudes son tiempos ilustrativos, no cantidades de espera. |
| Análisis pareado | ¿Cómo se comparan dos modelos bajo las mismas condiciones de tráfico? | Rechazar la matriz y simplificar: dos filas de cinco episodios, unidos por la semilla de tráfico compartida. Se eliminan todas las celdas con «w» y los resúmenes redundantes. El promedio y el remuestreo de pares completos se explican en el cuerpo. |

La simetría se aplica a paneles, nodos y márgenes; no se modifica la asimetría real de la red heterogénea para obtenerla. La cantidad no es un criterio de aceptación. Se conservaron estas figuras porque responden preguntas distintas; se retiraron subpaneles y recorridos sin una contribución suficiente.

## Fuentes, significado y verificaciones

Las fuentes de cada figura siguen en `imagenes/`. Las versiones previas se conservan para comparación. Los generadores de redes y curvas se modificaron junto con sus salidas; las capturas originales no se eliminaron.

La representación vial es esquemática entre centros de nodos. Cada franja representa un carril, con ancho convencional; no reproduce anchuras físicas ni trayectorias internas de giro. Los XML determinan agentes, conexiones, sentidos y número de carriles. Se contrastaron los conteos 3/20/40, 9/48/96 y 16/71/166 (agentes/tramos/carriles), y específicamente las conexiones ausentes B4–C4 y D1–E1, la asimetría de C, el sentido único al norte de D y los tres carriles por sentido de la fila 2.

El codificador conserva su función numérica, con 1.265 comprobaciones contra el código congelado de A/C. El índice de fase se explica en la ecuación de observación; no necesita un número arbitrario en una figura. La curva utiliza I=22 y M=1.136 veh·s como ejemplo, sin atribuir esos parámetros a A/C.

El contraste A/C sigue modificando conjuntamente observación y recompensa y aumentando el tamaño de entrada. La recompensa normalizada de C no se extiende a la fase 1 histórica. El protocolo urbano no se presenta como ejecución acreditada. La espera de memoria finita por carril no se equipara con la espera acumulada por viaje.

El control estático de TikZ, la compilación aislada y el renderizado preceden a la revisión visual. El script `metodologia_revisar_texto.py` usa las cajas de palabras extraídas por Poppler para detectar candidatos a solapamiento de texto; **no comprueba cruces entre texto y trazos**. Esos cruces, las puntas de flecha y las calles se inspeccionan en los PNG individuales y en las páginas de la tesis. No se confunde una compilación correcta con una revisión visual aprobada.


## Entrega y control final

La entrega actual es **v16**, revisada el 19 de octubre de 2026. La Figura 3.12 de v14 repetía «w» como marcador del dato de espera, sin mostrar valores; la repetición no explicaba el pareo y añadía dificultad. Se sustituye por dos filas de episodios alineados por semilla de tráfico, sin notación nueva. La Figura 3.11 se conserva porque distingue la población utilizada por las métricas de la demanda programada y separa inclusión de finalización. La Figura 3.8 se conserva porque hace visible la diferencia entre el mínimo continuo de verde y la comprobación en decisiones discretas. Su color salmón procedía de una paleta genérica y era semánticamente inadecuado: ahora los estados se representan con amarillo y verde, además de sus nombres.

La [hoja de contacto actual](imagenes/revision-metodologia/contacto-v16.png) y su [versión en gris](imagenes/revision-metodologia/contacto-v16-gris.png) muestran las doce figuras. Las versiones anteriores se conservan como historial. La [comparación vial v05–v10](imagenes/revision-metodologia/comparacion-redes-v05-v10.png) documenta la revisión previa de redes.

Se revisaron las introducciones y convenciones de las doce figuras: funciones y direcciones de flechas, identificadores viales, OSM, llamadas cartográficas, recorrido del muestreo al Learner, variables del codificador, identificadores de actores, tiempos de control, productos de HPO, símbolos de recompensa y vecinos, población evaluada y pareo. Las aclaraciones que faltaban se incorporaron al cuerpo antes de las figuras. No se atribuyen datos empíricos a las posiciones esquemáticas de círculos o trayectorias. La línea temporal semafórica sí conserva proporciones exactas: amarillo [0,4), mínimo de verde alcanzado en 9 y primera decisión admisible en 10, con seis segundos de verde.

Las doce fuentes principales se compilaron aisladas y se inspeccionaron individualmente, además de revisar las páginas que las contienen. El control textual de Poppler no detectó candidatos a solapamiento entre palabras en las doce figuras; los PDF aislados miden entre 12,78 y 15,61 cm de ancho, con rótulos a tamaño final. El control complementario de las dos fuentes del codificador también pasó. Se revisaron los recorridos de flechas y sus puntas, los espacios de rótulos y los paneles en color y en gris.

Para reproducir las figuras y el control textual:

```bash
python3 imagenes/metodologia_generar_redes.py --proyecto /ruta/al/repositorio/experimental
python3 imagenes/metodologia_v2_generar_encoder.py
python3 imagenes/metodologia_verificar_figuras.py --skill /ruta/a/tikz-diagrams --version v16
python3 imagenes/metodologia_revisar_texto.py --version v16
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex
```

El generador de la hoja de contacto se ejecutó con el entorno local existente que contiene Pillow; los demás controles de texto usan Poppler y la biblioteca estándar de Python. No se instaló ningún paquete. Las fuentes XML y las capturas se consultaron sin modificarlas; los hashes de los XML siguen registrados en `imagenes/metodologia_redes_procedencia.json`.

El PDF completo tiene 166 páginas. Se regeneraron glosarios y SyncTeX; se renderizaron las páginas con figuras a 150 dpi fuera del repositorio y se revisaron también sus explicaciones próximas. Se corrigió una línea aislada después del mapa de Mendoza. Compilación final sin referencias ni citas indefinidas y sin desbordes horizontales o verticales. Solo permanece la advertencia externa conocida de `tracklang` sobre el dialecto español. `git diff --check` no informa problemas.

SHA-256 de `main.pdf`: `f221311823658bf8d6a9823e7db8af5916513d90b20bf47b4a2a5596ff94d9dc`.
