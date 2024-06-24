#! /usr/bin/env python3
# Time-stamp: <2019-03-09 14:17:52 christophe@pallier.org>

""" synthesize simples sounds """

import numpy as np
import simpleaudio as sa


def create_pure_tone(frequency, amplitude, duration, sample_rate):
    t = np.linspace(start=0.0, stop=duration, num=int(duration * sample_rate))
    return amplitude * np.sin(frequency * t * 2 * np.pi)


def create_silence(duration, sample_rate):
    n_samples = int(duration * sample_rate)
    return np.zeros(n_samples)


def apply_sinusoidal_ramp_to_sound(audio_data, sample_rate, ramp_duration):
    ramp_length = int(ramp_duration * sample_rate)
    ramp = np.sin(np.linspace(-np.pi / 2, np.pi / 2, ramp_length))

    for i in range(audio_data.shape[1]):  # Loop through channels
        audio_data[:, i][:ramp_length] *= ramp
        audio_data[:, i][-ramp_length:] *= ramp[::-1]

    return audio_data




if __name__== '__main__':


    SAMPLE_RATE = 44100
    DURATION = 0.25

    # notes' frequencies
    A_freq = 440
    Csh_freq = A_freq * 2 ** (4 / 12)
    E_freq = A_freq * 2 ** (7 / 12)


    # generate sine wave notes
    A_note = create_pure_tone(A_freq, 1, DURATION, SAMPLE_RATE)
    Csh_note = create_pure_tone(Csh_freq, 1, DURATION, SAMPLE_RATE)
    E_note = create_pure_tone(E_freq, 1, DURATION, SAMPLE_RATE)

    silence = create_silence(DURATION, SAMPLE_RATE)

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
