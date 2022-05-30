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
    L = load.L * SF
    n = part.n
    E = material.E_modulus
    P = load.P * SF
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

    def radii(Vx, Vy, Mx, My):

        # Bending in lift-direction for TENSION
        def r1():
            r1 = (P + sqrt(abs(((P) ** 2) + 4 * 2 * pi * t * sigma_y * 2 * pi * Mx))) / (4 * pi * t * sigma_y)
            return r1

        # Bending in lift-direction for COMPRESSION
        def r2():
            if part.name == "beam":
                r2 = (abs(Mx * (l*2) ** 2) / (t * pi ** 2 * E)) ** (1 / 4)
            elif part.name == "gear":
                r2 = (P * l ** 2 / (2 * pi ** 3 * t)) ** 3
            return r2

        # Bending in axial-direction for TENSION
        def r3():
            r3 = (abs(My) + sqrt((My) ** 2 + 4 * 2 * pi * t * sigma_y * 2 * pi * P)) / (4 * pi * t * sigma_y)
            return r3

        # Bending in axial-direction for COMPRESSION
        def r4():
            r4 = (abs(My * (l*2) ** 2) / (t * pi ** 2 * E)) ** (1 / 4)
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

    def deflection_y(pos_z, radius, Mx, Ly):
        v = 1 / (E * part.thickness * radius **3) * (Mx / -2 * pos_z ** 2 + Ly / 6 * pos_z ** 3 - W / (24 * L) * pos_z ** 4)
        return v

    r = np.zeros((6, np.size(z)))
    r_max = np.zeros(np.size(z))
    defl = 0
    W = 0

    for j in range(np.size(z)):
        for i in range(6):
            r[i, j] = radii(v_x(z[j]), v_y(z[j]), m_x(z[j]), m_y(z[j]))[i]
            r_max[j] = np.max(r[:, j])
        if j < np.size(z)-1:
            defl += deflection_y(z[j+1], r_max[j], m_x(z[j+1]), v_y(z[j+1])) - deflection_y(z[j], r_max[j], m_x(z[j]), v_y(z[j]))
            W += 2 * pi * r_max[j] * t * use_material.density * dz
    return z, r, r_max, defl, W

for iteration in range(10):
    z_axis, r, r_design, defl, W = radii(use_beam, use_loadcase, use_material)
    use_beam.weight = W

for i in range(6):
    plt.plot(z_axis, r[i])
plt.plot(z_axis, r_design, '-.b')
plt.title("Radius required")
plt.xlabel("z [m]")
plt.ylabel("r [m]")
plt.show()

print(defl, use_beam.weight)




