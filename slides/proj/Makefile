# Time-stamp: <2022-03-23 07:03:24 christophe@pallier.org>
# generate slides from markdown (see https://pypi.org/project/darkslide/)


proj.html: proj.md
	darkslide -x tables --embed --relative -l table $< -d $@

clean_%.html: clean_%.md
	landslide -x tables --embed --relative -l table $< -d $@
