#! /usr/bin/env python
# Time-stamp: <2024-05-03 11:59:16 christophe@pallier.org>
""" Generate a sound file containing a square wave """

import argparse
import numpy as np
import numpy.typing as npt
import scipy.io.wavfile

DEFAULT_SAMPLE_RATE = 44100

verbose = False

def create_square_wave(
    on_duration: float,
    off_duration: float,
    n_cycles: int,
    sample_rate: int,
) -> npt.NDArray[np.int_]:

    on = 16384 * np.ones(int(np.ceil(on_duration * sample_rate)),
                         dtype=np.int16)
    off = np.zeros(int(np.ceil(off_duration * sample_rate)), dtype=np.int16)

    period = np.concatenate([on, off])

    wave = np.tile(period, n_cycles)

    if (verbose):
        print(f"period = {len(period) / sample_rate}")
        print(f"total duration = {len(wave) / sample_rate}s")
        print(f"n_frames = {len(wave)}")
        print(f"sample_rate = {sample_rate}Hz")

    return wave


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--on',
                        type=float,
                        required=True,
                        help="duration of the on  (float, in sec)")

    parser.add_argument("--off",
                        type=float,
                        required=True,
                        help="duration of off  (float, in sec)")

    parser.add_argument("--n-cycles",
                        type=int,
                        required=True,
                        help="number of repetitions (int)")

    parser.add_argument("--sample-rate",
                        type=int,
                        default=DEFAULT_SAMPLE_RATE,
                        help="sample rate")

    parser.add_argument("--verbose",
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help="print information")


    args = parser.parse_args()

    verbose = args.verbose

    stream = create_square_wave(args.on, args.off, args.n_cycles,
                                args.sample_rate)

    duration = int(len(stream) / args.sample_rate)

    wavfile_name = f"square-{args.on}on-{args.off}off-{duration}s.wav"
    scipy.io.wavfile.write(wavfile_name, args.sample_rate,
                           stream.T.astype(np.dtype('i2')))
    print(f"{wavfile_name} written.")
