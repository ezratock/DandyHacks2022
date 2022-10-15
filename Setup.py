from Player import *
import os
import platform

system_nav = "\\" if platform.system() == 'Darwin' else "/"

player = Player()
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768