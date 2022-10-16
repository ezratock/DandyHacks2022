from cgi import print_arguments
import pygame
from Object import *
from Player import *
from Setup import *
from Logic import *
import os 
from Map import *

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
dark_green = (0, 100, 0)
yellow = (255, 255, 0)
font_path = "PublicPixel-z84yD.ttf"
FPS = 60

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Fill the background with black
screen.fill(black)

game_name = 'M&T Bank: The Game'
pygame.display.set_caption(game_name)

font = pygame.font.Font(font_path, 40)
title = font.render(game_name, True, white)
start_text = font.render('START', True, green)
continue_text = font.render('CONTINUE', True, green)
options_text = font.render('OPTIONS', True, white)
title_location = ((SCREEN_WIDTH - title.get_width()) / 2, (SCREEN_HEIGHT - title.get_height()) / 4)
start_location = ((SCREEN_WIDTH - start_text.get_width()) / 2, (SCREEN_HEIGHT - start_text.get_height()) / 2)
continue_location = ((SCREEN_WIDTH - continue_text.get_width()) / 2, (SCREEN_HEIGHT - continue_text.get_height()) / 2)
options_location = (
(SCREEN_WIDTH - options_text.get_width()) / 2, (3 * (SCREEN_HEIGHT - options_text.get_height())) / 4)

clock = pygame.time.Clock()

def start_game(on_Start, game_status):
    screen.fill(black)
    if not on_Start:
        start_continue_text = font.render(game_status, True, green)
        options_text = font.render('OPTIONS', True, white)
    elif on_Start:
        start_continue_text = font.render(game_status, True, white)
        options_text = font.render('OPTIONS', True, green)

    screen.blit(title, title_location)
    if game_status == 'START':
        screen.blit(start_continue_text, start_location)
    if game_status == 'CONTINUE':
        screen.blit(start_continue_text, continue_location)
    screen.blit(options_text, options_location)
    pygame.display.update()


# objects = []
# objects.append(Wall(64, 128))
# objects.append(Wall(128, 64))
# objects.append(Wire(768, 320, None, 'lr'))
# objects.append(Wire(768-64*1, 320, objects[2], 'lr'))
# objects.append(Wire(768-64*2, 320, objects[3], 'lr'))
# objects.append(Pad(768-64*3, 320, objects[4]))

lvl_bg = pygame.image.load(os.path.join('src', 'Test-01.png'))


def draw_level():
    screen.blit(lvl_bg, (0, 0))


# Run until the user asks to quit
def run_game():
    frame_count = 0
    running = True
    j_pressed = False
    k_pressed = False
    right_pressed = False
    left_pressed = False
    up_pressed = False
    down_pressed = False
    game_finished = False
    game_won = False

    while running:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            start_game(False, 'CONTINUE')
            main_menu(True)

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
            # add method here
            if not j_pressed:
                # add action here
                j_pressed = True
        else:
            j_pressed = False

        if pygame.key.get_pressed()[pygame.K_k]:
            # add method here
            if not k_pressed:
                # add action here
                j_pressed = True
        else:
            k_pressed = False

        draw_level()

        frame_count += 1

        if frame_count >= 60:
            frame_count = 0
            for row in map:
                for obj in row:
                    try:
                        obj.logic_tick()
                        obj.draw(screen)
                    except AttributeError:
                        pass
        else:
            draw_map(screen)

        draw_map(screen)
        player.draw(screen)

        # for object in objects:
        #     object.draw(screen)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # updates screen with changes based on user input
        pygame.display.update()
        clock.tick(FPS)

        #print(clock.get_fps())
    if not game_finished:
        text_display(('YOU QUIT...', 'THE GAME'), red, red)
        time.sleep(2)
        pygame.quit()
        quit()
    elif game_won:
        text_display(('WINNER! WINNER!', 'CHICKEN DINNER!'), green, green)
        time.sleep(60)
        pygame.quit()
        quit()
    elif not game_won:
        text_display(('YOU LOST...', 'THE GAME'), red, red)
        time.sleep(60)
        pygame.quit()
        quit()

# main menu
def main_menu(game_started):
    game_running = False
    on_start = True
    up_pressed = False
    down_pressed = False
    while not game_running:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            if on_start:
                game_running = True
            else:
                options_running = True
                screen.fill(black)
                escape_font = pygame.font.Font(font_path, 12)
                text = escape_font.render("(Press Esc to go back to main menu)", True, green)
                height_difference = SCREEN_HEIGHT / 8
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 1 / 4))
                options_font = pygame.font.Font(font_path, 20)
                text = options_font.render("Arrow Key Up: moves character up.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 1))
                text = options_font.render("Arrow Key Down: moves character down.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 2))
                text = options_font.render("Arrow Key Right: moves character right.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 3))
                text = options_font.render("Arrow Key Left: moves character left.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 4))
                text = options_font.render("T Key: action key.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 5))
                text = options_font.render("K Key: cancel key.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 6))
                text = options_font.render("Esc Key: go back to the main menu.", True, white)
                screen.blit(text, (SCREEN_WIDTH / 20, height_difference * 7))
                pygame.display.update()

                while options_running:
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        if not game_started:
                            start_game(not on_start, 'START')
                        elif game_started:
                            start_game(not on_start, 'CONTINUE')
                        options_running = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            text_display(('YOU QUIT...', 'THE GAME'), red, red)
                            time.sleep(2)
                            pygame.quit()
                            quit()
        pygame.display.update()
        if pygame.key.get_pressed()[pygame.K_UP]:
            if not up_pressed:
                if not game_started:
                    start_game(on_start, 'START')
                elif game_started:
                    start_game(on_start, 'CONTINUE')
                on_start = not on_start
                up_pressed = True
        else:
            up_pressed = False

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            if not down_pressed:
                if not game_started:
                    start_game(on_start, 'START')
                elif game_started:
                    start_game(on_start, 'CONTINUE')
                on_start = not on_start
                down_pressed = True
        else:
            down_pressed = False

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                text_display(('YOU QUIT...', 'THE GAME'), red, red)
                time.sleep(2)
                pygame.quit()
                quit()
    run_game()

def text_display(phrase, text_color1, text_color2):
    screen.fill(black)
    font = pygame.font.Font(font_path, 40)
    h = 0
    for word in phrase:
        words = word.split(" ")
        word1 = words[0]
        word2 = words[1]
        end_title1 = font.render(word1, True, text_color1)
        end_title2 = font.render(word2, True, text_color2)
        combined_title = font.render(word, True, text_color1)
        x = 2 * (screen.get_width() - end_title1.get_width() - end_title2.get_width())/5
        screen.blit(end_title1, ((SCREEN_WIDTH - combined_title.get_width())/2, (SCREEN_HEIGHT - end_title1.get_height())/(3 - h)))
        pygame.display.update()
        time.sleep(0.50)
        screen.blit(end_title2, ((SCREEN_WIDTH - combined_title.get_width())/2 + combined_title.get_width() - end_title2.get_width(), (SCREEN_HEIGHT - end_title1.get_height())/(3 - h)))
        pygame.display.update()
        time.sleep(1)
        h += 1



def main():
    text_display(('M&T BANK...', 'THE GAME'), dark_green, yellow)
    load_map_data()
    time.sleep(2)
    start_game(False, 'START')
    main_menu(False)


main()

# Quits game
pygame.quit()
