from enum import Enum
from Setup import *
import platform
import pygame

FRICTION = 0.9
SPEED = 1

system_nav = "/" if platform.system() == 'Darwin' else "\\"

images = ["slime-v01-right.png", "slime-v01-left.png", "slime-v01-down.png", "slime-v01-up.png"]

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
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = Direction.UP;
        self.update_image(3);

    def draw(self, screen):
        self.velocity_y *= FRICTION
        self.velocity_x *= FRICTION
        self.x += self.velocity_x
        self.y += self.velocity_y
        img = pygame.image.load(self.image).convert()
        screen.blit(img, (0, 0))

    def right(self):
        if self.direction == Direction.RIGHT:
            self.velocity_x = SPEED
            self.update_image(0)

    def left(self):
        if self.direction == Direction.LEFT:
            self.velocity_x = -SPEED
            self.update_image(1)

    def down(self):
        if self.direction == Direction.DOWN:
            self.velocity_y = SPEED
            self.update_image(2)

    def up(self):
        if self.direction == Direction.UP:
            self.velocity_y = -SPEED
            self.update_image(3)

    def update_image(self, direction):
        self.image = "src" + system_nav + images[direction]
        # self.image = "Users/ezra/Documents/DandyHacks2022/src/slime-v01-right.png"
        # print(self.image)