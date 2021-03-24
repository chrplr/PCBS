#! /usr/bin/env python
# Time-stamp: <2021-03-24 08:15:54 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
from expyriment import design, control, stimuli

MAX_RESPONSE_DELAY = 2000
TARGETS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 5
EVEN_RESPONSE = 'f'
ODD_RESPONSE = 'j'

exp = design.Experiment(name="Parity Decision", text_size=40)
control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible, whether it is even or odd.

    if it is even, press '{EVEN_RESPONSE}'

    if it is odd, press '{ODD_RESPONSE}'

    There will be {len(TARGETS)} trials in total.

    Press the space bar to start.""")

# prepare the stimuli
trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str(number))))


exp.add_data_variable_names(['number', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    t[1].present()
    key, rt = exp.keyboard.wait(EVEN_RESPONSE + ODD_RESPONSE, duration=MAX_RESPONSE_DELAY)
    exp.data.add([t[0],  key, rt])

control.end()
