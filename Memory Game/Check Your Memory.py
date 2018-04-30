#Python Ver : 2.7.14
#Pygame Ver : 1.9.3

import pygame
import random
#from pygame.locals import *

#Intializing Pygame
pygame.init()

#Colours used in the game
White  = (255, 255, 255)
Blue = (0,191,255)
Green = (50,205,50)
Black = (0,0,0)

#Define screen Size
size = [1600, 200]
screen = pygame.display.set_mode(size)

#Game Name
pygame.display.set_caption("Memory Game")

#Font for display
font = pygame.font.SysFont("aerial", 150)
fon = pygame.font.SysFont("aerial", 20)
fo = pygame.font.SysFont("aerial", 100)
f= pygame.font.SysFont("aerial", 50)

#Number list and shufflng them
Num = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
random.shuffle(Num)

#Variables to use for the card flipping 
Rec = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
Final = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
count = 0
i1 = 0
i2 = 0
Condt = 0
attempt = 0

#start screen
done = False
while not done:
    screen.fill(Green)
    condition = f.render('Try finishing in as less attempts as possible',True,White)
    screen.blit(condition,(450,150))
    Start = fo.render('Start',True,White)
    pygame.draw.line(screen,Blue,(780,50),(780,115),200)
    screen.blit(Start,(700,50))
    
    #When clicked on start button the game starts
    for event in  pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                Pos = pygame.mouse.get_pos()
                a = Pos[0]
                b = Pos[1]

                if (a >= 680 and a<= 880) and ( b>= 50 and b<= 115):
                    done = True
                
    pygame.display.update()


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Screen Colour
    screen.fill(Green)

    if Condt > 7:
            done = True
            
    #Drawing numbres on the screen
    j = 25
    for i in range(0,16):
        Number = font.render(str(Num[i]),True,White)
        screen.blit(Number,(j,50))
        j += 100
    
    #Drawing blue cards to hide numbers    
    j = 0
    for i in range(50,1650,100):
        if Rec[j] == False:
            pygame.draw.line(screen,Blue,(i,0),(i,200),100)
        j += 1

        Attempt = fon.render('Attempts : '+str(attempt),True,Black)
        screen.blit(Attempt,(1510,20))
    
        #Getting the mouse position and determining the box which is clicked
        for event in  pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                Pos = pygame.mouse.get_pos()
                
                if count == 2:
                    attempt += 1
                    if Num[i1] == Num[i2] and i1 != i2:
                        count = 0
                        Final[i1] = True
                        Final[i2] = True
                        Condt += 1
                        i1 = i2 = 0
                        
                    else:
                        if Final[i1] == True:
                            count = 0
                            Rec[i2] = False
                            i1 = i2 = 0
                        elif Final[i2] == True:
                            count = 0
                            Rec[i1] = False
                            i1 = i2 = 0
                        else:
                            count = 0
                            Rec[i1] = False
                            Rec[i2] = False
                            i1 = i2 = 0

                #Flipping the card on click
                if Pos[0] >=0 and Pos[0] <= 100:
                    Rec[0] = True
                    count += 1
                    if count == 1:
                        i2 = 0
                    else:
                        i1 = 0
                    
                
                if Pos[0] >= 100 and Pos[0] <= 200:
                    Rec[1] = True
                    count += 1
                    if count == 1:
                        i2 = 1
                    else:
                        i1 = 1
                    
                if Pos[0] >=200 and Pos[0] <= 300:
                    Rec[2] = True
                    count += 1
                    if count == 1:
                        i2 = 2
                    else:
                        i1 = 2
                    
                if Pos[0] >=300 and Pos[0] <= 400:
                    Rec[3] = True
                    count += 1
                    if count == 1:
                        i2 = 3
                    else:
                        i1 = 3
                    
                if Pos[0] >=400 and Pos[0] <= 500:
                    Rec[4] = True
                    count += 1
                    if count == 1:
                        i2 = 4
                    else:
                        i1 = 4
                    
                if Pos[0] >=500 and Pos[0] <= 600:
                    Rec[5] = True
                    count += 1
                    if count == 1:
                        i2 = 5
                    else:
                        i1 = 5
                    
                if Pos[0] >=600 and Pos[0] <= 700:
                    Rec[6] = True
                    count += 1
                    if count == 1:
                        i2 = 6
                    else:
                        i1 = 6
                    
                if Pos[0] >=700 and Pos[0] <= 800:
                    Rec[7] = True
                    count += 1
                    if count == 1:
                        i2 = 7
                    else:
                        i1 = 7
                    
                if Pos[0] >=800 and Pos[0] <= 900:
                    Rec[8] = True
                    count += 1
                    if count == 1:
                        i2 = 8
                    else:
                        i1 = 8
                    
                if Pos[0] >=900 and Pos[0] <= 1000:
                    Rec[9] = True
                    count += 1
                    if count == 1:
                        i2 = 9
                    else:
                        i1 = 9
                    
                if Pos[0] >=1000 and Pos[0] <= 1100:
                    Rec[10] = True
                    count += 1
                    if count == 1:
                        i2 = 10
                    else:
                        i1 = 10
                    
                if Pos[0] >=1100 and Pos[0] <= 1200:
                    Rec[11] = True
                    count += 1
                    if count == 1:
                        i2 = 11
                    else:
                        i1 = 11
                    
                if Pos[0] >=1200 and Pos[0] <= 1300:
                    Rec[12] = True
                    count += 1
                    if count == 1:
                        i2 = 12
                    else:
                        i1 = 12
                    
                if Pos[0] >=1300 and Pos[0] <= 1400:
                    Rec[13] = True
                    count += 1
                    if count == 1:
                        i2 = 13
                    else:
                        i1 = 13
                    
                if Pos[0] >=1400 and Pos[0] <= 1500:
                    Rec[14] = True
                    count += 1
                    if count == 1:
                        i2 = 14
                    else:
                        i1 = 14
                    
                if Pos[0] >=1500 and Pos[0] <= 1600:
                    Rec[15] = True
                    count += 1
                    if count == 1:
                        i2 = 15
                    else:
                        i1 = 15
 
    #Drawing lines to give the illusion of boxes
    for i in range(100,1600,100):
        pygame.draw.line(screen,White,(i,0),(i,200),1)

    pygame.display.update()
    
done = False
timer = 2000
#Final loop to show win and attempts
while not done:
    timer -= 1
    screen.fill(Blue)
    Win = fo.render('You completed in '+str(attempt-1)+' Attempts', True, White)
    screen.blit(Win, (250,75))
    if timer == 0:
        done = True
    pygame.display.update()
pygame.quit()
