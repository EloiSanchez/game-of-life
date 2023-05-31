import pygame
from pygame.surface import Surface


class Cell(pygame.rect.Rect):
    def __init__(self, left: int, top: int, width: int) -> None:
        super().__init__(left, top, width, width)
        self.width = width
        self.color = 'white'

    def draw(self, screen: Surface) -> None:
        left = self.x + round(0.05 * self.width)
        top = self.y + round(0.05 * self.width)
        width = round(0.9 * self.width)

        pygame.draw.rect(screen, self.color, (left, top, width, width))

    def change(self) -> None:
        self.color = 'white' if self.color == 'black' else 'black'

    def set_state(self, state: int) -> None:
        self.color = 'white' if state == 0 else 'black'