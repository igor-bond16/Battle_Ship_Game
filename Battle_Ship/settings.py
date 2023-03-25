import os
import pygame

#game settings
SCREEN = (WIDTH,HEIGHT) = (1960,980)
HALF_WIDTH,HALF_HEIGHT = WIDTH/2,HEIGHT/2
ship_angle = [0,90,180,270]
TILE = 70

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (220,0,0)
GREEN = (0,220,0)
BLUE = (0,0,220)
DARKGRAY = (110,110,110)
PURPLE = (120,0,120)

#font
pygame.font.init()
TITLE_FONT = pygame.font.SysFont(None, 250)
SCORE = pygame.font.SysFont(None, 75)

#the game map
map = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#images
BACKGROUND = os.path.join("assets", "main_background.jpg")
PLAY_BUTTON = os.path.join("assets", "start_button.png")
HIT_MARKER = pygame.image.load(os.path.join("assets", "hit_marker.png"))
HOW_TO_PLAY = pygame.image.load(os.path.join("assets", "how_to_play.jpg"))


class Screen:
    def __init__(self,game):
        self.game = game

    def handle_event(self,event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

