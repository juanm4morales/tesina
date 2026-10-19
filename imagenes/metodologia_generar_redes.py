#!/usr/bin/env python3
"""Representaciones reproducibles de XML SUMO y anotaciones de captura urbana.

Uso: python3 imagenes/metodologia_generar_redes.py --proyecto RUTA
Los grosores sintéticos codifican carriles, no anchuras físicas. Los paneles esquematizan las conexiones entre nodos, con los sentidos y
carriles de los XML. Cada carril ocupa una franja diferenciada.
La captura urbana se conserva; el registro afín usa sus extremos y escala.
"""
import argparse
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--proyecto', type=Path, default=Path('/home/juanm4/Dev/marl-tlc'))
    args = parser.parse_args()
    sources = {}
    def load(relative):
        path = args.proyecto / relative
        sources[relative] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
        return ET.parse(path).getroot()
    commands = [r'\begingroup\setstretch{1}',r'\begin{tikzpicture}[met/base]']
    # Independent panel scales. Road widths are conventional, but each lane is
    # a distinct band; opposing directions occupy opposite sides of the axis.
    panels = [('3x1',8.8,4.4,3.1,8.6,3,20,40),
              ('3x3',6.6,6.6,0,0,9,48,96),
              ('4x4_H',6.6,6.6,8.4,0,16,71,166)]
    unit, median = .072, .025
    for scenario,w,h,ox,oy,n,ne,nl in panels:
        import math
        root = load(f'nets/{scenario}/{scenario}.net.xml')
        edges = [e for e in root.findall('edge') if e.get('function') != 'internal' and not e.get('id','').startswith(':')]
        junctions = {j.get('id'): (float(j.get('x')),float(j.get('y'))) for j in root.findall('junction') if j.get('type')!='internal'}
        tls = [j for j in root.findall('junction') if j.get('type','').startswith('traffic_light')]
        assert (len(tls),len(edges),sum(len(e.findall('lane')) for e in edges)) == (n,ne,nl)
        xmin,xmax=min(x for x,y in junctions.values()),max(x for x,y in junctions.values())
        ymin,ymax=min(y for x,y in junctions.values()),max(y for x,y in junctions.values())
        scale=min(w/(xmax-xmin),h/(ymax-ymin))
        def point(pt):
            x,y=pt
            return ox+(w-(xmax-xmin)*scale)/2+(x-xmin)*scale, oy+(h-(ymax-ymin)*scale)/2+(y-ymin)*scale
        def fmt(pt):return f'({pt[0]:.4f},{pt[1]:.4f})'
        # Carriageways: polygons, lane separators, then one direction arrow per
        # carriageway. Every endpoint and lane count comes directly from XML.
        for e in edges:
            start,end=point(junctions[e.get('from')]),point(junctions[e.get('to')])
            dx,dy=end[0]-start[0],end[1]-start[1];length=math.hypot(dx,dy)
            tx,ty=dx/length,dy/length;nx,ny=ty,-tx
            lanes=len(e.findall('lane'))
            def at(t,d):return (start[0]+t*dx+nx*d,start[1]+t*dy+ny*d)
            inner,outer=median/2,median/2+lanes*unit
            poly=[at(0,inner),at(1,inner),at(1,outer),at(0,outer)]
            commands.append(r'\path[fill=black!15,draw=black!50,line width=.28pt] '+' -- '.join(map(fmt,poly))+r' -- cycle;')
            for k in range(1,lanes):
                commands.append(r'\draw[black!45,line width=.22pt,dash pattern=on 2pt off 1.3pt] '+fmt(at(0,inner+k*unit))+' -- '+fmt(at(1,inner+k*unit))+';')
            offset=inner+unit/2
            # Keep arrowheads entirely inside one lane, away from junctions.
            mid=at(.35,offset)
            commands.append(r'\draw[-{Stealth[length=1.8mm,width=.6mm]},black!85,line width=.35pt] '+fmt((mid[0]-.13*tx,mid[1]-.13*ty))+' -- '+fmt((mid[0]+.13*tx,mid[1]+.13*ty))+';')
        # Mask lane separators inside crossings: road glyphs must not look
        # like grade-separated links passing through each other.
        for j in tls:
            here=junctions[j.get('id')]
            halfx,halfy=.09,.09
            for e in edges:
                if j.get('id') not in (e.get('from'),e.get('to')):continue
                other=junctions[e.get('to') if e.get('from')==j.get('id') else e.get('from')]
                breadth=median/2+len(e.findall('lane'))*unit+.01
                if abs(other[0]-here[0])<abs(other[1]-here[1]):halfx=max(halfx,breadth)
                else:halfy=max(halfy,breadth)
            x,y=point(here)
            commands.append(r'\path[fill=black!15] '+fmt((x-halfx,y-halfy))+' rectangle '+fmt((x+halfx,y+halfy))+';')
        for j in tls:
            x,y=point(junctions[j.get('id')])
            if scenario=='4x4_H' and j.get('id')=='C1':
                commands.append(r'\path[fill=colAgente!80!black,draw=white,line width=.5pt] '+fmt((x,y+.095))+' -- '+fmt((x+.095,y))+' -- '+fmt((x,y-.095))+' -- '+fmt((x-.095,y))+' -- cycle;')
            else:
                commands.append(r'\filldraw[fill=colAgente!75!black,draw=white,line width=.4pt] '+fmt((x,y))+' circle (.065cm);')
            if scenario=='3x1' or (scenario=='4x4_H' and j.get('id')=='C1'):
                commands.append(r'\node[anchor=north west,inner sep=0pt] at '+fmt((x+(.4 if scenario=='4x4_H' else .27),y-.28))+' {'+j.get('id')+'};')
        title={'3x1':r'(a) Corredor $3\times1$','3x3':r'(b) Cuadrícula $3\times3$','4x4_H':r'(c) Red heterogénea $4\times4\_H$'}[scenario]
        commands.append(r'\node[met/head] at '+fmt((ox+w/2,oy+h+.8))+' {'+title+'};')
        if scenario=='4x4_H':
            for col,x in zip('BCDE',[100,200,300,400]):
                px,py=point((x,500))
                commands.append(r'\node[anchor=south,inner sep=0pt] at '+fmt((px,py+.15))+' {'+col+'};')
            for row in range(1,5):
                px,py=point((0,row*100))
                commands.append(r'\node[anchor=east,inner sep=0pt] at '+fmt((px-.16,py))+' {'+str(row)+'};')
    commands += [r'\filldraw[fill=colAgente!75!black,draw=white] (3,-.8) circle (.065cm);',
                 r'\node[anchor=west,met/note] at (3.25,-.8) {Intersección controlada};',
                 r'\draw[-{Stealth[length=1.8mm,width=.6mm]},line width=.35pt] (9,-.8)--(9.6,-.8);',
                 r'\node[anchor=west,met/note] at (9.85,-.8) {Sentido de circulación};',
                 r'\end{tikzpicture}',r'\endgroup']
    OUT.joinpath('metodologia_redes_sinteticas.tex').write_text('\n'.join(commands)+'\n')
    root=load('nets/Mendoza/gran_mendoza2_fixed.net.xml')
    taz=load('nets/Mendoza/gran_mendoza2_fixed.taz.xml')
    assert taz.find("taz[@id='28']").get('edges')=='93904440#0'
    edge=root.find("edge[@id='93904440#0']")
    assert edge.get('name')=='José Vicente Zapata'
    # Capture registration: 0.59 pixels/m; bounds in SUMO coordinates.
    # Labels identify street corridors, not cadastral boundaries.
    def registered(pt):
        x,y=pt
        return ((27+(x-961.93)*.59)*10.8/962,(14+(y-639.2)*.59)*10.8/962)
    named={}
    for fragment in ('Las Heras','Manuel Belgrano','Colón','San Martín'):
        pts=[]
        for e in root.findall('edge'):
            if fragment not in e.get('name',''):continue
            pts.extend(registered(tuple(map(float,v.split(',')))) for v in e.find('lane').get('shape').split())
        if fragment in ('Las Heras','Colón'):named[fragment]=min(pts,key=lambda q:q[0])
        elif fragment=='San Martín':named[fragment]=max(pts,key=lambda q:q[0])
        else:named[fragment]=min(pts,key=lambda q:(q[0]-2.1)**2+(q[1]-4.8)**2)
    urban=r'''\begingroup\setstretch{1}
\begin{tikzpicture}[met/base,x=1.111111cm,y=1.111111cm]
\node[anchor=south west,inner sep=0] at (0,0) {\includegraphics[width=12cm,trim=330bp 0bp 377bp 0bp,clip]{imagenes/escenario_mendoza_sumo.png}};
\draw[met/arrow,line width=.8pt] (.55,9.7)--(.55,10.6) node[above]{N};
\draw[line width=.6pt] (.3,-.3)--(.9624,-.3);
\draw (.3,-.2)--(.3,-.4);\draw (.9624,-.2)--(.9624,-.4);
\node[met/note,anchor=north] at (.63,-.45) {100 m};
\draw[draw=colDatoPrimario,line width=1.2pt] (9.25,1.05) ellipse (.8 and .35);
\node[met/note,anchor=east] (lh) at (1.1,9.4) {Las Heras};
\node[met/note,anchor=east] (mb) at (1.1,4.8) {Manuel Belgrano};
\node[met/note,anchor=east] (co) at (-.25,2.7) {Colón};
\node[met/note,anchor=west] (sm) at (11.05,8) {San Martín};
\node[met/note,anchor=west,align=left] (vz) at (11.05,1.05) {Vicente Zapata\\TAZ 28};
\draw[colDatoPrimario,line width=.5pt] (10.05,1.05)--(vz.west);
'''
    for tag,name in (('lh','Las Heras'),('mb','Manuel Belgrano'),('co','Colón'),('sm','San Martín')):
        x,y=named[name]
        urban+=rf'\coordinate ({tag}street) at ({x:.4f},{y:.4f});'+'\n'
        side='east' if tag!='sm' else 'west'
        urban+=rf'\draw[colDatoPrimario,line width=.5pt] ({tag}.{side})--({tag}street);'+'\n'
        urban+=rf'\fill[colDatoPrimario] ({tag}street) circle (1.3pt);'+'\n'
    urban+=r'\end{tikzpicture}\endgroup'+'\n'
    OUT.joinpath('metodologia_red_mendoza.tex').write_text(urban)
    OUT.joinpath('metodologia_redes_procedencia.json').write_text(json.dumps({'generador':'imagenes/metodologia_generar_redes.py','fuentes':sources,'convenciones':{'geometria':'esquema entre centros de nodos; conectividad, sentidos y carriles del XML; sin giros internos','carril_cm':unit,'separacion_sentidos_cm':median,'escalas':'independientes por panel sintético','captura_urbana':'original conservada; corredores y TAZ 28; sin inserto redundante ni posición de cámara'}},ensure_ascii=False,indent=2)+'\n')
    print('Tres redes contrastadas: agentes, tramos y carriles; TAZ 28 y acceso verificados.')
if __name__=='__main__':
    main()
