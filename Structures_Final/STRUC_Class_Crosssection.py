from STRUC_Class_Boom import Boom
from matplotlib import pyplot as plt
from math import *
import numpy as np
from STRUC_Inputs import *


# Define Cross-Section
class CrossSection(Boom):


    def __init__(self, pos_z, radius, pos_x=None, pos_y=None, A=None, booms=None, t=None):
        self.Z = pos_z  # np.array([z1, z2]) [m]
        self.R = np.array(radius)  # np.array([r1, r2]) [m]
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
                self.L = self.Z[1]-self.Z[0]
                boom.properties_cs(self.R, self.L)

    def weight_booms(self):
        self.W_cs_booms = 0
        for boom in self.booms:
            self.W_cs_booms += boom.weight()
        return self.W_cs_booms

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
            boom.plot_b()
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

    def shear_CS(self, V_x, V_y, n):
        n_x, n_y = self.neutral_x()[n], self.neutral_y()[n]
        Ixx, Iyy = self.Ixx_cs()[n], self.Iyy_cs()[n]
        X_tab, Y_tab = [], []
        for boom in self.booms:
            boom.shear_boom(n_x, n_y, V_x, V_y, Ixx, Iyy, n)
            X_tab.append(boom.X[0])
            Y_tab.append(boom.Y[0])
        X_max, Y_max = max(X_tab), max(Y_tab)

        q_x, q_y = None, None
        index_x, index_y = None, None
        for boom in self.booms:
            if round(boom.Y[0], 4) == 0 and round(boom.X[0], 4) > 0:
                boom.q_x = boom.dq_x / 2
                q_x = boom.q_x
                index_x = self.booms.index(boom)
                print('x, y=0', index_x)
            elif round(boom.Y[0], 4) > 0 and round(boom.X[0], 4) == 0:
                boom.q_y = boom.dq_y / 2
                q_y = boom.q_y
                index_y = self.booms.index(boom)
                print('y, x=0', index_y)
            elif round(boom.Y[0], 4) == round(Y_max, 4) and round(boom.X[0], 4) > 0:
                boom.q_y = boom.dq_y
                q_y = boom.q_y
                index_y = self.booms.index(boom)
                print('y', index_y)
            elif round(boom.X[0], 4) == round(X_max, 4) and round(boom.Y[0], 4) > 0:
                boom.q_x = boom.dq_x
                q_x = boom.q_x
                index_x = self.booms.index(boom)
                print('x', index_x)


        for boom in (self.booms[index_x+1:] + self.booms[:index_x]):
            q_x += boom.dq_x
            boom.q_x = q_x

        for boom in (self.booms[index_y+1:] + self.booms[:index_y]):
            q_y += boom.dq_y
            boom.q_y = q_y

        for boom in self.booms:
            boom.q = boom.q_x + boom.q_y
            if boom.t != 0:
                boom.tau = boom.q / boom.t
            else:
                boom.tau = 0

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

    def weight_skins(self):
        t_b1 = self.skin_length(0)
        t_b2 = self.skin_length(1)

        self.W_cs_skins = 0
        for i in range(len(t_b1)-1):
            self.W_cs_skins += (t_b1[i] + t_b2[i] / 2 * self.booms[i].t * self.L) * Boom.density
        return self.W_cs_skins


