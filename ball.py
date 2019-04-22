import pygame
from utils import load_png

class Ball(pygame.sprite.Sprite):

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        self.vector = vector

    def center(self, container_rect):
        self.rect.centerx = container_rect.centerx
        self.rect.centery = container_rect.centery 

    def bounceX(self):
        self.vector = self.vector.reflect((1, 0))

    def bounceY(self):
        self.vector = self.vector.reflect((0, 1))

    def update(self):      
        self.rect = self.rect.move(self.vector.x, self.vector.y)