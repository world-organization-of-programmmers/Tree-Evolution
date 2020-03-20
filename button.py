import pygame

from text_area import TextArea


class Button(TextArea):
    def __init__(self, screen, color, rect, text, text_color, font_size):

        super().__init__(screen, color, rect, text, text_color, font_size)
        self._unpressed_font_color = text_color
        self._pressed_font_color = tuple(map(lambda a: a // 2, text_color))
        self._pressed = False
        self._unpressed_color = color
        self._pressed_color = tuple(map(lambda a: a // 2, color))

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
