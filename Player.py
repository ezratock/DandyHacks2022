from enum import Enum
import platform
import pygame
from Setup import *
import math

SPEED = 2

#SHOULD BE IN SETUP.PY
system_nav = "/" if platform.system() == 'Darwin' else "\\"
SCREEN_WIDTH = 1088
SCREEN_HEIGHT = 832

images = ["slime-right.png", "slime-left.png", "slime-down.png", "slime-up.png"]

class Direction(Enum):
    NONE = 0
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.UP
        self.update_image(3)

    def draw(self, screen):
        img = pygame.image.load(self.image)
        screen.blit(img, (SCREEN_WIDTH/2 - 32, SCREEN_HEIGHT/2 - 32))

    def right(self):
        self.x += SPEED
        self.update_image(0)

    def left(self):
        self.x -= SPEED
        self.update_image(1)

    def down(self):
        self.y += SPEED
        self.update_image(2)

    def up(self):
        self.y -= SPEED
        self.update_image(3)

    def on_grid(self):
        return self.x % 64 == 0 and self.y % 64 == 0


    def update_image(self, direction):
        self.image = "src" + system_nav + "slime" + system_nav + images[direction]
        # self.image = "Users/ezra/Documents/DandyHacks2022/src/slime-v01-right.png"
        # print(self.image)
