#! /usr/bin/env python
# Time-stamp: <2021-11-16 11:35:22 christophe@pallier.org>
""" This is a simple reaction-time experiment.

At each trial, a cross is presented at the center of the screen and
the participant must press a key as quickly as possible.
"""

import random
from expyriment import design, control, stimuli


MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 2000

RADIUS = 30
COLORS = ((20, 20, 20), (60, 60, 60), (120, 120, 120), (255, 255, 255))
NCOPIES = 10

exp = design.Experiment(name="Visual Detection", text_size=40)
control.initialize(exp)

block = design.Block()
for ic, color in enumerate(COLORS):
    t = design.Trial()
    t.set_factor("grey-level", ic)
    t.add_stimulus(stimuli.Circle(RADIUS, color))
    block.add_trial(t, copies=NCOPIES)

block.shuffle_trials()

blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""From time to time, a cross will appear at the center of screen.

    Your task is to press a key as quickly as possible when you see it (We measure your reaction-time).

    There will be {NCOPIES * len(COLORS)} trials in total.

    Press the space bar to start.""")

exp.add_data_variable_names(['grey-level', 'wait', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for t in block.trials:
    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    t.stimuli[0].present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([t.get_factor("grey-level"), waiting_time, key, rt])

control.end()
