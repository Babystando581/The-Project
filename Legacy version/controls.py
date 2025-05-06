import pygame
def mapper(action):
    if str(action) == 'up':
        return control_keybinds['move_up']
    if str(action) == 'down':
        return control_keybinds['move_down']
    if str(action) == 'left':
        return control_keybinds['move_left']
    if str(action) == 'right':
        return control_keybinds['move_right']


listenforinput = False


def setter(mapping, event):
    global listenforinput
    global control_keybinds
    if listenforinput is True:
        control_keybinds[mapping] = event.key
        listenforinput = False
        return event.key


control_keybinds = {
    'move_up': pygame.K_UP,
    'move_down': pygame.K_DOWN,
    'move_left': pygame.K_LEFT,
    'move_right': pygame.K_RIGHT
}


def rebind():
    global listenforinput
    listenforinput = True
