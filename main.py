import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from pixel import PixelNum
pygame.font.init()
setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана

# создание поля (объект np.array3D   размером : ширина экрана/размер пикселя , высота экрана/размер пикселя , RGB)
field = Field(screen, setting)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    field.draw_pixels([PixelNum((255, 0, 255), (0, 5), 5)])
    pygame.display.flip()
