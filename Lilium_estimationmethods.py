import numpy as np
import MassEstimation as EM
import PowerEstimation as PM

"""
Weight estimation and sizing of a 2-person UAM vehicle based on the Lilium Jet.
"""

rho = 1.225  # kg/m^3
g = 9.81  # m/s^2
#CLmax = 1.4  # ROUGH ESTIMATION
#CLopt = 0.52  # FROM DRAG POLAR IN LITERATURE
CL = 0.52
V_cr = 203 / 3.6  # m/s
N_prop = 24
n_ult = 2
D = 1.6  # m, diameter of fuselage
l = 3.5  # m, length of fuselage
R_prop = 0.10  # m
B_prop = 20  # nr of blades per propeller
RPM = 6000
S_nac = 11.6  # m^2, nacelle wetted area
l_t = l  # Rough estimation for Lilium configuration
energy_density = 170  # Wh/kg

Lambda = np.arctan(15 / 182)  # rad, from measurements of pixels in picture
t_chord = 0.14  # m, from measurements of pixels in picture


def wing_sizing(MTOW, n_ult):
    """
    This function sizes the wing and estimates its weight for a Lilium-type aircraft

    param    - MTOW: Maximum Take-Off Weight of the aircraft

    return   - Wwing: Weight of the aircraft wing
             - S:     Wing surface area
    """
    L = MTOW
    S_w = L / (CL * 0.5 * rho * V_cr * V_cr)
    b = np.sqrt(S_w) * np.sqrt(10)
    c = np.sqrt(S_w) / np.sqrt(10)

    return S_w, b


def battery_sizing(MTOW):
    # Pmax = PM.PowerEstimationFun(R_prop, N_prop, V_cr, RPM, rho, g, MTOW)
    Pmax = 170*10^3  # W
    Pcruise = 0.1 * Pmax  # Power for cruise

    # Energy needed for flight stages.
    Eto = (2 * Pcruise + 0.5 * Pmax) * ((10+20)/3600)  # Wh, take-off energy, including configuration transition
    Ecruise = Pcruise * (6/60)  # Wh, Ecruise also covers climb and descent, as these are double and half of the efficiency in cruise, so they cancel out.
    Eland = (0.5 * Pcruise + 0.5 * Pmax) * ((20+20)/3600)  # Wh, landing energy, including configuration transition.
    Eres = Pcruise * 5/V_cr + 2 * Pmax * 30/3600  # Wh, might be too much reserve power

    # Total energy needed
    Etot = (Eto + Ecruise + Eland + Eres)  # Wh

    # Needed battery weight
    W_bat = Etot / energy_density * g  # N

    return W_bat, Pmax, Pcruise, Etot


def weight_estimation(MTOW, P_cruise, W_bat, W_wg):
    OEW = W_bat + W_wg + EM.PropGroupMassFun(N_prop, R_prop, B_prop, P_cruise)[0] + \
          EM.FuselageGroupMassFun(MTOW, Wp, l_t, V_cr, D, l, S_nac, 1)[0]
    MTOW = Wp + W_bat + OEW
    return MTOW

########## First weight estimation ############
W_bat = 300 * g  # N
Wp = 250 * g  # N
OEW = (3174.6 - 771) * (3/5) * g  # N
new_MTOW = W_bat + Wp + OEW

print(new_MTOW/g)

n_iter = 5
for i in range(n_iter):
    MTOW = new_MTOW
    S_w, b = wing_sizing(MTOW, n_ult)
    W_bat, Pmax, P_cruise, Etot = battery_sizing(MTOW)
    W_e = EM.EngineMassFun(P_cruise)
    W_wg, Wts = EM.WingGroupMassFun(MTOW, Wp, b, Lambda, S_w, t_chord, n_ult)
    new_MTOW = weight_estimation(MTOW, P_cruise, W_bat, W_wg)
MTOW = new_MTOW

print(MTOW/g)
