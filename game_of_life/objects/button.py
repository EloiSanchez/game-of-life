import pygame
from pygame.surface import Surface

from typing import Union

class Button(pygame.rect.Rect):

    def __init__(self,
                 left: int, top: int, width: int, heigth: int,
                 pad: int = 10, text: Union[None, str] = None,
                 color: str = 'white', pressed_color: str = 'light_gray'
                 ) -> None:
        super().__init__(left + pad, top + pad, width - 2*pad, heigth - 2*pad)
        self.text = text
        self.font = pygame.font.Font(size = 28) if text is not None else None
        self.pad = pad
        self.default_color = color
        self.pressed_color = pressed_color

    def draw(self, screen: Surface) -> None:
        if self.is_pressed():
            pygame.draw.rect(screen, self.pressed_color, self.inflate(-7, -7))
        else:
            pygame.draw.rect(screen, self.default_color, self)

        if self.text:
            text = self.font.render(self.text, True, 'black')

            width = self.centerx - text.get_width() // 2
            height = self.centery - text.get_height() // 2

            screen.blit(text, (width, height))

    def is_pressed(self) -> bool:
        left_button, *_ = pygame.mouse.get_pressed()
        return left_button is True and \
            self.collidepoint(*pygame.mouse.get_pos())