import random
import numpy as np
from setting import Setting
from pixel import Pixel

setting = Setting


def get_occlusion(cell, trees):
    x, y = cell.position
    occlusion = 0
    for tree in trees:
        for pixel in tree.get_pixels():
            p_x, p_y = pixel.position
            if p_x == x and p_y < y:
                occlusion += 1
    return occlusion


def get_cell_energy(cell, trees):
    x, y = cell.position
    level = setting.height // setting.pixel_size - y + 5
    occlusion = get_occlusion(cell, trees)
    k = 3 - occlusion
    if k <= 0:
        return 0
    return k * level


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


def is_unique(position, array):
    position = tuple(position)
    for pixel in array:
        if pixel.position == position:
            return False
    return True


class Outgrowth(Pixel):
    def __init__(self, color, position, number=None):
        if 0 > position[0] or position[0] >= setting.width // setting.pixel_size or 0 > position[1] or position[
            1] >= setting.height // setting.pixel_size:
            raise Exception("position out of range")

        self.color = color
        self.border_color = (150, 150, 150)
        self.position = position
        self.number = number
        self.font_color = (0, 0, 0)

        self.energy = 0


class Tree:
    def __init__(self, start_x, start_y, genom):
        self.age = 0
        self.dead_age = random.randint(88, 92)
        self.energy = 300
        self.chromosoms = 16
        self.outgrowth_color = (150, 150, 150)
        self.wood_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.outgrowthes = [Outgrowth(self.outgrowth_color, (start_x, start_y), '0')]
        self.woods = []
        # up down left right
        if isinstance(genom, np.ndarray):
            self.genom = np.copy(genom)
        else:
            self.genom = np.array(
                [[random.randint(0, (self.chromosoms - 1) * 2) for _ in range(4)] for _ in range(self.chromosoms)])
        chance = random.randint(1, 100)
        if chance <= 25:
            # print('mutation')
            i, j = random.randint(0, self.chromosoms - 1), random.randint(0, 3)
            self.genom[i, j] = random.randint(0, (self.chromosoms - 1) * 2)
        # self.genom = np.array(
        #    [[13, 30, 14, 12],
        #     [30, 30, 30, 30],
        #     [30, 9, 30, 2],
        #     [30, 30, 30, 30],
        #     [30, 30, 30, 30],
        #     [30, 30, 30, 30],
        #     [30, 30, 30, 30],
        #     [30, 11, 30, 30],
        #     [15, 30, 30, 30],
        #     [30, 30, 30, 0],
        #     [30, 30, 30, 30],
        #     [6, 30, 8, 2],
        #     [30, 7, 30, 30],
        #     [8, 30, 30, 30],
        #     [30, 30, 30, 30],
        #     [30, 30, 30, 9]])

    def get_pixels(self):
        return self.outgrowthes + self.woods

    def grow(self, all_trees):
        # print('\nCells amount:', len(self.get_pixels()))
        # print('Energy:', self.energy)
        # print('Age:', self.age)
        consumption = len(self.get_pixels()) * 13
        coming = 0
        for wood in self.woods:
            coming += get_cell_energy(wood, all_trees)
        self.energy -= consumption
        self.energy += coming
        self.age += 1
        if self.energy < 0 or self.age == self.dead_age:
            # print('dead')
            new_t_x, y_field = set([]), setting.height // setting.pixel_size - 1
            for outgrowth in self.outgrowthes:
                t_x, t_y = outgrowth.position
                if is_free((t_x, y_field), all_trees):
                    new_t_x.add(t_x)
            sample_genom = np.copy(self.genom)
            new_trees = []
            for t_x in new_t_x:
                tree = Tree(t_x, y_field, sample_genom)
                new_trees.append(tree)
            return new_trees
        outgrowthes = sorted(self.outgrowthes, key=lambda x: get_occlusion(x, all_trees))
        self.outgrowthes = []
        appended_outgrowthes = []
        # print([o.number for o in outgrowthes])
        for outgrowth in outgrowthes:
            (x, y), genom_num = outgrowth.position, int(outgrowth.number)
            outgrowth.energy += get_cell_energy(outgrowth, all_trees)
            if outgrowth.energy >= 18:
                new_outgrowthes = self.genom[genom_num]
                # print(genom_num, new_outgrowthes)
                if new_outgrowthes[0] < self.chromosoms and is_free((x, y - 1), all_trees) and is_unique((x, y - 1),
                                                                                                         appended_outgrowthes):
                    appended_outgrowthes.append(Outgrowth(self.outgrowth_color, (x, y - 1), str(new_outgrowthes[0])))
                if new_outgrowthes[1] < self.chromosoms and is_free((x, y + 1), all_trees) and is_unique((x, y + 1),
                                                                                                         appended_outgrowthes):
                    appended_outgrowthes.append(Outgrowth(self.outgrowth_color, (x, y + 1), str(new_outgrowthes[1])))
                if new_outgrowthes[2] < self.chromosoms:
                    x_end = setting.width // setting.pixel_size - 1
                    if x == 0:
                        if is_free((x_end, y), all_trees) and is_unique((x_end, y), appended_outgrowthes):
                            appended_outgrowthes.append(
                                Outgrowth(self.outgrowth_color, (x_end, y), str(new_outgrowthes[2])))
                    else:
                        if is_free((x - 1, y), all_trees) and is_unique((x - 1, y), appended_outgrowthes):
                            appended_outgrowthes.append(
                                Outgrowth(self.outgrowth_color, (x - 1, y), str(new_outgrowthes[2])))
                if new_outgrowthes[3] < self.chromosoms:
                    x_end = setting.width // setting.pixel_size - 1
                    if x == x_end:
                        if is_free((0, y), all_trees) and is_unique((0, y), appended_outgrowthes):
                            appended_outgrowthes.append(
                                Outgrowth(self.outgrowth_color, (0, y), str(new_outgrowthes[3])))
                    else:
                        if is_free((x + 1, y), all_trees) and is_unique((x + 1, y), appended_outgrowthes):
                            appended_outgrowthes.append(
                                Outgrowth(self.outgrowth_color, (x + 1, y), str(new_outgrowthes[3])))
                outgrowth.color = self.wood_color
                outgrowth.number = None
                self.woods.append(outgrowth)
            else:
                appended_outgrowthes.append(outgrowth)
        self.outgrowthes = appended_outgrowthes
        return [self]