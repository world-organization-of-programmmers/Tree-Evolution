import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from tree import Tree
from dashboard import Dashboard

import game_function as gf

pygame.font.init()
setting = Setting

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
field = Field(screen, setting)

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
dashboard = Dashboard(screen, setting)
itteration = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        for button in dashboard.buttons:
            button.is_pressed(event)

    field.fill()
    dashboard.draw()
    dashboard.text_areas[0].text = "itteration: " + str(itteration)
    dashboard.blit((0, 0))

    for tree in trees:
        field.draw_pixels(tree.get_pixels())

    pygame.display.flip()

    new_trees = []
    for tree in trees:
        new_tree = tree.grow(trees + new_trees)
        new_trees += new_tree
    trees = new_trees
    if not trees:
        trees = [Tree(15, 119, 0), Tree(30, 119, 0), Tree(45, 119, 0), Tree(90, 119, 0)]
    itteration += 1

    # pygame.time.wait(50)
