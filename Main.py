import pygame

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



pygame.init()

X = 500
Y = 500

screen = pygame.display.set_mode([X, Y])

# Fill the background with white
screen.fill(white)

# Run until the user asks to quit
running = True
while running:
    
    text_shown = ''
    
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        text_shown = right()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        text_shown = left()

    if pygame.key.get_pressed()[pygame.K_UP]:
        text_shown = up()

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        text_shown = down()

    if pygame.key.get_pressed()[pygame.K_j]:
        text_shown = action()

    if pygame.key.get_pressed()[pygame.K_k]:
        text_shown = cancel()
    
    pygame.display.set_caption('M&T Bank: The Game')
 
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(text_shown, True, green, blue)
 
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
 
    # set the center of the rectangular object.
    textRect.center = (X // 2, Y // 2)

    screen.fill(white)

    screen.blit(text, textRect)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Flip the display (updates the display with changes made to the screen)
    pygame.display.flip()

    pygame.display.update()

# Done! Time to quit.
pygame.quit()
