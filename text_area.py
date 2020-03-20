import pygame


class TextArea:
    def __init__(self, screen, color, rect, text, text_color):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(rect)
        self.text = text
        self.text_color = text_color
        self._font_size = len(self.text) * 12

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect, )
        font = pygame.font.SysFont(None, self._font_size)
        text = font.render(self.text, 1, self.text_color)
        self.screen.blit(text, self.rect)
