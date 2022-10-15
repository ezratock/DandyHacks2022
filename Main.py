import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Flip the display (updates the display with changes made to the screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()