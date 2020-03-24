import pygame
import sys
import numpy as np
from service.setting import Setting
from field.field import Field
from tree.tree import Tree
from dashboard.dashboard import Dashboard

import service.game_function as gf

pygame.font.init()
setting = Setting
pygame.init()

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
field = Field(pygame.surfarray.pixels3d(screen), setting)

g = np.array(
    [[13, 30, 14, 12],
     [30, 30, 30, 30],
     [30, 9, 30, 2],
     [30, 30, 30, 30],
     [30, 30, 30, 30],
     [30, 30, 30, 30],
     [30, 30, 30, 30],
     [30, 11, 30, 30],
     [15, 30, 30, 30],
     [30, 30, 30, 0],
     [30, 30, 30, 30],
     [6, 30, 8, 2],
     [30, 7, 30, 30],
     [8, 30, 30, 30],
     [30, 30, 30, 30],
     [30, 30, 30, 9]])
trees = [Tree(15, 119, 0), Tree(30, 119, 0), Tree(45, 119, 0), Tree(90, 119, 0), Tree(75, 119, 0), Tree(150, 119, 0),
         Tree(105, 119, 0)]

while True:
    time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    new_trees = []
    for tree in trees:
        new_tree = tree.grow(trees + new_trees, field)
        new_trees += new_tree
    trees = new_trees

    field.fill()

    for tree in trees:
        field.draw_pixels(tree.get_pixels())

    field.blit()


    print(pygame.time.get_ticks() - time)

    pygame.display.flip()
