import numpy as np
import pygame


class Field:
    def __init__(self, surface_arr, setting):
        self.setting = setting
        self.surface_arr = surface_arr  # объект pygame.surfarray.pixels3d(screen)
        self.size = setting.pixel_size
        self.width = setting.width // setting.pixel_size
        self.height = setting.height // setting.pixel_size
        self.field = np.zeros((self.width, self.height, 3))  # поле для рисования

    def draw_pixels(self, pixels):  # добавление всех пикселей на поле
        for pixel in pixels:
            self.field[pixel.position] = pixel.color

    def fill(self, color=None):  # заливка одним цветом
        for i in range(self.width):
            for j in range(self.height):
                if not color:
                    color = self.setting.bg_color
                self.field[i, j] = color

    def blit(self):  # отображение на экране
        for i in range(self.width):
            for j in range(self.height):
                self.surface_arr[i * self.size + 1:(i + 1) * self.size + 1, j * self.size + 1:(j + 1) * self.size + 1] = self.field[i, j]
