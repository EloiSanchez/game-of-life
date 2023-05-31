import pygame

from objects.colony import Colony
from objects.menu import Menu, Button


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 900))
clock = pygame.time.Clock()
running = True
simulating = False
dt = 0

colony = Colony(40, 40, 20)

menu = Menu(0, 800, 800, 100)

while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    cursor = pygame.mouse.get_pos()
    left_button, *_ = pygame.mouse.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if colony.collidepoint(*cursor):
                colony.change_cell(*cursor)
            elif menu.play_button.collidepoint(*cursor):
                simulating = not simulating
                menu.change()
            elif menu.random_button.collidepoint(*cursor):
                colony.randomize()
            elif menu.clear_button.collidepoint(*cursor):
                colony.clear()

    menu.draw(screen)
    colony.draw(screen)

    if dt >= 0.25:
        dt = 0
        if simulating:
            colony.step()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt += clock.tick(60) / 1000


pygame.quit()