import pygame
from blocks import *


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
                       "                                        ",
                       "----------------------------------------"]
        self.levels = [self.level1]

    def build_level(self, n):
        entities = pygame.sprite.Group()
        x = y = 0
        for row in self.levels[n]:
            for col in row:
                if col == "-":
                    block = Block(x, y)
                    entities.add(block)
                x += Block.size
            y += Block.size
            x = 0
        return entities
