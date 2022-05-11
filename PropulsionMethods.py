import numpy as np
from inputs import *

def MOI_prop():
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def reaction_time():  # Assuming EMRAX 268 motor
    t_react = omega_prop * MOI_prop() / torque
    return t_react

def MOI_vehicle():
    return

def prop_thrust(P_TOL, R_prop):
    A = np.pi * R_prop**2
    T = P_TOL**(2/3) * (2 * rho * A)
    return T


def in_plane_rotors():
    # TODO: Add dimensions, placement
    return


def pretilted(P_TOL, tilt_angle=20):
    tilt_angle = tilt_angle * np.pi/180
    T_prop = prop_thrust(P_TOL, R_prop) / np.cos(tilt_angle)
    T_control = np.sin(tilt_angle) * T_prop
    return T_control


def tilt_rotors():

    return


print(reaction_time())
