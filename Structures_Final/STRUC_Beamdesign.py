from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses
"""

# Imports

from STRUC_Inputs import *
from math import *
import numpy as np


def axes(beam):
    dx, dy, dz = 0.005, 0.005, 0.01
    z_ax = np.arange(0, beam.length + dz, dz)  # Beam span Direction
    x_ax = np.arange(-beam.radius, beam.radius, dx)  # Vertical Direction
    y_ax = np.arange(-beam.radius, beam.radius, dy)
    return x_ax, y_ax, z_ax

x, y, z = axes(use_beam)


# Internal Load Function along z-axis
def v_beam(beam, load, pos_z):
    Vy = beam.weight + beam.weight_engine - load.L / n - beam.weight * pos_z / beam.length
    Vx = -load.D
    return Vx, Vy

def m_beam(beam, load, pos_z):
    M_ax = (beam.weight / 2 + beam.weight_engine - load.L / n) * beam.length
    Mx = (beam.weight + beam.weight_engine - load.L / n) * pos_z - beam.weight * pos_z ** 2 / (2 * beam.length) - M_ax
    M_ay = beam.length * load.D*beam.radius * 2 * beam.length
    My = M_ay - M_ay * pos_z/beam.length + load.T
    return Mx, My


# Bending stress along x- and z-axis
def stress_beam(beam, load, pos_z):
    x, y, z = axes(beam)
    sigma_L_z = load.P / (2 * pi * beam.radius * beam.thickness)
    sigma_bend_y = (m_beam(beam, load, pos_z)[1] / beam.Ixx) * y
    sigma_bend_x = (m_beam(beam, load, pos_z)[0] / beam.Iyy) * x
    sigma_z_y_max = np.max(np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y))))
    sigma_z_y_min = np.min(np.add(sigma_bend_y, sigma_L_z * np.ones(np.shape(sigma_bend_y))))
    sigma_z_x_max = np.max(np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x))))
    sigma_z_x_min = np.min(np.add(sigma_bend_x, sigma_L_z * np.ones(np.shape(sigma_bend_x))))
    return max(sigma_z_x_max, sigma_z_y_max), min(sigma_z_x_min, sigma_z_y_min)

def sigma_buckling(beam, material):
    sigma_b = -(pi**2 * material.E_modulus / (beam.K * beam.length / beam.radius)**2 + 1.2 * pi **2 * (material.E_modulus/material.G_modulus))
    return sigma_b

for i in np.arange(0, 2.41, 0.1):
    stress_t, stress_c = stress_beam(use_beam, use_loadcase, i)
    if use_material.sigma_t /1.25 > stress_t and sigma_buckling(use_beam, use_material)/1.25 < stress_c :
        print("OK", "OK")
    elif use_material.sigma_t /1.25 > stress_t and sigma_buckling(use_beam, use_material)/1.25 >= stress_c :
        print("OK", "not OK")
    elif use_material.sigma_t /1.25 <= stress_t and sigma_buckling(use_beam, use_material)/1.25 < stress_c :
        print("not OK", "OK")
    else:
        print("not OK", "not OK")

"""

def shear_beam(beam, load):
    x, y, z = axes(beam)
    Vx = v_beam(beam, load)[0]
    Vy = v_beam(beam, load)[1]
    shear_x = np.transpose([Vx]) / (-pi * beam.thickness * beam.radius ** 4) * [y]
    shear_y = np.transpose([Vy]) / (-pi * beam.thickness * beam.radius ** 4) * [x]
    return shear_x, shear_y

# Failure Modes - Tensile Strength


# Failure Modus - Buckling
def sigma_buckling(beam, material):
    sigma_b = pi**2 * material.E_modulus / (beam.K * beam.length / beam.radius)**2 + 1.2 * pi **2 * (material.E_modulus/material.G_modulus)
    return sigma_b
"""
