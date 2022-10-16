import time
from abc import ABC

import pygame
from Object import *
import os
from LoadPlayer import *
import abc

# logic tickrate, # ticks per second
LOGIC_TICKRATE = 1


# class Node(Object, ABC):
#
#     def __init__(self, x, y, node_out):
#         super().__init__(x, y)
#         self.node_out = node_out
#         self.state = False
#         self.state_next = False
#
#     def get_state(self):
#         return self.state
#
#     def set_state(self, new_state):
#         self.state = new_state
#
#     def set_state_next(self, new_state_next):
#         self.state_next = new_state_next
#
#     def logic_tick(self):
#         pass
#
#     def draw(self):
#         pass


class Node(Object, ABC):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.state = False
        self.state_next = False

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def set_state_next(self, new_state_next):
        self.state_next = new_state_next

    def logic_tick(self):
        pass

dirs = {"d":[0,1], "u":[0,-1], "r":[1,0], "l":[-1,0]}

class Wire(Node):
    def __init__(self, x, y, shape):
        super().__init__(x, y)
        self.shape = shape
        self.lock = False
        # shape = a string (e.g. 'lr' or 'ur' that describes the wire's connections

        self.filenames = [f'wire-{c}-off.png' for c in self.shape]
        self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]

    def logic_tick(self):
        #if the states of the adjacent connections differ from each other, toggle state
        counter = 0
        for c in self.shape:
            dir = dirs[c]
            adj_tile = map[int(self.y/64) + dir[1]][int(self.x/64) + dir[0]]
            if isinstance(adj_tile, list):
                adj_state = adj_tile[1].state
            elif isinstance(adj_tile, Node):
                adj_state = adj_tile.state
            else:
                print("hanging wire!")
                adj_state = False
            if adj_state:
                counter += 1
        if counter != len(self.shape) and counter != 0:
            self.toggle()


    def draw(self, surface):
        self.state = self.state_next
        if self.state:
            self.filenames = [f'wire-{c}-on.png' for c in self.shape]
            self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]
        else:
            self.filenames = [f'wire-{c}-off.png' for c in self.shape]
            self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]

        # Offset because player position is (512, 384) on the screen relative to top left corner
        pos_x = self.x - player.x + 512
        pos_y = self.y - player.y + 384
        if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
            self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
            for texture in self.tex:
                surface.blit(texture, self.object)

    def toggle(self):
        if not self.lock:
            self.state_next = not self.state_next
            self.lock = True
        else:
            self.lock = False



class Button(Node):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.wall = True
        self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))

    def update(self):
        if self.state:  # state == True -> button down
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-down.png'))
        else:
            self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))

    def toggle(self):
        self.state = not self.state
        self.update()

class Door(Node):
    def __init__(self, x, y, is_back):
        super().__init__(x, y)
        if is_back:
            self.texture = pygame.image.load(os.path.join('src', 'textures', 'Door-base.png'))
        else:
            self.texture = pygame.image.load(os.path.join('src', 'textures', 'Door.png'))
        self.state = False

    def draw(self, surface):
        for dir in [[0,1], [0,-1], [1,0], [-1,0]]:
            adj_tile = map[int(self.y/64) + dir[1]][int(self.x/64) + dir[0]]
            if isinstance(adj_tile, list):
                self.state = adj_tile[1].state
            elif isinstance(adj_tile, Node):
                self.state = adj_tile.state

        # Offset because player position is (512, 384) on the screen relative to top left corner
        pos_x = self.x - player.x + 512
        pos_y = self.y - player.y + 384
        if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
            if not self.state:
                self.wall = True
                self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
                surface.blit(self.texture, self.object)
            else:
                self.wall = False


# class Wire(Node):
#     def __init__(self, x, y, node_out, shape):
#         super().__init__(x, y, node_out)
#         self.shape = shape
#         # shape = a string (e.g. 'lr' or 'ur' that describes the wire's connections
#
#         self.filenames = [f'wire-{c}-off.png' for c in self.shape]
#         self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]
#
#     def logic_tick(self):
#         if self.state:
#             self.filenames = [f'wire-{c}-on.png' for c in self.shape]
#             self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]
#         else:
#             self.filenames = [f'wire-{c}-off.png' for c in self.shape]
#             self.tex = [pygame.image.load(os.path.join('src', 'wires', name)) for name in self.filenames]
#
#
#
#         # write next state of output node
#         self.node_out.set_state_next(True)
#
#         # read next state of self node
#         self.state = self.state_next
#
#     def draw(self, surface):
#         # Offset because player position is (512, 384) on the screen relative to top left corner
#         pos_x = self.x - player.x + 512
#         pos_y = self.y - player.y + 384
#         if -self.width <= pos_x <= SCREEN_WIDTH and -self.height <= pos_y <= SCREEN_HEIGHT:
#             self.object = pygame.Rect(pos_x, pos_y, self.width, self.height)
#             for texture in self.tex:
#                 surface.blit(texture, self.object)


# class Pad(Node):
#     def __init__(self, x, y, node_out):
#         super().__init__(x, y, node_out)
#         self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))
#
#     def update(self, state):
#         if state:  # state == True -> button down
#             self.set_state(state)
#             self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-down.png'))
#         else:
#             self.set_state(state)
#             self.texture = pygame.image.load(os.path.join('src', 'objects', 'button-up.png'))
#
#     def logic_tick(self):
#         self.node_out.set_state(True)
#         self.node_out.set_state_next(True)
#
#     def draw(self, surface):
#         if player.x - self.x + SCREEN_WIDTH // 2 == 0 and player.y - self.y + SCREEN_HEIGHT // 2 == 0:
#             self.update(True)
#         else:
#             self.update(False)
#         super().draw(surface)
#
#
# class Osc(Pad):
#     def __init__(self, x, y, node_out):
#         super().__init__(x, y, node_out)
#         self.logic_tick()
#
#     def logic_tick(self):
#         super().logic_tick()
#         self.update(not self.get_state())
