#! /usr/bin/env python3
# Time-stamp: <2023-01-07 14:06:25 chistophe@pallier.org>

""" Display text, word by word, at the center of the screen.

    Usage: 

     rsvp file.csv

    where file.csv has three colums: word, onset, duration 
    (onset and duration are in seconds)
"""

TEXT_SIZE = 20
TEXT_COLOR = (255, 255,255)
TEXT_FONT = "Inconsolata.ttf"
BACKGROUND_COLOR = (64, 64, 64)


import os
from queue import PriorityQueue
import pandas as pd
import expyriment
from expyriment import stimuli
from expyriment.misc import Clock

########
STIMFILE = os.argv[1]


expyriment.control.defaults.window_mode=True
expyriment.control.defaults.window_size = 1024, 768
expyriment.design.defaults.experiment_background_colour = BACKGROUND_COLOR

exp = expyriment.design.Experiment(name="RSVP",
                                   background_colour=BACKGROUND_COLOR,
                                   foreground_colour=TEXT_COLOR,
                                   text_size=TEXT_SIZE,
                                   text_font=TEXT_FONT)


expyriment.control.initialize(exp)
exp._screen_colour = BACKGROUND_COLOR
kb = expyriment.io.Keyboard()

stimlist = pd.read_csv(STIMFILE)
events = PriorityQueue()
map_text_surface = dict()

bs = stimuli.BlankScreen(colour=BACKGROUND_COLOR)

for row in stimlist.itertuples():
    text = row.word
    onset = row.onset 
    stim = stimuli.TextLine(text, 
                                              text_font=TEXT_FONT,
                                              text_size=TEXT_SIZE,
                                              text_colour=TEXT_COLOR,
                                              background_colour=BACKGROUND_COLOR)
    map_text_surface[text] = stim
    events.put((onset * 1000, text, stim))
    events.put(((onset + row.duration) * 1000, "", bs))


#############################################################
expyriment.control.start()

# Present a fixation cross and wait for a key press
               
fs = stimuli.FixCross(size=(25, 25), line_width=3)
fs.present()
kb.wait_char('t')
               
# let's go
a = Clock()
               
while not events.empty():
    onset, text, stim = events.get()
    print(a.time, onset, text)
            
    while a.time < (onset - 10):
        a.wait(1)
        k = kb.check()
        if k is not None:
            exp.data.add([a.time, 'keypressed,{}'.format(k)])

    stim.present()
