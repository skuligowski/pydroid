import pygame
from utils import load_png

LIFE_AMOUNT = 5
MAX_LIFE_AMOUNT = 5
LIFE_COLOR = 0, 204, 0
BAR_FILENAME = 'life_bar.png'
BORDER_WIDTH = 3

class LifeBar(pygame.sprite.Sprite):
        
    life_amount = MAX_LIFE_AMOUNT

    def __init__(self, area, side):
        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.background, self.rect = load_png(BAR_FILENAME)        
        self.rect.top = 20
        if side == 'left':
            self.rect.right = area.centerx - 10
        elif side == 'right':
            self.rect.left = area.centerx + 10
        self.paint()

    def paint(self):
        width = self.rect.width - 2*BORDER_WIDTH
        ratio = self.life_amount / MAX_LIFE_AMOUNT
        life_bar = pygame.surface.Surface((ratio * width, self.rect.height-2*BORDER_WIDTH))
        life_bar.fill(LIFE_COLOR)
        self.image = self.background.copy()
        self.image.blit(life_bar, (BORDER_WIDTH, BORDER_WIDTH))
        if self.side == 'right':
            self.image = pygame.transform.flip(self.image, True, False)
        
    def consume(self, amount):
        self.life_amount = self.life_amount - amount        
        self.paint()