from enum import Enum
from Setup import *
import platform
import pygame
import math
import os

SPEED = 4
START_X = 512
START_Y = 384

images = ["slime-right.png", "slime-left.png", "slime-down.png", "slime-up.png"]

class Direction(Enum):
    NONE = 0
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4


class Player:
    def __init__(self):
        self.x = START_X
        self.y = START_Y
        self.direction = Direction.UP
        self.update_image(3)

    def draw(self, screen):
        img = pygame.transform.scale(pygame.image.load(self.image),(48,48))
        #img = pygame.image.load(self.image)
        screen.blit(img, (SCREEN_WIDTH/2 - 24, SCREEN_HEIGHT/2 - 32))

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
        self.image = os.path.join("src", "slime", images[direction])
        # self.image = "Users/ezra/Documents/DandyHacks2022/src/slime-v01-right.png"
        # print(self.image)
