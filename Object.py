import abc
import pygame
import os
from Setup import *

# from Main import player

WALL_SIZE = 50

class Object:
    __metaclass__ = abc.ABCMeta

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def draw(self, surface):
        return

class Wall(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object = pygame.Rect(self.x-player.x, self.y-player.y, WALL_SIZE, WALL_SIZE)
        self.color = (128,128,128)
        self.width = WALL_SIZE
        self.height = WALL_SIZE

    def draw(self, surface):
        pos_x = self.x-player.x
        pos_y = self.y-player.y
        if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
            self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
            #pygame.draw.rect(surface, self.color, self.object)


class Box(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        