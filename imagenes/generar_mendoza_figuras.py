#!/usr/bin/env python3
"""Genera esquemas de red/TAZ y la curva histórica de vehículos pendientes."""
from pathlib import Path
import hashlib
import math
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
NET = Path('/home/juanm4/Dev/marl-tlc/nets/Mendoza/mendoza_220k_balance.net.xml')
TAZ = Path('/home/juanm4/Dev/marl-tlc/nets/Mendoza/mendoza_220k_balance.taz.xml')
RUNS = Path('/home/juanm4/Dev/marl-tlc/experiments/mendoza_scenario/results/mendoza_balance_multiseed_20261020/runs')
EXPECTED = {
    NET: '06222972799a5583f9d9846f69909e6a33cb01c06cc5e2f602c1511cf7671115',
    TAZ: 'b80859cb6f162601dd4b7dc8599144e0bf2608dd38a5bc1ca5cd2e1236702e0a',
}
SUMMARY_HASHES = {
    2026102001: 'ba65062022a65721a61c533660d2b863d16651228b19c2feab1b4855ef72001a',
    2026102002: '80dc2ee59d0258b3ad8dabfa2284df0c275dc62416ce5251aa7bbc668bf2f9d3',
    2026102003: 'e666915c5d7cd279863212fe98ce730582d1dcc7bb32f2c25882b9fb03562266',
}
SCALE = 0.007


def check_inputs():
    for path, digest in EXPECTED.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'XML cambió: {path}'
    net = ET.parse(NET).getroot()
    taz = ET.parse(TAZ).getroot()
    loc = net.find('location')
    assert loc is not None and '+proj=utm +zone=19' in loc.get('projParameter', '')
    edges = {e.get('id'): e for e in net.findall('edge')}
    junctions = {j.get('id'): j for j in net.findall('junction')}
    controllers = sorted({x.get('id') for x in net.findall('tlLogic')})
    assert len(edges) == 255 and sum(len(e.findall('lane')) for e in edges.values()) == 554
    assert len(net.findall('connection')) == 744 and len(controllers) == 74
    assert set(controllers) <= set(junctions)
    zones = sorted(taz.findall('taz'), key=lambda z: int(z.get('id')))
    assert len(zones) == 37 and {int(z.get('id')) for z in zones} == set(range(39)) - {6, 9}
    assert all(ref.get('id') in edges for zone in zones for ref in zone if ref.tag in ('tazSource','tazSink'))
    return net, edges, junctions, controllers, zones


def shape_points(element):
    shape = element.get('shape')
    if not shape:
        lane = element.find('lane')
        shape = lane.get('shape') if lane is not None else ''
    return [tuple(map(float, pair.split(','))) for pair in shape.split()]


def fmt(x):
    return f'{x:.2f}'


def xy(point, bounds):
    xmin, ymin, _, _ = bounds
    return (SCALE * (point[0] - xmin), SCALE * (point[1] - ymin))


def write_map(net, edges, junctions, controllers, zones, taz_map=False):
    b = list(map(float, net.find('location').get('convBoundary').split(',')))
    # Equal x/y scale preserves the metric proportions of the UTM projection.
    lines = [r'\begingroup\setstretch{1}',
             r'\begin{tikzpicture}[x=1cm,y=1cm,',
             r'  road/.style={draw=black!48,line width=.32pt,line cap=round,line join=round},',
             r'  avenue/.style={draw=colDatoPrimario,line width=1.05pt,line cap=round,line join=round},',
             r'  tls/.style={circle,fill=red!75!black,draw=white,line width=.35pt,minimum size=2.1pt,inner sep=0pt},',
             r'  access/.style={circle,fill=white,draw=colDatoPrimario,line width=.7pt,minimum size=3.4pt,inner sep=0pt},',
             r'  maplabel/.style={font=\sffamily\fontsize{6.5}{7.2}\selectfont,text=black!90},',
              r'  smalllabel/.style={font=\sffamily\fontsize{6}{6.5}\selectfont,text=black!85}]']
    for edge in edges.values():
        pts = shape_points(edge)
        if len(pts) < 2:
            continue
        style = 'avenue' if edge.get('name') in {
            'Avenida General San Martín', 'Avenida Juan Gregorio de Las Heras',
            'Avenida Emilio Civit', 'José Vicente Zapata'} else 'road'
        coords = ' -- '.join('(%s,%s)' % tuple(fmt(v) for v in xy(p,b)) for p in pts)
        lines.append(r'\draw[%s] %s;' % (style, coords))
    if taz_map:
        placed_labels=[]
        for zone in zones:
            zid = int(zone.get('id'))
            refs=[]
            for tag in ('tazSource','tazSink'):
                for ref in zone.findall(tag):
                    eid=ref.get('id')
                    edge=edges.get(eid)
                    if edge is not None:
                        pts=shape_points(edge)
                        p=pts[0] if tag=='tazSource' else pts[-1]
                        refs.append((p,tag))
            if not refs:
                continue
            # If an ID has both entry and exit references, use both marks but one label.
            marks=[xy(p,b) for p,_ in refs]
            for x,y in marks:
                if zid == 28:
                    lines.append(r'\node[circle,fill=colDatoPrimario,draw=white,line width=.4pt,minimum size=4pt,inner sep=0pt] at (%s,%s) {};' % (fmt(x),fmt(y)))
                else:
                    lines.append(r'\node[access] at (%s,%s) {};' % (fmt(x),fmt(y)))
            x,y=marks[0]
            # Spread adjacent IDs just enough to keep every short tag readable.
            offsets=[(sx*radius,sy*radius*.72) for radius in (.13,.22,.31)
                     for sx,sy in ((1,1),(-1,1),(1,-1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0))]
            def clearance(offset):
                lx,ly=x+offset[0],y+offset[1]
                return min([((lx-px)/.20)**2+((ly-py)/.12)**2 for px,py in placed_labels] or [9])
            dx,dy=max(offsets,key=clearance)
            placed_labels.append((x+dx,y+dy))
            label=rf'\bfseries {zid}' if zid==28 else str(zid)
            lines.append(r'\draw[black!45,line width=.25pt] (%s,%s)--(%s,%s);' % (fmt(x),fmt(y),fmt(x+dx*.78),fmt(y+dy*.78)))
            lines.append(r'\node[smalllabel,anchor=center,fill=white,inner sep=.35pt] at (%s,%s) {%s};' % (fmt(x+dx),fmt(y+dy),label))
    else:
        for ident in controllers:
            j=junctions[ident]
            x,y=xy((float(j.get('x')),float(j.get('y'))),b)
            lines.append(r'\node[tls] at (%s,%s) {};' % (fmt(x),fmt(y)))
        # Street names are attached to actual named avenue segments, not hand-placed points.
        names=[('Avenida Juan Gregorio de Las Heras', 'Las Heras', .22, .14),
               ('Avenida Emilio Civit', 'Emilio Civit', .15, -.20),
               ('Avenida General San Martín', 'San Martín', .18, .12),
               ('José Vicente Zapata', 'José V. Zapata', .04, .16)]
        for exact,label,dx,dy in names:
            candidates=[e for e in edges.values() if e.get('name')==exact]
            if candidates:
                if label == 'José V. Zapata':
                    edge=next((e for e in candidates if e.get('id')=='93904440#1'),candidates[0])
                else:
                    edge=max(candidates,key=lambda e: sum(math.dist(a,c) for a,c in zip(shape_points(e),shape_points(e)[1:])))
                pts=shape_points(edge)
                mid=pts[len(pts)//2]
                x,y=xy(mid,b)
                lines.append(r'\node[maplabel,fill=white,inner sep=1pt] at (%s,%s) {%s};' % (fmt(x+dx),fmt(y+dy),label))
        z28=next(z for z in zones if z.get('id')=='28')
        edge=edges[z28.find('tazSource').get('id')]
        ax,ay=xy(shape_points(edge)[0],b)
        lines.append(r'\node[rectangle,fill=white,draw=colDatoPrimario,line width=.8pt,minimum size=3.4pt,inner sep=0pt] at (%s,%s) {};' % (fmt(ax),fmt(ay)))
        lines.append(r'\node[maplabel,fill=white,inner sep=1pt,anchor=east] at (%s,%s) {TAZ 28};' % (fmt(ax-.08),fmt(ay+.10)))
    lines += [r'\end{tikzpicture}']
    if not taz_map:
        lines.insert(1, r'\noindent\begin{minipage}{\linewidth}\centering')
        # title/legend and truthful north/scale indicators
        lines[-1:-1] = [r'\node[maplabel,anchor=west] at (0,%.2f) {N};' % (SCALE*(b[3]-b[1])+.10),
                       r'\draw[-{Stealth[length=1.6mm]},line width=.6pt] (.12,%.2f)--(.12,%.2f);' % (SCALE*(b[3]-b[1])-.05,SCALE*(b[3]-b[1])+.08),
                       r'\draw[line width=.7pt] (.15,-.18)--(%.2f,-.18);' % (SCALE*100+.15),
                       r'\draw[line width=.5pt] (.15,-.13)--(.15,-.23) (%.2f,-.13)--(%.2f,-.23);' % (SCALE*100+.15,SCALE*100+.15),
                       r'\node[maplabel,anchor=north] at (%.2f,-.25) {100 m};' % (SCALE*50+.15),
                       r'\node[maplabel,anchor=west] at (%.2f,%.2f) {\tikz[baseline=-.5ex]\fill[red!75!black] (0,0) circle (1pt);  Nodos con programa fijo (74)};' % (SCALE*(b[2]-b[0])+.12,SCALE*(b[3]-b[1])*.75),
                        r'\node[maplabel,anchor=west] at (%.2f,%.2f) {\tikz[baseline=-.5ex]\draw[draw=colDatoPrimario,line width=1pt] (0,0)--(.25,0);  Avenidas de referencia};' % (SCALE*(b[2]-b[0])+.12,SCALE*(b[3]-b[1])*.69),
                        r'\node[maplabel,anchor=west] at (%.2f,%.2f) {\tikz[baseline=-.5ex]\draw[draw=colDatoPrimario,line width=.8pt] (0,0) rectangle (2pt,2pt);  Acceso TAZ 28; cámara 169 externa};' % (SCALE*(b[2]-b[0])+.12,SCALE*(b[3]-b[1])*.63),
                       ]
    else:
        width=SCALE*(b[2]-b[0]); height=SCALE*(b[3]-b[1])
        lines.insert(1, r'\noindent\begin{minipage}{\linewidth}\centering')
        lines[-1:-1] = [r'\node[maplabel,anchor=west] at (%.2f,%.2f) {\tikz[baseline=-.5ex]\draw[draw=colDatoPrimario,line width=.7pt] (0,0) circle (1.5pt);  Tramo asociado a zona};' % (width+.12,height*.75),
                        r'\node[maplabel,anchor=west] at (%.2f,%.2f) {\tikz[baseline=-.5ex]\fill[colDatoPrimario] (0,0) circle (1.5pt);  TAZ 28};' % (width+.12,height*.69),
                        r'\node[maplabel,anchor=west,align=left,text width=2.5cm] at (%.2f,%.2f) {Las marcas señalan tramos asociados, no límites territoriales.};' % (width+.12,height*.55)]
        # Metric scale and north arrow refer directly to the projected coordinates.
        lines[-1:-1] = [r'\node[maplabel,anchor=west] at (0,%.2f) {N};' % (height+.10),
                        r'\draw[-{Stealth[length=1.6mm]},line width=.6pt] (.12,%.2f)--(.12,%.2f);' % (height-.05,height+.08),
                        r'\draw[line width=.7pt] (.15,-.18)--(%.2f,-.18);' % (SCALE*100+.15),
                        r'\draw[line width=.5pt] (.15,-.13)--(.15,-.23) (%.2f,-.13)--(%.2f,-.23);' % (SCALE*100+.15,SCALE*100+.15),
                        r'\node[maplabel,anchor=north] at (%.2f,-.25) {100 m};' % (SCALE*50+.15)]
    lines += [r'\end{minipage}\endgroup']
    target=HERE/('metodologia_mendoza_balance_taz.tex' if taz_map else 'metodologia_mendoza_balance_dominio.tex')
    target.write_text('\n'.join(lines)+'\n')


def write_backlog():
    series=[]
    for seed,style in zip((2026102001,2026102002,2026102003),('solid','dashed','dotted')):
        path=RUNS/f'seed{seed}_12h/summary.xml'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == SUMMARY_HASHES[seed], f'Summary cambió: {path}'
        steps=ET.parse(path).getroot().findall('.//step')
        assert len(steps)==43200 and steps[0].get('time')=='0.00' and steps[-1].get('time')=='43199.00'
        assert all(float(step.get('time')) == i for i,step in enumerate(steps))
        sampled=[s for s in steps if int(float(s.get('time')))%300==0]
        if sampled[-1] is not steps[-1]: sampled.append(steps[-1])
        assert sampled[-1].get('waiting') == {'2026102001':'21913','2026102002':'21939','2026102003':'22216'}[str(seed)]
        series.append((seed,style,[(float(s.get('time'))/3600,int(s.get('waiting'))) for s in sampled]))
    W,H=640,350; L,R,T,B=70,18,35,58; pw,ph=W-L-R,H-T-B
    xmax,ymax=12,26000
    X=lambda x:L+x/xmax*pw
    Y=lambda y:T+(ymax-y)/ymax*ph
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<rect width="100%" height="100%" fill="white"/>',
         '<style>text{font-family:DejaVu Sans, sans-serif;fill:#222} .grid{stroke:#ddd;stroke-width:1}</style>',
         '<text x="320" y="20" text-anchor="middle" font-size="14" font-weight="600">Vehículos pendientes de ingreso</text>',
         '<text x="260" y="43" text-anchor="middle" font-size="8">Tres ejecuciones; muestreo cada 300 s y cierre incluido</text>']
    for y in range(0,ymax+1,5000):
        py=Y(y); out += [f'<line class="grid" x1="{L}" y1="{py:.1f}" x2="{W-R}" y2="{py:.1f}"/>',f'<text x="{L-8}" y="{py+4:.1f}" text-anchor="end" font-size="10">{y:,}</text>']
    for h in range(13):
        px=X(h); out += [f'<line class="grid" x1="{px:.1f}" y1="{T}" x2="{px:.1f}" y2="{H-B}"/>',f'<text x="{px:.1f}" y="{H-B+16}" text-anchor="middle" font-size="9">{6+h:02d}:00</text>']
    out += [f'<line x1="{L}" y1="{H-B}" x2="{W-R}" y2="{H-B}" stroke="#333"/>',f'<line x1="{L}" y1="{T}" x2="{L}" y2="{H-B}" stroke="#333"/>',
            f'<text x="{(L+W-R)/2}" y="{H-6}" text-anchor="middle" font-size="10">Hora del escenario (06:00–18:00)</text>',
            f'<text transform="translate(18 {(T+H-B)/2}) rotate(-90)" text-anchor="middle" font-size="10">Vehículos pendientes (Summary: waiting)</text>']
    colors=['#285f88','#ad4b38','#34745c']
    for idx,(seed,style,points) in enumerate(series):
        dash={'solid':'','dashed':' stroke-dasharray="8 5"','dotted':' stroke-dasharray="2 4"'}[style]
        d=' '.join(('M' if i==0 else 'L')+f'{X(x):.1f},{Y(y):.1f}' for i,(x,y) in enumerate(points))
        out.append(f'<path d="{d}" fill="none" stroke="{colors[idx]}" stroke-width="2.1"{dash}/>')
        ly=48+idx*20; out += [f'<line x1="435" y1="{ly}" x2="463" y2="{ly}" stroke="{colors[idx]}" stroke-width="2.0"{dash}/>',f'<text x="470" y="{ly+4}" font-size="9">Semilla {seed}</text>']
    out += ['</svg>']
    svg=HERE/'mendoza220k_balance_pendientes.svg'; svg.write_text('\n'.join(out))
    import subprocess
    subprocess.run(['rsvg-convert','-f','pdf','-o',str(HERE/'mendoza220k_balance_pendientes.pdf'),str(svg)],check=True)
    svg.unlink()


if __name__ == '__main__':
    parsed=check_inputs()
    write_map(*parsed,taz_map=False)
    write_map(*parsed,taz_map=True)
    write_backlog()
