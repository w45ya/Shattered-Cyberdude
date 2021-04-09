import pygame
SIZE = 32


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((60, 120, 120))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)


class DeathBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)