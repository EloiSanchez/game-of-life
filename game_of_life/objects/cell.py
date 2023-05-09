import pygame


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
