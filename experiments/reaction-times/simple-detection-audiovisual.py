#! /usr/bin/env python
# Time-stamp: <2018-05-12 13:01:11 cp983411>


"""A series of trials where a cross or a sound is presented and the participant must press a key as fast as possible. 
"""

import expyriment
from expyriment.stimuli import FixCross, Audio, BlankScreen

exp = expyriment.design.Experiment(name="Visual Detection")
# expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)

NTRIALS = 10
assert NTRIALS % 2 == 0  # should be an even number
ITI = 1000

# Prepare stimuli, trials anb blocks
target_visual = FixCross(size=(25, 25), line_width=4)
target_audio = Audio('click.wav')

trial_visual = expyriment.design.Trial()
trial_visual.add_stimulus(target_visual)
trial_audio = expyriment.design.Trial()
trial_audio.add_stimulus(target_audio)

blankscreen = BlankScreen()

block_visual = expyriment.design.Block()
for i in range(NTRIALS):
    block_visual.add_trial(trial_visual)

block_audio = expyriment.design.Block()
for i in range(NTRIALS):
    block_audio.add_trial(trial_audio)

block_audiovisual = expyriment.design.Block()
for i in range(NTRIALS//2):
    block_audiovisual.add_trial(trial_audio)
    block_audiovisual.add_trial(trial_visual)

exp.add_block(block_visual)
exp.add_block(block_audio)
exp.add_block(block_audiovisual)

exp.add_data_variable_names(['key', 'rt'])

# Run the experiment
expyriment.control.start(skip_ready_screen=True)

for b in exp.blocks:
    for t in b.trials:
        t.stimuli[0].present()
        key, rt = exp.keyboard.wait(duration=2000)
        blankscreen.present()
        exp.data.add([key, rt])
        exp.clock.wait(ITI)

expyriment.control.end()
