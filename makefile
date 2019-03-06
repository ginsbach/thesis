thesis.pdf: thesis.tex
	max_print_line=1000 pdflatex --interaction=nonstopmode thesis.tex
	bibtex thesis
	max_print_line=1000 pdflatex --interaction=nonstopmode thesis.tex