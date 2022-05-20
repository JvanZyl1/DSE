"""
Full Structural Design
"""


class VTOL:
    pass


class Beam(VTOL):

    def __init__(self, weight, length, radius, weight_engine, thickness):
        self.weight = weight
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
