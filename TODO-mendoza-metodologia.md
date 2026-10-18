# TODO: escenario de Mendoza y cierre de la metodología

Este documento reúne el checklist de preparación y el prompt para el coding agent. Los TODO se mantienen fuera del manuscrito LaTeX. Cada punto se cierra con una decisión justificada, su configuración efectiva y una fuente o versión de código identificable. Las decisiones nuevas se distinguen de los valores reconstruidos a partir de registros.

## Condiciones adoptadas

- Los cuatro algoritmos participan en ambas fases de búsqueda. La fase 1 de Mendoza comienza después de A–E y A/C y conserva los dominios iniciales por algoritmo, salvo el peso vecinal, que fija en ρ=0. Esta excepción fue confirmada por el autor el 13 de octubre y ratificada el 14 de octubre de 2026. Los límites de fase 1 son comunes: 100 propuestas iniciales por estudio, ampliables hasta 150; 40 iteraciones máximas; ASHA con gracia 10 y reducción 4; diagnóstico cada diez iteraciones. A/C modifica conjuntamente observación y recompensa: orienta la decisión, sin identificar un efecto aislado de ρ. Los dominios urbanos de fase 2 provienen de la fase 1 de Mendoza.
- Búsqueda, selección y entrenamiento urbano: inicio en 1500 s, calentamiento de 300 s y control en [1800,9000).
- Evaluación final urbana: [0,43200), sin calentamiento. Se especifica su contrato; la preparación no incluye crear ni ejecutar un evaluador final.
- El entrenamiento final comienza desde cero, utiliza el presupuesto completo de la búsqueda que aporta la configuración y conserva el checkpoint de última iteración.
- El panel urbano común de cinco semillas es el punto inicial acordado. Su tamaño necesita justificación operativa y debe fijarse antes de utilizarlo para seleccionar.
- La evaluación final mantiene veinte simulaciones por combinación con configuración seleccionada: 320 si se cubren las dieciséis combinaciones. Las estadísticas describen variación entre simulaciones del modelo evaluado.

## Checklist

- [x] **MDZ-01 — Escenario y demanda.** Identificar la versión definitiva y conservar un manifiesto con red, rutas, archivos adicionales, programas semafóricos, configuraciones SUMO, hashes y versiones. Precisar el perfil, volumen nominal y distribución OD efectivos; distinguir v14 de sus variantes y conservar separados los perfiles y las especificaciones históricas 60/40 y 70/30.

- [x] **MDZ-02 — Operación y referencia.** Vincular referencia y entorno aprendido con las ventanas adoptadas. Precisar inicialización, agentes, acciones, máscaras, tiempos semafóricos, memoria de espera, teletransportes, cierres anticipados y tratamiento de terminación y truncamiento.

- [x] **MDZ-03 — Señales y calibración.** Registrar la calibración urbana de max_lane_value con señal, unidades, percentil, semillas, ventanas y archivo consumidor. Documentar observación y recompensa por algoritmo y fase, incluido rho y la normalización por carriles; añadir calibración vecinal cuando se utilice.

- [ ] **MDZ-04 — Fase 1 urbana.** Completar los puntos de entrada, mapas de semillas y contratos para MAPPO, HAPPO, IPPO e IDQN, con los dominios iniciales compartidos salvo ρ=0. Documentar arquitecturas, propuestas, iteraciones máximas, ASHA, seguimiento diagnóstico, objetivo y semillas.

- [ ] **MDZ-05 — Fase 2 urbana.** Documentar las reglas y entradas que derivan los dominios desde la fase 1 de Mendoza; conservar el procedimiento y los dominios versionados. Precisar arquitecturas, presupuestos, semillas, objetivo y recompensa efectivos.

- [ ] **MDZ-06 — Candidatos.** Definir cantidad, tratamiento de arquitecturas y requisitos técnicos de presupuesto completo, métricas, configuración y checkpoint legibles. Vincular cada candidato con su ensayo, sin importar automáticamente las 60 iteraciones ni los filtros sintéticos.

- [ ] **MDZ-07 — Panel de selección.** Justificar y fijar su tamaño antes de seleccionar; cinco semillas es el punto inicial, no una garantía estadística. Comprobar las mismas condiciones para referencia y candidatos, los tres criterios por semilla, la media con igual peso, los desempates y el caso sin admisibles. Coordinar cualquier cambio de tamaño con el protocolo y su documentación.

- [ ] **MDZ-08 — Aleatoriedad efectiva.** Registrar la generación de semillas por función y campaña, sus separaciones y los valores recibidos por SUMO. Verificar procesos y restauraciones del calentamiento. Mantener identificado el archivo congelado de demanda y excluir 104729 del panel final urbano.

- [ ] **MDZ-09 — Entrenamiento final.** Conservar una receta por combinación con hiperparámetros, arquitectura, entorno, semilla nueva y presupuesto concreto. Vincular el checkpoint de última iteración con final_declared_budget y comprobar su restauración y correspondencia con training_iterations.

- [ ] **MDZ-10 — Métricas y registros.** Precisar identificadores por agente, las dos medidas locales y sus ponderaciones, Gini, espera de viaje, inserciones, CI, pérdida temporal e inicios de teletransporte. Mantener la cohorte por inserción efectiva, incluir viajes inconclusos y distinguir espera local, waitingTime y departDelay.

- [x] **MDZ-11 — Contrato de evaluación final.** Conservar veinte simulaciones por combinación, semillas registradas y separadas de selección, sin panel común entre algoritmos, y políticas fijas sin exploración. Precisar medias por simulación, desviación muestral con divisor 19, veinte valores válidos por resumen y tratamiento de valores indefinidos o cierres anticipados. Examinar los diagnósticos del modelo final independientemente de la selección, sin filtros retroactivos ni inferencia A/C añadida. Este punto es documental.

- [ ] **MDZ-12 — Coherencia documental.** Preparar los parámetros y fuentes que completan cuerpo y apéndice; coordinar tablas, flujo y referencias. Conservar A/C y los antecedentes históricos. Revisar el capítulo completo en orden y validar LaTeX y PDF cuando cambie texto visible.

## Evidencia de esta preparación — 2026-10-13

Informe: [informe-cierre-mendoza-metodologia.md](informe-cierre-mendoza-metodologia.md). Las fuentes de código y los manifiestos están en `/home/juanm4/Dev/marl-tlc`; se conserva la rama `v15-mendoza-fixed-tls-study` y el trabajo previo de ambos repositorios. Esta preparación no ejecuta HPO, selección, entrenamiento final ni evaluación final, y no modifica el manuscrito.

| Punto | Evidencia y verificación | Alcance de cierre / requisito restante |
|---|---|---|
| MDZ-01 | `docs/mendoza_preparation/initial_inventory.json`, `preparation_manifest.json`; `urban/protocol.json`, `frozen_resources`; red SHA `988a1d27…`, ruta `e7380990…`; resolución SUMO y programas 17/56 comprobados. Informe §1: volumen nominal, integral de tasas, conteos muestreados y procedencia 60/40 vs 70/30 separados. | Cerrado para el escenario que se consumirá. La matriz original 70/30 sigue ausente y se documenta esa limitación. |
| MDZ-02 | `mendoza_hpo_v14.sumocfg`, `mendoza_evaluation_v14.sumocfg`; `runtime_smoke.json`; `sumo_env.py`; tests urbanos de calentamiento, referencia, RNG, truncamiento y cero calentamiento. 73 agentes, máscara y ventanas verificadas. | Cerrado el contrato operativo. Las corridas históricas con inicio directo en 1800 s no se equiparan al panel con calentamiento. |
| MDZ-03 | `encoder_calibration.json` y `calibration.log`: memoria explícita 1000 s, dos semillas 5001/5002, 14400 muestras, P99=5396,04 veh·s, M=5396; recursos y consumidor comprobados. Rho=0 y observación local en las ocho celdas. | Cerrado para las señales urbanas adoptadas. M=1494 histórico se conserva; la calibración nueva es una envolvente conservadora de la señal atribuida a carriles. No corresponde calibración vecinal. |
| MDZ-04 | Runner Phase 1 y submitters adaptados a protocolo propio; la preparación anterior conserva `phase1.proposals_per_architecture=50`, ocho celdas y 400 propuestas; semillas por función y pruebas de parámetros efectivos. | Abierto: alinear protocolo, validador y submitters con la decisión del autor del 14/10: 100 propuestas iniciales, ampliables hasta 150; 40 iteraciones; ASHA 10/4; diagnóstico cada diez iteraciones. Precisar concurrencia, fallas, reanudaciones y recursos del clúster. |
| MDZ-05 | `urban/refinement.py`: reglas y validador exclusivos de ocho estudios completos de Mendoza. Runner/submitter Phase 2 consume protocolo urbano y dominios con hash. | Abierto: producir Phase 1 urbana, dominios concretos versionados y presupuesto completo de Phase 2. No se importan dominios sintéticos. |
| MDZ-06 | `urban/selection.py`, `audit_results`, `load_audited_study`, `candidate_panel`; tests de legibilidad/procedencia, presupuesto, arquitectura y restore. Hasta tres candidatos por algoritmo. | Abierto: lista real de candidatos con métricas y checkpoints de presupuesto urbano completo. |
| MDZ-07 | Cinco semillas predeclaradas; coste máximo 65 simulaciones de 2 h; ranking puro probado con tres criterios por semilla, pesos iguales, desempates y caso sin admisibles. | Abierto: medir coste/variabilidad de referencia, ratificar tamaño antes de seleccionar (`panel_size_accepted=false`) y ejecutar el panel completo. |
| MDZ-08 | `urban/seeds.py` / `seeds.json`; exclusiones y separaciones comprobadas; `seed_runtime_verification.json` consulta la semilla real antes/después de reset; `runtime_smoke.json` comprueba RNG restaurado. | Abierto: verificar y guardar evidencia de opciones/semillas en workers reales del clúster. La reanudación positiva y los reintentos siguen bloqueados hasta verificar persistencia del historial del objetivo; por ahora el preflight solo acepta valores cero para ambos límites. |
| MDZ-09 | `final_recipe` exige presupuesto de origen; `verify_final_checkpoint` restaura con API pública, compara iteración y cierra instancia; contrato `from_scratch` / `final_declared_budget`. | Abierto: cuatro recetas seleccionadas donde haya admisibilidad, sus entrenamientos y checkpoints reales con restauración verificada. El test del verificador usa un restaurador controlado. |
| MDZ-10 | Informe §8: IDs, dos medidas locales y ponderaciones, Gini, cohorte, espera, CI, pérdida temporal, departDelay e inicios de teletransporte; consumidores identificados. | Abierto: el compacto actual conserva la primera medida local por agente y resúmenes de equidad; el registro final debe conservar también la segunda medida por ID y sus acumuladores. No se implementa el evaluador final en esta preparación. |
| MDZ-11 | Informe §8 y `urban/protocol.json`, `final_evaluation`: veinte semillas propias por algoritmo; ventana diaria sin calentamiento; políticas fijas; medias con igual peso, divisor 19, veinte valores válidos, indefinidos y fallos documentados. | Cerrado el contrato documental solicitado. No acredita evaluaciones ejecutadas ni variabilidad entre entrenamientos. |
| MDZ-12 | Informe de ocho secciones con tabla Parámetro / Valor y unidad / Justificación / Fuente exacta; propuestas LaTeX, ubicaciones, etiquetas y correspondencias; A/C y antecedentes conservados. | Abierto: incorporar las propuestas, completar cifras pendientes, coordinar cuerpo/apéndice/figuras y compilar/revisar PDF en la etapa posterior. |

Verificaciones y comandos: `docs/mendoza_preparation/verification.json`, `verification_tests.log`, `final_urban_tests.log` y `evidence_sha256.json`. Se usan la venv, libsumo real en smokes breves, compilación Python, sintaxis shell y `git diff --check`. El manifiesto inicial y las diferencias previas se conservan; los cierres del checklist se limitan a requisitos con evidencia efectiva.

## Revisión e integración en la tesina — 2026-10-13

Se contrastó el informe con la copia real de `marl-tlc`, rama `v15-mendoza-fixed-tls-study`, HEAD `6081522`, incluidos sus cambios locales. Coinciden los 78 hashes revisados de recursos, implementación, calibración y aceptación del backend. Esta comprobación identifica los archivos consultados; no reemplaza los manifiestos de cada campaña. El informe de ocho secciones se conserva como antecedente.

La aclaración posterior del autor resuelve la diferencia con el espacio inicial común: la fase 1 urbana comienza después de A/C y fija ρ=0. La metodología conserva esa secuencia y la decisión de recompensa local, y mantiene el alcance conjunto del contraste A/C sobre observación y recompensa.

Se incorporaron a `5-metodologia.tex` y `8-apendice_arquitectura.tex` las configuraciones v14, los programas de referencia 17/56, la calibración urbana de M=5396 y su memoria de 1000 s, la restauración RNG por semilla, el cierre urbano por truncamiento, las 50 propuestas por cada uno de ocho estudios, las reglas urbanas de refinamiento, candidatos, semillas y checkpoint. Se precisaron los valores indefinidos y las repeticiones técnicas en el procedimiento final. El cálculo de 720 pasos por episodio quedó delimitado a las redes sintéticas; el urbano utiliza 1440.

Las fuentes nuevas de SUMO sobre guardado de estado y teletransportes se citan en el texto y tienen entradas BibTeX compatibles. La compilación con `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` produjo un PDF de 163 páginas. Se regeneraron los glosarios: sus logs finales no rechazan entradas. El log LaTeX final conserva únicamente la advertencia conocida de `tracklang`, sin desbordes ni referencias o citas indefinidas. Se comprobaron las páginas de apertura, flujo, entorno, calibración, horizontes, fase 1, selección, evaluación final y protocolo urbano. No se retiraron etiquetas ni ecuaciones numeradas existentes; se añadió únicamente `subsec:protocolo_urbano_mendoza`.

MDZ-12 queda parcialmente cerrado por la integración y la verificación documental. Para fijar todas las cifras del procedimiento, `urban/protocol.json` requiere estos valores concretos:

| Ámbito | Campos o decisiones por completar | Consecuencia |
|---|---|---|
| Ambas fases | `training_iterations`, `grace_period`, `reduction_factor`, `eval_interval`, `max_failures`, `max_concurrent`, `resume_limit` siguen en `null`. | Determinan presupuesto, ASHA, diagnóstico y condiciones de ejecución. El entrenamiento final hereda el presupuesto de su fase de origen; no se le asigna un valor sintético por analogía. |
| Fase 2 | `proposals_per_architecture`, `domains`, `domains_sha256` siguen en `null`. | El presupuesto necesita una decisión propia; los dominios y su hash son productos de la fase 1 urbana bajo las reglas documentadas. |
| Panel común | Cinco semillas es la decisión adoptada; el archivo conserva `panel_size_accepted=false`. | Coordinar el indicador con la decisión y su justificación de coste. El máximo de 65 simulaciones es una cota operativa, no una garantía de precisión estadística. |
| Aleatoriedad y registros | Conservar opciones efectivas en cada proceso, receta seleccionada y ambas medidas locales por identificador de agente. | La comprobación breve del backend se distingue de la trazabilidad de los productos de cada campaña. |

Las recetas y los dominios concretos se documentan como productos de los procedimientos; sus valores no se completan antes de obtener esas entradas. Los pendientes quedan en este checklist, fuera del manuscrito LaTeX. El prompt siguiente incorpora la aclaración del autor sobre ρ.

### Actualización del 14 de octubre: límites comunes de fase 1

Esta actualización sustituye la definición anterior de 50 propuestas por arquitectura. El autor fija los mismos límites de búsqueda de fase 1 en los cuatro escenarios: 100 propuestas iniciales por estudio, ampliables hasta 150; 40 iteraciones máximas; gracia de ASHA de 10 iteraciones; factor de reducción 4; diagnóstico cada diez iteraciones. En Mendoza se conservan ρ=0, observación local, sus semillas y las condiciones del escenario. Los ocho estudios urbanos suman 800 propuestas iniciales.

Debe alinearse `urban/protocol.json` y sus validadores con estos valores: `urban/protocol.py` exige actualmente 50 y `scripts/slurm/submit_phase1.sh` fuerza `NUM_SAMPLES=50` para Mendoza. La gestión de extensiones debe respetar el máximo común de 150 y conservar la identidad y procedencia del estudio. Los campos de fase 1 en `null` se completan con los valores fijados por el autor; los de fase 2 requieren su definición propia. El informe del 13 de octubre se conserva como antecedente, sin sobrescribirlo.

## Prompt completo para el coding agent

```text
Trabaja en /home/juanm4/Dev/marl-tlc y consulta la metodología de la tesina en /home/juanm4/Documentos/tesina, especialmente 5-metodologia.tex y 8-apendice_arquitectura.tex. Completa un escenario de Mendoza reproducible y define los contratos necesarios para las dos fases de búsqueda, la selección y el entrenamiento final de MAPPO, HAPPO, IPPO e IDQN.

Lee los AGENTS.md aplicables, registra rama, HEAD y cambios locales de ambos repositorios, y preserva el trabajo ajeno. Contrasta cada decisión con código, configuraciones y documentación identificables. Cuando fijes un valor nuevo, identifícalo como decisión de diseño y justifícalo por las restricciones del escenario; no lo atribuyas a registros históricos. Implementa las adaptaciones y configuraciones necesarias, con cambios acotados y verificaciones breves. Las campañas completas quedan fuera de esta preparación. La evaluación final se especifica documentalmente: no crees ni ejecutes un evaluador final.

1. Escenario y demanda. Identifica la versión urbana que utilizará la tesis y conserva un manifiesto con red, rutas, archivos adicionales, programas semafóricos, configuraciones SUMO, hashes y versiones. Distingue el escenario v14 de sus variantes posteriores. Documenta el perfil horario, volumen nominal, distribución OD y generación de demanda efectivos. Mantén separados los perfiles históricos y las especificaciones 60/40 y 70/30. Conserva los archivos históricos; cualquier escenario derivado debe tener sus propios archivos y justificación. Una semilla SUMO no sustituye el archivo de rutas ni sus parámetros.

2. Operación. Parte de las ventanas adoptadas: búsqueda, selección y entrenamiento urbano comienzan en 1500 s, incluyen 300 s de calentamiento y controlan [1800,9000); la evaluación final contempla [0,43200), sin calentamiento. Vincula esas condiciones con los archivos realmente consumidos. Identifica los programas de referencia, sus tipos, y la inicialización de referencia y políticas. Verifica agentes, carriles, acciones, máscaras y tiempos semafóricos. Precisa memoria de espera, teletransportes, cierres anticipados y tratamiento de terminación y truncamiento por el aprendiz.

3. Señales y calibración. Documenta observación y recompensa por algoritmo y fase, incluido rho y la normalización por carriles. No generalices la formulación vecinal C ni la recompensa local refinada sintética a todos los procedimientos. Vincula max_lane_value con la calibración urbana efectiva: señal, unidades, percentil, semillas, horizonte y archivo consumidor. Añade calibración vecinal únicamente cuando corresponda.

4. Búsquedas. Comprueba y completa el soporte urbano en los puntos de entrada, mapas de semillas y contratos de las dos fases para los cuatro algoritmos. La fase 1 de Mendoza comienza después de A–E y A/C y comparte los demás dominios iniciales por algoritmo, pero fija ρ=0 y observación local. Aplica los límites comunes fijados por el autor: 100 propuestas iniciales por estudio, ampliables hasta 150; 40 iteraciones; ASHA con gracia 10 y reducción 4; diagnóstico cada diez iteraciones. Actualiza los validadores y submitters que todavía fijan 50, y conserva la procedencia e identidad de los estudios al gestionar extensiones. Mantén las condiciones del escenario y sus semillas. Conserva la decisión de ρ=0 sin atribuir al contraste A/C un efecto aislado del coeficiente. Los dominios de fase 2 deben derivarse de la fase 1 de Mendoza mediante reglas explícitas y un procedimiento reproducible; sus límites y dominios concretos necesitan documentación propia. No traslades semillas ni límites de fase 2 por analogía.

5. Selección. Define la lista de candidatos urbanos y su admisibilidad técnica: presupuesto completo, métricas válidas, configuración y checkpoint legibles. Usa un panel común para candidatos y referencia. Cinco semillas es el punto inicial acordado; justifica y fija su tamaño antes de seleccionar mediante coste y variabilidad diagnóstica pertinente. En cada semilla, exige igualar o superar inserciones y CI de la referencia y no exceder sus inicios de teletransporte. Entre los admisibles, elige la menor espera media con igual peso por simulación. Conserva los desempates de la metodología y precisa el caso sin candidatos admisibles.

6. Aleatoriedad. Registra las semillas por función y campaña, su generación y las separaciones requeridas entre búsqueda, selección y evaluación final. Verifica el valor efectivo recibido por SUMO, incluidos procesos y restauraciones del calentamiento. La evaluación final urbana excluye 104729; sus semillas son aleatorias y registradas, sin imponer un panel común entre algoritmos.

7. Entrenamiento final. Define una receta por combinación: hiperparámetros seleccionados, arquitectura, entorno, semilla nueva y presupuesto concreto. Conserva la regla metodológica del presupuesto completo de la búsqueda que aporta la configuración. El entrenamiento comienza desde cero. Vincula el checkpoint de última iteración con final_declared_budget y verifica que la iteración restaurada coincida con training_iterations.

8. Métricas y contrato final. Precisa los registros individuales por agente y los globales de red. Distingue las dos medidas locales y sus ponderaciones de waitingTime por viaje; registra inserciones, CI, pérdida temporal, Gini e inicios de teletransporte con sus unidades. Usa la cohorte de inserción efectiva dentro de la ventana e incluye viajes inconclusos. El contrato final conserva veinte simulaciones por combinación, políticas fijas sin exploración, media entre simulaciones y desviación muestral con divisor 19. Define valores indefinidos y cierres anticipados. Los diagnósticos del modelo final se examinan independientemente del candidato seleccionado, sin filtros retroactivos; la dispersión entre simulaciones no representa variabilidad entre entrenamientos.

Entrega configuraciones y código verificables, manifiestos, comandos reproducibles y una tabla que relacione cada decisión con su justificación y fuente exacta. Actualiza el checklist de /home/juanm4/Documentos/tesina/TODO-mendoza-metodologia.md con los archivos y verificaciones que cierran cada punto. Prepara la especificación necesaria para completar la metodología con redacción académica natural, sin estados de avance ni TODO dentro del LaTeX. Conserva A/C y las campañas históricas. Explica el diff y las verificaciones realizadas; si cambias texto visible de la tesis, coordina cuerpo, apéndice, tablas y figuras, compila y revisa el PDF.
```

## Coordinación con la revisión de metodología — 14 de octubre de 2026

El capítulo distingue ahora los límites comunes de fase 1 de la excepción de Mendoza (ρ=0 y observación local, tras A–E y A/C) y de las condiciones que dependen de cada red. La cifra de 100 propuestas y 60 iteraciones se identifica como propia de la fase 2 sintética. La alineación del protocolo urbano de fase 1 con los límites comunes permanece en MDZ-04; los valores y dominios propios de fase 2 urbana, en MDZ-05.

