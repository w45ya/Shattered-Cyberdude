import pygame
import pyganim

SIZE = 32


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((60, 120, 120))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.image.set_colorkey((60, 120, 120))
        self.image = pygame.image.load('resources/textures/block.png')

class DeathBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((255, 0, 0))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.image.set_colorkey((255, 0, 0))
        self.image_frame_01 = pygame.image.load('resources/textures/death_block_01.png')
        self.image_frame_02 = pygame.image.load('resources/textures/death_block_02.png')
        self.image_frame_03 = pygame.image.load('resources/textures/death_block_03.png')
        self.image_frame_04 = pygame.image.load('resources/textures/death_block_04.png')
        self.image_frame_05 = pygame.image.load('resources/textures/death_block_05.png')
        self.image_animation = [self.image_frame_01, self.image_frame_02,
                                self.image_frame_03, self.image_frame_04, self.image_frame_05]
        self.animation_delay = 50
        self.animation_array = []
        for a in self.image_animation:
            self.animation_array.append((a, self.animation_delay))
        self.animation = pyganim.PygAnimation(self.animation_array)

    def update(self, g):
        self.animation.play()
        self.game = g
        self.game.screen.blit(self.image, self.rect)
        self.animation.blit(self.image, (0, 0))


class TeleportIn(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 120, 120))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.connect = n
        self.image.set_colorkey((0, 120, 120))
        self.image_frame_01 = pygame.image.load('resources/textures/teleport_in_01.png')
        self.image_frame_02 = pygame.image.load('resources/textures/teleport_in_02.png')
        self.image_frame_03 = pygame.image.load('resources/textures/teleport_in_03.png')
        self.image_frame_04 = pygame.image.load('resources/textures/teleport_in_04.png')
        self.image_animation = [self.image_frame_01, self.image_frame_02,
                                self.image_frame_03, self.image_frame_04]
        self.animation_delay = 150
        self.animation_array = []
        for a in self.image_animation:
            self.animation_array.append((a, self.animation_delay))
        self.animation = pyganim.PygAnimation(self.animation_array)

    def update(self, g):
        self.animation.play()
        self.game = g
        self.game.screen.blit(self.image, self.rect)
        self.animation.blit(self.image, (0, 0))


class TeleportOut(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 255, 255))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.connect = n
        self.image.set_colorkey((0, 255, 255))
        self.image_frame_01 = pygame.image.load('resources/textures/teleport_out_01.png')
        self.image_frame_02 = pygame.image.load('resources/textures/teleport_out_02.png')
        self.image_frame_03 = pygame.image.load('resources/textures/teleport_out_03.png')
        self.image_frame_04 = pygame.image.load('resources/textures/teleport_out_04.png')
        self.image_animation = [self.image_frame_01, self.image_frame_02,
                                self.image_frame_03, self.image_frame_04]
        self.animation_delay = 150
        self.animation_array = []
        for a in self.image_animation:
            self.animation_array.append((a, self.animation_delay))
        self.animation = pyganim.PygAnimation(self.animation_array)

    def update(self, g):
        self.animation.play()
        self.game = g
        self.game.screen.blit(self.image, self.rect)
        self.animation.blit(self.image, (0, 0))


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE / 2))
        self.image.fill((120, 120, 120))
        self.rect = pygame.Rect(x, y, SIZE, SIZE / 2)
        self.image.set_colorkey((120, 120, 120))
        self.image_unpressed = pygame.image.load('resources/textures/button.png').convert_alpha()
        self.image_pressed = pygame.image.load('resources/textures/button_pressed.png').convert_alpha()
        self.image = self.image_unpressed
        self.connect = n
        self.pressed = False


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(x, y, SIZE, SIZE)
        self.image.set_colorkey((0, 0, 0))
        self.texture = pygame.image.load('resources/textures/door.png')
        self.image = self.texture
        self.connect = n
        self.open = False
