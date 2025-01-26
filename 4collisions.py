from tkinter import CENTER
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
textfont = pygame.font.Font(None, 50)

grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()

sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
textsurface = textfont.render("Score", True, "red")
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

    screen.blit(textsurface,text_rect)
    screen.blit(playersurface, player_rect)

    snail_rect.right -= 4
    if(snail_rect.right < 0):
        snail_rect.right = 800
    screen.blit(snail, snail_rect)

    # this is the main part if hte collision
    # the methood given bellow triggers the collision multiple times
    if player_rect.colliderect(snail_rect):
        snail_rect.right = 800

    # the collide point method can be used to interact with mouse

    # Methdod 1 - using pygame.mouse
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
        
    #     if pygame.mouse.get_pressed() == (True, False, False):# here the tuple correspondsa to the valuse of left , middle,right mouse buttons
    #         player_rect.top = 0
            # lol this is  something funny

    pygame.display.update()

    clock.tick(60)
