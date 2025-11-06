import sys
import wave
import alsaaudio

device = 'default'

with wave.open(sys.argv[1], 'rb') as f:

	format = None

	if f.getsampwidth() == 1:
		format = alsaaudio.PCM_FORMAT_U8
	elif f.getsampwidth() == 2:
		format = alsaaudio.PCM_FORMAT_S16_LE
	elif f.getsampwidth() == 3:
		format = alsaaudio.PCM_FORMAT_S24_3LE
	elif f.getsampwidth() == 4:
		format = alsaaudio.PCM_FORMAT_S32_LE
	else:
	    raise ValueError('Unsupported format')

	periodsize = f.getframerate() // 8

	print('%d channels, %d sampling rate, format %d, periodsize %d\n' % (f.getnchannels(), f.getframerate(), format, periodsize))

	device = alsaaudio.PCM(channels=f.getnchannels(), rate=f.getframerate(), format=format, periodsize=periodsize, device=device)
	
	data = f.readframes(periodsize)
	while data:
	    if device.write(data) < 0:
	        print("Playback buffer underrun! Continuing nonetheless ...")
	    data = f.readframes(periodsize)
                                                                    
