
'''This scipt includes functions for weight estimation routines'''

import matplotlib.pyplot as plt
import numpy as np
from inputs import *
n_TO = 1.5 # ratio of P_cruise / P_takeoff.

### These estimation routines are for the multirotor configuration

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


### Mass estimation methods for wing-equipped aircraft
# Taken from Torenbeek chapter 8.

def StructureMassFun(n_ult, D, l, W_MTOW):
    W_s = W_MTOW * 0.447 * np.sqrt(n_ult) * (l * D**2 / W_MTOW)**0.24
    return W_s

def WingMassFun(W_MTOW, b, Lambda, S_w, t_chord, n_ult):
    k_w = 4.9 * 10**(-3)
    b_ref = 1.905
    b_s = b / np.cos(Lambda) #structural span
    W_frac = k_w * b_s**0.75 * (1 + np.sqrt(b_ref / b_s)) * n_ult**0.55 * ((b_s / t_chord)/(W_MTOW/S_w))**0.3
    # t_chord - thickness of the chord at the root; n_ult - ultimate load factor.
    return W_frac

def FuselageMassFun(l_t, V_cr, S_body):     # l_t - distance between 1/4 chord points of wings and horizontal tailplane root
    k_wf = 0.23
    V_D = 2*V_cr / 3.6
    W_f = k_wf * np.sqrt(V_D * (l_t/(D + D))) * S_body**1.2
    return W_f

def TailPlaneMassFun(S_t, n_ult):           # weight estimation for the tailplanes
    k_wt = 0.64
    W_tail = k_wt * (n_ult * S_t**2)**0.75
    return W_tail

def EngineMassFun(P_cruise):               # based off the perofrmance of the EMRAX electric motors
    return W_e = (P_cruise / PowWtRat) / N_prop

def PropGroupMassFun(N_prop, P_to, W_e):
    W_pg =  N_prop * (1.5 * W_e)      # extra 50% accounting for cabling. NACELLES NOT INCLUDED !
    return W_pg
