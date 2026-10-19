#!/usr/bin/env python3
"""Compila figuras aisladas, conserva vistas y crea hoja de contacto.

Requiere LaTeX, Poppler, y Pillow para la hoja de contacto. Las fuentes
permanecen en imagenes/ y los archivos de trabajo se crean fuera del repositorio.
Uso: python metodologia_verificar_figuras.py [--skill RUTA] [--version v01]
"""
import argparse
from pathlib import Path
import subprocess
import tempfile
import shutil

ROOT=Path(__file__).resolve().parent.parent
NAMES=['metodologia_v2_flujo','metodologia_redes_sinteticas','metodologia_construccion_urbana','metodologia_red_mendoza','metodologia_v2_integracion','metodologia_v2_encoder','metodologia_controladores','metodologia_cambio_mascara','metodologia_v2_protocolo','metodologia_contraste_ac','metodologia_cohorte']
PREAMBLE=r'''\documentclass[tikz,border=4pt]{standalone}
\usepackage[T1]{fontenc}\usepackage[utf8]{inputenc}
\usepackage[spanish,es-noquoting,es-nodecimaldot]{babel}
\usepackage{setspace,graphicx,amssymb}
\usetikzlibrary{positioning,arrows.meta,calc,shapes.geometric}
\definecolor{colEntorno}{HTML}{A4C8F0}
\definecolor{colInterfaz}{HTML}{A8E6CF}
\definecolor{colAgente}{HTML}{FFAAA5}
\definecolor{catLilaSuave}{HTML}{CBAACB}
\definecolor{catMelocoton}{HTML}{FFD3B6}
\colorlet{colDatoPrimario}{colEntorno!80!black}
'''
def run(cmd,log):
 p=subprocess.run(list(map(str,cmd)),cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 log.write_text(p.stdout)
 if p.returncode:raise RuntimeError(str(cmd)+'\n'+p.stdout[-2200:])
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--skill',type=Path,default=Path('/home/juanm4/.codex/skills/tikz-diagrams'));ap.add_argument('--version',default='v01');a=ap.parse_args()
 out=ROOT/'imagenes/revision-metodologia';out.mkdir(exist_ok=True)
 run(['python3',a.skill/'scripts/check_tikz_safety.py',*[ROOT/'imagenes'/f'{n}.tex' for n in NAMES]],out/f'estatico-{a.version}.txt')
 with tempfile.TemporaryDirectory(prefix='metodologia-qa-') as tmp:
  tmp=Path(tmp)
  for n in NAMES:
   content=ROOT.joinpath('imagenes',n+'.tex').read_text()
   src=tmp/f'{n}-{a.version}.tex'
   if r'\documentclass' in content:
    source=content
   else:
    source=PREAMBLE+'\n\\graphicspath{{'+ROOT.as_posix()+'/}}\n\\input{'+str(ROOT/'imagenes/metodologia_estilos.tex')+'}\n\\begin{document}\n'+content+'\n\\end{document}\n'
   src.write_text(source)
   run(['python3',a.skill/'scripts/compile_render.py',src,'--engine','pdflatex','--dpi','150'],out/f'{n}-{a.version}.log')
   for ext in ('pdf','png'):shutil.copyfile(src.with_suffix('.'+ext),out/(n+'-'+a.version+'.'+ext))
   run(['magick',out/(n+'-'+a.version+'.png'),'-colorspace','Gray',out/(n+'-'+a.version+'-gris.png')],tmp/'gray.log')
   print(n,flush=True)
 from PIL import Image,ImageOps,ImageDraw
 for suffix in ('','-gris'):
  sheet=Image.new('RGB',(1800,4*510),'white');d=ImageDraw.Draw(sheet)
  for i,n in enumerate(NAMES):
   im=Image.open(out/(n+'-'+a.version+suffix+'.png')).convert('RGB');im.thumbnail((570,465))
   x=(i%3)*600+(600-im.width)//2;y=(i//3)*510+25
   sheet.paste(im,(x,y));d.text(((i%3)*600+10,(i//3)*510+5),f'{i+1:02d} {n.removeprefix("metodologia_")}',fill='black')
  sheet.save(out/('contacto-'+a.version+suffix+'.png'))
if __name__=='__main__':main()
