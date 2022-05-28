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


# Internal Load Function along z-axis
def radii(part, load, material):
    # Shorter parameters:
    t = part.thickness
    l = part.length
    W = part.weight
    We = part.weight_engine
    L = load.L
    n = part.n
    E = material.E_modulus
    P = load.P
    tau = material.tau
    sigma_y = material.sigma_t

    # z-axis
    dz = 0.01
    z = np.arange(0, part.length + dz, dz)

    def v_x(pos_z):
        Vx = -load.D
        return Vx

    def v_y(pos_z):
        Vy = W + We / n - L / n - W * pos_z / l
        return Vy

    def m_x(pos_z):
        M_ax = (W / 2 + We / n - L / n) * l
        Mx = (W + We / n - L / n) * pos_z - \
             W * pos_z ** 2 / (2 * l) - M_ax
        return Mx

    def m_y(pos_z):
        M_ay = l * load.D * part.radius * 2 * L #RADIUS IS HERE!!!!!! REITERATE
        My = M_ay - M_ay * pos_z / l + load.T
        return My
    """
    #Radius should be input from radius function
    def deflection_y(load_y, moment_x, pos_z):
        v = 1 / (E * part.Ixx) * (moment_x / -2 * pos_z ** 2 + load_y / 6 * pos_z ** 3 - W / (24 * L) * pos_z ** 4)
        return v


    """

    def radii(Vx, Vy, Mx, My):

        # Bending in lift-direction for TENSION
        def r1():
            r1 = (P + sqrt(abs((P ** 2) + 4 * 2 * pi * t * sigma_y * 2 * pi * Mx))) / (4 * pi * t * sigma_y)
            return r1

        # Bending in lift-direction for COMPRESSION
        def r2():
            r2 = (abs(Mx * l ** 2) / (t * pi ** 2 * E)) ** (1 / 4)
            return r2

        # Bending in axial-direction for TENSION
        def r3():
            r3 = (abs(My) + sqrt(My ** 2 + 4 * 2 * pi * t * sigma_y * 2 * pi * P)) / (4 * pi * t * sigma_y)
            return r3

        # Bending in axial-direction for COMPRESSION
        def r4():
            r4 = (abs(My * l ** 2) / (t * pi ** 2 * E)) ** (1 / 4)
            return r4

        # Shear in lift-direction
        def r5():
            r5 = (abs(Vx / (-pi * t * tau))) ** (1 / 3)
            return r5

        # Shear in axial-direction
        def r6():
            r6 = (abs(Vy / (-pi * t * tau))) ** (1 / 3)
            return r6

        return r1(), r2(), r3(), r4(), r5(), r6()

    r = np.zeros((6, np.size(z)))
    for i in range(6):
        for j in range(np.size(z)):
            r[i, j] = radii(v_x(z[j]), v_y(z[j]), m_x(z[j]), m_y(z[j]))[i]
    return r


print(radii(use_beam, use_loadcase, use_material))
"""
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
        r = radius(use_beam, use_loadcase, use_material, i)
        x_plt.append(i)
        y_plt.append(max(r))
        y_plt1.append((r[0]))
        y_plt2.append((r[1]))
        y_plt3.append((r[2]))
        y_plt4.append((r[3]))
        y_plt5.append((r[4]))
        y_plt6.append((r[5]))
        deflection(use_beam, use_loadcase, use_material, i)
        W += 2 * pi * max(r) * use_beam.thickness * use_material.density * dt
    use_beam.weight = W

print(use_beam.weight)

plt.plot(x_plt, y_plt1)
plt.plot(x_plt, y_plt2)
plt.plot(x_plt, y_plt3)
plt.plot(x_plt, y_plt4)
plt.plot(x_plt, y_plt5)
plt.plot(x_plt, y_plt6)
plt.plot(x_plt, y_plt, '+b')
plt.show()
"""