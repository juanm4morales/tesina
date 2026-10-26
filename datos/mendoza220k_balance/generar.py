#!/usr/bin/env python3
"""Generate compact LaTeX tables from the archived Mendoza balance evidence."""
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "fuentes"
EXPECTED_INPUTS = {
    "nets/Mendoza/mendoza_220k_balance.net.xml": "06222972799a5583f9d9846f69909e6a33cb01c06cc5e2f602c1511cf7671115",
    "nets/Mendoza/mendoza_220k_balance.taz.xml": "b80859cb6f162601dd4b7dc8599144e0bf2608dd38a5bc1ca5cd2e1236702e0a",
    "nets/Mendoza/mendoza_220k_balance.rou.xml": "917e1904329d6b84fece04766a4196eebae0fb2304a729944f5f52df2c00e0ca",
    "nets/Mendoza/mendoza_220k_balance_12h.sumocfg": "eba9d238efdfc98d732d00d0c60183f30340b8869f03583b14f0da02ff2d3ddc",
    "nets/Mendoza/mendoza_220k_balance_2h.sumocfg": "6d0922b1c9374b60b214e30d85efeb50dcb90d0f311af9620d22d3ac470b03cd",
    "nets/Mendoza/gran_mendoza2.add.xml": "fe96f276987b8f9ccd71736a76a8524eb948b192b2326221b92f4959749b8a38",
}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def verify(project=None):
    manifest = load_json(SOURCE / "manifest.json")
    validation = load_json(SOURCE / "validation.json")
    assert manifest["scenario"] == validation["scenario"] == "mendoza_220k_balance"
    assert manifest["sumo_version"].endswith("1.27.1")
    assert manifest["inputs_sha256"] == validation["inputs_sha256"] == EXPECTED_INPUTS
    for name, digest in (("mendoza_220k_balance_2h.sumocfg", EXPECTED_INPUTS["nets/Mendoza/mendoza_220k_balance_2h.sumocfg"]),
                         ("mendoza_220k_balance_12h.sumocfg", EXPECTED_INPUTS["nets/Mendoza/mendoza_220k_balance_12h.sumocfg"])):
        assert hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == digest
    assert validation["development_seed"] == 104729
    assert validation["new_confirmatory_seeds"] == [2026102001, 2026102002, 2026102003]
    assert len(validation["validation"]) == 6
    expected_case_hashes = {
        (row["seed"], row["horizon"]): row["sha256"] for row in validation["validation"]
    }
    expected_case_hashes.update({
        (104729, "2h"): manifest["validation"]["compact_2h"]["sha256"],
        (104729, "12h"): manifest["validation"]["compact_12h"]["sha256"],
    })
    config_hashes = load_json(SOURCE / "configs_sha256.json")

    cases = {}
    for seed, horizon in [(104729, "2h"), (104729, "12h")]+[
            (s, h) for s in validation["new_confirmatory_seeds"] for h in ("2h", "12h")]:
        data = load_json(SOURCE / "casos" / f"{seed}_{horizon}.json")
        case_path = SOURCE / "casos" / f"{seed}_{horizon}.json"
        assert hashlib.sha256(case_path.read_bytes()).hexdigest() == expected_case_hashes[(seed, horizon)]
        case = data["case"]
        assert case["seed"] == seed and case["horizon"] == horizon
        assert case["begin"] == (1800 if horizon == "2h" else 0)
        assert case["end"] == (9000 if horizon == "2h" else 43200)
        if seed != 104729:
            cfg_name = f"seed{seed}_{horizon}.sumocfg"
            cfg_path = SOURCE / "configs" / cfg_name
            assert hashlib.sha256(cfg_path.read_bytes()).hexdigest() == config_hashes[cfg_name]
            cfg = ET.parse(cfg_path).getroot()
            cfg_values = {element.tag: element.attrib["value"] for element in cfg.iter() if "value" in element.attrib}
            assert cfg_values["seed"] == str(seed)
            assert cfg_values["begin"] == str(case["begin"]) and cfg_values["end"] == str(case["end"])
            assert cfg_values["step-length"] == "1" and cfg_values["time-to-teleport"] == "300"
            assert cfg_values["max-num-teleports"] == "0" and cfg_values["collision.action"] == "warn"
        assert data["acceptance"] == "passed" and data["horizon_complete"]
        last = data["last"]
        loaded, inserted = int(last["loaded"]), int(last["inserted"])
        arrived, running, waiting = int(last["arrived"]), int(last["running"]), int(last["waiting"])
        assert loaded == inserted + waiting and inserted == arrived + running
        assert int(last["teleports"]) == int(last["collisions"]) == int(last["discarded"]) == 0
        assert abs(float(data["CR"]) - arrived / loaded) < 1e-12
        cases[(seed, horizon)] = data

    programs = load_json(SOURCE / "programas.json")
    topology = load_json(SOURCE / "topologia.json")
    assert topology["network_sha256"] == EXPECTED_INPUTS["nets/Mendoza/mendoza_220k_balance.net.xml"]
    assert {k: topology["net_element_counts"][k] for k in ("edge", "lane", "connection", "tlLogic")} == {
        "edge": 255, "lane": 554, "connection": 744, "tlLogic": 74}
    assert len(topology["taz_ids"]) == 37
    assert set(range(39)) - {int(taz) for taz in topology["taz_ids"]} == {6, 9}
    assert topology["route_element_counts"]["flow"] == 6204
    assert len(programs) == 74 and len({p["id"] for p in programs}) == 74
    assert sorted(p["id"] for p in programs) == topology["tls_ids"]
    for p in programs:
        assert sum(phase["duration"] for phase in p["phases"]) == 90
        assert all(len(phase["state"]) == len(p["phases"][0]["state"]) for phase in p["phases"])
        assert any("y" in phase["state"] and phase["duration"] == 5 for phase in p["phases"])
    if project is not None:
        project = project.resolve()
        for relpath, digest in EXPECTED_INPUTS.items():
            actual = hashlib.sha256((project / relpath).read_bytes()).hexdigest()
            assert actual == digest, f"SHA-256 mismatch: {relpath}"
        net = project / "nets/Mendoza/mendoza_220k_balance.net.xml"
        net_counts, actual_programs = {}, []
        for _, element in ET.iterparse(net, events=("end",)):
            net_counts[element.tag] = net_counts.get(element.tag, 0) + 1
            if element.tag == "tlLogic":
                actual_programs.append({
                    "id": element.attrib["id"],
                    "offset": int(element.attrib.get("offset", "0")),
                    "phases": [{"duration": int(phase.attrib["duration"]), "state": phase.attrib["state"]}
                               for phase in element.findall("phase")],
                })
        taz_ids = []
        for _, element in ET.iterparse(project / "nets/Mendoza/mendoza_220k_balance.taz.xml", events=("end",)):
            if element.tag == "taz":
                taz_ids.append(element.attrib["id"])
            element.clear()
        flow_count = 0
        for _, element in ET.iterparse(project / "nets/Mendoza/mendoza_220k_balance.rou.xml", events=("end",)):
            flow_count += element.tag == "flow"
            element.clear()
        assert {k: net_counts.get(k, 0) for k in ("edge", "lane", "connection", "tlLogic")} == {
            "edge": 255, "lane": 554, "connection": 744, "tlLogic": 74}
        assert not any(element.tag == "edge" and element.attrib["id"].startswith(":")
                       for _, element in ET.iterparse(net, events=("end",)))
        assert sorted(taz_ids, key=int) == topology["taz_ids"]
        assert flow_count == topology["route_element_counts"]["flow"] == 6204
        assert sorted(actual_programs, key=lambda p: p["id"]) == sorted(programs, key=lambda p: p["id"])
        print(f"--proyecto: 6 input hashes, XML topology, 74 TLS programs, 37 TAZ, {flow_count} flows verified.")
    return manifest, validation, cases, programs


def fmt(n):
    return f"{int(n):,}".replace(",", ".")


def decimal(value):
    return f"{value:.2f}".replace(".", ",")


def write(name, body):
    (HERE / name).write_text(body.rstrip() + "\n", encoding="utf-8")


def phase_sequence(phases):
    """Label each archived signal state without inferring it from duration."""
    result = []
    for phase in phases:
        state = phase["state"]
        if any(signal in "yY" for signal in state):
            kind = "A"
        elif any(signal in "gG" for signal in state):
            kind = "V"
        elif set(state) == {"r"}:
            kind = "R"
        else:
            raise ValueError(f"Unclassified signal state: {state}")
        result.append(r"\mbox{" + f"{kind}\\,{phase['duration']}" + "}")
    return "; ".join(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proyecto", type=Path, help="marl-tlc root to verify input hashes and XML")
    args = parser.parse_args()
    manifest, validation, cases, programs = verify(args.proyecto)
    rows = [r"\begin{tabular}{@{}>{\raggedright\arraybackslash}p{5.2cm}>{\raggedright\arraybackslash}p{8.5cm}@{}}\hline", "Entrada & SHA-256 \\\\ \\hline"]
    for path, digest in manifest["inputs_sha256"].items():
        hash_breakable = "\\allowbreak{}".join(digest[i:i+8] for i in range(0, len(digest), 8))
        rows.append(f"\\path{{{path}}} & \\texttt{{{hash_breakable}}}" + " " + chr(92)*2)
    rows.extend([r"\hline\end{tabular}"])
    write("tabla_entradas.tex", "\n".join(rows))

    options = []
    for case in ("2h", "12h"):
        cfg_path = SOURCE / f"mendoza_220k_balance_{case}.sumocfg"
        cfg = ET.parse(cfg_path).getroot()
        vals = {element.tag: element.attrib["value"] for element in cfg.iter() if "value" in element.attrib}
        options.append((case, vals))
    opts = [r"\begin{tabular}{@{}lcc@{}}\hline", "Opción & 2 h & 12 h \\\\ \\hline"]
    opts += [
        f"Inicio $t$ (s) & {options[0][1]['begin']} & {options[1][1]['begin']}" + " " + chr(92)*2,
        f"Fin $t$ (s) & {options[0][1]['end']} & {options[1][1]['end']}" + " " + chr(92)*2,
        f"Paso (s) & {options[0][1]['step-length']} & {options[1][1]['step-length']}" + " " + chr(92)*2,
        f"Umbral de teletransporte (s) & {options[0][1]['time-to-teleport']} & {options[1][1]['time-to-teleport']}" + " " + chr(92)*2,
        f"Máximo de teletransportes & {options[0][1]['max-num-teleports']} & {options[1][1]['max-num-teleports']}" + " " + chr(92)*2,
        f"Acción ante colisión & \\texttt{{{options[0][1]['collision.action']}}} & \\texttt{{{options[1][1]['collision.action']}}}" + " " + chr(92)*2,
        f"Semilla de desarrollo & {options[0][1]['seed']} & {options[1][1]['seed']}" + " " + chr(92)*2,
        f"Asignación de zonas & \\texttt{{{options[0][1]['junction-taz']}}} & \\texttt{{{options[1][1]['junction-taz']}}}" + " " + chr(92)*2,
        r"\hline\end{tabular}",
    ]
    assert options[0][1] == options[1][1] | {"begin": "1800", "end": "9000"}
    write("tabla_opciones.tex", "\n".join(opts))

    cases_tex = r"\begin{tabular}{@{}rrrrrrrr@{}}\hline" + "\n"
    cases_tex += "Semilla & $L$ & $I$ & $A$ & $R$ & $W$ & CR & TP/Col./Desc. \\\\ \\hline\n"
    for seed in (104729, *validation["new_confirmatory_seeds"]):
        d = cases[(seed, "2h")]
        x = d["last"]
        cases_tex += f"{seed} & {fmt(x['loaded'])} & {fmt(x['inserted'])} & {fmt(x['arrived'])} & {fmt(x['running'])} & {fmt(x['waiting'])} & {decimal(float(d['CR'])*100)}\\% & 0/0/0 \\\\ \n"
    cases_tex += r"\hline\end{tabular}"
    write("tabla_casos_2h.tex", cases_tex)
    cases_tex = r"\begin{tabular}{@{}rrrrrrrr@{}}\hline" + "\n"
    cases_tex += "Semilla & $L$ & $I$ & $A$ & $R$ & $W$ & CR & TP/Col./Desc. \\\\ \\hline\n"
    for seed in (104729, *validation["new_confirmatory_seeds"]):
        d = cases[(seed, "12h")]
        x = d["last"]
        cases_tex += f"{seed} & {fmt(x['loaded'])} & {fmt(x['inserted'])} & {fmt(x['arrived'])} & {fmt(x['running'])} & {fmt(x['waiting'])} & {decimal(float(d['CR'])*100)}\\% & 0/0/0 \\\\ \n"
    cases_tex += r"\hline\end{tabular}"
    write("tabla_casos_12h.tex", cases_tex)

    summary = [r"\begin{tabular}{@{}lrrrr@{}}\hline", "Ventana & $n$ & Media $A$ & CR medio & Rango $W$ \\\\ \\hline"]
    for horizon in ("2h", "12h"):
        subset = [cases[(s, horizon)] for s in validation["new_confirmatory_seeds"]]
        arrivals = [int(d["last"]["arrived"]) for d in subset]
        cr = [float(d["CR"]) for d in subset]
        waiting = [int(d["last"]["waiting"]) for d in subset]
        summary.append(f"{horizon} & 3 & {fmt(round(sum(arrivals)/3))} & {decimal(sum(cr)/3*100)}\\% & {fmt(min(waiting))}--{fmt(max(waiting))}" + " " + chr(92)*2)
    summary.append(r"\hline\end{tabular}")
    write("tabla_sintesis.tex", "\n".join(summary))

    for index, group in enumerate((programs[:25], programs[25:50], programs[50:]), 1):
        body = [r"\begin{tabular}{@{}r>{\ttfamily\raggedright\arraybackslash}p{5.7cm}rp{6.5cm}@{}}\hline",
                "N.º & ID & Desfase (s) & Secuencia de estados y duraciones (s) \\\\ \\hline"]
        for num, p in enumerate(group, start=1 if index == 1 else (26 if index == 2 else 51)):
            seq = phase_sequence(p["phases"])
            body.append(f"{num} & \\path{{{p['id']}}} & {p['offset']} & {seq}" + " " + chr(92)*2)
        body.append(r"\hline\end{tabular}")
        write(f"tabla_programas_{index}.tex", "\n".join(body))
    print("Mendoza balance tables generated; 8 cases, 74 controllers, input hashes and balances verified.")


if __name__ == "__main__":
    main()
