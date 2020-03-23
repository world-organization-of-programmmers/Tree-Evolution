import pygame
import sys
from dashboard.button import Button


def check_event(event, dashboard, ):
    if event.type == pygame.QUIT:
        sys.exit()


def change_speed(event, dashboard, delay):
    if dashboard.buttons[0].is_pressed(event):
        if delay > 0:
            delay -= 10
    if dashboard.buttons[1].is_pressed(event):
        delay += 10
    return delay


def tree_event(trees):
    new_trees = []
    for tree in trees:
        new_tree = tree.grow(trees + new_trees)
        new_trees += new_tree
    return new_trees


def draw_objects(field, dashboard, trees, itteration):
    field.fill()
    dashboard.draw()
    dashboard.text_areas[0].text = "itteration: " + str(itteration)
    dashboard.blit((0, 0))

    for tree in trees:
        field.draw_pixels(tree.get_pixels())
