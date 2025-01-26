import pygame
from sys import exit
pygame.init()
start_time = 0

# This function gtes us our score
def display_score():
    curr_time=pygame.time.get_ticks()//1000 - start_time
    score_text= textfont.render("Score "+ f'{curr_time}', True, (64, 64, 64))
    score_rect = score_text.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_text,score_rect)
    return curr_time


screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()
textfont = pygame.font.Font(None, 50)

# Game Status
game_Active = False

# Background
textfont = pygame.font.Font(None, 50)
grasssurface = pygame.image.load("tools/graphics/grass.png").convert_alpha()
sky = pygame.image.load("tools/graphics/sky.png").convert_alpha()


# Intro screen
restart_surf = textfont.render("Pixel Runner", True,(111, 196, 189))
restart_rect = restart_surf.get_rect(center=(400, 80))
player_stand = pygame.image.load("tools/char/player_stand.png").convert_alpha()
#Scaling our player
#player_stand= pygame.transform.scale(player_stand,(150,100)) this is a crude method
#player_stand= pygame.transform.scale2x(player_stand) # this scales the item 2x
player_stand= pygame.transform.rotozoom(player_stand,0,2) # (surface,angle,scale)
player_stand_rect = player_stand.get_rect(center=(400, 200))
game_message = textfont.render("Press Space to run", True ,(111, 196, 189))
game_message_rect = game_message.get_rect(center=(400,320))



# Snail
snail = pygame.image.load("tools/char/snail1.png").convert_alpha()
snail_rect = snail.get_rect(bottomright=(800, 300))

# Player
playersurface = pygame.image.load("tools/char/player_stand.png").convert_alpha()
player_rect = playersurface.get_rect(midbottom=(100, 300))
player_gravity = 0
player_score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_Active:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and (player_rect.bottom == 300):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (player_rect.bottom == 300):
                    player_gravity = -20

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_Active = True
                start_time = pygame.time.get_ticks()//1000

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_Active = True
                    start_time = pygame.time.get_ticks()//1000

    if game_Active:
        
        screen.blit(sky, (0, 0))
        screen.blit(grasssurface, (0, 300))
        player_score=display_score()

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

        # If the snail collides with the player rect
        if player_rect.colliderect(snail_rect):
            game_Active = False

    else:
        screen.fill("#c0e8ec")
        screen.blit(player_stand,player_stand_rect)
        screen.blit(restart_surf,restart_rect)
        
        if player_score==0: 
            screen.blit(game_message,game_message_rect)
        else:
            game_score=textfont.render("Score "+f'{player_score}',True,(111, 196, 189))
            game_score_rect = game_score.get_rect(center=(400,320))
            screen.blit(game_score,game_score_rect)
        
        player_rect.midbottom = (100, 300)
        snail_rect.midbottom = (800, 300)

    pygame.display.update()
    clock.tick(60)
