import pygame
import os
from pygame.locals import *
import sys
import math
import random
from paddles import LeftPaddle, RightPaddle
from ball import Ball
from life_bar import LifeBar
from utils import load_png, Background

def main():
    pygame.init();
    
    screen = pygame.display.set_mode((737, 479), 0, 32);
    background = Background()
    background_sprite = pygame.sprite.RenderPlain(background)
    background_sprite.draw(screen)

    vec = pygame.math.Vector2()
    vec.from_polar((7, random.randint(30, 80)))
    ball = Ball(vec)
    ball.center(screen.get_rect())

    left_paddle = LeftPaddle(screen.get_rect())
    right_paddle = RightPaddle(screen.get_rect())
    left_life_bar = LifeBar(screen.get_rect(), 'left')
    right_life_bar = LifeBar(screen.get_rect(), 'right')
    
    ball_sprite = pygame.sprite.RenderPlain(ball)
    paddle_sprites = pygame.sprite.RenderPlain(left_paddle, right_paddle)    
    life_bar_sprites = pygame.sprite.RenderPlain(left_life_bar, right_life_bar)


    clock=pygame.time.Clock()
    
    while 1:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                key = event.key
                if key == K_q:
                    left_paddle.move_up()
                if key == K_a:
                    left_paddle.move_down()
                if key == K_UP:
                    right_paddle.move_up()
                if key == K_DOWN:
                    right_paddle.move_down()                    
            elif event.type == KEYUP:
                keys = pygame.key.get_pressed()
                if not (keys[K_q] or keys[K_a]):
                    left_paddle.stop()
                if not (keys[K_UP] or keys[K_DOWN]):
                    right_paddle.stop()          

        screen.blit(background.image, ball.rect, ball.rect)
        screen.blit(background.image, left_paddle.rect, left_paddle.rect)
        screen.blit(background.image, right_paddle.rect, right_paddle.rect)

        handle_ball_bounce_from_walls(ball, screen.get_rect())
        handle_ball_bounce_from_paddle(ball, left_paddle, right_paddle)
        handle_missed_ball(ball, screen.get_rect(), left_life_bar, right_life_bar)

        ball.update()
        paddle_sprites.update()
            
        ball_sprite.draw(screen)
        paddle_sprites.draw(screen);
        life_bar_sprites.draw(screen);
        
        pygame.display.flip()



def handle_ball_bounce_from_paddle(ball, left_paddle, right_paddle):
    if (ball.rect.colliderect(left_paddle.rect) and 
        ball.vector.x < 0):
        ball.bounceX()

    if (ball.rect.colliderect(right_paddle.rect) and 
        ball.vector.x > 0 and 
        abs(ball.rect.right - right_paddle.rect.left) < 5):
        ball.bounceX()


def handle_ball_bounce_from_walls(ball, area):
    if ball.rect.right > area.right or ball.rect.left < 0:
        ball.bounceX()
    if ball.rect.bottom > area.bottom or ball.rect.top < 0:
        ball.bounceY()

def handle_missed_ball(ball, area, left_life_bar, right_life_bar):
    if ball.rect.right > area.right:
        right_life_bar.consume(1)
    if ball.rect.left < 0:
        left_life_bar.consume(1)        

if __name__ == '__main__':
    main()