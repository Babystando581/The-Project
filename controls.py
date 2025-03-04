import pygame
import time


def mapper(action):
    match str(action):
        case 'up':
            return control_keybinds['move_up']
        case 'down':
            return control_keybinds['move_down']
        case 'left':
            return control_keybinds['move_left']
        case 'right':
            return control_keybinds['move_right']


listenforinput = False


def setter(mapping, event):
    global listenforinput
    global control_keybinds
    if listenforinput is True:
        control_keybinds[mapping] = event.key
        print(event.key)
        listenforinput = False
        return event.key


control_keybinds = {
    'move_up': 1073741906,
    'move_down': pygame.K_DOWN,
    'move_left': pygame.K_LEFT,
    'move_right': pygame.K_RIGHT
}


def wait():
    time.sleep(5)
    global listenforinput
    listenforinput = False


def bodge():
    global listenforinput
    listenforinput = True
