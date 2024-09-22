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
button_font = font.render("PLAY", True, black)




running = True
my_game = Game(Starting_player_lives)
my_game.starting_screen()
while running:
    
    display_surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        
    button = pygame.Rect(200,200,110,60)
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                    my_game.game_screen()
            elif events.type == pygame.QUIT:
                pygame.quit()    
        
    a,b = pygame.mouse.get_pos()
    if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
        pygame.draw.rect(display_surface,(pink_second),button )
    else:
        pygame.draw.rect(display_surface, (white),button)
    
    display_surface.blit(button_font,(button.x + 30, button.y + 15))
    #Update and set FPS
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()