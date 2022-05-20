"""
Full Structural Design
"""

from math import *

class VTOL:
    pass


class Beam(VTOL):
    K = 8
    def __init__(self, material, length, radius, weight_engine, thickness):
        self.weight = material.density*radius * 2 * pi * length * thickness
        self.length = length
        self.radius = radius
        self.weight_engine = weight_engine * 9.81
        self.thickness = thickness
        self.Ixx = thickness * radius ** 3
        self.Iyy = thickness * radius ** 3


class Fuselage(VTOL):
    pass


class Gear(VTOL):
    pass
