#! /usr/bin/env python
# Time-stamp: <2021-11-30 16:53:10 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
from expyriment import design, control, stimuli

N_TRIALS_PER_DIGIT = 50
MAX_RESPONSE_DELAY = 2000
TARGETS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * N_TRIALS_PER_DIGIT
EVEN_RESPONSE = 'f'
ODD_RESPONSE = 'j'

exp = design.Experiment(name="Parity Decision", text_size=40)
control.initialize(exp)

# prepare the stimuli
trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str(number))))

random.shuffle(trials)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible, whether it is even or odd.

    if it is even, press '{EVEN_RESPONSE}'

    if it is odd, press '{ODD_RESPONSE}'

    There will be {len(TARGETS)} trials in total.

    Press the space bar to start.""")

exp.add_data_variable_names(['number', 'oddity', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for number, number_stim in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    number_stim.present()
    key, rt = exp.keyboard.wait_char([EVEN_RESPONSE, ODD_RESPONSE], duration=MAX_RESPONSE_DELAY)
    exp.data.add([number, number % 2, key, rt])

control.end()
