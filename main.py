import pygame
import sys
import numpy as np
from service.setting import Setting
from field.field import Field
from tree.tree import Tree
from dashboard.dashboard import Dashboard

pygame.font.init()
pygame.init()

setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
field = Field(screen, setting)
master_time = np.zeros(5000)
master_trees = np.zeros(5000)

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
trees = [Tree(45, 59, np.array([[25, 12, 11, 15],
                                [28, 16, 6, 23],
                                [8, 13, 10, 24],
                                [23, 16, 3, 22],
                                [9, 22, 1, 10],
                                [28, 3, 21, 12],
                                [14, 20, 16, 10],
                                [1, 7, 24, 9],
                                [11, 19, 21, 24],
                                [24, 15, 25, 26],
                                [21, 2, 16, 24],
                                [30, 20, 1, 14],
                                [29, 28, 1, 6],
                                [25, 19, 20, 2],
                                [16, 23, 5, 13],
                                [12, 13, 10, 1], ]
                               ))]

for i in range(5000):
    time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    new_trees = []
    for tree in trees:
        new_tree = tree.grow(trees + new_trees)
        new_trees += new_tree
    trees = new_trees

    field.fill()  # заливка поля и отрисовка объектов

    for tree in trees:
        field.draw_pixels(tree.get_pixels())

    pygame.display.flip()
    master_time[i] = pygame.time.get_ticks() - time
    trees_count = 0
    for tree in trees:
        trees_count += len(tree.get_pixels())
    master_trees[i] = trees_count

np.save('master_time', master_time)
np.save('master_trees', master_trees)
