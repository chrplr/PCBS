#!/usr/bin/env python
"""
skeleton for an expyriment script

See <https://docs.expyriment.org/Tutorial.html>

"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

### insert here some code to generate the stimuli

NTRIALS = 10

stim1 

aTrial


control.start(skip_ready_screen=True)

stimuli.TextScreen('Instructions', """""")
exp.keyboard.wait()

### insert here some code to present the stimuli and record responses

for itrial in range(NTRIALS):
    stim

control.end()

