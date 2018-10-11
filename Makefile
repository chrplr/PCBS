INPUT_MDS := $(wildcard *.md)
INPUT_NB := $(wildcard *.ipynb)

OUTPUT_PDF = $(INPUT_MDS:.md=.pdf)
OUTPUT_HTML = $(INPUT_MDS:.md=.html) 
OUTPUT_NB = $(INPUT_NB:.ipynb=.html)

.PHONY: all html pdf clean

all: html pdf

pdf: $(OUTPUT_PDF)

%.pdf: %.md
	Rscript -e "rmarkdown::render('$<', output_file='$@', output_format='tufte::tufte_handout')"

html: $(OUTPUT_HTML)

%.html: %.md
	Rscript -e "rmarkdown::render('$<', output_file='$@', output_format='tufte::tufte_html')"

notebooks: $(OUTPUT_NB)

%.html: %.ipynb
	jupyter nbconvert $< --to html

clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF) $(OUTPUT_NB)
