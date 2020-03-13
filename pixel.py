class Pixel:
    def __init__(self, color, position):
        self.color = color
        self.position = position

class PixelNum(Pixel):
    def __init__(self, color, position, number):
        self.color = color
        self.position = position
        self.number = number