#! /usr/bin/env python
# Time-stamp: <2022-04-01 11:25:42 cp983411>
"""This is an example of a binary decision experiment.

At each trial, a number between 0 and 9 is presented at the center of the
screen and the participant must press the key 'F' if the number is even, 'J' if
it is odd. If s/he gives the wrong answer, s/he receives negative feedback (a buzzer sound is played).

"""

import random
from expyriment import design, control, stimuli

TARGETS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
N_TRIALS_PER_TARGET = 4
EVEN_RESPONSE_KEY = 'f'
ODD_RESPONSE_KEY = 'j'
MAX_RESPONSE_DELAY = 2000
BUZZER_SOUND = 'buzzer.wav'

exp = design.Experiment(name="Parity Decision", text_size=30)
control.initialize(exp)

## preparation
block = design.Block()
for number in (TARGETS * N_TRIALS_PER_TARGET):
    t = design.Trial()
    t.set_factor('number', number)
    t.set_factor('is_even', number % 2 == 0)
    t.add_stimulus(stimuli.TextLine(str(number)))
    block.add_trial(t)

block.shuffle_trials(max_repetitions=1)

cue = stimuli.FixCross(size=(50, 50), line_width=4)
blankscreen = stimuli.BlankScreen()
feedback = stimuli.Audio(BUZZER_SOUND)
instructions = stimuli.TextScreen(
    "Instructions",
    f"""When you'll see a number, your task to decide, as quickly as possible, whether it is even or odd.

    if it is even, press '{EVEN_RESPONSE_KEY}'

    if it is odd, press '{ODD_RESPONSE_KEY}'

    There will be {N_TRIALS_PER_TARGET * len(TARGETS)} trials in total.

    Press the space bar to start.""")

exp.add_data_variable_names(
    ['number', 'is_even', 'respkey', 'RT', 'is_correct'])

## run
control.start(skip_ready_screen=True)
instructions.present()
exp.keyboard.wait()

for trial in block.trials:
    blankscreen.present()
    exp.clock.wait(1000)
    cue.present()
    exp.clock.wait(500)
    trial.stimuli[0].present()
    key, rt = exp.keyboard.wait_char([EVEN_RESPONSE_KEY, ODD_RESPONSE_KEY],
                                     duration=MAX_RESPONSE_DELAY)

    is_correct_answer = (trial.get_factor('is_even') and key == EVEN_RESPONSE_KEY) or \
                        (not trial.get_factor('is_even') and key ==  ODD_RESPONSE_KEY)
    if not is_correct_answer:
        feedback.play()

    exp.data.add([
        trial.get_factor('number'),
        trial.get_factor('is_even'), key, rt, is_correct_answer
    ])

control.end()
