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


# Define Boom
class Boom:
    def __init__(self, pos_x, pos_y, A, t):
        self.X = pos_x
        self.Y = pos_y
        self.A = np.array([A, A])
        self.B = np.array([A, A])
        self.t = t
        self.sigma_z = [0, 0]

    def area(self, new_val):
        self.B = new_val

    def plot(self):
        plt.plot(self.X, self.Y, '--')
        plt.scatter(self.X, self.Y)

    def Ixx(self, n_y):
        return [self.B[0] * (self.Y[0]-n_y[0]) ** 2, self.B[1] * (self.Y[1]-n_y[1]) ** 2]

    def Iyy(self, n_x):
        return [self.B[0] * (self.X[0]-n_x[0]) ** 2, self.B[1] * (self.X[1]-n_x[1]) ** 2]

    def stress_z(self, n_x, n_y, M_x, M_y):
        self.sigma_z = [M_x[0] * self.Y[0] / self.Ixx(n_y)[0] + M_y[0] / self.X[0] * self.Iyy(n_x)[0],
                        M_x[1] * self.Y[1] / self.Ixx(n_y)[1] + M_y[1] / self.X[1] * self.Iyy(n_x)[1]]
        """
        print("| Mx =", M_x[1])
        print("| B1 =", self.B[1])
        print("| Y1 =", self.Y[1])
        print("| ny1 =", n_y[1])
        print("| My1 =", M_y[1])
        print("| X1 =", self.X[1])
        print("| nx1 =", n_x[1])
        print("| sigma_z =", self.sigma_z)
        """



# Define Cross-Section
class CrossSection(Boom):
    def __init__(self, pos_z, radius, pos_x=None, pos_y=None, A=None, booms=None, t=None):
        self.Z = pos_z
        self.radius = radius
        self.Ixx_CS = np.array([0,0])
        self.Iyy_CS = np.array([0,0])
        super().__init__(pos_x, pos_y, A, t)
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

    def plot_t(self):
        self.booms.append(self.booms[0])
        for n in range(len(self.booms) - 1):
            if self.booms[n].t != 0:
                plt.plot([self.booms[n].X[0], self.booms[n + 1].X[0]], [self.booms[n].Y[0], self.booms[n + 1].Y[0]],
                         linewidth=1000 * self.booms[n].t)
                plt.plot([self.booms[n].X[1], self.booms[n + 1].X[1]], [self.booms[n].Y[1], self.booms[n + 1].Y[1]],
                         linewidth=1000 * self.booms[n].t)
        plt.title('Skin panels')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.axis('equal')
        self.booms.remove(self.booms[-1])

    def step(self, pos_z_start):
        if self.Z[0] >= pos_z_start and self.Z[1] >= pos_z_start:
            return 1, 1
        elif self.Z[0] < pos_z_start and self.Z[1] >= pos_z_start:
            return 0, 1
        elif self.Z[0] >= pos_z_start and self.Z[1] < pos_z_start:
            return 1, 0
        return 0, 0  # np.where(self.z < pos_z_start, 0, 1)

    def Mx(self):
        Mx = [-2000 * self.Z[0] ** 2 + 400 * self.step(0.2)[0] ** 2,
              -2000 * self.Z[1] ** 2 + 400 * self.step(0.2)[1] ** 2]
        print('Mx =', Mx)
        return Mx

    def My(self):
        My = [-200 * self.Z[0] ** 2 + 400 * self.step(0.2)[0] ** 2,
              -200 * self.Z[1] ** 2 + 400 * self.step(0.2)[1] ** 2]
        print('My =', My)
        return My

    def Ixx_cs(self):
        for boom in self.booms:
            self.Ixx_CS[0] += boom.Ixx(self.neutral_y())[0]
            self.Ixx_CS[1] = np.add(self.Ixx_CS[1], boom.Ixx(self.neutral_y())[1])
            print(boom.Ixx(self.neutral_y())[1])
            print(self.Ixx_CS)

    def Iyy_cs(self):
        for boom in self.booms:
            self.Iyy_CS[0] += boom.Iyy(self.neutral_x())[0]
            self.Iyy_CS[1] += boom.Iyy(self.neutral_y())[1]

    def stresses_z(self, boom):
        nx = np.array(self.neutral_x())
        ny = np.array(self.neutral_y())
        Mx = np.array(self.Mx())
        My = np.array(self.My())

        boom.stress_z(nx, ny, Mx, My)
        return boom.sigma_z

    def boom_area(self):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[1])
        t_b1 = []
        t_b2 = []

        for n in range(len(nodes) - 1):
            b1 = sqrt((nodes[n].X[0] - nodes[n + 1].X[0]) ** 2 +
                      (nodes[n].Y[0] - nodes[n + 1].Y[0]) ** 2)
            b2 = sqrt((nodes[n].X[1] - nodes[n + 1].X[1]) ** 2 +
                      (nodes[n].Y[1] - nodes[n + 1].Y[1]) ** 2)
            t_b1.append(b1)
            t_b2.append(b2)
        for i in range(1):
            for n in range(len(nodes) - 2):
                b_n0 = self.booms[n]
                b_n1 = self.booms[n + 1]
                b_n2 = self.booms[n + 2]
                b_n1.area(np.array([b_n1.A[0] +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.Y[0] / b_n0.Y[0]) +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.Y[0] / b_n2.Y[0]),
                                    b_n1.A[1] +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.Y[1] / b_n0.Y[1]) +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.Y[1] / b_n2.Y[1])]))
        for boom in self.booms:
            print(boom.B)
        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])
