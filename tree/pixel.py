from setting import Setting

setting = Setting


class Pixel:
    def __init__(self, color, position, number=None):
        self.color = color
        self.border_color = (150, 150, 150)
        self.position = position
        self.number = number
        self.font_color = (0, 0, 0)
