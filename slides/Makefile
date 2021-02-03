# Time-stamp: <2021-02-03 08:05:58 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: presentation.html

%.html: %.md
	landslide -x tables --embed --relative $< -d $@
