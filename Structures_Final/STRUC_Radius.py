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
    Vy = beam.weight + beam.weight_engine / beam.n - load.L / beam.n - beam.weight * pos_z / beam.length
    Vx = -load.D
    return Vx, Vy


def m_beam(beam, load, pos_z):
    M_ax = (beam.weight / 2 + beam.weight_engine / beam.n - load.L / beam.n) * beam.length
    Mx = (beam.weight + beam.weight_engine / beam.n - load.L / beam.n) * pos_z - \
         beam.weight * pos_z ** 2 / (2 * beam.length) - M_ax
    M_ay = beam.length * load.D * beam.radius * 2 * beam.length
    My = M_ay - M_ay * pos_z / beam.length + load.T
    return Mx, My


def stress(beam, load, material, pos_z):
    tensile_strength = material.sigma_t
    # buckling_strength = -(pi ** 2 * material.E_modulus / (beam.K * beam.length / beam.radius) ** 2 + 1.2 * pi ** 2 * (
    #        material.E_modulus / material.G_modulus))
    V_x, V_y = v_beam(beam, load, pos_z)
    M_x, M_y = m_beam(beam, load, pos_z)
    print("M_x = ", M_x)
    print("M_y = ", M_y)
    # Bending in lift-direction for TENSION
    r1 = (abs(M_x) + sqrt(M_x ** 2 + 4 * 2 * pi * beam.thickness * tensile_strength * 2 * pi * load.P)) / \
         (4 * pi * beam.thickness * tensile_strength)

    # Bending in lift-direction for COMPRESSION
    r2 = (abs(M_x * beam.length ** 2)/ (beam.thickness * pi ** 2 * material.E_modulus))**(1/4)

    # Bending in axial-direction for TENSION
    r3 = (abs(M_y) + sqrt(M_y ** 2 + 4 * 2 * pi * beam.thickness * tensile_strength * 2 * pi * load.P)) / \
         (4 * pi * beam.thickness * tensile_strength)

    # Bending in axial-direction for COMPRESSION
    r4 = (abs(M_y * beam.length ** 2)/ (beam.thickness * pi ** 2 * material.E_modulus))**(1/4)

    # Shear in lift-direction
    r5 = (abs(V_x / (-pi * beam.thickness * material.tau))) ** (1/3)

    # Shear in axial-direction
    r6 = (abs(V_y / (-pi * beam.thickness * material.tau))) ** (1/3)




    # print(tensile_strength, buckling_strength)
    print(max(r1, r2, r3, r4, r5, r6))


for i in np.arange(0, use_beam.length + 0.1, 0.1):
    # print(m_beam(use_beam, use_loadcase, i))
    stress(use_beam, use_loadcase, use_material, i)

