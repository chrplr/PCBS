#! /usr/bin/env python
# Time-stamp: <2018-10-09 16:39:47 cp983411>

"""Add clicks to a sound track.

"""

import sys
import numpy as np
import scipy.io.wavfile  # for scipy.io.wavfile.read


def load_sound_as_array(filename):
    [sample_rate, audio_data] = scipy.io.wavfile.read(filename)
    return [sample_rate, audio_data]


def write_array_as_sound(nparray, sample_rate, filename):
    scipy.io.wavfile.write(filename,
                           sample_rate,
                           nparray.T.astype(np.dtype('i2')))


def mix_sound(target, mix, position, sample_rate=22050, replace=True):
    samples = range(int(sample_rate * position),
                    int(sample_rate * position) + len(mix))
    if replace:
        target[samples] = mix
    else:
        target[samples] = target[samples] + mix


def multi_mix(target, mix, positions, sample_rate=22050, replace=True):
    for pos in positions:
        mix_sound(target, mix, pos, sample_rate, replace)


def generate_click_train(channel1, positions, sr):
    assert len(channel1.shape) == 1  # must be mono
    channel2 = np.zeros(channel1.shape)
    sr_c, click = load_sound_as_array('click.wav')
    multi_mix(channel2, click, positions, sample_rate=sr)
    return channel2

if __name__ == '__main__':
    sr, channel1 =  load_sound_as_array(sys.argv[1])
    positions = np.loadtxt(sys.argv[2])
    outfile = sys.argv[3]

    channel2 = generate_click_train(channel1, positions, sr)
    stereo_sound = np.vstack([channel1, channel2])
    write_array_as_sound(stereo_sound, sr, outfile)
