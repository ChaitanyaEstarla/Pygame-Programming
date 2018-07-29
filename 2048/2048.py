#Python Version: 3.6.4
#Pygame Version: 1.9.3
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
orange = (225,94,58)
red = (255,0,0)
grey = (169,169,169)
yellow = (255, 248, 216)
yellowgrad = (255,220,0)

#Window Size
size = [1000,820]
screen = pygame.display.set_mode(size)

#logo image
logo = "lOGO.png"
background = pygame.image.load(logo).convert()

#Fonts used in Game
title_text = pygame.font.SysFont("aerial",60)
score_text = pygame.font.SysFont("aerial",40)
score_num = pygame.font.SysFont("aerial",50)
nums_disp = pygame.font.SysFont("aerial",75)
first_screen = pygame.font.SysFont("aerial",150)
home_page = pygame.font.SysFont("aerial",150)
play = pygame.font.SysFont("aerial",100)
end_page = pygame.font.SysFont("aerial",175)

#timer varable is used for the first page to control it's screen on time
timer = 600

#Lists
numbers = [['','','',''],
           ['','','',''],
           ['','','',''],
           ['','','','']]

keep_tab = [[False,False,False,True],
            [False,False,False,True],
            [False,False,False,True],
            [False,False,False,True]]

positions = [[[25,162],[205,162],[385,162],[565,162]],
             [[25,342],[205,342],[385,342],[565,342]],
             [[25,522],[205,522],[385,522],[565,522]],
             [[25,702],[205,702],[385,702],[565,702]]]
#Spawn function is switched to true when numbers of the matrix are moved when a key is pressed
spawn = False

#First Number is always 2
temp = [random.randint(0,3),random.randint(0,3)]
numbers[temp[0]][temp[1]]=2
keep_tab[temp[0]][temp[1]] = True

def temperory():
    global temp
    temp = [random.randint(0,3),random.randint(0,3)]

#Function is called when a key is pressed. To spawn a number randomly
def ins():
    global numbers, keep_tab, player_score
    temperory()
    while keep_tab[temp[0]][temp[1]] == True:
        temperory()       
    numbers[temp[0]][temp[1]]= random.choice([2,4])
    keep_tab[temp[0]][temp[1]] = True

ins()
    
#Left key Press
def block_check_left():
    global numbers, keep_tab
  
    if numbers[i][j] == numbers[i][j+1]:
        numbers[i][j] = numbers[i][j] + numbers[i][j+1]
        numbers[i][j+1] = ''
        keep_tab[i][j+1] = False
    else:
        k = j+1
        while numbers[i][k] == '' and k < 3:
            k += 1
        if numbers[i][j] == numbers[i][k]:
            numbers[i][j] = numbers[i][j] * 2
            numbers[i][k] = ''
            keep_tab[i][k] = False

def space_check_left(j):
    global numbers, keep_tab, spawn
    
    if numbers [i][j] == '':
        a = i
        for b in range(j+1,4,1):
            if numbers[a][b] != '':
                numbers[i][j] = numbers[a][b]
                keep_tab[i][j] = True
                numbers[a][b] = ''
                keep_tab[a][b] = False
                if j < 4:
                    j += 1
                spawn = True
                
#Right key Press
def block_check_right():
    global numbers, keep_tab

    if numbers[i][j] == numbers[i][j-1]:
        numbers[i][j-1] = numbers[i][j] + numbers[i][j-1]
        numbers[i][j] = ''
        keep_tab[i][j] = False
    else:
        k = j-1
        while numbers[i][k] == '' and k > 0:
            k-=1
        if numbers[i][j] == numbers[i][k]:
            numbers[i][j] = numbers[i][k] + numbers[i][j]
            numbers[i][k] = ''
            keep_tab[i][k] = False

def space_check_right(j):
    global numbers, keep_tab, spawn
    
    if numbers [i][j] == '':
        a = i
        for b in range(j-1,-1,-1):
            if numbers[a][b] != '':
                numbers[i][j] = numbers[a][b]
                keep_tab[i][j] = True
                numbers[a][b] = ''
                keep_tab[a][b] = False
                if j > 0:
                    j -= 1
                spawn = True

#Up Key Press
def block_check_up():
    global numbers, keep_tab

    if numbers[i][j] == numbers[i+1][j]:
        numbers[i][j] = numbers[i][j] + numbers[i+1][j]
        numbers[i+1][j] = ''
        keep_tab[i+1][j] = False
    else:
        k = i+1
        while numbers[j][k] == '' and k < 3:
            k += 1
        if numbers[i][j] == numbers[k][j]:
            numbers[i][j] = numbers[i][j] + numbers[k][j]
            numbers[k][j] = ''
            keep_tab[k][j] = False

def space_check_up(i):
    global numbers, keep_tab, spawn
    
    if numbers [i][j] == '':
        b = j
        for a in range(i+1,4,1):
            if numbers[a][b] != '':
                numbers[i][j] = numbers[a][b]
                keep_tab[i][j] = True
                numbers[a][b] = ''
                keep_tab[a][b] = False
                if i < 4:
                    i += 1
                spawn = True
        
#Down Key Press
def block_check_down():
    global numbers, keep_tab

    if numbers[i][j] == numbers[i-1][j]:
        numbers[i-1][j] = numbers[i][j] + numbers[i-1][j]
        numbers[i][j] = ''
        keep_tab[i][j] = False
    else:
        k = i-1
        while numbers[k][j] == '' and k > 0:
            k-=1
        if numbers[i][j] == numbers[k][j]:
            numbers[i][j] = numbers[k][j] + numbers[i][j]
            numbers[k][j] = ''
            keep_tab[k][j] = False

def space_check_down(i):
    global numbers, keep_tab, spawn
    
    if numbers [i][j] == '':
        b = j
        for a in range(i-1,-1,-1):
            if numbers[a][b] != '':
                numbers[i][j] = numbers[a][b]
                keep_tab[i][j] = True
                numbers[a][b] = ''
                keep_tab[a][b] = False
                if i > 0:
                    i -= 1
                spawn = True
        
#Clock is used to control the key pressed per second
clock = pygame.time.Clock()

#Company Name screen
done = False
while not done:
    logo = first_screen.render('Blaze Works',True,black)
    screen.blit(logo, (200,335))
    pygame.display.flip()
    screen.fill(white)
    timer -= 1
    if timer == 0:
        done = True

#Start Screen
done = False
while not done:
    
    start = play.render('Play',True,yellow)
    screen.blit(start,(450,600))
    pygame.draw.rect(screen,orange,(450,600,150,75),1)

    for event in  pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:  
                Pos = pygame.mouse.get_pos()
                a = Pos[0]
                b = Pos[1]

                if (a >= 450 and a<= 600) and ( b>= 600 and b<= 675):
                    done = True
                    
    pygame.display.flip()
    screen.fill(yellowgrad)
    screen.blit(background,(250,55))
    
#Main Loop
timer = 1000

done = False
while not done:

    #If Esc key is pressed anytime in game, the window will be terminated i.e. you quit the game
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            done = True
    #Presets
    pygame.draw.rect(screen,yellowgrad,(0,0,1000,99),0)
    pygame.draw.rect(screen,red,(720,100,280,720))
    pygame.draw.polygon(screen,yellowgrad,[[855,360],[815,410],[895,410]],0)
    pygame.draw.polygon(screen,yellowgrad,[[855,560],[815,510],[895,510]],0)
    pygame.draw.polygon(screen,yellowgrad,[[755,460],[805,420],[805,500]],0)
    pygame.draw.polygon(screen,yellowgrad,[[955,460],[905,420],[905,500]],0)

    #Game Text
    name = title_text.render("2048",True,red)
    screen.blit(name,(475,37.5))

    #Blue Boxes
    x=0     
    y=100
    for i in range(16):
        pygame.draw.rect(screen,blue,(x,y,179,179),0)
        x+=180
        if (x > 540):
            y+=180
            x=0
            
    #Logic for Keypresses
    if event.type == pygame.KEYDOWN:
        
        #Left
        if event.key == pygame.K_LEFT:
            print ('Left')
            for i in range(4):
                for j in range(3):
                    block_check_left()

            for i in range(4):
                for j in range(3):
                    space_check_left(j)

            if spawn == True:
                ins()
                spawn = False 

        #Right           
        if event.key == pygame.K_RIGHT:
            print ('Right')
            for i in range(4):
                for j in range(3, 0, -1):
                    block_check_right()

            for i in range(4):
                for j in range(3,0,-1):
                    space_check_right(j)
                    
            if spawn == True:
                ins()
                spawn = False
                
        #Up
        if event.key == pygame.K_UP:
            print ('Up')
            for j in range(4):
                for i in range(3):
                    block_check_up()

            for j in range(4):
                for i in range(3):
                    space_check_up(i)

            if spawn == True:
                ins()
                spawn = False 

        #Down           
        if event.key == pygame.K_DOWN:
            print ('Down')
            for j in range(4):
                for i in range(3, 0, -1):
                    block_check_down()

            for j in range(4):
                for i in range(3,0,-1):
                    space_check_down(i)
                    
            if spawn == True:
                ins()
                spawn = False

    #Displaying the list on the window as numbers
    for i in range(4):
        for j in range(4):
            num_disp = nums_disp.render(str(numbers[i][j]),True,white)
            screen.blit(num_disp,positions[i][j])
    #Condition for game over/ If all boxes are filled and there is no scope to move the numbers then GAME OVER
    fill = 0
    for i in range(4):
        for j in range(4):
            if keep_tab[i][j] == True:
                fill += 1
            if fill == 16:
                done = True
    #If the player manages to add upto 2048 then the player wins 
    for i in range(4):
        for j in range(4):
            if numbers[i][j] == 2048:
                #Player Win Screen
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
    
    pygame.display.flip()
    screen.fill(white)
    clock.tick(5)

#GAME OVER screen 
timer = 1000
done = False
while not done:

    gameover_page = end_page.render('GAME OVER :(',True,black)
    screen.blit(gameover_page, (75,325))

    timer -= 1
    if timer == 0:
        done = True
    pygame.display.flip()
    screen.fill(white)
pygame.quit()
