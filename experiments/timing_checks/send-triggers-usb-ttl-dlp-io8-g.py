#! /usr/bin/env python3
# Time-stamp: <2022-04-29 08:31:31 christophe@pallier.org>

""" Generate a square wave on pin1 of DLP-IO8-G """

from time import sleep, perf_counter
from serial import Serial

dlp = Serial(port='/dev/ttyUSB0', baudrate=115200)  # open serial port
# byte codes to control line 1:
ON1 = b'1'
OFF1 = b'Q'

# number of periods
NPERIODS = 1000

# Timing of the square wave
TIME_HIGH = 0.010   # 10ms pulse
TIME_LOW = 0.090    # send every 100ms
PERIOD = TIME_HIGH + TIME_LOW

onset_times = [(i * PERIOD) for i in range(NPERIODS)]

actual_onsets = []
i = 0
t0 = perf_counter()
while i < NPERIODS:
    # busy wait until the start of the next period
    while perf_counter() - t0 < onset_times[i]:
        pass

    actual_onsets.append(perf_counter() - t0)
    dlp.write(ON1)

    # busy wait for 'TIME_HIGH' seconds. 
    t1 = perf_counter()
    while perf_counter() - t1 < (TIME_HIGH):
        pass

    dlp.write(OFF1)
    i = i + 1
    print(f"\r{i:4d}", end='')

sleep(TIME_LOW)
print(f'\r{NPERIODS} periods of {PERIOD} seconds')
print('Total time-elapsed: ' + str(perf_counter() - t0))
print("Actual onsets:")
for t in actual_onsets:
    print(t, end=" ")
print(end="\n")
dlp.close()         # close the port
