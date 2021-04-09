import pygame
import blocks
from player import *

class Levels:
    def __init__(self):
        self.level1 = ["----------------------------------------",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "         -   -                          ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "        ---------                       ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                            X           ",
                       "                            X           ",
                       "                            X           ",
                       "----------------------------------------"]
        self.level2 = ["----------------------------------------",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "         -   -                          ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "        ---------                       ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                                        ",
                       "                            X           ",
                       "----------------------------------------"]
        self.player1 = [50, 50, 1230, 50]
        self.player2 = [50, 50, 1230, 50]
        self.levels = [self.level1, self.level2]
        self.players = [self.player1, self.player2]

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
                x += blocks.SIZE
            y += blocks.SIZE
            x = 0
        return entities
