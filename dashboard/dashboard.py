from dashboard.button import Button, Switch
from dashboard.text_area import TextArea
import pygame


class Dashboard:

    def __init__(self, screen, setting):
        self.screen = screen
        self.width = setting.width
        self.height = setting.dashboard_height
        self.surface = pygame.Surface((self.width, self.height))
        self._obj_count = 6
        self._border = 4
        tmp = (self.width - (self._obj_count-2) * self._border) / 25
        print(tmp)
        self.buttons = [Button(self.surface, (210, 210, 250), (0, 0, 3*tmp, self.height), "speed +", (0, 0, 0),int(tmp*1.1)),
                        Button(self.surface, (250, 210, 210), (3*tmp+3, 0, 3*tmp, self.height), "speed -", (0, 0, 0), int(tmp*1.1)),
                        Button(self.surface, (210, 250, 210), (6*tmp+6, 0, 4*tmp, 100), "save genom", (0, 0, 0), int(tmp)),
                        Button(self.surface, (250, 250, 210), (10*tmp+9, 0, 5*tmp, 100), "new simulation", (0, 0, 0),int(tmp*0.98))]
        self.text_areas = [TextArea(self.surface, (210, 250, 250), (15*tmp+12, 0, 6*tmp, 100), "itteration: ", (0, 0, 0),int(tmp))]
        self.switches = [Switch(self.surface, (250, 210, 250), (21*tmp+15, 0, 4*tmp, 100), "step mode", (0, 0, 0),int(tmp*1.1))]

    def draw(self):
        for obj in self.buttons + self.text_areas + self.switches:
            obj.draw()

    def blit(self, pos):
        self.screen.blit(self.surface, pos)
