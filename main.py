import pygame
import sys
import random
from controls import mapper, setter, bodge
from gravity import air_time, jumping_bodge

size = [0, 0]


class Block:
    def __init__(self, coords, dimensions=None, image=None, colour=None):
        self.coords = coords
        if image:
            self.surf = pygame.image.load(image).convert()
        else:
            self.dimensions = dimensions
            self.surf = pygame.Surface(self.dimensions)
            if colour:
                self.surf.fill(colour)
            else:
                self.surf.blit(
                    pygame.image.load('data/images/source_mod.png').subsurface(pygame.Rect((0, 0), self.dimensions)),
                    (0, 0))

        self.hitbox = pygame.Rect(coords, dimensions)

        if not colour:
            self.colour = (255, 255, 255)


floor = Block((0, 720 - 30), (1280, 30), None, None)
tester = Block((0, 0), (30, 30))


class Game:
    def __init__(self):
        global size
        pygame.init()
        pygame.display.set_caption("Celeste clone")
        self.screen = pygame.display.set_mode(size := (1280, 720))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load('data/images/sample2.png').convert()
        self.img.set_colorkey((0, 0, 0))
        self.hitbox_pos = [160, 260]

        self.hitbox = self.img.get_rect()

        self.x_movement = [False, False]

        self.y_movement = [False, False]

        self.x_speed = 0

        self.y_speed = 0

        self.background = pygame.Surface(size)

        print(pygame.display.Info())

        self.angle = 0

    def run(self):
        global size
        print('WOAH', backgroundcolour := (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        timer = 0

        while True:
            timer += 0.2
            self.x_speed = (self.x_movement[1] - self.x_movement[0]) * 6
            if pygame.Rect.colliderect(self.hitbox, floor.hitbox) is True:
                self.y_speed = 0
            else:
                self.y_speed = ((self.y_movement[1] - self.y_movement[0]) * 15) + (0.8 * (air_time(timer))) ** 1.8
            self.screen.fill(backgroundcolour)
            self.hitbox.move_ip(self.x_speed, self.y_speed)
            if pygame.Rect.colliderect(self.hitbox, floor.hitbox) is True:
                jumping_bodge(True)
                self.hitbox.bottom = size[1] - floor.dimensions[1]
                self.y_movement[0] = False
            else:
                jumping_bodge(False)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    setter('move_up', event)
                    # print('Down:', event.key)
                    if event.key == mapper('up'):
                        self.y_movement[0] = True
                    if event.key == mapper('down'):
                        self.y_movement[1] = True
                    if event.key == mapper('left'):
                        self.x_movement[0] = True
                    if event.key == mapper('right'):
                        self.x_movement[1] = True
                    if event.key == pygame.K_q:
                        bodge()
                    if event.key == pygame.K_END:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYUP:
                    # print('Up:', event.key)
                    if event.key == mapper('up') and pygame.Rect.colliderect(self.hitbox, floor.hitbox) is True:
                        self.y_movement[0] = False
                    if event.key == mapper('down'):
                        self.y_movement[1] = False
                    if event.key == mapper('left'):
                        self.x_movement[0] = False
                    if event.key == mapper('right'):
                        self.x_movement[1] = False

            self.hitbox.clamp_ip(self.background.get_rect())
            self.screen.blit(floor.surf, floor.coords)
            self.screen.blit(self.img, self.hitbox.topleft)
            self.screen.blit(tester.surf, tester.coords)
            pygame.display.update()
            self.clock.tick(60)


Game().run()
