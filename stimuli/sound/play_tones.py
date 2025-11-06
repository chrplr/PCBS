#! /usr/bin/env python3
# Time-stamp: <2019-03-09 14:17:52 christophe@pallier.org>

""" synthesize simples sounds """

import time
import numpy as np
import simpleaudio as sa

# calculate note frequencies
A_freq = 440
Csh_freq = A_freq * 2 ** (4 / 12)
E_freq = A_freq * 2 ** (7 / 12)

# get timesteps for each sample, T is note duration in seconds
SAMPLE_RATE = 44100
DURATION = 0.25
t = np.linspace(start=0.0,
                stop=DURATION,
                num=int(DURATION * SAMPLE_RATE))

# generate sine wave notes
A_note = np.sin(A_freq * t * 2 * np.pi)
Csh_note = np.sin(Csh_freq * t * 2 * np.pi)
E_note = np.sin(E_freq * t * 2 * np.pi)
silence = np.zeros(int(DURATION * SAMPLE_RATE))

# concatenate notes
audio = np.hstack((A_note, silence, Csh_note, silence, E_note))
# normalize to 16-bit range
audio *= 32767 / np.max(np.abs(audio))
# convert to 16-bit data
audio = audio.astype(np.int16)

# start playback
play_obj = sa.play_buffer(audio, 1, 2, SAMPLE_RATE)

# wait for playback to finish before exiting
play_obj.wait_done()

