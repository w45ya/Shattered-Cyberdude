import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.vel_x = 0
        self.vel_y = 0
        self.max_speed = 10
        self.jump_power = -10
        self.gravity = 0.35
        self.on_ground = False
        self.flipped = False
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(x, y, 32, 32)
        #self.image.set_colorkey((32, 64, 64))

    def death(self):
        self.vel_x = 0
        self.vel_y = 0
        self.teleporting(self.start_x, self.start_y)

    def teleporting(self, go_to_x, go_to_y):
        self.rect.x = go_to_x
        self.rect.y = go_to_y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, move, up, delta):
        if up and self.on_ground:
            self.vel_y = self.jump_power


class PlayerLeft(Player):
    def update(self, move, up, delta):
        if up and self.on_ground:
            self.vel_y = self.jump_power
        if move:
            self.vel_x += self.max_speed * delta
        if not move:
            self.vel_x = 0
        if not self.on_ground:
            self.vel_y += self.gravity
        if self.rect.y > 5000:
            self.death()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class PlayerRight(Player):
    def update(self, move, up, delta):
        if up and self.on_ground:
            self.vel_y = self.jump_power
        if move:
            self.vel_x -= self.max_speed * delta
        if not move:
            self.vel_x = 0
        if not self.on_ground:
            self.vel_y += self.gravity
        if self.rect.y > 5000:
            self.death()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
