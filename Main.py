import pygame
from Object import *
from Player import *
from Setup import *
import os

def left():
    return 'left'

def right():
    return 'right'

def up():
    return 'up'

def down():
    return 'down'

def action():
    return 'action'

def cancel():
    return 'cancel'

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)



pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Fill the background with black
screen.fill(black)

game_name = 'M&T Bank: The Game'
pygame.display.set_caption(game_name)

font = pygame.font.Font('freesansbold.ttf', 32)
start_text = font.render('START', True, black, green)
options_text = font.render('OPTIONS', True, white)
start_location = (SCREEN_WIDTH - start_text.get_width()) / 2, (SCREEN_HEIGHT - start_text.get_height()) / 2
options_location = (SCREEN_WIDTH - start_text.get_width()) / 2, (3 * (SCREEN_HEIGHT - start_text.get_height())) / 2

def start_game():
    text = font.render(game_name, True, white)
    start_text = font.render('START', True, black, green)
    options_text = font.render('OPTIONS', True, white)
    screen.blit(text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 4))
    screen.blit(start_text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 2))

start_game()
#main menu
game_started = False
while not game_started:
    onStart = True
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        if onStart:
            game_started = True
        else:
            options_running = True
            screen.fill(black)
            text = font.render("Press Esc to go back to main menu.", True, white)
            screen.blit(text, (0,0))
            while options_running:
                if(pygame.key.get_pressed(pygame.K_ESCAPE)):
                    start_game()
                    options_running = False
    if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_DOWN]:
        onStart = not onStart
        if onStart:
            start_text = font.render('START', True, black, green)
            options_text = font.render('OPTIONS', True, white)
        else:
            start_text = font.render('START', True, black, green)
            options_text = font.render('OPTIONS', True, white)
        screen.blit(start_text, start_location)
        screen.blit(options_text, options_location)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

screen.fill(white)

objects = []
objects.append(Wall(100,100))

lvl_bg = pygame.transform.scale(pygame.image.load
                                (os.path.join('src', 'Test-01.png')),(SCREEN_WIDTH,SCREEN_HEIGHT))

def draw_level():
    screen.blit(lvl_bg,(0,0))

# Run until the user asks to quit
running = True
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
j_pressed = False
k_pressed = False
while running:
    text_shown = ''
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        text_shown = right()
        player.right()
        if not right_pressed:
            player.direction = Direction.RIGHT
            right_pressed = True
    else:
        right_pressed= False
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        text_shown = left()
        player.left()
        if not left_pressed:
            player.direction = Direction.LEFT
            left_pressed = True
    else:
        left_pressed = False
    if pygame.key.get_pressed()[pygame.K_UP]:
        text_shown = up()
        player.up()
        if not up_pressed:
            player.direction = Direction.UP
            up_pressed = True
    else:
        up_pressed = False
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        text_shown = down()
        player.down()
        if not down_pressed:
            player.direction = Direction.DOWN
            down_pressed = True
    else:
        down_pressed = False
    if pygame.key.get_pressed()[pygame.K_j]:
        text_shown = action()
    if pygame.key.get_pressed()[pygame.K_k]:
        text_shown = cancel()

    # 1st parameter is the font file
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(text_shown, True, green, blue)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    player.update()

    draw_level()

    for object in objects:
        object.draw(screen)

    screen.blit(text, textRect)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #updates screen with changes based on user input
    pygame.display.update()

# Quits game
pygame.quit()
