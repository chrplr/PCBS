#! /usr/bin/env python
# Time-stamp: <2021-03-04 13:36:14 christophe@pallier.org>

""" sound playback and generation. """

import numpy as np
from scipy.io import wavfile
import simpleaudio as sa # to play sound with play_buffer


DEFAULT_SAMPLE_RATE = 22050


def time_to_sample(t, sr=DEFAULT_SAMPLE_RATE):
    return int(t * sr)


def sample_to_time(s, sr=DEFAULT_SAMPLE_RATE):
    return float(s) / sr


def load_sound_as_array(wavfile_name):
    """ Read a wav file and returns (sample_rate, audio_data). """
    return wavfile.read(wavfile_name)


def write_array_as_sound(wavfile_name, audio_data, sr=DEFAULT_SAMPLE_RATE):
    """ save audiodata in a wav file """
    wavfile.write(wavfile_name, sr, audio_data)


def play_mono(audio_data, sr=DEFAULT_SAMPLE_RATE, normalize=True):
    audio = audio_data[:]
    if normalize:  # normalize to 16-bit range
        factor = 32767 / np.max(np.abs(audio))
        audio = np.multiply(audio, factor)

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 1, 2, sr)
    # wait for playback to finish before exiting
    play_obj.wait_done()


def play_stereo(audio_data, sr=DEFAULT_SAMPLE_RATE, normalize=True):
    audio = audio_data[:]
    if normalize:  # normalize to 16-bit range
        factor = 32767 / np.max(np.abs(audio))
        audio = np.multiply(audio, factor)

    # convert to 16-bit data
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio, 2, 2, sr)
    # wait for playback to finish before exiting
    play_obj.wait_done()


def silence(duration, sr=DEFAULT_SAMPLE_RATE):
    return np.zeros(time_to_sample(duration, sr), dtype=np.int16)


def tone(freq, phase, duration, amplitude=1.0, sr=DEFAULT_SAMPLE_RATE):
    t = np.linspace(0, float(duration), num = time_to_sample(duration, sr))
    return amplitude * np.sin(2 * np.pi * freq * t - phase)


def whitenoise(duration, amplitude=.1, sr=DEFAULT_SAMPLE_RATE):
    return amplitude * np.random.randn(duration * sr)


def pinknoise(nrows, ncols=16):
    """Generates pink noise using the Voss-McCartney algorithm
      (borrowed from https://www.dsprelated.com/showarticle/908.php).

    nrows: number of values to generate
    rcols: number of random sources to add

    returns: NumPy array
    """
    array = np.empty((nrows, ncols))
    array.fill(np.nan)
    array[0, :] = np.random.random(ncols)
    array[:, 0] = np.random.random(nrows)

    # the total number of changes is nrows
    n = nrows
    cols = np.random.geometric(0.5, n)
    cols[cols >= ncols] = 0
    rows = np.random.randint(nrows, size=n)
    array[rows, cols] = np.random.random(n)

    import pandas as pd
    df = pd.DataFrame(array)
    df.fillna(method='ffill', axis=0, inplace=True)
    total = df.sum(axis=1)

    return total.values

def mix_sound(target, mix, position, sr=DEFAULT_SAMPLE_RATE, replace=True):
    """ Adds 'mix' into 'target' at 'position'.  """
    samples = range(int(sr * position), int(sr * position) + len(mix))
    if (replace):
        target[samples] = mix
    else:
        target[samples] = target[samples] + mix


def multi_mix(target, mix, positions, sr=DEFAULT_SAMPLE_RATE, replace=True):
    """ Adds 'mix' into 'target' at 'positions' (a list of timepoints).  """
    for pos in positions:
        mix_sound(target, mix, pos, sr, replace)



if __name__ == '__main__':
    pitch = 440  # Hz
    duration = 1.0  # sec
    tone1 = tone(pitch, 0 , duration, amplitude = .5)
    tone2 = tone(pitch + 20, 0 , duration, amplitude = .25)
    tone3 = tone(pitch - 100 , 0 , duration, amplitude = .1)
    sil = silence(duration)

    play_mono(np.concatenate([tone1, sil, tone2, sil, tone3]))
    play_mono(tone1 + tone2)
