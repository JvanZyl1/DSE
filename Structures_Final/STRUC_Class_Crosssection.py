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

    def boom_area(self, sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[1])
        t_b = self.skin_length(n)

        for i in range(len(nodes) - 2):
            b_i0, b_i1, b_i2 = self.booms[i], self.booms[i + 1], self.booms[i + 2]
            s_i0 = b_i0.stress_max(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)
            s_i1 = b_i1.stress_max(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)
            s_i2 = b_i2.stress_max(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)
            if self.Z[n] == 0:
                b_i1.area(n, b_i1.A[0])
            else:

                b_i1.area(n, b_i1.A[0] +
                          t_b[n + 1] * b_i1.t / 6 * (2 + s_i1 / s_i0) +
                          t_b[n + 1] * b_i1.t / 6 * (2 + s_i1 / s_i2))
        self.Ixx_cs(), self.Iyy_cs()
        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])

    def stress_CS(self, sigma_y, E, M_x, M_y, n):
        n_x, n_y = self.neutral_x()[n], self.neutral_y()[n]
        Ixx, Iyy = self.Ixx_cs()[n], self.Iyy_cs()[n]
        for boom in self.booms:
            boom.stress_boom(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)
            boom.stress_max(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)

        self.boom_area(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)
        for boom in self.booms:
            boom.stress_boom(sigma_y, E, n_x, n_y, M_x, M_y, Ixx, Iyy, n)

    def skin_length(self, n):
        nodes = self.booms
        nodes.insert(0, nodes[-1])
        nodes.append(nodes[1])
        t_b = []

        for i in range(len(nodes) - 1):
            node, node1 = nodes[i], nodes[i + 1]
            b = sqrt((node.X[n] - node1.X[n]) ** 2 + (node.Y[n] - node1.Y[n]) ** 2)
            t_b.append(b)

        nodes.remove(nodes[0])
        nodes.remove(nodes[-1])

        return t_b




"""
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
