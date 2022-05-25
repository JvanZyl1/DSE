import numpy as np
import math
import PowerEstimation as PE
from inputs import *

def BAT_weight():

    P_cruise    = PE.PowerEstimationFun(R_prop, N_prop, V_cr, omega_prop, rho, g, W_MTOW)
    P_hover     = PE.PowerEstimationHover(R_prop,N_prop, W_MTOW)
    P_TOextra = W_MTOW * g * 3
    P_TO = P_hover + P_TOextra


    t_cruise    = 25000 / (100 / 3.6)
    t_TO        = 100 / 3
    t_lan       = 100 / 2

    E_cruise = P_cruise * t_cruise
    E_TO = P_TO * t_TO
    E_lan = P_hover * t_lan
    E_reserve = E_cruise * 0.25
    E_total = E_cruise + E_TO + E_lan + E_reserve

    energy_density = 170  # Wh/kg

    BAT_weight = E_total / 3600 / energy_density

    print('Battery weight of:', BAT_weight, 'kg')

    return BAT_weight

