from enum import Enum
from Setup import *

FRICTION = 0.9
SPEED = 1

images = ["", "slime-v01-right.png", "slime-v01-left.png", "slime-v01-down.png", "slime-v01-up.png"]

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
        self.image = update_image(Direction.UP);

    def draw(self):
        self.velocity_y *= FRICTION
        self.velocity_x *= FRICTION
        self.x += self.velocity_x
        self.y += self.velocity_y
        pygame.image.load(self.image).convert()

    def right(self):
        if self.direction == Direction.RIGHT:
            self.velocity_x = SPEED
            update_image(Direction.RIGHT)

    def left(self):
        if self.direction == Direction.LEFT:
            self.velocity_x = -SPEED
            update_image(Direction.LEFT)

    def down(self):
        if self.direction == Direction.DOWN:
            self.velocity_y = SPEED
            update_image(Direction.DOWN)

    def up(self):
        if self.direction == Direction.UP:
            self.velocity_y = -SPEED
            update_image(Direction.UP)



def update_image(direction):
    self.image = "src" + system_nav + images[direction]