# Define Boom
from matplotlib import pyplot as plt
from math import *
from STRUC_Inputs import *
import numpy as np


class Boom:
    K = 2
    g = 9.81
    density = 2.8e3 * g
    tau_cr = [283e6, 283e6]
    sigma_y = 400e6
    E = 70e9
    dz = 0.01
    MTOW = 950
    n_ult = 2
    SF = 1.5

    def __init__(self, pos_x, pos_y, B, t):
        self.N_B = None
        self.W_skinb = None
        self.X = pos_x
        self.Y = pos_y
        self.A = np.array([None, None])
        self.B = np.array([B, B])
        self.t = t
        self.sigma_z = [0, 0]
        self.shear_z = [0, 0]
        self.sigma_cr = [0, 0]
        self.q_y = [0, 0]
        self.q_x = [0, 0]
        self.q = [0, 0]
        self.tau = [0, 0]
        # print('1 -->', self.__dict__)

    def properties_cs(self, radius, length):
        self.R = radius
        self.L = length
        self.X = self.X * 1.341 / 1.103
        # print('2 -->', self.__dict__)


    def plot_b(self):
        plt.plot(self.X, self.Y, '--g')
        plt.scatter(self.X, self.Y, s=self.B[0] * 300000, c='g')

    # Try to delete this
    def area(self, i, new_B):
        self.B[i] = new_B
        # print("Area updated", new_B)

    def Ixx(self, n_y):  # Checked
        return [self.B[0] * (self.Y[0] - n_y[0]) ** 2, self.B[1] * (self.Y[1] - n_y[1]) ** 2]

    def Iyy(self, n_x):  # Checked
        return [self.B[0] * (self.X[0] - n_x[0]) ** 2, self.B[1] * (self.X[1] - n_x[1]) ** 2]

    def stress_boom(self, sigma_y, E, n_x, n_y, M_x, M_y, I_xx_cs, I_yy_cs, n):
        self.sigma_z[n] = M_x * (self.Y[n] - n_y) / I_xx_cs + M_y * (self.X[n] - n_x) / I_yy_cs
        if self.sigma_z[n] >= 0:
            self.sigma_cr[n] = sigma_y
        else:
            self.sigma_cr[n] = -pi * E * self.B[n] / (Boom.K * self.L) ** 2
        return self.sigma_z[n]

    def shear_boom(self, n_x, n_y, V_x, V_y, Ixx, Iyy, n):
        self.dq_x = -V_x / Iyy * self.B * (self.X - n_x)
        self.dq_y = -V_y / Ixx * self.B * (self.Y - n_y)
        return self.dq_x, self.dq_y

    def weight_boom(self):  # Checked
        self.L_boom = sqrt((self.X[1] - self.X[0]) ** 2 + (self.Y[1] - self.Y[0]) ** 2 + self.L ** 2)
        self.V_boom = (self.A[1] + self.A[0]) / 2 * self.L_boom
        self.W_boom = self.V_boom * Boom.density
        return self.W_boom
