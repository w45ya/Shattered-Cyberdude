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


class TeleportIn(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 120, 120))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.connect = n


class TeleportOut(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 255, 255))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.connect = n


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE/2))
        self.image.fill((120, 120, 120))
        self.rect = pygame.Rect(x, y + SIZE/2, SIZE, SIZE/2)
        self.connect = n
        self.pressed = False


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.connect = n
        self.open = False
