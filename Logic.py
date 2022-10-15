from abc import ABC

import pygame
from Object import *
import os
import abc

# logic tickrate, # ticks per second
LOGIC_TICKRATE = 1


class Node(Object, ABC):

    def __init__(self, x, y, node_out):
        super.__init__(x, y)
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

