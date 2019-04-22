import pygame
import os
from pygame.locals import *
import sys
import math
import random

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

class Ball(pygame.sprite.Sprite):

    def __init__(self, vector, area):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        self.rect.centerx = area.centerx
        self.rect.centery = area.centery
        self.vector = vector
        self.area = area

    def bounce(self):
        self.vector = self.vector.reflect((1, 0))

    def update(self):      
        if self.rect.right > self.area.right or self.rect.left < 0:
            self.vector = self.vector.reflect((1, 0))
        if self.rect.bottom > self.area.bottom or self.rect.top < 0:
            self.vector = self.vector.reflect((0, 1))            
        self.rect = self.rect.move(self.vector.x, self.vector.y)

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

    def keydown(self, key):
        if key == K_q:
            self.move_up()
        if key == K_a:
            self.move_down()

    def keyup(self, keys):
        if not (keys[K_q] or keys[K_a]):
            self.stop()



class RightPaddle(Paddle):

    def __init__(self, area):
        Paddle.__init__(self, area, 'paddle_right.png')
        self.rect = self.rect.move(area.right - 65, 0)     
  
    def keydown(self, key):
        if key == K_UP:
            self.move_up()
        if key == K_DOWN:
            self.move_down()
    
    def keyup(self, keys):
        if not (keys[K_UP] or keys[K_DOWN]):
            self.stop()

def main():
    pygame.init();
    
    screen = pygame.display.set_mode((737, 479), 0, 32);
    background = Background()
    background_sprite = pygame.sprite.RenderPlain(background)
    background_sprite.draw(screen)

    vec = pygame.math.Vector2()
    vec.from_polar((7, random.randint(30, 80)))
    ball = Ball(vec, screen.get_rect());

    left_paddle = LeftPaddle(screen.get_rect())
    right_paddle = RightPaddle(screen.get_rect())
    
    ball_sprite = pygame.sprite.RenderPlain(ball)
    paddle_sprites = pygame.sprite.RenderPlain(left_paddle, right_paddle)    

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                left_paddle.keydown(event.key)
                right_paddle.keydown(event.key)           
            elif event.type == KEYUP:
                keys = pygame.key.get_pressed() 
                left_paddle.keyup(keys)
                right_paddle.keyup(keys)                   
            
        screen.blit(background.image, ball.rect, ball.rect)
        screen.blit(background.image, left_paddle.rect, left_paddle.rect)
        screen.blit(background.image, right_paddle.rect, right_paddle.rect)

        if (ball.rect.colliderect(left_paddle.rect) and 
            ball.vector.x < 0 and 
            abs(ball.rect.left - left_paddle.rect.right) < 5):
            ball.bounce()

        if (ball.rect.colliderect(right_paddle.rect) and 
            ball.vector.x > 0 and 
            abs(ball.rect.right - right_paddle.rect.left) < 5):
            ball.bounce()

        ball.update()
        paddle_sprites.update()
            
        ball_sprite.draw(screen)
        paddle_sprites.draw(screen);
        pygame.display.flip()

if __name__ == '__main__':
    main()