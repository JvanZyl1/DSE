import numpy as np
from unused_files.python_scripts import MassEstimation as EM, PowerEstimation as PM
from unused_files.python_scripts.inputs import *

"""
Weight estimation and sizing of a 2-person UAM vehicle based on the Lilium Jet.
"""


def wing_sizing(MTOW):
    """
    This function sizes the wing and estimates its weight for a Lilium-type aircraft

    param    - MTOW: Maximum Take-Off Weight of the aircraft

    return   - Wwing: Weight of the aircraft wing
             - S:     Wing surface area
    """
    L = MTOW
    S_w = L / (CL * 0.5 * rho * V_cr * V_cr)
    print(S_w)
    b = np.sqrt(S_w) * np.sqrt(10)
    # c = np.sqrt(S_w) / np.sqrt(10)

    return S_w, b


def battery_sizing(MTOW):
    Pmax = PM.Power_DiskActuatorTheory(MTOW, N_prop, R_prop, duct=True)
    # Pmax = PM.PowerEstimationHover(R_prop, N_prop, MTOW)
    # Pmax = 187*10^3  # W
    Pcruise = 0.1 * Pmax  # Power for cruise

    # Energy needed for flight stages.
    Eto = (2 * Pcruise + 0.5 * Pmax) * ((10+20)/3600)  # Wh, take-off energy, including configuration transition
    Ecruise = Pcruise * (6/60)  # Wh, Ecruise also covers climb and descent, as these are double and half of the efficiency in cruise, so they cancel out.
    Eland = (0.5 * Pcruise + 0.5 * Pmax) * ((20+20)/3600)  # Wh, landing energy, including configuration transition.
    Eres = Pcruise * 5/V_cr + 2 * Pmax * 30/3600  # Wh, might be too much reserve power

    # Total energy needed
    Etot = (Eto + Ecruise + Eland + Eres)  # Wh

    # Needed battery weight
    W_bat = Etot / energy_density  # kg

    return W_bat, Pmax, Pcruise, Etot


def weight_estimation(MTOW, P_cruise, W_bat, W_wg):
    OEW = W_bat + W_wg + EM.PropGroupMassFun(N_prop, R_prop, B_prop, P_cruise)[0] + \
          EM.FuselageGroupMassFun(MTOW, W_PL, l_t, V_cr, D, l, S_nac, 1)[0]
    MTOW = W_PL + W_bat + OEW
    return MTOW

new_MTOW = W_MTOW
n_iter = 10
for i in range(n_iter):
    MTOW = new_MTOW
    S_w, b = wing_sizing(MTOW)
    W_bat, Pmax, P_cruise, Etot = battery_sizing(MTOW)
    W_e = EM.EngineMassFun(P_cruise)
    W_wg, Wts = EM.WingGroupMassFun(MTOW, W_PL, b, Lambda, S_w, t_chord, n_ult)
    new_MTOW = weight_estimation(MTOW, P_cruise, W_bat, W_wg)
MTOW = new_MTOW

print(MTOW/g)
