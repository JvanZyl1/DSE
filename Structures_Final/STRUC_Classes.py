"""
Classes
"""
from matplotlib import pyplot as plt

class Load:
    C_D = 1.
    rho = 1.225

    def __init__(self, L, gustspeed, P, torque):
        self.L = L
        self.D = 0.5*self.C_D*self.rho*gustspeed**2
        self.P = P
        self.T = torque


class Material:

    def __init__(self, tensile_strength, yield_strength, E_modulus, shear_strength, density, G_modulus):
        self.sigma_t = tensile_strength  # Pa
        self.sigma_y = yield_strength  # Pa
        self.E_modulus = E_modulus  # Pa
        self.tau = shear_strength  # Pa
        self.density = density  # kg/m**3
        self.G_modulus = G_modulus

class Boom:
    def __init__(self, pos_x, pos_y):
        self.X = pos_x
        self.Y = pos_y


class CrossSection(Boom):
    def __init__(self, pos_x, pos_y, pos_z, radius, booms = None):
        self.Z = pos_z
        self.radius = radius
        super().__init__(pos_x, pos_y)
        if booms is None:
            self.booms = []
        else:
            self.booms = booms

    def add_boom(self, boom_lst):
        for boom in boom_lst:
            if boom not in self.booms:
                self.booms.append(boom)

    def remove_boom(self, boom):
        for boom in self.booms:
            self.booms.remove(boom)

    def print_booms(self):
        for boom in self.booms:
            print('-->', boom.X)
