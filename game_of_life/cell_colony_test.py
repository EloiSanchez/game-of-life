import pygame

from objects.colony import Colony


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 900))
clock = pygame.time.Clock()
running = True
simulating = False
dt = 0

colony = Colony(40, 40, 20)

while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    colony.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            colony.change_cell(*pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            simulating = not simulating

    if dt >= 0.25:
        dt = 0
        if simulating:
            colony.step()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt += clock.tick(60) / 1000


pygame.quit()