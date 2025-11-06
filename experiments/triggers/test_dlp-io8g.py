from serial import Serial
from time import sleep

dlp = Serial(port='/dev/ttyUSB1', baudrate=115200)  # open serial port


for i in range(50):
    dlp.write(b'QWERTYUI')  # sets all lines to '0'
    sleep(0.5)
    dlp.write(b'12345678')  # sets all lines to '1'
    sleep(0.5)

dlp.write(b'QWERTYUI')  # sets all lines back to '0'
