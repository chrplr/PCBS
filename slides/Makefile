# Time-stamp: <2021-02-23 22:17:43 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: lecture1.html lecture2.html lecture3.html lecture4.html solutions_ex3.html

%.html: %.md
	landslide -x tables --embed --relative -l table $< -d $@
