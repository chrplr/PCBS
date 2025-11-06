#! /usr/bin/env python
# Time-stamp: <2022-05-12 10:56:29 christophe@pallier.org>
# See doc at https://docs.expyriment.org/expyriment.io.ParallelPort

from time import sleep
from expyriment.io import ParallelPort

pp = ParallelPort('/dev/parport4')

while True:
    pp.set_data(255)
    sleep(1)
    pp.set_data(0)
    sleep(1)

