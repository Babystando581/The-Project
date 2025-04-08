import pygame
from globals import a_g


class Block(pygame.sprite.Sprite):
    def __init__(self, coords, dimensions=None, image=None, colour=None, special=None):
        super().__init__()
        self.coords = coords
        self.rect = pygame.Rect(coords, dimensions)
        self.special = special
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
        a_g['screen'].blit(self.surf, self.coords)


class EntityGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self):
        for sprite in self.sprites():
            sprite.draw()


solid_group = EntityGroup()