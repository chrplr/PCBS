from serial import Serial
from time import sleep

serialport = '/dev/ttyUSB1'  

dlp = Serial(port=serialport, baudrate=115200)  # open serial port

def triggers_up():
    dlp.write(b'12345678')  # sets all lines to '1'

def triggers_down():
    dlp.write(b'QWERTYUI')  # sets all lines to '0'

