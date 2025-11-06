#! /usr/bin/env python

""" Test of LabJack U3 IO device """ 

# Installation of labjack software
# 1. install exodriver
#
#      git clone https://github.com/labjack/exodriver.git
#      cd exodriver
#      sudo ./install.sh
#
# 2. install labjack Python's module
#
#      pip install LabJackPython

import time
import u3

d = u3.U3()

# code from https://labjack.com/support/software/examples/ud/labjackpython/modbus 
# (see also https://labjack.com/support/software/api/modbus/ud-modbus)

# READ 0/1 on FIO6
FIO6_DIR_REGISTER = 6106
FIO6_STATE_REGISTER = 6006
d.writeRegister(FIO6_DIR_REGISTER, 0)  # Set FIO4 to digital input
d.readRegister(FIO6_STATE_REGISTER)    # Read the state of FIO6


# OUTPUT 0/1 on FIO4
FIO4_STATE_REGISTER = 6004
d.writeRegister(FIO4_STATE_REGISTER, 0)  # Set FIO4 low, LED on
time.sleep(1)
d.writeRegister(FIO4_STATE_REGISTER, 1) # Set FIO4 high, LED off
