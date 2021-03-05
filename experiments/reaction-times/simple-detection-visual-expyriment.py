#! /usr/bin/env python
# Time-stamp: <2021-03-04 16:54:58 christophe@pallier.org>

""" This is a simple reaction time experiment.

At each trial, a cross is presented at the center of the screen and the participant must press a key as fast as possible.

"""

import random
import numpy as np
import expyriment
from  expyriment.stimuli import FixCross, BlankScreen

exp = expyriment.design.Experiment(name="Visual Detection")
#expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)

N_TRIALS = 50
MAX_RESPONSE_DELAY = 2000

target = FixCross(size=(25, 25), line_width=4)
blankscreen = BlankScreen()

exp.add_data_variable_names(['clock', 'trial', 'wait', 'respkey', 'RT'])
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen(
    "Your task is to detect a cross appearing at the center of screen",
    "Press a key as quickly as possible when you see the cross. There will be %d trials " % N_TRIALS).present()
exp.keyboard.wait()
blankscreen.present()

clock = expyriment.misc.Clock()

for i_trial in range(N_TRIALS):
    blankscreen.present()
    waiting_time = 1000 + random.randint(0, 1000)
    exp.clock.wait(waiting_time)
    target.present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial, waiting_time, key, rt])

expyriment.control.end()
