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

    field.draw((0, 0, 0), (2, 9), 15)
    field.blit()
    pygame.display.flip()
