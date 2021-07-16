#! /usr/bin/env python
# Time-stamp: <2021-04-05 07:55:39 christophe@pallier.org>

""" Display Kanisza illusory square

(see https://openi.nlm.nih.gov/detailedresult?img=PMC4211395_fnhum-08-00854-g0001&req=4 )

"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Kanisza square", background_colour=(127, 127, 127))
control.set_develop_mode(on=True)  # Comment out for full screen experiment
control.initialize(exp)
control.start(skip_ready_screen=True)

width, height = 200, 200
left = - width // 2
right = width // 2
top = height // 2
bottom = - height // 2

stimuli.Circle(50, (0,0,0), 0, (left, top)).present(clear=True, update=False)
stimuli.Circle(50, (0,0,0), 0, (right, top)).present(clear=False, update=False)
stimuli.Circle(50, (0,0,0), 0, (left, bottom)).present(clear=False, update=False)
stimuli.Circle(50, (0,0,0), 0, (right, bottom)).present(clear=False, update=False)
stimuli.Rectangle((width, height), (127,127,127), 0, None, None, (0, 0)).present(clear=False, update=True)

exp.screen.save('kanisza-squares2.png')
exp.keyboard.wait()

control.end()

