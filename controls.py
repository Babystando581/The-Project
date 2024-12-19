import pygame


def mapper(action):
    if str(action) == 'up':
        return move_up
    if str(action) == 'down':
        return move_down
    if str(action) == 'left':
        return move_left
    if str(action) == 'right':
        return move_right


listenforinput = True


def setter(event):
    global listenforinput
    if listenforinput:
        # listenforinput = False
        return event.key


move_up = 1073741906
move_down = pygame.K_DOWN
move_left = pygame.K_LEFT
move_right = pygame.K_RIGHT
