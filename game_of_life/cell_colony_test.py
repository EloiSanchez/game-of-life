# Example file showing a circle moving on screen
import pygame
import numpy as np

class Colony():
    def __init__(self, m, n, cell_size) -> None:
        self.m, self.n = m, n
        self.states = np.zeros((m, n))
        self.cell_size = cell_size
        self.cells = np.empty((m, n), dtype=object)
        self.area = pygame.rect.Rect(0, 0, m * cell_size, n * cell_size)

        for i in range(m):
            for j in range(n):
                self.cells[i, j] = Cell(cell_size, j * cell_size, i * cell_size)

    def draw(self, screen):
        for cell in self.cells.flatten():
            cell.draw(screen)

    def change_cell(self, x, y):
        if 0 <= x < self.area.right and 0 <= y < self.area.bottom:
            i = y // self.cell_size
            j = x // self.cell_size
            print(f'changing cell ({i}, {j}) at position ({x}, {y})')
            self.cells[i, j].change()
        else:
            print('out of bounds')


class Cell(pygame.rect.Rect):
    def __init__(self, width, x, y, indices = None) -> None:
        self.rect = pygame.rect.Rect(x, y, width, width)
        self.width = width
        self.indices = indices
        self.color = 'white'

    def draw(self, surf):
        left = self.rect.x + round(0.05 * self.width)
        top = self.rect.y + round(0.05 * self.width)
        width = round(0.9 * self.width)

        pygame.draw.rect(surf, self.color, (left, top, width, width))

    def change(self):
        self.color = 'white' if self.color == 'black' else 'black'


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 900))
clock = pygame.time.Clock()
running = True
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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt += clock.tick(60) / 1000


pygame.quit()