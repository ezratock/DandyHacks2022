import pygame
from Object import *
from Player import *
from Setup import *
import os

print(pygame.font.get_fonts())

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
                height_difference = SCREEN_HEIGHT / 7
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
                pygame.display.update()

                while options_running:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        start_game(True)
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

screen.fill(white)
start_game(False)
main_menu()

objects = []
objects.append(Wall(100,100))

lvl_bg = pygame.image.load(os.path.join('src', 'Test-01.png'))

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
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        choice_made = False
        while not choice_made:
            exit_font = pygame.font.SysFont('freesansbold', 32)
            text = exit_font.render("Are you sure you want to quit? \n 1 - Yes \n 2 - No.", True, red, black)
            screen.blit(text, (0, SCREEN_HEIGHT//2))
            pygame.display.update()
            if pygame.key.get_pressed()[pygame.K_1]:
                start_game(True)
                main_menu()
                choice_made = True
            if pygame.key.get_pressed()[pygame.K_1]:
                screen.remove(text)
                choice_made = True

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
    font = pygame.font.SysFont('freesansbold', 40)
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



