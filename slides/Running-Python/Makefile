# Time-stamp: <2015-09-14 19:44 christophe@pallier.org>

PANDOC_DOC_OPTS := --standalone -s -S --toc -c pandoc.css
PANDOC_SLIDES_OPTS := --standalone -s -S --toc -t slidy -V slidy-url=../css 


INPUT_MDS := $(wildcard *.md)

OUTPUT_HTML = $(INPUT_MDS:.md=-doc.html) $(INPUT_MDS:.md=-slides.html) 

.PHONY: all html clean

all: html 

html: $(OUTPUT_HTML)

%-slides.html: %.md
	pandoc $(PANDOC_SLIDES_OPTS) $< -o $@


%-doc.html: %.md
	pandoc $(PANDOC_DOC_OPTS) $< -o $@

clean:
	@rm -f $(OUTPUT_HTML)
