import numpy as np
import os
import sys
import getopt


def save_genom(arguments, trees, itteration):
    if arguments['itter_save'] and arguments['folder'] and itteration % arguments['itter_save'] == 0:
        name = arguments['folder'] + '/TreesGenom_' + str(itteration) + '_iteration'
        os.mkdir(name)
        for i in range(len(trees)):
            np.save(name + '/tree_' + str(i), trees[i].genom)


def create_arguments(arguments, args,setting):
    opts, argv = getopt.getopt(args, 'o:i:t:', ['cli', 'step_mode', 'width=', 'height=', 'pixel_size='])

    for opt, arg in opts:
        if opt == '-o':
            arguments['folder'] = arg
            os.mkdir(arg)
        if opt == '-i':
            arguments['itter_save'] = int(arg)
        if opt == '-t':
            arguments['trees_count'] = int(arg)
        if opt == '--cli':
            arguments['non_gui'] = True
        if opt == '--step_mode':
            arguments['step_mode'] = True
        if opt == '--width':
            setting.width = int(arg)
        if opt == '--height':
            setting.height = int(arg)
        if opt == '--pixel_size':
            setting.pixel_size = int(arg)

    return arguments, setting
