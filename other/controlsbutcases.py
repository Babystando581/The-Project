import pygame


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


control_keybinds = {
    'move_up': 1073741906,
    'move_down': pygame.K_DOWN,
    'move_left': pygame.K_LEFT,
    'move_right': pygame.K_RIGHT
}
