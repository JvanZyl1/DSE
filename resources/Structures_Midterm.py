"""
Hello
"""

from math import *
import numpy as np
from matplotlib import pyplot as plt

W_beam = 200  # N
L = 0  # N
W_engine = 1000  # N

d = 2  # m
t = 0.001  # m
r = 0.1  # m

Ixx = t * r ** 3  # m**4

# Functions
dx, dz = 0.005, 0.01
x = np.arange(-r, r, dx)
z = np.arange(0, d + dz, dz)


def v_beam(W_beam, W_engine, d, z, L):
    Vz = W_beam + W_engine - L / 4 - W_beam * z / d
    return Vz
Vz = v_beam(W_beam, W_engine, d, z, L)

def m_beam(W_beam, W_engine, d, z, L):
    M_a = (W_beam / 2 + W_engine - L / 4) * d
    Mz = (W_beam + W_engine - L / 4) * z - W_beam * z ** 2 / (2 * d) - M_a
    return Mz
Mz = m_beam(W_beam, W_engine, d, z, L)


def stress_beam(W_beam, W_engine, d, z, L, x, Ixx):
    sigma_x = np.transpose([(m_beam(W_beam, W_engine, d, z, L) / Ixx)]) * [x]
    return sigma_x

sigma_x = stress_beam(W_beam, W_engine, d, z, L, x, Ixx)

plt.plot(sigma_x[200], x)
plt.show()

