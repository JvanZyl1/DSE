from STRUC_Class_Boom import Boom
from matplotlib import pyplot as plt
from math import *
import numpy as np
from STRUC_Inputs import *


# Define Cross-Section
class CrossSection(Boom):
    def __init__(self, pos_z, radius, pos_x=None, pos_y=None, A=None, booms=None, t=None):
        self.Z = pos_z  # np.array([z1, z2]) [m]
        self.R = radius  # np.array([r1, r2]) [m]
        self.L = float(pos_z[1]) - float(pos_z[0])
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
                boom.properties_cs(self.R, self.L)
                self.booms.append(boom)

    def remove_boom(self, boom):
        self.booms.remove(boom)

    def print_booms(self):
        for boom in self.booms:
            print('-->', boom.X)

    def neutral_x(self):
        tBx, tB = 0, 0
        for boom in self.booms:
            tBx += boom.B * boom.X
            tB += boom.B
        self.nx = tBx / tB
        return self.nx

    def neutral_y(self):
        tBy, tB = 0, 0
        for boom in self.booms:
            tBy += boom.B * boom.Y
            tB += boom.B
        self.ny = tBy / tB
        return self.ny

    def plot_booms(self, show=False):
        for boom in self.booms:
            boom.plot()
        plt.plot(self.neutral_x(), self.neutral_y(), '+k')
        plt.title('Booms')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.axis('equal')
        if show:
            plt.show()

    def plot_skin(self, show=False):
        self.booms.append(self.booms[0])
        for n in range(len(self.booms) - 1):
            boom_n = self.booms[n]
            boom_n1 = self.booms[n + 1]
            if boom_n.t != 0:
                print(boom_n.t, boom_n.X, boom_n.Y)
                plt.plot([boom_n.X[0], boom_n1.X[0]], [boom_n.Y[0], boom_n1.Y[0]], c='y',
                         linewidth=1000 * boom_n.t, zorder=0)
                plt.plot([boom_n.X[1], boom_n1.X[1]], [boom_n.Y[1], boom_n1.Y[1]], c='y',
                         linewidth=1000 * boom_n.t, zorder=0)
        plt.title('Skin panels')
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.axis('equal')
        self.booms.remove(self.booms[-1])
        if show:
            plt.show()
    """
    def step(self, z_start):
        if self.Z[0] >= z_start and self.Z[1] >= z_start:
            return 1, 1
        elif self.Z[0] < z_start and self.Z[1] >= z_start:
            return 0, 1
        elif self.Z[0] >= z_start and self.Z[1] < z_start:
            return 1, 0
        return 0, 0  # np.where(self.z < z_start, 0, 1)

    def Mx(self):
        Mx = [-2000 * self.Z[0] ** 2 + 400 * self.step(0.2)[0] ** 2,
              -2000 * self.Z[1] ** 2 + 400 * self.step(0.2)[1] ** 2]
        return Mx

    def My(self):
        My = [-200 * self.Z[0] ** 2 + 400 * self.step(0.2)[0] ** 2,
              -200 * self.Z[1] ** 2 + 400 * self.step(0.2)[1] ** 2]
        return My
    """

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

    def stresses_z(self, yield_strength, M_x, M_y):
        print(M_x, M_y)
        Ixx, Iyy = self.Ixx_cs(), self.Iyy_cs()


        """
        stress_cs0, stress_cs1 = [], []

        for boom in self.booms:
            stress_cs0.append(boom.stress_z(self.nx, self.ny, Mx, My, Ixx, Iyy)[0])
            stress_cs1.append(boom.stress_z(self.nx, self.ny, Mx, My, Ixx, Iyy)[1])

        return stress_cs0, stress_cs1
        """
    def skin_length(self):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[1])
        t_b1 = []
        t_b2 = []

        for n in range(len(nodes) - 1):
            node, node1 = nodes[n], nodes[n + 1]
            b1 = sqrt((node.X[0] - node1.X[0]) ** 2 + (node.Y[0] - node1.Y[0]) ** 2)
            b2 = sqrt((node.X[1] - node1.X[1]) ** 2 + (node.Y[1] - node1.Y[1]) ** 2)
            t_b1.append(b1), t_b2.append(b2)

        return t_b1, t_b2


"""
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
        x_i = []
        ny = []
        boom1 = []
        boom2 = []
        boom3 = []
        boom4 = []
        for i in range(200):
            x_i.append(i)
            ny.append(self.neutral_y())
            self.stresses_z()
            for n in range(len(nodes) - 2):
                b_n0, b_n1, b_n2 = self.booms[n], self.booms[n + 1], self.booms[n + 2]
                if self.Z[0] == 0:
                    b_n1.area(np.array([b_n1.A[0],
                                        b_n1.A[1] +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n0.sigma_z[1]) +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n2.sigma_z[1])]))
                else:
                    b_n1.area(np.array([b_n1.A[0] +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[0] / b_n0.sigma_z[0]) +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[0] / b_n2.sigma_z[0]),
                                        b_n1.A[1] +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n0.sigma_z[1]) +
                                        t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n2.sigma_z[1])]))
                if n == 1:
                    print('Previous node', t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n0.sigma_z[1]), '   Next node', t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n2.sigma_z[1]))

            boom1.append(self.booms[1].B[1])
            boom2.append(self.booms[2].B[1])
            boom3.append(self.booms[3].B[1])
            boom4.append(self.booms[4].B[1])
        plt.plot(x_i, boom1)
        plt.plot(x_i, boom2)
        plt.plot(x_i, boom3)
        plt.plot(x_i, boom4)

        plt.plot(x_i, ny)
        plt.show()
        for boom in self.booms:
            print(boom.B)
        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])

    def boom_area_updated(self):
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

        for n in range(len(nodes) - 2):
            nx, ny = self.neutral_x(), self.neutral_y()
            b_n0, b_n1, b_n2 = self.booms[n], self.booms[n + 1], self.booms[n + 2]
            if (b_n1.Y[0]-self.nx[0]) / (b_n0.Y[0]-self.ny[0]) >= 0:
                ratio_1_2 = 1
            elif:
                pass
            if (b_n1.Y[0]-self.nx[0]) / (b_n2.Y[0]-self.ny[0]) >= 0:
                ratio_1_0 = 1








            if self.Z[0] == 0:
                b_n1.area(np.array([b_n1.A[0],
                                    b_n1.A[1] +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n0.sigma_z[1]) +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n2.sigma_z[1])]))
            else:
                b_n1.area(np.array([b_n1.A[0] +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[0] / b_n0.sigma_z[0]) +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[0] / b_n2.sigma_z[0]),
                                    b_n1.A[1] +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n0.sigma_z[1]) +
                                    t_b1[n + 1] * b_n1.t / 6 * (2 + b_n1.sigma_z[1] / b_n2.sigma_z[1])]))

        for boom in self.booms:
            print(boom.B)
        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])
"""
