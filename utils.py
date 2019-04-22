import pygame
import os
import sys

def load_png(filename):
    try:
        image = pygame.image.load(os.path.join('data', filename))
        image = image.convert_alpha()
    except:
        print(sys.exc_info()[1])
        raise SystemExit(sys.exc_info()[1])
    return image, image.get_rect()

class Background(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('bg.jpg')    