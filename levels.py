import pygame
import blocks
from player import *

class Levels:
    def __init__(self):
        self.level1 = ["----------------------------------------",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "--------X  12                          -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-             X                        -",
                       "----------------------------------------"]
        self.level2 = ["----------------------------------------",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "----------------------------------------"]
        self.level3 = ["----------------------------------------",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "-                                      -",
                       "----------------------------------------"]
        self.player1 = [100, 100, 1200, 600]
        self.player2 = [50, 50, 1200, 600]
        self.player3 = [50, 50, 1200, 600]
        self.levels = [self.level1, self.level2, self.level3]
        self.players = [self.player1, self.player2, self.player3]

    def build_level(self, n):
        entities = pygame.sprite.Group()
        player_left = PlayerLeft(self.players[n][0], self.players[n][1])
        player_right = PlayerRight(self.players[n][2], self.players[n][3])
        entities.add(player_left, player_right)
        x = y = 0
        for row in self.levels[n]:
            for col in row:
                if col == "-":
                    block = Block(x, y)
                    entities.add(block)
                if col == "X":
                    block = DeathBlock(x, y)
                    entities.add(block)
                if col == "1":
                    block = TeleportIn(x, y, 1)
                    entities.add(block)
                if col == "2":
                    block = TeleportOut(x, y, 1)
                    entities.add(block)
                if col == "3":
                    block = TeleportIn(x, y, 2)
                    entities.add(block)
                if col == "4":
                    block = TeleportOut(x, y, 2)
                    entities.add(block)
                if col == "5":
                    block = TeleportIn(x, y, 3)
                    entities.add(block)
                if col == "6":
                    block = TeleportOut(x, y, 3)
                    entities.add(block)
                if col == "7":
                    block = TeleportIn(x, y, 4)
                    entities.add(block)
                if col == "8":
                    block = TeleportOut(x, y, 4)
                    entities.add(block)
                if col == "B":
                    block = Button(x, y, 1)
                    entities.add(block)
                if col == "D":
                    block = Door(x, y, 1)
                    entities.add(block)
                if col == "b":
                    block = Button(x, y, 2)
                    entities.add(block)
                if col == "d":
                    block = Door(x, y, 2)
                    entities.add(block)
                x += blocks.SIZE
            y += blocks.SIZE
            x = 0
        return entities
