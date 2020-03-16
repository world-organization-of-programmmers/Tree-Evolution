from setting import Setting

setting = Setting


class Pixel:
    def __init__(self, color, position, number=None):
        if 0 > position[0] or position[0] >= setting.width // setting.pixel_size or 0 > position[1] or position[
            1] >= setting.height // setting.pixel_size:
            raise Exception("position out of range")
        
        self.color = color
        self.border_color = (150, 150, 150)
        self.position = position
        self.number = number
        self.font_color = (0, 0, 0)
