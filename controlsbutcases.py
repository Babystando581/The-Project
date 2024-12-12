import pygame

def controlcase(action):
    match str(action):
        case 'up':
            return pygame.K_UP
        case 'down':
            return pygame.K_DOWN
        case 'left':
            return pygame.K_LEFT
        case 'right':
            return pygame.K_RIGHT



