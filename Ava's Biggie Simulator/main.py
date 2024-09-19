import pygame
from Function_1 import *
 
# Initialize game
pygame.init()

# Set display
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

icon_image = pygame.image.load(("Ava's Biggie Simulator_icon.png"))
pygame.display.set_icon(icon_image)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ava's Biggie Simulator")

ava_image = icon_image.get_rect()
ava_image.centerx = (300)
ava_image.centery = (150)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(icon_image,ava_image)
    pygame.display.update()

pygame.quit()