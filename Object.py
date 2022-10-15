import abc
import pygame
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

    def draw(self, surface):
        self.object = pygame.Rect(self.x-player.x, self.y-player.y, WALL_SIZE, WALL_SIZE)
        pygame.draw.rect(surface, self.color, self.object)



