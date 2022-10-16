import abc
import pygame
import os
from Setup import *
from LoadPlayer import *

# from Main import player

WALL_SIZE = 64


class Object:
    # __metaclass__ = abc.ABCMeta

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = self.height = 64

        # rect representing hitbox
        self.object = pygame.Rect(self.x - player.x, self.y - player.y, WALL_SIZE, WALL_SIZE)

        # default texture = None -> black square
        self.texture = None
        self.wall = False

    def draw(self, surface):
        # Offset because player position is (512, 384) on the screen relative to top left corner
        pos_x = self.x - player.x + 512
        pos_y = self.y - player.y + 384
        if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
            self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
            if self.texture is not None:
                surface.blit(self.texture, self.object)
            else:
                pygame.draw.rect(surface, (0, 0, 0), self.object)


class Wall(Object):
    def __init__(self, x, y, is_base):
        super().__init__(x, y)
        self.color = (128, 128, 128)
        self.width = WALL_SIZE
        self.height = WALL_SIZE
        self.texture = pygame.image.load(os.path.join('src', 'textures', 'Wall-base-64px-1.png' if is_base else 'Wall-64px-1.png'))
        self.wall = True


class Box(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = pygame.image.load(os.path.join('src', 'objects', 'box.png'))


class Win(Object):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, surface):
        pos_x = self.x - player.x + 512
        pos_y = self.y - player.y + 384
        self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
        pygame.draw.rect(surface, (255, 192, 203), self.object)
        if player.x == self.x and player.y == self.y:
            game_won = True
            running = False