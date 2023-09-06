#! /usr/bin/env python
# Time-stamp: <2021-03-02 18:24:19 christophe@pallier.org>

""" Displays a vertical moving bar to check the absence (or presence) of tearing. """

from collections import Counter
from expyriment import design, control, stimuli


exp = design.Experiment(name="First Experiment")  
# control.open_gl = 0  # 0, 1, 2 or 3 


## Set develop mode. Comment for real experiment
# expyriment.control.set_develop_mode(on=True)

control.initialize(exp)

W, H = exp.screen.size
print(f"Screen size: {W}x{H}")


# Create a white vertical line
rect = stimuli.Rectangle((4, H), colour=(255, 255, 255))
rect.preload()

exp.add_data_variable_names(['skip', 'xpos', 'time', 'delta_time'])

control.start(subject_id=1, skip_ready_screen=True)

stimuli.TextScreen('Tearing test', """A moving vertical bar will be displayed. 

If the synchronization to vertical blank is set, 
and the computer is fast enough, 
the bar should not be brokeni""").present()
exp.keyboard.wait()

t0 = exp.clock.time
timings= []
for skip in [8, 16, 32]:
    xpos = 0
    rect.reposition((-W // 2, 0))
    while xpos < W:
        rect.move((skip, 0))
        rect.present(clear=True, update=True)
        t1 = exp.clock.time
        exp.data.add([skip, xpos, t1, t1 - t0])
        timings.append(t1 - t0)
        xpos += skip
        t0 = t1

control.end()


print('histogram of time differences between displays')
print(Counter(timings))
