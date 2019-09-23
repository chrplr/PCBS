#! /usr/bin/env python
# Time-stamp: <2019-09-19 17:08:26 cp983411>


""" Displays a vertical moving bar """


import expyriment

## Initialisation
exp = expyriment.design.Experiment(name="First Experiment")  # create an Experiment object

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

## Creating the stimulus

W, H = exp.screen.size
print(W, H)
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
print(timings)
