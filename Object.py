import pygame
WALL_SIZE = 50

class Object:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object = pygame.Rect(self.x, self.y, WALL_SIZE, WALL_SIZE)
        self.color = (128,128,128)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.object)



