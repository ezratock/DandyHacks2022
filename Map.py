from Setup import *
from Object import *
from LoadPlayer import *
from Logic import *
import os

map_data = os.path.join("src", "map.csv")
# https://docs.google.com/spreadsheets/d/1NnE3MMM4u7MKn5g_7s0xIo47Jr5qB_RUd2QM87LDB6k/edit?usp=sharing
# ...download to .csv to src/map.csv
# Format:
# B = back wall
# W = regular wall
# ...
# other (non-empty!) char = blank square

def load_map_data():
    with open(map_data) as csvfile:
        line_index = 0
        for line in csvfile:
            map.append([])
            line = line.split(",")
            line_arr = []
            for tile in range(len(line)):
                if line[tile] == "B":
                    line_arr.append(Wall(tile*64, line_index*64, True))
                elif line[tile] == "W":
                    line_arr.append(Wall(tile*64, line_index*64, False))
                elif line[tile][0] == "B":
                    line_arr.append([Wall(tile*64, line_index*64, True),
                                     Wire(tile*64, line_index*(64), line[tile][1:])
                                     ])
                elif line[tile][0] == "W":
                    line_arr.append([Wall(tile*64, line_index*64, False),
                                     Wire(tile*64, line_index*(64), line[tile][1:])
                                     ])
                elif line[tile][0] == "I":
                    line_arr.append(Wire(tile*64, line_index*(64), line[tile][1:]))
                elif line[tile] == "U":
                    line_arr.append(Button(tile*64, line_index*(64)))
                elif line[tile] == "D":
                    line_arr.append(Door(tile*64, line_index*64, False))
                elif line[tile] == "T":
                    line_arr.append(Door(tile*64, line_index*64, False))
                elif line[tile] == "*":
                    line_arr.append(Win(tile*64, line_index*64))
                else:
                    line_arr.append("")
            map[line_index] = line_arr
            line_index += 1

def draw_map(surface):
    # Only drawing objects on the screen
    for row in range(math.floor(player.y/64) - 6, math.ceil(player.y/64) + 7):
        for col in range(math.floor(player.x/64) - 8, math.ceil(player.x/64) + 9):
            if row < len(map) and col < len(map[0]):
                if isinstance(map[row][col], list):
                    map[row][col][0].draw(surface)
                    map[row][col][1].draw(surface)
                    continue
                if isinstance(map[row][col], Object):
                    map[row][col].draw(surface)

def tile_in_front(dir):
    if dir == Direction.RIGHT:
        return map[int(player.y/64)][int(player.x/64)+1]
    if dir == Direction.LEFT:
        return map[int(player.y/64)][int(player.x/64 + 0.99999) - 1]
    if dir == Direction.UP:
        return map[int(player.y/64 + 0.99999) - 1][int(player.x/64)]
    if dir == Direction.DOWN:
        return map[int(player.y/64)+1][int(player.x/64)]

def collision(dir):
    tile = tile_in_front(dir)

    if isinstance(tile, Object):
        return tile.wall
    return False

def until_bar(string):
    rtrn = ""
    while string[len(rtrn)] != "|":
        rtrn += string[len(rtrn)]
    return rtrn