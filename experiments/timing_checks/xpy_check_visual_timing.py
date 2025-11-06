#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2021-11-16 13:23:44 christophe@pallier.org>

''' Display a white square for various durations in order to check timing with external equipment (oscilloscope, BlackBox ToolKit, ...) '''

from expyriment import design, control, stimuli, misc


exp = design.Experiment(name="visual-timing-test")
control.set_develop_mode(True)  # commented because we need fullscreen

#control.defaults.open_gl = 2

control.initialize(exp)
##

bs = stimuli.BlankScreen()
square_top = stimuli.Rectangle((400, 400), colour=(255, 255, 255), position=(0, 300))
square_top.preload()


## 
control.start(skip_ready_screen=True)
clock = misc.Clock()

# Evaluate framerate (FPS)
exp.screen.clear()
bs.present(update=True)
nframe = 0
t1 = clock.time
while clock.time - t1 <= 3000:
    bs.present(update=True)
    nframe += 1
FPS = nframe // 3
print(FPS)

frame = stimuli.Canvas((800, 800))
msg = stimuli.TextScreen("",f"""This script displays a white rectangle,
This permits to check the timing with some external equipment
(an oscilloscope, the Blackbox toolkit, etc.).

FPS = {FPS} Hz

Press any key for next screen (Later, to exit the program, just press 'Esc')."""
                ,
                position=(0, -200))
msg.plot(frame)

FRAME_DURATION_MS = 1000 / 60

square_top.plot(frame)
frame.present()
exp.keyboard.wait()
stimuli.TextScreen("","Press a key to start").present(clear=True, update=True)
exp.keyboard.wait()

PERIOD = 200
iperiod = 1
clock2 = misc.Clock()
while True:  # until the Esc key is pressed
    # wait until the next target period
    for N in [1, 2, 3, 4, 5]:
        while (clock2.time) < (iperiod * PERIOD - 3):   
            pass
        start_time = clock2.time + square_top.present(update=True)
        intended_duration = int((N - 1/2) * FRAME_DURATION_MS)
        while (clock2.time - start_time < intended_duration):
            pass
        end_time = clock2.time + bs.present(update=True)
        exp.data.add([iperiod, start_time, end_time])
        print(iperiod, start_time, N, intended_duration, end_time - start_time)
        exp.keyboard.process_control_keys()
        iperiod += 1

control.end()

