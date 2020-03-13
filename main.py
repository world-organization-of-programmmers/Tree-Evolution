import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from pixel import Pixel

setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана

# создание поля (объект np.array3D   размером : ширина экрана/размер пикселя , высота экрана/размер пикселя , RGB)
field = Field(pygame.surfarray.pixels3d(screen), setting)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pixels = [Pixel((0, 0, 0), (0, 0))]  # список пикселей , которые отображаються на экране
    field.fill(setting.bg_color)  # заливка поля одним цветом
    field.draw_pixel(pixels)  # отрисовка на экране всех пикселей
    field.blit()  # отображение на экране всех пикселей

    pygame.display.flip()
