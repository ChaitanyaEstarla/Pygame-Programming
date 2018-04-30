#Python Ver : 2.7.14
#Pygame Ver : 1.9.3

bluecar = 'bluecar.png'
redcar = 'redcar.png'

import pygame
import random
from pygame.locals import *

#Initialize Pygame
pygame.init()

#Colors for game
BLUE = (40,56,108)
WHITE = (255, 255, 255)

#defining screen size
size = [360,640]
screen = pygame.display.set_mode(size)

#Speeds for cars
speed = 500
speedb = 10

#Game name on the display bar
pygame.display.set_caption("Car Crash")

#Loading images
Blucar = pygame.image.load(bluecar).convert_alpha()
Redcar = pygame.image.load(redcar).convert_alpha()

#Initial positions of cars
#Blue car
a = random.randint(15,290)
b = 520
#Red car
y = -100
x = random.randint(15,290)

#No. of lives
life = 3

#Font for display
font = pygame.font.SysFont("aerial", 50)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Game components
    pressed_keys = pygame.key.get_pressed()
    screen.fill(BLUE)
    pygame.draw.line(screen, WHITE, (4,0),(4,640),9)
    pygame.draw.line(screen,WHITE, (355,0),(355,640),9)
    Life = font.render('Lives: '+str(life), True, WHITE)
    screen.blit(Life, (120,100))
    screen.blit(Blucar, (a,b))
    screen.blit(Redcar, (x,y))
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0


    #Additoin variable car speeds
    distance_moved = time_passed_seconds * speed
    distance_movedb = time_passed_seconds * speedb

    y +=distance_moved


    #If red car reaches 660 it's positon will be reset
    if y >= 660:
        y = -100
        x = random.randint(15,290)

    #Movement of Blue car
    if b >= 100:
        b -= distance_movedb
        
    
    #Right/Left movement for blue car
    if pressed_keys[K_LEFT] and a >= 10:
        a -= 0.15
    elif pressed_keys[K_RIGHT] and a <= 300:
        a += 0.15
        
    #Condtion for car hit
    if (((y+85) >= (b - 20) and (y+85) <= (b+20)) and (x >= (a-40) and x <= (a+40))):
        life -= 1
        y = -1000

        x = random.randint(15,290)
        if life == 0: 
            done = True
    pygame.display.update()

done =False
#Game over font at the end
Time = 5000
while not done:
    Time -= 1 
    screen.fill(BLUE)   
    Over = font.render('Game Over', True, WHITE)
    screen.blit(Over,(90,320))
    if Time == 0:
        done = True
    pygame.display.update()
pygame.quit()
