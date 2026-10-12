#!/usr/bin/env python3
"""Render the twelve Phase 2 domain tables from the rho=0 v3 manifest."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
CELLS = {
    "happo": ["happo/3x1", "happo/3x3", "happo/4x4_H"],
    "idqn": ["idqn/3x1", "idqn/3x3", "idqn/4x4_H"],
    "ippo": ["ippo/3x1", "ippo/3x3", "ippo/4x4_H"],
    "mappo": ["mappo/3x1", "mappo/3x3", "mappo/4x4_H"],
}
PARAM_ORDER = {
    "happo": ["clip_param", "encoder_intervals", "entropy_coeff", "grad_clip",
              "greedy_selection_prob", "kl_coeff", "kl_target", "lambda_gae", "lr",
              "minibatch_size", "num_epochs", "train_batch_episodes", "vf_clip_param"],
    "idqn": ["encoder_intervals", "epsilon_final", "epsilon_timesteps", "grad_clip", "lr",
             "n_step", "num_steps_sampled_before_learning_starts", "target_network_update_freq",
             "train_batch_size_per_learner"],
    "ippo": ["clip_param", "encoder_intervals", "entropy_coeff", "grad_clip", "kl_coeff",
             "kl_target", "lambda_gae", "lr", "minibatch_size", "num_epochs",
             "train_batch_episodes", "vf_clip_param"],
    "mappo": ["clip_param", "encoder_intervals", "entropy_coeff", "grad_clip", "kl_coeff",
              "kl_target", "lambda_gae", "lr", "minibatch_size", "num_epochs",
              "train_batch_episodes", "vf_clip_param"],
}
PARAMETER_LABELS = {'neighborhood_relevance': 'Peso de recompensa vecinal', 'lr': 'Tasa de aprendizaje', 'clip_param': 'Recorte del actor', 'lambda_gae': 'Parámetro de GAE', 'entropy_coeff': 'Peso de entropía', 'grad_clip': 'Límite del gradiente', 'kl_coeff': 'Coeficiente de penalización KL', 'kl_target': 'Objetivo de divergencia KL', 'vf_clip_param': 'Cota de pérdida de valor', 'num_epochs': 'Recorridos de optimización', 'train_batch_episodes': 'Episodios por lote', 'encoder_intervals': 'Niveles del codificador', 'minibatch_size': 'Tamaño del minilote', 'greedy_selection_prob': 'Probabilidad de ordenación (HAPPO)', 'train_batch_size_per_learner': 'Transiciones por lote', 'target_network_update_freq': 'Actualización de red objetivo', 'epsilon_timesteps': 'Pasos para reducir exploración', 'epsilon_final': 'Exploración final', 'n_step': 'Horizonte del retorno', 'num_steps_sampled_before_learning_starts': 'Pasos antes de aprender'}
SCENARIO_LABEL = {"3x1": r"$3\times1$", "3x3": r"$3\times3$", "4x4_H": r"$4\times4_{\mathrm{H}}$"}


def latex_number(value: int | float, parameter: str) -> str:
    if isinstance(value, bool):
        raise TypeError("boolean is not a numeric domain value")
    if isinstance(value, int):
        return f"{value:,}".replace(",", r"\,")
    if parameter == "lr":
        exponent = math.floor(math.log10(abs(value))) if value else 0
        mantissa = value / (10 ** exponent) if value else 0
        mantissa_text = f"{mantissa:.4g}".replace(".", "{,}")
        return rf"{mantissa_text}\times10^{{{exponent}}}"
    text = f"{value:.5g}"
    if "e" in text.lower():
        mantissa, exponent = text.lower().split("e")
        return rf"{mantissa.replace('.', '{,}')}\times10^{{{int(exponent)}}}"
    return text.replace(".", "{,}")


def domain_cell(domain: dict[str, Any], parameter: str) -> str:
    kind = domain["type"]
    if kind in ("uniform", "loguniform"):
        low = latex_number(domain["lower"], parameter)
        high = latex_number(domain["upper"], parameter)
        return rf"$[{low};\,{high}]$"
    if kind == "randint":
        low = int(domain["lower"])
        high = int(domain["upper_exclusive"])
        return rf"$[{latex_number(low, parameter)};\,{latex_number(high, parameter)})$"
    if kind == "choice":
        values = [latex_number(v, parameter) for v in domain["values"]]
        return "$" + r"\{" + r";\,".join(values) + r"\}" + "$"
    raise ValueError(f"Unsupported domain type {kind!r} for {parameter}")


def kind_label(domain: dict[str, Any]) -> str:
    return {"uniform": "Uniforme continua", "loguniform": "Loguniforme",
            "randint": "Uniforme entera", "choice": "Categórico"}[domain["type"]]


def parameter_label(name: str, domain: dict[str, Any], algorithm: str) -> str:
    label = PARAMETER_LABELS[name]
    if name == "greedy_selection_prob":
        label = "Probabilidad de ordenación"
    if algorithm == "happo" and name == "minibatch_size":
        label += r"$^{*}$"
    return label


def validate_manifest(manifest: dict[str, Any]) -> None:
    if manifest.get("schema_version") != 3:
        raise ValueError("Expected the Phase 2 informed-domain v3 manifest")
    budget = manifest.get("budget", {})
    if budget.get("num_samples") != 100 or budget.get("training_iterations") != 60:
        raise ValueError("Manifest budget differs from the 100-configuration v3 protocol")
    cells = manifest.get("cells", {})
    expected = {cell for group in CELLS.values() for cell in group}
    if set(cells) != expected:
        raise ValueError(f"Expected exactly the 12 v3 cells; got {sorted(cells)}")
    for algorithm, names in CELLS.items():
        for name in names:
            cell = cells[name]
            if cell.get("architecture") not in ("h128", "h256"):
                raise ValueError(f"Missing architecture for {name}")
            if set(cell.get("search_space", {})) != set(PARAM_ORDER[algorithm]):
                raise ValueError(f"Parameter/domain mismatch for {name}")
            if set(cell.get("seeds", {})) != {"train", "evaluation", "optimizer"}:
                raise ValueError(f"Seed set mismatch for {name}")


def render_table(algorithm: str, manifest: dict[str, Any], heading: bool = False) -> str:
    cells = CELLS[algorithm]
    parameters = PARAM_ORDER[algorithm]
    col_spec = (r"@{}>{\raggedright\arraybackslash}p{5.5cm}"
                r"@{\hspace{6pt}}>{\raggedright\arraybackslash}p{3.3cm}"
                r"@{\hspace{6pt}}lll@{}")
    lines = [r"\begingroup\small\setstretch{1.05}\renewcommand{\arraystretch}{1.18}",
             rf"\begin{{tabular}}{{{col_spec}}}", r"\hline",
             r"\rowcolor{catAzulCielo!25}"]
    if heading:
        title = algorithm.upper()
        lines.extend([rf"\multicolumn{{5}}{{l}}{{\textbf{{{title}}}}}\\", r"\hline",
                      r"\rowcolor{catAzulCielo!25}"])
    labels = ["Parámetro", "Muestreo"]
    for cell_name in cells:
        scenario = cell_name.split("/", 1)[1]
        architecture = manifest["cells"][cell_name]["architecture"]
        labels.append(rf"{SCENARIO_LABEL[scenario]} ({architecture})")
    lines.extend([" & ".join(labels) + " " + chr(92) * 2, r"\hline"])
    for parameter in parameters:
        domains = [manifest["cells"][cell]["search_space"][parameter] for cell in cells]
        row = [parameter_label(parameter, domains[0], algorithm), kind_label(domains[0])]
        row.extend(domain_cell(domain, parameter) for domain in domains)
        lines.append(" & ".join(row) + " " + chr(92) * 2)
    lines.extend([r"\hline", r"\end{tabular}", r"\endgroup"])
    return "\n".join(lines) + "\n"


def render_outputs(manifest: dict[str, Any]) -> dict[Path, str]:
    validate_manifest(manifest)
    outputs = {
        HERE / "metodologia_v2_dominios_happo.tex": render_table("happo", manifest),
        HERE / "metodologia_v2_dominios_idqn.tex": render_table("idqn", manifest),
        HERE / "metodologia_v2_dominios_ippo.tex": render_table("ippo", manifest, heading=True),
        HERE / "metodologia_v2_dominios_mappo.tex": render_table("mappo", manifest, heading=True),
    }
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    for path, content in render_outputs(manifest).items():
        path.write_text(content, encoding="utf-8")
    print("Rendered all 12 domain cells from the v3 manifest.")


if __name__ == "__main__":
    main()
