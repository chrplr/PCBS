#!/usr/bin/env python
"""
skeleton for an expyriment script

See <https://docs.expyriment.org/Tutorial.html>

"""

from random import randint
import expyriment as xpy

# SETTINGS
xpy.control.defaults.window_mode = 1  # 0=FULLSCREEN
xpy.control.defaults.window_size = 1024, 768
xpy.control.set_develop_mode()

# DESIGN
exp = xpy.design.Experiment(name="My Experiment")

xpy.control.initialize(exp)

### insert here some code to generate the stimuli/trials/blocks

N_BLOCKS = 4

target_location = ['left', 'center', 'right']
nrep_by_location = 5

stimuli = { 'left':   xpy.stimuli.FixCross(position=(-300, 0)),
            'center': xpy.stimuli.FixCross(position=(0, 0)),
            'right':  xpy.stimuli.FixCross(position=(300, 0))
           }

for k, v in stimuli.items():
    v.preload()

bs = xpy.stimuli.BlankScreen()
bs.preload()

block = xpy.design.Block()
for loc in target_location:
    t = xpy.design.Trial()
    t.set_factor('location', loc)
    t.add_stimulus(stimuli[loc])
    block.add_trial(t, copies=nrep_by_location)

for _ in range(N_BLOCKS):
    block.shuffle_trials()
    exp.add_block(block)

exp.add_data_variable_names(['block', 'trial', 'location', 'resp', 'rt', 'correct'])

# RUN the experiment (present the stimuli and record responses)

xpy.control.start()

xpy.stimuli.TextScreen("", f"""
A cross will randomly appear either at the left, center or right of the screen.

If it is on the left, you must press 'F', in the center 'G', on the right 'H'.

Press a key to start the first block (1/{N_BLOCKS})""").present()
exp.keyboard.wait()

for iblock, block in enumerate(exp.blocks):
    good = 0  # keep track of good answers
    for itrial, trial in enumerate(block.trials):
        for stim in trial.stimuli:
            bs.present()
            exp.clock.wait(randint(1000, 2000))
            stim.present()
            resp, rt = exp.keyboard.wait_char('fgh', duration=1000)
            loc = trial.get_factor('location')
            resp_correct = (loc, resp) in [('left', 'f'), ('center', 'g'), ('right', 'h')]
            good += resp_correct
            exp.data.add([iblock, itrial, loc, resp, rt, resp_correct])

    proportion_correct = good / len(block.trials)
    xpy.stimuli.TextScreen("", f"""
    %correct responses = {100 * proportion_correct:3.1f}%
    
    Press any key to start next block ({iblock + 2}/{N_BLOCKS})""").present()
    exp.keyboard.wait()
    
xpy.control.end(goodbye_text="Thank you for participating!")
