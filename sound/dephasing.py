#! /usr/bin/env python3
# Time-stamp: <2021-03-03 08:45:57 christophe@pallier.org>

from time import sleep
import numpy as np
from sound_synth import load_sound_as_array, write_array_as_sound, play_mono, play_stereo, tone

sr, wave = load_sound_as_array('cymbal22050.wav')
# play_mono(wave, sr)


sr = 22050
wave = tone(440, 0, .1, 1000)
play_mono(wave, sr, normalize=False)
print(wave.shape)
channel1 = wave
shift = 10
channel2 = np.roll(wave, shift)
channel2[0:shift] = 0

stereo_wave = np.stack([channel1, channel2])
print(stereo_wave.shape)
sleep(1)
play_stereo(stereo_wave, 22050, normalize=False)
