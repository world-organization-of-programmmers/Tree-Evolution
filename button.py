import pygame

from pygame import font


class Button:
    def __init__(self, screen, color, rect, text, text_color):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(rect)
        self.text = text
        self.text_color = text_color
        self._unpressed_font_color = text_color
        self._pressed_font_color = tuple(map(lambda a: a // 2, text_color))
        self._font_size = len(self.text) * 12
        self._pressed = False
        self._unpressed_color = color
        self._pressed_color = tuple(map(lambda a: a // 2, color))

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect,)
        font = pygame.font.SysFont(None, self._font_size)
        text = font.render(self.text, 1, self.text_color)
        self.screen.blit(text, self.rect)

    def _press(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1 and self.rect.left < mouse_pos[
                0] < self.rect.right and self.rect.top < mouse_pos[1] < self.rect.bottom:
                self.color = self._pressed_color
                self.text_color = self._pressed_font_color
                self._pressed = True

        if event.type == pygame.MOUSEBUTTONUP:
            self.color = self._unpressed_color
            self.text_color = self._unpressed_font_color
            self._pressed = False

    def is_pressed(self, event):
        self._press(event)
        return self._pressed
