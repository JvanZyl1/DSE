from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses (for Ehang concept)
"""

# Imports
from math import *
import numpy as np
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
    sigma_bend_y = np.transpose([(m_beam(beam, load)[1] / beam.Ixx)]) * [y]
    sigma_bend_x = np.transpose([(m_beam(beam,load)[0]) / beam.Iyy]) * [x]
    sigma_z_y = np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y)))
    sigma_z_x = np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x)))
    return sigma_z_x, sigma_z_y


def shear_beam(beam, load):
    x, y, z = axes(beam)
    Vx = v_beam(beam, load)[0]
    Vy = v_beam(beam, load)[1]
    shear_x = np.transpose([Vx]) / (-pi * beam.thickness * beam.radius ** 4) * [y]
    shear_y = np.transpose([Vy]) / (-pi * beam.thickness * beam.radius ** 4) * [x]
    return shear_x, shear_y


def weight_beam(material, beam):
    W = material.density * 2 * pi * beam.thickness * beam.radius * beam.length
    return W


print(weight_beam(use_material, use_beam))




