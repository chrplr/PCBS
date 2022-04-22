#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2021-11-16 13:23:44 christophe@pallier.org>

''' Display a white square for 100ms and play a 100ms tone simultanously, every half second 
in order to check timing with external equipment (oscilloscope, BlackBox ToolKit, ...) '''

from expyriment import design, control, stimuli, misc


PERIOD = 500  
TONE_DURATION = 100
SQUARE_DURATION = 100  # should be 6 frames with a video refresh rate at 60Hz

exp = design.Experiment(name="Cross-modal-timing-test")
#control.set_develop_mode(True)  # commented because we need fullscreen

control.defaults.open_gl = 2
control.defaults.audiosystem_buffer_size = 256
control.initialize(exp)

##

bs = stimuli.BlankScreen()
square_top = stimuli.Rectangle((400, 400), position=(0, 300))
tone = stimuli.Tone(TONE_DURATION, 440)

bs.preload()
square_top.preload()
tone.preload()


## 
control.start(skip_ready_screen=True)
clock = misc.Clock()

exp.screen.clear()
bs.present(update=True)
nframe = 0
t1 = clock.time
while clock.time - t1 <= 1000:
    bs.present(update=True)
    nframe += 1
FPS = nframe

frame = stimuli.Canvas((800, 800))
msg = stimuli.TextScreen("",f"""This script displays a white rectangle,
plays a tone and clears the screen, in a loop.

This permits to check the timing with some external equipment
(an oscilloscope, the Blackbox toolkit, etc.).

The current parameters are:

Tone duration = {TONE_DURATION} ms
Display duration = {SQUARE_DURATION} ms
Period = {PERIOD} ms
FPS = {FPS} Hz

Press any key for next screen (Later, to exit the program, just press 'Esc')."""
                ,
                position=(0, -200))
msg.plot(frame)
square_top.plot(frame)
frame.present()
exp.keyboard.wait()
stimuli.TextScreen("","Press a key to start").present(clear=True, update=True)
exp.keyboard.wait()

iperiod = 1
clock2 = misc.Clock()
while True:  # until the Esc key is pressed
    # wait until the next target period
    while (clock2.time) < (iperiod * PERIOD - 3):
       pass
    start_time = clock2.time + square_top.present(update=True)
    tone.present()

    while (clock2.time - start_time < SQUARE_DURATION - 3):
        pass
    end_time = clock2.time + bs.present(update=True)
    exp.data.add([iperiod, start_time, end_time])
    exp.keyboard.process_control_keys()
    iperiod += 1

control.end()

