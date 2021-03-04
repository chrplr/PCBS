import argparse
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

n_rows = 10
n_columns = 15

cell_side_length = 50
# space_between_cells = 50

parser = argparse.ArgumentParser()
parser.add_argument('--space_between_cells', type=int)
# parser.add_argument('--n_rows', type=int)
args = parser.parse_args()
space_between_cells = args.space_between_cells

color_space = WHITE
color_cell = BLACK

image_path = f"herman_grid_cedric_space-{space_between_cells}.png"

# grid_specs = {
#     "n_rows": 10,
#     "n_columns": 15,
#     # ...
# }

def grid_side_length(n_segments):
    return space_between_cells + \
                (cell_side_length + space_between_cells) * n_segments

def grid_size():
    grid_width = grid_side_length(n_columns)
    grid_height = grid_side_length(n_rows)
    return grid_width, grid_height

def create_screen():
    grid_width, grid_height = grid_size()
    screen = pygame.display.set_mode((grid_width, grid_height), pygame.DOUBLEBUF)
    return screen

def draw_grid_background(screen):
    screen.fill(color_space)

def draw_grid_cells(screen):
    cell_indices = [ (i_row, i_col) \
                     for i_row in range(n_rows) \
                     for i_col in range(n_columns)
    ]
    for cell_index in cell_indices:
        draw_square_at_cell_index(screen, cell_index)

def draw_square_at_cell_index(screen, cell_index):
    i_row, i_col = cell_index
    x_left = space_between_cells + \
            (cell_side_length + space_between_cells) * i_col
    y_top = space_between_cells + \
            (cell_side_length + space_between_cells) * i_row
    draw_square(screen, x_left, y_top, cell_side_length)

def draw_square(screen, x_left, y_top, cell_side_length):
    pygame.draw.rect(screen, color_cell,
        (x_left, y_top, cell_side_length, cell_side_length))

def display_screen_in_window():
    pygame.display.flip()

def save_screen_to_image_path(image_path):
    pygame.image.save(screen, image_path)

def wait_until_user_closes_window():
    done = False
    while not done:
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

pygame.init()

screen = create_screen()
draw_grid_background(screen)
draw_grid_cells(screen)

display_screen_in_window()
save_screen_to_image_path(image_path)

wait_until_user_closes_window()

pygame.quit()
