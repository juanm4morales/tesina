#!/usr/bin/env python3
"""Genera diagramas desde XML SUMO, sin simulación ni dependencias externas.
Uso: python imagenes/metodologia_generar_redes.py [--proyecto RUTA]
Una polilínea por tramo externo; puntos de intersecciones semaforizadas.
El ingreso asociado al conteo se identifica con un recuadro y una flecha.
"""
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument('--proyecto', type=Path, default=Path('/home/juanm4/Dev/marl-tlc'))
args = parser.parse_args()
out = Path(__file__).resolve().parent
provenance = {}


def load(relative):
    path = args.proyecto / relative
    provenance[relative] = {
        'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'representacion': 'primera polilínea de carril por tramo externo; geometría SUMO sin giros internos',
    }
    root = ET.parse(path).getroot()
    edges = []
    for edge in root.findall('edge'):
        if edge.get('function') == 'internal' or edge.get('id', '').startswith(':'):
            continue
        lane = edge.find('lane')
        if lane is not None:
            pts = [tuple(map(float, v.split(','))) for v in lane.get('shape', '').split()]
            if pts:
                edges.append((edge.get('id'), pts))
    tls = [(float(j.get('x')), float(j.get('y'))) for j in root.findall('junction')
           if j.get('type', '').startswith('traffic_light')]
    return edges, tls


def draw(relative, width, height, offset=0.0, yoffset=0.0):
    edges, tls = load(relative)
    coords = [c for _, pts in edges for c in pts]
    xmin, ymin = min(x for x, y in coords), min(y for x, y in coords)
    xmax, ymax = max(x for x, y in coords), max(y for x, y in coords)
    scale = min(width / (xmax - xmin), height / (ymax - ymin))
    dx = (width - (xmax - xmin) * scale) / 2
    dy = (height - (ymax - ymin) * scale) / 2

    def pos(pt):
        return f'({offset + dx + (pt[0] - xmin) * scale:.4f},' \
               f'{yoffset + dy + (pt[1] - ymin) * scale:.4f})'

    commands = []
    is_mendoza = relative.startswith('nets/Mendoza/')
    road_width = '.82pt' if is_mendoza else '.95pt'
    for name, pts in edges:
        is_count_entry = is_mendoza and name == '93904440#0'
        style = (f'draw=colDatoPrimario,line width=2.0pt,line cap=round,line join=round'
                 if is_count_entry else
                 f'draw=black!62,line width={road_width},line cap=round,line join=round')
        commands.append('\\draw[' + style + '] ' + ' -- '.join(pos(c) for c in pts) + ';')
        if is_count_entry:
            commands.append('\\coordinate (ingreso) at ' + pos(pts[len(pts) // 2]) + ';')
    for pt in tls:
        commands.append('\\fill[colAgente!80!black] ' + pos(pt) + ' circle (1.7pt);')
    return '\n'.join(commands)


synthetic = ['\\begin{tikzpicture}[font=\\sffamily\\small]']
panels = [
    ('3x1', r'$3\times1$', 3, 9.2, 2.9, 2.8, 6.6),
    ('3x3', r'$3\times3$', 9, 7.0, 5.6, 0.0, 0.0),
    ('4x4_H', r'$4\times4\_H$', 16, 7.0, 5.6, 7.7, 0.0),
]
for scenario, title, n, width, height, xoffset, yoffset in panels:
    synthetic.append(draw(f'nets/{scenario}/{scenario}.net.xml', width, height,
                          xoffset, yoffset))
    synthetic.append(
        f'\\node[align=center] at ({xoffset + width / 2:.3f},'
        f'{yoffset + height + .7:.3f}) {{{title}}};'
    )
synthetic.append('\\end{tikzpicture}\n')
(out / 'metodologia_redes_sinteticas.tex').write_text('\n'.join(synthetic))

urban = [
    '\\begin{tikzpicture}[font=\\sffamily\\small]',
    draw('nets/Mendoza/gran_mendoza2_fixed.net.xml', 12.1, 8.0),
    r'''\node[draw=colDatoPrimario,fill=colEntorno!15,text width=4.0cm,align=center,rounded corners,inner sep=5pt] (conteo) at (13.6,1.5) {Ingreso estimado\\(cámara 169)};
\draw[-{Stealth},colDatoPrimario,dashed,line width=.85pt] (conteo.west) -- (ingreso);
\node[anchor=west,font=\sffamily\footnotesize] at (0,-.55) {\textcolor{colAgente!80!black}{$\bullet$} intersecciones semaforizadas};
\end{tikzpicture}''',
]
(out / 'metodologia_red_mendoza.tex').write_text('\n'.join(urban))
(out / 'metodologia_redes_procedencia.json').write_text(
    json.dumps({'generador': 'imagenes/metodologia_generar_redes.py', 'fuentes': provenance},
               ensure_ascii=False, indent=2) + '\n'
)
print('Redes generadas a partir de cuatro fuentes XML; hashes conservados.')
