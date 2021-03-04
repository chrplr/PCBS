"""
Script to display a Hermann grid with the given grid parameters
in a window and save it to a png file on disk.

Execute this script from the Terminal and pass the parameters
as command-line arguments, for example:
    `python hermann_grid_cedric.py --space_between_cells 17`
"""

import argparse
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def grid_side_length(n_segments, cell_side_length, space_between_cells):
    return space_between_cells + \
                (cell_side_length + space_between_cells) * n_segments

def grid_size(n_rows, n_columns, cell_side_length, space_between_cells):
    grid_width = grid_side_length(n_columns, cell_side_length, space_between_cells)
    grid_height = grid_side_length(n_rows, cell_side_length, space_between_cells)
    return grid_width, grid_height

def create_screen_with_size(screen_size):
    screen = pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)
    return screen

def draw_grid_background_on_screen(screen, color):
    screen.fill(color)

def draw_grid_cells_on_screen(screen,
    n_rows, n_columns, cell_side_length, space_between_cells, color):
    cell_indices = [ (i_row, i_col) \
                     for i_row in range(n_rows) \
                     for i_col in range(n_columns)
    ]
    for cell_index in cell_indices:
        draw_square_on_screen_at_cell_index(screen, cell_index,
            cell_side_length, space_between_cells, color)

def draw_square_on_screen_at_cell_index(screen, cell_index,
    cell_side_length, space_between_cells, color):
    i_row, i_col = cell_index
    x_left = space_between_cells + \
            (cell_side_length + space_between_cells) * i_col
    y_top = space_between_cells + \
            (cell_side_length + space_between_cells) * i_row
    draw_square_on_screen_at_coordinates(screen, x_left, y_top, cell_side_length, color)

def draw_square_on_screen_at_coordinates(screen, x_left, y_top, side_length, color):
    pygame.draw.rect(screen, color,
        (x_left, y_top, side_length, side_length))

def display_screen_in_window():
    pygame.display.flip()

def save_screen_to_image_path(screen, image_path):
    pygame.image.save(screen, image_path)

def wait_until_user_closes_window():
    done = False
    while not done:
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

# `n_rows, `n_columns`, and `cell_side_length` could also be given as
# command-line arguments using `add_arguments()`, like `space_between_cells`.
n_rows = 10
n_columns = 15
cell_side_length = 50

parser = argparse.ArgumentParser()
parser.add_argument('--space_between_cells', type=int)
args = parser.parse_args()
space_between_cells = args.space_between_cells

color_space = WHITE
color_cell = BLACK

image_path = f"hermann_grid_cedric_space-{space_between_cells}.png"

pygame.init()

size = grid_size(n_rows, n_columns, cell_side_length, space_between_cells)
screen = create_screen_with_size(size)
draw_grid_background_on_screen(screen, color_space)
draw_grid_cells_on_screen(screen, n_rows, n_columns,
    cell_side_length, space_between_cells, color_cell)

display_screen_in_window()
save_screen_to_image_path(screen, image_path)

wait_until_user_closes_window()

pygame.quit()
