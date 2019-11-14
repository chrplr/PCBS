# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:26:41 2019

@author: install
"""

import sys
if sys.argv[1]=="F":
    temp = (int(sys.argv[2]) - 32)*5/9
    print(temp, " °C")
if sys.argv[1] == "C":
    temp = int(sys.argv[2]) *9/5 + 32
    print(temp, " °F")
