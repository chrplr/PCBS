#! /usr/bin/env python3
# Time-stamp: <2024-06-24 08:58:38 christophe@pallier.org>

import sys
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav(sys.argv[1])
play(song)


