import pygame


def controls(keybind):
    if str(keybind) == 'up':
        return pygame.K_UP
    if str(keybind) == 'down':
        return pygame.K_DOWN
    if str(keybind) == 'left':
        return pygame.K_LEFT
    if str(keybind) == 'right':
        return pygame.K_RIGHT