#! /usr/bin/env python
# Time-stamp: <2021-03-23 21:24:50 christophe@pallier.org>
"""A series of trials where a cross or a sound is presented and the participant must press a key as quickly as possible.
"""

import random
from expyriment import design, control, stimuli

NTRIALS = 20
ITI = 1000  # inter trial interval
MAX_RESPONSE_TIME = 2000
AUDIO_STIMULUS = 'click.wav'

exp = design.Experiment(name="AudioVisual Detection")
control.initialize(exp)

blankscreen = stimuli.BlankScreen()

visual_trial = design.Trial()
visual_trial.add_stimulus(stimuli.FixCross(size=(50, 50), line_width=4))

audio_trial = design.Trial()
audio_trial.add_stimulus(stimuli.Audio(AUDIO_STIMULUS))

visual_block = design.Block("visual")
for i in range(NTRIALS):
    visual_block.add_trial(visual_trial)
exp.add_block(visual_block)

audio_block = design.Block("audio")
for i in range(NTRIALS):
    audio_block.add_trial(audio_trial)
exp.add_block(audio_block)

audiovisual_block = design.Block("audiovisual")
for i in range(NTRIALS // 2):
    audiovisual_block.add_trial(audio_trial)
    audiovisual_block.add_trial(visual_trial)
audiovisual_block.shuffle_trials()
exp.add_block(audiovisual_block)

exp.add_data_variable_names(['block', 'key', 'rt'])

control.start(skip_ready_screen=True)

for b in exp.blocks:
    for t in b.trials:
        blankscreen.present()
        exp.clock.wait(ITI)
        exp.clock.wait(random.randint(1000, 2000))
        t.stimuli[0].present()
        key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_TIME)
        exp.data.add([b.name, key, rt])

control.end()
