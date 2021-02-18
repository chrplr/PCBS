# Time-stamp: <2021-02-17 21:27:27 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: lecture1.html lecture2.html lecture3.html solutions_ex3.html

%.html: %.md
	landslide -x tables --embed --relative -l table $< -d $@
