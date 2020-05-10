import pygame
from pygame.locals import *
from test import set_ships
import math
import time

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1500,1500))
MENU_BACK = pygame.image.load('sinking_ship.jpg')
pygame.display.set_caption("battle ship")

line1 = 'Player1, Player2 both of you can set one 5block ship,     '
line2 = 'two 4block ship, three 3block ship, and four 2block ship.'
line3 = 'Press key and set your ship!                                            '

#clock = pygame.time.Clock()

st_list = ("A","B","C","D","E","F","G","H","I","J","K","L")
num_list = ("F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12")
ship_list = []

def drawexplain(win,line,y):
    font = pygame.font.SysFont('comicsens',30)
    text = font.render(line,1,(0,0,0))
    win.blit(text,(1167.5 - text.get_width()/2,y))

def drawWindow(ship_list,win,keys,pos):
    rows = 12
    x = 55
    y = 55
     
    sizeBwn = 65

    win.fill((255,255,255))

    for i in range(rows):
        x += sizeBwn
        y += sizeBwn
        pygame.draw.line(win,(0,0,0),(x,55),(x,835))
        pygame.draw.line(win,(0,0,0),(55,y),(835,y))

        pygame.draw.line(win,(0,0,0),(55,55),(55,835),5)
        pygame.draw.line(win,(0,0,0),(55,55),(835,55),5)
        pygame.draw.line(win,(0,0,0),(55,835),(835,835),5)
        pygame.draw.line(win,(0,0,0),(835,55),(835,835),5)

    reset_button = pygame.Rect(1000,150,110,50)
    back_button = pygame.Rect(1000,210,110,50)
    game_start_button = pygame.Rect(1000,270,110,50)
    pygame.draw.rect(win,(255,0,0),reset_button)
    pygame.draw.rect(win,(0,255,0),back_button)
    pygame.draw.rect(win,(0,0,255),game_start_button)
    font = pygame.font.SysFont('comicsens',45)
    text = font.render('RESET',1,(0,0,0))
    text2 = font.render('BACK',1,(0,0,0))
    text3 = font.render('START',1,(0,0,0))
    win.blit(text,(1010,160))
    win.blit(text2,(1010,220))
    win.blit(text3,(1010,280))

    
    drawnumbers()
    drawstring()
    drawexplain(win,line1,55)
    drawexplain(win,line2,85)
    drawexplain(win,line3,115)

    ship_list = set_ships(ship_list,keys)

    if game_start_button.collidepoint(pos):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_game()

    elif reset_button.collidepoint(pos):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ship_list.clear()

    elif back_button.collidepoint(pos):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ship_list[-1:] = []

    
    for s in ship_list:
        pygame.draw.rect(win,(0,0,0),s,0)

    pygame.display.update()


def start_game():
    font = pygame.font.SysFont('comicsens',50)
    text = font.render('First Player1 please set ships',1,(255,0,0))
    win.blit(text,(1010,750))
    pygame.display.update()
    #pygame.time.deley(100)


def drawnumbers():
    i = 87.5
    for b in num_list:
        font = pygame.font.SysFont('comicsens',25)
        text = font.render(b,1,(0,0,0))
        win.blit(text,(i - (text.get_width()/2),5))
        i += 65

def drawstring():
    l = 87.5
    for i in st_list:
        font = pygame.font.SysFont('comicsens',25)
        text = font.render(i,1,(0,0,0))
        win.blit(text,(5,l - (text.get_width()/2)))
        l += 65


def draw_example(win,st_list):
    pygame.init()
    pygame.font.init()
    x = 55
    y = 55
    rows = 12
    sizeBwn = 30

    win.fill((255,255,255))

    for i in range(rows):
        x += sizeBwn
        y += sizeBwn
        pygame.draw.line(win,(0,0,0),(x,55),(x,415))
        pygame.draw.line(win,(0,0,0),(55,y),(415,y))

        pygame.draw.line(win,(0,0,0),(55,55),(55,415),5)
        pygame.draw.line(win,(0,0,0),(55,55),(415,55),5)
        pygame.draw.line(win,(0,0,0),(55,415),(415,415),5)
        pygame.draw.line(win,(0,0,0),(415,55),(415,415),5)

    ex_plain1 = 'As you know you can set one 5block ship, two 4block ship, '
    ex_plain2 = 'three 3block ship, and four 2block ship.                       '

    drawexplain(win,ex_plain1,55)
    drawexplain(win,ex_plain2,105)
        
    draw_numbers(win)
    draw_string(win,st_list)
    draw_ship(win)

    
    pygame.display.update()


def draw_ship(win):
    pygame.draw.rect(win,(0,0,0),(55,85,120,30),0)
    pygame.draw.rect(win,(0,0,0),(235,115,30,120),0)
    pygame.draw.rect(win,(0,0,0),(295,115,90,30),0)
    pygame.draw.rect(win,(0,0,0),(85,145,60,30),0)
    pygame.draw.rect(win,(0,0,0),(145,235,30,90),0)
    pygame.draw.rect(win,(0,0,0),(235,295,60,30),0)
    pygame.draw.rect(win,(0,0,0),(385,265,30,150),0)
    pygame.draw.rect(win,(0,0,0),(55,325,30,90),0)
    pygame.draw.rect(win,(0,0,0),(175,355,30,60),0)
    pygame.draw.rect(win,(0,0,0),(325,355,30,60),0)


def draw_numbers(win):
    i = 70
    l = 1
    for b in range(12):
        font = pygame.font.SysFont('comicsens',20)
        text = font.render(str(l),1,(0,0,0))
        win.blit(text,(i - (text.get_width()/2),5))
        i += 30
        l += 1
            

def draw_string(win,st_list):
    l = 70
    for i in st_list:
        font = pygame.font.SysFont('comicsens',20)
        text = font.render(i,1,(0,0,0))
        win.blit(text,(5,l - (text.get_width()/2)))
        l += 30

def main_loop(win,st_list):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_example(win,st_list)


def main(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        pos = pygame.mouse.get_pos() 

        drawWindow(ship_list,win,keys,pos)



    pygame.quit()

def main_menu(st_list):
    click = False
    run_menu = True
    while run_menu:
        win = pygame.display.set_mode((1500,1500))
        mx,my = pygame.mouse.get_pos()
        win.blit(MENU_BACK,(0,0))
        font = pygame.font.SysFont('comicsens',100)
        text = font.render('BATTLE SHIP',1,(0,0,0))
        win.blit(text,(750 - text.get_width()/2,55))
        button1 = pygame.Rect(596,150,150,60)
        button2 = pygame.Rect(596,250,150,60)
        pygame.draw.rect(win,(255,255,255),button1)
        pygame.draw.rect(win,(255,255,255),button2)
        font2 = pygame.font.SysFont('comicsens',45)
        text2 = font2.render('play',1,(0,0,0))
        text3 = font2.render('example',1,(0,0,0))
        win.blit(text2,(645,165))
        win.blit(text3,(600,265))
        pygame.draw.line(win,(108,173,119),(650-(25*math.sqrt(3)),155),(650-(25*math.sqrt(3)),205),5)
        pygame.draw.line(win,(108,173,119),(650-(25*math.sqrt(3)),155),(640,180),5)
        pygame.draw.line(win,(108,173,119),(650-(25*math.sqrt(3)),205),(640,180),5)
        

        if button1.collidepoint((mx,my)):
            if  click:
                main(win)

        if button2.collidepoint((mx,my)):
            if click:
                main_loop(win,st_list)
                click = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass

            if event.type == pygame.QUIT:
                run_menu = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    pygame.quit()

main_menu(st_list)

