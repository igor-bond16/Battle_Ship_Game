import pygame
import sys
from test import set_ships


pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1500,1500))
MENU_BACK = pygame.image.load('sink_ship.jpg')
MENU_BACK = pygame.transform.scale(MENU_BACK,(1075,1075))
pygame.display.set_caption("battle ship")

st_list = ("A","B","C","D","E","F","G","H","I","J","K","L")
num_list = ("F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12")
ship_list = []

class Ship:
    def __init__(self):
        pass

    def draw(self):
        pass


line1 = 'Player1, Player2 both of you can set one 5block ship,     '
line2 = 'two 4block ship, three 3block ship, and four 2block ship.'
line3 = 'Press key and set your ship!                                            '

   

def drawexplain(win,line,y):
    font = pygame.font.SysFont('comicsens',30)
    text = font.render(line,1,(0,0,0))
    win.blit(text,(1167.5 - text.get_width()/2,y))

def drawWindow(ship_list,win,keys):
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
    
    drawnumbers()
    drawstring()
    drawexplain(win,line1,55)
    drawexplain(win,line2,85)
    drawexplain(win,line3,115)

    ship_list = set_ships(ship_list,keys)
    
    for s in ship_list:
        pygame.draw.rect(win,(0,0,0),s,0)

    pygame.display.update()


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


def main(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        drawWindow(ship_list,win,keys)



    pygame.quit()

def main_menu(win):
    run_menu = True
    while run_menu:
        win.blit(MENU_BACK,(225,0))
        font = pygame.font.SysFont('comicsens',100)
        text = font.render('BATTLE SHIP',1,(0,0,0))
        win.blit(text,(750 - text.get_width()/2,55))
        font2 = pygame.font.SysFont('comicsens',45)
        text2 = font2.render('press any key to play',1,(0,0,0))
        win.blit(text2,(750 - text2.get_width()/2,150))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main(win)

            if event.type == pygame.QUIT:
                run_menu = False
            
        pygame.display.update()
    pygame.quit()

main_menu(win)