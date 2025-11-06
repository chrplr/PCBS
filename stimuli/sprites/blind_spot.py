import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Disk Controller")

# Define colors
white = (255, 255, 255)
gray = (226, 232, 240)
dark_gray = (26, 32, 44)
disk_color = (76, 81, 191)

# Disk properties
disk_x = width // 2
disk_y = height // 2
disk_radius = 40
disk_speed = 10

# Fixation cross properties
cross_size = 20
cross_thickness = 2
cross_x = width * 0.25
cross_y = height / 2

# Main game loop
def main():
    global disk_x, disk_y, disk_radius, width, height, cross_x, cross_y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    disk_y -= disk_speed
                elif event.key == pygame.K_DOWN:
                    disk_y += disk_speed
                elif event.key == pygame.K_LEFT:
                    disk_x -= disk_speed
                elif event.key == pygame.K_RIGHT:
                    disk_x += disk_speed
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    disk_radius = min(disk_radius + 5, 100)
                elif event.key == pygame.K_MINUS:
                    disk_radius = max(disk_radius - 5, 5)
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resizing
                width, height = event.size
                cross_x = width * 0.25
                cross_y = height / 2
                disk_x = min(max(disk_x, disk_radius), width - disk_radius)
                disk_y = min(max(disk_y, disk_radius), height - disk_radius)

        # Keep disk within boundaries
        disk_x = min(max(disk_x, disk_radius), width - disk_radius)
        disk_y = min(max(disk_y, disk_radius), height - disk_radius)

        # Drawing
        screen.fill(gray)
        
        # Draw the fixation cross
        pygame.draw.rect(screen, dark_gray, (cross_x - cross_size / 2, cross_y - cross_thickness / 2, cross_size, cross_thickness))
        pygame.draw.rect(screen, dark_gray, (cross_x - cross_thickness / 2, cross_y - cross_size / 2, cross_thickness, cross_size))

        # Draw the disk
        pygame.draw.circle(screen, disk_color, (disk_x, disk_y), disk_radius)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
