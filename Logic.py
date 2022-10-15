from abc import ABC

import pygame
from Object import *
import os
import abc

# logic tickrate, # ticks per second
LOGIC_TICKRATE = 1


class Node(Object, ABC):

    def __init__(self, x, y, node_out):
        super().__init__(x, y)
        self.node_out = node_out
        self.state = False
        self.state_next = False

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def set_state_next(self, new_state_next):
        self.state_next = new_state_next

    def logic_tick(self):
        # write next state of output node
        self.node_out.set_state_next(self.state)

        # read next state of self node
        self.state = self.state_next


class Wire(Node):
    def __init__(self, x, y, node_out, shape):
        super().__init__(x, y, node_out)
        self.shape = shape
        # shape = a string (e.g. 'lr' or 'ur' that describes the wire's connections


class Pad(Node):
    def __init__(self, x, y, node_out):
        super().__init__(x, y, node_out)
        self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))

    def switch(self, state):
        if state:  # player standing on button -> button down
            self.set_state(state)
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-down.png'))
        else:
            self.set_state(state)
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))
