#! /usr/bin/env python
# Time-stamp: <2024-06-24 09:00:16 christophe@pallier.org>

import sys
import wave
import pyaudio

chunk_size = 1024

sound = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format =
                p.get_format_from_width(sound.getsampwidth()),
                channels = sound.getnchannels(),
                rate = sound.getframerate(),
                output = True)

data = sound.readframes(chunk_size)

while data:
    stream.write(data)
    data = sound.readframes(chunk_size)

sound.close()
stream.close()
p.terminate()
