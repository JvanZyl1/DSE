"""
DSE: Structures
Beam Loading and Stresses
"""

from math import *
from inputs import *
import numpy as np
from matplotlib import pyplot as plt


class Wing:
    Weight = 500  # N
    b = 5  # m (span)
    c = 0.7  # m
    S = b * c  # m**2
    t = 1e-3  # m
    B = 0.001  # m**2 boom cross-sectional area
    Cl = 0.5
    Cd = 0.1
    file = "C:/Users/mitch/PycharmProjects/DSE/DSE GIT/structures/airfoil.dat"
    airfoil = np.genfromtxt(file, float, skip_header=1)


def Inertia(airfoil, boom_area):
    Ixx = np.sum(airfoil[:, 1] ** 2) * boom_area
    Iyy = np.sum(airfoil[:, 0] ** 2) * boom_area
    Ixy = np.sum(airfoil[:, 0] * airfoil[:, 1]) * boom_area
    return Ixx, Iyy, Ixy

Ixx, Iyy, Ixy = Inertia(Wing.airfoil, Wing.B)


class Engines:
    weight_total = 0
    lift_total = 0
    count = 0

    def __init__(self, weight, max_lift, rpos_z):
        self.weight = weight
        self.rpos_z = rpos_z  # Relative position on wing
        self.max_lift = max_lift
        Engines.weight_total += weight
        Engines.lift_total += max_lift
        Engines.count += 1


def V_wing(rho_air, lift_coef, max_V, S_wing, W_wing, W_engines, L_engines):
    L = 0.5 * lift_coef * rho_air * max_V ** 2 * S_wing
    Ax = W_wing - L + W_engines - L_engines


# Engines
engine1 = Engines(2000, 5000, 0.2)
engine2 = Engines(1000, 2500, 0.6)
engine3 = Engines(1000, 2500, 0.9)

dz = 0.01
z = np.arange(0, Wing.b + dz, dz)

def V_step(z, force, r_position, wingspan):
    Vz = np.where(z < r_position*wingspan, 0, force)
    return Vz

def V_span(z, force, wingspan):
    Vz = np.ones(np.size(z)) * force / wingspan
    return Vz

# Internal Load
Lift = 0.5 * Wing.Cl rho * Wing.S * (V_cr*1.2)^2

"""
V = []
V_L_Wing = V_span(z, Lift, Wing.b)
V_W_Wing = -V_span(z, Wing.Weight, Wing.b)
V_W_Engine1 = V_step(z, engine1.weight, engine1.rpos_z, Wing.b)
V_W_Engine2 = V_step(z, engine2.weight, engine2.rpos_z, Wing.b)
V_W_Engine3 = V_step(z, engine3.weight, engine3.rpos_z, Wing.b)
V_L_Engine1 = V_step(z, engine1.max_lift, engine1.rpos_z, Wing.b)
V_L_Engine2 = V_step(z, engine2.max_lift, engine2.rpos_z, Wing.b)
V_L_Engine3 = V_step(z, engine3.max_lift, engine3.rpos_z, Wing.b)
V.append(V_L_Wing), V.append(V_W_Wing), V.append(V_W_Engine1), V.append(V_L_Engine1)
V.append(V_W_Engine2), V.append(V_L_Engine2), V.append(V_W_Engine3), V.append(V_L_Engine3)
"""

#V1 = V_step(z, engine1.weight, engine1.rpos_z, Wing.b)
#V2 = V_span(z, 1000, 2)


# Plot
plt.plot(z, V2)
plt.show()