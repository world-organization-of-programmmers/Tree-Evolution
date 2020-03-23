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

screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
field = Field(screen, setting)
dashboard = Dashboard(screen, setting)

itteration = 0
delay = 0

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
    for event in pygame.event.get():
        gf.check_event(event, dashboard)
        delay = gf.change_speed(event, dashboard, delay)
    trees = gf.tree_event(trees)
    gf.draw_objects(field, dashboard, trees, itteration)

    pygame.display.flip()
    itteration += 1
    pygame.time.wait(delay)
    print(delay)
