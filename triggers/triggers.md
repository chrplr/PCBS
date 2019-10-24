=====================================
Sending TTL triggers throught the USB
=====================================

Many pieces of equipment synchronize by exchanging triggers (0/1 bits) on a [TTL interface](https://en.wikipedia.org/wiki/Transistor%E2%80%93transistor_logic)A TTL input signal is defined as "low" when between 0 V and 0.8 V with respect to the ground terminal, and "high" when between 2 V and VCC (5 V).

For example, you may need to send a trigger to an EEG or MEG recording machine, or wait for a MRI scanner signaling that it is starting the image acquistiong. 

To send or read TTL signals with your computer, you need some extra hardware (unless you have a Raspberry Pi which has a GPIO port).


# DLP-IO8-G

The [DLP-IO8-G](http://www.ftdichip.com/Support/Documents/DataSheets/DLP/dlp-io8-ds-v15.pdf) is a USB-TTL device that provides 8 digital lines on which you can read or write. It appears to your computer as a serial device, so you simply communicate with it by opening the relevant serial port and then simply write to or read from it.

Under Linux, the dlp-OI8-G driver is already in the kernel, so you just have to plug it in a USB port of your computer. To determine the serial port it is attached to, type the command `dmesg` in a Terminal. You should get something like::

---
[ 5128.109725] usbcore: registered new interface driver usbserial_generic
[ 5128.109730] usbserial: USB Serial support registered for generic
[ 5128.112142] usbcore: registered new interface driver ftdi_sio
[ 5128.112148] usbserial: USB Serial support registered for FTDI USB Serial Device
[ 5128.112175] ftdi_sio 1-1:1.0: FTDI USB Serial Device converter detected
[ 5128.112190] usb 1-1: Detected FT232RL
[ 5128.113130] usb 1-1: FTDI USB Serial Device converter now attached to ttyUSB0
---

The last line tells you that the device is at `/dev/ttyUSB0`.

## Python 

To use the device under Python, you need the [pyserial module](https://pyserial.readthedocs.io/en/latest/shortintro.html)


### sending a trigger 

---
import time, serial

dlp = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)  # open serial port

dlp.write(b'Q')     # Low
time.sleep(1)       # wait 1s
dlp.write(b'1')     # High
time.sleep(0.01)    # wait 10ms
dlp.write(b'Q')     # Low

dlp.close()         # close the port
---

## reading an input line


---
import time
import serial
import numpy as np
import matplotlib.pyplot as plt


dlp = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)  # open serial port
print(dlp.name)         # check which port was really used
dlp.write(b'`')  # switch to ascii mode

N = 1000
i = 0
o = np.zeros(N)
while i < N:
   dlp.write(b'A')
   x = dlp.read(3).decode('utf-8')
   if x[0]=='1':
      o[i] = time.perf_counter()
      i += 1
plt.hist(np.diff(o)*1000.0) 
---

### Latencies and reliability to measure a time interval

TODO


# Arduino

If you do not have a DLP-IO8-G, another approach is to use an [Arduino](https://www.arduino.cc) and program it to send a signal to your PC when it received a trigger. The [Leonardo version](https://www.arduino.cc/en/Main/Arduino_BoardLeonardo) is recommended as it can be seen as an HID device and it is trivial to program it to send a key press to your computer upon receving a trigger. Thus, you stimulation program just has to wait for a keypress and does not even need to open a serial port.  


# Raspberry Pi

TODO

You can use [gpizero](https://gpiozero.readthedocs.io/en/stable/) or [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) 

The RPi.GPIO web page warns that "this module is unsuitable for real-time or timing critical applications. This is because you can not predict when Python will be busy garbage collecting. It also runs under the Linux kernel which is not suitable for real time applications - it is multitasking O/S and another process may be given priority over the CPU, causing jitter in your program.  If you are after true real-time performance and predictability, buy yourself an Arduino"

This is true, but nevertheless the Raspberry PI may be sufficient for an application that does not overloard the PC and just need to read or send some sparse triggers. The only way to know is to check for latencies using an external equipment.


