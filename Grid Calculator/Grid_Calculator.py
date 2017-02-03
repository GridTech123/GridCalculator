try:
    import os
    import pygame
    from pygame import *
    from pygame.locals import *
    import random
    import sys
    import pickle
    import time
    import pyError
    from Tkinter import *
    from tkFileDialog import*
    import random
except:
    os.chdir('html')
    os.startfile('missingModule.html')

try:
    import pyError
except:
    os.chdir('html')
    os.startfile('missingPyError.html')

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)
gray3 = (140, 138, 139)

colorScheme = [black, white, blue2, blue3, gray, gray2, gray3]

#images
try:
    more = pygame.image.load('more.png')
    more2 = pygame.image.load('more2.png')
    logo = pygame.image.load('logo.png')
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue getting images', 20, 20) 

#setup
clock = pygame.time.Clock()

#vars
rendermode = 0
value = ''
moreTab = False
preValuesEquation = []
preValuesAnswer = []
value1 = ''
value2 = ''
opperation = 'no opperation'

#pygame start
try:
    from win32api import GetSystemMetrics
except:
    pyError.newError('temp Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
    #prfloat "Width =", GetSystemMetrics(0)
    #prfloat "Height =", GetSystemMetrics(1)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
    pygame.init()
    wsx = GetSystemMetrics(0)
    wsy = GetSystemMetrics(1)
    sx = wsx - 100
    sy = wsy - 100
    mode = RESIZABLE
    screen = pygame.display.set_mode([sx,sy], mode)
except:
    pyError.newError('poly cities Error', 'There was an error on start', 'We dont know what happened', 20, 20)   

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
value2_font = pygame.font.SysFont('Calibri', 100)
value_font = pygame.font.SysFont('Calibri', 200)
size = 200

#window settings
pygame.display.set_icon(logo)
pygame.display.set_caption("Grid Calculator")

#first time
try:
    pickle_in = open('firstStart.pcr', 'r')
    rendermode = 0
except:
    pickle_out = open('firstStart.pcr', 'w')
    pickle.dump(True, pickle_out)
    pickle_out.close()
    rendermode = 'firstStart'

#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()

    #settings
    screen.fill(colorScheme[4])
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    pygame.draw.rect(screen, colorScheme[1], [0,0,sx,200])
    screen.blit(pygame.font.SysFont('Calibri', size).render(str(value), True, colorScheme[0]), (10,10))

    try:
        if mx > 10 and mx < 10 + 290 and my > 210 and my < 210 + 150:
            pygame.draw.rect(screen, colorScheme[3], [10, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(7), True, colorScheme[0]), (10 + 110, 210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '7'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [10, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(7), True, colorScheme[0]), (10 + 110, 210))

        if mx > 310 and mx < 310 + 290 and my > 210 and my < 210 + 150:
            pygame.draw.rect(screen, colorScheme[3], [310, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(8), True, colorScheme[0]), (310 + 110, 210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '8'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [310, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(8), True, colorScheme[0]), (310 + 110, 210))

        if mx > 610 and mx < 610 + 290 and my > 210 and my < 210 + 150:
            pygame.draw.rect(screen, colorScheme[3], [610, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(9), True, colorScheme[0]), (610 + 110, 210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '9'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [610, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(9), True, colorScheme[0]), (610 + 110, 210))

        if mx > 910 and mx < 910 + 290 and my > 210 and my < 210 + 150:
            pygame.draw.rect(screen, colorScheme[3], [910, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('C'), True, colorScheme[0]), (910 + 110, 210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = '' 
                value1 = ''
                value2 = ''
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [910, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('C'), True, colorScheme[0]), (910 + 110, 210))

        if mx > 1210 and mx < 1210 + 290 and my > 210 and my < 210 + 150:
            pygame.draw.rect(screen, colorScheme[3], [1210, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('<'), True, colorScheme[0]), (1210 + 110, 210))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value[0:len(value) - 1]
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [1210, 210, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('<'), True, colorScheme[0]), (1210 + 110, 210))

        if mx > 10 and mx < 10 + 290 and my > 370 and my < 370 + 150:
            pygame.draw.rect(screen, colorScheme[3], [10, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(4), True, colorScheme[0]), (10 + 110, 370))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '4'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [10, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(4), True, colorScheme[0]), (10 + 110, 370))

        if mx > 310 and mx < 310 + 290 and my > 370 and my < 370 + 150:
            pygame.draw.rect(screen, colorScheme[3], [310, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(5), True, colorScheme[0]), (310 + 110, 370))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '5'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [310, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(5), True, colorScheme[0]), (310 + 110, 370))

        if mx > 610 and mx < 610 + 290 and my > 370 and my < 370 + 150:
            pygame.draw.rect(screen, colorScheme[3], [610, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(6), True, colorScheme[0]), (610 + 110, 370))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '6'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [610, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(6), True, colorScheme[0]), (610 + 110, 370))

        if value == '':
            pygame.draw.rect(screen, colorScheme[6], [910, 370, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('+'), True, colorScheme[0]), (910 + 110, 370))
        else:
            if mx > 910 and mx < 910 + 290 and my > 370 and my < 370 + 150:
                pygame.draw.rect(screen, colorScheme[3], [910, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('+'), True, colorScheme[0]), (910 + 110, 370))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if value1 == '':
                        value1 = float(value)
                        value = ''
                    opperation = '+'
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [910, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('+'), True, colorScheme[0]), (910 + 110, 370))

        if value == '':
            if mx > 1210 and mx < 1210 + 290 and my > 370 and my < 370 + 150:
                pygame.draw.rect(screen, colorScheme[3], [1210, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('-'), True, colorScheme[0]), (1210 + 110, 370))
                screen.blit(pygame.font.SysFont('Calibri', 30).render(str('Mode: Negate'), True, colorScheme[0]), (1210, 490))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    value = value + '-'
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [1210, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('-'), True, colorScheme[0]), (1210 + 110, 370))
                screen.blit(pygame.font.SysFont('Calibri', 30).render(str('Mode: Negate'), True, colorScheme[0]), (1210, 490))
        else:
            if mx > 1210 and mx < 1210 + 290 and my > 370 and my < 370 + 150:
                pygame.draw.rect(screen, colorScheme[3], [1210, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('-'), True, colorScheme[0]), (1210 + 110, 370))
                screen.blit(pygame.font.SysFont('Calibri', 30).render(str('Mode: Subtract'), True, colorScheme[0]), (1210, 490))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if value1 == '':
                        value1 = float(value)
                        value = ''
                    opperation = '-'
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [1210, 370, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('-'), True, colorScheme[0]), (1210 + 110, 370))
                screen.blit(pygame.font.SysFont('Calibri', 30).render(str('Mode: Subtract'), True, colorScheme[0]), (1210, 490))

        if mx > 10 and mx < 10 + 290 and my > 530 and my < 530 + 150:
            pygame.draw.rect(screen, colorScheme[3], [10, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(1), True, colorScheme[0]), (10 + 110, 530))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '1'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [10, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(1), True, colorScheme[0]), (10 + 110, 530))

        if mx > 310 and mx < 310 + 290 and my > 530 and my < 530 + 150:
            pygame.draw.rect(screen, colorScheme[3], [310, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(2), True, colorScheme[0]), (310 + 110, 530))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '2'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [310, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(2), True, colorScheme[0]), (310 + 110, 530))

        if mx > 610 and mx < 610 + 290 and my > 530 and my < 530 + 150:
            pygame.draw.rect(screen, colorScheme[3], [610, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(3), True, colorScheme[0]), (610 + 110, 530))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '3'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [610, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(3), True, colorScheme[0]), (610 + 110, 530))

        if value == '':
            pygame.draw.rect(screen, colorScheme[6], [910, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('x'), True, colorScheme[0]), (910 + 110, 530))
        else:
            if mx > 910 and mx < 910 + 290 and my > 530 and my < 530 + 150:
                pygame.draw.rect(screen, colorScheme[3], [910, 530, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('x'), True, colorScheme[0]), (910 + 110, 530))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if value1 == '':
                        value1 = float(value)
                        value = ''
                    opperation = '*'
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [910, 530, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('x'), True, colorScheme[0]), (910 + 110, 530))

        if value == '':
            pygame.draw.rect(screen, colorScheme[6], [1210, 530, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('/'), True, colorScheme[0]), (1210 + 110, 530))
        else:
            if mx > 1210 and mx < 1210 + 290 and my > 530 and my < 530 + 150:
                pygame.draw.rect(screen, colorScheme[3], [1210, 530, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('/'), True, colorScheme[0]), (1210 + 110, 530))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if value1 == '':
                        value1 = float(value)
                        value = ''
                    opperation = '/'
                    pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [1210, 530, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('/'), True, colorScheme[0]), (1210 + 110, 530))

        if mx > 10 and mx < 10 + 290 and my > 690 and my < 690 + 150:
            pygame.draw.rect(screen, colorScheme[3], [10, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(0), True, colorScheme[0]), (10 + 110, 690))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '0'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [10, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str(0), True, colorScheme[0]), (10 + 110, 690))

        if mx > 310 and mx < 310 + 290 and my > 690 and my < 690 + 150:
            pygame.draw.rect(screen, colorScheme[3], [310, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('.'), True, colorScheme[0]), (310 + 110, 690))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = value + '.'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [310, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('.'), True, colorScheme[0]), (310 + 110, 690))

        if value2 == '':
            pygame.draw.rect(screen, colorScheme[6], [610, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('='), True, colorScheme[0]), (610 + 110, 690))
        else:
            if mx > 610 and mx < 610 + 290 and my > 690 and my < 690 + 150:
                pygame.draw.rect(screen, colorScheme[3], [610, 690, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('='), True, colorScheme[0]), (610 + 110, 690))
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if opperation == '+':
                        preValuesEquation.append(str(value1)+'+'+str(value2))
                        preValuesAnswer.append(str(float(value1) + float(value2)))
                        value = float(value1) + float(value2)
                        pygame.time.delay(100)
                    if opperation == '-':
                        preValuesEquation.append(str(value1)+'-'+str(value2))
                        preValuesAnswer.append(str(float(value1) - float(value2)))
                        value = float(value1) - float(value2)
                        pygame.time.delay(100)
                    if opperation == '*':
                        preValuesEquation.append(str(value1)+'*'+str(value2))
                        preValuesAnswer.append(str(float(value1) * float(value2)))
                        value = float(value1) * float(value2)
                        pygame.time.delay(100)
                    if opperation == '/':
                        preValuesEquation.append(str(value1)+'/'+str(value2))
                        preValuesAnswer.append(str(float(value1) / float(value2)))
                        value = float(value1) / float(value2)
                        pygame.time.delay(100)
            else:
                pygame.draw.rect(screen, colorScheme[5], [610, 690, 290, 150])
                screen.blit(pygame.font.SysFont('Calibri', 150).render(str('='), True, colorScheme[0]), (610 + 110, 690))

        if mx > 910 and mx < 910 + 290 and my > 690 and my < 690 + 150:
            pygame.draw.rect(screen, colorScheme[3], [910, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('PI'), True, colorScheme[0]), (910 + 90, 690))
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                value = '3.1415926535897932'
                pygame.time.delay(100)
        else:
            pygame.draw.rect(screen, colorScheme[5], [910, 690, 290, 150])
            screen.blit(pygame.font.SysFont('Calibri', 150).render(str('PI'), True, colorScheme[0]), (910 + 90, 690))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:   
                value = value + '1'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP2:   
                value = value + '2'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP3:   
                value = value + '3'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP4:   
                value = value + '4'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP5:   
                value = value + '5'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP6:   
                value = value + '6'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP7:   
                value = value + '7'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP8:   
                value = value + '8'
                pygame.time.delay(100)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP9:   
                value = value + '9'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP0:   
                value = value + '0'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:   
                value = '' 
                value1 = ''
                value2 = ''
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PERIOD:   
                value = '' 
                value1 = ''
                value2 = ''
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_PLUS:   
                if value1 == '':
                    value1 = float(value)
                    value = ''
                opperation = '+'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_MINUS:   
                if value == '':
                    value = value + '-'
                else:
                    value1 = float(value)
                    value = ''
                    opperation = '-'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_MULTIPLY:   
                if value1 == '':
                    value1 = float(value)
                    value = ''
                opperation = '*'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_DIVIDE:   
                if value1 == '':
                    value1 = float(value)
                    value = ''
                opperation = '/'
                pygame.time.delay(100)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:  
                if not value2 == '': 
                    if opperation == '+':
                        preValuesEquation.append(str(value1)+'+'+str(value2))
                        preValuesAnswer.append(str(float(value1) + float(value2)))
                        value = float(value1) + float(value2)
                        pygame.time.delay(100)
                    if opperation == '-':
                        preValuesEquation.append(str(value1)+'-'+str(value2))
                        preValuesAnswer.append(str(float(value1) - float(value2)))
                        value = float(value1) - float(value2)
                        pygame.time.delay(100)
                    if opperation == '*':
                        preValuesEquation.append(str(value1)+'*'+str(value2))
                        preValuesAnswer.append(str(float(value1) * float(value2)))
                        value = float(value1) * float(value2)
                        pygame.time.delay(100)
                    if opperation == '/':
                        preValuesEquation.append(str(value1)+'/'+str(value2))
                        preValuesAnswer.append(str(float(value1) / float(value2)))
                        value = float(value1) / float(value2)
                        pygame.time.delay(100)
                pygame.time.delay(100)

    except:
        value = '' 
        value1 = ''
        value2 = ''

    if sx > 1919:
        pygame.draw.rect(screen, colorScheme[5], [1511, 200, sx , sy])
        tabClock = 0
        while True:
            try:
                test = preValuesEquation[tabClock]
                pygame.draw.rect(screen, colorScheme[6], [1511, tabClock * 65 + 210, sx, 60])
                screen.blit(hud_font.render(str(preValuesEquation[tabClock]), True, colorScheme[4]),(1511, tabClock * 65 + 208))
                screen.blit(hud_font.render(str(preValuesAnswer[tabClock]), True, colorScheme[4]),(1511, (tabClock) * 65 + 205 + 30))
                if tabClock * 65 - 60 > sy - 300:
                    preValuesEquation.remove(preValuesEquation[0])
                    preValuesAnswer.remove(preValuesAnswer[0])
                tabClock = tabClock + 1
            except:
                break

    if not value1 == '':
        value2 = value

    if moreTab == 'open':
        pygame.draw.rect(screen, colorScheme[2], [tabx, 0, 400, sy])
        if tabx > tabxLocation:
            tabx = tabx - 15
            #pygame.time.delay(1)
        else:
            moreTab = True

    if moreTab == 'close':
        pygame.draw.rect(screen, colorScheme[2], [tabx, 0, 400, sy])
        if tabx < sx:
            tabx = tabx + 15
            #pygame.time.delay(1) 
        else:
            moreTab = False

    if moreTab == True:
        pygame.draw.rect(screen, colorScheme[2], [sx - 400, 0, 600, sy])

    if moreTab == False:
        screen.blit(more, (sx - 100, 10))
        if mx > sx - 100 and mx < sx - 100 + 90 and my > 10 and my < 10 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                moreTab = 'open'
                tabx = sx
                tabxLocation = sx - 400
                pygame.time.delay(100)
    elif moreTab == 'close':
        screen.blit(more, (sx - 100, 10))
        if mx > sx - 100 and mx < sx - 100 + 90 and my > 10 and my < 10 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                moreTab = 'open'
                tabxLocation = sx - 400
                pygame.time.delay(100)
    elif moreTab == True:
        screen.blit(more2, (sx - 100, 10))
        if mx > sx - 100 and mx < sx - 100 + 90 and my > 10 and my < 10 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                moreTab = 'close'
                #tabx = sx
                pygame.time.delay(100)
    elif moreTab == 'open':
        screen.blit(more2, (sx - 100, 10))
        if mx > sx - 100 and mx < sx - 100 + 90 and my > 10 and my < 10 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                moreTab = 'close'
                #tabx = sx
                pygame.time.delay(100)
    display.update()
