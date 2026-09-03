# Convención de terminología y notación

Documento de control para la revisión de la tesina. Esta matriz se utilizará
durante la corrección de los capítulos, el glosario, las ecuaciones y los
algoritmos. No constituye texto destinado a incorporarse literalmente al PDF.

## Criterio general

Se traduce al español cuando existe un equivalente académico asentado y se
incluye el término inglés y la sigla en la primera aparición. Se conserva en
inglés el nombre propio con el que fue publicado un algoritmo, un mecanismo de
software o un término para el que no existe un equivalente español único y
estable en la literatura del área. En este último caso se añade una explicación
en español en la primera aparición.

## Nombres propios que se conservan en inglés

| Nombre | Sigla | Forma de presentación |
|---|---|---|
| Deep Q-Network | DQN | Nombre exacto del algoritmo; explicar que aproxima valores de acción con una red neuronal profunda. |
| Proximal Policy Optimization | PPO | Nombre exacto; explicar que restringe la magnitud de las actualizaciones de la política. |
| Trust Region Policy Optimization | TRPO | Nombre exacto; explicar la restricción basada en una región de confianza. |
| Independent Proximal Policy Optimization | IPPO | Nombre exacto. |
| Multi-Agent Proximal Policy Optimization | MAPPO | Nombre exacto. |
| Heterogeneous-Agent Proximal Policy Optimization | HAPPO | Nombre exacto. |
| Heterogeneous-Agent Trust Region Policy Optimization | HATRPO | Nombre exacto. |
| Generalized Advantage Estimation | GAE | Nombre del estimador; explicar su función en español. |
| Win or Learn Fast Policy Hill-Climbing | WoLF-PHC | Nombre exacto. |
| Value-Decomposition Networks | VDN | Nombre exacto. |
| QMIX, MADDPG, DDPG y A2C | — | Conservar las denominaciones y siglas originales. |

No se usarán como nombres canónicos expresiones como «optimización de política
próxima», «optimización de política mediante región de confianza» o
«optimización de política para agentes heterogéneos». Esas expresiones podrán
aparecer únicamente como descripciones explicativas, nunca como sustitutos de
PPO, TRPO, HAPPO o HATRPO.

## Términos sin equivalente español único y estable

Estos términos se conservarán en inglés, preferentemente en cursiva en su
primera aparición, y se explicarán en español:

| Término | Explicación que debe acompañarlo |
|---|---|
| *rollout* | Secuencia de transiciones obtenida durante la interacción del agente con el entorno. |
| *replay buffer* / *experience replay* | Memoria que almacena transiciones para volver a muestrearlas durante el entrenamiento. |
| *bootstrapping* | Estimación de un valor futuro a partir de otra estimación ya disponible. |
| *on-policy* / *off-policy* | Si los datos provienen de la política que se está actualizando o de otra política. |
| *action masking* | Enmascaramiento de acciones que impide seleccionar acciones no válidas. |
| *logit* / *logits* | Valores reales producidos antes de convertirlos en probabilidades mediante *softmax*. |
| *softmax* | Función que transforma valores reales en una distribución de probabilidades. |
| *feedforward* | Propagación de la información desde la entrada hacia la salida sin ciclos internos. |
| *framework* | Infraestructura de software que proporciona componentes y reglas de integración. |
| *bindings* | Enlaces que permiten utilizar desde un lenguaje una biblioteca implementada en otro. |
| *checkpoint* | Estado guardado del modelo o de la simulación para poder restaurarlo. |
| *mock* | Objeto de prueba que simula el comportamiento de una dependencia real. |
| *parameter sharing* | Uso de los mismos parámetros de aprendizaje por varios agentes. |
| *feature pruning* | Eliminación selectiva de variables o características de una representación. |
| *gridlock* | Bloqueo mutuo de la red que impide el avance de los vehículos. |
| *spillback* | Propagación de una cola hacia tramos o intersecciones aguas arriba. |
| *teleport* | Mecanismo específico de SUMO para retirar y reinsertar un vehículo bloqueado. |
| *epoch* | Recorrido completo de optimización sobre los datos recolectados durante una iteración. |
| *minibatch* | Subconjunto de muestras utilizado para calcular una actualización de los parámetros. |

Los identificadores de código, configuración y API (`linkIndex`, `action_mask`,
`grad_clip`, `vf_clip`, `TripInfo`, `env runner`, `learner`,
`neighborhood_relevance`, entre otros) se conservarán literalmente y se
marcarán con `\texttt{}` cuando aparezcan en la prosa.

## Términos que se expresarán en español

La primera aparición incluirá el equivalente inglés y la sigla cuando
corresponda:

- inteligencia artificial (*Artificial Intelligence*, IA);
- aprendizaje automático (*Machine Learning*, ML);
- aprendizaje supervisado y no supervisado;
- aprendizaje por refuerzo (*Reinforcement Learning*, RL);
- aprendizaje profundo (*Deep Learning*, DL);
- aprendizaje por refuerzo multiagente (*Multi-Agent Reinforcement Learning*, MARL);
- proceso de decisión de Markov (*Markov Decision Process*, MDP);
- proceso de decisión de Markov parcialmente observable (POMDP);
- proceso de decisión de Markov parcialmente observable descentralizado (Dec-POMDP);
- entrenamiento centralizado y ejecución descentralizada (*Centralized Training with Decentralized Execution*, CTDE);
- actor-crítico (*actor--critic*);
- diferencia temporal (*temporal difference*, TD);
- descenso por gradiente y retropropagación;
- entrada/salida (*Input/Output*, E/S);
- tasa de aprendizaje, función de activación, función de pérdida y gradiente de política.

En tránsito se mantendrán las formas españolas establecidas por el proyecto:
`corriente de tránsito`, `flujo`, `densidad`, `velocidad media espacial`,
`demora`, `cola`, `movimientos en conflicto`, `corrientes vehiculares
incompatibles` y `puntos de conflicto`.

## Notación que se debe normalizar

| Símbolo | Convención prevista |
|---|---|
| `T` | Horizonte o duración temporal; definir siempre su unidad y el intervalo al que se refiere. |
| `t` | Instante o paso temporal; no alternar sin explicación entre segundos de simulación y pasos de decisión. |
| `I` | Número de intersecciones o agentes; fijar el significado en cada capítulo. |
| `M` | Factor de ventaja reponderada acumulado de HAPPO; no reutilizarlo para otro conjunto o cantidad. |
| `M_{\mathrm{lane}}` | Cota de saturación del carril utilizada por `Encoder`; distinguirla visualmente del factor `M` de HAPPO. |
| `F` | Número de fases válidas, si se utiliza; distinguirlo de `K_i` cuando represente acciones por intersección. |
| `x` | Variable de entrada del codificador; indicar que representa una magnitud de tránsito y su unidad. |
| `\xi_{od}` | Fracción de demanda del par origen-destino; declarar su normalización y suma total. |
| `W_{\mathrm{acc},i}` | Espera acumulada asociada al agente o intersección `i`; definirla antes de usarla. |
| `\epsilon_{\mathrm{exp}}` | Coeficiente de exploración de la política `\epsilon`-greedy. |
| `\epsilon_{\mathrm{clip}}` | Margen de recorte de PPO; no confundirlo con exploración. |
| `\alpha_{\mathrm{lr}}` | Tasa de aprendizaje. |
| `\alpha_{\mathrm{CVaR}}` | Nivel de cola utilizado en CVaR. |
| `\alpha_{\mathrm{sig}}` | Nivel de significación estadística. |
| `\rho_{\mathrm{coop}}` | Peso o coeficiente de cooperación de la recompensa. |
| `\rho_{\mathrm{post}}` | Razón de probabilidades posterior de HAPPO, si corresponde. |
| `\lambda` | Parámetro de GAE o de la mezcla de recompensas; usar subíndices si ambos aparecen en la misma sección. |
| `\eta` | Tasa del optimizador, diferenciada de la tasa de aprendizaje conceptual. |

## Reglas de aplicación

1. Definir cada término técnico antes de emplearlo como si el lector no tuviera formación en informática.
2. No introducir una traducción diferente para el mismo concepto en capítulos distintos.
3. No usar el glosario como sustituto de la explicación local.
4. Revisar títulos, pies de figura, tablas, algoritmos y marcadores PDF para que mantengan la misma convención.
5. Actualizar el glosario y las abreviaturas solamente después de aprobar esta matriz.
