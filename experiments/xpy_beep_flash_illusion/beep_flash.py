#!/usr/bin/env python
# Time-stamp: <2023-05-03 christophe@pallier.org>
"""
Embryo of a beep flash illusion script

Reference:

L. Shams, Y. Kamitani, S. Shimojo (2000).  What you see is what you hear
Nature, 408, p. 788, 10.1038/35048669
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Experiment")
control.set_develop_mode(on=True)  ## Set develop mode. Comment out for actual experiment

control.initialize(exp)

### insert here some code to generate the stimuli

tone = stimuli.Tone(duration=16, frequency=440)
circle = stimuli.Circle(radius=20, colour=(255, 255, 255))

tone.preload()
circle.preload()

control.start()


# a trials is described by a list* of (onset_time, stimulus)
stims = [(100, tone), (120, circle), (160, tone), (200, circle)]  # 



start = exp.clock.time

next_stim = stims[0]
stims = stims[1:]
need_to_clear_screen= False

while exp.clock.time - start < 1000:
    if need_to_clear_screen:
        exp.screen.clear()
        exp.screen.update()
        need_to_clear_screen= False
    if next_stim is not None:
        if exp.clock.time - start >= next_stim[0]:
            
            # try to determine the actual onset
            onset = exp.clock.time - start
            delta = next_stim[1].present()
            if delta != None:
                onset = onset + delta
            print(onset, next_stim[0], next_stim[1])

            if next_stim[1] == circle:
                need_to_clear_screen = True

            if len(stims) > 0:
                next_stim = stims[0]
                stims = stims[1:]
            else:
                next_stim = None   
                         

exp.clock.wait(1000)
control.end()

