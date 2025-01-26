import pygame
from sys import exit
from random import randint , choice

# The sprite class --> has a susrface and own rectangle
class Player(pygame.sprite.Sprite):
    health = 3
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
        global fire_state
        keys = pygame.key.get_pressed() # gives us all the keys pressed in input
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity=-20
        if keys[pygame.K_RIGHT] and self.rect.right<800:
            self.rect.x+=5
        if keys[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x-=5 
            
        # LOOOOOOL LOOOOOOL LOOOOOOOOL LOOOOOOOOL LOOOOOOOL
        if ((keys[pygame.K_g] and keys[pygame.K_o]) and keys[pygame.K_d] ): #LOL!!!!!LOL!!!
            Player.health = 100000;
            
        if keys[pygame.K_LCTRL] and level_cursor==2 and fire_state==1:
            projectiles_group.add(projectiles(self.rect.x,self.rect.y+30))
            fire_state=0
            
    
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
        self.detroy()
        self.animation_state()
        self.rect.x-=6
        
    def detroy(self):
        if  self.rect.x <= -100:
            self.kill()

class items(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type =='gem':
            gem = pygame.image.load('tools/graphics/gem.png').convert_alpha()
            self.frame = gem
        else:
            coin = pygame.image.load('tools/graphics/coin.png').convert_alpha()
            self.frame = coin
        
        self.image = self.frame
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),150))
    
    def update(self):
        self.rect.x -= 5
    
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
            
class Boss(pygame.sprite.Sprite):
    health = 1000
    def __init__(self):
        super().__init__()
        # Attacking 
        boss_att_1 = pygame.image.load('tools/char/Bringer-of-Death_Attack_1.png').convert_alpha()
        boss_att_2 = pygame.image.load('tools/char/Bringer-of-Death_Attack_2.png').convert_alpha()
        boss_att_3 = pygame.image.load('tools/char/Bringer-of-Death_Attack_3.png').convert_alpha()
        boss_att_4 = pygame.image.load('tools/char/Bringer-of-Death_Attack_4.png').convert_alpha()
        boss_att_5 = pygame.image.load('tools/char/Bringer-of-Death_Attack_5.png').convert_alpha()
        boss_att_6 = pygame.image.load('tools/char/Bringer-of-Death_Attack_6.png').convert_alpha()
        boss_att_7 = pygame.image.load('tools/char/Bringer-of-Death_Attack_7.png').convert_alpha()
        boss_att_8 = pygame.image.load('tools/char/Bringer-of-Death_Attack_8.png').convert_alpha()
        boss_att_9 = pygame.image.load('tools/char/Bringer-of-Death_Attack_9.png').convert_alpha()
        
        boss_att_1 = pygame.transform.scale2x(boss_att_1)
        boss_att_2 = pygame.transform.scale2x(boss_att_2)
        boss_att_3 = pygame.transform.scale2x(boss_att_3)
        boss_att_4 = pygame.transform.scale2x(boss_att_4)
        boss_att_5 = pygame.transform.scale2x(boss_att_5)
        boss_att_6 = pygame.transform.scale2x(boss_att_6)
        boss_att_7 = pygame.transform.scale2x(boss_att_7)
        boss_att_8 = pygame.transform.scale2x(boss_att_8)
        boss_att_9 = pygame.transform.scale2x(boss_att_9)
        
        # Walking 
        boss_walk_1 = pygame.image.load('tools/char/Bringer-of-Death_Walk_1.png').convert_alpha()
        boss_walk_2 = pygame.image.load('tools/char/Bringer-of-Death_Walk_2.png').convert_alpha()
        boss_walk_3 = pygame.image.load('tools/char/Bringer-of-Death_Walk_3.png').convert_alpha()
        boss_walk_4 = pygame.image.load('tools/char/Bringer-of-Death_Walk_4.png').convert_alpha()
        boss_walk_5 = pygame.image.load('tools/char/Bringer-of-Death_Walk_5.png').convert_alpha()
        boss_walk_6 = pygame.image.load('tools/char/Bringer-of-Death_Walk_6.png').convert_alpha()
        boss_walk_7 = pygame.image.load('tools/char/Bringer-of-Death_Walk_7.png').convert_alpha()
        boss_walk_8 = pygame.image.load('tools/char/Bringer-of-Death_Walk_8.png').convert_alpha()
        
        boss_walk_1 = pygame.transform.scale2x(boss_walk_1)
        boss_walk_2 = pygame.transform.scale2x(boss_walk_2)
        boss_walk_3 = pygame.transform.scale2x(boss_walk_3)
        boss_walk_4 = pygame.transform.scale2x(boss_walk_4)
        boss_walk_5 = pygame.transform.scale2x(boss_walk_5)
        boss_walk_6 = pygame.transform.scale2x(boss_walk_6)
        boss_walk_7 = pygame.transform.scale2x(boss_walk_7)
        boss_walk_8 = pygame.transform.scale2x(boss_walk_8)
        
        # Waiting
        boss_Idle_1 = pygame.image.load('tools/char/Bringer-of-Death_Idle_1.png').convert_alpha()
        boss_Idle_2 = pygame.image.load('tools/char/Bringer-of-Death_Idle_2.png').convert_alpha()
        boss_Idle_3 = pygame.image.load('tools/char/Bringer-of-Death_Idle_3.png').convert_alpha()
        boss_Idle_4 = pygame.image.load('tools/char/Bringer-of-Death_Idle_4.png').convert_alpha()
        boss_Idle_5 = pygame.image.load('tools/char/Bringer-of-Death_Idle_5.png').convert_alpha()
        boss_Idle_6 = pygame.image.load('tools/char/Bringer-of-Death_Idle_6.png').convert_alpha()
        boss_Idle_7 = pygame.image.load('tools/char/Bringer-of-Death_Idle_7.png').convert_alpha()
        boss_Idle_8 = pygame.image.load('tools/char/Bringer-of-Death_Idle_8.png').convert_alpha()
        
        boss_Idle_1 = pygame.transform.scale2x(boss_Idle_1)
        boss_Idle_2 = pygame.transform.scale2x(boss_Idle_2)
        boss_Idle_3 = pygame.transform.scale2x(boss_Idle_3)
        boss_Idle_4 = pygame.transform.scale2x(boss_Idle_4)
        boss_Idle_5 = pygame.transform.scale2x(boss_Idle_5)
        boss_Idle_6 = pygame.transform.scale2x(boss_Idle_6)
        boss_Idle_7 = pygame.transform.scale2x(boss_Idle_7)
        boss_Idle_8 = pygame.transform.scale2x(boss_Idle_8)
        
        self.boss_index = 0
        self.boss_att=[ boss_att_1, boss_att_2, boss_att_3, boss_att_4, boss_att_5, boss_att_6, boss_att_7, boss_att_8, boss_att_9]
        self.boss_walk=[ boss_walk_1, boss_walk_2, boss_walk_3, boss_walk_4, boss_walk_5, boss_walk_6, boss_walk_7, boss_walk_8]
        self.boss_Idle=[ boss_Idle_1, boss_Idle_2, boss_Idle_3, boss_Idle_4, boss_Idle_5, boss_Idle_6, boss_Idle_7, boss_Idle_8]
        self.image = self.boss_att[self.boss_index]
        self.rect = self.image.get_rect(midbottom=(650,300))
        
        
    def walkanimation(self):
        self.boss_index += 0.2
        if self.boss_index >=len(self.boss_walk):
            self.boss_index = 0
        self.image = self.boss_walk[int(self.boss_index)]
        self.rect.x -=3
        if self.rect.x < 0:
            self.rect.x = 650
    
    def attackanimation(self):
           
        self.boss_index += 0.2
        if self.boss_index >=len(self.boss_att):
            self.boss_index = 0
        self.image = self.boss_att[int(self.boss_index)]
        
    def waitanimation(self):
        self.boss_index += 0.2
        if self.boss_index >=len(self.boss_Idle):
            self.boss_index = 0
        self.image = self.boss_Idle[int(self.boss_index)]
               
    def update(self):
        if state ==1:
            self.walkanimation()
        elif state ==2 :
            self.attackanimation()
        elif state == 3:
            self.waitanimation()                     

class projectiles(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        fire_1 = pygame.image.load("tools/projectiles/projectile1.png").convert_alpha()
        fire_2 = pygame.image.load("tools/projectiles/projectile2.png").convert_alpha()
        fire_3 = pygame.image.load("tools/projectiles/projectile3.png").convert_alpha()
        fire_4 = pygame.image.load("tools/projectiles/projectile4.png").convert_alpha()
        fire_5 = pygame.image.load("tools/projectiles/projectile5.png").convert_alpha()
        fire_6 = pygame.image.load("tools/projectiles/projectile6.png").convert_alpha()
        fire_7 = pygame.image.load("tools/projectiles/projectile7.png").convert_alpha()
        fire_8 = pygame.image.load("tools/projectiles/projectile8.png").convert_alpha()
        fire_9 = pygame.image.load("tools/projectiles/projectile9.png").convert_alpha()
        
        fire_1 = pygame.transform.scale2x(fire_1)
        fire_2 = pygame.transform.scale2x(fire_2)
        fire_3 = pygame.transform.scale2x(fire_3)
        fire_4 = pygame.transform.scale2x(fire_4)
        fire_5 = pygame.transform.scale2x(fire_5)
        fire_6 = pygame.transform.scale2x(fire_6)
        fire_7 = pygame.transform.scale2x(fire_7)
        fire_8 = pygame.transform.scale2x(fire_8)
        fire_9 = pygame.transform.scale2x(fire_9)
        
        self.fire = [fire_1,fire_2,fire_3,fire_4,fire_5,fire_6,fire_7,fire_8,fire_9]
        self.index = 0
        self.image = self.fire[self.index]
        self.rect = self.image.get_rect(midbottom = (x,y))
        
    def animation(self):
        self.index +=0.1
        if self.index >= len(self.fire) : self.index = 0
        self.image = self.fire[int(self.index)]
    
    def update(self):
        self.detroy()
        self.animation()
        self.rect.x +=5
    
    def detroy(self):
        if  self.rect.x > 800:
            self.kill()
                   
# This function gets us our score
def display_score():
    global score_withitems
    curr_time = pygame.time.get_ticks()//1000 - start_time + score_withitems
    score_text = textfont.render("Score " + f'{curr_time}', True, (64, 64, 64))
    score_rect = score_text.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_text, score_rect)
    return curr_time

# This function checks the collisions  
def collision_sprite():

    if pygame.sprite.spritecollide(player.sprite,items_group,True):
        global score_withitems
        score_withitems += 5
    
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,True): # if set to true , every time an obstacle collides with player then obstacle will be deleted
        Player.health -=1
        if Player.health<=0:
            obstacle_group.empty()
            items_group.empty()
            player.empty()
            Player.health = 3
            return False
        else:
            return True
    else:
        return True

def healthsystem(health):
    heart = pygame.image.load("tools/graphics/health.png").convert_alpha()
    heart_rect1 = heart.get_rect(midbottom = (750,60))
    heart_rect2 = heart.get_rect(midbottom = (700,60))
    heart_rect3 = heart.get_rect(midbottom = (650,60))
    heart_rect4 = heart.get_rect(midbottom = (600,60))
    heart_rect5 = heart.get_rect(midbottom = (550,60))
    
    if health == 3:
        screen.blit(heart,heart_rect1)
        screen.blit(heart,heart_rect2)
        screen.blit(heart,heart_rect3)
    elif health == 2:
        screen.blit(heart,heart_rect1)
        screen.blit(heart,heart_rect2)
    elif health == 1:
        screen.blit(heart,heart_rect1)

def boss_collision():
    if pygame.sprite.collide_rect(player.sprite,boss.sprite):
        Player.health -=1;
        
    if Player.health <=0:
        global level_cursor,game_Active
        game_Active=False
        level_cursor =4
        return False
    else:
        return True

def projectile_collision():
    if pygame.sprite.spritecollide(boss.sprite,projectiles_group,True):
        Boss.health -=30
    if Boss.health <=0:
        global level_cursor ,game_Active
        game_Active=False
        level_cursor =3
        return False
    else :
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
boss_music = pygame.mixer.Sound('tools/music/boss_music.mp3')
boss_sound = pygame.mixer.Sound('tools/music/boss_sound.WAV')

# Game Status
game_Active = False
state = 3

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

# Level 2 Start Screen
level2_surf = textfont.render("CONGRATULATIONS !!!", True, (111, 196, 189))
level2_rect = level2_surf.get_rect(center=(400, 80))
player_stand = pygame.image.load("tools/char/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
level2_message = textfont.render("Press Space to Start LEVEL 2", True, (111, 196, 189))
level2_message_rect = level2_message.get_rect(center=(400, 320))

#LEVEL 2
level_cursor=0
level2_bg = pygame.image.load("tools/graphics/level2_bg.jpg").convert_alpha()
level2_font = pygame.font.Font("tools/font/Zabdilus.ttf",45)
player_name_surf = level2_font.render("Pixel BOY", True,"red") 
player_name_rect = player_name_surf.get_rect( midbottom =(150,70))
boss_name_surf = level2_font.render("Bringer-of-Death", True,"red") 
boss_name_rect = boss_name_surf.get_rect( midbottom =(650,70))

#LEVEL 2 END SCREEN WINNING
level2_surf_win = textfont.render("CONGRATULATIONS !!!", True, (111, 196, 189))
level2_rect_win = level2_surf_win.get_rect(center=(400, 80))
level2_message_win = textfont.render("!!!!!!!!!! You WON !!!!!!!", True, (111, 196, 189))
level2_message_rect_win = level2_message_win.get_rect(center=(400, 320))

#LEVEL 2 END SCREEN LOSING
level2_surf_loose = textfont.render("! HAHAHA !", True, (111, 196, 189))
level2_rect_loose = level2_surf_loose.get_rect(center=(400, 80))
level2_message_loose = textfont.render("! YOU LOSE!", True, (111, 196, 189))
level2_message_rect_loose = level2_message_loose.get_rect(center=(400, 320))
boss_stand = pygame.image.load('tools/char/Bringer-of-Death_Idle_1.png').convert_alpha()
boss_stand = pygame.transform.rotozoom(boss_stand,0,3)
boss_stand_rect = boss_stand.get_rect(center = (400,150))

# Obstacles
obstacle_group = pygame.sprite.Group()

# Player
player = pygame.sprite.GroupSingle()
player_score = 0

#BOSS
boss = pygame.sprite.GroupSingle()
boss.add(Boss())

# Items
items_group = pygame.sprite.Group()
score_withitems=0

#projectiles
projectiles_group = pygame.sprite.Group()
fire_state = 0

# Timer for better game logic
# +1 is imp as events are also reserved by pygame for some special events
obstalce_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstalce_timer, 900)

items_timer = pygame.USEREVENT+2
pygame.time.set_timer(items_timer, 900)

boss_timer = pygame.USEREVENT+3
pygame.time.set_timer(boss_timer, 500)

fire_timer = pygame.USEREVENT+4
pygame.time.set_timer(fire_timer, 500)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_Active==False:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_Active = True
                start_time = pygame.time.get_ticks()//1000
                score_withitems = 0 
                player.add(Player())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_Active = True
                    start_time = pygame.time.get_ticks()//1000
                    score_withitems = 0
                    player.add(Player())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and level_cursor == 1:
                    game_Active = True
                    level_cursor = 2
                    bg_music.stop()
                    boss_music.play(loops = -1)
                    boss_sound.play(loops = 0)
                    Player.health = 1000
                elif event.key == pygame.K_SPACE and level_cursor==4:
                    game_Active=True
                    level_cursor =2
                    Player.health = 1000
                    Boss.health = 1000
                    
                    
        if game_Active:
            
            if event.type == obstalce_timer:
                obstacle_group.add(Obstacle(choice(['snail','snail','fly'])))
                
            if event.type == items_timer:
                items_group.add(items(choice(['coin','coin','coin','gem'])))
            
            if event.type == boss_timer:
                state = choice([1,2,3])
            
            if event.type == fire_timer:
                fire_state =1
            
        
    if game_Active and level_cursor==0:
        screen.blit(sky, (0, 0))
        screen.blit(grasssurface, (0, 300))
        player_score = display_score()

        # Player
        player.draw(screen) # 1st main function of sprite class 
        player.update() # 2nd main function of sprite class

        # Obstacle
        obstacle_group.draw(screen)
        obstacle_group.update()
        healthsystem(Player.health)
        
        #Items 
        items_group.draw(screen)
        items_group.update()
        # Collision
        game_Active = collision_sprite()
        if player_score > 25:
            level_cursor =1
        

    elif level_cursor == 0:
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(restart_surf, restart_rect)

        if player_score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            game_score = textfont.render("Score "+f'{player_score}', True, (111, 196, 189))
            game_score_rect = game_score.get_rect(center=(400, 320))
            screen.blit(game_score, game_score_rect)

    if game_Active and level_cursor == 1 :
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(level2_surf, level2_rect)
        screen.blit(level2_message, level2_message_rect)
        game_Active = False
        

    if game_Active and level_cursor == 2 :
         
        screen.blit(level2_bg, (0, 0))
        screen.blit(grasssurface, (0, 300))
        screen.blit(player_name_surf,player_name_rect)
        screen.blit(boss_name_surf,boss_name_rect)
        
        player.draw(screen) 
        player.update()
        
        boss.draw(screen)
        boss.update()
        
        projectiles_group.draw(screen)
        projectiles_group.update()
        
        projectile_collision()
        if game_Active:
            boss_collision()
        
        pygame.draw.rect(screen,(128, 0, 0),pygame.draw.line(screen,"red",(20,20),(Player.health//3,20),20),5)
        pygame.draw.rect(screen,(128, 0, 0),pygame.draw.line(screen,(77, 12, 90 ),(450,20),(450+Boss.health//3,20),20),5)
    
    if game_Active == False and level_cursor ==3:
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(level2_message_win,level2_message_rect_win)
        screen.blit(level2_surf_win,level2_rect_win)
        
    if game_Active == False and level_cursor ==4:
        screen.fill("#c0e8ec")
        screen.blit(boss_stand,boss_stand_rect)
        screen.blit(level2_message_loose,level2_message_rect_loose)
        screen.blit(level2_surf_loose,level2_rect_loose)
        
        
    pygame.display.update()
    clock.tick(60)