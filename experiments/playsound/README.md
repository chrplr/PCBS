# playsound 

Examples of playing sound with various backends:

playsound-with-expyriment.py
playsound-with-pyaudio.py
playsound-with-pygame.py
playsound-with-simpleaudio.py



# Linux

aplay -L  # get the list of devices

pasuspender -- aplay -v -D iec958:CARD=X,DEV=0 --dump-hw-params --buffer-size=64 --period-size=16 wahwah.wav 
