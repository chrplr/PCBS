#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal skeleton for an experyment script  
(see <https://docs.expyriment.org/Tutorial.html>)

Created on Sat Sep 21 11:36:41 2019

@author: christophe@pallier.org
"""

import expyriment

exp = expyriment.design.Experiment(name="First Experiment")

## Set develop mode. Comment for real experiment
expyriment.control.set_develop_mode(on=True)

expyriment.control.initialize(exp)

### insert here some code to generate the stimuli

expyriment.control.start()

### insert here some code to present the stimuli and record responses

expyriment.control.end()

