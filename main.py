import pygame
import sys
import random
from controls import mapper, setter, bodge
from gravity import air_time, grounded_check, jump_start

pygame.init()

print(pygame.display.get_desktop_sizes()[0])

size = [round(0.75 * pygame.display.get_desktop_sizes()[0][0]),
        round(0.75 * pygame.display.get_desktop_sizes()[0][1])]

timer = 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)


class Block(pygame.sprite.Sprite):
    def __init__(self, coords, dimensions=None, image=None, colour=None):
        super().__init__()
        self.coords = coords
        self.rect = pygame.Rect(coords, dimensions)
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

    def draw(self):
        screen.blit(self.surf, self.coords)


class EntityGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self):
        for sprite in self.sprites():
            sprite.draw()


class Character(pygame.sprite.Sprite):
    def __init__(self, coords, img):
        super().__init__()
        self.coords = coords
        self.img = img
        self.rect = self.img.get_rect()
        self.rect_pos = coords
        self.x_movement = [False, False]

        self.y_movement = [False, False]

        self.x_speed = 0

        self.y_speed = 0

    def update(self):
        global timer
        self.y_speed = (self.y_movement[1] - self.y_movement[0]) * 15 + (0.8 * air_time(timer)) ** 1.8
        self.rect.move_ip(self.x_speed, self.y_speed)

    def draw(self):
        screen.blit(self.img, self.rect.topleft)


class Human(Character):
    def __init__(self, coords, img):
        super().__init__(coords, img)

    def move(self, movement, start):
        if start is True:
            if movement == 'up':
                self.y_movement[0] = True
            if movement == 'down':
                self.y_movement[1] = True
            if movement == 'left':
                self.x_speed -= 5
            if movement == 'right':
                self.x_speed += 5
        if start is False:
            if movement == 'up':
                self.y_movement[0] = False
            if movement == 'down':
                self.y_movement[1] = False
            if movement == 'left':
                self.x_speed += 5
            if movement == 'right':
                self.x_speed -= 5

    def collide(self, collided_sprite: Block):
        if 0 <= self.rect.bottom - collided_sprite.rect.top <= 0.15 * self.rect.height:
            self.rect.bottom = collided_sprite.rect.top

        else:
            self.move('left',False)
            self.move('right',False)


class Player(Human):
    def __init__(self, coords, img):
        super().__init__(coords, img)


mii = Human([160, 260], pygame.image.load('data/images/sample2.png').convert_alpha())

solid_group = EntityGroup()

floor = Block((0, size[1] - 30), (size[0], 30), None, (255, 255, 255))

solid_group.add(floor)

test_platform = Block((0.6*size[0], 0.65*size[1]), (200, 50), None, (100, 100, 100))

solid_group.add(test_platform)


class Game:
    def __init__(self):
        global size
        pygame.display.set_caption("Celeste clone")

        self.clock = pygame.time.Clock()

        self.background = pygame.Surface(size)

        print(pygame.display.Info())

        self.angle = 0

    def run(self):
        global size
        global timer
        print('WOAH', backgroundcolour := (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        while True:
            mii.update()
            if collision := pygame.sprite.spritecollide(mii, solid_group, dokill=False):
                grounded_check(True)
                for sprite in collision:
                    mii.collide(sprite)
            else:
                grounded_check(False)
            timer += 0.2
            screen.fill(backgroundcolour)
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    print('a')
                    print(floor.rect.bottom)
                    size = screen.get_size()
                    print(floor.rect.bottom)
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
                        mii.rect.bottom = size[1] - floor.dimensions[1]
                    if event.key == pygame.K_f:
                        floor.rect.bottom -= 10
                        print(floor.rect.bottom)
                if event.type == pygame.KEYUP:
                    if event.key == mapper('up') and pygame.sprite.spritecollide(mii, solid_group, dokill=False) is True:
                        mii.move('up', False)
                    if event.key == mapper('down'):
                        mii.move('down', False)
                    if event.key == mapper('left'):
                        mii.move('left', False)
                    if event.key == mapper('right'):
                        mii.move('right', False)

            mii.rect.clamp_ip(self.background.get_rect())
            solid_group.draw()
            screen.blit(mii.img, mii.rect.topleft)
            pygame.display.update()
            print(mii.y_speed == 0)
            self.clock.tick(60)


Game().run()
