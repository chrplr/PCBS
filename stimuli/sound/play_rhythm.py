#! /usr/bin/env python3
# Time-stamp: <2019-03-09 14:53:26 christophe@pallier.org>

""" Loads a sound file and plays it 10 times in a loop (once per second)"""

import numpy as np
import scipy.io.wavfile  # for scipy.io.wavfile.read
import simpleaudio  # to play sound


SAMPLE = 'cymbal22050.wav'


def load_sound_as_array(filename):
    [sample_rate, audio_data] = scipy.io.wavfile.read(filename)
    return [sample_rate, audio_data]

def write_array_as_sound(nparray, sample_rate, filename):
    audio = nparray[:]
    # convert to 16-bit data
    audio = audio.astype(np.int16)
    scipy.io.wavfile.write(filename, sample_rate, audio)


def play_mono(nparray, sample_rate=22050, normalize=True):
    audio = nparray[:]
    if normalize:  # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))

    # convert to 16-bit data
    audio = audio.astype(np.int16)
    play_obj = simpleaudio.play_buffer(audio, 1, 2, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()


sr, beat = load_sound_as_array(SAMPLE)
duration = len(beat) / sr
silence = np.zeros(int((1.0 - duration) * sr))

loop = silence[:]
for i in range(10):
    loop = np.hstack((loop, beat, silence))

write_array_as_sound(loop, sr, 'loop.wav')
play_mono(loop)

