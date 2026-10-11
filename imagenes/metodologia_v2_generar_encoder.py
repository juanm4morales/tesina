#!/usr/bin/env python3
"""Regenerate both encoder PDFs with the standard library and installed LaTeX stack.

Optional --verify-code PATH compares the formula against an external encoder.py
(for example the release snapshot). No absolute path is required to generate plots.
"""
from __future__ import annotations

import argparse
import importlib.util
import math
import subprocess
import tempfile
from collections.abc import Sequence
from pathlib import Path

I, M = 22, 1136.0  # illustrative 3x3 scenario; not a universal setting
OUT = Path(__file__).resolve().parent


def encoded(x: float) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")
    if x >= M:
        return I - 1
    L = (I - 1) / M  # numerical x and M use the same vehicle·s unit
    # Preserve the operation order in Encoder.log_interval for boundary fidelity.
    F = (1 - L) * ((I - 1) / math.log2(M / (M * L) + 1))
    return min(I - 1, max(0, math.ceil(F * math.log2(x / (M * L) + 1) + L**2 * x)))


def blend(xhat: float) -> tuple[float, float, float]:
    L = (I - 1) / M
    log_part = (1 - L) * math.log2(1 + xhat / L) / math.log2(1 + 1 / L)
    linear_part = L * xhat
    return log_part, linear_part, log_part + linear_part


def validate(reference_path: Path | None) -> tuple[int, int]:
    if reference_path is None:
        return 0, 0
    spec = importlib.util.spec_from_file_location("snapshot_encoder", reference_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import encoder at {reference_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    ref = module.Encoder(I, M)
    probes = {j * (1.2 * M) / 1200 for j in range(1201)}
    probes.update((0.0, M - 1e-7, M, 1.2 * M))
    if ref.log_interval(0) != encoded(0):
        raise AssertionError("Mismatch at x=0")
    try:
        encoded(-1e-9)
        raise AssertionError("negative x was not rejected")
    except ValueError:
        pass
    try:
        ref.log_interval(-1e-9)
        raise AssertionError("reference did not reject negative x")
    except ValueError:
        pass
    # Find one representative threshold for every attained encoded level; test
    # immediately below, at, and above each ceil transition.
    last = encoded(0.0)
    for j in range(1, 20001):
        x = M * j / 20000
        y = encoded(x)
        if y > last:
            lo, hi = M * (j - 1) / 20000, x
            for _ in range(60):
                mid = (lo + hi) / 2
                if encoded(mid) >= y:
                    hi = mid
                else:
                    lo = mid
            probes.update((math.nextafter(hi, -math.inf), hi, math.nextafter(hi, math.inf)))
            last = y
    for x in sorted(probes):
        got, expected = encoded(x), ref.log_interval(x)
        if got != expected:
            raise AssertionError(f"encoder mismatch x={x:.17g}: formula={got}, snapshot={expected}")
    return len(probes), last


def coordinates(points: Sequence[tuple[float, float | int]]) -> str:
    return "\n".join(f"({x:.9f},{y:.9f})" for x, y in points)


def standalone(figure: str) -> str:
    return r"""\documentclass[tikz,border=3pt]{standalone}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}\usepackage[spanish,es-noquoting]{babel}
\usepackage{pgfplots}\pgfplotsset{compat=1.18}
\definecolor{blueplot}{HTML}{4D8FBD}\definecolor{mintplot}{HTML}{3A9274}
\definecolor{salmonplot}{HTML}{CF706E}\definecolor{inkplot}{HTML}{263746}
\begin{document}
""" + figure + r"""\end{document}
"""


def pgf(output: Path) -> None:
    # 1201 samples resolve each staircase transition and the saturation edge.
    stair = [(1.2 * M * j / 1200, encoded(1.2 * M * j / 1200)) for j in range(1201)]
    stair += [(M, I - 1), (1.2 * M, I - 1)]
    stair.sort()
    fig1 = rf"""\begin{{tikzpicture}}
\begin{{axis}}[width=14.3cm,height=8cm,axis lines=left,xmin=0,xmax={1.2*M},ymin=-.5,ymax=21.8,
 xlabel={{Espera $x$ (vehículo$\cdot$s)}},ylabel={{Nivel $e(x)$}},
 ytick={{0,5,10,15,21}},yticklabels={{0,5,10,15,$I-1$}},
 grid=major,grid style={{inkplot!12}},
 tick label style={{font=\small}},label style={{font=\small}},title style={{font=\small}}]
\addplot[blueplot,thick,const plot] coordinates {{
{coordinates(stair)}
}};
\addplot[salmonplot,dashed,thick] coordinates {{({M},0) ({M},21)}};
\node[anchor=east,align=right,text=salmonplot,font=\small,fill=white,inner sep=2pt]
 at (axis cs:1070,15) {{$M_{{\mathrm{{lane}}}}$}};
\draw[->,salmonplot,thin] (axis cs:1085,15)--(axis cs:{M},15);
\end{{axis}}\end{{tikzpicture}}"""
    L = (I - 1) / M
    points = [blend(j / 1000) for j in range(1001)]
    fig2 = rf"""\begin{{tikzpicture}}
\begin{{axis}}[width=14.3cm,height=8cm,axis lines=left,xmin=0,xmax=1,ymin=0,ymax=1.05,
 xlabel={{Espera normalizada, $\hat{{x}}=x/M_{{\mathrm{{lane}}}}$}},ylabel={{Contribución normalizada}},
 title={{Mezcla logarítmico-lineal antes de discretizar}},grid=major,grid style={{inkplot!12}},
 legend style={{draw=none,fill=none,font=\small,at={{(.98,.50)}},anchor=east}},
 tick label style={{font=\small}},label style={{font=\small}},title style={{font=\small}}]
\node[anchor=north west,align=left,text width=8cm,font=\scriptsize,fill=white,fill opacity=.9,text opacity=1]
 at (rel axis cs:.02,.98) {{Escenario $3\times3$; $I={I}$; $M_{{\mathrm{{lane}}}}={M:.0f}$ vehículo·s.\\$L=(I-1)/M_{{\mathrm{{num}}}}={L:.4f}$, con $M_{{\mathrm{{num}}}}=M_{{\mathrm{{lane}}}}/u$ y $u=1$ vehículo·s.}};
\addplot[blueplot,thick] coordinates {{{coordinates([(j/1000, p[0]) for j,p in enumerate(points)])}}};
\addlegendentry{{Componente logarítmica ponderada}}
\addplot[mintplot,thick] coordinates {{{coordinates([(j/1000, p[1]) for j,p in enumerate(points)])}}};
\addlegendentry{{Componente lineal ponderada}}
\addplot[salmonplot,very thick] coordinates {{{coordinates([(j/1000, p[2]) for j,p in enumerate(points)])}}};
\addlegendentry{{Mezcla $g(\hat{{x}})$}}
\end{{axis}}\end{{tikzpicture}}"""
    for name, figure in (("encoder", fig1), ("componentes_encoder", fig2)):
        with tempfile.TemporaryDirectory(prefix="metodologia-v2-") as tmp:
            src = Path(tmp) / "plot.tex"
            src.write_text(standalone(figure), encoding="utf-8")
            result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                                     "-output-directory", tmp, str(src)],
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                    encoding="utf-8", errors="replace")
            if result.returncode:
                raise RuntimeError(f"pdflatex failed for {name}:\n{result.stdout}")
            (output / f"metodologia_v2_{name}.pdf").write_bytes((Path(tmp) / "plot.pdf").read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-code", type=Path, help="optional external encoder.py for numerical comparison")
    args = parser.parse_args()
    count, last = validate(args.verify_code)
    # pgfplots uses the installed LaTeX stack and keeps PDF text/vector output
    # consistent with the thesis; no Python plotting package is required.
    pgf(OUT)
    print(f"PDF generated: I={I}, M_lane={M:g} vehicle·s, maximum level={I-1}; comparison probes={count}, attained={last}")


if __name__ == "__main__":
    main()
