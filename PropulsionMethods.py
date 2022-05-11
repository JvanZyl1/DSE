import numpy as np

def MOI_prop(R_prop, B_prop):
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    print(M)
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def MOI_vehicle():
    return

def in_plane_rotors():
    # TODO: Add dimensions, placement
    return


def pretilted(P_TOL, tilt_angle):
    sideforce = np.sin(tilt_angle) * P_TOL
    P_TOL = P_TOL / np.cos(tilt_angle)
    return


def tilt_rotors():

    return


print(MOI(0.8, 2))
