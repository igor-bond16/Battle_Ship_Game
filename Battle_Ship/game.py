import pygame,sys
from settings import *
from map import Map
from ai import The_ai
from player import Player
from ship import Ship
from button import Button,Message
import math,time
import pygame

class Game:
    def __init__(self):
        # initialize Pygame
        pygame.init()

        # create the game window
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BattleShip Game")

        #nitialize
        self.player = Player(self.win)
        self.ai = The_ai()
        self.map = Map(self.win)
        self.ai_ships = self.ai.set_ships()
        self.hits = 0  
        self.players_ship = set()
        self.attacked_pos = set() 

        #set ships to initial position
        ship_images = []
        for i in range(5):
            image = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"ship{1+i}.jpg")).convert_alpha(),(70+70*i, 70))
            ship_images.append(image)

        self.ships = []
        for i in range(5):
            ship = Ship(ship_images[i],ship_images[i].get_width()//70)
            ship.place(910, 100+i*70)
            self.ships.append(ship)

        # create the screens
        self.main_screen = MainScreen(self)
        self.set_ships_screen = SetShips(self)
        self.rules_screen = RuleScreen(self)
        self.game_screen = Game_Play(self)
        self.gameset_screen = Game_Set(self)
        self.current_screen = self.main_screen

        #sound
        main_sound = pygame.mixer.Sound('audio/main.ogg')
        main_sound.set_volume(0.1)
        main_sound.play(loops=-1)
    
    def restart_game(self):
        #nitialize
        self.player = Player(self.win)
        self.ai = The_ai()
        self.map = Map(self.win)
        self.ai_ships = self.ai.set_ships()
        self.hits = 0  
        self.players_ship = set()
        self.attacked_pos = set() 

        #set ships to initial position
        ship_images = []
        for i in range(5):
            image = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"ship{1+i}.jpg")).convert_alpha(),(70+70*i, 70))
            ship_images.append(image)

        self.ships = []
        for i in range(5):
            ship = Ship(ship_images[i],ship_images[i].get_width()//70)
            ship.place(910, 100+i*70)
            self.ships.append(ship)

        # create the screens
        self.main_screen = MainScreen(self)
        self.set_ships_screen = SetShips(self)
        self.rules_screen = RuleScreen(self)
        self.game_screen = Game_Play(self)
        self.gameset_screen = Game_Set(self)
        self.current_screen = self.main_screen

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                self.current_screen.handle_event(event)

            self.current_screen.draw()

            self.current_screen.update()

            pygame.display.update()
            clock.tick(60)

    def switch_screen(self, screen):
        self.current_screen = screen

class MainScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.win = self.game.win
        self.background = pygame.image.load(BACKGROUND)
        self.background = pygame.transform.scale(self.background,(WIDTH,HEIGHT))
        self.start_btn = pygame.image.load(PLAY_BUTTON).convert_alpha()
        self.start_btn.set_colorkey(-1,pygame.RLEACCEL)
        self.btn = (HALF_WIDTH - self.start_btn.get_width()/2, HALF_HEIGHT, self.start_btn.get_width(), self.start_btn.get_height())
        self.rules_button = Button(WIDTH-500, HEIGHT-300, 250, 100, 'HOW TO PLAY')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = pygame.mouse.get_pos()
            if (self.btn[0] <= x <= self.btn[0] + self.btn[2]) and (self.btn[1] <= y <= self.btn[1] + self.btn[3]):
                self.game.switch_screen(self.game.set_ships_screen)
            elif self.rules_button.handle_event(event):
                self.game.switch_screen(self.game.rules_screen)
                # self.win.blit(self.how_to_play, (self.rules_img[0],self.rules_img[1]))

    def draw(self):
        self.game.win.blit(self.background, (0,0))
        self.game.win.blit(self.start_btn, (self.btn[0], self.btn[1]))
        self.rules_button.draw(self.win)
        message = TITLE_FONT.render('BATTLE SHIP',True,'red')
        self.win.blit(message,(HALF_WIDTH - message.get_width()//2, message.get_height()//2))

class RuleScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.win = self.game.win
        self.exit_button = Button(WIDTH-500, HEIGHT-300, 250, 100, 'EXIT')
        self.how_to_play = pygame.transform.scale(HOW_TO_PLAY, (TILE*16, TILE*16))
        self.rules_img = (HALF_WIDTH - self.how_to_play.get_width()//2, HALF_HEIGHT - self.how_to_play.get_height()//2, self.how_to_play.get_width(), self.how_to_play.get_height())

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.exit_button.handle_event(event):
                self.game.switch_screen(self.game.main_screen)

    def draw(self):
        self.win.fill(WHITE)
        self.exit_button.draw(self.win)
        message = TITLE_FONT.render('HOW TO PLAY BATTLE SHIP',True,'blue')
        self.win.blit(message,(HALF_WIDTH - message.get_width()//2, message.get_height()//2))

class SetShips(Screen):
    def __init__(self, game):
        super().__init__(game)

        #initial setup
        self.win = self.game.win
        self.font = pygame.font.SysFont(None, 20)
        self.map = self.game.map
        self.start_button = Button(980, 800, 200, 50, 'Start Game')
        self.exit_button = Button(1200, 800, 200, 50, 'Exit')
        self.players_ship = self.game.players_ship
        self.ships = self.game.ships
        self.selected_ship = None
        self.messages = []
        self.inside_fiield = True
        self.collide = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for ship in self.ships:
                if ship.rect.collidepoint(pos):
                    self.selected_ship = ship
                    break

            if self.exit_button.handle_event(event):
                self.game.switch_screen(self.game.main_screen)

            elif self.start_button.handle_event(event):
                for ship in self.ships:
                    if ship.orientation == 'horizontal':
                        for i in range(ship.size):
                            self.players_ship.add((ship.rect.x+i*TILE,ship.rect.y))
                            ship.positions.add((ship.rect.x+i*TILE,ship.rect.y))
                    elif ship.orientation == 'vertical':
                        for i in range(ship.size):
                            self.players_ship.add((ship.rect.x,ship.rect.y+i*TILE))
                            ship.positions.add((ship.rect.x,ship.rect.y+i*TILE))


                self.game.switch_screen(self.game.game_screen)
                    

        #ADJUST SHIP TO FIELD
        elif event.type == pygame.MOUSEBUTTONUP and self.selected_ship:
            x,y = self.selected_ship.rect.x-70,self.selected_ship.rect.y-70
            X,Y = (math.floor(x/TILE)*TILE)+70,(math.floor(y/TILE)*TILE)+70
            self.selected_ship.rect.x,self.selected_ship.rect.y = X,Y

            self.selected_ship = None

            for ship in self.ships:
                self.win.blit(ship.image, ship.rect)

        #MOVE SHIP
        elif event.type == pygame.MOUSEMOTION and self.selected_ship:
            x,y = pygame.mouse.get_pos()
            if self.selected_ship:
                self.selected_ship.rect.x = x
                self.selected_ship.rect.y = y

        #ROTATE SHIP
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.selected_ship:
            if self.selected_ship:
                self.selected_ship.rotate()
    
    def draw(self):
        self.win.fill(WHITE)
        self.map.draw(False)

        for ship in self.ships:
            self.win.blit(ship.image, ship.rect)

        self.start_button.draw(self.win)
        self.exit_button.draw(self.win)

class Game_Play(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.win = self.game.win
        self.map = self.game.map
        self.ships = self.game.ships
        self.player = self.game.player
        self.ai = self.game.ai
        self.ai_ships = self.game.ai_ships
        self.hits = self.game.hits
        self.attacked_pos = self.game.attacked_pos
        self.players_ship = self.game.players_ship
        self.hit_marker = pygame.transform.scale(HIT_MARKER, (70, 70))

        #sound
        self.bomb_sound = pygame.mixer.Sound('audio/bomb_sound.wav')
        self.miss_sound = pygame.mixer.Sound('audio/miss.wav')
        self.bomb_sound.set_volume(0.1)
        self.miss_sound.set_volume(0.1)


    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
                    
            self.player.attack(pos,self.ai.ai_ships)  
            
            y,x = self.ai.select_target(self.attacked_pos)
            
            self.attacked_pos.add((x*TILE+70,y*TILE+70))

            # Check whether the shot hits or misses
            if (x*TILE+70,y*TILE+70) in self.players_ship:
                self.ai.update_probabilities(y, x, True,self.attacked_pos,self.ships)
                self.hits += 1
                self.bomb_sound.play()
                        
            else:
                self.ai.update_probabilities(y, x, False,self.attacked_pos,self.ships)
                self.miss_sound.play()

            if self.hits == 15 or self.player.destroyed == 15:
                self.game.switch_screen(self.game.gameset_screen)

    def draw(self):
        self.win.fill(WHITE)
        self.map.draw(True)

        for ship in self.ships:
            self.win.blit(ship.image, ship.rect)

        for x,y in self.player.attacked_positions:
            if (x,y) in self.ai_ships:
                self.win.blit(self.hit_marker, (x, y))
            else:
                pygame.draw.circle(self.win,BLACK,(x+TILE/2,y+TILE/2),TILE/2)

        for x,y in self.attacked_pos:
            if (x,y) in self.players_ship:
                self.win.blit(self.hit_marker, (x, y))
            else:
                pygame.draw.circle(self.win,BLACK,(x+TILE/2,y+TILE/2),TILE/2)

class Game_Set(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.win = self.game.win
        self.hit_marker = pygame.transform.scale(HIT_MARKER, (70, 70))
        self.restart_button = Button(980, 800, 250, 100, 'ReStart Game')
        self.exit_button = Button(1250, 800, 250, 100, 'Exit')
        self.victory_message = Message(HALF_WIDTH - 1000, HALF_HEIGHT - 250, 2000, 500, "You Win!!")
        self.game_over_message = Message(HALF_WIDTH - 1000, HALF_HEIGHT - 250, 2000, 500, "Game Over....")


    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.exit_button.handle_event(event):
                self.game.restart_game()
                self.game.switch_screen(self.game.main_screen)

            elif self.restart_button.handle_event(event):
                self.game.restart_game()
                self.game.switch_screen(self.game.set_ships_screen)

    def draw(self):
        self.win.fill(WHITE)
        self.game.map.draw(True)

        for ship in self.game.ships:
            self.win.blit(ship.image, ship.rect)

        for x,y in self.game.player.attacked_positions:
            if (x,y) in self.game.ai_ships:
                self.win.blit(self.hit_marker, (x, y))
            else:
                pygame.draw.circle(self.win,BLACK,(x+TILE/2,y+TILE/2),TILE/2)

        for x,y in self.game.attacked_pos:
            if (x,y) in self.game.players_ship:
                self.win.blit(self.hit_marker, (x, y))
            else:
                pygame.draw.circle(self.win,BLACK,(x+TILE/2,y+TILE/2),TILE/2)

        if self.game.player.destroyed == 15:
            self.victory_message.draw(self.win) 

        if self.game.hits == 15:
            self.game_over_message.draw(self.win)         

        self.restart_button.draw(self.win)
        self.exit_button.draw(self.win)

        
if __name__ == '__main__':
    game = Game()
    game.run()





