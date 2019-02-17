#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2019-02-09 09:52:16 christophe@pallier.org>

''' Display two white squares in alternance and play sounds simultanously, 
to check timing with external equipment (oscilloscope, BlackBox ToolKit, ...) '''

import expyriment

TONE_DURATION = 100
SQUARE_DURATION = 20 * (1000.0 / 60) - 2  # Twenty video refresh periods at 60Hz
SOA = 1000  


exp = expyriment.design.Experiment(name="Cross-modal-timing-test")
# expyriment.control.set_develop_mode(True)  # commented because we need fullscreen

expyriment.control.initialize(exp)

##

square_top = expyriment.stimuli.Rectangle((200, 200), position=(0, 300))
tone = expyriment.stimuli.Tone(TONE_DURATION, 440)


square_top.preload()
tone.preload()

frame = expyriment.stimuli.Canvas((800, 800))
msg = expyriment.stimuli.TextScreen("",f"""This script displays a white rectangle,
plays a tone and clears the screen, in a loop.

This permits to check the timing with some external equipment
(an oscilloscope, the Blackbox toolkit, etc.).

Currently, the parameters are:

Tone duration = {TONE_DURATION} ms
Display duration = {SQUARE_DURATION} ms
SOA = {SOA} ms

These can be changed in the source code.

Press any key to start (Later, to exit the program, just press 'Esc')."""
                ,
                position=(0,-200))
msg.plot(frame)
square_top.plot(frame)
#square_bottom.plot(frame)

## 
expyriment.control.start(skip_ready_screen=True)

exp.screen.clear()
frame.present()
exp.keyboard.wait()


clock = expyriment.misc.Clock()

period = 0

while True:  # until the Esc key is pressed
    period += 1
    while (clock.time < (SOA * period)):
        pass

    if (period % 3) == 0:
       exp.screen.clear()
       t = 0 # ?
    elif (period % 3) == 1:
        start_time = clock.time
        t = square_top.present(clear=False)
        start_time = start_time + t
        # t = square_top.present(clear=False)  # twice for double buffering
        while (clock.time - start_time) < SQUARE_DURATION:
            None
        exp.data.add([period, 'square', start_time, clock.time ])
        exp.screen.clear()
        exp.screen.update()

    elif (period %3) ==2:
        exp.data.add([period, 'tone', clock.time, 0 ])
        tone.play()
 
    exp.keyboard.process_control_keys()

expyriment.control.end()

