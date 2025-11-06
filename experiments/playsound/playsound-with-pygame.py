import sys
import pygame

sound_filename = sys.argv[1]

pygame.mixer.init()

pygame.mixer.music.load(sound_filename) 
pygame.mixer.music.play()

while pygame.mixer.Channel(0).get_busy():
    pygame.time.wait(100)  # ms
    print("Playing...")

print("Finished.")

# or

sound = pygame.mixer.Sound(sound_filename)
channel = sound.play()

while channel.get_busy():
    pygame.time.wait(100)
    print("Playing...")

print("Finished.")


