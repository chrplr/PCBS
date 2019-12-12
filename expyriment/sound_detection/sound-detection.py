#! /usr/bin/env python

""" Sound (pure tone) detection.

# Time-stamp: <2019-12-12 12:32:42 christophe@pallier.org>

The experiment consists in a series of trials in which a tone is played and the participant must press on a response key as quickly as possible. The tone can be high or low (50% proba)

This is basic example of a psychology experiment implemented with the expyriment module <https://www.expyriment.org/>
"""


import random
import expyriment

NTRIALS = 20
ITI = 2000  # inter trial interval

## Initialisation
exp = expyriment.design.Experiment(name="Simple Audio  Experiment")  # create an Experiment object

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

## Creating the stimuli and trials

instructions = expyriment.stimuli.TextScreen("Instructions",
                                             "You will hear a successions of tones; Press the 'J' key as quickly as possible upon hearing a tone\n\nPress the SPACEBAR to start")


tone1 = expyriment.stimuli.Tone(100, 440, 22050, 16, 1)
tone1.preload()

tone2 = expyriment.stimuli.Tone(100, 560, 22050, 16, 1)
tone2.preload()

fixcross = expyriment.stimuli.FixCross()
fixcross.preload()

# create a block (which will consists in a series of trials)
block = expyriment.design.Block(name="First and only block") 

# populate the bloc with trials
for _ in range(NTRIALS//2):
    trial = expyriment.design.Trial()
    trial.add_stimulus(tone1)
    trial.set_factor('tone', 1)
    block.add_trial(trial)


for _ in range(NTRIALS//2):
    trial = expyriment.design.Trial()
    trial.add_stimulus(tone2)
    trial.set_factor('tone', 2)
    block.add_trial(trial)

block.shuffle_trials()

exp.add_block(block) # add the block to the experiment

kb = exp.keyboard  # response device
exp.add_data_variable_names(['tone', 'waiting_time', 'key', 'rt'])

## Run the experiment
expyriment.control.start()

instructions.present()
kb.wait()

fixcross.present(update=True, clear=True)

for b in exp.blocks:
    for t in b.trials:
        exp.clock.wait(ITI)
        tone = t.stimuli[0]
        waiting_time = 1000 + random.random() * 1000 
        exp.clock.wait(waiting_time)
        tone.present()
        key, rt = kb.wait(keys='j', duration=2000)
        exp.data.add([t.get_factor('tone'), waiting_time, key, rt])

expyriment.control.end()
