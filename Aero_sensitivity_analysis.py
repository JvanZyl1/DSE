import csv
from inputs import *
from Parasitedrag_Estimation_Multirotor import *
import scipy.optimize as sc
from sympy.solvers import solve
from sympy import Symbol
import matplotlib.pyplot as plt

import DragEstimation as de


T_1= de.RC_AoAandThrust(V_cr, parasite_drag()[1], rho, MTOW, g)[1]/N_prop #Thrust per rotor
V_1 = 30 #Hovering
AoA_1 = de.RC_AoAandThrust(V_cr, parasite_drag()[1], rho, MTOW, g)[0] #AoA
delta_1 = 10*np.pi/180
S_flap_1 = 0.15 * 2 * R_prop # chord of the flap is assumed to be 15 cm and the width is assumed to be the diameter of the propeller
airfoilcsv_1 ='Xfoil-NACA0012.csv' #NACA0012 data
D_q_tot_x = parasite_drag()[1]


Config = VehicleConfig
Input = 'MTOW'
Input_val = MTOW

Output = 'AoA'
Output_val = de.RC_AoAandThrust(V_1, D_q_tot_x, rho, MTOW, g)

filename = str(Config) + '_' + Input + '_' + Output + '.txt'

with open(filename, 'a') as f:
    f.write(str(Input_val) + ' ' + str(Output_val) + '\n')

