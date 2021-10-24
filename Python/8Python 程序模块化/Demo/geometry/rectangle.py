'''
This file defines Rectangle
'''
from math_lib.add import add


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_lenth(self):
        return 2*add(self.height, self.width)
