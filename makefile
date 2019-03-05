thesis.pdf: thesis.tex
	pdflatex --output-directory=build thesis.tex
	cd build && bibtex thesis
	pdflatex --output-directory=build thesis.tex