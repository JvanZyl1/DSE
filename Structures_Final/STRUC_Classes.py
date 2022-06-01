"""
Classes
"""
from matplotlib import pyplot as plt
from math import *
import numpy as np
from STRUC_Fuselage import FuselageLoads

class Load:
    C_D = 1.
    rho = 1.225

    def __init__(self, L, gustspeed, P, torque):
        self.L = L
        self.D = 0.5 * self.C_D * self.rho * gustspeed ** 2
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
    def __init__(self, pos_x, pos_y, A, skin):
        self.X = pos_x
        self.Y = pos_y
        self.A = A
        self.B = 1
        self.skin = skin

    def boomarea(self, new_val):
        self.B = new_val

    def plot(self):
        plt.plot(self.X, self.Y, '--')
        plt.scatter(self.X, self.Y)

    def stress_z(self, n_x, n_y, Mx, My):
        pass

class CrossSection(Boom, FuselageLoads):
    def __init__(self, pos_z, radius, pos_x=None, pos_y=None, A=None, booms=None, skin=None):
        self.Z = pos_z
        self.radius = radius
        super().__init__(pos_x, pos_y, A, skin)
        if booms is None:
            self.booms = []
        else:
            self.booms = booms

    def add_boom(self, boom_lst):
        for boom in boom_lst:
            if boom not in self.booms:
                self.booms.append(boom)

    def remove_boom(self, boom):
        self.booms.remove(boom)

    def print_booms(self):
        for boom in self.booms:
            print('-->', boom.X)

    def neutral_x(self):
        tAx = 0
        tA = 0
        for boom in self.booms:
            tAx += boom.A * boom.X
            tA += boom.A
        return tAx / tA

    def neutral_y(self):
        tAy = 0
        tA = 0
        for boom in self.booms:
            tAy += boom.A * boom.Y
            tA += boom.A
        return tAy / tA

    def plot_booms(self):
        for boom in self.booms:
            boom.plot()
        plt.plot(self.neutral_x(), self.neutral_y(), '+k')
        plt.title('Booms')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.axis('equal')

    def plot_skin(self):
        self.booms.append(self.booms[0])
        for n in range(len(self.booms) - 1):
            if self.booms[n].skin != 0:
                plt.plot([self.booms[n].X[0], self.booms[n + 1].X[0]], [self.booms[n].Y[0], self.booms[n + 1].Y[0]],
                         linewidth=1000 * self.booms[n].skin)
                plt.plot([self.booms[n].X[1], self.booms[n + 1].X[1]], [self.booms[n].Y[1], self.booms[n + 1].Y[1]],
                         linewidth=1000 * self.booms[n].skin)
        plt.title('Skin panels')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.axis('equal')
        self.booms.remove(self.booms[-1])

    def boom_area(self):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[1])
        skin_b1 = []
        skin_b2 = []
        for n in range(len(nodes)-1):
            b1 = sqrt((nodes[n].X[0] - nodes[n + 1].X[0]) ** 2 +
                      (nodes[n].Y[0] - nodes[n + 1].Y[0]) ** 2)
            b2 = sqrt((nodes[n].X[1] - nodes[n + 1].X[1]) ** 2 +
                      (nodes[n].Y[1] - nodes[n + 1].Y[1]) ** 2)
            skin_b1.append(b1)
            skin_b2.append(b2)

        for n in range(0, len(nodes) - 2):
            self.booms[n].boomarea(np.array([self.booms[n].A + skin_b1[n] * self.booms[n].skin / 6 * 2 +
                                        skin_b1[n + 1] * self.booms[n+1].skin / 6 * (2),
                                        self.booms[n].A + skin_b2[n] * self.booms[n].skin / 6 * 2 +
                                        skin_b2[n + 1] * self.booms[n+1].skin / 6 * (2)]))
        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])



"""
    def stress_z(self):
        for boom in self.booms:
            sigma_z = self.Mx / (boom.B * (boom.Y - self.neutral_y()))
            print('$\sigma_z$ = ', sigma_z)
            """