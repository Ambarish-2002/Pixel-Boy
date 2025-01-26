import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game of Life") 
clock=pygame.time.Clock() 
testfont= pygame.font.Font(None,50)

grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()  

sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
textsurface= testfont.render("Score", True,"red")  

snail = pygame.image.load("tools/char/snail1.png").convert_alpha()
snail_rect = snail.get_rect(bottomright = (800,250))

playersurface=pygame.image.load("tools/char/player_stand.png").convert_alpha()
# creating rectangles
 
player_rect = playersurface.get_rect(midbottom =(100,250) )
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    screen.blit(sky,(0,0))
    screen.blit(grasssurface,(0,250))
    
    screen.blit(textsurface,(0,0))
    # here we have used the player rectangles 
    # herer we move the rectangle instead of the player . 
    #player_rect.left += 1
    screen.blit(playersurface,player_rect)
    #print(player_rect.left)
    
    snail_rect.right-=4
    if(snail_rect.right<0):
        snail_rect.right =800
    
    screen.blit(snail,snail_rect) 
    
    pygame.display.update()
    
    clock.tick(60) 