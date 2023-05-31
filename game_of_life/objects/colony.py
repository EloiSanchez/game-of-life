import pygame
import numpy as np

from .cell import Cell


class Colony(pygame.rect.Rect):
    def __init__(self, m, n, cell_size) -> None:
        super().__init__(0, 0, m * cell_size, n * cell_size)
        self.rows, self.cols = m, n
        self.states = np.zeros((m, n), dtype=int)
        self.cell_size = cell_size
        self.cells = np.empty((m, n), dtype=object)
        self.indices = np.arange(m*n).reshape(m,n)

        for i in range(m):
            for j in range(n):
                self.cells[i, j] = Cell(cell_size, j * cell_size, i * cell_size)

    def draw(self, screen):
        for cell, state in zip(self.cells.flatten(), self.states.flatten()):
            cell.set_state(state)
            cell.draw(screen)

    def clear(self):
        self.states = np.zeros((self.rows, self.cols), dtype=int)

    def randomize(self):
        self.states = np.random.randint(0, 2, (self.rows, self.cols))

    def change_cell(self, x, y):
        if 0 <= x < self.right and 0 <= y < self.bottom:
            i = y // self.cell_size
            j = x // self.cell_size
            print(f'changing cell ({i}, {j}) at position ({x}, {y})')
            self.cells[i, j].change()
            self.states[i, j] = 1 if self.states[i, j] == 0 else 0
        else:
            print('out of bounds')

    def step(self):
        iter_states = np.vstack((
            np.zeros(self.cols, dtype=int),
            self.states,
            np.zeros(self.cols, dtype=int)
            ))
        iter_states = np.hstack((
            np.zeros((self.rows+2,1), dtype=int),
            iter_states,
            (np.zeros((self.rows+2,1), dtype=int))
            ))

        neighbours = self._neigh(self.indices, iter_states)

        self.states = np.where(
            (neighbours == 3) | (iter_states[1:self.rows+1, 1:self.cols+1] == 1) & (neighbours == 2),
            1, 0)

    def _neigh(self, indices, GoLArr):
        def neigh(element, GoLArr):
            row, column = element // self.cols, element % self.cols
            return np.sum(GoLArr[row:row+3, column:column+3]) - GoLArr[row+1,column+1]

        return np.vectorize(neigh, excluded=(1, ))(indices, GoLArr)
