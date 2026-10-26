#!/usr/bin/env python3
"""Build the explicitly requested Civit variant; never starts a simulation.

Edit plain XML patches and TLS definitions, then let netconvert write the net.
The historically validated 220k files are immutable inputs.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal, getcontext
import hashlib
import json
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
NETS = ROOT / 'nets/Mendoza'
CAMPAIGN = ROOT / 'experiments/mendoza_scenario/results/mendoza_civit_static_20261020'
BUILD = CAMPAIGN / 'build'
NAME = 'mendoza_civit_static'
TARGET = '10936722266'
YELLOW = 5
PINS = {
    'mendoza_220k_static.net.xml': '2efa0e9f9806040a596d446f6668635307649c610db020c13b6fd52f03b9e0a8',
    'mendoza_220k_static.rou.xml': '84d512c8f25b30f743f432cafdcfd4c5fcbd643634c10f46e674e172e96b4c46',
    'gran_mendoza2_fixed.taz.xml': 'cf710f36e1c5021d3d3e585d897262310579bf1c34466ecca6290e1715923e40',
    'gran_mendoza2.add.xml': 'fe96f276987b8f9ccd71736a76a8524eb948b192b2326221b92f4959749b8a38',
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()


def write_xml(root, path):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)
    ET.indent(root, space='    ')
    with path.open('xb') as f:
        ET.ElementTree(root).write(f, encoding='utf-8', xml_declaration=True)


def write_json(data, path):
    with Path(path).open('x') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write('\n')


def command(argv, label):
    p = subprocess.run(list(map(str, argv)), text=True, capture_output=True, timeout=120)
    write_json({'argv': list(map(str, argv)), 'returncode': p.returncode,
                'stdout': p.stdout, 'stderr': p.stderr}, BUILD / f'{label}.json')
    if p.returncode:
        raise RuntimeError(f'{label}: {p.stderr}')
    return p


def movement(c):
    return tuple(c.get(k, '') for k in ('from', 'to', 'fromLane', 'toLane'))


def apportion(total, weights, minimum=1):
    """Largest remainders; exact integer budget and deterministic tie breaks."""
    from fractions import Fraction
    raw = [Fraction(total * w, sum(weights)) for w in weights]
    result = [int(x) for x in raw]
    for i in sorted(range(len(raw)), key=lambda i: (-(raw[i] - result[i]), i))[:total - sum(result)]:
        result[i] += 1
    if min(result) < minimum or sum(result) != total:
        raise ValueError('insufficient green budget')
    return result


def normalize_logic(old, index_map):
    logic = deepcopy(old)
    phases = logic.findall('phase')
    before = [int(p.get('duration')) for p in phases]
    green = [i for i, p in enumerate(phases)
             if not any(c in p.get('state') for c in 'yY') and any(c in p.get('state') for c in 'gG')]
    for p in phases:
        state = p.get('state')
        p.set('state', ''.join(state[index_map[i]] for i in range(len(state))))
        if any(c in state for c in 'yY'):
            p.set('duration', str(YELLOW))
    budget = 90 - sum(int(p.get('duration')) for i, p in enumerate(phases) if i not in green)
    new_green = apportion(budget, [before[i] for i in green], minimum=5)
    for i, seconds in zip(green, new_green):
        phases[i].set('duration', str(seconds))
    assert sum(int(p.get('duration')) for p in phases) == 90
    return logic, {'id': old.get('id'), 'before': before,
                   'after': [int(p.get('duration')) for p in phases]}


def directional_zones(source, net):
    """A boundary exit is a sink, not an origin requiring a U-turn."""
    edges = {e.get('id'): e for e in net.findall('edge')}
    outgoing, incoming = defaultdict(set), defaultdict(set)
    for c in net.findall('connection'):
        outgoing[c.get('from')].add(c.get('to'))
        incoming[c.get('to')].add(c.get('from'))
    root = ET.Element('additional')
    changes = []
    zone_map = {}
    for z in source.findall('taz'):
        members = z.get('edges').split()
        src = [e for e in members if outgoing[e]]
        sink = [e for e in members if incoming[e]]
        if not src and not sink:
            # An isolated pre-existing edge may belong to an unused zone. Keep
            # the role map so reachability rejects it if any flow uses it.
            zone_map[z.get('id')] = ([], [])
            changes.append({'id': z.get('id'), 'old': members, 'sources': [],
                            'sinks': [], 'omitted_unused_isolated_zone': True})
            continue
        nz = ET.SubElement(root, 'taz', {'id': z.get('id')})
        for tag, selected in [('tazSource', src), ('tazSink', sink)]:
            for e in selected:
                ET.SubElement(nz, tag, {'id': e, 'weight': '1'})
        zone_map[z.get('id')] = (src, sink)
        if src != members or sink != members:
            changes.append({'id': z.get('id'), 'old': members, 'sources': src, 'sinks': sink})
    return root, zone_map, changes


def reduce_benegas(source):
    """Reduce TAZ10 by 5%; redistribute within destination/hour, fixed TAZ28.

    The hourly destination totals and full expected volume remain unchanged.
    Origin marginals deliberately change. This is a synthetic sensitivity.
    """
    getcontext().prec = 40
    root = deepcopy(source)
    groups = defaultdict(list)
    for f in root.findall('flow'):
        groups[(f.get('begin'), f.get('end'), f.get('toTaz'))].append(f)
    ledger = []
    for key, flows in sorted(groups.items()):
        selected = [f for f in flows if f.get('fromTaz') == '10']
        if not selected:
            continue
        assert len(selected) == 1
        f = selected[0]
        # Cells touching TAZ28 stay frozen, including 10->28 if ever present.
        if f.get('toTaz') == '28':
            continue
        rate = Decimal(f.get('period')[4:-1])
        removed = rate * Decimal('0.05')
        recipients = [g for g in flows if g.get('fromTaz') not in ('10', '28')]
        if not recipients:
            raise ValueError(f'no existing support to redistribute {key}')
        base = [Decimal(g.get('period')[4:-1]) for g in recipients]
        total = sum(base)
        changes = []
        f.set('period', f'exp({rate - removed:.18f})')
        allocated = Decimal(0)
        for i, (g, old_rate) in enumerate(zip(recipients, base)):
            delta = removed - allocated if i == len(recipients) - 1 else (removed * old_rate / total).quantize(Decimal('0.000000000000000001'))
            allocated += delta
            g.set('period', f'exp({old_rate + delta:.18f})')
            changes.append({'flow': g.get('id'), 'delta_rate': str(delta)})
        ledger.append({'from_flow': f.get('id'), 'removed_rate': str(removed),
                       'expected_vehicles': str(removed * (Decimal(key[1]) - Decimal(key[0]))),
                       'recipients': changes})
    return root, ledger


def reachability(net, zones, routes):
    adj = defaultdict(set)
    for c in net.findall('connection'):
        adj[c.get('from')].add(c.get('to'))
    cache = {}
    pairs = {(f.get('fromTaz'), f.get('toTaz')) for f in routes.findall('flow')}
    failures, unavailable_choices = [], []
    for origin, destination in sorted(pairs):
        if not zones[origin][0] or not zones[destination][1]:
            raise ValueError(f'used zone role is disconnected: {origin}->{destination}')
        for src in zones[origin][0]:
            if src not in cache:
                seen, q = {src}, deque([src])
                while q:
                    for e in adj[q.popleft()] - seen:
                        seen.add(e)
                        q.append(e)
                cache[src] = seen
            if not any(sink in cache[src] for sink in zones[destination][1]):
                failures.append([origin, destination, src])
            for sink in zones[destination][1]:
                if sink not in cache[src]:
                    unavailable_choices.append([origin, destination, src, sink])
    if failures:
        raise ValueError(f'unreachable OD choices: {failures}')
    return {'pairs': len(pairs), 'each_source_reaches_destination_TAZ': True,
            'unavailable_individual_sink_choices': unavailable_choices,
            'note': 'TAZ sinks are alternative destinations connected to a virtual sink; at least one must be reachable from each source'}


def config(path, begin, end):
    cfg = ET.Element('sumoConfiguration')
    sections = {
        'input': {'net-file': f'{NAME}.net.xml', 'route-files': f'{NAME}.rou.xml',
                  'additional-files': f'{NAME}.taz.xml,gran_mendoza2.add.xml', 'junction-taz': 'true'},
        'time': {'begin': str(begin), 'end': str(end), 'step-length': '1'},
        'processing': {'time-to-teleport': '300', 'max-num-teleports': '0',
                       'max-depart-delay': '-1', 'collision.action': 'warn'},
        'random_number': {'seed': '104729'},
    }
    for name, values in sections.items():
        s = ET.SubElement(cfg, name)
        for key, value in values.items():
            ET.SubElement(s, key, {'value': value})
    write_xml(cfg, path)


def build():
    if (BUILD / 'manifest.json').exists() or any(NETS.glob(NAME + '*')):
        raise FileExistsError('candidate already exists; refusing rebuild')
    for name, digest in PINS.items():
        if sha(NETS / name) != digest:
            raise ValueError(f'frozen input changed: {name}')
    BUILD.mkdir(parents=True, exist_ok=True)
    source = ET.parse(NETS / 'mendoza_220k_static.net.xml').getroot()
    routes = ET.parse(NETS / 'mendoza_220k_static.rou.xml').getroot()
    turns = [c for c in source.findall('connection') if c.get('dir') in ('t', 'T')]
    patch = ET.Element('connections')
    for c in turns:
        ET.SubElement(patch, 'delete', {k: c.get(k) for k in ('from', 'to', 'fromLane', 'toLane')})
    write_xml(patch, BUILD / 'remove_uturns.con.xml')
    nodes = ET.Element('nodes')
    ET.SubElement(nodes, 'node', {'id': TARGET, 'type': 'traffic_light', 'tl': TARGET})
    write_xml(nodes, BUILD / 'benegas_civit.nod.xml')
    raw_path = BUILD / 'rebuilt.net.xml'
    command(['/usr/bin/netconvert', '-s', NETS / 'mendoza_220k_static.net.xml',
             '--node-files', BUILD / 'benegas_civit.nod.xml',
             '--connection-files', BUILD / 'remove_uturns.con.xml',
             '--tls.rebuild', '--tls.yellow.time', str(YELLOW), '--tls.cycle.time', '90',
             '--no-turnarounds', '--no-internal-links', '--output.street-names',
             '--offset.disable-normalization', '-o', raw_path], 'netconvert_rebuild')
    raw = ET.parse(raw_path).getroot()
    src_conn = {movement(c): c for c in source.findall('connection')}
    raw_conn = {movement(c): c for c in raw.findall('connection')}
    removed = set(src_conn) - set(raw_conn)
    added = set(raw_conn) - set(src_conn)
    if removed != {movement(c) for c in turns} or added:
        raise ValueError(f'unregistered connection changes: removed={removed}, added={added}')
    # Netconvert may change link ordering. Recover old state by movement identity.
    tls = ET.Element('tlLogics')
    timing = []
    for old in source.findall('tlLogic'):
        tid = old.get('id')
        mapping = {}
        for key, c in raw_conn.items():
            if c.get('tl') == tid:
                prev = src_conn[key]
                if prev.get('tl') != tid:
                    raise ValueError('controller identity changed')
                new_i, old_i = int(c.get('linkIndex')), int(prev.get('linkIndex'))
                if new_i in mapping and mapping[new_i] != old_i:
                    raise ValueError('ambiguous TLS signal mapping')
                mapping[new_i] = old_i
        size = len(old.find('phase').get('state'))
        if sorted(mapping) != list(range(size)):
            raise ValueError(f'{tid}: incomplete TLS mapping')
        logic, diff = normalize_logic(old, mapping)
        tls.append(logic)
        timing.append(diff)
    # Netconvert assigns the target's new links. Keep generated permissive greens
    # for Civit's opposed left turn, protecting all Benegas movements separately.
    target_conn = [c for c in raw.findall('connection') if c.get('tl') == TARGET]
    if len(target_conn) != 10 or sorted(int(c.get('linkIndex')) for c in target_conn) != list(range(10)):
        raise ValueError('expected ten unique newly signalled movements')
    generated = next(t for t in raw.findall('tlLogic') if t.get('id') == TARGET)
    civit_state = None
    for p in generated.findall('phase'):
        s = p.get('state')
        if all(s[int(c.get('linkIndex'))] == 'r' for c in target_conn if c.get('from') == '446118223#7') and 'y' not in s and 'G' in s:
            civit_state = s
    if civit_state is None:
        raise ValueError('netconvert did not generate a separate Civit service stage')
    benegas = ''.join('G' if next(c for c in target_conn if int(c.get('linkIndex')) == i).get('from') == '446118223#7' else 'r' for i in range(10))
    target = ET.SubElement(tls, 'tlLogic', {'id': TARGET, 'type': 'static', 'programID': '0', 'offset': '0'})
    for green, seconds, name in [(benegas, 18, 'Benegas'), (civit_state, 60, 'Civit')]:
        ET.SubElement(target, 'phase', {'duration': str(seconds), 'state': green, 'name': name})
        ET.SubElement(target, 'phase', {'duration': str(YELLOW), 'state': ''.join('y' if v in 'Gg' else 'r' for v in green), 'name': f'{name}_amarillo'})
        ET.SubElement(target, 'phase', {'duration': '1', 'state': 'r' * 10, 'name': f'{name}_despeje'})
    write_xml(tls, BUILD / 'static_plans.tll.xml')
    output = NETS / f'{NAME}.net.xml'
    command(['/usr/bin/netconvert', '-s', raw_path, '--tllogic-files', BUILD / 'static_plans.tll.xml',
             '--no-turnarounds', '--no-internal-links', '--output.street-names',
             '--offset.disable-normalization', '-o', output], 'netconvert_plans')
    final = ET.parse(output).getroot()
    if {movement(c) for c in final.findall('connection')} != set(raw_conn):
        raise ValueError('connections changed during TLS plan import')
    if any(c.get('dir') in ('t', 'T') for c in final.findall('connection')):
        raise ValueError('U-turn survived')
    if len(final.findall('tlLogic')) != 74 or any(t.get('type') != 'static' for t in final.findall('tlLogic')):
        raise ValueError('expected 74 static controllers')
    zones, zone_map, zone_diff = directional_zones(ET.parse(NETS / 'gran_mendoza2_fixed.taz.xml').getroot(), final)
    candidate_routes, ledger = reduce_benegas(routes)
    # Freeze insertion semantics that were implicit in the successful SUMO 1.25
    # campaign; do not rely on changed 1.27 global defaults.
    for f in candidate_routes.findall('flow'):
        f.set('departLane', 'first')
        f.set('departSpeed', '0')
    route_path, zone_path = NETS / f'{NAME}.rou.xml', NETS / f'{NAME}.taz.xml'
    write_xml(candidate_routes, route_path)
    write_xml(zones, zone_path)
    connectivity = reachability(final, zone_map, candidate_routes)
    for suffix, begin, end in [('2h', 1800, 9000), ('4h', 0, 14400), ('12h', 0, 43200)]:
        config(NETS / f'{NAME}_{suffix}.sumocfg', begin, end)
    schema_checks = []
    for path in [output, route_path, zone_path] + sorted(NETS.glob(NAME + '*.sumocfg')):
        schema = 'net_file.xsd' if path == output else 'routes_file.xsd' if path == route_path else 'additional_file.xsd' if path == zone_path else 'sumoConfiguration.xsd'
        p = subprocess.run(['xmllint', '--nonet', '--noout', '--schema', '/usr/share/sumo/data/xsd/' + schema, str(path)], capture_output=True, text=True, timeout=60)
        schema_checks.append({'file': str(path.relative_to(ROOT)), 'returncode': p.returncode, 'stderr': p.stderr})
        if p.returncode:
            raise ValueError(p.stderr)
    manifest = {
        'candidate': NAME, 'status': 'built_pending_screen', 'nominal_daily': 220000,
        'source_hashes': PINS, 'builder_sha256': sha(__file__),
        'netconvert_sha256': sha('/usr/bin/netconvert'), 'sumo_sha256': sha('/usr/bin/sumo'),
        'version': subprocess.check_output(['/usr/bin/sumo', '--version'], text=True).splitlines()[0],
        'inputs': {str(p.relative_to(ROOT)): sha(p) for p in sorted(NETS.glob(NAME + '*'))},
        'support_shapes': {'path': 'nets/Mendoza/gran_mendoza2.add.xml', 'sha256': PINS['gran_mendoza2.add.xml']},
        'removed_uturns': [dict(c.attrib) for c in turns], 'zone_diff': zone_diff,
        'timing_diff': timing, 'target_phases': [dict(p.attrib) for p in target.findall('phase')],
        'target_movements': [dict(c.attrib) for c in target_conn],
        'demand_ledger': ledger, 'reachability': connectivity, 'schema_checks': schema_checks,
        'limits': {'max_wall_seconds': 3600, 'max_bytes': 2 * 1024**3, 'close_seconds': 120, 'retries': 0},
        'registered_cases': [
            {'id': 'screen_4h_104729', 'seed': 104729, 'begin': 0, 'end': 14400},
            {'id': 'validation_12h_104729', 'seed': 104729, 'begin': 0, 'end': 43200, 'requires': ['screen_4h_104729']},
            {'id': 'validation_2h_104729', 'seed': 104729, 'begin': 1800, 'end': 9000, 'requires': ['validation_12h_104729']},
        ],
        'acceptance': {'teleports': 0, 'collisions': 0, 'discarded': 0, 'min_CR': .75, 'complete_horizon': True},
        'caveat': 'combined model revision; no attribution to an individual change; one known seed; no field timing validation',
    }
    write_json(manifest, BUILD / 'manifest.json')
    return manifest


if __name__ == '__main__':
    m = build()
    print(json.dumps({'candidate': m['candidate'], 'inputs': m['inputs'], 'reachability': m['reachability']}, indent=2))
