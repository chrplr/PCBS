#! /usr/bin/env python
# Time-stamp: <2021-04-05 07:40:32 christophe@pallier.org>

""" Display Kanisza illusory square

(see https://openi.nlm.nih.gov/detailedresult?img=PMC4211395_fnhum-08-00854-g0001&req=4 )

"""

from expyriment import design, control
from expyriment.misc import Colour
from expyriment.stimuli import BlankScreen, Circle, Rectangle

GRAY = Colour('gray')
BLACK = Colour('black')
WHITE = Colour('white')


def Kanisza_square(width, height, radius, backgroung_color=GRAY, square_color=GRAY,
                   color_tl=BLACK, color_tr=BLACK, color_bl=BLACK,  color_br=BLACK):
    """ Creates a surface with Kanisza illusory square

    (see https://openi.nlm.nih.gov/detailedresult?img=PMC4211395_fnhum-08-00854-g0001&req=4 )

    """

    surface = BlankScreen(backgroung_color)

    # coordinates  of the corners of the rectangle (also that of the circles' centers)
    left = - width // 2
    right = width // 2
    top = height // 2
    bottom = - height // 2

    c_tl = Circle(radius, color_tl, position = (left, top), anti_aliasing = 10)
    c_tr = Circle(radius, color_tr, position = (right, top), anti_aliasing = 10)
    c_bl = Circle(radius, color_bl, position = (left, bottom), anti_aliasing = 10)
    c_br = Circle(radius, color_br, position = (right, bottom), anti_aliasing = 10)
    rect = Rectangle((width, height), square_color,  position = (0, 0), corner_anti_aliasing = True)

    c_tl.plot(surface)
    c_tr.plot(surface)
    c_bl.plot(surface)
    c_br.plot(surface)
    rect.plot(surface)

    return surface


if __name__ == '__main__':
    exp = design.Experiment(name="Kanisza square")
    control.set_develop_mode(on=True)  # Comment out for full screen experiment
    control.initialize(exp)
    control.start(skip_ready_screen=True)

    RADIUS = 50
    WIDTH, HEIGHT = 200, 200
    surface = Kanisza_square(WIDTH, HEIGHT, RADIUS, backgroung_color=GRAY, square_color=GRAY,
                             color_tl=BLACK, color_tr=BLACK, color_bl=BLACK,  color_br=BLACK)

    surface.present()
    exp.screen.save('kanisza-squares2.png')
    exp.keyboard.wait()

    control.end()

