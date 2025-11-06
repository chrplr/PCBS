#! /usr/bin/env python3
# Time-stamp: <2022-05-05 19:24:05 christophe@pallier.org>

"""Monitors the // ports"""

from expyriment import io

pports = [io.ParallelPort('/dev/' + pp) for pp in io.ParallelPort.get_available_ports()]

prev_state = []
while True:
    state = str([bin(p.poll()) for p in pports])
    if state != prev_state:
        print(state)
        prev_state = state
