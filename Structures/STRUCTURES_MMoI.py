"""STRUCTURES: Mass Moment of Inertia (MMoI)"""

import numpy as np

from math import *




#   Weights
W_rotors = np.array([50, 75, 75, 50])  # [kg]

#   Positions (Convention: X=nose, Y=right wing, Z=downward)
P_cg = np.array([0, 1, 2])

# Rotor         [X, Y, Z]
P_r = np.array([[1, 2, 3],  # [m]
                [4, 5, 6],  # [m]
                [7, 8, 9],  # [m]
                [10, 11, 12]  # [m]
                ])


# Beams
# Wings


# Relative Positions
def relative_pos(p_arr, p_cg):
    """
    This function calculates the position relative to the c.g.

    :param p_arr:   An array with the X, Y and Z positions of the given parts
    :param p_cg:    An array with the X, Y and Z position of the c.g.
    :return:        An array with the X, Y and Z positions of the given parts relative to the c.g.
    """
    i, j = np.shape(p_arr)
    for n in range(i):
        for m in range(j):
            p_arr[n, m] = (p_arr[n, m] - p_cg[m])
    return p_arr  # [m]


#   Inertia's due position
def inertia(p_arr, p_cg, w_arr):
    """
    This function calculates the Mass Moment of Inertia of given parts as a point mass
    :param p_arr: An array with the X, Y and Z positions of the given parts
    :param p_cg:  An array with the X, Y and Z position of the c.g.
    :param w_arr: An array with the weights of the given parts
    :return:      MMoI of the given parts
    """

    p_arr = relative_pos(p_arr, p_cg)
    i, j = np.shape(p_arr)
    i_mass = np.zeros(i)
    for n in range(i):
        i_mass[n] = w_arr[n] * (p_arr[n, 0] ** 2 + p_arr[n, 1] ** 2 + p_arr[n, 2] ** 2)
    return i_mass  # [kg m^2]


#   Inertia's due to shape

#   Inertia's individual rotor
def inertia_r(n_blades, r_rot, w_blade):
    """
    Calculates the MMoI of a rotor at the centre of this rotor

    :param n_blades: Amount of blades
    :param r_rot:    Radius of rotor
    :param w_blade:  Weight of a single blade
    :return: MMoI of a rotor
    """
    i_mass = n_blades * w_blade * (r_rot / 2) ** 2
    return i_mass  # [kg m^2]


#   Total MMoI
print(inertia(P_r, P_cg, W_rotors))
# print(relative_pos(P_r, P_cg))
