from setting import Setting

setting = Setting


def is_free(position, trees):
    for tree in trees:
        for wood in tree.woods:
            if wood.position == position:
                return False
        for outgrowth in tree.outgrowthes:
            if outgrowth.position == position:
                return False

        if 0 > position[0] or position[0] >= setting.width // setting.pixel_size or 0 > position[1] or position[
            1] >= setting.height // setting.pixel_size:
            return False
    return True
