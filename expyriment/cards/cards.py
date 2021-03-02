#!/usr/bin/env python3
# Time-stamp: <2021-03-02 20:55:41 christophe@pallier.org>
"""
Minimal skeleton for an expyriment script

See <https://docs.expyriment.org/Tutorial.html>

"""

import os
import os.path as op
import random
import pandas as pd
import expyriment


LIST = 'trials.csv'  # description of the trials (3 cards, and which to turn)
cards_directory = "images"
W, H  = 691, 1056  # dimension of cards in pixels
gap = 60  # distance between borders of play cards
shift = W + gap  # displacement from center of left and right images


exp = expyriment.design.Experiment(name="Cards")
## Set develop mode. Comment for real experiment
# expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

# load all card images in a dictionary mapping card name to Picture stimuli
stim = dict()
for f in os.listdir(cards_directory):
    card_name = os.path.splitext(f)[0]
    stim[card_name] = expyriment.stimuli.Picture(op.join(cards_directory, f))

# reads the description of trials and prepare the stimuli 
trials_desc = pd.read_csv(LIST, sep='\t')

block = expyriment.design.Block()
for i in trials_desc.itertuples():
    t = expyriment.design.Trial()
    b = expyriment.stimuli.BlankScreen()
    t.add_stimulus(stim[i.C1])
    t.add_stimulus(stim[i.C2])
    t.add_stimulus(stim[i.C3])
    t.set_factor("Turn", int(i.T))
    block.add_trial(t)



# canvas mapped onto left, middle and right rectangles
C = [ expyriment.stimuli.Canvas((W, H), (- shift, 0)),
      expyriment.stimuli.Canvas((W, H), (0, 0)),
      expyriment.stimuli.Canvas((W, H), (+ shift, 0))
    ]

# Three backgrounds, depending on the position of the red back card 
back1 = expyriment.stimuli.BlankScreen()
stim['red_back'].plot(C[0])
stim['blue_back'].plot(C[1])
stim['blue_back'].plot(C[2])
C[0].plot(back1)
C[1].plot(back1)
C[2].plot(back1)
back1.preload()

back2 = expyriment.stimuli.BlankScreen()
stim['blue_back'].plot(C[0])
stim['red_back'].plot(C[1])
stim['blue_back'].plot(C[2])
C[0].plot(back2)
C[1].plot(back2)
C[2].plot(back2)
back2.preload()

back3 = expyriment.stimuli.BlankScreen()
stim['blue_back'].plot(C[0])
stim['blue_back'].plot(C[1])
stim['red_back'].plot(C[2])
C[0].plot(back3)
C[1].plot(back3)
C[2].plot(back3)
back3.preload()

backgrounds = [back1, back2, back3]

b = expyriment.stimuli.BlankScreen()

expyriment.control.start()

for trial in block.trials:
    # selects a random background
    i = random.choice(range(3))
    backgrounds[i].present(update=True, clear=True)

    backgrounds[i].plot(b)

    pos = trial.get_factor("Turn") - 1
    trial.stimuli[pos].plot(C[pos])
    C[pos].plot(b)

    exp.clock.wait(1000)
    b.present(update=True, clear=True)
    exp.clock.wait(2000)
    # trial.stimuli[0].present()
    # trial.stimuli[1].present()
    # trial.stimuli[2].present()

    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(2000)

expyriment.control.end()

