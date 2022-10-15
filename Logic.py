import pygame
import os

#logic tickrate, # ticks per second
LOGIC_TICKRATE = 1

class Logic:

    def __init__(self, node_in):
        self.node_in = node_in
        self.active = False
        self.next_state = False

    def active(self):
        return self.active

    def logic_tick(self):
        self.active = self.next_state
