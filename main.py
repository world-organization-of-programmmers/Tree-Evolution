import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from pixel import PixelNum

pygame.init()
pygame.font.init()
setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
field = Field(screen, setting)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    field.fill(setting.bg_color)
    field.draw((0, 0, 0), (2, 9), 'h')
    field.draw((0, 0, 0), (3, 8), 'e')
    field.draw((0, 0, 0), (4, 7), 'l')
    field.draw((0, 0, 0), (5, 6), 'l')
    field.draw((0, 0, 0), (6, 5), 'o')

    field.blit()
    pygame.display.flip()
