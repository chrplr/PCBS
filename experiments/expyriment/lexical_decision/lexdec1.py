#! /usr/bin/env python
# Time-stamp: <2021-11-30 16:11:06 christophe@pallier.org>
"""This is a simple decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'f' if the number is even, 'j' if
it is odd.

"""

import random
import pandas
from expyriment import design, control, stimuli, misc

MAX_RESPONSE_DELAY = 2000
WORD_RESPONSE = misc.constants.K_f
NONW_RESPONSE = misc.constants.K_j

#words = ['bonjour', 'chien', 'president']
#pseudos = ['lopadol', 'mirance', 'clapour' ]

stims = pandas.read_csv('stimuli.csv')

exp = design.Experiment(name="Parity Decision", text_size=40)
control.initialize(exp)

cue = stimuli.FixCross(size=(50, 50), line_width=4)

blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a stimulus, your task to decide, as quickly as possible, whether it is a word or not.

    if it is a word, press '{chr(WORD_RESPONSE)}'

    if it is odd, press '{chr(NONW_RESPONSE)}'

    Press the space bar to start.""")

# prepare the stimuli
trials = []
for t in range(6):
    trials.append((stims["category"][t],
                   stims["stimulus"][t],
                   stimuli.TextLine(stims["stimulus"][t])))

random.shuffle(trials)

exp.add_data_variable_names(['cat', 'word', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    t[2].present()
    key, rt = exp.keyboard.wait([WORD_RESPONSE, NONW_RESPONSE], duration=MAX_RESPONSE_DELAY)
    exp.data.add([t[0], t[1], key, rt])

control.end()
