#! /usr/bin/env python3
# Time-stamp: <2018-11-02 13:11:04 cp983411>

"""Experiment 2 consists in a series of trials where a written stimulus is presented: the stimulus can be a French word or pseudowords, or an English words or pseudowords (the task is a lexical decision, that is, the participants must decide as quickly as possible if the stimulus is an existing word or not). Create text files listing 100 trials in random order."""

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
            for t in trials:
                f.write(','.join(t) + '\n')


if __name__ == '__main__':
    create_multiple_lists([('English', 'Word'),
                           ('English', 'Pseudo'),
                           ('French', 'Word'),
                           ('French', 'Pseudo')], 100, 20)
