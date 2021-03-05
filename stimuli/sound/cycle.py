#! /usr/bin/env python3
# Time-stamp: <2021-02-23 20:57:32 christophe@pallier.org>

""" Loads a sound file and plays it 10 times in a loop (once per second)"""

import numpy as np
from sound_synth import load_sound_as_array, write_array_as_sound, play_mono

def create_loop(sample, TR, nrep):
    """ Repeats nrep times an audio sample with a period of TR 
    Args:
       - sample   : a sound file name
       - TR       : Repetition Time (period)
       - nrep     : number of repetitions

    Return:
       - sampling rate
       - a numpy array containing the samples of the loop
    """
    sr, beat = load_sound_as_array(sample)
    duration = len(beat) / sr
    assert duration < TR  # the sample must be shorter than the TR
    silence = np.zeros(int((TR - duration) * sr))

    loop = silence[:]
    for _ in range(nrep):
        loop = np.hstack((loop, beat, silence))

    return sr, loop


if __name__ == '__main__':
    sr, loop = create_loop('cymbal22050.wav', 1.0, 10)
    write_array_as_sound(loop, sr, 'loop.wav')
    play_mono(loop)

