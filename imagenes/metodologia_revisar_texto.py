#!/usr/bin/env python3
"""Busca intersecciones entre palabras en PDFs de figuras, usando Poppler.

Es una comprobación textual, no un detector de líneas sobre texto. Las
intersecciones de índices matemáticos necesitan inspección visual.
"""
import argparse
import json
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


def inspect(path):
    result=subprocess.run(['pdftotext','-bbox',str(path),'-'],capture_output=True,text=True,check=True)
    root=ET.fromstring(result.stdout)
    pages=root.findall('.//{*}page')
    found=[]
    for pageno,page in enumerate(pages,1):
        words=[]
        for node in page.findall('.//{*}word'):
            box=[float(node.get(k)) for k in ('xMin','yMin','xMax','yMax')]
            words.append((''.join(node.itertext()),box))
        for i,(first,a) in enumerate(words):
            for second,b in words[i+1:]:
                w=min(a[2],b[2])-max(a[0],b[0]);h=min(a[3],b[3])-max(a[1],b[1])
                if w>.5 and h>1.5:
                    overlap=w*h
                    if overlap>.12*min((a[2]-a[0])*(a[3]-a[1]),(b[2]-b[0])*(b[3]-b[1])):
                        found.append({'page':pageno,'words':[first,second],'boxes':[a,b]})
    return {'file':str(path),'pages':len(pages),'width_cm':round(float(pages[0].get('width'))*2.54/72,2),'candidates':found}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--version',required=True);a=ap.parse_args()
    folder=Path(__file__).resolve().parent/'revision-metodologia'
    data=[inspect(p) for p in sorted(folder.glob(f'*-{a.version}.pdf'))]
    (folder/f'texto-{a.version}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    for item in data:
        print(Path(item['file']).name,item['width_cm'],'cm',len(item['candidates']),'candidatos')
        for c in item['candidates']:print(' ',c['words'])
if __name__=='__main__':main()
