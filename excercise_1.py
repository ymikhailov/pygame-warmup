import pygame


# init pygame engine
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 600])

# run main game loop
running = True
while running:
    # process event from pygame events queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background with color in RGB format
    screen.fill((40, 44, 52))

    # TODO: draw simple home using drawing primitives like pygame.draw.line, pygame.draw.rect etc

    # flip the display
    pygame.display.flip()

# quit pygame engine
pygame.quit()
