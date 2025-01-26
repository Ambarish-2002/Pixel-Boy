import pygame
from sys import exit
from random import randint


# This function gets us our score
def display_score():
    curr_time = pygame.time.get_ticks()//1000 - start_time
    score_text = textfont.render("Score " + f'{curr_time}', True, (64, 64, 64))
    score_rect = score_text.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    screen.blit(score_text, score_rect)
    return curr_time

# This function spawns enemies
def obstacle_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstalce_rect in obstacle_rect_list:
            obstalce_rect.x -= 5

            if obstalce_rect.bottom == 300:
                screen.blit(snail_surf, obstalce_rect)

            else:
                screen.blit(fly_surf, obstalce_rect)

        # this only gives us the obejects which have x >-50 to keep the list clean
        obstacle_rect_list = [
            obstacle for obstacle in obstacle_rect_list if obstacle.x > -100]
        return obstacle_rect_list
    else:
        return []

# This function detects collisions
def collisions(player, obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True

# This animates the player onto the surface
def player_animation():
    # Walking animation when player is on the ground and jumping when the player is jumping
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]
    

pygame.init()
start_time = 0
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
restart_surf = textfont.render("Pixel Runner", True, (111, 196, 189))
restart_rect = restart_surf.get_rect(center=(400, 80))
player_stand = pygame.image.load("tools/char/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))
game_message = textfont.render("Press Space to run", True, (111, 196, 189))
game_message_rect = game_message.get_rect(center=(400, 320))


# Obstacles
obstacle_rect_list = []
# -->Snails
snail_1 = pygame.image.load("tools/char/snail1.png").convert_alpha()
snail_2 = pygame.image.load("tools/char/snail2.png").convert_alpha()
snail_frames =[snail_1,snail_2]
snail_index=0
snail_surf=snail_frames[snail_index]
#--> FLy
fly_1 = pygame.image.load("tools/char/fly1.png").convert_alpha()
fly_2 = pygame.image.load("tools/char/fly2.png").convert_alpha()
fly_frames = [fly_1,fly_2]
fly_index=0
fly_surf=fly_frames[fly_index]

# Player

player_walk_1 = pygame.image.load(
    "tools/char/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load(
    "tools/char/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("tools/char/player_jump.png")
player_walk = [player_walk_1, player_walk_2]
player_index = 0

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(100, 300))
player_gravity = 0
player_score = 0

# Timer for better game logic

# +1 is imp as events are also reserved by pygame for some special events
obstalce_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstalce_timer, 1100)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 300)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


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

        if event.type == obstalce_timer:
            if randint(0, 3) % 2 == 0:
                obstacle_rect_list.append(snail_surf.get_rect(
                    bottomright=(randint(900, 1300), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(
                    bottomright=(randint(900, 1300), 100)))
                
        if event.type==snail_animation_timer and game_Active:
            snail_index+=1
            if snail_index >1:
                snail_index=0
            snail_surf=snail_frames[snail_index]
            
        if event.type==fly_animation_timer and game_Active:
            fly_index+=1
            if fly_index >1:
                fly_index=0
            fly_surf=fly_frames[fly_index]
            

    if game_Active:
        screen.blit(sky, (0, 0))
        screen.blit(grasssurface, (0, 300))
        player_score = display_score()

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle Movement
        obstacle_rect_list = obstacle_movement(
            obstacle_rect_list)  # Awesome method this !!!

        # Collision
        game_Active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill("#c0e8ec")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(restart_surf, restart_rect)
        obstacle_rect_list.clear()

        if player_score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            game_score = textfont.render(
                "Score "+f'{player_score}', True, (111, 196, 189))
            game_score_rect = game_score.get_rect(center=(400, 320))
            screen.blit(game_score, game_score_rect)

        player_rect.midbottom = (100, 300)
        player_gravity = 0

    pygame.display.update()
    clock.tick(60)
