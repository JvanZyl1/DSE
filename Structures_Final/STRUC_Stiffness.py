from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses (for Ehang concept)
"""

# Imports
from math import *
import numpy as np
from matplotlib import pyplot as plt
from STRUC_Classes import Lift, Material
from STRUC_Design import Beam
from STRUC_Inputs import *

use_beam = beam2
use_material = aluminium
use_liftcase = Gust
SF = 1.25

def axes(beam):
    dx, dy, dz = 0.005, 0.005, 0.01
    z = np.arange(0, beam.length + dz, dz)  # Beam span Direction
    x = np.arange(-beam.radius, beam.radius, dx)  # Vertical Direction
    y = np.arange(-beam.radius, beam.radius, dy)
    return x, y, z


# Internal Load Function along z-axis
def v_beam(beam, lift):
    _, _, z = axes(beam)
    Vx = beam.weight + beam.weight_engine - lift.L_x / n - beam.weight * z / beam.length
    return Vx


# Moment Function along z-axis
def m_beam(beam, lift):
    x, _, z = axes(beam)
    M_a = (beam.weight / 2 + beam.weight_engine - lift.L_x / n) * beam.length
    Mz = (beam.weight + beam.weight_engine - lift.L_x / n) * z - beam.weight * z ** 2 / (2 * beam.length) - M_a
    return Mz


# Bending stress along x- and z-axis
def stress_beam(beam, lift):
    x, _, z = axes(beam)
    sigma_x_L_z = lift.L_z / (2 * pi * beam.radius * beam.thickness)
    sigma_x_bend = np.transpose([(m_beam(beam, lift) / beam.Ixx)]) * [x]
    sigma_x = np.add(sigma_x_bend, sigma_x_L_z * np.ones(np.shape(sigma_x_bend)))
    print(sigma_x_L_z)
    print(sigma_x[0])
    return sigma_x


def shear_beam(beam, lift):
    x, _, z = axes(beam)
    Vz = v_beam(beam, lift)
    shear = np.transpose([Vz]) / (-pi * beam.thickness * beam.radius ** 4) * [x]
    return shear




def weight_beam(material, beam):
    W = material.density * 2 * pi * beam.thickness * beam.radius * beam.length
    return W


print(weight_beam(use_material, use_beam))

x, y, z = axes(use_beam)


# Matplotlib
fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
plt.gcf().subplots_adjust(left=0.15)
ax1.plot(z, v_beam(use_beam, use_liftcase))
ax1.set_ylim(np.min(v_beam(use_beam, use_liftcase)), 0)
ax1.set_title("Internal Load diagram")
ax1.set(ylabel = r'$\bar{V}$ [N]')
ax1.grid(True)
ax1.axhline(0, color='black', lw=1.2)
ax2.plot(z, m_beam(use_beam, use_liftcase))
ax2.set_title("Bending Moment diagram")
ax2.set(xlabel = r'$z$ [m]', ylabel = r'$\bar{M}$ [N/m]')
ax2.grid(True)
ax2.axhline(0, color='black', lw=1.2)
fig1.savefig("Loading_diagrams")


fig2, (ax3, ax4) = plt.subplots(1, 2, sharey=True)
ax3.plot(stress_beam(use_beam, use_liftcase)[0], x)
ax3.plot(np.ones(np.size(x))*use_material.sigma_t, x, '-.r')
ax3.plot(-np.ones(np.size(x))*use_material.sigma_t, x, '-.r', label='line1')
ax3.set_title("Bending stress")
ax3.set(xlabel = r'$\bar{\sigma}_x$ [Pa]', ylabel = "x [m]")
ax3.grid(True)
ax3.axhline(0, color='black', lw=1.2)
ax4.plot(shear_beam(use_beam, use_liftcase)[0], x)
ax4.plot(np.ones(np.size(x))*use_material.tau/1.25, x, '-.r')
ax4.plot(-np.ones(np.size(x))*use_material.tau/1.25, x, '-.r')
ax4.set_title("Shear stress")
ax4.set(xlabel = r'$\bar{\tau}$ [Pa]')
ax4.grid(True)
ax4.axhline(0, color='black', lw=1.2)
fig2.savefig("Stress_diagrams")
plt.show()