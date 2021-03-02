#! /usr/bin/env python
# Time-stamp: <2021-03-02 18:24:19 christophe@pallier.org>

""" Displays a vertical moving bar """

from numpy import diff, histogram
import expyriment

## Initialisation
exp = expyriment.design.Experiment(name="First Experiment")  # create an Experiment object

## Set develop mode. Comment for real experiment
# expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

## Creating the stimulus

W, H = exp.screen.size

rect = expyriment.stimuli.Rectangle((5, H), colour=(255, 255, 255))
rect.preload()

## Run the experiment
expyriment.control.start()

timings = []
for skip in [2, 4, 8, 16]:
    xpos = 0
    rect.reposition((-W // 2, 0))
    while xpos < W:
        rect.move((skip, 0))
        rect.present(clear=True, update=True)
        timings.append(exp.clock.time)
        xpos += skip

expyriment.control.end()

print('histogram of time differences between displays')
n, val = histogram(diff(timings))
for i in n:
    print(f'{i:>5}', end='')
print()
for v in val:
    print(f'{v:>5}', end='')
print()
