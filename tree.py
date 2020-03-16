import numpy as np
from setting import Setting
from pixel import Pixel

setting = Setting


def is_free(position, trees):
    position = tuple(position)
    if 0 > position[0] or position[0] >= setting.width // setting.pixel_size or \
            0 > position[1] or position[1] >= setting.height // setting.pixel_size:
        return False
    for tree in trees:
        for pixel in tree.get_pixels():
            if pixel.position == position:
                return False
    return True


class Tree:
    def __init__(self, start_x, start_y):
        self.chromosoms = 4
        self.outgrowth_color = (150, 150, 150)
        self.wood_color = (0, 255, 0)
        self.outgrowthes = [Pixel(self.outgrowth_color, (start_x, start_y), '0')]
        self.woods = []
        # up down left right
        self.genom = np.array(
            [[2, 0, 4, 6],
             [4, 4, 6, 7],
             [5, 8, 0, 7],
             [0, 5, 7, 3]])

    def get_pixels(self):
        return self.outgrowthes + self.woods

    def grow(self, all_trees):
        outgrowthes = self.outgrowthes
        self.outgrowthes = []
        for i, outgrowth in enumerate(outgrowthes):
            (x, y), genom_num = outgrowth.position, int(outgrowth.number)
            new_outgrowthes = self.genom[genom_num]
            print(new_outgrowthes)
            if new_outgrowthes[0] < self.chromosoms and is_free((x, y - 1), all_trees):
                self.outgrowthes.append(Pixel(self.outgrowth_color, (x, y - 1), str(new_outgrowthes[0])))
            if new_outgrowthes[1] < self.chromosoms and is_free((x, y + 1), all_trees):
                self.outgrowthes.append(Pixel(self.outgrowth_color, (x, y + 1), str(new_outgrowthes[1])))
            if new_outgrowthes[2] < self.chromosoms and is_free((x - 1, y), all_trees):
                self.outgrowthes.append(Pixel(self.outgrowth_color, (x - 1, y), str(new_outgrowthes[2])))
            if new_outgrowthes[3] < self.chromosoms and is_free((x + 1, y), all_trees):
                self.outgrowthes.append(Pixel(self.outgrowth_color, (x + 1, y), str(new_outgrowthes[3])))
            outgrowth.color = self.wood_color
            outgrowth.number = None
            self.woods.append(outgrowth)
