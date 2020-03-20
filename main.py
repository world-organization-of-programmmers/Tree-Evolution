import pygame
import sys
import numpy as np
from setting import Setting
from field import Field
from tree import Tree
from button import Button

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
button = Button(screen, (150, 150, 150), (0, 0, 100, 40), "hello", (0, 255, 255))

while True:

    gf.check_event(button)

    field.fill()
    button.draw_button()

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

    # pygame.time.wait(50)
