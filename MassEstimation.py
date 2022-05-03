'''This scipt includes functions for weight estimation routines'''

import matplotlib.pyplot as plt
import numpy as np
from inputs import *
n_TO = 1.5 # ratio of P_cruise / P_takeoff.

def BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_cruise):
    t_CR = (R + R_div) * 1000 / (V_cr / 3.6)     # Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2                     # Calculate the time spent in vertical flight
    # Energy required for flight phases
    E_CR = t_CR * P_cruise
    E_TO = t_TO * P_cruise * n_TO
    E_total = (E_TO + E_CR) / 3600               # total energy needed in [Wh]
    M_bat = E_total / eta_E

    print('The mass of the battery in [kg]: ', M_bat)

    return M_bat

def PowerPlantWeightEstFun(P_cruise):
    W_pwp = 59.077 + P_cruise * 0.0004948372 # Weight of the powerplant in [kg]
    return W_pwp
    # using from  W = 130.243 + .369 HP_e

def DriveTrainWeightEstFun(W_MTOW):
    W_dt = -16.125 + W_MTOW * 0.045812829 # Weight of the drive train in [kg]
    return W_dt


A = 75 # [-] Rotor aspect ratio
S_disk = 80 #[m^2] Rotor disk area
b = 2* np.sqrt(S_disk/np.pi) # [m] Span width
c = b / A # [m] chord length
n_blades = 2 # [-] Number of blades
S_rot = n_blades* b/2 * c #[m^2] rotor planform length (assumed to be two blades)


def Est_rotor_mass(S_rot):
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    return (-194.685 + 12.164*S_rot_ft2)*0.4536