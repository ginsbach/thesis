thesis.pdf: thesis.tex
	bibtex thesis
	max_print_line=10000 pdflatex --interaction=nonstopmode thesis.tex | python latexfilter.py