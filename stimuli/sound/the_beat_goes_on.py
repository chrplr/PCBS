#! /usr/bin/env python
# Time-stamp: <2021-02-23 20:39:01 christophe@pallier.org>

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile  # for scipy.io.wavfile.read
import simpleaudio  # to play sound


def play_mono(nparray, sample_rate=22050, normalize=True):
    audio = nparray[:]
    if normalize:  # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))

    # convert to 16-bit data
    audio = audio.astype(np.int16)
    play_obj = simpleaudio.play_buffer(audio, 1, 2, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()


def play_stereo(nparray, sample_rate=22050, normalize=True):
    audio = nparray[:]
    if normalize:  # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
    # convert to 16-bit data
    audio = nparray.astype(np.int16)
    play_obj = simpleaudio.play_buffer(audio, 2, 2, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()


def tone(freq, phase, duration, amplitude=0.1, sample_rate=22050):
    t = np.linspace(0, duration, num = int(duration * sample_rate))
    return amplitude * np.sin(2 * np.pi * freq * t - phase)


def whitenoise(duration, amplitude=0.1, sample_rate=22050):
    return amplitude * np.random.randn(duration * sample_rate)

def pinknoise(nrows, ncols=16):
    """Generates pink noise using the Voss-McCartney algorithm (orrowed from https://www.dsprelated.com/showarticle/908.php).

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


def load_sound_as_array(filename):
    [sample_rate, audio_data] = scipy.io.wavfile.read(filename)
    return [sample_rate, audio_data]

def write_array_as_sound(nparray, sample_rate, filename):
     scipy.io.wavfile.write(filename, sample_rate, np_array)

def mix_sound(target, mix, position, sample_rate=22050, replace=True):
    samples = range(int(sample_rate * position), int(sample_rate * position) + len(mix))
    if (replace):
        target[samples] = mix
    else:
        target[samples] = target[samples] + mix


def multi_mix(target, mix, positions, sample_rate=22050, replace=True):
    for pos in positions:
        mix_sound(target, mix, pos, sample_rate, replace)



if __name__ == '__main__':
    sample_rate = 22050

    # preparation of stimuli
    pitch = 440
    duration = 0.2
    beat1 = tone(pitch, 0 , duration, amplitude = .5, sample_rate=sample_rate)
    beat2 = tone(pitch, 0 , duration, amplitude = .25, sample_rate=sample_rate)
    beat3 = tone(pitch, 0 , duration, amplitude = .1, sample_rate=sample_rate)
    plt.plot(beat1)
    plt.show()

    SOA = .4
    totalduration = SOA * 17

    # stim1
    a = np.zeros(int(sample_rate * totalduration))
    multi_mix(a, beat1, SOA * np.array([2, 4, 6, 8, 10, 12, 14]))
    multi_mix(a, beat2, SOA * np.array([3, 5, 9, 11, 13]))
    multi_mix(a, beat3, SOA * np.array([1, 7, 15]))

    # stim2
    b = np.zeros(int(sample_rate * totalduration))
    multi_mix(b, beat1, SOA * np.array([2, 3, 5, 6, 8, 9, 11, 12]))
    multi_mix(b, beat2, SOA * np.array([4, 10]))
    multi_mix(b, beat3, SOA * np.array([1, 7, 13]))

    sr, beat = load_sound_as_array('cymbal22050.wav')
    # stim2
    c = np.zeros(int(sample_rate * totalduration))
    multi_mix(b, beat, SOA * np.array([2, 3, 5, 6, 8, 9, 11, 12]))
    #multi_mix(b, beat, SOA * np.array([4, 10]))
    #multi_mix(b, beat, SOA * np.array([1, 7, 13]))

    stimuli = [a, b, c]

    # run the experiment
    for trial, stim in enumerate(stimuli):
        play_mono(stim)
