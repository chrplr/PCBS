#! /usr/bin/env python
# Time-stamp: <2021-03-24 10:59:19 christophe@pallier.org>
""" This is a simple reaction-time experiment.

At each trial, a brief sound is played and
the participant must press a key as quickly as possible.
"""

import random
from expyriment import design, control, stimuli

N_TRIALS = 50
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 2000

exp = design.Experiment(name="Visual Detection", text_size=40)
control.initialize(exp)

target = stimuli.Audio('click.wav')
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""Your task is to detect a sound

    Press a key as quickly as possible when you hear any sound. There will be {N_TRIALS} trials """)

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
