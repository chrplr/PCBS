#! /usr/bin/env python3
# Time-stamp: <2024-06-24 08:58:38 christophe@pallier.org>

import sys
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file(sys.argv[1])
play_obj = wave_obj.play()
play_obj.wait_done()  
