import pygame

FRICTION = 0.9
SPEED = 1.5

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = 0

    def update(self):
        self.velocity_y *= FRICTION
        self.velocity_x *= FRICTION
        self.x += self.velocity_x
        self.y += self.velocity_y

    def right(self):
        self.velocity_x = SPEED

    def left(self):
        self.velocity_x = -SPEED

    def down(self):
        self.velocity_y = SPEED

    def up(self):
        self.velocity_y = -SPEED