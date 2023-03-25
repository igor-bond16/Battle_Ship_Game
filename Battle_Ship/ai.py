from settings import *
import random
import math


class The_ai:
    def __init__(self):
        self.ai_ships = set()
        self.probabilities = [[1.0 / (144) for i in range(12)] for j in range(12)]
        self.ship_size = [1,2,3,4,5]
        self.miss_shoot = 1

    def is_collide(self,positions):
        check_pos = []
        for x,y in positions:
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    check_row, check_col = y + drow*TILE, x + dcol*TILE
                    check_pos.append((check_col,check_row))
        
        if any(pos in self.ai_ships for pos in check_pos):
            return True
        return False

    def set_ships(self):
        for i in range(1,6):
            while True:
                x,y = random.randrange(14,24,1),random.randrange(1,11,1)
                angle = ship_angle[random.randrange(0,4,1)]
                X,Y = x+i*math.cos(math.radians(angle)),y+i*math.sin(math.radians(angle))
                
                #check if ship is inside of field
                if  (14 <= X <= 24) and (1 <= Y <= 11) and (not((X,Y) in self.ai_ships)):
                    #down
                    if angle == 90:

                        positions = []
                        
                        for d in range(i):
                            positions.append((x*TILE,(y+d)*TILE))

                        if self.is_collide(positions):
                            continue
                        else:
                            self.ai_ships.update(positions)
                            break
                    #up
                    if angle == 270:
                        positions = []

                        for d in range(i):
                            positions.append((x*TILE,(y-d)*TILE))

                        if self.is_collide(positions):
                            continue
                        else:
                            self.ai_ships.update(positions)
                            break

                    #right
                    if angle == 0:
                        positions = []

                        for d in range(i):
                            positions.append(((x+d)*TILE,y*TILE))

                        if self.is_collide(positions):
                            continue
                        else:
                            self.ai_ships.update(positions)
                            break

                    #left
                    if angle == 180:
                        positions = []

                        for d in range(i):
                            positions.append(((x-d)*TILE,y*TILE))

                        if self.is_collide(positions):
                            continue
                        else:
                            self.ai_ships.update(positions)
                            break

        return self.ai_ships
    
    #update the probability based on a shot
    def update_probabilities(self,row, col, hit,attacked_pos,ships):
        if hit:
            self.miss_shoot = 1
            self.probabilities[row][col] = 0
            for angle in ship_angle:
                for ship in ships:
                    if ship.is_sunk(attacked_pos):
                        if ship.size in self.ship_size:
                            self.ship_size.remove(int(ship.size))

                            # avoid attacking around destroyed ship
                            for x,y in ship.ship_pos():
                                X,Y = math.floor((x-70)//TILE),math.floor((y-70)//TILE)
                                for drow in [-1, 0, 1]:
                                    for dcol in [-1, 0, 1]:
                                        check_row, check_col = Y + drow, X + dcol
                                        if 1 <= check_row <= 11 and 1 <= check_col <= 11:
                                            self.probabilities[check_row][check_col] = 0

                num = 1
                if self.ship_size:
                    num = max(self.ship_size) - 1

                for l in range(num):
                    if 0 <= row+int(l*math.sin(math.radians(angle))) < 12 and 0 <= col+int(l*math.cos(math.radians(angle))) < 12:
                        self.probabilities[row + int(l*math.sin(math.radians(angle)))][col + int(l*math.cos(math.radians(angle)))] *= 2
                    else:
                            continue 
        
        else:
            self.miss_shoot += 1
            self.probabilities[row][col] = 0

    #select the next target based on the probability
    def select_target(self,attacked_pos):
        max_prob = 0
        targets = []
        if self.miss_shoot%3 == 0:
            while True:
                x,y = random.randrange(1,11,1),random.randrange(1,11,1)
                if (x*TILE+70,y*TILE+70) in attacked_pos or self.probabilities[y][x] == 0:
                    continue
                else:
                    targets = [(y,x)]
                    break
        else:
            for i in range(12):
                for j in range(12):
                    if self.probabilities[i][j] > max_prob:
                        max_prob = self.probabilities[i][j]
                        targets = [(i, j)]
                    elif self.probabilities[i][j] == max_prob and self.probabilities[i][j] != 0:
                        targets.append((i, j))
            
        return random.choice(targets)
