import pygame
import numpy as np

from .cell import Cell


class Colony():
    def __init__(self, m, n, cell_size) -> None:
        self.rows, self.cols = m, n
        self.states = np.zeros((m, n), dtype=int)
        self.cell_size = cell_size
        self.cells = np.empty((m, n), dtype=object)
        self.area = pygame.rect.Rect(0, 0, m * cell_size, n * cell_size)
        self.indices = np.arange(m*n).reshape(m,n)


        for i in range(m):
            for j in range(n):
                self.cells[i, j] = Cell(cell_size, j * cell_size, i * cell_size)

    def draw(self, screen):
        for cell, state in zip(self.cells.flatten(), self.states.flatten()):
            cell.set_state(state)
            cell.draw(screen)

    def change_cell(self, x, y):
        if 0 <= x < self.area.right and 0 <= y < self.area.bottom:
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




def cellNeigh(element, GoLArr, m):
    # This changes from 1, 2, 3, 4, ... indexing to (i,j) indexing
    row, column = element // m, element % m
    return np.sum(GoLArr[row:row+3, column:column+3]) - GoLArr[row+1,column+1]


def GoLStep(GoLArr):
     # We start by creating the extended matrix with outer zero rows and columns
    n, m = np.shape(GoLArr)
    GoLArr = np.vstack((np.zeros(m, dtype=int), GoLArr, np.zeros(m, dtype=int)))
    GoLArr = np.hstack(((np.zeros((n+2,1), dtype=int)), GoLArr, (np.zeros((n+2,1), dtype=int))))

    indices = np.arange(n*m).reshape(n,m)

    # We call the cellNeigh function FOR EACH element in the indices array. We use
    # this elements to obtain the submatrices of the GoLArr. Finally, we obtain
    # the number of neighbors for each cell and store it in a (n,m) matrix
    neigh = np.vectorize(cellNeigh, excluded=(1,2))(indices, GoLArr, m)

    return np.where((neigh == 3) | (GoLArr[1:n+1, 1:m+1] == 1) & (neigh == 2), 1, 0)