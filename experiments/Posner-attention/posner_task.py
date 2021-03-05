#! /usr/bin/env python
# Time-stamp: <2018-05-12 13:01:11 cp983411>
# License: Creative Commons Attribution-ShareAlike CC BY-SA


""" Implementation of Posner endogeneous attention cueing task (see https://en.wikipedia.org/wiki/Posner_cueing_task)
"""


import random
import numpy as np
import expyriment

GREY = (127, 127, 127)
BLACK = (0, 0, 0)

MAX_RESPONSE_DURATION = 2000

trials = [('congruent', 'left'), ('congruent', 'right')] * 40
trials += [('incongruent', 'left'), ('incongruent', 'right')] * 10
random.shuffle(trials)


exp = expyriment.design.Experiment(name="Posner-task",
                                   background_colour=GREY,
                                   foreground_colour=BLACK)
# expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)


cross = expyriment.stimuli.FixCross(size=(40, 40),
                                    colour=BLACK,
                                    line_width=6)
cross.preload()

blankscreen = expyriment.stimuli.BlankScreen(colour=GREY)

target_left = expyriment.stimuli.Picture("star.png", position=(-150, 0))
target_left.preload()

target_right = expyriment.stimuli.Picture("star.png", position=(+150, 0))
target_right.preload()

cue_left = expyriment.stimuli.Picture('left_arrow.png')
cue_left.preload()

cue_right = expyriment.stimuli.Picture('right_arrow.png')
cue_right.preload()


exp.add_data_variable_names(['congruency', 'side', 'respkey', 'RT'])
expyriment.control.start(skip_ready_screen = True)

expyriment.stimuli.TextScreen("Instructions",
    """Keep your eyes fixated on the central cross.

    A cue will appear followed by a star.
    Press the spacebar as quickly as possible when you see the *STAR*: your reaction time is measured.

    Note that the cue indicates the most probable location of the following star (left or right).
    You should direct your attention towards this side, but keeping your eyes fixating on the center.
    """).present()
exp.keyboard.wait()
blankscreen.present()
exp.clock.wait(1000)

for cond, side in trials:
    exp.clock.wait(1000)
    cross.present(clear=True, update=True)
    exp.clock.wait(1000)
    if ((cond == 'congruent') and (side == 'left')) or ((cond == 'incongruent') and (side =='right')):
        cue_left.present(update=True)
    else:
        cue_right.present(update=True)
    exp.clock.wait(2000)
    if (side == 'left'):
        target_left.present(update=True)
    else:
        target_right.present(update=True)
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DURATION)
    exp.data.add([cond, side, key, rt])
    blankscreen.present()

expyriment.control.end()
