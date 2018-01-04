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
horse = {0:'horse1.png',1:'horse2.png',2:'horse4.png'}
cowboyspeed = 10
cowboy_forward = [cowboy['F1'],cowboy['F3'],cowboy['F2']]
cowboy_backward = [cowboy['B1'],cowboy['B3'],cowboy['B2']]
cowboy_left = [cowboy['L1'],cowboy['L2'],cowboy['L1']]
cowboy_right = [cowboy['R1'],cowboy['R2'],cowboy['R1']]
cowboyImg = pygame.image.load (cowboy['Forward'])

selectorImg = pygame.image.load('selector.png')
selector_y = 195

townImg = pygame.image.load('town.png')
titleImg = pygame.image.load('title2.PNG')
menuImg = pygame.image.load('menu.png')
backgroundImg = titleImg

hotel_rx = 425
hotel_lx = 165
hotel_uy = -65
hotel_dy = 120
bank_rx = 530
bank_lx = 305
bank_uy = 200
bank_dy = 410
saloon_rx = 705
saloon_lx = 440
saloon_uy = -40
saloon_dy = 120
generalstore_rx = 830
generalstore_lx = 615
generalstore_uy = 190
generalstore_dy = 415
hardwarestore_rx = 920
hardwarestore_lx = 720
hardwarestore_uy = -55
hardwarestore_dy = 120

collision = False
a = 0
x = 0
back_x = -1200
back_y = 0
animationspeed = 2

moveUp = False
moveDown = False
moveLeft = False
moveRight = False
mD = True
mU = True
mR = True
mL = True
pressA = False

level = 0
pygame.init()
pygame.mixer.init()
if level == 0:
        
        pygame.mixer.music.load('BSTS.mp3')
        pygame.mixer.music.play()
else:
    pygame.mixer.music.load('BOBTK2.mp3')
    pygame.mixer.music.play()
 
# Set the width and height of the screen [width, height]
size = (1175, 600)
fullscreen = False
if fullscreen == True: screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
else: screen = pygame.display.set_mode(size)

pygame.display.set_caption("Cowboy")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#-------- Main Program Loop ----------
while not done:
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            done = True

        elif event.type == KEYDOWN:
            if event.key in (K_UP,K_w):
                if mU == True:
                    moveDown = False
                    moveUp = True
                    moveRight = False
                    moveLeft = False
                    mD = True
                    mU = True
                    mR = True
                    mL = True
            elif event.key in (K_DOWN,K_s):
                if mD == True:
                    moveUp = False
                    moveDown = True
                    moveRight = False
                    moveLeft = False
                    mD = True
                    mU = True
                    mR = True
                    mL = True
            elif event.key in (K_LEFT,K_a):
                if mL == True:
                    moveUp = False
                    moveDown = False
                    moveRight = False
                    moveLeft = True
                    mD = True
                    mU = True
                    mR = True
                    mL = True
            elif event.key in (K_RIGHT,K_d):
                if mR == True:
                    moveUp = False
                    moveDown = False
                    moveLeft = False
                    moveRight = True
                    mD = True
                    mU = True
                    mR = True
                    mL = True

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

            elif event.key == K_RETURN and selector_y == 195 and level == 0:
                level = 1
                cowboyImg = pygame.image.load (cowboy['Forward'])
                cowboy_x = 600
                cowboy_y = 300
                pygame.mixer.music.stop
                pygame.mixer.music.load('BOBTK2.mp3')
                pygame.mixer.music.play()
                
    # --- Game logic should go here
    if level == 0:
        animationspeed = 10
    if level == 1:
        animationspeed = 5

    if x == animationspeed:
        a += 1
        x = 0
    x += 1

    if level == 0:
        cowboyImg = pygame.image.load(horse[a])
        cowboy_x = 500
        cowboy_y = 400
        if moveUp == True and selector_y >= 150:
                selector_y -= 75
                clock.tick(10)
        if moveDown == True and selector_y <= 350:
                selector_y += 75
                clock.tick(10)
        
    else:
        if cowboy_x <= bank_rx and cowboy_x >= bank_lx and cowboy_y >= bank_uy and cowboy_y <= bank_dy:
            collision = True
        elif cowboy_x <= hotel_rx and cowboy_x >= hotel_lx and cowboy_y >= hotel_uy and cowboy_y <= hotel_dy:
            collision = True
        elif cowboy_x <= saloon_rx and cowboy_x >= saloon_lx and cowboy_y >= saloon_uy and cowboy_y <= saloon_dy:
            collision = True
        elif cowboy_x <= generalstore_rx and cowboy_x >= generalstore_lx and cowboy_y >= generalstore_uy and cowboy_y <= generalstore_dy:
            collision = True
        elif cowboy_x <= hardwarestore_rx and cowboy_x >= hardwarestore_lx and cowboy_y >= hardwarestore_uy and cowboy_y <= hardwarestore_dy:
            collision = True
        
        else:
            collision = False

        if collision == True:
            if moveLeft == True:
                cowboy_x += 10
                mL= False
                moveLeft = False
                
            if moveRight == True:
                mR = False
                moveRight = False
                cowboy_x -= 10
            if moveUp == True:
                mU = False
                moveUp = False
                cowboy_y += 10
            if moveDown == True:
                mD = False
                moveDown = False
                cowboy_y -= 10

        if moveLeft == True:
            cowboyImg = pygame.image.load(cowboy_left[a])
            cowboy_x -= cowboyspeed
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
    if level == 0:
        back_x +=1
        backgroundImg = titleImg
        screen.blit(backgroundImg, (back_x,back_y))
        screen.blit(backgroundImg, (back_x - 2290,back_y))
        screen.blit(backgroundImg, (back_x - 2290 * 2,back_y))
        screen.blit(backgroundImg, (back_x - 2290 * 3,back_y))
        screen.blit(backgroundImg, (back_x - 2290 * 4,back_y))
        screen.blit(menuImg, (cowboy_x - 105,100))
        screen.blit(selectorImg,(cowboy_x - 45, selector_y))
        
    else:
        backgroundImg = townImg
        screen.blit(backgroundImg,(0,0))
        #print(cowboy_y)
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

