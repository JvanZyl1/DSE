"""
DSE: Structures
Beam Loading and Stresses (for Ehang concept)
"""

# Imports
from math import *
import numpy as np
from matplotlib import pyplot as plt
from Structures_Classes import *


# Material
mat = aluminium
W_beam = 3.6 * 9.81  # N
L = 8000  # N
W_engine = 52 * 9.81 / 4  # N

d = 2  # m
t = 0.5e-3  # m
r = 0.13  # m

Ixx = t * r ** 3  # m**4


#W_beam = 0.001 # Initial Value



# Internal Load Function along z-axis
def v_beam(Beam, W_engine, Axes, L):
    Vz = Beam.weight + W_engine - L / 4 - W_beam * Axes.z / Beam.length
    return Vz


# Moment Function along z-axis
def m_beam(W_beam, W_engine, d, Axes, L):
    M_a = (W_beam / 2 + W_engine - L / 4) * d
    Mz = (W_beam + W_engine - L / 4) * Axes.z - W_beam * Axes.z ** 2 / (2 * d) - M_a
    return Mz

# Bending stress along x- and z-axis
def stress_beam(W_beam, W_engine, d, Axes, L, Ixx):
    sigma_x = np.transpose([(m_beam(W_beam, W_engine, d, Axes.z, L) / Ixx)]) * [Axes.x]
    return sigma_x


# Shear stress
def shear_beam(W_beam, W_engine, d, Axes, L, t, r):
    Vz = v_beam(W_beam, W_engine, d, Axes, L)
    tau = np.transpose([Vz])/(-pi * t * r**4) * [Axes.x]
    return tau


def weight_beam(mat, t, r, d):
    W = mat.density * 2 * pi * t * r * d
    return W


def deflections():
    pass


# Functions
Vz = v_beam(beam1, W_engine, Axes, L)
Mz = m_beam(W_beam, W_engine, d, Axes, L)
sigma_x = stress_beam(W_beam, W_engine, d, Axes, L, Ixx)
tau = shear_beam(W_beam, W_engine, d, Axes, L, t, r)
W = weight_beam(mat, t, r, d)



# Matplotlib

fig1, (ax3, ax4) = plt.subplots(2, 1, sharex=True)
plt.gcf().subplots_adjust(left=0.15)
ax3.plot(z, Vz)
ax3.set_ylim(np.min(Vz), 0)
ax3.set_title("Internal Load diagram")
ax3.set(ylabel = r'$\bar{V}$ [N]')
ax3.grid(True)
ax3.axhline(0, color='black', lw=1.2)
ax4.plot(z, Mz)
ax4.set_title("Bending Moment diagram")
ax4.set(xlabel = r'$z$ [m]', ylabel = r'$\bar{M}$ [N/m]')
ax4.grid(True)
ax4.axhline(0, color='black', lw=1.2)
fig1.savefig("Loading_diagrams")


fig2, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(sigma_x[0], Axes.x)
ax1.plot(np.ones(np.size(Axes.x))*mat.sigma_t, x, '-.r')
ax1.plot(-np.ones(np.size(Axes.x))*mat.sigma_t, x, '-.r', label='line1')
ax1.set_title("Bending stress")
ax1.set(xlabel = r'$\bar{\sigma}_x$ [Pa]', ylabel = "x [m]")
ax1.grid(True)
ax1.axhline(0, color='black', lw=1.2)
ax2.plot(tau[0], Axes.x)
ax2.plot(np.ones(np.size(x))*mat.tau, Axes.x, '-.r')
ax2.plot(-np.ones(np.size(x))*mat.tau, Axes.x, '-.r')
ax2.set_title("Shear stress")
ax2.set(xlabel = r'$\bar{\tau}$ [Pa]')
ax2.grid(True)
ax2.axhline(0, color='black', lw=1.2)
fig2.savefig("Stress_diagrams")
