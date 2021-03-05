import pygame
from math import *
import random
 
## Lilac Chaser
 
def lilac_chaser(color=(227, 154, 220), step=100, W=500, H=500) :
    
    GRAY = (196, 196, 196)
    BLACK = (0, 0, 0)
    xcenter = int(W//2)
    ycenter = int(H//2)
    xcenter = int(W//2)
 
    # Parameters
    cross_side = W//100 # Size of the cross
    nb_circles = 12 # Number of circles
    radius = W//50 # Radius of each circle
    R = int(64*radius/pi) # Radius of the big circle
    grad = int(3*radius) # Size of the fading gradient
 
    # Loop
    hidden_circle = 0 
    done = False
    while not done:
        
        pygame.init()
        screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
        screen.fill(GRAY)
        pygame.time.wait(step)
        
        # Center cross
        pygame.draw.line(screen, BLACK, (xcenter-cross_side, ycenter), (xcenter+cross_side, ycenter))
        pygame.draw.line(screen, BLACK, (xcenter, ycenter-cross_side), (xcenter, ycenter+cross_side))
        
        # Draw circles
        hidden_circle = hidden_circle % nb_circles
        for i in range(nb_circles) :
            if i != hidden_circle :
                alpha = i*2*pi/nb_circles
                x = int(R*cos(alpha))
                y = int(R*sin(alpha))
                pygame.draw.circle(screen, color, (xcenter+x, ycenter+y), radius)
                # Make gradient
                for k in range(grad) :
                    fade_color = tuple(map(lambda x, y: int(x*(grad-k)/grad + y*k/grad), color, GRAY))
                    pygame.draw.circle(screen, fade_color, (xcenter+x, ycenter+y), radius+k, 3) # Linewidth=3 for a more homogenous gradient
        
        
        # Change the circle to hide
        hidden_circle += 1
        
        # Display-end stuff
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    pygame.quit()
