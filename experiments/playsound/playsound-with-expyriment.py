#! /usr/bin/env python
# Time-stamp: <2024-06-24 06:49:39 christophe@pallier.org>


import sys
from expyriment import design, control, stimuli, io, misc

filename = sys.argv[1]

exp = design.Experiment(name="Audio Test")

control.defaults.initialize_delay = 0
control.defaults.audio_system_buffer_size = 128 
control.audiosystem_channels = 2
control.audiosystem_sample_rate = 96000

control.set_develop_mode(True)

control.initialize(exp)

stim = stimuli.Audio(filename)
stim.preload()

control.start(exp, subject_id=1)

stim.present()
control.wait_end_audiosystem(process_control_events=True)

control.end()
