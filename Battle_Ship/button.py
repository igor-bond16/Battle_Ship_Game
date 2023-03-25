import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, font_size=30,color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.rendered_text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.rendered_text, self.rendered_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    

class Message(Button):
    def __init__(self, x, y, width, height, text, font_size=200,color=(50,50,50)):
        super().__init__(x, y, width, height, text, font_size,color)

    def draw(self, surface):
        super().draw(surface)