import numpy as np
import pygame


class Field:
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting
        self.bg_color = setting.bg_color
        self.size = setting.pixel_size
        self.width = setting.width // setting.pixel_size
        self.height = setting.height // setting.pixel_size

    def draw_pixels(self, pixels):  # добавление всех пикселей на поле
        for pixel in pixels:
            rect = pygame.draw.rect(self.screen, pixel.color,
                                    (
                                        pixel.position[0] * self.size, pixel.position[1] * self.size, self.size,
                                        self.size), 0)
            rect = pygame.draw.rect(self.screen, pixel.border_color,
                                    (
                                        pixel.position[0] * self.size, pixel.position[1] * self.size, self.size,
                                        self.size), 1)
            if pixel.number:
                font = pygame.font.Font(None, self.size)
                number = font.render(str(pixel.number), 1, pixel.font_color)
                rect.centery += self.size // 4
                rect.centerx += self.size // 5
                self.screen.blit(number, rect)

    def fill(self):  # заливка одним цветом
        color_code = 150
        dif = color_code // self.height

        for i in range(self.height):
            pygame.draw.rect(self.screen, (color_code, color_code, 0),
                             (0, i * self.size, self.setting.width, self.size))
            color_code -= dif

    def get_size(self):
        return self.width, self.height
