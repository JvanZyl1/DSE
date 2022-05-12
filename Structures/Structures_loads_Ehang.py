"""
DSE: Structures
Beam Loading and Stresses (for Ehang concept)
"""

# Imports
from math import *
import numpy as np
from matplotlib import pyplot as plt
from Materials import *


# Material
mat = titanium


# Inputs
W_beam = 3.6   *9.81 # N
L = 8000  # N
W_engine = 52*9.81/4  # N

d = 2  # m
t = 0.5e-3  # m
r = 0.13  # m

Ixx = t * r ** 3  # m**4

# Functions
dx, dy, dz = 0.005, 0.005, 0.01
x = np.arange(-r, r, dx)
y = np.arange(-r, r, dy)
z = np.arange(0, d + dz, dz)


# Internal Load Function along z-axis
def v_beam(W_beam, W_engine, d, z, L):
    Vz = W_beam + W_engine - L / 4 - W_beam * z / d
    return Vz


# Moment Function along z-axis
def m_beam(W_beam, W_engine, d, z, L):
    M_a = (W_beam / 2 + W_engine - L / 4) * d
    Mz = (W_beam + W_engine - L / 4) * z - W_beam * z ** 2 / (2 * d) - M_a
    return Mz


# Bending stress along x- and z-axis 25% SF-MARGIN INCLUDED
def stress_beam(W_beam, W_engine, d, z, L, x, Ixx):
    sigma_x = 1.25*np.transpose([(m_beam(W_beam, W_engine, d, z, L) / Ixx)]) * [x]
    return sigma_x


# Shear stress
def shear_beam(W_beam, W_engine, d, z, L, x, t, r):
    Vz = v_beam(W_beam, W_engine, d, z, L)
    tau = np.transpose([Vz])/(-pi * t * r**4) * [x]
    return tau


def weight_beam(mat, t, r, d):
    W = mat.weight * 2 * pi * t * r * d
    return W


# Functions
Vz = v_beam(W_beam, W_engine, d, z, L)
Mz = m_beam(W_beam, W_engine, d, z, L)
sigma_x = stress_beam(W_beam, W_engine, d, z, L, x, Ixx)
tau = shear_beam(W_beam, W_engine, d, z, L, x, t, r)
W = weight_beam(mat, t, r, d)



"""
# Matplotlib
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
fig.suptitle("Stress in cross-section of beam")
ax1.plot(sigma_x[0], x)
ax1.plot(np.ones(np.size(x))*mat.sigma_t, x, 'r')
ax1.plot(-np.ones(np.size(x))*mat.sigma_t, x, 'r')
ax1.set_title("Bending stress")
ax1.set(xlabel = r'$\sigma_x$ [Pa]', ylabel = "x [m]")
ax2.plot(tau[0], x)
ax2.plot(np.ones(np.size(x))*mat.tau, x, 'r')
ax2.plot(-np.ones(np.size(x))*mat.tau, x, 'r')
ax2.set_title("Shear stress")
ax2.set(xlabel = r'$/tau$ [Pa]')
plt.show()
"""