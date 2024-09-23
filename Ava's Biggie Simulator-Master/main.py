import pygame
from file_Path_fn import *
from Game_class import *

# Initialize game
pygame.init()

# Set display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

#Set Colors
white = (255, 255, 255)
pink_main = (255, 153, 255)
pink_second = (255, 204, 255)
black = (0, 0, 0)

#Set Screen and related values
# ava = pygame.image.load("Ava_starting.png")
# icon_image = pygame.image.load(("Ava's Biggie Simulator_icon.png"))
# pygame.display.set_icon(icon_image)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
# pygame.display.set_caption("Ava's Biggie Simulator")
font = pygame.font.Font("Soda Cream.otf", 25)
FPS = 60
clock = pygame.time.Clock()


#Set global varialbles
Starting_player_lives = 5


running = True
my_game = Game(Starting_player_lives)
my_game.starting_screen()
while running:
    my_game.pause_screen()
pygame.quit()

