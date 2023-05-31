import pygame


class Menu(pygame.rect.Rect):

    def __init__(self, left, top, width, height) -> None:
        super().__init__(left, top, width, height)
        self.info = pygame.font.Font(size = 48)
        self.state = 'stopped'
        self.config = {
            'running': ('Running', 'dark green'),
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
            color = '#E0E0E0'
        )

        self.random_button = Button(
            self.button_area.left + self.button_area.width // 3,
            self.button_area.top,
            self.button_area.width // 3,
            self.button_area.height,
            text = 'Random',
            color = '#E0E0E0'
        )

        self.play_button = Button(
            self.button_area.left + 2 * self.button_area.width // 3,
            self.button_area.top,
            self.button_area.width // 3,
            self.button_area.height,
            text = 'Play',
            color = '#E0E0E0'
        )

        self.buttons = (self.clear_button, self.random_button, self.play_button)

    def draw(self, screen):
        info, color = self.config[self.state]

        text = self.info.render(info, True, color)

        width = self.width // 6 - text.get_width() // 2
        height = self.centery - text.get_height() // 2

        screen.blit(text, (width, height))

        for button in self.buttons:
            button.draw(screen)

    def change(self):
        self.state = 'running' if self.state != 'running' else 'stopped'


class Button(pygame.rect.Rect):

    def __init__(self, left, top, width, heigth,
                 pad=10, text=None, color='pink') -> None:
        super().__init__(left + pad, top + pad, width - 2*pad, heigth - 2*pad)
        self.text = text
        self.font = pygame.font.Font(size = 28) if text is not None else None
        self.pad = pad
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self)

        if self.text:
            text = self.font.render(self.text, True, 'black')

            width = self.centerx - text.get_width() // 2
            height = self.centery - text.get_height() // 2

            screen.blit(text, (width, height))