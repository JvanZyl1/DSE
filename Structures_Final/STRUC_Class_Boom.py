# Define Boom
from matplotlib import pyplot as plt
from math import *
import numpy as np
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
        return [self.B[0] * (self.Y[0]-n_y[0]) ** 2, self.B[1] * (self.Y[1]-float(n_y[1])) ** 2]

    def Iyy(self, n_x):
        return [self.B[0] * (self.X[0]-n_x[0]) ** 2, self.B[1] * (self.X[1]-n_x[1]) ** 2]

    def stress_z(self, n_x, n_y, M_x, M_y, Ixxcs, Iyycs):
        self.sigma_z = [M_x[0] * (self.Y[0]-n_y[0]) / Ixxcs[0] + M_y[0] * (self.X[0]-n_x[0]) / Ixxcs[0],
                        M_x[1] * (self.Y[1]-n_y[1]) / Ixxcs[1] + M_y[1] * (self.X[1]-n_x[0]) / Iyycs[1]]
        return self.sigma_z