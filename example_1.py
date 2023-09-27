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

    # draw a red line with x1 = 300, y1 = 225 and x2 = 500, y2 = 225
    pygame.draw.line(screen, (255, 0, 0), [300, 225], [500, 225], 2)

    # draw a green rectangle with x = 300, y = 250, w = 200, h = 100
    pygame.draw.rect(screen, (0, 255, 0), [300, 250, 200, 100], 2)

    # draw a yellow circle with a radius of 50 with x = 400, y = 150
    pygame.draw.circle(screen, (255, 255, 0), (400, 150), 50, 2)

    # flip the display
    pygame.display.flip()

# quit pygame engine
pygame.quit()
