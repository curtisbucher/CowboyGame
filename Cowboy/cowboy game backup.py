"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame, sys
from pygame.locals import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SAND = (245,216,130)

cowboy_x = 100
cowboy_y = 100
cowboy = {'F1':'For1.png','F2':'For2.png','F3': 'For3.png',
          'B1':'Back1.png','B2':'Back2.png','B3':'Back3.png',
          'L1':'Left1.png','L2':'Left2.png',
          'R1':'Right1.png','R2':'Right2.png',
          'Forward':'cowboy_forward.png','Backward':'cowboy_backward.png',
          'Shoot_Left':'shoot_left.png','Shoot_Right':'shoot_right.png'}
cowboyspeed = 10
cowboy_forward = [cowboy['F1'],cowboy['F3'],cowboy['F2']]
cowboy_backward = [cowboy['B1'],cowboy['B3'],cowboy['B2']]
cowboy_left = [cowboy['L1'],cowboy['L2'],cowboy['L1']]
cowboy_right = [cowboy['R1'],cowboy['R2'],cowboy['R1']]
cowboyImg = pygame.image.load (cowboy['Forward'])
townImg = pygame.image.load('town.png')
backgroundImg = townImg
a = 0
x = 0
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('BOBTK2.mp3')
pygame.mixer.music.play()
 
# Set the width and height of the screen [width, height]
size = (1175, 600)
fullscreen = True

if fullscreen == True: screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
else: screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------

while not done:
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            done = True

        elif event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                moveDown = False
                moveUp = True
                moveRight = False
                moveLeft = False
            elif event.key in (K_DOWN, K_s):
                moveUp = False
                moveDown = True
                moveRight = False
                moveLeft = False
            elif event.key in (K_LEFT, K_a):
                moveUp = False
                moveDown = False
                moveRight = False
                moveLeft = True
            elif event.key in (K_RIGHT, K_d):
                moveUp = False
                moveDown = False
                moveLeft = False
                moveRight = True

        elif event.type == KEYUP:
            # stop moving the player's cat
            if event.key in (K_LEFT, K_a):
                moveLeft = False
                cowboyImg = pygame.image.load(cowboy['L2'])
            elif event.key in (K_RIGHT, K_d):
                moveRight = False
                cowboyImg = pygame.image.load(cowboy['R2'])
            elif event.key in (K_UP, K_w):
                moveUp = False
                cowboyImg = pygame.image.load(cowboy['Backward'])
            elif event.key in (K_DOWN, K_s):
                moveDown = False
                cowboyImg = pygame.image.load(cowboy['Forward'])

            elif event.key == K_ESCAPE:
                pygame.quit()
    # --- Game logic should go here
    x += 1
    if x == 2:
        a += 1
        x = 0
    if moveLeft == True:
        cowboy_x -= cowboyspeed
        cowboyImg = pygame.image.load(cowboy_left[a])
    if moveRight == True:
        cowboy_x += cowboyspeed
        cowboyImg = pygame.image.load(cowboy_right[a])
    if moveUp == True:
        cowboy_y -= cowboyspeed
        cowboyImg = pygame.image.load(cowboy_backward[a])
    if moveDown == True:
        cowboy_y += cowboyspeed
        cowboyImg = pygame.image.load(cowboy_forward[a])
    # --- Screen-clearing code goes here
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(backgroundImg,(0,0))
 
    # --- Drawing code should go here
    screen.blit(cowboyImg, (cowboy_x, cowboy_y))
    if a == 2:
        a = 0
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()

