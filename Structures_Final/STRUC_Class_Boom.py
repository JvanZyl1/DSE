# Define Boom
from matplotlib import pyplot as plt
from math import *
from STRUC_Inputs import *
import numpy as np



class Boom:
    K = 2
    density = 2.8e3
    def __init__(self, pos_x, pos_y, A, t):
        self.x = pos_x
        self.y = pos_y
        self.A = np.array([A, A])
        self.B = np.array([A, A])
        self.t = t
        self.sigma_z = [0, 0]
        self.shear_z = [0, 0]
        self.sigma_max = [0, 0]

    def properties_cs(self, radius, length):
        self.R = radius
        self.L = length
        self.X = self.x * radius
        self.Y = self.y * radius

    def weight(self):
        self.L_boom = sqrt((self.X[1]-self.X[0])**2 + (self.Y[1]-self.Y[0])**2 + self.L**2)
        self.V_boom = (self.A[1]+self.A[0]) / 2 * self.L_boom
        self.W_boom = self.V_boom * Boom.density
        return self.W_boom

    def plot_b(self):
        plt.plot(self.X, self.Y, '--')
        plt.scatter(self.X, self.Y)

    def area(self, n, new_B):
        self.B[n] = new_B

    def Ixx(self, n_y):
        return [self.B[0] * (self.Y[0]-n_y[0]) ** 2, self.B[1] * (self.Y[1]-n_y[1]) ** 2]

    def Iyy(self, n_x):
        return [self.B[0] * (self.X[0]-n_x[0]) ** 2, self.B[1] * (self.X[1]-n_x[1]) ** 2]

    def stress_max(self, sigma_y, E, n_x, n_y, M_x, M_y, I_xx_cs, I_yy_cs, n):
        self.sigma_z[n] = M_x * (self.Y[n]-n_y) / I_xx_cs + M_y * (self.X[n]-n_x) / I_yy_cs

        if self.sigma_z[n] >= 0:
            self.sigma_max[n] = sigma_y
        else:
            self.sigma_max[n] = max(-sigma_y, -pi ** 2 * E * (self.B[n]/pi)/ (Boom.K * self.L) ** 2)
        return self.sigma_max[n]

    def stress_boom(self, sigma_y, E, n_x, n_y, M_x, M_y, I_xx_cs, I_yy_cs, n):

        self.sigma_z[n] = M_x * (self.Y[n]-n_y) / I_xx_cs + M_y * (self.X[n]-n_x) / I_yy_cs
        return self.sigma_z[n]

    def shear_boom(self, n_x, n_y, V_x, V_y, Ixx, Iyy, n):
        self.dq_x = -V_x / Iyy * self.B * (self.X-n_x)
        self.dq_y = -V_y / Ixx * self.B * (self.Y-n_y)
        if round(self.X[0], 4) == 0 and round(self.Y[0], 4) > 0:
            pass
        if round(self.X[0], 4) > 0 and round(self.Y[0], 4) == 0:
            print(self)
        return self.dq_x, self.dq_y


