import pygame
pygame.init()
import sys
import random
from controls import mapper, setter, bodge
from gravity import air_time
from blocks import Block, EntityGroup, solid_group
from globals import a_g
from blocks_storage import *
from people import *

pygame.init()

a_g['size'] = round(0.75 * pygame.display.Info().current_w), round(0.75 * pygame.display.Info().current_h)

a_g['screen'] = pygame.display.set_mode(a_g['size'], pygame.RESIZABLE)

a_g['screen_rect'] = a_g['screen'].get_rect()

mii = Human([160, 260], pygame.image.load('data/images/sample2.png'))

a_g['game_framerate'] = 144

prev_time = pygame.time.get_ticks()

class Game:
    def __init__(self):
        pygame.display.set_caption("Celeste clone")

        self.clock = pygame.time.Clock()

        self.background = pygame.Surface(a_g['size'])

        print(pygame.display.Info())

        self.angle = 0

    def run(self):
        global prev_time
        print('WOAH', backgroundcolour := (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        while True:
            mii.update()
            now_time = pygame.time.get_ticks()
            a_g['dt'] = (now_time - prev_time)/1000
            prev_time = now_time
            a_g['screen'].fill(backgroundcolour)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    size = a_g['screen'].get_size()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    setter('move_up', event)
                    if event.key == mapper('up'):
                        mii.move('up', True)
                    if event.key == mapper('down'):
                        mii.move('down', True)
                    if event.key == mapper('left'):
                        mii.move('left', True)
                    if event.key == mapper('right'):
                        mii.move('right', True)
                    if event.key == pygame.K_q:
                        bodge()
                    if event.key == pygame.K_END:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_s:
                        mii.img = pygame.transform.scale_by(mii.img, 1.2)
                        mii.rect.width *= 1.2
                        mii.rect.height *= 1.2
                        mii.rect.bottom = a_g['size'][1] - floor.dimensions[1]
                if event.type == pygame.KEYUP:
                    if event.key == mapper('up') and pygame.sprite.spritecollide(mii, solid_group,
                                                                                 dokill=False) is True:
                        mii.move('up', False)
                    if event.key == mapper('down'):
                        mii.move('down', False)
                    if event.key == mapper('left'):
                        mii.move('left', False)
                    if event.key == mapper('right'):
                        mii.move('right', False)
            solid_group.draw()
            a_g['screen'].blit(mii.img, mii.rect.topleft)
            pygame.display.update()
            print(a_g['dt'])
            a_g['dt'] = self.clock.tick(a_g['game_framerate'])


Game().run()
