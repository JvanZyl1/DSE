# Define Boom
from matplotlib import pyplot as plt
from math import *
from STRUC_Inputs import *
import numpy as np


class Boom:
    sigma_y = 400e6
    E = 70e9
    K = 2

    def __init__(self, pos_x, pos_y, A, t):
        self.X = pos_x
        self.Y = pos_y
        self.A = np.array([A, A])
        self.B = np.array([A, A])
        self.t = t
        self.sigma_z = [0, 0]
        self.shear_z = [0, 0]
        self.stress_max = [0, 0]

    def properties_cs(self, radius, length):
        self.R = radius
        self.L = length

    def plot(self):
        plt.plot(self.X, self.Y, '--')
        plt.scatter(self.X, self.Y)

    def area(self, new_B):
        self.B = new_B

    def Ixx(self, n_y):
        return [self.B[0] * (self.Y[0]-n_y[0]) ** 2, self.B[1] * (self.Y[1]-n_y[1]) ** 2]

    def Iyy(self, n_x):
        return [self.B[0] * (self.X[0]-n_x[0]) ** 2, self.B[1] * (self.X[1]-n_x[1]) ** 2]

    def stress_z(self, n_x, n_y, M_x, M_y, I_xx_cs, I_yy_cs):
        if M_x[0] * (self.Y[0] - n_y[0]) + M_y[0] * (self.X[0] - n_x[0]) >= 0:
            print(self.sigma_y)
            self.stress_max[0] = Boom.sigma_y
        else:
            self.stress_max[0] = max(-Boom.sigma_y, -pi ** 2 * Boom.E * self.r ** 2 / (Boom.K * self.L) ** 2)

        if M_x[1] * (self.Y[1] - n_y[1]) + M_y[1] * (self.X[1] - n_x[1]) >= 0:
            self.stress_max[1] = Boom.sigma_y
        else:
            self.stress_max[1] = max(-Boom.sigma_y, -pi ** 2 * Boom.E * self.r ** 2 / (Boom.K * self.L) ** 2)



        self.sigma_z = [M_x[0] * (self.Y[0]-n_y[0]) / I_xx_cs[0] + M_y[0] * (self.X[0]-n_x[0]) / I_xx_cs[0],
                        M_x[1] * (self.Y[1]-n_y[1]) / I_xx_cs[1] + M_y[1] * (self.X[1]-n_x[0]) / I_yy_cs[1]]
        return self.sigma_z

    def shear(self, Ixxcs, Iyycs):

        """
        Vx, Vy = 1, 1
        self.shear_z = -"""
        pass

