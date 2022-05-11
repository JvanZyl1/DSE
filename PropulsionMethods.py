import numpy as np
from inputs import *
from PowerEstimation import *

def MOI_prop():
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def reaction_time(omega):  # Assuming EMRAX 268 motor
    t_react = omega * MOI_prop() / torque
    return t_react

def MOI_vehicle():
    return

def prop_thrust(P_TOL, R_prop, N_prop):
    A = np.pi * R_prop**2
    T = (P_TOL/N_prop)**(2/3) * (2 * rho * A)
    return T

def power_from_thrust(T, R_prop):
    A = np.pi * R_prop**2
    P = T**(3/2) / np.sqrt(2*rho*A)
    return P


def in_plane_rotors():
    # TODO: Add dimensions, placement
    return


def pretilted(T_gust=1000, theta=40):  # theta = tilt angle
    # MOTOR PROPERTIES
    theta = theta * np.pi/180
    T_react = T_gust / np.sin(theta)  # N
    T_TOL = MTOW * g * 1.1 / np.cos(theta) / N_prop  # N
    P_react = power_from_thrust(T_react, R_prop)
    P_TOL = PowerReq(MTOW/np.cos(theta), N_prop, R_prop, V_cr)
    P_increase = P_react - P_TOL
    omega_increase = (omega_max - omega_prop) / (max_power - cont_power) * P_increase
    t_react = reaction_time(omega_increase)
    print(P_react, P_TOL, omega_increase*60/(np.pi*2), t_react)
    return P_increase, omega_increase


def tilt_rotors():

    return

print(prop_thrust(20000, 0.8, 8))

print(prop_thrust(60000, 0.8, 8))
print(pretilted())