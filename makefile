thesis.pdf: thesis.tex
	max_print_line=10000 pdflatex --interaction=nonstopmode thesis.tex | python latexfilter.py
	bibtex thesis
	max_print_line=10000 pdflatex --interaction=nonstopmode thesis.tex | python latexfilter.py