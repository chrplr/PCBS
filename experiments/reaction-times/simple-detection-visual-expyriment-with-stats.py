#! /usr/bin/env python
# Time-stamp: <2018-05-12 13:01:11 cp983411>

"""A series of trials where a cross is presented at the center of the screen and the participant must press a key as fast as possible. The statistics of reactions times are displayed at the end of the experiment.

"""

import random
import numpy as np

import expyriment

from  expyriment.stimuli import FixCross, BlankScreen

exp = expyriment.design.Experiment(name="Visual Detection")
#expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)

NTRIALS = 50
MAXDURATION = 2000

target = FixCross(size=(25, 25), line_width=4)
blankscreen = BlankScreen()

exp.add_data_variable_names(['clock', 'trial', 'wait', 'respkey', 'RT'])

expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen(
    "Your task is to detect a cross appearing at the center of screen",
    "Press a key as quickly as possible when you see the cross. There will be %d trials " % NTRIALS).present()
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

x = np.array(reactiontimes)
x = x[x < MAXDURATION]  # supress the No RT trials
print('================ RTs ==================')
print(" n = {}\n min = {}\n max = {}\n median = {}\n mean = {}".format(x.shape[0],
      np.min(x), np.max(x), np.median(x), np.mean(x)))
