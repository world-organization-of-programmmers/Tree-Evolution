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
dashboard = Dashboard(screen, setting)

next_step = False

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
        if event.type == pygame.QUIT:
            sys.exit()

        for button in dashboard.buttons:  # отработка нажатий кнопок и выключателей
            button.button_down(event)
        for switcher in dashboard.switches:
            switcher.press(event)

        if event.type == pygame.KEYDOWN:  # следующий шаг в step mode при нажатии пробела или стрелки
            if event.key == pygame.K_SPACE or event.key == pygame.K_RIGHT:
                next_step = True

    if dashboard.buttons[0].is_pressed():  # изменение задержки
        if delay > 0:
            delay -= 10
    if dashboard.buttons[1].is_pressed():
        delay += 10

    if dashboard.buttons[3].is_pressed():  # новая симуляция
        trees = [Tree(15, 119, 0), Tree(30, 119, 0), Tree(45, 119, 0), Tree(90, 119, 0), Tree(75, 119, 0),
                 Tree(150, 119, 0),
                 Tree(105, 119, 0)]
        itteration = 0

    if dashboard.buttons[2].is_pressed():
        file = input("enter file_name : ")  # соханение генома

        with open(file + '.txt', 'w') as f:
            for tree in trees:
                f.write(str(tree.genom) + '\n\n\n')

    if not dashboard.switches[0].is_pressed() or (dashboard.switches[0].is_pressed() and next_step):  # рост деревьев
        new_trees = []
        for tree in trees:
            new_tree = tree.grow(trees + new_trees)
            new_trees += new_tree
        trees = new_trees

        itteration += 1
        next_step = False

    field.fill()  # заливка поля и отрисовка объектов
    dashboard.draw()
    dashboard.text_areas[0].text = "itteration: " + str(itteration)
    dashboard.blit((0, 0))
    for tree in trees:
        field.draw_pixels(tree.get_pixels())

    for button in dashboard.buttons:  # отработка разжатия кнопок
        button.button_up()
    pygame.display.flip()
    pygame.time.wait(delay)  # задержка
