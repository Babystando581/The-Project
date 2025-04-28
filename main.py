import pygame
pygame.init()
import sys
import random
from controls import mapper, setter, bodge
from gravity import air_time
from blocks import Block, EntityGroup, solid_group
from globals import all_globals
from blocks_storage import *
from people import *

pygame.init()

all_globals['size'] = round(0.75 * pygame.display.Info().current_w), round(0.75 * pygame.display.Info().current_h)

all_globals['screen'] = pygame.display.set_mode(all_globals['size'], pygame.RESIZABLE)

all_globals['screen_rect'] = all_globals['screen'].get_rect()

mii = Human([160, 260], pygame.image.load('data/images/sample2.png'))

all_globals['game_framerate'] = 144

prev_time = pygame.time.get_ticks()

class Game:
    def __init__(self):
        pygame.display.set_caption("Celeste clone")

        self.clock = pygame.time.Clock()

        self.background = pygame.Surface(all_globals['size'])

        print(pygame.display.Info())

        self.angle = 0

    def run(self):
        global prev_time
        print('WOAH', backgroundcolour := (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        while True:
            mii.update()
            now_time = pygame.time.get_ticks()
            all_globals['dt'] = (now_time - prev_time)/1000
            prev_time = now_time
            all_globals['screen'].fill(backgroundcolour)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    size = all_globals['screen'].get_size()
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
                        mii.rect.bottom = all_globals['size'][1] - floor.dimensions[1]
                if event.type == pygame.KEYUP:
                    if event.key == mapper('up'):
                        mii.move('up', False)
                    if event.key == mapper('down'):
                        mii.move('down', False)
                    if event.key == mapper('left'):
                        mii.move('left', False)
                    if event.key == mapper('right'):
                        mii.move('right', False)
            solid_group.draw()
            all_globals['screen'].blit(mii.img, mii.rect.topleft)
            pygame.display.update()
            #print('dt is',all_globals['dt'])
            all_globals['dt'] = self.clock.tick(all_globals['game_framerate'])


Game().run()
