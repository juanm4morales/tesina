#!/usr/bin/env python3
"""Verifica evidencia conservada y genera tablas/figuras; nunca ejecuta SUMO.

python3 datos/mendoza220k/generar.py
python3 datos/mendoza220k/generar.py --proyecto /ruta/a/marl-tlc
La segunda forma contrasta además todos los hashes del inventario y los XML
nativos. Las fuentes externas se abren solo para lectura.
"""
import argparse
import csv
import hashlib
import json
from collections import defaultdict
from decimal import Decimal as D
from pathlib import Path
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def rows(name):
    with (HERE / name).open(newline='') as f:
        return list(csv.DictReader(f))


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def es(value, places=0):
    return f'{D(str(value)):,.{places}f}'.replace(',', '@').replace('.', ',').replace('@', '.')


def table(name, columns, header, data):
    (HERE / name).write_text(
        '% Generado por datos/mendoza220k/generar.py; no editar.\n'
        + '\\begin{tabular}{' + columns + '}\\hline\n'
        + ' & '.join(header) + ' \\\\\\hline\n'
        + '\n'.join(' & '.join(r) + ' \\\\' for r in data)
        + '\n\\hline\\end{tabular}\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--proyecto', type=Path)
    args = parser.parse_args()
    copies = json.loads((HERE / 'procedencia_copias.json').read_text())
    for name, digest in copies['archivos'].items():
        assert sha(HERE / name) == digest, name
    matrix = rows('matrices_od_completas.csv')
    cases = rows('resultados_12_ejecuciones.csv')
    programs = rows('programas_tls_completos.csv')
    trajectories = rows('trayectorias_agregadas_300s.csv')
    changes = rows('intercambio_o2.csv')
    assert len(matrix) == len({r['flow_id'] for r in matrix}) == 6204
    assert len({(r['origin'], r['destination']) for r in matrix}) == 517
    hourly = defaultdict(D)
    margins = defaultdict(D)
    changed = []
    for r in matrix:
        h = int(r['hour_index'])
        before, after = (D(r[x + '_rate_veh_s']) for x in ('O1_220k', 'O2_220k'))
        dt = D(r['end']) - D(r['begin'])
        assert dt == 3600
        assert after * dt == D(r['O2_220k_expected'])
        hourly[h] += after * dt
        delta = after - before
        for side in ('origin', 'destination'):
            margins[h, side, r[side]] += delta
        if delta:
            changed.append(r)
            assert h == 3 and abs(delta) == D('0.001117230520')
            assert D('0.8') <= after / before <= D('1.2')
    assert len(changed) == 4
    assert {r['flow_id'] for r in changed} == {r['flow_id'] for r in changes}
    assert all(v == 0 for v in margins.values())
    assert sum(hourly.values()) == D('152168.75388006840000')
    assert {int(r['seed']) for r in cases} == {104759, 104729, 104771, 104861, 104879, 104891}
    assert len(cases) == 12
    for r in cases:
        L, I, A, R, W = (int(r[k]) for k in ('loaded', 'inserted', 'arrived', 'running', 'waiting'))
        assert L == I + W and I == A + R
        assert int(D(r['last_summary_label'])) + 1 == int(r['end'])
        assert D(A) / L >= D('0.75')
        assert all(int(r[k]) == 0 for k in ('teleports', 'collisions', 'discarded', 'read_ahead_residual'))
        assert abs(D(r['CR']) - D(A) / L) < D('1e-15')
        ts = [t for t in trajectories if t['case'] == r['case']]
        assert int(ts[-1]['waiting']) == W
        assert D(ts[-1]['native_time']) == D(r['end']) - 1
    grouped = defaultdict(list)
    for r in programs:
        grouped[r['tls']].append(r)
    assert len(grouped) == 73 and len(programs) == 294
    assert all(sum(D(r['duration_s']) for r in rs) == 90 for rs in grouped.values())
    assert all(r['type'] == 'static' for r in programs)
    excess = [r for r in programs if r['source_maxDur_s'] and D(r['duration_s']) > D(r['source_maxDur_s'])]
    assert len(excess) == 18
    report = {'nuevas_simulaciones': 0, 'flujos': len(matrix), 'pares_OD': 517,
              'solicitudes_esperadas_12h': str(sum(hourly.values())),
              'marginales_esperadas_conservadas': True, 'tasas_modificadas': 4,
              'programas_fijos_90s': len(grouped), 'fases_sobre_maxDur_historico': len(excess),
              'casos_verificados': len(cases)}

    if args.proyecto:
        project = args.proyecto.resolve()
        inventory = json.loads((HERE / 'fuentes_locales_sha256.json').read_text())['files']
        verified, missing = 0, []
        for name, info in inventory.items():
            p = project / name
            if info['exists']:
                assert p.is_file(), p
                assert sha(p) == info['sha256'], p
                verified += 1
            else:
                missing.append({'archivo': name, 'presente_actualmente': p.is_file()})
        commands = json.loads((HERE / 'comandos_originales.json').read_text())
        for r, command in zip(cases, commands, strict=True):
            assert r['case'] == command['case']
            relative = Path(command['command'][command['command'].index('--summary-output') + 1])
            # Los comandos originales contienen la ruta absoluta del equipo de origen.
            relative = relative.relative_to('/home/juanm4/Dev/marl-tlc')
            n, integral = 0, 0
            for _, e in ET.iterparse(project / relative, events=('end',)):
                if e.tag == 'step':
                    assert D(e.get('time')) == int(r['begin']) + n
                    n += 1
                    integral += int(e.get('waiting'))
                    assert all(int(e.get(k)) == 0 for k in ('teleports', 'collisions', 'discarded'))
                    last = dict(e.attrib)
                    e.clear()
            assert n == int(r['end']) - int(r['begin'])
            assert integral == int(r['backlog_vehicle_seconds'])
            for k in ('loaded', 'inserted', 'arrived', 'running', 'waiting'):
                assert last[k] == r[k]
        # Contraste de cada tasa contra los XML efectivos y de la geometría heredada.
        final = project / 'experiments/mendoza_scenario/results/mendoza_220k_od_adjustment_20261017'
        for name, col in [('O1_220000_reference.rou.xml', 'O1_220k'), ('O2_220000_benegas_h3.rou.xml', 'O2_220k')]:
            fs = {f.get('id'): f for f in ET.parse(final / 'demand' / name).getroot().findall('flow')}
            assert len(fs) == len(matrix)
            for r in matrix:
                assert D(fs[r['flow_id']].get('period')[4:-1]) == D(r[col + '_rate_veh_s'])
        nets = [p for name, info in inventory.items() if info['exists'] and name.endswith('.net.xml')
                for p in [project / name]]
        p2 = next(p for p in nets if sha(p).startswith('2efa0e9f'))
        old = next(p for p in nets if sha(p).startswith('988a1d27'))
        a, b = (ET.parse(p).getroot() for p in (old, p2))
        for tag in ('edge', 'junction', 'connection'):
            assert [ET.tostring(e) for e in a.findall(tag)] == [ET.tostring(e) for e in b.findall(tag)], tag
        def states(net):
            return {t.get('id'): [p.get('state') for p in t.findall('phase')] for t in net.findall('tlLogic')}
        assert states(a) == states(b)
        report.update(hashes_externos_verificados=verified, summaries_nativos_verificados=12,
                      geometria_conexiones_estados_conservados=True, antecedentes_ausentes=missing)
    (HERE / 'verificacion.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')

    summary = []
    for window in ('2h', '12h'):
        rs = [r for r in cases if r['window'] == window]
        ratios = [D(r['arrived']) / D(r['loaded']) for r in rs]
        summary.append([window.replace('h', ' h'), '6/6', es(sum(int(r['arrived']) for r in rs) / 6, 1),
                        es(min(int(r['waiting']) for r in rs)) + '--' + es(max(int(r['waiting']) for r in rs)),
                        es(100 * min(ratios), 2) + '--' + es(100 * max(ratios), 2) + r'\%'])
    table('tabla_sintesis.tex', 'lrrrr', ['Ventana', 'Aceptados', 'Completados (media)', 'Pendientes (rango)', r'\shortstack{Llegaron/\\cargados (\%)}'], summary)
    for window in ('2h', '12h'):
        data = [[r['seed']] + [es(r[k]) for k in ('loaded', 'inserted', 'arrived', 'running', 'waiting')]
                + [es(D(r['arrived']) / D(r['loaded']), 6)] for r in cases if r['window'] == window]
        table('tabla_casos_' + window + '.tex', 'rrrrrrr', ['Semilla', '$L$', '$I$', '$A$', '$R$', '$W$', '$A/L$'], data)
    table('tabla_tasas.tex', 'lrr', ['Par OD', 'O1 a 220.000 (veh/s)', 'O2 (veh/s)'],
          [[r['origin'] + r'$\to$' + r['destination'], es(r['O1_220k_rate_veh_s'], 12), es(r['O2_220k_rate_veh_s'], 12)] for r in changes])
    offsets = json.loads((HERE / 'diferencias_tls.json').read_text())['T0_to_P2']
    assert len(offsets) == 11
    def ident(s):
        return r'\texttt{' + s.replace('_', r'\_}\allowbreak\texttt{') + '}'
    table('tabla_desfases.tex', 'lrr', ['Controlador', 'T0 (s)', 'P2 (s)'],
          [[ident(r['tls']), *r['offset']] for r in offsets])
    table('tabla_fases_excedidas.tex', 'lrrr', ['Controlador', 'Índice de fase', 'Duración P2 (s)', r'\texttt{maxDur} anterior (s)'],
          [[ident(r['tls']), r['phase_index'], r['duration_s'], r['source_maxDur_s']] for r in excess])
    # Tres tablas: mantienen tamaño legible sin reducir las 73 filas.
    pg = [[ident(tls), rs[0]['offset_s'], ', '.join(r['duration_s'] for r in rs)] for tls, rs in grouped.items()]
    for j, start in enumerate(range(0, len(pg), 25), 1):
        table(f'tabla_programas_{j}.tex', r'>{\raggedright\arraybackslash}p{6.4cm}r>{\raggedright\arraybackslash}p{6.4cm}',
              ['Controlador', 'Desfase (s)', 'Duraciones en orden (s)'], pg[start:start + 25])

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False, 'pdf.fonttype': 42})
    fig, ax = plt.subplots(figsize=(6.3, 3.5), layout='constrained')
    ax.axvspan(0, 12, color='0.94', label='Horizonte largo (12 h)')
    ax.axvspan(.5, 2.5, color='0.78', label='Horizonte corto (2 h)')
    ax.stairs([float(hourly[h]) for h in range(12)], range(13), baseline=None, color='#426d96', linewidth=2)
    ax.set(ylabel='Solicitudes esperadas por hora', xlim=(0, 12), ylim=(0, 18000))
    ax.set_title('Perfil horario de solicitudes', fontsize=10)
    ax.set_xticks([0, 3, 6, 9, 12], ['06:00', '09:00', '12:00', '15:00', '18:00'])
    ax.tick_params(axis='x', labelsize=8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: es(x)))
    ax.grid(axis='y', color='0.9')
    ax.legend(loc='lower right', fontsize=8, framealpha=1)
    ax.set_xlabel('Hora del día (convención del escenario)')
    fig.savefig(ROOT / 'imagenes/mendoza220k_demanda.pdf', metadata={'CreationDate': None})
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(6.3, 3.4), layout='constrained')
    for i, seed in enumerate(dict.fromkeys(r['seed'] for r in cases)):
        ts = [r for r in trajectories if r['window'] == '12h' and r['seed'] == seed]
        ax.plot([float(r['native_time']) for r in ts], [int(r['waiting']) for r in ts],
                color=str(.15 + i * .10), linewidth=1.25, linestyle=['-', '--', ':', '-.', (0, (5, 1)), (0, (2, 1))][i])
    ax.axvspan(10800, 14400, facecolor='none', edgecolor='0.55', hatch='///')
    ax.text(12600, 28500, 'Redistribución', ha='center', fontsize=9)
    ax.set(xlabel='Tiempo del modelo (s)', ylabel='Vehículos pendientes de ingreso', xlim=(0, 43200), ylim=(0, 31000))
    ax.set_xticks([0, 10800, 21600, 32400, 43200])
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: es(x)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: es(x)))
    ax.grid(axis='y', color='0.9')
    fig.savefig(ROOT / 'imagenes/mendoza220k_pendientes.pdf', metadata={'CreationDate': None})
    plt.close(fig)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
