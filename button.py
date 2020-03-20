import pygame

from pygame import font


class Button:
    def __init__(self, screen, color, rect, text, text_color):
        self.screen = screen
        self.color = color
        self.rect = pygame.Rect(rect)
        self.text = text
        self.text_color = text_color
        self.font_size = len(self.text) * 12

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.SysFont(None, self.font_size)
        text = font.render(self.text, 1, self.text_color)
        self.screen.blit(text, self.rect)

    def pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1 and self.rect.left < mouse_pos[
                0] < self.rect.right and self.rect.top < mouse_pos[1] < self.rect.bottom:
                return True
        return False
