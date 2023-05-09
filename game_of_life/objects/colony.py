import pygame
import numpy as np

from .cell import Cell


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
