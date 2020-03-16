import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from tree import Tree

pygame.font.init()
setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана

field = Field(screen, setting)
tree = Tree(20, 19)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    field.fill()
    field.draw_pixels(tree.get_pixels())

    pygame.display.flip()
    
    tree.grow([tree])
    pygame.time.wait(1000)
