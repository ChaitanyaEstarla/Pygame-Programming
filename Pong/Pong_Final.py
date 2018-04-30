#Python Ver : 2.7.14
#Pygame Ver : 1.9.3

import pygame
import random
from pygame.locals import *


#Initialising Pygame
pygame.init()

#Diffrent colours predefned
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)


move=0

#Initialising the Screen and its size
size = [1280, 720]
screen = pygame.display.set_mode(size)

#Initial positons of the bars 
right = 360 
left = 360

#Speed of ball
speed = 250

#The name shown on the top bar
pygame.display.set_caption("Pong")

#Score Text Font
font = pygame.font.SysFont("arial", 50);

#Initial position of the ball
x = 640
y = random.randint(60,660)

#Initial Flags and score for the Players(Flag defines the direction of the ball)    
flagx = random.randint(0,1)
flagy = random.randint(0,1)
scorea = 0
scoreb = 0

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True

    #Rendering the Game Objects
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (30,0),(30,720), 1)
    pygame.draw.line(screen, WHITE, (640,0),(640,720), 1)
    pygame.draw.line(screen, WHITE, (1250,0),(1250,720), 1)
    pygame.draw.line(screen, RED, (1265,right-60),(1265,right+60), 31)
    pygame.draw.line(screen, RED, (15,left-60),(15,left+60), 31)
    pygame.draw.circle(screen, BLUE, (int(x),int(y)),30,0)
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    #Used for increment or decrement of ball coordinates to give it a moving effect
    #Speed variable defines the number of pixels it will cover per second
    distance_moved = time_passed_seconds * speed

    #Displaying Score
    playera = font.render(str(scorea), True, WHITE)
    screen.blit(playera, (320,100))

    playerb = font.render(str(scoreb), True, WHITE)
    screen.blit(playerb, (960,100))
    
    #if the ball reaches the last pixel of the Y axis on either side then the flag is changed
    # so that a bounce effect can be given 
    if y >= 690 or y <= 30:
        if flagy == 0:
            flagy = 1
        elif flagy == 1:
            flagy = 0

    #Key press functoin for movement of the bars

    #for right bar
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[K_UP] and right >= 60:
        move = -1
        right += move * speed * time_passed_seconds

    if pressed_keys[K_DOWN] and right < 660:
        move = +1
        right += move * speed * time_passed_seconds
    #for left bar
    if pressed_keys[K_w] and left >= 60:
        move = -1
        left += move * speed * time_passed_seconds

    if pressed_keys[K_s] and left < 660:
        move = +1
        left += move * speed * time_passed_seconds

    #Collision with the paddles
    if (x >= 1220 and (y >= (right-60) and y <= (right+60))) or (x <= 60 and (y >= (left-60) and y <= (left+60))):
        if flagx == 0:
            flagx = 1
        elif flagx == 1:
            flagx = 0
    
    #If the ball hits the bar either side it is reset and also the opposite player scores a point
    if x >= 1250:
        scorea += 1
        x = 640
        y = random.randint(60,660)
        flagx = 0
        flagy = 0

    if x <= 30:
        scoreb += 1
        x = 640
        y = random.randint(60,660)
        flagx = 1
        flagy = 1

    #Deciding directon of ball based on the flag       
    if flagx == 1:
        x +=distance_moved
    if flagx == 0:
        x -=distance_moved

    if flagy == 1:
        y +=distance_moved
    if flagy == 0:
        y -=distance_moved

    pygame.display.update()
pygame.quit()
