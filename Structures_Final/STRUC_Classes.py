"""
Classes
"""
from matplotlib import pyplot as plt
from math import *
import numpy as np


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
        self.skin = skin


class CrossSection(Boom):
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

    def plot_booms(self):
        for boom in self.booms:
            plt.plot(boom.X, boom.Y, '--')
            plt.scatter(boom.X, boom.Y)
        plt.title('Booms')
        plt.xlabel('y [m]')
        plt.ylabel('x [m]')
        plt.axis('equal')
        plt.show()

    def plot_skin(self):
        self.booms.append(self.booms[0])
        for n in range(len(self.booms) - 1):
            if self.booms[n].skin != 0:
                plt.plot([self.booms[n].X[0], self.booms[n + 1].X[0]], [self.booms[n].Y[0], self.booms[n + 1].Y[0]],
                         linewidth=1000 * self.booms[n].skin)
                plt.plot([self.booms[n].X[1], self.booms[n + 1].X[1]], [self.booms[n].Y[1], self.booms[n + 1].Y[1]],
                         linewidth=1000 * self.booms[n].skin)
        plt.title('Skin panels')
        plt.xlabel('y [m]')
        plt.ylabel('x [m]')
        plt.axis('equal')
        plt.show()
        self.booms.remove(self.booms[-1])

    def boom_area(self):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[0])
        skin_l1 = []
        skin_l2 = []
        for n in range(len(nodes) - 1):
            l1 = sqrt((nodes[n].X[0] - nodes[n + 1].X[0]) ** 2 +
                      (nodes[n].Y[0] - nodes[n + 1].Y[0]) ** 2)
            l2 = sqrt((nodes[n].X[1] - nodes[n + 1].X[1]) ** 2 +
                      (nodes[n].Y[1] - nodes[n + 1].Y[1]) ** 2)
            skin_l1.append(l1)
            skin_l2.append(l2)

        for n in range(len(nodes) - 2):
            self.booms[n].B = np.array([self.booms[n].A + skin_l1[n] * self.booms[n].skin / 6 * 2 +
                                        skin_l1[n + 1] * self.booms[n+1].skin / 6 * 2,
                                        self.booms[n].A + skin_l2[n] * self.booms[n].skin / 6 * 2 +
                                        skin_l2[n + 1] * self.booms[n+1].skin / 6 * 2])
            print(self.booms[n].B)

        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])

