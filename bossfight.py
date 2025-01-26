from random import randint
from random import choice
import pygame
from sys import exit
pygame.init()

class Boss(pygame.sprite.Sprite):
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
        if self.rect.x < 50:
            self.rect.midbottom = (650,300)
    
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
            
            
        
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game of Life") 
clock=pygame.time.Clock() 
testfont= pygame.font.Font(None,50)

grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()  

sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
player_stand=pygame.image.load("tools/char/player_stand.png").convert_alpha()
player_rect = player_stand.get_rect(midbottom =(100,300) )
player_gravity = 0
state = 0
boss = pygame.sprite.GroupSingle()
boss.add(Boss())


def player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player_rect.right<800:
        player_rect.x+=5
    if keys[pygame.K_LEFT] and player_rect.x>0:
        player_rect.x-=5
    if keys[pygame.K_SPACE] and player_rect.bottom>=300:
        global player_gravity
        player_gravity = -20       
  
boss_timer = pygame.USEREVENT+1
pygame.time.set_timer(boss_timer, 500)

 
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

        if event.type == boss_timer:
            state = choice([1,2,3])
            
            
    
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300 
    
    screen.blit(sky,(0,0))
    screen.blit(grasssurface,(0,300))
    boss.draw(screen)
    boss.update()
    player_movement()
    screen.blit(player_stand,player_rect)
    
    
    pygame.display.update()
    
    clock.tick(60)