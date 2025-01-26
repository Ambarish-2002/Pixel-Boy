import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()
textfont = pygame.font.Font(None, 50)

grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()

sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()
textsurface = textfont.render("Score", True, (64, 64, 64))
text_rect = textsurface.get_rect(center=(400, 50))

snail = pygame.image.load("tools/char/snail1.png").convert_alpha()
snail_rect = snail.get_rect(bottomright=(800, 300))

playersurface = pygame.image.load(
    "tools/char/player_stand.png").convert_alpha()


player_rect = playersurface.get_rect(midbottom=(100, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and (player_rect.bottom == 300):
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (player_rect.bottom == 300):
                player_gravity = -20
        

    screen.blit(sky, (0, 0))
    screen.blit(grasssurface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_rect)
    pygame.draw.rect(screen, "#c0e8ec", text_rect, 10)
    screen.blit(textsurface, text_rect)

    # Snail
    snail_rect.right -= 5
    if(snail_rect.right < 0):
        snail_rect.right = 800
    screen.blit(snail, snail_rect)

    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
    screen.blit(playersurface, player_rect)

    pygame.display.update()

    clock.tick(60)
