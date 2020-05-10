import pygame
from battle_ship_re import main_menu

st_list = ("A","B","C","D","E","F","G","H","I","J","K","L")

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

    #main_menu(st_list)

