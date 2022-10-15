from cgi import print_arguments
import pygame
from Object import *
from Player import *
from Setup import *
from Logic import *
import os
import sys
import subprocess
 
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
 
 
 
pygame.init()
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Fill the background with black
screen.fill(black)
 
game_name = 'M&T Bank: The Game'
pygame.display.set_caption(game_name)
 
font = pygame.font.SysFont('skia', 40)
title = font.render(game_name, True, white)
start_text = font.render('START', True, black, green)
options_text = font.render('OPTIONS', True, white)
title_location = ((SCREEN_WIDTH - title.get_width()) / 2, (SCREEN_HEIGHT - title.get_height()) / 4)
start_location = ((SCREEN_WIDTH - start_text.get_width()) / 2, (SCREEN_HEIGHT - start_text.get_height()) / 2)
options_location = ((SCREEN_WIDTH - options_text.get_width()) / 2, (3 * (SCREEN_HEIGHT - options_text.get_height())) / 4)
 
clock = pygame.time.Clock()

def start_game(on_Start):
   screen.fill(black)
   if not on_Start:
       start_text = font.render('START', True, black, green)
       options_text = font.render('OPTIONS', True, white)
   elif on_Start:
       start_text = font.render('START', True, white)
       options_text = font.render('OPTIONS', True, black, green)
 
   screen.blit(title, title_location)
   screen.blit(start_text, start_location)
   screen.blit(options_text, options_location)
   pygame.display.update()
 
 
objects = []
objects.append(Wall(64, 128))
objects.append(Wall(128, 64))
objects.append(Pad(320, 320, None))
 
lvl_bg = pygame.image.load(os.path.join('src', 'Test-01.png'))
 
def draw_level():
   screen.blit(lvl_bg,(0,0))
 
# Run until the user asks to quit
def run_game():   
    running = True
    j_pressed = False
    k_pressed = False
    right_pressed = False
    left_pressed = False
    up_pressed = False
    down_pressed = False

    while running:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            start_game(True)
            main_menu()
    
        text_shown = ''
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if (player.on_grid() and not right_pressed) or player.direction == Direction.RIGHT:
                player.direction = Direction.RIGHT
                player.right()
                right_pressed = True
        else:
            right_pressed = False
            if not player.on_grid() and player.direction == Direction.RIGHT:
                player.right()

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if (player.on_grid() and not left_pressed) or player.direction == Direction.LEFT:
                player.direction = Direction.LEFT
                player.left()
                left_pressed = True
        else:
            left_pressed = False
            if not player.on_grid() and player.direction == Direction.LEFT:
                player.left()

        if pygame.key.get_pressed()[pygame.K_UP]:
            if (player.on_grid() and not up_pressed) or player.direction == Direction.UP:
                player.direction = Direction.UP
                player.up()
                up_pressed = True
        else:
            up_pressed = False
            if not player.on_grid() and player.direction == Direction.UP:
                player.up()

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if (player.on_grid() and not down_pressed) or player.direction == Direction.DOWN:
                player.direction = Direction.DOWN
                player.down()
                down_pressed = True
        else:
            down_pressed = False
            if not player.on_grid() and player.direction == Direction.DOWN:
                player.down()

        if pygame.key.get_pressed()[pygame.K_j]:
            #add method here
            if not j_pressed:
                # add action here
                j_pressed = True
        else:
            j_pressed = False
            
        if pygame.key.get_pressed()[pygame.K_k]:
            #add method here
            if not k_pressed:
                # add action here
                j_pressed = True
        else:
            k_pressed = False

        draw_level()
        player.draw(screen)
 
        for object in objects:
            object.draw(screen)
 
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
  
        #updates screen with changes based on user input
        pygame.display.update()
        clock.tick(30)

#main menu
def main_menu():
   game_started = False
   on_Start = True
   up_pressed = False
   down_pressed = False
   while not game_started:
       onStart = True
       if pygame.key.get_pressed()[pygame.K_RETURN]:
           if on_Start:
               game_started = True
           else:
               options_running = True
               screen.fill(black)
               escape_font = pygame.font.SysFont('freesansbold', 20)
               text = escape_font.render("Press Esc to go back to main menu.", True, green)
               height_difference = SCREEN_HEIGHT / 8
               screen.blit(text, (SCREEN_WIDTH/20,height_difference * 1/4 ))
               options_font = pygame.font.SysFont('freesansbold', 32)
               text = options_font.render("Arrow Key Up: moves character up.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 1))
               text = options_font.render("Arrow Key Down: moves character down.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 2))
               text = options_font.render("Arrow Key Right: moves character right.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 3))
               text = options_font.render("Arrow Key Left: moves character left.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 4))
               text = options_font.render("T Key: action key", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 5))
               text = options_font.render("K Key: cancel key.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 6))
               text = options_font.render("Esc Key: quit the game.", True, white)
               screen.blit(text, (SCREEN_WIDTH/20, height_difference * 7))
               pygame.display.update()
 
               while options_running:
                   if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                       start_game(False)
                       options_running = False
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()
       pygame.display.update()
       if pygame.key.get_pressed()[pygame.K_UP]:
           if not up_pressed:
               start_game(on_Start)
               on_Start = not on_Start
               up_pressed = True
       else:
           up_pressed = False
 
       if pygame.key.get_pressed()[pygame.K_DOWN]:
           if not down_pressed:
               start_game(on_Start)
               on_Start = not on_Start
               down_pressed = True
       else:
           down_pressed = False
 
       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
   run_game()

def main():
    screen.fill(white)
    start_game(False)
    main_menu()

main()

# Quits game
pygame.quit()   