import pygame
import random
from pygame.locals import *

#Pygame Initialization
pygame.init()

#Colours used in game
green = (57,255,20)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
orange = (225,150,0)
red = (178,34,34)
grey = (169,169,169)

#Window Size
size = [1000,820]
screen = pygame.display.set_mode(size)

#Fonts used in Game
nums_disp = pygame.font.SysFont("aerial",75)
end_page = pygame.font.SysFont("aerial",175)
    
#Clock is used to control the key pressed per second
clock = pygame.time.Clock()

timer = 1000
end = False
while not end:
    win_page = end_page.render("You Win!!! :D",True,black)
    
    screen.blit(win_page,(100,325))
    timer -= 1
    if timer == 0:
        end = True
    pygame.display.flip()
    screen.fill(white)
pygame.quit()
