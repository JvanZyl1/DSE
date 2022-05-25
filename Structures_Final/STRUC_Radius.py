from STRUC_Inputs import *

"""
DSE: Structures
Beam Loading and Stresses
"""

# Imports

from STRUC_Inputs import *
from math import *
import numpy as np
from matplotlib import pyplot as plt


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


print(v_beam(use_beam, use_loadcase, 0))


def m_beam(beam, load, pos_z):
    M_ax = (beam.weight / 2 + beam.weight_engine / beam.n - load.L / beam.n) * beam.length
    Mx = (beam.weight + beam.weight_engine / beam.n - load.L / beam.n) * pos_z - \
         beam.weight * pos_z ** 2 / (2 * beam.length) - M_ax
    M_ay = beam.length * load.D * beam.radius * 2 * beam.length
    My = M_ay - M_ay * pos_z / beam.length + load.T
    return Mx, My, M_ax, M_ay


def deflection(beam, load, material, pos_z):
    _, _, M_ax, M_ay = m_beam(beam, load, pos_z)
    v = 1 / (material.E_modulus * beam.Ixx) * \
        (-M_ax / 2 * pos_z ** 2 + (-load.L/beam.n + beam.weight + beam.weight_engine/beam.n) / 6 * pos_z ** 3 -
         beam.weight / (24 * beam.length) * pos_z ** 4)
    return v


def radius(beam, load, material, pos_z):
    tensile_strength = material.sigma_t
    V_x, V_y = v_beam(beam, load, pos_z)
    M_x, M_y, _, _ = m_beam(beam, load, pos_z)

    # Bending in lift-direction for TENSION

    r1 = (use_loadcase.P + sqrt(abs((use_loadcase.P ** 2) + 4 * 2 * pi * beam.thickness * tensile_strength
                                    * 2 * pi * M_x))) / (4 * pi * beam.thickness * tensile_strength)

    # Bending in lift-direction for COMPRESSION
    r2 = (abs(M_x * beam.length ** 2) / (beam.thickness * pi ** 2 * material.E_modulus)) ** (1 / 4)

    # Bending in axial-direction for TENSION
    r3 = (abs(M_y) + sqrt(M_y ** 2 + 4 * 2 * pi * beam.thickness * tensile_strength * 2 * pi * load.P)) / \
         (4 * pi * beam.thickness * tensile_strength)

    # Bending in axial-direction for COMPRESSION
    r4 = (abs(M_y * beam.length ** 2) / (beam.thickness * pi ** 2 * material.E_modulus)) ** (1 / 4)

    # Shear in lift-direction
    r5 = (abs(V_x / (-pi * beam.thickness * material.tau))) ** (1 / 3)

    # Shear in axial-direction
    r6 = (abs(V_y / (-pi * beam.thickness * material.tau))) ** (1 / 3)

    # print(tensile_strength, buckling_strength)
    return r1, r2, r3, r4, r5, r6


for iteration in range(10):
    x_plt = []
    y_plt = []
    y_plt1 = []
    y_plt2 = []
    y_plt3 = []
    y_plt4 = []
    y_plt5 = []
    y_plt6 = []



    W = 0
    dt = 0.1
    for i in np.arange(0, use_beam.length + dt, dt):
        x_plt.append(i)
        y_plt.append(max(radius(use_beam, use_loadcase, use_material, i)))
        y_plt1.append((radius(use_beam, use_loadcase, use_material, i)[0]))
        y_plt2.append((radius(use_beam, use_loadcase, use_material, i)[1]))
        y_plt3.append((radius(use_beam, use_loadcase, use_material, i)[2]))
        y_plt4.append((radius(use_beam, use_loadcase, use_material, i)[3]))
        y_plt5.append((radius(use_beam, use_loadcase, use_material, i)[4]))
        y_plt6.append((radius(use_beam, use_loadcase, use_material, i)[5]))
        deflection(use_beam, use_loadcase, use_material, i)
        W += 2 * pi * max(radius(use_beam, use_loadcase, use_material, i)) * use_beam.thickness * use_material.density * dt
    use_beam.weight = W

print(use_beam.weight)
plt.plot(x_plt, y_plt)
plt.plot(x_plt, y_plt1)
plt.plot(x_plt, y_plt2)
plt.plot(x_plt, y_plt3)
plt.plot(x_plt, y_plt4)
plt.plot(x_plt, y_plt5)
plt.plot(x_plt, y_plt6)
plt.show()