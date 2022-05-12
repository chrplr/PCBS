# Time-stamp: <2021-03-29 10:20:33 christophe@pallier.org>
""" """

from random import shuffle
import pandas as pd

card0 = ('QH', 'red_back')  # distinguished card
card1 = ('AS', 'blue_back')
card2 = ('AD', 'blue_back')


def generate_list_of_trials():
    """ Returns a table (DataFrame) defining trials for the "Mental Logic Cards" experiment.

    The columns are:
            "Condition"       : 'Inference', 'LackofI', 'NoInf1', 'NoInf2' or 'NoInf3'
            "back1"           : 'red_back' or 'blue_back'
            "back2"           : 'red_back' or 'blue_back'
            "back3"           : 'red_back' or 'blue_back'
            "position_to_turn": 1, 2 or 3
            "card_to_turn"    : 'QH', 'AS' or 'AD'
            "expected_resp"   : 0=card0; 1=card1, 2=card2, -1=impossible to decide
    """

    # Condition 1: Inference
    # Queen presented on one side, one Ace on the other side,
    # therefore the middle cards can be deduced

    cond1 = [
        ("Inference", (card0, card1, card2), 3, 1),
        ("Inference", (card0, card2, card1), 3, 2),
        ("Inference", (card1, card2, card0), 1, 2),
        ("Inference", (card2, card1, card0), 1, 1),
    ]

    # Condition 2: Lack of inference
    # Queen on side, Queen revealed

    cond2 = [
        ("LackOfI", (card0, card1, card2), 1, -1),
        ("LackOfI", (card0, card2, card1), 1, -1),
        ("LackOfI", (card1, card2, card0), 3, -1),
        ("LackOfI", (card2, card1, card0), 3, -1),
    ]

    # Condition 3: No inference
    # Queen in the middle, a random Ace shown

    cond3 = [
        ("NoInf1", (card1, card0, card2), 1, 0),
        ("NoInf1", (card1, card0, card2), 3, 0),
        ("NoInf1", (card2, card0, card1), 1, 0),
        ("NoInf1", (card2, card0, card1), 3, 0),
    ]

    # Condition 4: No inference Type2
    # Queen in the middle, Queen revealed

    cond4 = [
        ("NoInf2", (card1, card0, card2), 2, 0),
        ("NoInf2", (card2, card0, card1), 2, 0),
    ]

    # Condition 5: No inference Type3
    # Queen on side, middle card revealed

    cond5 = [
        ("NoInf3", (card0, card1, card2), 2, 1),
        ("NoInf3", (card0, card2, card1), 2, 2),
        ("NoInf3", (card2, card1, card0), 2, 1),
        ("NoInf3", (card1, card2, card0), 2, 2),
    ]

    trials = cond1 + cond2 + cond3 + cond4 + cond5

    df = pd.DataFrame(columns=[
        "Condition", "back1", "back2", "back3", "position_to_turn",
        "card_to_turn", "expected_resp"
    ])

    data = []
    for t in trials:
        t_info = {
            "Condition": t[0],
            "back1": t[1][0][1],
            "back2": t[1][1][1],
            "back3": t[1][2][1],
            "position_to_turn": t[2],
            "card_to_turn": t[1][t[2] - 1][0],
            "expected_resp": t[3]
        }
        data.append(t_info)

    shuffle(data)

    df = df.append(data, ignore_index=True)

    return df
