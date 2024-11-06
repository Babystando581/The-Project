import os

import pygame
import sys

# no need for a class if your only using it once???!?!?!?
# brother you are not that cool
pygame.init()

pygame.display.set_caption("Celeste clone")
screen = pygame.display.set_mode((640, 480))
screen_center = tuple(i/2 for i in screen.get_size())
clock = pygame.time.Clock()

# please use os.path.join for file paths so the linux users are happy :)
character = pygame.image.load(os.path.join('data', 'images', 'sample2.png'))
character_hitbox = character.get_rect()
# move character to the center

character_hitbox.move_ip(screen_center[0] - character.get_width() / 2,
                            screen_center[1] - character.get_height() / 2)
background = pygame.Surface(screen.get_size())
dx, dy = 0, 0

# no need for a function either fella.
while True:
    # you have to clear the screen every frame g
    screen.blit(background, (0, 0))
    # ya update events before drawing the character get it??!?!??!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # movement not perfect but making perfect is hard idc figure it out
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_UP:
                dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                dx = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                dy = 0
    character_hitbox.move_ip(dx, dy)
    # dont leave the screen buddy
    character_hitbox.clamp_ip(background.get_rect())

    screen.blit(character, character_hitbox)

    pygame.display.flip()
    clock.tick(60)
