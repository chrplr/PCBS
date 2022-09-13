#! /usr/bin/env python
# Time-stamp: <2021-11-16 15:36:47 christophe@pallier.org>
""" This is a simple reaction-time experiment.

At each trial, a cross is presented at the center of the screen and
the participant must press a key as quickly as possible.
"""

import random
from expyriment import design, control, stimuli

N_TRIALS = 20
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 2000

exp = design.Experiment(name="Visual Detection", text_size=40)
#control.set_develop_mode(on=True)
control.initialize(exp)

target = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()

instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a cross will appear at the center of screen.

    Your task is to press the SPACEBAR as quickly as possible when you see it (We measure your reaction-time).

    There will be {N_TRIALS} trials in total.

    Press the spacebar to start.""")

exp.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for i_trial in range(N_TRIALS):
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    target.present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial, waiting_time, key, rt])

control.end()
