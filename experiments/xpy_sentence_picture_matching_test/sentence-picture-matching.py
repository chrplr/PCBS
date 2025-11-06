#! /usr/bin/env python
# Time-stamp: <2019-11-19 11:07:19 christophe@pallier.org>

""" Example of a sentence picture matching task.

In a series of trials, a sound file is played, then a  picture is displayed. The participant must press one of two keys to indicate whether the picture matches the content of the sound file or not.

The experiment is driven by the file `trials.csv`  with one row per trial and two columns: `Sound` and `Img`.

"""

from os.path import join
from pandas import read_csv
import expyriment


exp = expyriment.design.Experiment(name="sentence picture matching task")  # create an Experiment object
expyriment.control.set_develop_mode(on=True)  ## Set develop mode. Comment for real experiment

expyriment.control.initialize(exp)

fixcross = expyriment.stimuli.FixCross(size=(25, 25),
                                 line_width=3,
                                 colour=expyriment.misc.constants.C_WHITE)

trials = read_csv("trials.csv")

exp.add_data_variable_names(['sound', 'picture', 'key', 'rt'])

expyriment.control.start()
fixcross.present()  # clear screen, presenting fixation cross


for row in trials.itertuples():
    sound = expyriment.stimuli.Audio(join("sounds", row.Sound))
    image = expyriment.stimuli.Picture(join("pictures", row.Img))

    sound.present()
    exp.clock.wait(3000)
    image.present()

    key, rt = exp.keyboard.wait()
    exp.data.add([row.Sound,
                  row.Img,
                  key,
                  rt])

    fixcross.present()
    exp.clock.wait(1000)

expyriment.control.end()
