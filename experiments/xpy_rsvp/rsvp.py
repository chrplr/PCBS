#! /usr/bin/env python3
# Time-stamp: <2023-01-07 18:06:25 chistophe@pallier.org>

""" Display text, word by word, at the center of the screen.

    Usage: 

     rsvp file.tsv

    where file.tsv is a tab-separated-values files with three colums: word, onset, duration 
    (onset and duration are in seconds)
"""

import argparse
from queue import PriorityQueue
import pandas as pd
import expyriment
from expyriment import stimuli
from expyriment.misc import Clock

TEXT_FONT = "Inconsolata.ttf"  
TEXT_SIZE = 40
TEXT_COLOR = (255, 255,255)  # white
BACKGROUND_COLOR = (64, 64, 64)  # grey
WINDOW_SIZE = 1024, 768

######## command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('csv_files',
                    nargs='+',
                    action="append",
                    default=[])
parser.add_argument("--text-font",
                    type=str,
                    default=TEXT_FONT,
                    help="set the font for text stimuli")
parser.add_argument("--text-size",
                    type=int,
                    default=TEXT_SIZE,
                    help="set the vertical size of text stimuli")
parser.add_argument("--text-color",
                    nargs='+',
                    type=int,
                    default=TEXT_COLOR,
                    help="set the font for text stimuli")
parser.add_argument("--background-color",
                    nargs='+',
                    type=int,
                    default=BACKGROUND_COLOR,
                    help="set the background color")
parser.add_argument("--window-size",
                    nargs='+',
                    type=int,
                    default=WINDOW_SIZE,
                    help="in window mode, sets the window size")
args = parser.parse_args()
TEXT_SIZE = args.text_size
TEXT_COLOR = tuple(args.text_color)
TEXT_FONT = args.text_font
BACKGROUND_COLOR = tuple(args.background_color)
WINDOW_SIZE = tuple(args.window_size)

stimlist = pd.read_csv(args.csv_files[0][0], sep="\t", quoting=True, quotechar="*")


###############################
expyriment.control.defaults.window_mode=True
#expyriment.control.defaults.window_size = WINDOW_SIZE
#expyriment.design.defaults.experiment_background_colour = BACKGROUND_COLOR

exp = expyriment.design.Experiment(name="RSVP",
                                   background_colour=BACKGROUND_COLOR,
                                   foreground_colour=TEXT_COLOR,
                                   text_size=TEXT_SIZE,
                                   text_font=TEXT_FONT)
expyriment.control.initialize(exp)
exp._screen_colour = BACKGROUND_COLOR
kb = expyriment.io.Keyboard()


####################################################
# Prepare the queue of events 
bs = stimuli.BlankScreen(colour=BACKGROUND_COLOR)
events = PriorityQueue()
map_text_surface = dict()

for row in stimlist.itertuples():
    text = row.word
    onset = row.onset 
    duration = row.duration

    if text in map_text_surface.keys():
        stim = map_text_surface[text]
    else:
        stim = stimuli.TextLine(text, 
                                text_font=TEXT_FONT,
                                text_size=TEXT_SIZE,
                                text_colour=TEXT_COLOR,
                                background_colour=BACKGROUND_COLOR)
        map_text_surface[text] = stim

    events.put((onset * 1000, text, stim))
    events.put(((onset + duration) * 1000, "", bs))


#############################################################
# let's go
expyriment.control.start(subject_id=0)

a = Clock()
               
while not events.empty():
    onset, text, stim = events.get()
            
    while a.time < (onset - 10):
        a.wait(1)
        k = kb.check()
        if k is not None:
            exp.data.add([a.time, 'keypressed,{}'.format(k)])

    stim.present()
