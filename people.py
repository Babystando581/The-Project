import sys

import pygame

from globals import all_globals
from gravity import air_time, grounded_check
from blocks import solid_group
from blocks_storage import *


class Character(pygame.sprite.Sprite):
    def __init__(self, coords, img: pygame.image):
        super().__init__()
        self.coords = coords
        self.img = img
        self.rect = self.img.get_rect()
        self.rect_pos = coords
        self.x_movement = [False, False]

        self.y_movement = [False, False]

        self.x_speed = 0

        self.y_speed = 0
        self.grounded = True

    def update(self):
        if (0.0008 * air_time(pygame.time.get_ticks(),self.grounded)) ** 1.6 >= 35:
            self.gravity = 35
        else:
            self.gravity = (0.0008 * air_time(pygame.time.get_ticks(),self.grounded)) ** 1.8
        self.y_speed = (self.y_movement[1] - self.y_movement[0]) * 15 + self.gravity
        self.x_speed = (self.x_movement[1] - self.x_movement[0]) * 5
        old_pos = self.rect.topleft
        self.rect.move_ip(self.x_speed, self.y_speed)
        collision = pygame.sprite.spritecollide(self, solid_group, dokill=False)
        if collision is True:
            self.grounded = True
        else:
            self.grounded = False

        for sprite in collision:
            if sprite.special == 'end':
                print('YOU WIN!!!!!1!!1!!11!!')
                pygame.quit()
                sys.exit()
            if self.rect.bottom <= sprite.rect.top:
                print('colliding')
                self.rect.topleft = old_pos
            # print('invalid movement')
        else:
            ...
            # print('valid movement')
        self.rect.clamp_ip(all_globals['screen_rect'])

    def draw(self):
        all_globals['screen'].blit(self.img, self.rect.topleft)


class Human(Character):
    def __init__(self, coords, img):
        super().__init__(coords, img)

    def move(self, movement, start):
        if start is True:
            if movement == 'up':
                self.y_movement[0] = True
            if movement == 'down':
                self.y_movement[1] = True
            if movement == 'left':
                self.x_movement[0] = True
            if movement == 'right':
                self.x_movement[1] = True
        if start is False:
            if movement == 'up':
                self.y_movement[0] = False
            if movement == 'down':
                self.y_movement[1] = False
            if movement == 'left':
                self.x_movement[0] = False
            if movement == 'right':
                self.x_movement[1] = False

    # def collide(self, collided_sprite: Block):
    #    if collided_sprite.special == 'end':
    #        print('YOU WIN!!!!!1!!1!!11!!')
    #        pygame.quit()
    #        sys.exit()
    #    if 0 <= self.rect.bottom - collided_sprite.rect.top <= 0.5 * self.rect.height:
    #        self.rect.bottom = collided_sprite.rect.top
    #    else:
    #        self.move('left', False)
    #        self.move('right', False)
    #        self.x_speed = 0


class Player(Human):
    def init__(self, coords, img):
        super().__init__(coords, img)
