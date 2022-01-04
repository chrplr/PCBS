# Time-stamp: <2022-01-04 11:13:21 christophe@pallier.org>
# generate slides from markdown (see https://pypi.org/project/darkslide/)

ALL: lecture1.html lecture2.html lecture3.html lecture4.html \
	lecture5.html lecture6.html lecture7.html

%.html: %.md
	darkslide -x tables --embed --relative -l table $< -d $@
