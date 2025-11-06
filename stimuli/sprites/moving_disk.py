import pygame
import random
import math

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
DISK_RADIUS = 25
DISK_SPEED = 3

# --- Colors ---
# Using a pleasant color palette
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
DISK_COLOR = (70, 130, 180)  # Steel Blue
SHADOW_COLOR = (50, 50, 50)

# --- Initialization ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smooth Random Disk Movement")
clock = pygame.time.Clock()

# --- Disk Properties ---
# Start the disk in the center of the screen
disk_x = SCREEN_WIDTH // 2
disk_y = SCREEN_HEIGHT // 2

# Generate a random initial direction
angle = random.uniform(0, 2 * math.pi)
vel_x = DISK_SPEED * math.cos(angle)
vel_y = DISK_SPEED * math.sin(angle)

# --- Game Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movement Logic ---
    # Add a small random perturbation to the velocity for a smooth, wandering path
    # This prevents the movement from being too linear and predictable.
    turn_strength = 0.5  # How sharply the disk can turn
    vel_x += random.uniform(-turn_strength, turn_strength)
    vel_y += random.uniform(-turn_strength, turn_strength)

    # Normalize the velocity vector to maintain constant speed
    current_speed = math.sqrt(vel_x**2 + vel_y**2)
    if current_speed > 0:
        vel_x = (vel_x / current_speed) * DISK_SPEED
        vel_y = (vel_y / current_speed) * DISK_SPEED

    # Update disk position
    disk_x += vel_x
    disk_y += vel_y

    # --- Boundary Collision Detection ---
    # Check for collision with the window edges and bounce
    if disk_x <= DISK_RADIUS or disk_x >= SCREEN_WIDTH - DISK_RADIUS:
        vel_x *= -1  # Reverse horizontal direction
        # Nudge the disk back inside to prevent it from getting stuck
        disk_x = max(DISK_RADIUS, min(disk_x, SCREEN_WIDTH - DISK_RADIUS))
        
    if disk_y <= DISK_RADIUS or disk_y >= SCREEN_HEIGHT - DISK_RADIUS:
        vel_y *= -1  # Reverse vertical direction
        # Nudge the disk back inside
        disk_y = max(DISK_RADIUS, min(disk_y, SCREEN_HEIGHT - DISK_RADIUS))

    # --- Drawing ---
    # Fill the background
    screen.fill(BLACK)

    # Draw a subtle shadow first for a slight 3D effect
    pygame.draw.circle(screen, SHADOW_COLOR, (int(disk_x) + 3, int(disk_y) + 3), DISK_RADIUS)

    # Draw the main disk
    pygame.draw.circle(screen, DISK_COLOR, (int(disk_x), int(disk_y)), DISK_RADIUS)

    # --- Update the Display ---
    pygame.display.flip()

    # --- Frame Rate Control ---
    clock.tick(FPS)

# --- Quit ---
pygame.quit()
