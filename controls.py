import pygame


def controls(action):
    if str(action) == 'up':
        return pygame.K_UP
    if str(action) == 'down':
        return pygame.K_DOWN
    if str(action) == 'left':
        return pygame.K_LEFT
    if str(action) == 'right':
        return pygame.K_RIGHT
