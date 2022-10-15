import time
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

        self.filenames = [f'wire-{c}-off.png' for c in self.shape]
        self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]

    def logic_tick(self):
        super().logic_tick()
        if self.state:
            self.filenames = [f'wire-{c}-on.png' for c in self.shape]
            self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]
        else:
            self.filenames = [f'wire-{c}-off.png' for c in self.shape]
            self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]

    def draw(self, surface):
        pos_x = self.x - player.x
        pos_y = self.y - player.y
        if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
            self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
            for texture in self.tex:
                surface.blit(texture, self.object)


class Pad(Node):
    def __init__(self, x, y, node_out):
        super().__init__(x, y, node_out)
        self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))

    def update(self, state):
        if state:  # state == true -> button down
            self.set_state(state)
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-down.png'))
        else:
            self.set_state(state)
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))


class Osc(Pad):
    def __init__(self, x, y):
        super().__init__(x, y, self)
        self.logic_tick()

    def __init__(self, x, y, node_out):
        super().__init__(x, y, node_out)
        self.logic_tick()

    def logic_tick(self):
        super().logic_tick()
        self.update(not self.get_state())


class Door(Node):

    def logic_tick(self):
        pass
