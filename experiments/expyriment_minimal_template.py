#!/usr/bin/env python
"""
Minimal skeleton for an expyriment script

See <https://docs.expyriment.org/Tutorial.html>

"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

### insert here some code to generate the stimuli

control.start()

### insert here some code to present the stimuli and record responses

control.end()

