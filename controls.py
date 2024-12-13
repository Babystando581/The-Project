import pygame

move_up = pygame.K_UP
move_down = pygame.K_DOWN
move_left = pygame.K_LEFT
move_right = pygame.K_RIGHT
def controls(action):
    if str(action) == 'up':
        return move_up
    if str(action) == 'down':
        return move_down
    if str(action) == 'left':
        return move_left
    if str(action) == 'right':
        return move_right

