from settings import *
import math
from map import *

class Player:
    def __init__(self,win):
        self.attacked_positions = set()
        self.win = win
        self.destroyed = 0
        self.destroyed_pos = set()
        
    
    def attack(self,pos,ai_ships):
        x,y = pos
        X,Y = math.floor((x-70)/TILE)*TILE,math.floor((y-70)/TILE)*TILE

        if (13 <= X/TILE <= 24) and (0 <= Y/TILE <= 11) and not((X+70,Y+70) in self.attacked_positions):
            self.attacked_positions.add((X+70,Y+70))

        if (X+70,Y+70) in ai_ships and not (X+70,Y+70) in self.destroyed_pos:
            self.destroyed_pos.add((X+70,Y+70))
            self.destroyed += 1

        return self.attacked_positions,self.destroyed
    
    


        
