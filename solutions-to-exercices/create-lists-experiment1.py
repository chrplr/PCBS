#! /usr/bin/env python3
# Time-stamp: <2018-11-02 13:11:04 cp983411>

"""Experiment 1 consists in a series of trials of two types, 'TypeA' or 'TypeB'.
   - Write a function which takes `N`, the total number of trials, and returns a list of labels 'TypeA' and 'typeB', in a random order (hint: use `random.shuffle`).
   - Create lists of trials for 20 participants. Each list must be saved in a text file with one column and one line per trial where each line contains a labelcorresponding the trial type).
"""

import random


def create_trials(conditions, ntrials):
    """ returns a list of length 'ntrials' (approximately) containing the conditions in random order """
    liste = conditions * (ntrials//len(conditions))
    random.shuffle(liste)
    return liste


def create_multiple_lists(conditions, ntrials, nparticipants):
    """ create 'nparticipants' text files containing ntrials of typeA or typeB. """
    for p in range(1, nparticipants + 1):
        trials = create_trials(conditions, ntrials)
        with open(f"subj{p:02d}.txt", 'w') as f:
            f.write('\n'.join(trials))


if __name__ == '__main__':
    create_multiple_lists(['TypeA', 'TypeB'], 100, 20)
