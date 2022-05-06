
'''
This scipt includes functions for weight estimation routines
Estimates the following component weights:

Battery Weight:         * Inputs: R, R_div, V_cr, V_TO, h_TO, eta_E, P_cruise

Propulsion Group:       * Inputs: P_cruise, N_prop, B_prop, R_prop,
* Blade weight
* Motor weight
* Cable weight

Wing group:             * Inputs: W_MTOW, W_Pl, b, Lambda, S, t_chord, n_ult
* Hydraulics
* Wing structure weight
* Surface control

Fuselage group           * Inputs: W_MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac
* Fuselage structural mass
* Furnishing
* Nacelle
* Landing gear
* Avionics

Tailplane group          * Inputs: S_h, S_v, n_ult
* Horizontal tailplane
* Vertical tailplane
'''

import matplotlib.pyplot as plt
import numpy as np
from inputs import *
from DragEstimation import *
from PowerEstimation import *

def TOL_cr_wing(V_cr, rho, S, C_L, P_TOL):
    C_D = DragPolar(C_L)
    T = 0.5 * C_D * rho * V_cr**2 * S
    P_cruise = T * V_cr
    print(P_cruise)
    print(P_TOL)
    n_TO = P_TOL / P_cruise
    print(n_TO)
    return n_TO

### These estimation routines are for the multirotor configuration

def BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, rho, S, C_L):
    '''
    This function estimates the battery mass in [kg]
    based off the energy denisty and mission profile
    '''
    t_CR = (R + R_div) / V_cr     # Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2                     # Calculate the time spent in vertical flight
    # Energy required for flight phases
    E_CR = t_CR * P_cruise
    E_TO = t_TO * P_TOL
    E_total = (E_TO + E_CR) / 3600               # total energy needed in [Wh]
    W_bat = E_total / eta_E
    Wts = np.array([["Battery Weight", W_bat]], dtype=object)
    return W_bat, Wts

### Mass estimation methods for wing-equipped aircraft
# Taken from Torenbeek chapter 8.

def StructureMassFun(n_ult, D, l, MTOW):
    '''
    This function estimates the mass of the structure as a whole
    based off the 'aircraft density' concept. Only used for preliminary OEW.
    '''
    W_s = MTOW * 0.447 * np.sqrt(n_ult) * (l * D**2 / MTOW)**0.24
    return W_s

def WingMassFun(MTOW, b, Lambda, S_w, t_chord, n_ult):
    '''
    This function returns the estimate for Wing mass in [kg]
    based off MTOW, wingspan 'b', half chord sweep 'Lambda',
    root chord thickness 't_chord' and ultimate load factor 'n_ult'
    '''
    k_w = 4.9 * 10**(-3)
    b_ref = 1.905
    b_s = b / np.cos(Lambda) #structural span
    W_frac = k_w * b_s**0.75 * (1 + np.sqrt(b_ref / b_s)) * n_ult**0.55 * ((b_s / t_chord)/(MTOW/S_w))**0.3
    # t_chord - thickness of the chord at the root; n_ult - ultimate load factor.
    W_w = W_frac * MTOW
    return W_w

def FuselageMassFun(l_t, V_cr, D, l):     # l_t - distance between 1/4 chord points of wings and horizontal tailplane root
    '''
    This functinon estimates the fuselage weight based off
    its dimensions 'D', 'l', dive speed 'V_D', and tail length 'l_t'
    '''
    S_body = np.pi ** 2 * l * D / 4  # Assume fuselage to be an ellipse of revolution and calculate its wetted area
    k_wf = 0.23
    V_D = 2*V_cr / 3.6
    W_f = k_wf * np.sqrt(V_D * (l_t/(D + D))) * S_body**1.2
    return W_f

def TailPlaneMassFun(S_t, n_ult):           # weight estimation for the tailplanes
    '''
    This function estimates horizontal and vertical tailplane weight
    based off its size and ultimate load factor.
    '''
    k_wt = 0.64
    W_tail = k_wt * (n_ult * S_t**2)**0.75
    return W_tail

def EngineMassFun(P_cruise):               # based off the perofrmance of the EMRAX electric motors
    '''
    This function estimates motor weight based off EMRAX motor Power/Weight rating of ~7 kw/kg.
    It returns the weight off a SINGLE motor !!!
    '''
    W_e = (P_cruise / PowWtRat) / N_prop
    return W_e

def BladeMassFun(N_prop, R_prop, B_prop, P_TOL):
    '''
    This function estimates the mass of propeller blades
    based off the cruise / take-off overall power and propeller configuration.
    Returns the weight of ALL the blades.
    '''
    k_p = 0.124
    D_prop = 2 * R_prop
    P_to = P_TOL * 0.00134102 / N_prop      # Assumed take-off power per engine [hp], change later !!!
    W_blades = k_p * N_prop * (D_prop * P_to * np.sqrt(B_prop))**0.78174
    return W_blades

def LandingGearMassFun(MTOW):
    '''
    This function estimates the FIXED landing gear weight for
    MAIN + NOSE gear config.
    '''
    k_uc = 1.0 # based off Table 8-6 from Torenbeek.
    A_m = 9.1; B_m = 0.082; C_m = 0.019
    A_n = 11.3; C_n = 0.0024   #Main and nose LG weight coefficients
    W_uc_m = k_uc * (A_m + B_m*MTOW**0.75 + C_m * MTOW)
    W_uc_n = k_uc * (A_n +  + C_n * MTOW)
    W_uc = W_uc_n + W_uc_m
    return W_uc

def SurfaceControlsMassFun(MTOW):
    '''
    This function gives the weight of surface control group.
    '''
    W_sc = 8 * (MTOW ** 0.2)
    return W_sc

def NacelleMassFun(S_nac, V_cr):
    '''
    This function is used to estimate the weight of nacelles, struts, etc.
    It takes design dive speed and wetted surface area as inputs.
    Designed for one nacelle
    '''
    V_D = 2*V_cr / 3.6      # S_nac - total area of nacelle wetted by the airflow externally and internally.
                            # Also works for pylons, struts etc.
    W_nac = 0.405 * np.sqrt(V_D) * (S_nac ** 1.3)
    return W_nac

def CableMassFun(N_prop, W_e):
    '''
    This function estimate the cable length based off the values found in the NASA report:
    https://ntrs.nasa.gov/api/citations/20200000289/downloads/20200000289.pdf?attachment=true
    It is developed adhoc and takes into account the weight off the engine, as that is relevant for the motor power.
    We take a reference engine and assume it needs R_prop + 2 m of cables from battery to engine (2m for the beam).
    '''
    rho_c = 0.25     # [kg/m]
    W_e_ref = 10    # [kg]
    l_cab = R_prop + 2      # m
    W_cable = ( W_e / W_e_ref * (l_cab * 2) ) * N_prop
    return W_cable

def HydraulicsMassFun(MTOW, W_PL):
    '''
    This function estimates the weight of the hydraulics, pneumatics and
    sine electrical component based off the empty weight
    '''
    W_e = MTOW - W_PL
    W_hd = 0.00914 * (W_e ** 1.2)
    return W_hd

def FurnishingMassFun(W_PL):
    '''
    This function estimates the weight of the furnishing based off the payload and number
    of passengers.
    '''
    W_fur = 5.9 * (W_PL/125) + 2.3
    return W_fur

def AvionicsMassFun(MTOW):
    '''
    This function calculates the weight of hte instrumentation and avionics.
    '''
    W_av = 18.1 + 0.008 * MTOW
    return W_av

def PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL):
    '''
    This function gives the weight of the whole propulsion group
    based off the motor and blade weight.
    '''
    W_e = EngineMassFun(P_cruise)
    W_engs = W_e * N_prop
    W_bl = BladeMassFun(N_prop, R_prop, B_prop, P_TOL)
    W_cab = CableMassFun(N_prop, W_e)
    W_pg = W_engs + W_bl + W_cab          # propulsion group is only cables, blades and motors :) NO NACELLE !a = np.array([["String",1,2]], dtype=object)
    Wts = np.array([["Blade Weight", W_bl], ["Engines Weight", W_engs], ["Cable Weight", W_cab]], dtype=object)
    return W_pg, Wts

def WingGroupMassFun(MTOW, W_PL, b, Lambda, S, t_chord, n_ult):
    '''
    This functions gives the weight of the wing group
    '''
    W_w = WingMassFun(MTOW, b, Lambda, S, t_chord, n_ult)
    W_hd = HydraulicsMassFun(MTOW, W_PL)
    W_sc = SurfaceControlsMassFun(MTOW)
    W_wg = W_w + W_hd + W_sc
    Wts = np.array([["Wing Structural Weight", W_w], ["Surface controls Weight", W_sc], ["Hydraulics Weight", W_hd]], dtype=object)
    return W_wg, Wts

def FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac):
    '''
    This functions returns the weight of the fuselage group
    '''
    W_fs = FuselageMassFun(l_t, V_cr, D, l)
    W_fur = FurnishingMassFun(W_PL)
    W_lg = LandingGearMassFun(MTOW)
    W_nac = N_nac * NacelleMassFun(S_nac, V_cr)
    W_av = AvionicsMassFun(MTOW)
    W_fg = W_fs + W_fur + W_lg + W_nac + W_av
    Wts = np.array([["Fuselage Structural Weight", W_fs], ["Furnishing Weight", W_fur], \
            ["Landing Gear Weight", W_lg], ["Nacelles Weight", W_nac], ["Avionics Weight", W_av]], dtype=object)
    return W_fg, Wts

def TailplaneGroupFun(S_h, S_v, n_ult):
    '''
    This functions returns the weight of the tailplane group
    '''
    W_ht = TailPlaneMassFun(S_h, n_ult)
    W_vt = TailPlaneMassFun(S_v, n_ult)
    W_tg = W_ht + W_vt
    Wts = np.array([["Vertical Tail Weight", W_vt], ["Horizontal Tail Weight", W_ht]], dtype = object)
    return W_tg, Wts

