#! /usr/bin/env python
# Time-stamp: <>

import sys
import time
from openal.audio import SoundSink, SoundSource
from openal.loaders import load_wav_file

sink = SoundSink()
sink.activate()

source = SoundSource()
source.looping = True

wavsound = load_wav_file(sys.argv[1])
source.queue(wavsound)

sink.play(source)

time.sleep(10) # I do not know how to check if playback is going on !

# while source.position[0] > -10:
#         source.position = [source.position[0] - 1,
#                            source.position[1],
#                            source.position[2]]
#         sink.update()
#         print("playing at %r" % source.position)
#         time.sleep(2)

print("done")
