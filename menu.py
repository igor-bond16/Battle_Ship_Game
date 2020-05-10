import pygame,sys
from pygame.locals import *

mainclock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
win = pygame.display.set_mode((500,500),0,32)

font = pygame.font.SysFont(None,20)

def draw_text(text,font,color,win,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    win.blit(textobj,textrect)

def main_menu():
    while True:
        win.fill((0,0,0))
        draw_text('main menu',font,(255,255,255),win,20,20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        mainclock.tick(60)

main_menu()