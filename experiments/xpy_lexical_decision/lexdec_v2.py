#! /usr/bin/env python
# Time-stamp: <2021-12-08 12:28:18 christophe@pallier.org>
"""This is a simple lexical decision experiment.

At each trial, an item is displayed and the participant must press the key 'f' if it is a word,
'j' if it is a non-word.
"""

import random
import pandas
from expyriment import design, control, stimuli

STIM_FILE = "stimuli.csv"  # a csv file with two columns: `item` (containing a word or a pseudoword) and `category` ('P' or 'W')
WORD_RESPONSE_KEY = 'f'
NONW_RESPONSE_KEY = 'j'
MAX_RESPONSE_DELAY = 2000

exp = design.Experiment(name="Lexical Decision", text_size=40)
control.initialize(exp)

# prepare the stimuli
materials = pandas.read_csv(STIM_FILE)
trials = [(row.category, row.item, stimuli.TextLine(row.item)) for row in materials.itertuples()]

random.shuffle(trials)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""When you'll see a stimulus, your task to decide, as quickly as possible, whether it is a word or not.

    if it is a word, press '{WORD_RESPONSE_KEY.upper()}'

    if it is a non-word, press '{NONW_RESPONSE_KEY.upper()}'

    Press the space bar to start.""")

exp.add_data_variable_names(['cat', 'word', 'respkey', 'RT'])

control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait_char(" ")

for category, item, stim in trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    stim.present()
    key, rt = exp.keyboard.wait_char([WORD_RESPONSE_KEY, NONW_RESPONSE_KEY],
                                     duration=MAX_RESPONSE_DELAY)
    exp.data.add([category, item, key, rt])

control.end()
