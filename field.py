from pixel import PixelNum
import pygame


class Field:
    def __init__(self, screen, setting):
        self.screen = screen
        self.size = setting.pixel_size
        self.width = setting.width // setting.pixel_size
        self.height = setting.height // setting.pixel_size
        print(self.width, self.height)
        self.field = [[PixelNum() for i in range(self.height)] for j in range(self.width)]

    def blit(self):
        for i in range(self.width):
            for j in range(self.height):
                pixel = self.field[i][j]
                rect = pygame.draw.rect(self.screen, pixel.color,
                                        (i * self.size, j * self.size, (i + 1) * self.size, (j + 1) * self.size))
                if pixel.number:
                    font = pygame.font.Font(None, self.size)
                    number = font.render(str(pixel.number), 1, pixel.font_color)
                    rect.centery += self.size // 4
                    rect.centerx += self.size // 5
                    self.screen.blit(number, rect)

    def draw(self, color, position, number):
        self.field[position[0]][position[1]].color = color
        self.field[position[0]][position[1]].number = number

    def fill(self, color):
        for arr in self.field:
            for pixel in arr:
                pixel.color = color
                pixel.number = None
