import pygame
from blocks import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.max_speed = 3
        self.jump_power = -10
        self.gravity = 0.35
        self.on_ground_left = False
        self.on_ground_right = False
        self.flipped = False
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x, y, 32, 32)
        #self.image.set_colorkey((32, 64, 64))

    def death(self):
        self.vel_x = 0
        self.vel_y = 0
        self.teleporting(self.start_x, self.start_y)
        print("dead")
    def teleporting(self, go_to_x, go_to_y):
        self.rect.x = go_to_x
        self.rect.y = go_to_y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class PlayerLeft(Player):
    def update(self, move, up, delta, entities):
        if up and self.on_ground_left:
            self.vel_y = self.jump_power
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
            self.death()
        self.rect.y += self.vel_y
        self.collide(0, self.vel_y, entities)
        self.rect.x += self.vel_x
        self.collide(self.vel_x, 0, entities)

    def collide(self, vel_x, vel_y, entities):
        for e in entities:
            if pygame.sprite.collide_rect(self, e):
                if isinstance(e, Block):
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

class PlayerRight(Player):
    def update(self, move, up, delta, entities):
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
            self.death()
        self.on_ground_right = False
        self.rect.y += self.vel_y
        self.collide(0, self.vel_y, entities)
        self.rect.x += self.vel_x
        self.collide(self.vel_x, 0, entities)

    def collide(self, vel_x, vel_y, entities):
        for e in entities:
            if pygame.sprite.collide_rect(self, e):
                if isinstance(e, Block):
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