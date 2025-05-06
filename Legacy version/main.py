import pygame
import sys
import random
from controls import mapper, setter, rebind


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Celeste clone")
        self.screen = pygame.display.set_mode(size := (640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/sample2.png')
        self.img.set_colorkey((0, 0, 0))
        self.hitbox_pos = [160, 260]

        self.hitbox = self.img.get_rect()

        self.x_movement = [False, False]

        self.y_movement = [False, False]

        self.background = pygame.Surface(size)

        print(pygame.display.Info())

    def run(self):

        print(backgroundcolour := (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timer = 0
        timer_start = 0
        while True:
            timer += 1
            self.screen.fill(backgroundcolour)
            self.hitbox.move_ip((self.x_movement[1] - self.x_movement[0]) * 6,
                                ((self.y_movement[1] - self.y_movement[0]) * 6) + 1 + 1.005**(timer - timer_start))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    setter('move_up', event)
                    print('Down:', event.key)
                    if event.key == mapper('up'):
                        self.y_movement[0] = True
                        timer_start = timer
                    if event.key == mapper('down'):
                        self.y_movement[1] = True
                    if event.key == mapper('left'):
                        self.x_movement[0] = True
                    if event.key == mapper('right'):
                        self.x_movement[1] = True
                    if event.key == pygame.K_q:
                        rebind()
                if event.type == pygame.KEYUP:
                    print('Up:', event.key)
                    if event.key == mapper('up'):
                        self.y_movement[0] = False
                        timer_start = 0
                    if event.key == mapper('down'):
                        self.y_movement[1] = False
                    if event.key == mapper('left'):
                        self.x_movement[0] = False
                    if event.key == mapper('right'):
                        self.x_movement[1] = False
            self.hitbox.clamp_ip(self.background.get_rect())
            self.screen.blit(self.img, self.hitbox.topleft)
            pygame.display.update()
            self.clock.tick(60)


Game().run()