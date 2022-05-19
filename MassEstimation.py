
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
from PowerEstimation import *

### These estimation routines are for the multirotor configuration

def BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_TOL, P_cruise, P_cont, nu_discharge):
    '''
    This function estimates the battery mass in [kg]
    based off the energy density and mission profile
    '''
    eta_E = eta_E * 1.08**(yop-2022)
    t_CR = (R + R_div) / (V_cr)     # Calculate time in cruise + diversion
    t_TO = (h_TO / V_TO) * 2                     # Calculate the time spent in vertical flight
    t_cont = t_TO
    # Energy required for flight phases
    E_CR = t_CR * P_cruise
    E_TO = t_TO * P_TOL
    E_cont = t_cont * P_cont
    E_total = (E_TO + E_CR + E_cont) / 3600               # total energy needed in [Wh]
    W_bat = (E_total / eta_E) / nu_discharge
    Wts = np.array([["Battery Weight", W_bat]], dtype=object)
    return W_bat, Wts, E_total

### Mass estimation methods for wing-equipped aircraft
# Taken from Torenbeek chapter 8.

def StructureMassFun(n_ult, D, l, MTOW):
    '''
    This function estimates the mass of the structure as a whole
    based off the 'aircraft density' concept. Only used for preliminary OEW.
    '''
    W_s = MTOW * 0.447 * np.sqrt(n_ult) * (l * D**2 / MTOW)**0.24
    return W_s

def WingMassFun(W_MTOW, b, S_w, n_ult):
    '''
    This function returns the estimate for Wing mass in [kg]
    based off MTOW, wingspan 'b', half chord sweep 'Lambda',
    root chord thickness 't_chord' and ultimate load factor 'n_ult'
    '''
    # k_w = 4.9 * 10**(-3)
    # b_ref = 1.905
    # b_s = b / np.cos(Lambda) #structural span
    # W_frac = k_w * b_s**0.75 * (1 + np.sqrt(b_ref / b_s)) * n_ult**0.55 * ((b_s / t_chord)/(W_MTOW/S_w))**0.3
    # # t_chord - thickness of the chord at the root; n_ult - ultimate load factor.
    # W_w = W_frac * W_MTOW
    A = b**2 / S_w
    W_TO = W_MTOW * 2.20462
    S = S_w * 10.7639
    W_w = (0.04674 * (W_TO**0.397) * (S**0.360) * (n_ult**0.397) * (A**1.712)) * 0.453592
    return W_w

def FuselageMassFun(l_t, V_cr, D, l):     # l_t - distance between 1/4 chord points of wings and horizontal tailplane root
    '''
    This functinon estimates the fuselage weight based off
    its dimensions 'D', 'l', dive speed 'V_D', and tail length 'l_t'
    '''
    S_body = np.pi ** 2 * l * D / 4  # Assume fuselage to be an ellipse of revolution and calculate its wetted area
    k_wf = 0.23
    V_D = 2*V_cr / 3.6
    W_f = (k_wf * np.sqrt(V_D * (l_t/(D + D))) * S_body**1.2) * 0.453592
    return W_f

def VertTailPlaneMassFun(W_MTOW, S_v, A_v, Lambda_v, t_rv):           # weight estimation for the tailplanes
    '''
    This function estimates horizontal and vertical tailplane weight
    based off its size and ultimate load factor.
    '''
    W_TO = W_MTOW * 2.20462
    W_v = 0.453592 * (1.68 * (W_TO**0.567) * (S_v**1.249)*(A_v**0.482)) / \
          (639.95 * (t_rv**0.747) * (np.cos(Lambda_v)**0.882))
    return W_v

def HorTailPlaneMassFun(W_MTOW, S_h, A_h, t_rh):           # weight estimation for the tailplanes
    '''
    This function estimates horizontal and vertical tailplane weight
    based off its size and ultimate load factor.
    '''
    W_TO = W_MTOW * 2.20462
    W_h = 0.453592 * (3.184 * (W_TO**0.887) * (S_h**0.101)*(A_h**0.138)) / \
          (174.04 * (t_rh**0.223))
    return W_h

def EngineMassFun(P_TOL, N_prop):               # based off the perofrmance of the EMRAX electric motors
    '''
    This function estimates motor weight based off EMRAX motor Power/Weight rating of ~7 kw/kg.
    It returns the weight off a SINGLE motor !!!
    '''
    W_e = (P_TOL / PowWtRat) / N_prop
    return W_e

def BladeMassFun(N_prop, R_prop, B_prop, P_TOL):
    '''
    This function estimates the mass of propeller blades
    based off the cruise / take-off overall power and propeller configuration.
    Returns the weight of ALL the blades.
    '''
    k_p = 0.124
    D_prop = 2 * R_prop
    P_hp = P_TOL * 0.00134102 / N_prop      # Assumed take-off power per engine [hp], change later !!!
    W_blades = k_p * N_prop * (D_prop * P_hp * np.sqrt(B_prop))**0.78174
    return W_blades

def LandingGearMassFun(W_MTOW):
    '''
    This function estimates the FIXED landing gear weight for
    MAIN + NOSE gear config.
    '''
    k_uc = 1.0 # based off Table 8-6 from Torenbeek.
    A_m = 9.1; B_m = 0.082; C_m = 0.019
    A_n = 11.3; C_n = 0.0024   #Main and nose LG weight coefficients
    W_uc_m = k_uc * (A_m + B_m*W_MTOW**0.75 + C_m * W_MTOW)
    W_uc_n = k_uc * (A_n +  + C_n * W_MTOW)
    W_uc = W_uc_n + W_uc_m
    return W_uc

def SurfaceControlsMassFun(W_MTOW):
    '''
    This function gives the weight of surface control group.
    '''
    W_sc = 8 * (W_MTOW ** 0.2)
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

def CableMassFun(N_prop, R_prop, W_e):
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

def HydraulicsMassFun(W_MTOW, W_PL):
    '''
    This function estimates the weight of the hydraulics, pneumatics and
    sine electrical component based off the empty weight
    '''
    W_e = W_MTOW - W_PL
    W_hd = 0.00914 * (W_e ** 1.2)
    return W_hd

def FurnishingMassFun(W_PL):
    '''
    This function estimates the weight of the furnishing based off the payload and number
    of passengers.
    '''
    W_fur = 5.9 * (W_PL/125) + 2.3
    return W_fur

def AvionicsMassFun(W_MTOW):
    '''
    This function calculates the weight of hte instrumentation and avionics.
    '''
    W_av = 18.1 + 0.008 * W_MTOW
    return W_av

def PropGroupMassFun(N_prop, R_prop, B_prop, P_TOL):
    '''
    This function gives the weight of the whole propulsion group
    based off the motor and blade weight.
    '''
    W_e = EngineMassFun(P_TOL, N_prop)
    W_engs = W_e * N_prop
    W_bl = BladeMassFun(N_prop, R_prop, B_prop, P_TOL)
    W_cab = CableMassFun(N_prop, R_prop, W_e)
    W_pg = W_engs + W_bl + W_cab          # propulsion group is only cables, blades and motors :) NO NACELLE !a = np.array([["String",1,2]], dtype=object)
    Wts = np.array([["Blade Weight", W_bl], ["Engines Weight", W_engs], ["Cable Weight", W_cab]], dtype=object)
    return W_pg, Wts

def WingGroupMassFun(W_MTOW, W_PL, b, S_w, n_ult):
    '''
    This functions gives the weight of the wing group
    '''
    W_w = WingMassFun(W_MTOW, b, S_w, n_ult)
    W_hd = HydraulicsMassFun(W_MTOW, W_PL)
    W_sc = SurfaceControlsMassFun(W_MTOW)
    W_wg = W_w + W_hd + W_sc
    Wts = np.array([["Wing Structural Weight", W_w], ["Surface controls Weight", W_sc], ["Hydraulics Weight", W_hd]], dtype=object)
    return W_wg, Wts

def FuselageGroupMassFun(W_MTOW, W_PL, l_t, V_cr, D, l, S_nac, N_nac):
    '''
    This functions returns the weight of the fuselage group
    '''
    W_fs = FuselageMassFun(l_t, V_cr, D, l)
    W_fur = FurnishingMassFun(W_PL)
    W_lg = LandingGearMassFun(W_MTOW)
    W_nac = N_nac * NacelleMassFun(S_nac, V_cr)
    W_av = AvionicsMassFun(W_MTOW)
    W_fg = W_fs + W_fur + W_lg + W_nac + W_av
    Wts = np.array([["Fuselage Structural Weight", W_fs], ["Furnishing Weight", W_fur],
            ["Landing Gear Weight", W_lg], ["Nacelles Weight", W_nac], ["Avionics Weight", W_av]], dtype=object)
    return W_fg, Wts

def TailplaneGroupFun(W_MTOW, S_h, t_rh, t_rv, Lambda_v, A_v, A_h):
    '''
    This functions returns the weight of the tailplane group
    '''
    W_ht = HorTailPlaneMassFun(W_MTOW, S_h, A_h, t_rh)
    W_vt = VertTailPlaneMassFun(W_MTOW, S_v, A_v, Lambda_v, t_rv)
    W_tg = W_ht + W_vt
    Wts = np.array([["Vertical Tail Weight", W_vt], ["Horizontal Tail Weight", W_ht]], dtype = object)
    return W_tg, Wts

def control_group_mass(N_cont, R_cont, B_cont, P_cont):
    W_cb = BladeMassFun(N_cont, R_cont, B_cont, P_cont)
    W_cm = EngineMassFun(P_cont, N_cont)
    W_cg = W_cb + W_cm
    Wts = np.array([["Control propellers weight: ", W_cb], ["Control motor weight: ", W_cm]], dtype = object)
    return W_cg, Wts


def Est_rotor_mass(S_rot):
    S_rot_ft2 = S_rot/(0.3048**2) #[ft^2]
    return (-194.685 + 12.164*S_rot_ft2)*0.4536
