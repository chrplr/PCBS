# Time-stamp: <2015-09-10 20:29 christophe@pallier.org>

#PANDOC_OPTS := --standalone -S --toc -t slidy -V slidy-url=../css 
PANDOC_OPTS :=  -t slidy -V slidy-url=../css --toc  --standalone 

INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=-sol.html) $(INPUT_MDS:.md=-nosol.html)

OUTPUT_PDF = $(INPUT_MDS:.md=-sol.pdf) $(INPUT_MDS:.md=-nosol.pdf)

.PHONY: all html clean pdf

all: html pdf

%-nosol.md: %.md
	gpp  $< > $@

%-sol.md: %.md
	gpp -D ANSWERS=1 $< > $@

html: $(OUTPUT_HTML)


%.html: %.md
	pandoc $(PANDOC_OPTS) $< -o $@

pdf: $(OUTPUT_PDF)

%.pdf: %.md
	pandoc $< -o $@


clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF)
