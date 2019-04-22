import pygame
from utils import load_png
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self, area, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(filename)        
        self.rect.centery = area.centery
        self.move_vector = (0, 0)
        self.area = area

    def move_up(self):
        self.move_vector = (0, -7)

    def move_down(self):        
        self.move_vector = (0, 7)

    def stop(self):
        self.move_vector = (0, 0)

    def update(self):
        new_pos = self.rect.move(self.move_vector)
        if self.area.contains(new_pos):
            self.rect = new_pos


class LeftPaddle(Paddle):

    def __init__(self, area):
        Paddle.__init__(self, area, 'paddle_left.png')
        self.rect = self.rect.move(40, 0)


class RightPaddle(Paddle):

    def __init__(self, area):
        Paddle.__init__(self, area, 'paddle_right.png')
        self.rect = self.rect.move(area.right - 65, 0)     
