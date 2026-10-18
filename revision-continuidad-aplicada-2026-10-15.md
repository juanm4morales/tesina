# Revisión conservadora de continuidad — 15 de octubre de 2026

La revisión parte de `origin/main` en `ecf6182e2fb48f303d8023383327a05c92eceba0`. La versión local `8d1642a` permanece intacta. Las fuentes y los PDF de ambas versiones, junto con los documentos locales no versionados, se guardaron en `respaldo-continuidad-20261015/`. La copia de integración está en `/tmp/tesina-continuidad-20261015`.

## Cambios de lectura

La metodología concentra la revisión. Se separaron los párrafos al cambiar su función: indicadores de cierre y uso en el aprendizaje; propuestas de búsqueda y ASHA; fases 1 y 2; escenario urbano y condiciones compartidas; admisibilidad y evidencia necesaria; hiperparámetros de A/C y dimensión de entrada de C; entrenamiento de dos horas y evaluación de doce; intervalos principales y sensibilidad con Student. En el apéndice se separó el presupuesto urbano del tamaño del lote. Los cortes no incorporan frases de transición.

«Cada red se refina» se reemplazó por una referencia a los dominios de búsqueda. La apertura de A/C recupera su pregunta específica y señala que se comparte una configuración fija de hiperparámetros. La remisión a observaciones y recompensas cierra ese párrafo; permanece la limitación del contraste conjunto. «Configuración transferida» se sustituyó por «configuración común de hiperparámetros». Resultados atribuye al informe histórico la separación de 3×3 y declara que la tesina analiza las tres redes por separado.

En el marco teórico se acotó la mezcla de señales locales y vecinales a las variantes correspondientes, se mantuvo «recompensa individual» en las descripciones generales y se precisó que HAPPO conserva la actualización sucesiva de actores. Se unificaron los usos previstos de «bootstrapping» y «búsqueda refinada».

Se conservaron las supresiones del remoto: el recorrido experimental permanece en la apertura y el diagrama; la descripción del crítico conserva su funcionamiento y la consecuencia sobre el gradiente; las referencias conjuntas al apéndice conservan sus destinos. No se recuperaron las frases generales sobre capacidad y cierre temporal: permanecen sus consecuencias concretas.

## Cuestión científica pendiente, fuera del pase

Los presupuestos y las reglas de refinamiento urbanos se conservaron tal como figuran en `ecf6182`. Esto no valida su correspondencia con el código experimental. La discrepancia está documentada en `revision-comparativa-remoto-2026-10-15.md`, apartado 3, y no se volvió a auditar el código en este pase editorial.

Ese informe compara el manuscrito con una copia experimental en `6081522`, con cambios locales: fase 1 urbana de 100 propuestas iniciales frente a 50 en el protocolo consultado; presupuestos de fase 2 fijados en el manuscrito frente a campos `null`; y reglas distintas de dispersión, ampliación de intervalos y conservación de categorías. Queda pendiente identificar qué versión del protocolo y del código respalda la especificación que se adoptará. La comparación previa no descarta una implementación posterior en otra copia o en el clúster.

## Verificación y publicación

Se ejecutaron `pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`, `makeglossaries main` y `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex`. La compilación final conserva únicamente la advertencia conocida de `tracklang`; no presenta desbordes, citas o referencias indefinidas ni etiquetas duplicadas. `qpdf --check` y `git diff --check` finalizaron correctamente.

La comparación de fuentes verificó que se conservaron las ecuaciones, las expresiones matemáticas, las citas, las referencias, los usos de glosario y los identificadores técnicos. Las secciones de fase 1 y fase 2 no cambiaron; el apéndice solo recibió una separación de párrafo. No se editaron la bibliografía, el glosario, las imágenes ni los borradores excluidos del build.

Se inspeccionaron las páginas afectadas del PDF, con prioridad en metodología. En la versión final se revisaron visualmente las páginas físicas 61, 67, 71, 76, 79, 97, 102–104, 108–112, 114–117, 120 y 147–148. La inspección fue focalizada, no una revisión visual de las 161 páginas. Se permitió que la figura de controladores se colocara al inicio de la página siguiente (`[!ht]`) para evitar un gran hueco; se reservó espacio antes del párrafo de evidencia urbana para evitar una línea aislada. La figura y su epígrafe conservan su contenido.

Se publicaron mediante push normal únicamente a `main`:

- `78342b5`: fuentes revisadas.
- `fc1669f`: PDF actualizado.

El remoto no había avanzado desde `ecf6182`. La copia de integración quedó limpia. La rama local original sigue en `8d1642a`; sus fuentes y `main.pdf` no se reemplazaron. El PDF publicado se entrega como `respaldo-continuidad-20261015/main-revisado-publicado.pdf`; las fuentes publicadas también se conservaron en `publicado-fc1669f.tar.gz`. Los logs, el comprobador y las imágenes de inspección se guardaron en la misma carpeta de respaldo.
