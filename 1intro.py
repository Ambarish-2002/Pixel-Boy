import pygame
from sys import exit
pygame.init() # necessary to initate all the components

# now we hsould create a display surface.
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption("Game of Life") # title of the window
clock=pygame.time.Clock() # this is a clock object , ui tink it will work like a clock for memory and all the think i learned in CAO

#testsurface=pygame.Surface((200,200)) # take in widht and height
grasssurface = pygame.image.load("tools/graphics/grass.png")
sky = pygame.image.load("tools/graphics/sky.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit is opposite to inti.
            exit() # this closes everyhting including the loop and the progtma itself
            
    screen.blit(sky,(0,0))
    screen.blit(grasssurface,(0,250)) # block image treansfer blit(surafce ,position )
    #draw all elements
    #update everything
    # this is the main event loop
    pygame.display.update()
    #FPS IS fixed to 60 with this command
    clock.tick(60) # This is telling pygame that the while loop should not run faster than 60 fps.


