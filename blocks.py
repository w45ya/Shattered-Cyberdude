import pygame


class Block(pygame.sprite.Sprite):
    size = 32

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((60, 120, 120))
        self.rect = pygame.Rect(x, y, self.size, self.size)
