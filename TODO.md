# TODO — pendientes tras la revisión de metodología

Origen: revisión profunda de `5-metodologia.tex` (septiembre 2026) contrastada con las referencias exactas `tuning` (`79262e54`) y `cluster` (`f16076fb`) de `/home/juanm4/Dev/marl-tlc`. El texto de la tesis ya describe fielmente el código vigente; estos ítems quedan abiertos del lado de la implementación y de los resultados.

## Campaña de Mendoza (tesis: §HPO, §Evaluación)

- [ ] Ejecutar el pipeline de HPO para el escenario de la Ciudad de Mendoza. En ambas ramas el protocolo lo declara `blocked_until_synthetic_lock` sin presupuesto (`experiments/marl_experiments/tuning/shared/protocol.py`, claves `scenarios` y `status`); `shared/seeds.py` no tiene entradas para Mendoza. Al desbloquear: definir y registrar semillas de entrenamiento, evaluación de HPO, confirmación y reservadas, más el presupuesto (`trials`, iteraciones), antes de seleccionar candidatos.
- [ ] Volcar esos valores concretos en `5-metodologia.tex` (hoy describe la secuencia protocolar de Mendoza sin enumerar sus semillas; los huecos se llenan al cerrar resultados).
- [ ] Calcular el GEH del escenario canónico v14 con la hipótesis de retención declarada (`camera_retention = 1,0`), archivo `mendoza_12h.rou.xml` y ventana explícita. Los únicos valores GEH archivados (`cluster:experiments/mendoza_scenario/SCENARIO_95_VALIDATION.md`) corresponden a la hipótesis histórica 0,95 y no deben mezclarse con el canónico.

## Métricas de demanda (tesis: ecuación \eqref{eq:tasa_completitud}, tablas de calibración y validación)

- [ ] Decidir si se exhibe un único cociente de completitud en todas las tablas. Estado actual: la calibración sintética por bisección computó `arrived/departed` (verificado en `cluster:experiments/fixed_tls/fixed_tls_reports/calibration_results_cr0p70_4200_current.json`), y la tesis la reetiquetó correctamente como \acrshort{acr-ci}. Los JSON guardan `pending_vehicles_end` y `throughput`, suficiente para recalcular la CR sobre demanda cargada sin rerutear, si se prefiere unificar bajo CR.
- [ ] Persistir en la campaña MARL los contadores `loaded`/`pending_vehicles_end` al cierre del episodio (hoy `sumo_env.py` registra `inserted`, `arrived` y `arrived_inserted`, pero no `pending`/`loaded`). Sin ellos, CR no es recomputable desde los logs de entrenamiento y la tabla de Mendoza depende de los artefactos de `fixed_tls`.

## HAPPO (tesis: §Formulación del modelo Dec-POMDP, viñeta de \acrshort{acr-happo}; opcional, no bloqueante)

- [ ] La tesis describe ahora el procedimiento realmente ejecutado: anidación epoch→agentes, un paso full-batch por actor y epoch, `M` reinicializado en cada epoch, coeficiente de \acrshort{acr-kl} fijo y `minibatch_size`/`kl_target` inertes en HAPPO (dimensiones efectivas: 12 de 14 nominales). Verificado en `src/marlTLC/agents/multi_agent/happo/torch/happo_torch_learner.py` (ambas ramas, blob idéntico).
- [ ] Si en el futuro se quisiera HAPPO canónico (orden único por rollout, pases internos de cada actor con minibatches reales, factor secuencial acumulado sin reinicio, scheduling adaptativo de KL, espejo de `PKU-MARL/HARL`): es un cambio de algoritmo que invalida los estudios HAPPO en curso y exigiría re-ejecutar su HPO y confirmación. Decidir solo con tiempo holgado; la redacción actual no lo requiere.

## Cierre de resultados (tesis: `6-resultados.tex`, hoy esqueleto de 32 líneas)

- [ ] Completar el capítulo cuando estén todas las corridas: tablas por escenario y algoritmo con media, mediana, desviación e intervalo bootstrap percentil; confirmación pareada (`paired_bootstrap`, 20.000 remuestreos, semilla 910001); comparación relativa contra el tiempo fijo del mismo escenario; `num_env_steps_sampled` de cada receta final (la metodología promete reportar la experiencia consumida); valores GEH v14 del punto anterior; resultados de Mendoza para los cuatro algoritmos.
- [ ] Registrar en un manifiesto el entorno efectivo de las corridas finales (versiones exactas de Python, SUMO, Ray, PyTorch, Optuna; `requirements.txt` solo fija rangos mínimos).

## Verificaciones menores

- [ ] Verificar en runtime (no solo estático) que el selector de candidatos de la campaña final coincide con el descripto: rechaza métricas ausentes, no numéricas o `NaN`; la finitud la garantiza el lector de `TripInfo` (`src/marlTLC/environments/tripinfo_metrics.py`), que aborta ante atributos infinitos o negativos e identificadores duplicados.
- [ ] Confirmar que ninguna corrida activa depende de cambios del árbol sucio de `tuning` no commiteados (protocolo, selector y submitter están modificados sin versionar); comitear el estado con el que se generen los resultados definitivos.
- [ ] Al terminar ediciones de este ciclo: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` y revisar `main.log`. Pendiente preexistente conocido: overfull de 3,9pt en `1-agradecimientos.tex` (líneas 19–21), ajeno a metodología.
