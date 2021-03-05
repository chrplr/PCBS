#! /usr/bin/env python
# Time-stamp: <2021-03-04 16:44:55 christophe@pallier.org>

"""A series of trials where a cross is presented at the center of the screen and the participant must press a key as fast as possible. The statistics of reactions times are displayed at the end of the experiment.

"""

import random
import expyriment
from expyriment.stimuli import Audio, BlankScreen

exp = expyriment.design.Experiment(name="Visual Detection")
# expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)

NTRIALS = 50
MAXDURATION = 2000
target = Audio('click.wav')
blankscreen = BlankScreen()

exp.add_data_variable_names(['clock', 'trial', 'wait', 'respkey', 'RT'])

expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen(
    "Your task is to detect sound",
    "Press a key as quickly as possible when you hear the sound. There will be %d trials " % NTRIALS).present()
exp.keyboard.wait()
blankscreen.present()

clock = expyriment.misc.Clock()
reactiontimes = []
for i in range(NTRIALS):
    waitingtime = 2000 + int(1000 * random.expovariate(1))
    exp.clock.wait(waitingtime)
    time = clock.time
    target.present()
    key, rt = exp.keyboard.wait(duration=MAXDURATION)
    exp.data.add([time, i, waitingtime, key, rt])
    reactiontimes.append(rt)
    blankscreen.present()

expyriment.control.end()
