import numpy as np
from setting import Setting
from field import Field
from pixel import Pixel, PixelNum

setting = Setting

class Tree:
    def __init__(self, start_y, start_x):
        self.chromosoms = 4
        self.outgrowth_color = (150, 150, 150)
        self.wood_color = (0, 255, 0)
        self.outgrowthes = [PixelNum(self.outgrowth_color, (start_y, start_x), 0)]
        self.woods = []
        # up down left right
        self.genom = np.array(
            [[2, 0, 4, 6],
             [4, 4, 6, 7],
             [5, 8, 0, 7],
             [0, 5, 7, 3]])

    def grow(self, area):
        for i, outgrowth in enumerate(self.outgrowthes):
            (y, x), genom_num = outgrowth.position, outgrowth.number
            new_outgrowthes = self.genom[genom_num]
            print(new_outgrowthes)
            if y > 0 and new_outgrowthes[0] < self.chromosoms and area.field[y - 1, x] == setting.bg_color:
                area[y - 1, x] = self.outgrowth_color
                str(new_outgrowthes[0])
                Outgrowthes.append([y - 1, x])
            if y < N - 1 and new_outgrowthes[1] < self.chromosoms and Area[y + 1, x] != '*':
                Area[y + 1, x] = str(new_outgrowthes[1])
                Outgrowthes.append([y + 1, x])
            if x > 0 and new_outgrowthes[2] < self.chromosoms and Area[y, x - 1] != '*':
                Area[y, x - 1] = str(new_outgrowthes[2])
                Outgrowthes.append([y, x - 1])
            if x < N - 1 and new_outgrowthes[3] < self.chromosoms and Area[y, x + 1] != '*':
                Area[y, x + 1] = str(new_outgrowthes[3])
                Outgrowthes.append([y, x + 1])
            del Outgrowthes[i]
            Area[y, x] = '*'