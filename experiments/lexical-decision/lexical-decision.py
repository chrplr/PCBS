#! /usr/bin/env python
# Time-stamp: <2018-10-06 20:08:31 cp983411>

import random
import csv
import expyriment


WORD_RESP = expyriment.misc.constants.K_j
NONWORD_RESP = expyriment.misc.constants.K_f
MAX_RESP_TIME = 2500
ITI = 1500

exp = expyriment.design.Experiment(name="Lexical Decision Task") 

expyriment.control.initialize(exp)

trials = []

## Load the stimuli
with open('stimuli.csv', encoding="utf-8") as f:
    r = csv.reader(f)
    next(r)  # skip header line
    for row in r:
        cat, freq, item = row[0], row[1], row[2]
        trial = expyriment.design.Trial()
        trial.add_stimulus(expyriment.stimuli.TextLine(item))
        trial.set_factor("Category", cat)
        trial.set_factor("Frequency", freq)
        trial.set_factor("Item", item)
        trials.append(trial)

random.shuffle(trials)

exp.add_data_variable_names(['key', 'rt'])

## Run the experiment
expyriment.control.start()

expyriment.stimuli.TextScreen("Instructions", """You will see a series of written stimuli displayed at the center of the screen.

After each stimulus, your task is to press the right key ('J') if you think it is an existing word, the left key ('F') otherwise. Place now your index fingers on the keys 'F' and 'J'.

Press the spacebar when you are ready to start.""").present()

exp.keyboard.wait_char(' ')
exp.screen.clear()
exp.screen.update()

for t in trials:
    exp.clock.wait(ITI - t.stimuli[0].preload())
    t.stimuli[0].present()
    button, rt = exp.keyboard.wait([WORD_RESP, NONWORD_RESP],
                                   duration=MAX_RESP_TIME)
    exp.screen.clear()
    exp.screen.update()
    cat, freq = t.get_factor("Category"), t.get_factor("Frequency")
    ok = ((button == WORD_RESP) and (cat != 'PSEUDO')) or ((button == NONWORD_RESP) and (cat == 'PSEUDO'))
    exp.data.add([cat, freq, t.get_factor("Item"), button, ok, rt])

expyriment.control.end()
