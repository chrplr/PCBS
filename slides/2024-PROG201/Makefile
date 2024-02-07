# Time-stamp: <2022-01-04 11:13:21 christophe@pallier.org>
# generate slides from markdown (see https://pypi.org/project/darkslide/)

#ALL: lecture1.html lecture2.html lecture3.html lecture4.html \
#	lecture5.html lecture6.html lecture7.html


INPUT_MDS := $(wildcard *.md)
OUTPUT_HTML = $(INPUT_MDS:.md=.html) 

.PHONY: all html clean

all: html

html: $(OUTPUT_HTML)

%.html: %.md
	darkslide -x tables --embed --relative -l table $< -d $@

clean:
	@rm -f $(OUTPUT_HTML) $(OUTPUT_PDF) $(OUTPUT_NB)
