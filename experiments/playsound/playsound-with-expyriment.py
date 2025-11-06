#! /usr/bin/env python
# Time-stamp: <2024-06-24 06:49:39 christophe@pallier.org>


import sys
from expyriment import design, control, stimuli, io, misc
#from trigger_dlp_io8_g import triggers_down, triggers_up

filename = sys.argv[1]

#triggers_down()

exp = design.Experiment(name="Audio Test")

control.defaults.initialize_delay = 2
control.defaults.audio_system_buffer_size = 2048
control.audiosystem_channels = 2
control.audiosystem_sample_rate = 44100

control.set_develop_mode(True)

control.initialize(exp)

stim = stimuli.Audio(filename)
stim.preload()

control.start(exp, subject_id=1)

exp.screen.clear()
stim.present()

#triggers_up()
exp.clock.wait(10)
#triggers_down()

control.wait_end_audiosystem(process_control_events=True)

#triggers_up()
exp.clock.wait(10)
#triggers_down()


control.end()
