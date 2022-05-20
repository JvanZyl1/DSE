from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses (for Ehang concept)
"""

# Imports
from math import *
import numpy as np
from matplotlib import pyplot as plt
from STRUC_Inputs import *

# Input choices
use_beam = beam2
use_material = aluminium
use_loadcase = Gust


def axes(beam):
    dx, dy, dz = 0.005, 0.005, 0.01
    z = np.arange(0, beam.length + dz, dz)  # Beam span Direction
    x = np.arange(-beam.radius, beam.radius, dx)  # Vertical Direction
    y = np.arange(-beam.radius, beam.radius, dy)
    return x, y, z


# Internal Load Function along z-axis
def v_beam(beam, load):
    x, y, z = axes(beam)
    Vy = beam.weight + beam.weight_engine - load.L / n - beam.weight * z / beam.length
    Vx = -load.D*np.ones(np.shape(z))
    return Vx, Vy


# Moment Function along z-axis
def m_beam(beam, load):
    x, y, z = axes(beam)
    M_ax = (beam.weight / 2 + beam.weight_engine - load.L / n) * beam.length
    Mx = (beam.weight + beam.weight_engine - load.L / n) * z - beam.weight * z ** 2 / (2 * beam.length) - M_ax
    M_ay = beam.length * load.D*beam.radius * 2 * beam.length
    My = M_ay - M_ay * z/beam.length + load.T
    return Mx, My


# Bending stress along x- and z-axis
def stress_beam(beam, load):
    x, y, z = axes(beam)
    sigma_L_z = load.P / (2 * pi * beam.radius * beam.thickness)
    sigma_bend_y = np.transpose([(m_beam(beam, load)[1] / beam.Ixx)]) * [x]
    sigma_bend_x = np.transpose([(m_beam(beam,load)[0]) / beam.Iyy]) * [y]
    sigma_z_y = np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y)))
    sigma_z_x = np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x)))
    return sigma_z_x, sigma_z_y


def shear_beam(beam, load):
    x, y, z = axes(beam)
    Vz = v_beam(beam, load)[0]
    shear = np.transpose([Vz]) / (-pi * beam.thickness * beam.radius ** 4) * [y]
    return shear


def weight_beam(material, beam):
    W = material.density * 2 * pi * beam.thickness * beam.radius * beam.length
    return W


print(weight_beam(use_material, use_beam))

x, y, z = axes(use_beam)

V_x, V_y = v_beam(use_beam, use_loadcase)
M_x, M_y = m_beam(use_beam, use_loadcase)
sigma_zx, sigma_zy = stress_beam(use_beam, use_loadcase)
use_V = V_x
use_M = M_y
use_sigma_z = sigma_zx


# Matplotlib
fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
plt.gcf().subplots_adjust(left=0.15)
ax1.plot(z, use_V)
ax1.set_ylim(np.min(use_V), 0)
ax1.set_title("Internal Load diagram")
ax1.set(ylabel=r'$\bar{V}$ [N]')
ax1.grid(True)
ax1.axhline(0, color='black', lw=1.2)
ax2.plot(z, use_M)
ax2.set_title("Bending Moment diagram")
ax2.set(xlabel=r'$z$ [m]', ylabel=r'$\bar{M}$ [N/m]')
ax2.grid(True)
ax2.axhline(0, color='black', lw=1.2)
fig1.savefig("Loading_diagrams")

fig2, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
ax3.plot(use_sigma_z[0], x)
ax3.plot(np.ones(np.size(x)) * use_material.sigma_t, x, '-.r')
ax3.plot(-np.ones(np.size(x)) * use_material.sigma_t, x, '-.r', label='line1')
ax3.set_title("Bending stress")
ax3.set(xlabel=r'$\bar{\sigma}_x$ [Pa]', ylabel="x [m]")
ax3.grid(True)
ax3.axhline(0, color='black', lw=1.2)
ax4.plot(shear_beam(use_beam, use_loadcase)[0], x)
ax4.plot(np.ones(np.size(x)) * use_material.tau / 1.25, x, '-.r')
ax4.plot(-np.ones(np.size(x)) * use_material.tau / 1.25, x, '-.r')
ax4.set_title("Shear stress")
ax4.set(xlabel=r'$\bar{\tau}$ [Pa]')
ax4.grid(True)
ax4.axhline(0, color='black', lw=1.2)
fig2.savefig("Stress_diagrams")
plt.show()
