#!/usr/bin/env python3
# Time-stamp: <2021-03-22 19:28:58 christophe@pallier.org>
"""
Card guessing game.

"""

import os
import os.path as op
import random
import pandas as pd
from generate_lists import generate_list_of_trials
from expyriment import stimuli, control, design

BACK_DISPLAY_DURATION = 1000
MAX_RESPONSE_TIME = 5000
RESPONSE_MAPPING = {'0': 'q', '1': 's', '2': 'd', '-1': 'n'}
response_keys = ''.join(RESPONSE_MAPPING.values())
INTER_TRIAL_TIME = 2000

W, H = 300, 458  # dimension of cards in pixels
gap = 100  # distance between borders of play cards
shift = W + gap  # displacement from center of left and right images

################################################################################
exp = design.Experiment(name="Cards", text_size=40)

control.initialize(exp)

#######################   Stimuli Preparation ##################################

# load all card images in a dictionary mapping card name to Picture stimuli
cards_directory = "cards_pics_small"

stim = {
    op.splitext(f)[0]: stimuli.Picture(op.join(cards_directory, f))
    for f in os.listdir(cards_directory)
}

# canvas mapped onto left, middle and right rectangles
C = [
    stimuli.Canvas((W, H), (-shift, 0)),
    stimuli.Canvas((W, H), (0, 0)),
    stimuli.Canvas((W, H), (+shift, 0))
]

# Create mapping 3 cards triplets -> surfaces
three_cards_surfaces = dict()


def create_3cards(card1, card2, card3):
    """ create a surface with the 3 cards """
    surf = stimuli.Canvas((3 * W + 2 * gap, H), (0, 0))
    stim[card1].plot(C[0])
    stim[card2].plot(C[1])
    stim[card3].plot(C[2])
    C[0].plot(surf)
    C[1].plot(surf)
    C[2].plot(surf)
    surf.preload()
    return surf


def get_3_cards_surface(card1, card2, card3, three_cards_surfaces):
    """ Create a surface with 3 cards and memoize it in three_cars_surfaces """
    key = (card1, card2, card3)
    if key in three_cards_surfaces:
        surf = three_cards_surfaces[key]
    else:
        surf = create_3cards(card1, card2, card3)
        three_cards_surfaces[key] = surf
    return surf


# Prepare trials

trials_desc = generate_list_of_trials()

print(trials_desc)

block = design.Block()  # nothing by a list of trials

for row in trials_desc.itertuples():
    t = design.Trial()

    t.set_factor("Condition", row.Condition)
    t.set_factor("back1", row.back1)
    t.set_factor("back2", row.back2)
    t.set_factor("back3", row.back3)
    t.set_factor("Card", row.card_to_turn)
    t.set_factor("Turn", int(row.position_to_turn))
    t.set_factor("Expected_response", row.expected_resp)

    backs = [row.back1, row.back2, row.back3]

    first_display = get_3_cards_surface(*backs, three_cards_surfaces)
    t.add_stimulus(first_display)

    fronts = backs[:]
    fronts[row.position_to_turn - 1] = row.card_to_turn
    second_display = get_3_cards_surface(*fronts, three_cards_surfaces)
    t.add_stimulus(second_display)

    block.add_trial(t)

negative_feedback_sound = stimuli.Audio('wrong-answer.ogg')


def give_feedback(t):
    negative_feedback_sound.play()
    exp.clock.wait(500)


def is_correct(actual_response, expected_response):
    """ check if the key "`resp` is the correct response for trial `t`. """
    print(expected_response, actual_response)
    expected_key = RESPONSE_MAPPING[expected_response]
    print(expected_key)
    return resp == expected_key


################################################################################
control.start(skip_ready_screen=True)

######################## Display Instructions ##################################

exp.data.add_variable_names(['condition', 'response', 'rt', 'is_correct'])

INSTRUCTIONS = stimuli.TextScreen(
    'Instructions', """
    Three cards are going to be used throughout the experiement:

         * Queen of Hearts   (red back)
         * Black Spade Ace   (blue back)
         * Red Diamond Ace   (blue back)

    Note that only the queen card has a red back while the two ace cards have blue backs.

    The experiment is a series of trials where the three cards are presented in a row.
    First their backs are presented, then one of the three cards is unmasked a second later.

    Your task is to identify the *middle* card as quickly as possible, when possible.
    You will indicate your response by pressing a key:

         Queen -> Press 'Q'
         Black Spade Ace -> Press 'S'
         Red Diamond Ace -> Press 'D'
         Dont know -> Press 'N'


    Note that  the answer will sometimes be obvious (e.g. when the card to guess has a blue back,
    because only the Queen has a blue back; or when the middle card is be displayed).
    Yet at other times, it will not be possible to provide an answer. Then press 'N'

         When you are Ready, press the SPACE BAR to start""")

INSTRUCTIONS.present(clear=True, update=True)
exp.keyboard.wait_char(' ')

exp.screen.clear()
exp.screen.update()
exp.clock.wait(2000)

#######################  Presenting trials  #################################

for trial in block.trials:
    # displays back of cards
    t0 = trial.stimuli[0].present(update=True, clear=True)
    exp.clock.wait(BACK_DISPLAY_DURATION)
    # turn one card
    t1 = trial.stimuli[1].present(update=True, clear=True)
    # record response
    resp, rt = exp.keyboard.wait_char(response_keys, MAX_RESPONSE_TIME)
    # if not is_correct(resp, t.get_factor("Expected_response")):
    #    give_feedback(t)
    exp.data.add([t.get_factor("Condition"), resp, rt, is_correct(resp, t)])
    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(INTER_TRIAL_TIME)

control.end()
