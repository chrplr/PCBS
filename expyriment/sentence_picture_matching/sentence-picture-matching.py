#! /usr/bin/env python
# Time-stamp: <2019-11-18 17:34:02 christophe@pallier.org>

""" sentence picture matching task """

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
