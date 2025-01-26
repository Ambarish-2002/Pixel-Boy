from tkinter import CENTER
import pygame
from sys import exit

import pygments
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
textfont = pygame.font.Font(None, 50)

grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()

sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
textsurface = textfont.render("Score", True,(64,64,64))
text_rect=textsurface.get_rect(center= (400,50))

snail = pygame.image.load("tools/char/snail1.png").convert_alpha()
snail_rect = snail.get_rect(bottomright=(800, 250))

playersurface = pygame.image.load(
    "tools/char/player_stand.png").convert_alpha()
# creating rectangles

player_rect = playersurface.get_rect(midbottom=(100, 250))
player_cursor=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos) and (player_cursor == 0):
                player_rect.top = 50
                player_cursor=1
            elif player_rect.collidepoint(event.pos) and (player_cursor == 1):
                player_rect.bottom = 250
                player_cursor=0
                
            

    screen.blit(sky, (0, 0))
    screen.blit(grasssurface, (0, 250))
    
    pygame.draw.rect(screen,"#c0e8ec",text_rect)
    pygame.draw.rect(screen,"#c0e8ec",text_rect,10) # refer to the draw docs for in detial info
    #pygame.draw.line(screen,"gold",(0,0),pygame.mouse.get_pos(),20)
    #pygame.draw.ellipse(screen,"brown",pygame.Rect(50,200,100,100))
    
    
    screen.blit(textsurface,text_rect)
    screen.blit(playersurface, player_rect)

    snail_rect.right -= 4
    if(snail_rect.right < 0):
        snail_rect.right = 800
    screen.blit(snail, snail_rect)


    if player_rect.colliderect(snail_rect):
        snail_rect.right = 800
        
    pygame.display.update()

    clock.tick(60)