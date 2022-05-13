import numpy as np
from inputs import *
from PowerEstimation import *

def MOI_prop(R_prop, B_prop):
    M = (28 - 2.25) / 2 / 7 * (R_prop*2)    # From literature, https://aircommand.com/pages/rotor-blade-selection-and-planning#
    I = (1/3) * M * R_prop*R_prop * B_prop
    return I

def reaction_time(omega, R_prop, B_prop):  # Assuming EMRAX 268 motor
    t_react = abs(omega) * MOI_prop(R_prop,B_prop) / torque
    return t_react

def power_from_thrust(T, R_prop, N_prop=1):
    A = np.pi * R_prop**2 * N_prop
    P = (((T * V_TO) / 2) * (np.sqrt(1 + (2 * T) / (rho * V_TO ** 2 * A)))) / eta_final
    return P

def in_plane_rotors(R_cont, N_cont, F_gust=500):
    T_cont = F_gust / N_cont  # Thrust required per control propeller
    P_cont = power_from_thrust(T_cont, R_cont)  # Power required per control propeller
    omega = (omega_max - omega_prop) / (max_power - av_power) * P_cont  # Required angular velocity of control propeller
    t_react = reaction_time(omega, R_cont,B_cont)
    P_total = power_from_thrust(MTOW * g, R_prop) + P_cont * N_cont
    W_e = (P_cont / PowWtRat) / N_cont
    k_p = 0.124
    D_prop = 2 * R_cont
    P_hp = P_cont * 0.00134102 / N_cont  # Assumed take-off power per engine [hp], change later !!!
    W_blades = k_p * N_prop * (D_prop * P_hp * np.sqrt(B_cont)) ** 0.78174
    Mass = W_e + W_blades
    Ang_acc = omega / reaction_time(omega,R_cont, B_cont)
    Torque_req = Mass * R_cont**2 * Ang_acc
    chars = np.array([["PROP RADIUS = ", R_cont, "m"],
                      ["Control power: ", P_cont/1000, "kW"],
                      ["Total power: ", P_total/1000, "kW"],
                      ["Reaction time: ", t_react, "s"],
                      ["Torque required: ", Torque_req, "Nm"]])

    return P_cont, P_total, t_react, omega, chars


def pre_tilted(F_gust, theta_deg, MTOW):  # theta = tilt angle
    print("For F_gust = ", F_gust, " and theta = ", theta_deg)
    theta = theta_deg * np.pi/180
    T_cont = F_gust / np.sin(theta)  # N
    P_cont = power_from_thrust(T_cont, R_prop)  # Power during counteracting gust load
    T_TOL = MTOW * g / N_prop / np.cos(theta)
    P_TOL = power_from_thrust(T_TOL, R_prop)  # Power during normal hover by tilted motor
    P_increase = P_cont - P_TOL
    omega_change = (omega_max - omega_prop) / (max_power - av_power) * P_increase
    t_react = reaction_time(omega_change, R_prop,B_prop)
    T1 = MTOW * g / N_prop
    T2 = MTOW * g / N_prop / np.cos(theta)
    T2_z = T2*np.cos(theta)
    T3 = MTOW * g / N_prop
    T4 = MTOW * g / N_prop
    T5 = MTOW * g / N_prop / np.cos(theta)
    T5_z = T5*np.cos(theta)
    T6 = MTOW * g / N_prop
    d_tilt_to_bod = 0.4 + 0.5 + R_prop
    d_prop_to_bod = -0.2 + 0.5 + R_prop
    if P_increase > 0:
        T5 = T_cont
        T5_z = T5*np.cos(theta)
        T1 = (T5_z * d_tilt_to_bod / d_prop_to_bod) / 2
        T3 = T1; T4 = 0; T6 = 0
        if T5_z+T1+T3+T4+T6-MTOW*g < -0.05*MTOW*g:
            while T5_z+T1+T3+T4+T6-MTOW*g < -0.05*MTOW*g:
                T4 += 10
                T6 += 10
                T1 = (T5_z * d_tilt_to_bod / d_prop_to_bod + T4 + T6) / 2
                T3 = T1
    else:
        T2 -= F_gust / np.sin(theta)
        T2_z = T2*np.cos(theta)
        T1 += (F_gust / np.tan(theta) * d_tilt_to_bod / d_prop_to_bod) / 2
        T3 = T1

        if T5_z+T2_z+T1+T3+T4+T6-MTOW*g < -0.05*MTOW*g:
            while T5_z+T2_z+T1+T3+T4+T6-MTOW*g < -0.05*MTOW*g:
                T4 += 10
                T6 += 10
                T1 = (T5_z * d_tilt_to_bod / d_prop_to_bod + T4 + T6) / 2
                T3 = T1

    T_total = T1 + T3 + T4 + T5 + T6
    P_total = power_from_thrust(T_total, R_prop, N_prop)

    # CONSTRAINTS
    if T5_z+T2_z+T1+T3+T4+T6-MTOW*g > 0.1*MTOW*g:    # Too much lift to counteract gust
        print("Error: Total thrust exceeds thrust to hover")
        return
    if omega_change*60/(2*np.pi) > 3000:      # RPM too high for rotors for rotors
        print("Error: RPM increase of tilted motor too high")
        return
    print("T1 = ", T1, "T3 = ", T3, "T4 = ", T4, "T5 = ", T5, "T6 = ", T6, )
    return T_total, P_total, t_react, omega_change*60/(2*np.pi)


for F_gust in np.arange(100, 1100, 100):
    for theta in np.arange(15, 50, 5):
        print(pre_tilted(F_gust, theta, MTOW))

#for R_cont in np.arange(0.2, 0.9, 0.1):
#    print(in_plane_rotors(R_cont, 3)[3])

print(in_plane_rotors(R_cont, N_cont, F_gust=500)[4])
#
