# Classes

from math import *
import numpy as np



class Material:

    def __init__(self, tensile_strength, yield_strength, E_modulus, shear_strength, density):
        self.sigma_t = tensile_strength  # Pa
        self.sigma_y = yield_strength  # Pa
        self.E_modulus = E_modulus  # Pa
        self.tau = shear_strength  # Pa
        self.density = density  # kg/m**3


class Beam:

    def __init__(self, material, length=0, radius, thickness):
        self.weight = None
        self.length = length
        self.radius = radius
        self.thickness = thickness
        self.density = material.density

    def W_beam(self, density, radius, thickness, length):
        self.weight = density * 2 * pi * radius * thickness * length


class Axes(Beam):
    dx, dy, dz = 0.005, 0.005, 0.01
    z = np.arange(0, Beam.length + dz, dz)  # Beam span Direction
    x = np.arange(-r, r, dx)  # Vertical Direction
    y = np.arange(-r, r, dy)

class CaseLift:

    def __init__(self, L_x, L_y, L_z):
        self.L_x = L_x
        self.L_y = L_y
        self.L_z = L_z


# Lift Cases
Lift_Grounded = (0, 0, 0)
Lift_Vertical = (8000,0,0)




print(beam1.density)
# print(aluminium.sigma_t)
