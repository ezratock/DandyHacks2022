from enum import Enum

FRICTION = 0.9
SPEED = 1

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

    def update(self):
        self.velocity_y *= FRICTION
        self.velocity_x *= FRICTION
        self.x += self.velocity_x
        self.y += self.velocity_y

    def right(self):
        if self.direction == Direction.RIGHT:
            self.velocity_x = SPEED

    def left(self):
        if self.direction == Direction.LEFT:
            self.velocity_x = -SPEED

    def down(self):
        if self.direction == Direction.DOWN:
            self.velocity_y = SPEED

    def up(self):
        if self.direction == Direction.UP:
            self.velocity_y = -SPEED