#!/usr/bin/env python
# Time-stamp: <2022-05-12 07:39:59 christophe@pallier.org>
"""
Example of an expyriment script

A succession of trials where a cross will randomly appear either at the left or right of the screen.

If it is on the left, the participant must press 'F', 'J' if it is on the right.


"""

import random
import numpy as np
import expyriment as xpy

exp = xpy.design.Experiment(name="My Experiment")

xpy.control.initialize(exp)
# prepare the instructions/stimuli/trials/blocks


trials = ['left', 'right'] * 10
random.shuffle(trials)

center_fixation = xpy.stimuli.Circle(position=(0, 0), radius=5)

left_stim = xpy.stimuli.FixCross(position=(-300, 0))
left_resp = 'f'

right_stim = xpy.stimuli.FixCross(position=(300, 0))
right_resp = 'j'

instructions = f"""In a series of trials, a dot will appear. Look at it and do not move your eyes. Later a cross will appear, either on the left or on the right

If the cross appears on the left, press the '{left_resp.upper()}' key.

If the cross appears on the right, press the '{right_resp.upper()}' key.


You must respond as quickly as possible as you response-time is measured.

Rest you index fingers on the response key.


Press any key to start. 
"""


exp.add_data_variable_names(['location', 'resp_key', 'rt', 'correct'])

# RUN the experiment (present the stimuli and record responses)
xpy.control.start()

xpy.stimuli.TextScreen("Instructions", instructions).present()
exp.keyboard.wait()

good_responses, rts = 0, []
for side in trials:
    exp.screen.clear()
    center_fixation.present()
    exp.clock.wait(random.randint(1000, 2000))

    if side == 'left':
        left_stim.present()
    else:
        right_stim.present()

    resp_key, rt = exp.keyboard.wait_char([left_resp, right_resp],
                                          duration=1000)
    resp_correct = (side == 'left' and resp_key == left_resp) or \
                   (side == 'right' and resp_key == right_resp)
    good_responses += resp_correct
    if rt is not None:
        rts.append(rt)

    exp.data.add([side, resp_key, rt, resp_correct])

# display performance
proportion_correct = good_responses / len(trials)
median_rt = np.median(rts)
xpy.stimuli.TextLine(
    f"{100 * proportion_correct:3.1f}% correct. Median reaction-time: {median_rt:5.1f} Check full data in {exp.data.fullpath}").present()
exp.keyboard.wait()

xpy.control.end(goodbye_text=f"Thank you for participating! ")
