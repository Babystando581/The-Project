import pygame
import sys
import random
from controls import mapper, setter, bodge
from gravity import air_time, grounded_check, jump_start
from blocks import Block, EntityGroup
from globals import all_globals

pygame.init()

print(pygame.display.get_desktop_sizes()[0])

size = round(0.75 * pygame.display.Info().current_w), round(0.75 * pygame.display.Info().current_h)

timer = 0

all_globals['screen'] = pygame.display.set_mode(size, pygame.RESIZABLE)


class Character(pygame.sprite.Sprite):
    def __init__(self, coords, img: pygame.image):
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
        if (0.8 * air_time(timer)) ** 1.8 >= 30:
            self.gravity = 30
        else:
            self.gravity = (0.8 * air_time(timer)) ** 1.8
        print(self.gravity)
        self.y_speed = (self.y_movement[1] - self.y_movement[0]) * 15 + self.gravity
        self.x_speed = (self.x_movement[1] - self.x_movement[0]) * 5
        old_pos = self.rect.topleft
        self.rect.move_ip(self.x_speed, self.y_speed)
        if collision := pygame.sprite.spritecollide(self, solid_group, dokill=False) is True:
            #for sprite in collision:
                #print(sprite)
            grounded_check(True)
            print(self.rect.topleft, old_pos)
            self.rect.topleft = old_pos
            #print('invalid movement')
        else:
            grounded_check(False)
            #print('valid movement')

    def draw(self):
        all_globals['screen'].blit(self.img, self.rect.topleft)


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
                self.x_movement[0] = True
            if movement == 'right':
                self.x_movement[1] = True
        if start is False:
            if movement == 'up':
                self.y_movement[0] = False
            if movement == 'down':
                self.y_movement[1] = False
            if movement == 'left':
                self.x_movement[0] = False
            if movement == 'right':
                self.x_movement[1] = False

    def collide(self, collided_sprite: Block):
        if collided_sprite.special == 'end':
            print('YOU WIN!!!!!1!!1!!11!!')
            pygame.quit()
            sys.exit()
        if 0 <= self.rect.bottom - collided_sprite.rect.top <= 0.5 * self.rect.height:
            self.rect.bottom = collided_sprite.rect.top
        else:
            self.move('left', False)
            self.move('right', False)
            self.x_speed = 0


class Player(Human):
    def init__(self, coords, img):
        super().__init__(coords, img)


mii = Human([160, 260], pygame.image.load('data/images/sample2.png'))

solid_group = EntityGroup()

floor = Block((0, size[1] - 30), (size[0], 30), None, (255, 255, 255))

solid_group.add(floor)

test_platform_1 = Block((0.2 * size[0], 0.85 * size[1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_1)

test_platform_2 = Block((0.4 * size[0], 0.8 * size[1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_2)

test_platform_3 = Block((0.6 * size[0], 0.75 * size[1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_3)

goal = Block((size[0] - 50, size[1] - (50 + floor.dimensions[1])), (50, 50), None, (250, 0, 0), 'end')

solid_group.add(goal)


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
                mii.move('up', False)
                for sprite in collision:
                    mii.collide(sprite)
            else:
                grounded_check(False)
            timer += 0.2
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
                        mii.rect.bottom = size[1] - floor.dimensions[1]
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
            all_globals['screen'].blit(mii.img, mii.rect.topleft)
            pygame.display.update()
            self.clock.tick(60)


Game().run()
