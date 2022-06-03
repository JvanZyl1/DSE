from STRUC_Class_Boom import Boom
from matplotlib import pyplot as plt
from math import *
import numpy as np

# Define Cross-Section
class CrossSection(Boom):
    def __init__(self, pos_z, radius, pos_x=None, pos_y=None, A=None, booms=None, t=None):
        self.Z = pos_z
        self.nx = [0, 0]
        self.ny = [0, 0]
        self.radius = radius
        self.Ixx_CS = [0, 0]
        self.Iyy_CS = [0, 0]
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
            self.Ixx_CS[1] += boom.Ixx(self.neutral_y())[1]
        return self.Ixx_CS

    def Iyy_cs(self):
        for boom in self.booms:
            self.Iyy_CS[0] += boom.Iyy(self.neutral_x())[0]
            self.Iyy_CS[1] += boom.Iyy(self.neutral_y())[1]
        return self.Iyy_CS

    def stresses_z(self):
        nx, ny = np.array(self.neutral_x()), np.array(self.neutral_y())
        Mx, My = np.array(self.Mx()), np.array(self.My())
        Ixx, Iyy = self.Ixx_cs(), self.Iyy_cs()
        for boom in self.booms:
            print(boom.stress_z(nx, ny, Mx, My, Ixx, Iyy))

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