import pygame

from objects.colony import Colony
from objects.menu import Menu


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 900))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # hardcode colony and menu sizes
    colony = Colony(40, 40, 20)
    menu = Menu(0, 800, 800, 100)

    while running:

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")

        # event loop
        cursor = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # on left click
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if colony.collidepoint(*cursor):
                    colony.change_cell(*cursor)
                elif menu.play_button.collidepoint(*cursor):
                    menu.change()
                elif menu.random_button.collidepoint(*cursor):
                    colony.randomize()
                elif menu.clear_button.collidepoint(*cursor):
                    colony.clear()

        # draw the colony and menu
        menu.draw(screen)
        colony.draw(screen)

        # hardcoded ~4 iterations per second
        if dt >= 0.25:
            dt = 0
            if menu.state == 'simulating':
                colony.step()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        dt += clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()
