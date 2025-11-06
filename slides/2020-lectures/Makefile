# Time-stamp: <2021-03-30 21:40:58 christophe@pallier.org>
# generate slides from markdown (see https://github.com/adamzap/landslide)

ALL: lecture1.html lecture2.html lecture3.html lecture4.html solutions_ex3.html \
	lecture5.html lecture5_exercises.html lecture5_exercises_with_solutions.html \
  lecture6.html lecture7.html

%.html: %.md
	landslide -x tables --embed --relative -l table $< -d $@
