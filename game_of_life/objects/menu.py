import pygame
from pygame.surface import Surface

from objects.button import Button


class Menu(pygame.rect.Rect):

    def __init__(self, left: int, top: int, width: int, height: int) -> None:
        super().__init__(left, top, width, height)
        self.info = pygame.font.Font(size = 48)
        self.state = 'stopped'
        self.config = {
            'simulating': ('Running', 'dark green'),
            'stopped': ('Not running', 'red'),
        }

        self.button_area = pygame.rect.Rect(
            self.width // 3,
            self.top,
            self.right - self.width // 3,
            self.height
        )

        self.clear_button = Button(
            self.button_area.left,
            self.button_area.top,
            self.button_area.width // 3,
            self.button_area.height,
            text = 'Clear',
            color = '#E0E0E0',
            pressed_color='#CCFFCC'
        )

        self.random_button = Button(
            self.button_area.left + self.button_area.width // 3,
            self.button_area.top,
            self.button_area.width // 3,
            self.button_area.height,
            text = 'Random',
            color = '#E0E0E0',
            pressed_color='#CCFFCC'
        )

        self.play_button = Button(
            self.button_area.left + 2 * self.button_area.width // 3,
            self.button_area.top,
            self.button_area.width // 3,
            self.button_area.height,
            text = 'Play',
            color = '#E0E0E0',
            pressed_color='#CCFFCC'
        )

        self.buttons = (self.clear_button, self.random_button, self.play_button)

    def draw(self, screen: Surface) -> None:
        info, color = self.config[self.state]

        text = self.info.render(info, True, color)

        width = self.width // 6 - text.get_width() // 2
        height = self.centery - text.get_height() // 2

        screen.blit(text, (width, height))

        for button in self.buttons:
            button.draw(screen)

    def change(self) -> None:
        self.state = 'simulating' if self.state != 'simulating' else 'stopped'
