# AGENTS.md

## Repository Shape
- This is a Spanish LaTeX thesis repository, not an application project. The real entrypoint is `main.tex`.
- `main.tex` currently includes only `0-titulo`, `1-agradecimientos`, `3-introduccion`, and `4-marco_teorico`; `2-resumen`, `5-metodologia`, `6-resultados`, and `7-conclusiones` are present but commented out.
- `4-marco_teorico_2.tex` is an alternate/draft file and is not compiled by `main.tex`.
- `.agents/skills/` is a vendored local skill library tracked by the repo; do not edit it unless the task is explicitly about skills.
- `codigo_fuente/` is not a configured software package; it currently contains only `ejemplo1.sh`.

## Build And Verification
- Use `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from the repo root to build the thesis PDF.
- The existing `main.fdb_latexmk` shows the actual toolchain is `pdflatex` plus `bibtex main`; do not switch to `biber`/`biblatex` unless the LaTeX sources are changed accordingly.
- Bibliography is configured in `main.tex` with `\bibliographystyle{babalpha}` and `\bibliography{bibliografia}`; citations should resolve through `bibliografia.bib`.
- For bibliography-only troubleshooting, the manual sequence is `pdflatex main.tex`, `bibtex main`, `pdflatex main.tex`, `pdflatex main.tex`.

## LaTeX Conventions
- Keep chapter files as top-level `*.tex` files included from `main.tex`; avoid adding a new build system unless requested.
- Images live in `imagenes/`; reference them relative to the repo root, consistent with existing files.
- `main.tex` defines Spanish document settings, `listings` styles, algorithm packages, and comment macros `\JM`, `\PJV`, and `\ACO`; reuse existing definitions instead of redefining them in chapter files.
- This repo uses `babelbib`/`babalpha`, so BibTeX entries in `bibliografia.bib` should remain compatible with classic BibTeX.
- With `babelbib`, cited BibTeX entries without a `language` field can produce non-fatal `empty language` warnings; add `language` when cleaning or adding references.
- In this repo's `babelbib` setup, `language = {english}` is not a safe cleanup option for cited entries; use the repo-consistent `language = {spanish}` when the goal is to eliminate `empty language` warnings.

## Thesis Writing Notes
- In thesis prose, prefer `este trabajo`, `esta investigación`, or `el presente trabajo`; avoid using `tesis` unless the user asks otherwise.
- For traffic-engineering theory, keep the purpose narrow: justify the computational traffic-control model, not a broad civil-engineering treatment.
- In `4-marco_teorico.tex`, traffic terminology should align with `ite_handbook`, `calymayor`, and `fernandez`; avoid uncited terminology even if it sounds plausible.
- In `4-marco_teorico.tex`, clean up multi-source citations sentence by sentence: `\cite[^\n]*\cite` is useful for spotting candidates, but it also catches separate citations that merely share one wrapped LaTeX line.
- Keep paired citations only when the sources play different roles in the same passage, e.g. `ite_handbook` for operational or simulation motivation and `fernandez` for traffic-model taxonomy or queueing details; otherwise prefer one source attached to the exact claim.
- For intersection conflicts, prefer natural ITE-aligned Spanish such as `movimientos en conflicto`, `corrientes vehiculares incompatibles`, or `puntos de conflicto`; avoid `conflictos direccionales`.
- Translate concepts consistently in Spanish; for example, write `enfoques basados en indicadores de desempeño` instead of pairing Spanish with `performance-based design` unless the English term is being explicitly discussed.
- For traffic dynamics, keep established terms such as `corriente de tránsito`, `condiciones de operación`, `variables principales`, `variables asociadas`, `flujo`, `densidad`, and `velocidad media espacial`.
- In `\subsubsection{Descripción Probabilística del Flujo}`, present Poisson arrivals as an approximation valid for free or moderate flow with weak upstream signal influence; explicitly acknowledge platooning and temporal dependence in coordinated or saturated networks.
- In `4-marco_teorico.tex`, present car-following and lane-changing as internal microscopic-simulator mechanisms; omit Herman/Greenshields/stability derivations unless they are later used in methodology or experiments.
- When connecting simulation to RL, avoid meta-section titles such as `Vínculo...`; prefer substantive headings like `Entorno de Simulación para Control Semafórico` or integrate the transition in prose.
- For SUMO/SUMO-RL framing, map traffic variables to observations, phase choices to actions, and delay/queue/stop metrics to rewards or evaluation, while keeping the wording grounded in cited sources.
- Motivate MARL for signal control through spatial/temporal interdependence between intersections; avoid implying each semaforized node is independent when queues and arrivals propagate.

## Workflow Gotchas
- LaTeX build artifacts (`*.aux`, `main.pdf`, `main.bbl`, logs, etc.) are tracked and there is no `.gitignore`; do not run broad cleanup commands or delete generated files unless explicitly asked.
- Before editing, check `git status --short`; generated files and thesis chapters may already be dirty from prior writing or compilation.
- Prefer small, section-scoped edits in chapter files and preserve the academic Spanish tone already used in the thesis.
- After changing section levels or headings, stale `hyperref`/TOC destination warnings can appear on an intermediate pass; use the full `latexmk` command rather than judging from a single `pdflatex` run.
- `main.synctex.gz` is tracked; a plain `latexmk -pdf ...` can leave it deleted if the last build used SyncTeX. Regenerate it with `latexmk -g -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` before finishing if the file matters to the worktree.
