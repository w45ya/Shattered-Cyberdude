import pygame
import pyganim
from blocks import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.start_x = x
        self.start_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.max_speed = 3
        self.jump_power = -10
        self.gravity = 0.35
        self.on_ground_left = False
        self.on_ground_right = False
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x, y, 32, 32)
        self.win = False
        self.image.set_colorkey((255, 255, 255))

    def death(self, entities):
        self.vel_x = 0
        self.vel_y = 0
        self.teleporting(self.start_x, self.start_y)
        for e in entities:
            if isinstance(e, Button):
                for i in entities:
                    if isinstance(i, Door) and e.connect == i.connect:
                        e.pressed = False
                        i.open = False
                        e.image = e.image_unpressed
                        i.image = i.texture

    def teleporting(self, go_to_x, go_to_y):
        self.rect.x = go_to_x
        self.rect.y = go_to_y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class PlayerLeft(Player):
    def update(self, move, up, entities, sound):
        self.image = pygame.image.load('resources/textures/dude_left.png')
        if up and self.on_ground_left:
            self.vel_y = self.jump_power
            sound[0].play()
        if move:
            self.vel_x += self.max_speed
        if not move:
            self.vel_x = 0
        if not self.on_ground_left:
            self.vel_y += self.gravity
        self.on_ground_left = False
        if self.vel_x > self.max_speed:
            self.vel_x = self.max_speed
        if self.rect.y > 5000:
            self.death(entities)
        self.rect.y += self.vel_y
        self.collide(0, self.vel_y, entities, sound)
        self.rect.x += self.vel_x
        self.collide(self.vel_x, 0, entities, sound)

    def collide(self, vel_x, vel_y, entities, sound):
        for e in entities:
            if pygame.sprite.collide_rect(self, e):
                if isinstance(e, Block) or (isinstance(e, Door) and not e.open):
                    if vel_x > 0:
                        self.rect.right = e.rect.left
                    if vel_x < 0:
                        self.rect.left = e.rect.right
                    if vel_y > 0:
                        self.rect.bottom = e.rect.top
                        self.on_ground_left = True
                        self.vel_y = 0
                    if vel_y < 0:
                        self.rect.top = e.rect.bottom
                        self.vel_y = 0
                if isinstance(e, DeathBlock):
                    self.death(entities)
                    for i in entities:
                        if isinstance(i, PlayerRight):
                            i.death(entities)
                if isinstance(e, PlayerRight):
                    self.vel_x = 0
                    self.vel_y = 0
                    e.vel_x = 0
                    e.vel_y = 0
                    self.teleporting(e.rect.x-4, e.rect.y)
                    self.win = True
                if isinstance(e, TeleportIn):
                    for i in entities:
                        if isinstance(i, TeleportOut) and e.connect == i.connect:
                            self.teleporting(i.rect.x, i.rect.y)
                    sound[2].play()
                if isinstance(e, Button):
                    if not e.pressed:
                        sound[1].play()
                    for i in entities:
                        if isinstance(i, Door) and e.connect == i.connect:
                            e.pressed = True
                            i.open = True
                            e.image = e.image_pressed
                            i.image = pygame.Surface((SIZE, SIZE))
                            i.image.set_colorkey((0, 0, 0))


class PlayerRight(Player):
    def update(self, move, up, entities, sound):
        self.image = pygame.image.load('resources/textures/dude_right.png')
        if up and self.on_ground_right:
            self.vel_y = self.jump_power
        if move:
            self.vel_x -= self.max_speed
        if not move:
            self.vel_x = 0
        if not self.on_ground_right:
            self.vel_y += self.gravity
        if self.vel_x < -self.max_speed:
            self.vel_x = -self.max_speed
        if self.rect.y > 5000:
            self.death(entities)
        self.on_ground_right = False
        self.rect.y += self.vel_y
        self.collide(0, self.vel_y, entities, sound)
        self.rect.x += self.vel_x
        self.collide(self.vel_x, 0, entities, sound)

    def collide(self, vel_x, vel_y, entities, sound):
        for e in entities:
            if pygame.sprite.collide_rect(self, e):
                if isinstance(e, Block) or (isinstance(e, Door) and not e.open):
                    if vel_x > 0:
                        self.rect.right = e.rect.left
                    if vel_x < 0:
                        self.rect.left = e.rect.right
                    if vel_y > 0:
                        self.rect.bottom = e.rect.top
                        self.on_ground_right = True
                        self.vel_y = 0
                    if vel_y < 0:
                        self.rect.top = e.rect.bottom
                        self.vel_y = 0
                if isinstance(e, DeathBlock):
                    self.death(entities)
                    for i in entities:
                        if isinstance(i, PlayerLeft):
                            i.death(entities)
                if isinstance(e, TeleportIn):
                    for i in entities:
                        if isinstance(i, TeleportOut) and e.connect == i.connect:
                            self.teleporting(i.rect.x, i.rect.y)
                    sound[2].play()
                if isinstance(e, Button):
                    if not e.pressed:
                        sound[1].play()
                    for i in entities:
                        if isinstance(i, Door) and e.connect == i.connect:
                            e.pressed = True
                            i.open = True
                            e.image = e.image_pressed
                            i.image = pygame.Surface((SIZE, SIZE))
                            i.image.set_colorkey((0, 0, 0))

