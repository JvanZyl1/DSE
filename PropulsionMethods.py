import numpy as np
from inputs import *
from PowerEstimation import *

def MOI_prop():
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def reaction_time(omega):  # Assuming EMRAX 268 motor
    t_cont = omega * MOI_prop() / torque
    return t_cont

def prop_thrust(P_TOL, R_prop, N_prop):
    A = np.pi * R_prop**2
    T = (P_TOL/N_prop)**(2/3) * (2 * rho * A)
    return T

def power_from_thrust(T, R_prop):
    A = np.pi * R_prop**2
    P = (((T * V_TO) / 2) * (np.sqrt(1 + (2 * T) / (rho * V_TO ** 2 * A)))) / eta_final
    return P


def in_plane_rotors():
    R_cont = R_prop/2

    return


def pretilted(F_gust=1000, theta=30):  # theta = tilt angle
    # MOTOR PROPERTIES
    theta = theta * np.pi/180
    T_cont = F_gust / np.sin(theta)  # N
    P_cont = power_from_thrust(T_cont, R_prop)  # Power during counteracting gust load
    T_TOL = MTOW * g / N_prop / np.cos(theta)
    P_TOL = power_from_thrust(T_TOL, R_prop)  # Power during normal hover by tilted motor
    P_increase = P_cont - P_TOL
    omega_increase = (omega_max - omega_prop) / (max_power - av_power) * P_increase
    t_react = reaction_time(omega_increase)
    print(P_cont, P_TOL, omega_increase*60/(np.pi*2), t_react)
    print(F_gust/np.tan(theta))
    return P_increase, omega_increase, t_react


def tilt_rotors():
    # TODO: Add Jonny's function
    return

print(pretilted())

