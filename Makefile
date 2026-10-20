# Compilación determinista de la tesina.
#
# Por qué no `latexmk -pdf`: al no existir main.aux, latexmk genera un main.aux
# provisional sin las líneas \citation de los capítulos y ejecuta BibTeX sobre
# ese archivo; el resultado es un main.bbl vacío y un PDF sin bibliografía.
# La receta de abajo es la verificada: la primera pasada de pdflatex siembra los
# .aux por capítulo, makeglossaries construye los índices de glosario y siglas,
# BibTeX lee las citas a través de los \@input de main.aux y las dos pasadas
# finales fijan las referencias cruzadas.

TEX      := pdflatex
TEXFLAGS := -synctex=1 -interaction=nonstopmode -halt-on-error

.PHONY: all pdf check clean distclean

all: pdf

pdf:
	$(TEX) $(TEXFLAGS) main.tex
	makeglossaries main
	-bibtex main
	@test -s main.bbl || { echo "ERROR: main.bbl quedó vacío (BibTeX no leyó las citas)."; exit 1; }
	$(TEX) $(TEXFLAGS) main.tex
	$(TEX) $(TEXFLAGS) main.tex

# Verificación del artefacto: debe quedar en cero todo lo que el jurado
# detectaría como referencia rota o caja desbordada.
check:
	@printf 'errores de LaTeX        : %s\n' "$$(grep -c '^! ' main.log)"
	@printf 'referencias indefinidas : %s\n' "$$(grep -c 'Reference .* undefined' main.log)"
	@printf 'citas indefinidas       : %s\n' "$$(grep -c 'Citation .* undefined' main.log)"
	@printf 'etiquetas redefinidas   : %s\n' "$$(grep -c 'multiply defined' main.log)"
	@printf 'Overfull hbox            : %s\n' "$$(grep -c 'Overfull' main.log)"
	@grep 'Output written on' main.log || true

clean:
	rm -f main.aux main.acn main.acr main.alg main.bbl main.blg main.fdb_latexmk \
	      main.fls main.glo main.glg main.gls main.ist main.log main.lof main.lot \
	      main.out main.toc main.acn

distclean: clean
	rm -f main.pdf
