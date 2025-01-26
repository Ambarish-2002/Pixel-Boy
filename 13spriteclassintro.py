from numpy import true_divide
import pygame
from sys import exit
from random import randint , choice

# The sprite class --> has a susrface and own rectangle
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("tools/char/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("tools/char/player_walk_2.png").convert_alpha()
        self.player_jump = pygame.image.load("tools/char/player_jump.png")
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        
        self.image = self.player_walk[self.player_index]  # image and rect are always needed , else pygmae throws an error
        self.rect = self.image.get_rect(midbottom=(100,300))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('tools/music/player_jump.WAV')
        self.jump_sound.set_volume(0.75)
    
    def player_input(self):
        keys = pygame.key.get_pressed() # gives us all the keys pressed in input
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity=-20 
    
    def apply_gravity(self):
        self.gravity +=1
        self.rect.y+=self.gravity
        if self.rect.bottom >=300:
            self.rect.bottom = 300 
            
    def animation_state(self):
        if self.rect.bottom >300:
            self.image = self.player_jump
        else:
            self.player_index +=0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
           
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load("tools/char/fly1.png").convert_alpha()
            fly_2 = pygame.image.load("tools/char/fly2.png").convert_alpha()
            self.frames = [fly_1,fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load("tools/char/snail1.png").convert_alpha()
            snail_2 = pygame.image.load("tools/char/snail2.png").convert_alpha()
            self.frames =[snail_1,snail_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
        
    def animation_state(self):
        self.animation_index +=0.1
        if self.animation_index >= len(self.frames) : self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x-=6
        
    def detroy(self):
        if  self.rect.x <= -100:
            self.kill()
               
# This function gets us our score
def display_score():
    curr_time = pygame.time.get_ticks()//1000 - start_time
    score_text = textfont.render("Score " + f'{curr_time}', True, (64, 64, 64))
    score_rect = score_text.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_text, score_rect)
    return curr_time

# This function checks the collisions
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False): # if set to true , every time an obstacle collides with player then obstacle will be deleted
        obstacle_group.empty()
        return False
    else:
        return True
    
    
pygame.init()
start_time = 0
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()
textfont = pygame.font.Font(None, 50)
bg_music = pygame.mixer.Sound('tools/music/bg_music.WAV')
bg_music.set_volume(0.50)
bg_music.play(loops = -1 ) # this tells the pygame to loop this track forever

# Game Status
game_Active = False

# Background
textfont = pygame.font.Font(None, 50)
grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()
sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()


# Intro screen
restart_surf = textfont.render("Pixel Runner", True, (111, 196, 189))
restart_rect = restart_surf.get_rect(center=(400, 80))
player_stand = pygame.image.load("tools/char/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
game_message = textfont.render("Press Space to run", True, (111, 196, 189))
game_message_rect = game_message.get_rect(center=(400, 320))


# Obstacles
obstacle_group = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()
player.add(Player())
player_score = 0

# Timer for better game logic

# +1 is imp as events are also reserved by pygame for some special events
obstalce_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstalce_timer, 900)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_Active==False:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_Active = True
                start_time = pygame.time.get_ticks()//1000

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_Active = True
                    start_time = pygame.time.get_ticks()//1000
        
        if game_Active:
            
            if event.type == obstalce_timer:
                obstacle_group.add(Obstacle(choice(['snail','snail','fly'])))
            

    if game_Active:
        screen.blit(sky, (0, 0))
        screen.blit(grasssurface, (0, 300))
        player_score = display_score()

        # Player
        player.draw(screen) # 1st main function of sprite class 
        player.update() # 2nd main function of sprite class

        # Obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # Collision
        game_Active = collision_sprite()
        

    else:
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(restart_surf, restart_rect)
        

        if player_score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            game_score = textfont.render(
                "Score "+f'{player_score}', True, (111, 196, 189))
            game_score_rect = game_score.get_rect(center=(400, 320))
            screen.blit(game_score, game_score_rect)

    pygame.display.update()
    clock.tick(60)