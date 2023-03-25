import pygame
from settings import *

class Ship:
    def __init__(self, image,size):
        self.image = image
        self.orientation = 'horizontal'
        self.rect = self.image.get_rect()
        self.size = size
        self.positions = set()

    def place(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def is_sunk(self,attacked_pos):
        if all(pos in attacked_pos for pos in self.positions):
                return True
        return False

    def rotate(self):
        if self.orientation == 'horizontal':
            self.image = pygame.transform.rotate(self.image, 90)
            self.orientation = 'vertical'
        else:
            self.image = pygame.transform.rotate(self.image, -90)
            self.orientation = 'horizontal'

    def ship_pos(self):
        self.ship_positions = set()
        if self.orientation == 'horizontal':
            for i in range(self.size):
                self.ship_positions.add((self.rect.x+i*TILE,self.rect.y))
        elif self.orientation == 'vertical':
            for i in range(self.size):
                self.ship_positionsp.add((self.rect.x,self.rect.y+i*TILE))

        return self.ship_positions
            
