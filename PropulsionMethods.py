import numpy as np
from inputs import *
from PowerEstimation import *

def MOI_prop(R_prop):
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def reaction_time(omega, R_prop):  # Assuming EMRAX 268 motor
    t_react = omega * MOI_prop(R_prop) / torque
    return t_react

def prop_thrust(P_TOL, R_prop, N_prop):
    A = np.pi * R_prop**2
    T = (P_TOL/N_prop)**(2/3) * (2 * rho * A)
    return T

def power_from_thrust(T, R_prop, N_prop=1):
    A = np.pi * R_prop**2 * N_prop
    P = (((T * V_TO) / 2) * (np.sqrt(1 + (2 * T) / (rho * V_TO ** 2 * A)))) / eta_final
    return P


def in_plane_rotors(R_cont, N_cont, F_gust=1000):
    T_cont = F_gust / N_cont  # Thrust required per control propeller
    P_cont = power_from_thrust(T_cont, R_cont)  # Power required per control propeller
    omega = (omega_max - omega_prop) / (max_power - av_power) * P_cont  # Required angular velocity of control propeller
    t_react = reaction_time(omega, R_cont)

    P_total = power_from_thrust(MTOW * g, R_prop) + P_cont * N_cont

    chars = np.array([["PROP RADIUS = ", R_cont, "m"],
                      ["Control power: ", P_cont/1000, "kW"],
                      ["Total power: ", P_total/1000, "kW"],
                      ["Reaction time: ", t_react, "s"]])

    return P_cont, P_total, t_react, chars


def pretilted(F_gust=1000, theta=45):  # theta = tilt angle
    theta = theta * np.pi/180
    T_cont = F_gust / np.sin(theta)  # N
    P_cont = power_from_thrust(T_cont, R_prop)  # Power during counteracting gust load
    T_TOL = MTOW * g / N_prop / np.cos(theta)
    P_TOL = power_from_thrust(T_TOL, R_prop)  # Power during normal hover by tilted motor
    P_increase = P_cont - P_TOL
    omega_increase = (omega_max - omega_prop) / (max_power - av_power) * P_increase
    t_react = reaction_time(omega_increase, R_prop)
    d_tilt_to_bod = 0.4 + 0.5 + R_prop
    d_prop_to_bod = -0.2 + 0.5 + R_prop
    T1 = 0.25 * (F_gust / np.tan(theta) * (d_tilt_to_bod/d_prop_to_bod - 1) + MTOW * g)
    T2 = 0
    T3 = T1
    T4 = (MTOW * g - F_gust / np.tan(theta) - 2 * T1) / 2
    T5 = T_cont
    T6 = T4
    print(T1, T2, T3, T4, T5, T6)
    return P_increase, omega_increase, t_react


def tilt_rotors():
    # TODO: Add Jonny's function
    return

print(pretilted())

#for R_cont in np.arange(0.2, 0.9, 0.1):
#    print(in_plane_rotors(R_cont, 3)[3])

