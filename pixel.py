from setting import Setting

setting = Setting


class PixelNum:
    def __init__(self, color, position, number=None):
        self.color = color
        if 0 > position[0] or position[0] >= setting.width // setting.pixel_size or 0 > position[1] or position[
            1] >= setting.height // setting.pixel_size:
            raise Exception("position out of range")

        self.position = position
        self.number = number
        self.font_color = (0, 0, 0)
