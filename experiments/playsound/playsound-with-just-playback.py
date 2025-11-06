#! /usr/bin/env python3
# Time-stamp: <2024-06-24 08:58:38 christophe@pallier.org>

import sys
from time import sleep
from just_playback import Playback

playback = Playback()
playback.load_file(sys.argv[1])
playback.play()


while playback.active:
    sleep(.1)
