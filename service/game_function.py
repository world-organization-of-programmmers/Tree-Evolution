import pygame
import sys


def check_event(button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if button.is_pressed(event):
            print("pressed")


