#! /usr/bin/env python
# Time-stamp: <2018-10-06 20:08:31 cp983411>

import random
import expyriment

NTRIALS = 10
ITI = 2000  # inter trial interval

## Initialisation
exp = expyriment.design.Experiment(name="First Experiment")  # create an Experiment object

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)


## Creating the stimuli and trials

instructions = expyriment.stimuli.TextScreen("Instructions", "You will hear a successions of tones; Press the 's' key as quickly as possible upon hearing a tone")

block = expyriment.design.Block(name="A name for the block")  # create a block (which will consists in a series of trials)

warning = expyriment.stimuli.TextLine(text="Prepare!")
warning.preload()
stim1 = expyriment.stimuli.Tone(500, 440, 22050,16, 1)
stim1.preload()
stim2 = expyriment.stimuli.Tone(500, 560, 22050,16, 1)
stim2.preload()

for i in range(NTRIALS):
    trial = expyriment.design.Trial()
    trial.add_stimulus(warning)
    if random.choice((1, 2)) == 1:
        trial.add_stimulus(stim1)
    else:
        trial.add_stimulus(stim2)
    block.add_trial(trial, random_position=True)

exp.add_block(block)

kb = exp.keyboard  # response device
exp.data_variable_names(['key', 'rt'])

## Run the experiment
expyriment.control.start()

for b in exp.blocks:
    for t in b.trials:
        exp.clock.wait(ITI)
        for s in t.stimuli:
            exp.clock.wait(1000)
            s.present()
        key, rt =kb.wait(keys='s', duration=2000)
        exp.data.add([key, rt])

expyriment.control.end()
