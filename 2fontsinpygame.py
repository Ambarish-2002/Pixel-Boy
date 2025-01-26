import pygame
from sys import exit
pygame.init() 


screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Game of Life") 
clock=pygame.time.Clock() 
testfont= pygame.font.Font(None,50)  #FOnt(font tpye, font size)


grasssurface1 = pygame.image.load("tools/graphics/grass.png").convert_alpha()  # convert alpha is important as it helps the performance
grasssurface2 = pygame.image.load("tools/graphics/grass.png").convert_alpha()
grasssurface3 = pygame.image.load("tools/graphics/grass.png").convert_alpha()
sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
textsurface= testfont.render("Score", True,"red")  #(text,AA,color)

snail = pygame.image.load("tools/char/snail1.png").convert_alpha()

snail_pos=600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit() 
    screen.blit(sky,(0,0))
    screen.blit(grasssurface1,(0,250))
    screen.blit(grasssurface2,(300,250))
    screen.blit(grasssurface3,(600,250))
    screen.blit(textsurface,(0,0))
    
    snail_pos+=-5
    if(snail_pos<-50):
        snail_pos=600
    screen.blit(snail,(snail_pos,50)) 
    
    pygame.display.update()
    
    clock.tick(60) 
