#Python Ver : 2.7.14
#Pygame Ver : 1.9.3

background_image_filename = 'AA.jpg'
sprite_image_filename = 'Ball.png'
wall = 'Wall.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1280, 720), 0, 0)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
wall1 = pygame.image.load(wall).convert_alpha()
wall2 = pygame.image.load(wall).convert_alpha()

clock = pygame.time.Clock()

x, y = 100, 100
speedx, speedy = 200, 200

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    screen.blit(sprite, (x, y))
    screen.blit(wall1, (50, 280))
    screen.blit(wall2, (1160, 280))


    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    x += speedx * time_passed_seconds
    y += speedy * time_passed_seconds

    # If the sprite goes off the edge of the screen,
    # make it move in the opposite direction
    if x > 1280 - sprite.get_width():
        speedx = -speedx
        x = 1280 - sprite.get_width()
    elif x < 0:
        speedx = -speedx
        x = 0
    if y > 720 - sprite.get_height():
        speedy = -speedy
        y = 720 - sprite.get_height()
    elif y < 0:
        speedy = -speedy
        y = 0
    pygame.display.update()
