from settings import *
import pygame


class Map:
    def __init__(self,win):
        self.win = win
        self.map = map
        self.world_map = {}
        self.ai_map = {}
        self.get_map()

    def get_map(self): 
        for j,row in enumerate(self.map):
            for i,value in enumerate(row):
                if value == 1:
                    self.world_map[(i,j)] = value


        for j,row in enumerate(self.map):
            for i,value in enumerate(row):
                if value == 1:
                    self.ai_map[(i,j)] = value

    def draw(self,game_start):
        self.win.fill(WHITE)
        
        [pygame.draw.rect(self.win,DARKGRAY,(pos[0]*TILE,pos[1]*TILE,TILE,TILE),2) 
          for pos in self.world_map]
        
        if game_start:
            [pygame.draw.rect(self.win,DARKGRAY,(pos[0]*TILE+910,pos[1]*TILE,TILE,TILE),2) 
            for pos in self.ai_map]
        
        # pygame.display.update()
        





        

        

    

