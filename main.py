'''Conceptual Design of the Urban Air Vehicle'''
import numpy as np
from inputs import *
from PowerEstimation import PowerEstimatinonFun

print(PowerEstimatinonFun(R_prop, N_prop, V_cr, omega_prop, rho, g, M_MTOW))