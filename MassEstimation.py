
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
#For rotorcrafts
def PowerPlantWeightEstFun(P_cruise):
    W_pwp = 59.077 + P_cruise * 0.0004948372 # Weight of the powerplant in [kg]
    return W_pwp
    # using from  W = 130.243 + .369 HP_e
#For rotorcrafts
def DriveTrainWeightEstFun(W_MTOW):
    W_dt = -16.125 + W_MTOW * 0.045812829 # Weight of the drive train in [kg]
    return W_dt
#For rotorcrafts
def Est_rotor_mass(S_rot):
    '''Input rotor planform area'''
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    M_rot_sys = (-194.685 + 12.164*S_rot_ft2)*0.4536 # [kg] Helicopter rotor mass estimation
    return M_rot_sys
#For rotorcrafts
def BodyMass(S_body):
    '''Input body surface area'''
    S_body_ft2 = S_body/(0.3048**2) #[ft^2]
    M_body = (-269.023 + 2.356 * S_body_ft2)*0.4536 # [kg] Estimation relation
    return M_body
