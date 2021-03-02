#!/usr/bin/env python3
# Time-stamp: <2021-03-02 18:12:01 christophe@pallier.org>
"""
Minimal skeleton for an expyriment script  

See <https://docs.expyriment.org/Tutorial.html>

"""

import expyriment

exp = expyriment.design.Experiment(name="Experiment")

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

### insert here some code to generate the stimuli

expyriment.control.start()

### insert here some code to present the stimuli and record responses

expyriment.control.end()

