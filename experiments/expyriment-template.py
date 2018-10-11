#! /usr/bin/env python
# Time-stamp: <2018-10-06 20:08:31 cp983411>

import expyriment

exp = expyriment.design.Experiment(name="First Experiment")
expyriment.control.initialize(exp)

block = expyriment.design.Block(name="A name for the block")
trial = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="Hello World")
stim.preload()
trial.add_stimulus(stim)
block.add_trial(trial)
exp.add_block(block)

expyriment.control.start()

for b in exp.blocks:
    for t in b.trials:
        for s in t.stimuli:
            s.present()
            exp.clock.wait(1000)

expyriment.control.end()
