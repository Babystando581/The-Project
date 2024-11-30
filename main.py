import pygame
import sys
from controls import controls

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Celeste clone")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()  # eeeeeeee

        self.img = pygame.image.load('data/images/sample2.png')
        self.img.set_colorkey((0, 0, 0))

        self.img_pos = [160, 260]

        self.x_movement = [False, False]

        self.y_movement = [False, False]

    def run(self):
        while True:
            self.screen.fill(14)
            self.img_pos[0] += (self.x_movement[1] - self.x_movement[0]) * 6
            self.img_pos[1] += (self.y_movement[1] - self.y_movement[0]) * 6
            self.screen.blit(self.img, self.img_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.y_movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.y_movement[1] = True
                    if event.key == pygame.K_LEFT:
                        self.x_movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.x_movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.y_movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.y_movement[1] = False
                    if event.key == pygame.K_LEFT:
                        self.x_movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.x_movement[1] = False

            pygame.display.update()
            self.clock.tick(60)
            self.img = pygame.image.load('data/images/sample2.png')


Game().run()
