import pygame, random
pygame.init()
    
tarting_player_lives = 5 

# Set display
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

#Set Colors
white = (255, 255, 255)
pink_main = (255, 153, 255)
pink_second = (255, 204, 255)
black = (0, 0, 0)

#Set Screen and related values
icon_image = pygame.image.load(("Ava's Biggie Simulator_icon.png"))
pygame.display.set_icon(icon_image)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Ava's Biggie Simulator")
FPS = 60
clock = pygame.time.Clock()
    
    
    
class Game():
    def __init__(self, starting_player_lives):
        self.lives = starting_player_lives
        self.score = 0
        #setting up fonts
        self.font = pygame.font.Font("Extra Days.ttf", 32)
        self.second_font = pygame.font.Font("Soda Cream.otf", 25)
        
    def starting_screen(self):
        pygame.mixer.music.load("main_game_music.mp3")
        pygame.mixer.music.play(-1,0)
        starting_screen = True
        display_surface.fill(white)
        
        #setting up main screen image
        ava_starting = pygame.image.load("ava_starting.png")
        ava_starting_rect = ava_starting.get_rect()
        ava_starting_rect.topleft = (166.5, 50)
        
        #setting up main screen font
        font = self.font.render("Ava's Biggie Simulator", True, pink_main)
        font_rect = font.get_rect()
        font_rect.centerx = (500)
        font_rect.centery = (50)
        
        #setting up secondary main screen font
        second_main_font = self.second_font.render("An Aidan Gutierrez Original", True, black)
        second_font_rect = second_main_font.get_rect()
        second_font_rect.centerx = (588)
        second_font_rect.centery = (85)
        
        #setting up play button 
        
        
        #bliting static media
        display_surface.blit(ava_starting, ava_starting_rect)
        display_surface.blit(font, font_rect)
        display_surface.blit(second_main_font, second_font_rect)
        
        #setting up loop
        while starting_screen:
            button_font = self.second_font.render("PLAY", True, black)
            button = pygame.Rect(200,200,110,60)
            for events in pygame.event.get():
                
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(events.pos):
                        starting_screen = False
                        pygame.mixer.music.stop()
                        self.game_screen()
                        break
                elif events.type == pygame.QUIT:
                    pygame.quit()
                    
            a,b = pygame.mouse.get_pos()
            if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
                pygame.draw.rect(display_surface,(pink_second),button )
            else:
                pygame.draw.rect(display_surface, (white),button)
            
            display_surface.blit(button_font,(button.x + 30, button.y + 15))
            pygame.display.update()
            clock.tick(FPS)
        
                
    def game_screen(self):
        pygame.mixer.music.load("playing_music.mp3")
        pygame.mixer.music.play(-1,0)
        eat_sound = pygame.mixer.Sound("eat_sound.mp3")
        disgust_sound = pygame.mixer.Sound("disgust_sound.mp3")
        game_screen = True
        player_velocity = 10
        food_velocity = 15
        BUFFER_DISTANCE = 100
        score = 0
        timer = 0
        
        
        
        player_eat = pygame.image.load("ava_player_eat.png")
        # player_eat_rect = player_eat.get_rect()
        # player_eat_rect.centerx = (38)
        # player_eat_rect.centery = (300)
        
        player = pygame.image.load("ava_player.png")
        player_rect = player.get_rect()
        player_rect.centerx = (38)
        player_rect.centery = (300)
        player_image = player
        
        food_list = ("cucumber.png", "bubblr.png", "popcorners.png", "sushi.png","treadmill.png")
        food_choice = random.choice(food_list)
        food = pygame.image.load(food_choice)
        food_rect = food.get_rect()
        food_rect.centerx = WINDOW_WIDTH + BUFFER_DISTANCE
        food_rect.bottom = random.randint(50, WINDOW_HEIGHT)
        
        score_title_font = pygame.font.Font("Soda Cream.otf", 50)
        score_title = score_title_font.render(f"Score: {score}", True, pink_main)
        score_title_rect = score_title.get_rect()
        score_title_rect.topleft = (50,0)
        
        title_main = self.font.render("Ava's Biggie Simulator", True, pink_main )
        title_main_rect = title_main.get_rect()
        title_main_rect.topleft = (310,10)
        
        score_lives = score_title_font.render(f"lives: {self.lives}", True, pink_main)
        score_lives_rect = score_lives.get_rect()
        score_lives_rect.topright = (950,0)
        
        while game_screen: 
            display_surface.fill(white)
            current_food = food_choice
            if timer > 10:
                player_image = player
            
            else:
                timer += 1
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_screen = False
                    pygame.quit()
                    break
            pygame.init()
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_UP] or keys[pygame.K_w]):
                if (player_rect.top > 72):
                    player_rect.centery -= player_velocity
              
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                if (player_rect.bottom < WINDOW_HEIGHT):
                    player_rect.centery += player_velocity
                
                
            #setting working and moving food
            if food_rect.centerx < 0:
                food_choice = random.choice(food_list)
                food = pygame.image.load(food_choice)
                food_rect = food.get_rect()
                food_rect.centerx = WINDOW_WIDTH + BUFFER_DISTANCE
                food_rect.centery = random.randint(72+(food_rect.h//2), (WINDOW_HEIGHT - (food_rect.h//2)))
                if current_food != "treadmill.png":
                    self.lives -=1
                    food_velocity += 1
                    score_lives = score_title_font.render(f"lives: {self.lives}", True, pink_main)
                if self.lives <= 0:
                    game_screen = False
                    pygame.mixer.music.stop()
                    self.pause_screen
                    continue
            else:
                food_rect.centerx -= food_velocity   
            
            if player_rect.colliderect(food_rect):
                if current_food == "treadmill.png":
                    if self.lives > 0:
                        disgust_sound.play()
                        self.lives -= 2
                        score_lives = score_title_font.render(f"lives: {self.lives}", True, pink_main)
                    if self.lives <= 0:
                        game_screen = False
                        pygame.mixer.music.stop()
                        self.pause_screen
                        continue
            
                else:
                    eat_sound.play()
                    timer = 0
                    score += 100
                    score_title = score_title_font.render(f"Score: {score}", True, pink_main)
                    player_image = player_eat
                    food_velocity += 1
                food_choice = random.choice(food_list)
                food = pygame.image.load(food_choice)
                food_rect = food.get_rect()
                food_rect.centerx = WINDOW_WIDTH + BUFFER_DISTANCE
                food_rect.centery = random.randint(72+(food_rect.h//2), (WINDOW_HEIGHT - (food_rect.h//2)))

                
            
            display_surface.blit(score_lives, score_lives_rect)
            display_surface.blit(title_main, title_main_rect)
            display_surface.blit(score_title, score_title_rect)
            display_surface.blit(food, food_rect)
            display_surface.blit(player_image, player_rect)
            pygame.display.update()
            clock.tick(FPS)
        
            
    def pause_screen(self):
        self.lives = 5
        pygame.mixer.music.load("pause_screen_music.mp3")
        pygame.mixer.music.play()
        button = pygame.Rect(200,200,110,60)
        font = pygame.font.Font("Soda Cream.otf", 25)
        button_font = font.render("Try again", True, black)
        text_font = self.font.render("You didn't eat enough :(", True, pink_main)
        text_font_rect = text_font.get_rect()
        text_font_rect.centerx = (500)
        text_font_rect.centery = (button.y - 40)
        pause_screen = True
        display_surface.fill(white)
        while pause_screen:
            
            button = pygame.Rect(200,200,110,60)
            button.centerx = (500)
            for events in pygame.event.get():
                
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(events.pos):
                        pause_screen = False
                        display_surface.fill(white)
                        pygame.mixer.music.stop()
                        self.game_screen()
                        break

                elif events.type == pygame.QUIT:
                    pygame.quit()    
            
            a,b = pygame.mouse.get_pos()
            if button.x <= a <= button.x + 110 and button.y <= b <= button.y +60:
                pygame.draw.rect(display_surface,(pink_second),button )
            else:
                pygame.draw.rect(display_surface, (white),button)
        
            display_surface.blit(button_font,(button.x + 15, button.y + 15))
            display_surface.blit(text_font, text_font_rect)
            pygame.display.update()
            clock.tick(FPS)
                        
        
        
        