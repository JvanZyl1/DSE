import numpy as np
from inputs import *
from MassEstimation import *
from main import P_hov

W_bat = BatteryMassFun(R, R_div, V_cr, V_TO, h_TO, eta_E, P_hov, P_cruise, nu_discharge)
W_s = StructureMassFun(n_ult, D, l, MTOW)