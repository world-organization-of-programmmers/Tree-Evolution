import pygame
import sys, getopt
import numpy as np
from service.setting import Setting
from field.field import Field
from tree.tree import Tree
from dashboard.dashboard import Dashboard
import service.game_function as gf
import os

setting = Setting

arguments = {'non_gui': False,
             'step_mode': False,
             'trees_count': 10,
             'itter_save': None,
             'folder': 'TreesGenom',
             'genoms_folder': None}

arguments, setting = gf.create_arguments(arguments, sys.argv[1:], setting)

map = np.array(
    [[0 for _ in range(setting.width // setting.pixel_size)] for _ in range(setting.height // setting.pixel_size)])

trees, itteration = gf.create_trees(arguments, setting, map)
if not arguments['non_gui']:
    delay = 0
    pygame.font.init()
    pygame.init()

    screen = pygame.display.set_mode((setting.width, setting.height))  # создание экрана
    field = Field(screen, setting)
    dashboard = Dashboard(screen, setting)
    dashboard.switches[0].pressed = arguments['step_mode']
    next_step = False

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
            trees, itteration = gf.create_trees(arguments, setting, map)
            map = np.array(
                [[0 for _ in range(setting.width // setting.pixel_size)] for _ in
                 range(setting.height // setting.pixel_size)])

            if arguments['itter_save']:
                for folder in os.listdir(arguments['folder']):
                    for file in os.listdir(arguments['folder'] + '/' + folder):
                        os.remove(arguments['folder'] + '/' + folder + '/' + file)
                    os.rmdir(arguments['folder'] + '/' + folder)

        if dashboard.buttons[2].is_pressed():
            file = input("enter file_name : ")  # соханение генома

            with open(file + '.txt', 'w') as f:
                for tree in trees:
                    f.write(str(tree.genom) + '\n\n\n')

        gf.save_genom(arguments, trees, itteration)

        if not dashboard.switches[0].is_pressed() or (
                dashboard.switches[0].is_pressed() and next_step):  # рост деревьев
            new_trees = []
            for tree in trees:
                new_tree = tree.grow(map)
                new_trees += new_tree
            trees = new_trees

            itteration += 1
            next_step = False

        field.fill()  # заливка поля и отрисовка объектов
        dashboard.draw()
        dashboard.text_areas[0].text = "iter: " + str(itteration)
        dashboard.blit((0, 0))
        for tree in trees:
            field.draw_pixels(tree.get_pixels())

        for button in dashboard.buttons:  # отработка разжатия кнопок
            button.button_up()
        pygame.display.flip()
        pygame.time.wait(delay)  # задержка
else:
    while True:
        new_trees = []
        for tree in trees:
            new_tree = tree.grow(map)
            new_trees += new_tree
        trees = new_trees
        itteration += 1

        gf.save_genom(arguments, trees, itteration)
