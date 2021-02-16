# Time-stamp: <2021-02-16 13:36:04 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: lecture1.html lecture2.html lecture3.html

%.html: %.md
	landslide -x tables --embed --relative -l table $< -d $@
