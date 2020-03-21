from dashboard.button import Button
from dashboard.text_area import TextArea
import pygame
import re


class Dashboard:

    def __init__(self, screen, setting):
        self.screen = screen
        self.width = setting.width
        self.height = 60
        self.surface = pygame.Surface((self.width, self.height))
        self.buttons = [Button(self.surface, (250, 250, 250), (3, 0, 184, 100), "speed +", (0, 0, 0), 70),
                        Button(self.surface, (150, 150, 150), (193, 0, 184, 100), "speed -", (0, 0, 0), 70),
                        Button(self.surface, (250, 250, 250), (383, 0, 234, 100), "save genom", (0, 0, 0), 50),
                        Button(self.surface, (150, 150, 150), (623, 0, 254, 100), "new simulation", (0, 0, 0), 50)]
        self.text_areas = [TextArea(self.surface, (250, 250, 250), (883, 0, 314, 100), "itteration: ", (0, 0, 0), 50)]

    def draw(self):
        for obj in self.buttons + self.text_areas:
            obj.draw()

    def blit(self, pos):
        self.screen.blit(self.surface, pos)
