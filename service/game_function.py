import numpy as np
import os
import sys
import getopt
import re
from service.setting import Setting
from tree.tree import Tree


def save_genom(arguments, trees, itteration):
    if arguments['itter_save'] and trees and itteration % arguments['itter_save'] == 0:
        name = arguments['folder'] + '/TreesGenom_' + str(itteration) + '_iteration'
        os.mkdir(name)
        for i in range(len(trees)):
            np.save(name + '/tree_' + str(i), trees[i].genom)


def create_arguments(arguments, args, setting):
    opts, argv = getopt.getopt(args, 'o:i:t:',
                               ['cli', 'step_mode', 'width=', 'height=', 'pixel_size=', 'genoms=', 'restore'])
    restore = False

    for opt, arg in opts:
        if opt == '-o':
            arguments['folder'] = arg

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
        if opt == '--genoms':
            arguments['genoms_folder'] = arg
        if opt == '--restore':
            restore = True
    if restore and arguments['genoms_folder']:
        raise Exception('--restore and --genom at the same time')

    try:
        os.mkdir(arguments['folder'])
    except FileExistsError:
        if restore:
            last_seved_genom = get_max_itteration(os.listdir(arguments['folder']))

            arguments['genoms_folder'] = arguments['folder'] + '/' + last_seved_genom




        else:
            raise FileExistsError

    return arguments, setting


def get_genoms(arguments):
    genoms = []

    for file in os.listdir(arguments['genoms_folder']):  # read genomes from files
        genoms.append(np.load(arguments['genoms_folder'] + '/' + file))

    return genoms


def create_trees(arguments, setting, map):
    if arguments['genoms_folder']:  # create trees with genoms from files
        genoms = get_genoms(arguments)

        arguments['trees_count'] = len(genoms)

        trees = [Tree(i * int(setting.width / setting.pixel_size / arguments['trees_count']),
                      setting.height // setting.pixel_size - 1, genoms[i], map) for i in
                 range(arguments['trees_count'])]
        iteration = int(re.search(r'\d+', arguments['genoms_folder'])[0]) + 1



    else:
        trees = [Tree(step, setting.height // setting.pixel_size - 1, 0, map) for step in
                 range(0, setting.width // setting.pixel_size,
                       int(setting.width / setting.pixel_size // arguments['trees_count']))]
        iteration = 0
    return trees, iteration


def get_max_itteration(folder):
    last_seves_genoms = re.search('\D*(\d+)\D*', folder[0])
    for genom in folder:
        index = re.search('\D*(\d+)\D*', genom)

        if int(last_seves_genoms[1]) < int(index[1]):
            last_seves_genoms = index

    return last_seves_genoms[0]
