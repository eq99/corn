'''
This file defines Circle
'''

from math_lib.constant import pi


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return pi*self.radius**2
