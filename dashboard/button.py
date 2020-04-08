import pygame

from dashboard.text_area import TextArea


class Button(TextArea):
    def __init__(self, screen, color, rect, text, text_color, font_size):

        super().__init__(screen, color, rect, text, text_color, font_size)
        self._unpressed_font_color = text_color
        self._pressed_font_color = tuple(map(lambda a: a // 2, text_color))
        self._pressed = False
        self._unpressed_color = color
        self._pressed_color = tuple(map(lambda a: a // 2, color))
        self._pressed_time = 0

    def button_down(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1 and self.rect.left < mouse_pos[
                0] < self.rect.right and self.rect.top < mouse_pos[1] < self.rect.bottom:
                self._pressed_time = pygame.time.get_ticks()
                self.color = self._pressed_color
                self.text_color = self._pressed_font_color
                self._pressed = True

    def button_up(self):
        self._pressed = False
        if pygame.time.get_ticks() - self._pressed_time > 30:
            self.color = self._unpressed_color
            self.text_color = self._unpressed_font_color

    def is_pressed(self):
        return self._pressed


class Switch(TextArea):
    def __init__(self, screen, color, rect, text, text_color, font_size):

        super().__init__(screen, color, rect, text, text_color, font_size)
        self._unpressed_font_color = text_color
        self._pressed_font_color = tuple(map(lambda a: a // 2, text_color))
        self.pressed = False
        self._unpressed_color = color
        self._pressed_color = tuple(map(lambda a: a // 2, color))

    def press(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1 and self.rect.left < mouse_pos[
                0] < self.rect.right and self.rect.top < mouse_pos[1] < self.rect.bottom:
                if not self.pressed:
                    self.color = self._pressed_color
                    self.text_color = self._pressed_font_color
                    self.pressed = True
                elif self.pressed:
                    self.color = self._unpressed_color
                    self.text_color = self._unpressed_font_color
                    self.pressed = False

    def is_pressed(self):
        return self.pressed
