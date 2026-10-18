# Preparación de Mendoza e informe de cierre metodológico

Fecha: 13 de octubre de 2026. Alcance: preparación técnica, contratos y propuestas de redacción; las búsquedas, el panel de selección, los entrenamientos finales y las evaluaciones finales quedan para las campañas posteriores. Las propuestas LaTeX de este informe no se incorporan al manuscrito.

Se distinguen **C** (comprobación de archivos o ejecución breve), **D** (decisión nueva del protocolo), **R** (cálculo derivado) y **P** (dependencia pendiente). Un contrato implementado no acredita una campaña ejecutada ni un resultado experimental.

Las rutas de código de este informe son relativas a `/home/juanm4/Dev/marl-tlc`; las del manuscrito, a `/home/juanm4/Documentos/tesina`. La fuente íntegra de trazabilidad es [initial_inventory.json](/home/juanm4/Dev/marl-tlc/docs/mendoza_preparation/initial_inventory.json): guarda el estado anterior a esta intervención, hashes de fuentes y diferencias de ambos repositorios. Los archivos ajenos se conservan.

| Repositorio | Rama y HEAD inicial | Estado previo |
|---|---|---|
| MARL-TLC | `v15-mendoza-fixed-tls-study`, `6081522f1bb108f7faceb02cc52be345b6f4bba4` | Modificaciones y archivos locales de estudios anteriores; inventario y `marl_tlc_initial.diff` conservados. |
| Tesina | `main`, `464b9121a657e1ab0c2f47e5d1b4f11bbd455e13` | Cambios previos en marco teórico, metodología, apéndice, glosario, figura y PDF; `tesina_initial.diff` conservado. |

La preparación usa Python 3.13.16, Ray 2.53.0, Torch 2.10.0, Optuna 4.7.0, NumPy 2.2.6 y bibliotecas SUMO 1.26.0 de la venv. `libsumo.getVersion()` devuelve API 22 / SUMO 1.26.0. El ejecutable `/home/juanm4/sumo/bin/sumo` informa `v1_25_0+0570-f59cd14e561`; es el que aparece en las comprobaciones de referencia existentes. Sus hashes y el ejecutable de sistema se registran en [preparation_manifest.json](/home/juanm4/Dev/marl-tlc/docs/mendoza_preparation/preparation_manifest.json). No se atribuyen al nuevo backend los resultados de SUMO 1.25.

## 1. Escenario congelado, demanda y procedencia

**C/D.** Se adopta v14 con la red mixta y el archivo de flujos congelados. Los archivos de v15 y los candidatos de semáforos estáticos conservan su procedencia separada. El manifiesto enumera los 73 programas, sus identificadores, fases, tipo y offset: 17 estáticos y 56 accionados. La ausencia de detectores explícitos en XML no demuestra ausencia de actuación.

| Recurso consumido | SHA-256 |
|---|---|
| `nets/Mendoza/gran_mendoza2_fixed.net.xml` | `988a1d277fec9188aea5996b96dd9aa1893781e1d0fa4c85770a0c7415274a86` |
| `nets/Mendoza/mendoza_12h.rou.xml` | `e7380990e07dbaea1df2cf1013d3ee886b92820ad74f6064786f1082b6716055` |
| `nets/Mendoza/gran_mendoza2_fixed.taz.xml` | `cf710f36e1c5021d3d3e585d897262310579bf1c34466ecca6290e1715923e40` |
| `nets/Mendoza/gran_mendoza2.add.xml` | `fe96f276987b8f9ccd71736a76a8524eb948b192b2326221b92f4959749b8a38` |
| Especificación OD actual, `experiments/mendoza_scenario/mendoza_od_proportions.json` | `82c5cc1932c9e755f4284fb2639fa51dd34592667fc126ace77ed86f57b8c4a7` |

Se comprueba la resolución relativa de `net-file`, `route-files` y `additional-files` desde cada configuración. La mezcla de vehículos está **embebida en la ruta**: `td_urban_mix`, proporciones 0,25/0,60/0,15, aplicada a los 6204 flujos. El archivo adicional consumido contiene polígonos; no sustituye a esos tipos.

**C.** El `gen.log` de `experiments/mendoza_scenario/results/scenario_canonico_v14/seed_search/s104773/` informa 32 días seleccionados, 260000 veh/día nominales, expansión 10,327359932077748, `camera_retention=1`, 181 pares explícitos y reparto 70/30 desde `od_calibrated_7030.json`. Esa matriz y la ruta original nombrada en los logs no se conservan. El JSON actual tiene 476 entradas y suma 0,60; su contrato documental 60/40 se conserva **como especificación separada**, sin presentarlo como la entrada original de esos registros. El resumen histórico `results/scenario_12h/generation_summary.json` informa otros valores: 33 días, 290000 veh/día y retención 0,95. No se combinan los tres artefactos en una supuesta generación única.

El hash del archivo congelado identifica la ruta que se utilizará ahora; no prueba cuál se utilizó en una corrida histórica que carece de esa ruta. Esta limitación coincide con `8-apendice_arquitectura.tex`, etiquetas `sec:procedencia_mendoza`, `tab:fuentes_mendoza` y `tab:archivos_procedencia_mendoza`.

**R.** Para cada flujo se integra su tasa sobre la intersección con la ventana: `E = sum(rate * max(0, min(end,b)-max(begin,a)))`. En `period="exp(X)"`, X es veh/s, por lo que una tasa horaria se convierte con `X=flow/3600`. La capacidad puede limitar la inserción efectiva. [Documentación oficial de aleatoriedad de SUMO](https://sumo.dlr.de/docs/Simulation/Randomness.html).

| Magnitud | Valor | Interpretación y fuente |
|---|---:|---|
| Volumen diario nominal | 260000 veh/día | Decisión de expansión del `gen.log`; corresponde a 24 h. |
| Integral de tasas de la ruta, `[0,43200)` | 179835,800 veh | Cálculo sobre el XML congelado; 12 h, no un conteo observado. |
| Integral de tasas, `[1800,9000)` | 31083,255 veh | Demanda programada esperada del recorte de control. |
| Integral de tasas, `[1500,9000)` | 31799,716 veh | Demanda programada esperada desde el inicio del calentamiento. |
| Referencia medida existente, 2 h sin calentamiento | cargados 30629; insertados 23735; llegados 22702 | Último `<step>` a 8999 s en `original_mixed_head_tls_measurement_bounded_20261012/summary.xml`; manifiesto `completed`, SUMO 1.25. |
| Adquisición existente de 12 h | cargados 180122; insertados 143787; llegados 142997 | Último `<step>` a 43190 s en `original_mixed_head_full_day_acquisition_20261012/summary.xml`; período 10 s y manifiesto `partial`. No son los conteos exactos a 43200 s. |

Los registros finales de ambos XML indican `teleports=0` y `collisions=0` hasta su tiempo de muestreo. El manifiesto conserva el tiempo y rol de cada registro; no se infiere un cierre completo de un nombre de carpeta. La cifra documental histórica de 12 h, 180163/143819/143022, se conserva por separado con su fuente `sumo_12h.log`; no sustituye al último registro de esa adquisición posterior. Los logs históricos no contienen un contador explícito de teletransportes.

`loaded` puede incluir lectura anticipada de rutas; `waiting` representa vehículos esperando inserción. Ninguno es la integral esperada ni la cola física dentro de la red. El inicio en 1500 s incorpora vehículos antes del control y cambia el estado inicial respecto del recorte histórico que comienza directamente en 1800 s. La selección necesita una referencia nueva en sus condiciones propias.

| Hora local | Integral de tasas (veh en una hora) |
|---|---:|
| 06–07 | 8597,530 |
| 07–08 | 17415,800 |
| 08–09 | 18737,380 |
| 09–10 | 17552,640 |
| 10–11 | 16947,520 |
| 11–12 | 15048,250 |
| 12–13 | 14355,680 |
| 13–14 | 13585,320 |
| 14–15 | 13392,000 |
| 15–16 | 13756,370 |
| 16–17 | 14721,970 |
| 17–18 | 15725,340 |

Fuente exacta del cálculo: `urban/prepare.py:17`, función `expected_demand`, y campo `demand.hourly` del manifiesto. La semilla del remanente documentada es 104773; la semilla canónica de simulación es 104729. Cambiar esta última no reconstruye la OD ni el archivo de flujos.

**Propuesta LaTeX — ubicación:** `5-metodologia.tex`, `subsec:escenario_mendoza`; correspondencia con `tab:fuentes_mendoza`, `tab:archivos_procedencia_mendoza` y `sec:procedencia_mendoza` del apéndice. Mantener los antecedentes y sus resultados en sus pasajes actuales, sin trasladarlos como resultados de políticas urbanas.

```latex
El escenario urbano utiliza la red y los flujos congelados de la versión v14.
La referencia conserva 17 programas estáticos y 56 accionados. Los archivos
se identifican mediante sus códigos SHA-256, que se reúnen en el apéndice
\ref{sec:procedencia_mendoza}. El volumen nominal de 260\,000 vehículos por
día representa la escala de expansión de la demanda; los flujos de la ventana
de doce horas y las inserciones efectivas constituyen magnitudes diferentes.
La especificación OD actual de 60/40 se documenta por separado del registro
de generación de 70/30, cuya matriz original no se conserva.
```

## 2. Operación del entorno y condiciones por procedimiento

**D/C.** Se añaden dos configuraciones propias: `nets/Mendoza/mendoza_hpo_v14.sumocfg` y `mendoza_evaluation_v14.sumocfg`. Ambas consumen los cuatro recursos congelados. Las configuraciones canónicas e históricas permanecen intactas. El cambio respecto de las configuraciones MARL anteriores es declarar `time-to-teleport=300` y `max-num-teleports=-1`; se cuentan las incidencias durante toda la ventana en lugar de cerrar al primer evento. No se desactiva el mecanismo de teletransporte. Su umbral mide tiempo bloqueado, no duración total del viaje. [Documentación oficial sobre teletransportes](https://sumo.dlr.de/docs/Simulation/Why_Vehicles_are_teleporting.html).

| Procedimiento | Inicio SUMO | Calentamiento | Control | Condición de aleatoriedad |
|---|---:|---:|---|---|
| Calibración nueva | 1500 s | 300 s | `[1800,9000)` | 5001 y 5002; programas mixtos nativos. |
| Phase 1 urbana | 1500 s | 300 s | `[1800,9000)` | Roles separados por estudio; `rho=0`. |
| Phase 2 urbana | 1500 s | 300 s | `[1800,9000)` | Nuevos roles por estudio; `rho=0`. |
| Candidatos y referencia de selección | 1500 s | 300 s | `[1800,9000)` | Cinco semillas comunes y registradas; tamaño aún pendiente de ratificación operativa. |
| Entrenamiento urbano final | 1500 s | 300 s | `[1800,9000)` | Semillas nuevas de aprendizaje y SUMO por algoritmo. |
| Evaluación urbana final | 0 s | 0 s | `[0,43200)` | Veinte semillas por algoritmo; contrato documental. |
| Comprobaciones históricas | 0 o 1800 s | Sin calentamiento añadido | 12 o 2 h | 104729; no constituyen el panel urbano nuevo. |

El constructor lee el inicio de la configuración: `sim_start=begin+warming_time`, `sim_end=sim_start+sim_time`. El horizonte de 7200 s representa exclusivamente el control y produce 1440 decisiones de 5 s. Se valida que el fin configurado alcance el fin requerido. El calentamiento avanza hasta el tiempo absoluto 1800 s; un calentamiento cero ya no llama a `simulationStep(0)`, que avanzaría un paso en SUMO.

La referencia conserva el programa activo durante calentamiento y control. Se corrigió `_warming_up_simulation` para que `fixed_tl=True` no fuerce un estado todo rojo; aquí ese nombre significa conservar el programa nativo, incluso si es accionado. Las políticas utilizan los movimientos agrupados de la red y el estado seguro todo rojo al abrir el control. El estado posterior al calentamiento se guarda con RNG y se restaura en cada episodio. Las inicializaciones difieren por diseño; no se atribuye a aprendizaje aislado toda diferencia respecto de la referencia.

**C.** El smoke real registra 73 identificadores SUMO como agentes. Se conservan 4 acciones `Discrete(1)`, 67 `Discrete(2)`, una `Discrete(3)` y una `Discrete(4)`. Los carriles controlados únicos por agente se distribuyen como 3×2, 4×9, 5×32, 6×15, 7×11, 8×3 y 10×1; la observación local tiene `1+n_carriles`, entre 4 y 11 coordenadas. Un agente con una acción sigue aportando información y recompensa. Los identificadores y tamaños individuales están en `runtime_smoke.json`.

`TrafficLight._build_phases` excluye fases amarillas del conjunto de acciones y agrega la fase segura de inicialización. La máscara permite mantener la fase cuando no se cumple el verde mínimo; actor PPO y módulo DQN aplican la máscara en sus consumidores propios. Se mantienen amarillo de 4 s y verde mínimo de 5 s. Fuente: `traffic_light.py:211`, `:214`, `:277`, `:330`, `:407`; `core/algo_factory.py`, `_build_policy_specs`; `tests/test_action_masking_ippo_idqn.py`.

El protocolo fija `terminate_on_empty=False`. En el corte temporal urbano se emite `terminated=False`, `truncated=True`, por agente y globalmente; el consumidor de GAE recibe ambos indicadores y puede conservar el valor de continuación. Se mantiene el comportamiento histórico de terminación dual para procedimientos que no activan `time_limit_as_truncation`. Una interrupción, error del simulador o cierre anterior al fin no se convierte en observación válida del panel. `checkpoint_at_end` puede guardar un ensayo podado; la igualdad con el presupuesto declarado sigue siendo obligatoria para hacerlo candidato.

Fuentes efectivas: `sumo_env.py:282`, `:402`, `:579`, `:684`; `mappo/connectors/general_advantage_estimation.py:246`; `urban/protocol.py`, `environment_contract`; pruebas `test_real_sumo_warmup_reference_rng_and_truncation` y `test_zero_warmup_does_not_advance_one_second`.

**Propuesta LaTeX — ubicación:** `subsec:ciclo_episodico`, `sec:stack_tecnologico` y `sec:parametros_sumo`; coordinar `tab:horizontes_simulacion` y `fig:informacion_controladores`.

```latex
En Mendoza, el simulador comienza en $t=1500$ s y conserva los programas de
la red durante 300 s de calentamiento. El control comprende $[1800,9000)$,
con una decisión cada cinco segundos. La referencia mantiene sus programas
estáticos y accionados; las políticas comienzan desde el estado seguro del
entorno. Al alcanzar el horizonte, el episodio se registra como truncado.
El estado del generador aleatorio se conserva junto con el calentamiento.
```

## 3. Observación, recompensa y calibración efectiva

**D/C.** Las dos fases urbanas y el entrenamiento final usan observación local, máscara de acciones y `neighborhood_relevance=0.0`. El constructor de recompensa resuelve `diff_cumulative_waiting_time_with_neighbors` como composición canónica, pero su valor efectivo es únicamente `prev_acc_waiting_time-acc_waiting_time`; no se divide por carriles ni por vehículos. MAPPO y HAPPO usan crítico centralizado durante entrenamiento; IPPO y IDQN conservan módulos independientes. Todos los actores urbanos reciben la fase actual y la señal codificada de cada carril local.

La fase 1 sintética conserva su dominio vecinal histórico. La fase 2 sintética fija recompensa local. La condición C de A/C incorpora observación y recompensa vecinal normalizadas por carriles. Estas tres formulaciones se mantienen separadas de la nueva decisión urbana. La comparación A/C conserva su alcance específico para MAPPO y las tres redes sintéticas.

**C.** La calibración histórica `.encoder_M.json` contiene M=1494, P99, dos semillas 5001/5002 y ventana 2 h. Su script no declaraba la memoria de espera, mientras el entorno de aprendizaje fija 1000 s. Se conserva esa evidencia y se crea una calibración separada con memoria explícita de 1000 s:

```bash
LIBSUMO_AS_TRACI=1 SUMO_HOME=/home/juanm4/sumo .venv/bin/python -u \
  scripts/calibrate_encoder_m.py --scenario Mendoza --sumocfg mendoza_hpo_v14.sumocfg \
  --sim-time 7200 --warming-time 300 --trials 2 --seed 5001 \
  --waiting-time-memory 1000 --output docs/mendoza_preparation/encoder_calibration.json
```

Se registran 7200 muestras por semilla, una por segundo, y se agrupan las 14400 muestras para calcular P99=5396,040000000001 veh·s. Se redondea con `round` a **M=5396**. Los máximos por corrida son 6294 y 5116 veh·s. Fuente exacta: `calibration.log`, `encoder_calibration.json`, `scripts/calibrate_encoder_m.py`, funciones `run_simulation` y `compute_M_from_samples`.

La medida de calibración es el máximo, entre carriles controlados, de la suma de `getAccumulatedWaitingTime` de los vehículos presentes. El consumidor `Lane.calculate_acc_waiting_time` atribuye al carril actual la espera total menos la ya atribuida a otros carriles, con límite inferior cero. Por tanto, la calibración usa una **envolvente conservadora** de esa señal atribuida, no una identidad entre ambas medidas. La memoria finita de 1000 s limita la historia del vehículo; no equivale al acumulado de `TripInfo.waitingTime` por viaje. M escala la codificación y puede saturarse: no es un tiempo máximo permitido.

Los niveles `encoder_intervals` se muestrean de 4 a 64; `Encoder` usa `I=encoder_intervals-1`. Los espacios del probe urbano abarcan el máximo de ese dominio para que su límite no quede fijado accidentalmente a los seis niveles del probe histórico. La calibración no se vuelve a ajustar según el desempeño de cada ensayo. No se necesita calibración vecinal porque `neighbor_info=False`.

El runner pasa `calibration_file` al espacio inicial y registra su hash. El validador exige coincidencia de memoria, ventana, configuración y hashes de recursos, además de libsumo 1.26.0. Fuentes efectivas: `shared/search_space.py:19`, `core/env_factory.py:155`, `urban/protocol.py`, `validate_ready`; `src/marlTLC/utils/encoder.py`; `src/marlTLC/environments/lane.py`, `calculate_acc_waiting_time`.

**Propuesta LaTeX — ubicación:** observaciones y recompensas del cuerpo; calibración local del apéndice, cerca de `subsec:calibraciones_cooperacion`, conservando los valores sintéticos y vecinales existentes.

```latex
Las búsquedas urbanas fijan $\rho_{\mathrm{coop}}=0$ y utilizan observaciones
locales con máscara de acciones. La escala del codificador urbano se calibra
con los programas de referencia, una memoria de espera de 1000 s y dos
semillas reservadas para este procedimiento. El percentil 99 del máximo
de espera acumulada por carril se redondea a $M=5396$ veh\,$\cdot$\,s. Esta
medida proporciona una envolvente de la espera atribuida por el entorno;
no representa un límite de espera por viaje.
```

## 4. Las dos búsquedas y sus espacios reproducibles

**D/C.** Phase 1 usa 50 propuestas h128 y 50 h256 para cada uno de MAPPO, HAPPO, IPPO e IDQN: ocho estudios y 400 propuestas urbanas. Cada arquitectura tiene su proceso Ray y su trabajo SLURM. Una propuesta fallida o podada sigue siendo una propuesta; no se promete obtener 400 ensayos de presupuesto completo.

El runner existente `phase1_hpo/run.py:160` acepta `--urban-protocol`; consume ventanas, presupuesto y semillas del protocolo independiente `urban/protocol.json`, sin heredar silenciosamente los defaults sintéticos. Los parámetros iniciales conservan sus dominios por algoritmo, salvo la decisión expresa de fijar rho=0 y la calibración urbana. Los nombres urbanos son `p1_mendoza_rho0_v1_<algo>_mendoza_<arch>` y `p2_mendoza_rho0_v1_<algo>_mendoza_<arch>`.

| Parámetro | MAPPO / IPPO | HAPPO | IDQN |
|---|---|---|---|
| `lr` | loguniforme `[3e-5,1e-3]` | Igual | loguniforme `[1e-5,1e-3]` |
| `clip_param` | uniforme `[0,10;0,22]` | Igual | No se aplica |
| `lambda_gae` | uniforme `[0,88;0,99]` | Igual | No se aplica |
| `entropy_coeff` | uniforme `[0;0,01]` | Igual | No se aplica |
| `grad_clip` | loguniforme `[0,25;5]` | Igual | elección `{0,5;1;2;5;10}` |
| `kl_coeff`, `kl_target` | loguniformes `[0,05;0,5]`, `[0,005;0,03]` | Igual | No se aplica |
| `vf_clip_param` | loguniforme `[5;20]` | Igual | No se aplica |
| `num_epochs` | enteros 5–15 | enteros 5–18 | No se aplica |
| `train_batch_episodes` | enteros 2–12 | Igual | No se aplica |
| `minibatch_size` | `{128,256,512}` | Mismo dominio declarado; actualización efectiva por lote completo | No se aplica |
| `greedy_selection_prob` | No se aplica | uniforme `[0,20;0,90]` | No se aplica |
| `train_batch_size_per_learner` | episodios × 1440 | Igual | `{64,128,256,512}` |
| Frecuencia red objetivo | No se aplica | No se aplica | `{500,1000,2000,5000}` pasos |
| Duración de epsilon | No se aplica | No se aplica | `{5000,10000,20000}` pasos |
| Epsilon final | No se aplica | No se aplica | uniforme `[0,02;0,10]` |
| `n_step` | No se aplica | No se aplica | `{1,3,5}` |
| Inicio del aprendizaje | No se aplica | No se aplica | `{1000,2000,5000}` pasos muestreados |
| Factores fijos comunes | gamma=0,99; rho=0; señal `acc_waiting_time`; M=5396; niveles 4–64 | Iguales | Iguales |

Los límites superiores de `randint` son exclusivos. Fuente exacta: `shared/search_space.py:19`; consumidores `_apply_ppo_training` en `phase1_hpo/run.py:63` e `_apply_idqn_training` en `:82`. `use_kl_loss=True` se activa deliberadamente para PPO. El buffer IDQN es `MultiAgentPrioritizedEpisodeReplayBuffer`, preservando el resto de su configuración. HAPPO utiliza `greedy_selection_prob` para el orden de actualización; su implementación actual no subdivide por `minibatch_size` (`happo/torch/happo_torch_learner.py:218`). Se registra esta limitación: no se atribuye un efecto independiente al tamaño de minilote HAPPO.

Se corrige la resolución de funciones dependientes de Tune con `_sampled_value`: espera a que esté resuelto el parámetro fuente antes de usarlo. Las pruebas materializan el espacio efectivo de los cuatro algoritmos y las dos arquitecturas; comprueban rho=0 tanto en entrenamiento como en diagnóstico, niveles compartidos, memoria, semillas, lote PPO y programación epsilon de IDQN.

La búsqueda minimiza `tripinfo/stable_mean_waiting_time_inserted`: espera física agregada de entrenamiento más la media del 20% superior de aumentos positivos recientes, excluyendo las primeras cinco mediciones válidas y reteniendo hasta diez. El coeficiente de penalización es uno; si hay menos de dos mediciones posteriores al descarte, el incremento es cero. Los ceros se conservan. El episodio diagnóstico actúa sin exploración y se registra por separado; no decide las propuestas ni sustituye a la selección. Fuente: `callbacks.py:468` y `:1208`, etiqueta del manuscrito `eq:objetivo_estable_espera`.

**P.** Antes del envío deben fijarse por fase: `training_iterations`, `grace_period`, `reduction_factor`, `eval_interval`, `max_failures`, `max_concurrent` y `resume_limit`. Phase 2 también requiere propuestas por arquitectura y dominios con hash. El protocolo conserva `null` para esas decisiones: no importa 40/10/4 ni 60/30/2 desde campañas sintéticas. El seguimiento debe coincidir con la última iteración. Tiempo SLURM, trabajadores, CPU/GPU y timeout de muestreo se deben ajustar al entorno donde se ejecutará; no son evidencia de un presupuesto urbano ya validado.

`urban.persistence.register_execution` conserva identidad, presupuesto y semillas entre restauraciones, y aplica el límite explícito de reanudación. Se prohíben `force_new`, extensiones implícitas, timestamp y smoke dentro de la identidad de campaña. Los submitters hacen la validación antes de `sbatch`; el job repite la validación antes del lifecycle. Se conservan locks, traps, `TRAIN_PID` y sincronización por estudio. Las fallas no se completan con propuestas adicionales que excedan 50.

**P. Persistencia del objetivo temporal.** El historial del callback es memoria local y no se demuestra su restauración desde un checkpoint. Por eso el preflight urbano solo acepta `resume_limit=0` y `max_failures=0` hasta implementar y verificar la recuperación de ese historial junto con la iteración restaurada. El valor permanece pendiente en el protocolo; no se autoriza una reanudación que reinicie silenciosamente el historial. Las pruebas del registro de ejecución verifican identidad y conteo, pero no sustituyen esa comprobación del objetivo. Los hashes de implementación de `urban/protocol.json` también impiden ejecutar fuentes modificadas sin una nueva revisión del protocolo.

**D. Reglas urbanas de refinamiento.** Se implementan en `urban/refinement.py:15`, `:36`, `:64`, con entrada exclusiva de ocho estudios auditados de Phase 1 urbana. Cada celda requiere al menos diez ensayos completos con puntuación finita y parámetros dentro del espacio original. Se ordenan por objetivo e identificador, se toman los diez mejores y se conserva su intervalo en escala lineal o logarítmica, según la distribución. Si toca el 5% extremo o cubre al menos el 50% del ancho original, se conserva el dominio amplio. En otro caso se usa un ancho mínimo del 10% del dominio, con ampliación del 25% por cada lado y recorte a las fronteras. Los enteros se redondean hacia fuera y mantienen extremo superior exclusivo. Se retienen todas las categorías originales; se evita eliminar alternativas por una muestra pequeña. Son heurísticas nuevas, no criterios derivados de resultados urbanos ni la regla sintética del apéndice.

El artefacto futuro `urban_domains.json` conserva regla, IDs de los diez ensayos, tamaño de población, fuentes y hashes por algoritmo/arquitectura. Su generación requiere `urban_trial_audit.json`, `run_manifest.json`, `urban_execution.json`, configuraciones legibles y checkpoints restaurables de las ocho celdas. El loader comprueba hashes, escenario, fase, claves, constantes y fronteras. No carga dominios sintéticos ni puntajes históricos como observaciones de Phase 2.

Comando del procedimiento posterior, con ocho directorios de estudio explícitos y un protocolo de Phase 1 completo y congelado:

```text
LIBSUMO_AS_TRACI=1 .venv/bin/python -m experiments.marl_experiments.tuning.urban.refinement \
  --protocol <protocolo-fase1-congelado.json> --output <urban_domains.json> \
  <mappo-h128> <mappo-h256> <happo-h128> <happo-h256> \
  <ippo-h128> <ippo-h256> <idqn-h128> <idqn-h256>
```

Los argumentos entre ángulos son productos futuros, no archivos producidos por esta preparación. El hash del artefacto obtenido se registra en el protocolo de Phase 2 antes de validar su envío.

**P.** Hoy no existen dominios concretos derivados por esta preparación, resultados urbanos ni cuatro recetas seleccionadas. El procedimiento y los artefactos de entrada están definidos; los productos necesitan las búsquedas posteriores. Si una celda no alcanza diez ensayos completos, el refinamiento se detiene y requiere una decisión registrada; no rellena la población con ensayos podados.

**Propuesta LaTeX — ubicación:** `subsec:hpo_phase1`, `subsec:hpo_phase2` y apéndice `subsec:espacio_busqueda_fase1` / `subsec:dominios_refinados`; coordinar `tab:dominios_fase1_ppo`, `tab:dominios_fase1_idqn`, `tab:factores_fase1`, `fig:protocolo_informado_v2`. La frase actual que extiende la búsqueda de rho a los cuatro escenarios requiere esta excepción urbana.

```latex
La fase 1 urbana mantiene los dominios iniciales de cada algoritmo y fija
la recompensa local, con $\rho_{\mathrm{coop}}=0$. Comprende ocho estudios:
cuatro algoritmos y dos arquitecturas, con 50 propuestas por estudio y
400 en total. Cada arquitectura permanece fija dentro de su estudio.
La fase 2 obtiene sus dominios exclusivamente de los ensayos completos
de Mendoza, mediante las reglas de refinamiento del apéndice. Las dos
fases comienzan cada política desde cero y conservan sus semillas y
presupuestos en el protocolo urbano.
```

Esta propuesta describe las decisiones ya fijadas. Los valores numéricos pendientes se incorporan al texto académico solo después de completarlos en el protocolo; no se insertan TODO ni estados de avance dentro de LaTeX.

## 5. Candidatos urbanos y panel de selección

**D.** Se adopta una lista de hasta tres candidatos por algoritmo. Se toman los mejores diagnósticos completos de cada arquitectura disponible y se completa la lista por espera diagnóstica e identificador. No se exige que existan candidatos de ambas arquitecturas. Tampoco se importa el filtro sintético CI≥0,95 o el 95% de inserciones.

La admisibilidad técnica exige igualdad exacta con las iteraciones declaradas por la búsqueda de origen, ausencia de error, objetivo y espera diagnóstica finitos, configuración íntegra y checkpoint de última iteración restaurable. Se revisa el entorno efectivo de entrenamiento y diagnóstico. `urban_trial_audit.json` conserva también ensayos fallidos o podados, separados de los elegibles; no basta un compacto ni la existencia de un directorio. `load_audited_study` contrasta fase, presupuesto, procedencia, recursos, calibración, parámetros y checkpoint. `verify_final_checkpoint` restaura con la API pública de RLlib, compara `Algorithm.iteration` y detiene la instancia restaurada.

**P.** El panel común inicial tiene cinco semillas registradas. El coste máximo es `5*(1+4*3)=65` simulaciones de 2 h: cinco de referencia y hasta sesenta de candidatos. Si se conservan menos candidatos, disminuye. Esta cuenta justifica un punto operativo acotado; no garantiza potencia ni estabilidad del ranking. Antes de seleccionar se deben medir coste y variabilidad del baseline en ese panel, ratificar cinco o registrar otro protocolo antes de observar los candidatos. `selection.panel_size_accepted=false` deja esa dependencia visible. No se ha ejecutado el panel ni estimado su variabilidad.

En cada semilla se exige: inserciones del candidato ≥ referencia, CI ≥ referencia y comienzos de teletransporte ≤ referencia. Las inserciones pertenecen a la cohorte de `depart` efectivo en `[1800,9000)`. El ranking usa la media aritmética de las cinco esperas medias por simulación, con igual peso. Desempates exactos: mayor media de CI, menor media de comienzos de teletransporte, identificador ascendente. Si no hay admisibles, no se selecciona una receta para esa combinación. Si faltan registros, hay un denominador nulo o una simulación no llega a 9000 s, la decisión queda incompleta.

Se implementa la función de decisión `urban/selection.py:111`, sin ejecutar simulaciones ni crear un evaluador final. Las condiciones de entrada incluyen cinco semillas distintas, recursos comunes, fin completo y métricas finitas. El procedimiento posterior debe congelar el listado de candidatos y registrar opciones SUMO efectivas, calibración, calentamiento y cohorte de referencia antes del ranking. Los resultados anteriores de la referencia a 104729 no sustituyen a este panel.

**Propuesta LaTeX — ubicación:** conservar `subsec:seleccion_mendoza` y sus tres filtros y desempates; añadir la procedencia de la lista en `subsec:criterios_admisibilidad_hpo`. Correspondencia con las tablas de candidatos que se produzcan después.

```latex
La lista urbana reúne hasta tres candidatos por algoritmo que completan
el presupuesto declarado y conservan una configuración y un modelo
restaurables. Se incluye el primer candidato de cada arquitectura disponible
y se completa la lista por espera diagnóstica e identificador. El panel
compara cada candidato con los programas de referencia bajo la misma
semilla, calentamiento y ventana. Los criterios de admisibilidad y los
desempates se aplican según la subsección \ref{subsec:seleccion_mendoza}.
```

## 6. Aleatoriedad efectiva y restauraciones

**D/C.** `urban/seeds.json` registra funciones separadas: aprendizaje, SUMO de entrenamiento, SUMO diagnóstico y Optuna para cada fase/algoritmo/arquitectura; cinco semillas comunes de selección; nuevas semillas de entrenamiento final; veinte semillas finales distintas por algoritmo. El manifiesto se reproduce con `urban/seeds.py`, `random.Random(20261013)`, extracción sin reemplazo en `[1000001,2**31)`. El valor raíz es una decisión de diseño previa a los resultados, no una semilla histórica reconstruida.

La lista de exclusión conserva 42, 5001/5002 de calibración, 104773 de generación, 104729 canónica y las semillas históricas conocidas enumeradas. Se comprueba que los roles nuevos no se solapen. Las semillas finales no forman un panel común entre algoritmos. La ausencia de colisiones se verifica en estos registros; no acredita un inventario exhaustivo de toda corrida externa al repositorio.

`args.seed` controla el aprendizaje y las RNG del driver. `args.sumo_train_seed` se pasa a `env_config.sumo_seed`; el diagnóstico utiliza `args.eval_seed`. No se utiliza `reset(seed=...)` como sustituto de la semilla SUMO: ese argumento solo afecta NumPy en el entorno actual. Cada entorno se construye con su semilla, y los reinicios vuelven a usarla en `traci.start` / `traci.load`.

Se activa `--save-state.rng true` al guardar el calentamiento. SUMO no guarda por defecto toda la aleatoriedad en el estado, por lo que esa opción es parte del contrato reproducible. [Documentación oficial de guardar y cargar estados](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html).

`seed_runtime_verification.json` verifica con `simulation.getOption("seed")`, antes y después de restaurar, las semillas urbanas MAPPO/h128: entrenamiento 982693574 y diagnóstico 416253520. El simulador confirma memoria 1000 s y conservación RNG; el reset vuelve a 1800 s. `runtime_smoke.json` comprueba una secuencia idéntica de inserciones y observaciones tras dos resets, tanto para referencia como para control aprendido. Las pruebas de configuración cubren las ocho celdas y separan los cuatro roles.

**P.** Antes de una campaña real deben comprobarse también las opciones y versiones recibidas por los workers del clúster y conservar sus logs; aquí se verifica libsumo local y la configuración que recibe RLlib, sin lanzar trabajos Ray distribuidos ni estudios de aprendizaje.

**Propuesta LaTeX — ubicación:** `subsec:ciclo_episodico` y `sec:apendice_reproduccion`; mantener `tab:semillas_fase1` y `tab:busquedas_v2` como tablas sintéticas y añadir una tabla urbana propia desde el JSON.

```latex
El protocolo urbano distingue la semilla del aprendizaje, la del simulador
de entrenamiento, la del seguimiento diagnóstico y la del optimizador.
Las semillas se registran por estudio antes de la búsqueda. La selección
utiliza semillas comunes a candidatos y referencia; la evaluación final
dispone de veinte semillas propias por algoritmo y excluye la semilla
canónica 104729. La restauración del calentamiento conserva el estado
aleatorio del simulador, además de los vehículos y semáforos.
```

## 7. Recetas y contrato del entrenamiento final

**D.** Cada combinación algoritmo/Mendoza que obtenga un candidato admisible produce una receta: hiperparámetros íntegros, arquitectura, entorno, ruta/configuración y hashes, ventanas, semillas nuevas de aprendizaje y SUMO, ensayo y fase de origen, presupuesto concreto y rol del checkpoint. `urban/selection.py:146`, `final_recipe`, usa el presupuesto completo de la búsqueda que aporta la configuración y exige igualdad con la iteración del candidato.

El entrenamiento final comienza desde cero: no restaura el modelo candidato, su estado de Optuna ni su replay buffer. Conserva rho=0 y la calibración urbana. Se retiene el checkpoint de **última iteración**, identificado como `final_declared_budget`; no se reemplaza por uno intermedio de mejor métrica. La restauración posterior debe devolver exactamente `training_iterations` y conservar los hashes y la receta del entrenamiento. La función `urban/persistence.py:37` comprueba la iteración usando la restauración pública de RLlib.

**P.** Las cuatro recetas concretas y sus presupuestos no se pueden completar antes de las búsquedas y la selección. No se han producido checkpoints finales urbanos; las pruebas del verificador usan un restaurador controlado y comprueban aceptación, rechazo y cierre de instancia, sin acreditar restauración de una política urbana entrenada. Tampoco se implementa en esta preparación un entrenamiento final como si ya hubiese una receta ganadora.

Artefactos requeridos después: `candidate_panel.json`, cinco episodios de referencia, episodios de candidatos, `selection_decision.json`, cuatro recetas donde haya admisibilidad, manifiesto de cada entrenamiento final y checkpoint final. La correspondencia debe conservar `source_trial_id`, fase, arquitectura, semilla nueva, `training_iterations` y `checkpoint_role`. Una combinación sin candidato admisible no se rellena con una configuración sintética o una receta manual.

**Propuesta LaTeX — ubicación:** `sec:evaluacion_modelos_finales` y requisitos de reproducción del apéndice; conservar el contrato actual de reentrenamiento y última iteración.

```latex
La configuración seleccionada se entrena desde cero con nuevas semillas
de aprendizaje y simulación. El presupuesto coincide con el presupuesto
completo de la búsqueda que aporta esa configuración. La receta conserva
la arquitectura, los hiperparámetros, las condiciones del entorno y su
procedencia. El modelo final corresponde a la última iteración declarada;
su restauración comprueba la correspondencia entre la iteración guardada
y el presupuesto de entrenamiento.
```

## 8. Métricas, evaluación final, parámetros y aceptación

**C/D.** Los identificadores individuales son los 73 IDs de controladores SUMO, conservados sin renumerar. Sea `W_i(t)` la espera acumulada atribuida a carriles del controlador, en veh·s, y `n_i(t)` sus vehículos presentes. Se mantienen dos medidas locales distintas:

| Medida | Fórmula por simulación | Ponderación / unidad / consumidor |
|---|---|---|
| Espera local ponderada por presencia | `sum_t W_i(t) / sum_t n_i(t)` | Da más peso a pasos con más vehículos; s/vehículo observado. `MeanWaitingTimeCallback`, claves `mean_waiting_time/<id>` o agrupación equivalente. Si el denominador es cero, el código informa cero. |
| Media temporal de espera local por vehículo | `mean_t(W_i(t)/n_i(t))`, con cero cuando `n_i=0` | Igual peso a cada decisión; s/vehículo presente. Base de `_fairness_tl_means` y `fairness_wait_mean`. |
| Espera local global ponderada | `sum_(i,t) W_i(t) / sum_(i,t) n_i(t)` | Ponderación por presencia de vehículos en carriles controlados; `global_mean_waiting_time`. No equivale a esperar por viaje. |
| Gini espacial | Gini de las 73 medias temporales locales | Adimensional, igual peso por controlador; `fairness_wait_gini`. Si todas son cero, Gini=0; con suma positiva, cero significa igualdad. |
| Espera media de viaje | `sum_v TripInfo.waitingTime / N_insertados` | s/vehículo insertado en la cohorte; incluye viajes inconclusos. `tripinfo/mean_waiting_time_inserted`. |
| Pérdida temporal media | `sum_v TripInfo.timeLoss / N_insertados` | s/vehículo; incluye los inconclusos. `tripinfo/mean_time_loss_inserted`. |
| Inserciones y CI | `N_insertados`; `N_completados_de_cohorte/N_insertados` | vehículos y fracción adimensional. `inserted_count`, `completion_inserted`; numerador y denominador de la misma cohorte. |
| Inicios de teletransporte | Suma de listas TraCI de inicio por segundo | Eventos durante el control; `teleport_starts`, no finalizaciones ni necesariamente vehículos distintos. |
| `departDelay` | Retraso anterior a la inserción | s/vehículo; separado de `waitingTime`. No sustituye las inserciones ni forma parte del objetivo actual. |

Fuentes exactas: `traffic_light.py:501`; `callbacks.py:647`, `:672`, `:1045`; `sumo_env.py`, `_collect_w_net_step`, `_fairness_tl_means`, `fairness_wait_gini`; `tripinfo_metrics.py`, `read_tripinfo_metrics`; manuscrito `eq:espera_media_insertados`, `eq:tasa_completitud`, `eq:gini_espera`.

La segunda medida local se reconstruye actualmente desde los acumuladores del entorno; el compacto conserva la primera por agente y los resúmenes globales de equidad. El registro final debe conservar también la segunda por identificador, con sus sumas y cantidades de pasos. Esa persistencia individual forma parte del contrato del evaluador posterior y no se presenta aquí como una salida final ya implementada.

La cohorte de viaje incluye únicamente `depart` efectivo dentro de `[inicio,fin)`. Se excluyen vehículos anteriores al control; quienes siguen presentes al fin se incluyen en el denominador y aportan su espera y pérdida acumuladas hasta el cierre. El entorno solicita `--tripinfo-output.write-unfinished` y cierra SUMO para completar el XML. Teletransportar un vehículo no significa que complete su viaje. Las tasas operacionales `arrived/loaded` e `inserted/loaded` se informan con su propio horizonte; no se sustituyen por CI de la cohorte.

`W_net` existente integra segundos de espera de vehículos expuestos, incluidos presentes al terminar el calentamiento; se conserva como diagnóstico separado. No se usa para redefinir la cohorte insertada de la evaluación final.

**Contrato documental final.** Se ejecutan posteriormente veinte simulaciones por combinación que tenga receta final, con modelo fijo y `explore=False`: fases permitidas de mayor probabilidad para PPO o mayor Q para IDQN. Mendoza utiliza `[0,43200)` y cero calentamiento sobre `mendoza_evaluation_v14.sumocfg`, con las veinte semillas registradas de su algoritmo. Serían 80 simulaciones urbanas si las cuatro combinaciones tienen receta; 320 en las dieciséis combinaciones del diseño completo. No se desarrolla ni ejecuta un evaluador final en esta preparación.

Cada episodio conserva sus registros por agente y de red, opciones SUMO, semilla efectiva, recursos, versión, checkpoint, tiempo de cierre, cohorte, inserciones, CI, pérdida temporal y teletransportes. Para cada métrica y agente se requieren **veinte valores válidos**: `media=sum(x_q)/20`, `s=sqrt(sum((x_q-media)^2)/19)`. Cada simulación tiene igual peso; no se agrupan sus vehículos para reemplazar esa media. Un denominador de viajes cero se representa como indefinido; no se imputa cero. Un cierre anticipado conserva el diagnóstico de fallo, pero no cuenta como una jornada completa ni se omite silenciosamente. Si falta un valor, no se calcula el resumen de esa métrica. Una repetición de un fallo requiere un registro explícito y conserva el intento original; no se cambia la semilla por observar un resultado desfavorable.

Los diagnósticos del modelo reentrenado se examinan independientemente del candidato de selección. No operan como filtros retroactivos, ni autorizan reescoger modelos usando el panel final. La desviación describe variación entre simulaciones de una política fija, no variación entre entrenamientos. No se añaden intervalos, hipótesis o inferencia A/C a la comparación descriptiva de cuatro algoritmos.

La tabla siguiente vincula decisiones y consumidores. Las líneas remiten a las fuentes auditadas en esta preparación; los manifiestos conservan sus hashes.

| Parámetro | Valor y unidad | Justificación | Fuente exacta |
|---|---|---|---|
| Referencia urbana | C/D: v14, 17 estáticos + 56 accionados | Identidad de red congelada y preservación de programas | `urban/protocol.json`, `frozen_resources`; `preparation_manifest.json`, `reference_programs`; `SCENARIO_CANONICO_V14.md`, §10 |
| Volumen nominal | C: 260000 veh/día | Escala declarada de expansión | `seed_search/s104773/gen.log`, bloque [3/7] |
| Demanda esperada 12 h / control | R: 179835,800 / 31083,255 veh | Integración de tasas sobre ventanas | `urban/prepare.py:17`; `preparation_manifest.json`, `demand` |
| Inicio / calentamiento / control | D/C: 1500 s / 300 s / 7200 s | Ventana adoptada 06:30–08:30 | `mendoza_hpo_v14.sumocfg`; `urban/protocol.json`, `window`; `sumo_env.py:402` |
| Evaluación final | D: 0–43200 s; calentamiento 0 s | Examinar condiciones diarias con política fija | `mendoza_evaluation_v14.sumocfg`; protocolo `final_evaluation` |
| Decisión / amarillo / verde mínimo | C: 5 s / 4 s / 5 s | Contrato de movimientos y máscara | `urban/protocol.py`, `environment_contract`; `traffic_light.py:407` |
| Agentes y espacios | C: 73; acciones 1–4; obs 4–11 coordenadas | Controladores de la red, con heterogeneidad conservada | `runtime_smoke.json`; `core/env_factory.py:213` |
| Memoria de espera | D/C: 1000 s | Alinear señal y calibración con el entorno | `sumo_env.py:282`; `encoder_calibration.json`, `waiting_time_memory` |
| Teletransporte | D: 300 s bloqueado; límite de eventos -1 | Conservar el mecanismo y medir ventana completa | Configuraciones urbanas, `processing` |
| Terminación temporal | D/C: truncamiento verdadero; terminación falsa | Distinguir límite artificial de final terminal | `sumo_env.py:579`; `test_real_sumo_warmup_reference_rng_and_truncation` |
| Estado de calentamiento | D/C: RNG guardado | Repetición efectiva tras `loadState` | `sumo_env.py:282`, `:684`; `runtime_smoke.json` |
| Rho / observación vecinal | D/C: 0 / desactivada | Recompensa y actor locales para las dos búsquedas urbanas | `phase1_hpo/run.py:160`; `urban/protocol.json`, `environment` |
| Escala local | C: P99, M=5396 veh·s; dos semillas; 14400 muestras | Envolvente conservadora con memoria alineada | `calibration.log`; `encoder_calibration.json`; `calibrate_encoder_m.py`, `run_simulation` |
| Niveles del codificador | C/D: enteros 4–64, sin unidad | Mantener espacio inicial; probe cubre todo el dominio | `shared/search_space.py:19`; `phase1_hpo/run.py`, `probe_env_spaces` |
| Arquitecturas | D: h128/h256, dos capas 128/256 unidades | Comparación de capacidades con aislamiento de estudios | `shared/architectures.py`, `ARCHITECTURES` |
| Phase 1 | D: 50 propuestas/arquitectura/algoritmo; total 400 | Presupuesto urbano acordado | `urban/protocol.json`, `phase1`; `apply_protocol` |
| Iteraciones / ASHA / frecuencia / concurrencia | P: `null` por fase | Necesitan decisión urbana propia antes de enviar | `urban/protocol.json`, `phase1` y `phase2`; `pending_fields` |
| Fallas / reanudaciones | P: `max_failures` y `resume_limit` | Evitar extensiones y cambios de identidad inadvertidos | `urban/persistence.py:9`; protocolo por fase |
| Objetivo | D/C: espera + penalización, s/vehículo; minimizar | Mantener criterio físico y diagnóstico separado | `callbacks.py:468`, `:1208`; protocolo `objective` |
| Dominios Phase 2 | P: artefacto posterior, regla implementada | Solo resultados completos de Mendoza | `urban/refinement.py:36`; `phase2.domains=null` |
| Candidatos | D: hasta 3/algoritmo; arquitecturas si disponibles | Panel acotado, sin descartar una arquitectura completa | `urban/selection.py:99`; protocolo `selection` |
| Panel de selección | P/D: 5 semillas; hasta 65 simulaciones 2 h | Punto inicial operativo; ratificación pendiente por coste/variabilidad | `urban/seeds.json`, `selection`; `panel_size_accepted=false` |
| Filtros y desempates | D: por semilla y referencia; medias con igual peso | Coherencia con selección urbana del manuscrito | `urban/selection.py:111`; `5-metodologia.tex`, `subsec:seleccion_mendoza` |
| Semillas por función | D/C: registro separado y sin solapamiento nuevo | Separar aprendizaje, demanda, propuesta y paneles | `urban/seeds.py`; `seeds.json`; `seed_runtime_verification.json` |
| Entrenamiento final | D/P: desde cero; presupuesto completo de origen | Evitar elegir retrospectivamente una iteración | `urban/selection.py:146`; protocolo `final_training` |
| Checkpoint final | D/P: `final_declared_budget`; iteración exacta | Vincular receta, presupuesto y estado restaurado | `urban/persistence.py:37`; checkpoint real pendiente |
| Evaluaciones finales | D: 20/combinación; 80 urbanas si hay 4 recetas | Descripción de variación entre simulaciones | protocolo `final_evaluation`; `sec:evaluacion_modelos_finales` |
| Desviación muestral | D: divisor 19 | Veinte observaciones por métrica, igual peso por simulación | `5-metodologia.tex`, `sec:evaluacion_modelos_finales`; contrato de esta sección |

**Propuestas LaTeX — ubicación y correspondencias.** Actualizar conjuntamente cuerpo y apéndice en una etapa posterior: ventanas en `tab:horizontes_simulacion`; rho urbano en `tab:factores_fase1`; nueva tabla urbana de presupuesto/semillas sin alterar las sintéticas; dominios futuros junto a `subsec:dominios_refinados`; procedencia en `tab:archivos_procedencia_mendoza`; flujo `fig:protocolo_informado_v2`; métricas con las etiquetas existentes. Conservar `eq:intervalo_exponencial`, `eq:objetivo_estable_espera`, `eq:espera_media_insertados`, `eq:tasa_completitud` y `eq:gini_espera`; no crear ecuaciones duplicadas. Las referencias bibliográficas existentes `akiba2019optuna`, `li2020system`, `Eimer2023HPO` y `Agarwal2021RLiable` fundamentan mecanismos y límites generales, no los nuevos números urbanos.

```latex
\begin{table}[htbp]
\centering\small
\caption{Condiciones urbanas del escenario v14.}
\label{tab:condiciones_urbanas_v14}
\begin{tabular}{lll}\hline
Parámetro & Búsqueda, selección y entrenamiento & Evaluación final\\\hline
Inicio de simulación & 1500 s & 0 s\\
Calentamiento & 300 s & 0 s\\
Ventana de control & $[1800,9000)$ & $[0,43200)$\\
Recompensa & Local, $\rho_{\mathrm{coop}}=0$ & Política fija\\
Rutas & \multicolumn{2}{l}{Flujos congelados de v14}\\\hline
\end{tabular}
\end{table}

\begin{table}[htbp]
\centering\small
\caption{Presupuesto de propuestas de la fase 1 urbana.}
\label{tab:propuestas_urbanas_fase1}
\begin{tabular}{lrrr}\hline
Algoritmo & h128 & h256 & Total\\\hline
MAPPO & 50 & 50 & 100\\
HAPPO & 50 & 50 & 100\\
IPPO & 50 & 50 & 100\\
IDQN & 50 & 50 & 100\\\hline
Total & 200 & 200 & 400\\\hline
\end{tabular}
\end{table}

Cada combinación con una configuración seleccionada dispone de veinte
simulaciones finales con el modelo fijo y sin exploración. Cada simulación
tiene igual peso en la media; la desviación estándar muestral utiliza el
divisor 19. Un resumen exige veinte valores válidos de la métrica. Las
medidas indefinidas y los cierres anticipados se conservan en el registro,
sin imputarlos como cero. La dispersión describe la variación entre
simulaciones del modelo obtenido, sin estimar variación entre entrenamientos
independientes \cite{Agarwal2021RLiable}.
```

**Verificación y aceptación de esta preparación.** Los comandos se ejecutan desde la raíz con la venv. Los logs preservan los resultados; las comprobaciones no envían trabajos.

```bash
LIBSUMO_AS_TRACI=1 .venv/bin/python -m experiments.marl_experiments.tuning.urban.prepare \
  --output docs/mendoza_preparation/preparation_manifest.json
LIBSUMO_AS_TRACI=1 SUMO_HOME=/home/juanm4/sumo .venv/bin/python -m pytest \
  tests/test_mendoza_urban_protocol.py tests/test_mendoza_urban_submitters.py -q
LIBSUMO_AS_TRACI=1 .venv/bin/python -m experiments.marl_experiments.tuning.urban.protocol \
  --protocol experiments/marl_experiments/tuning/urban/protocol.json --phase phase1
bash -n scripts/slurm/submit_phase1.sh scripts/slurm/run_phase1_job.sh \
  scripts/slurm/submit_phase2_refined.sh scripts/slurm/run_phase2_refined_job.sh
.venv/bin/python -m py_compile experiments/marl_experiments/tuning/shared/search_space.py \
  experiments/marl_experiments/tuning/phase1_hpo/run.py \
  experiments/marl_experiments/tuning/phase2_refined/run.py
git diff --check
```

El preflight de campaña debe fallar mientras permanezcan las siete decisiones de Phase 1 sin completar; es el comportamiento esperado. Los tests de submitters usan un `sbatch` controlado y comprueban que no se invoque. Phase 2 añade sus dominios, hash y presupuesto de propuestas a los pendientes. Las pruebas enfocadas también verifican candidatos, medias, desempates, ausencia de admisibles, restore inmutable y checkpoint final. Las pruebas de configuración sustituyen el arranque Ray y no equivalen a entrenar políticas urbanas. El smoke SUMO es real y corto; la calibración cubre dos ventanas completas de 2 h, sin ejecutar una validación nueva de 12 h.

Resultados conservados: `verification_tests.log` (138 pruebas de contratos urbanos y regresión), `final_urban_tests.log` (26 pruebas urbanas y de submitters). Compilación Python, sintaxis shell y `git diff --check` pasan. `verification.json` y `evidence_sha256.json` reúnen comandos, resultados y hashes finales. El manuscrito visible no cambia, por lo que no se recompila LaTeX ni se afirma haber validado las propuestas en su PDF; esa comprobación corresponde a su incorporación posterior.

El checklist mantiene abiertos los requisitos que dependen de decisiones o productos posteriores: presupuestos completos, dominios urbanos concretos, candidatos reales, ratificación y ejecución del panel, verificación de workers del clúster, cuatro recetas y checkpoints reales e incorporación coordinada al manuscrito. Se cierra el contrato documental de veinte evaluaciones; no la ejecución de esas evaluaciones.
