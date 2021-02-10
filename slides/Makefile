# Time-stamp: <2021-02-10 08:19:06 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: lecture1.html lecture2.html

%.html: %.md
	landslide -x tables --embed --relative $< -d $@
