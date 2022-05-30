"""
Full Structural Design
"""

from math import *


class Part:

    def __init__(self, material, length):
        self.area = 0
        self.weight = material.density * length * self.area



class Beam(Part):
    name = "beam"
    K = 8
    n = 0
    def __init__(self, material, length, radius, weight_engine, thickness):
        super().__init__(material, length)
        self.area = 2 * pi * thickness * radius
        self.length = length
        self.radius = radius
        self.thickness = thickness
        self.Ixx = thickness * radius ** 3
        self.Iyy = thickness * radius ** 3
        Beam.n += 1
        self.weight_engine = weight_engine * 9.81


class Fuselage(Part):
    pass


class Gear(Part):
    name = "gear"
    def __init__(self, material, length, radius, thickness):
        super().__init__(material, length)
        self.area = 2 * pi * thickness * radius
        self.length = 0.2
        self.radius = radius
        self.thickness = thickness
        self.weight_engine = 0
        self.n = 4

