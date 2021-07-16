#! /usr/bin/env python
# Time-stamp: <2021-04-20 15:38:58 christophe@pallier.org>
""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

from expyriment import design, control, stimuli, misc

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# parameters of the grid
n_rows, n_cols = 10, 10
cell_side_length = 50
space_between_cells = 10

# graphic window cell_side_length
W = n_cols * cell_side_length + (n_cols - 1) * space_between_cells
H = n_rows * cell_side_length + (n_rows - 1) * space_between_cells

exp = design.Experiment(name="Herman's Grid",
                        background_colour=GRAY)
#control.set_develop_mode(on=True)  # Comment out for full screen experiment
control.initialize(exp)
control.start(subject_id=1, skip_ready_screen=True)

# construction of the grid
b = stimuli.BlankScreen(GRAY)

quit = False
while not quit:
    b.clear_surface()
    for i_row in range(n_rows):
        for i_col in range(n_cols):
            x_left = i_col * (cell_side_length +
                              space_between_cells) - cell_side_length // 2 - W // 2
            y_top = i_row * (cell_side_length +
                             space_between_cells) - cell_side_length // 2 - H // 2
            r = stimuli.Rectangle((cell_side_length, cell_side_length), BLACK,
                                  position=(x_left, y_top))
            r.plot(b)
    b.present()

    keyp, _ = exp.keyboard.wait([misc.constants.K_LEFT, misc.constants.K_RIGHT])

    if keyp == misc.constants.K_RIGHT and space_between_cells < 100:
        space_between_cells += 1


    if keyp == misc.constants.K_LEFT and space_between_cells > 1:
        space_between_cells -= 1


control.end()
